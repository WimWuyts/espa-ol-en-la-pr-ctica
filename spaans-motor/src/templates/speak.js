/* Spreken / opname (speak): een communicatieve SPREEK-taak. De leerling
   luistert naar een model (Web Speech TTS), zegt na, NEEMT ZICHZELF OP
   (MediaRecorder, volledig offline), luistert terug en herneemt. Na elke
   opname een korte zelfevaluatie (☹/😐/☺) — deelname telt, een opname is
   nooit strikt goed/fout. Realiseert het productieve/interactieve uiteinde
   van de vaardighedenladder (§14) mét échte stemopname.

   Modi via cfg.speak.mode:
   - "repeat"       : luister → zeg na → neem op → herbeluister → herneem.
   - "shadowing"    : idem, met afbouwende fasen (tekst → sleutelwoorden → geen tekst → eigen versie).
   - "substitution" : één modelzin met wisselende bouwstenen (carrusel).
   - "voicemessage" : ontvanger·situatie·doel + verplichte bouwstenen → één spraakbericht.

   Content (cfg.speak):
     mode, prompt?, phases?(shadowing), frame?(substitution),
     items:[ … ] (velden verschillen per modus, zie schema.md ).

   Robuust: als de micro niet beschikbaar is (of geweigerd) blijft de TTS +
   een ☑-bevestiging werken (print/offline-fallback). Nooit crashen; streams
   worden opgeruimd in api._cleanup. */
window.MotorTemplates = window.MotorTemplates || {};
window.MotorTemplates.speak = {
  init(api){
    const cfg = api.config, el = api.el;
    const conf = cfg.speak || {};
    const mode = conf.mode || "repeat";
    const items = (conf.items || []).slice();
    api.setTarget(items.length);

    const DEF_PHASES = ["Texto completo","Palabras clave","Sin texto","Tu versión"];
    const phases = (conf.phases && conf.phases.length ? conf.phases : DEF_PHASES);

    /* ---- schil ---- */
    const root = api.root; root.innerHTML = "";
    const card = el("div","sp-card");
    card.innerHTML =
      '<div class="sp-eye" id="spEye"></div>'+
      '<div class="sp-count" id="spCount"></div>'+
      '<div class="sp-stage" id="spStage"></div>'+
      '<div class="sp-controls" id="spCtl">'+
        '<button class="sp-btn listen" id="spListen" type="button">▶ Escuchar</button>'+
        '<button class="sp-btn rec" id="spRec" type="button">⏺ Grabar</button>'+
        '<button class="sp-btn play" id="spPlay" type="button" disabled>▶ Mi grabación</button>'+
        '<button class="sp-btn ghost" id="spAgain" type="button" disabled>↻ Otra vez</button>'+
      '</div>'+
      '<div class="sp-timer" id="spTimer">&nbsp;</div>'+
      '<audio class="sp-audio" id="spAudio" controls hidden></audio>'+
      '<div class="sp-note" id="spNote"></div>'+
      '<div class="sp-assess" id="spAssess">'+
        '<div class="sp-alabel">¿Cómo ha ido? · <span class="nl">hoe ging het?</span></div>'+
        '<div class="sp-moods">'+
          '<button class="sp-mood" data-m="0" type="button" title="cuesta un poco">☹</button>'+
          '<button class="sp-mood" data-m="1" type="button" title="más o menos">😐</button>'+
          '<button class="sp-mood" data-m="2" type="button" title="¡bien!">☺</button>'+
        '</div>'+
      '</div>';
    root.appendChild(card);

    const eyeEl   = card.querySelector("#spEye");
    const countEl = card.querySelector("#spCount");
    const stageEl = card.querySelector("#spStage");
    const bListen = card.querySelector("#spListen");
    const bRec    = card.querySelector("#spRec");
    const bPlay   = card.querySelector("#spPlay");
    const bAgain  = card.querySelector("#spAgain");
    const timerEl = card.querySelector("#spTimer");
    const audioEl = card.querySelector("#spAudio");
    const noteEl  = card.querySelector("#spNote");
    const moods   = card.querySelectorAll(".sp-mood");

    eyeEl.textContent = conf.prompt || "Escucha · repite · grábate";

    /* ---- media-staat ---- */
    const mediaOK = !!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia && typeof MediaRecorder !== "undefined");
    let stream=null, rec=null, chunks=[], blobUrl=null, recording=false, hasRec=false, timerId=null, t0=0, micDead=!mediaOK;

    async function ensureStream(){
      if(stream) return stream;
      stream = await navigator.mediaDevices.getUserMedia({audio:true});
      return stream;
    }
    function fmt(ms){ const s=Math.floor(ms/1000); return (s<10?"0":"")+s+"s"; }
    function stopTimer(){ if(timerId){ clearInterval(timerId); timerId=null; } }
    function stopRecording(){
      if(rec && recording){ try{ rec.stop(); }catch(e){} }
      recording=false; stopTimer();
      bRec.classList.remove("on"); bRec.textContent="⏺ Grabar";
    }

    async function startRecording(){
      if(!mediaOK){ micFallback(); return; }
      try{ await ensureStream(); }
      catch(e){ micFallback(); return; }
      chunks=[]; hasRec=false;
      try{ rec = new MediaRecorder(stream); }
      catch(e){ micFallback(); return; }
      rec.ondataavailable = ev => { if(ev.data && ev.data.size) chunks.push(ev.data); };
      rec.onstop = () => {
        if(blobUrl){ URL.revokeObjectURL(blobUrl); blobUrl=null; }
        if(chunks.length){
          const blob = new Blob(chunks, {type: chunks[0].type || "audio/webm"});
          blobUrl = URL.createObjectURL(blob);
          audioEl.src = blobUrl; audioEl.hidden=false;
          bPlay.disabled=false; bAgain.disabled=false; hasRec=true;
          note("¡Grabado! Escúchate y compara con el modelo. <span class='nl'>opgenomen — luister terug en vergelijk.</span>", "ok");
        }
      };
      rec.start(); recording=true; t0=Date.now();
      bRec.classList.add("on"); bRec.textContent="⏹ Parar";
      timerEl.textContent="● grabando… 00s";
      stopTimer();
      timerId=setInterval(()=>{ timerEl.textContent="● grabando… "+fmt(Date.now()-t0); }, 250);
      note("Habla ahora. Pulsa ⏹ Parar cuando termines. <span class='nl'>spreek nu; klik ⏹ om te stoppen.</span>", "");
    }

    bRec.addEventListener("click", ()=>{
      if(recording){ stopRecording(); timerEl.innerHTML="&nbsp;"; }
      else { startRecording(); }
    });
    bPlay.addEventListener("click", ()=>{
      if(blobUrl){ audioEl.currentTime=0; audioEl.play().catch(()=>{}); }
    });
    bAgain.addEventListener("click", ()=>{ resetRec(); note("Otra vez: escucha el modelo y grábate de nuevo. <span class='nl'>opnieuw opnemen.</span>",""); });

    function micFallback(){
      micDead=true;
      recording=false; stopTimer(); timerEl.innerHTML="&nbsp;";
      bRec.classList.remove("on"); bRec.textContent="⏺ Grabar";
      note("🎙️ Micrófono no disponible — usa Chrome/Edge y permite el micrófono. "+
           "<span class='nl'>Geen micro? Beluister het model en oefen hardop, y confirma abajo.</span>", "warn");
      /* fallback-knop: hardop geoefend zonder opname */
      if(!noteEl.querySelector(".sp-confirm")){
        const b = el("button","sp-confirm","☑ Lo he practicado en voz alta");
        b.type="button";
        b.addEventListener("click", ()=>{ b.classList.add("done"); b.textContent="☑ ¡hecho!"; hasRec=true; api.sfx.move(); });
        noteEl.appendChild(b);
      }
    }
    function note(html, kind){
      noteEl.className = "sp-note" + (kind?(" "+kind):"");
      noteEl.innerHTML = html || "";
    }
    function resetRec(){
      stopRecording();
      if(blobUrl){ URL.revokeObjectURL(blobUrl); blobUrl=null; }
      audioEl.pause(); audioEl.removeAttribute("src"); audioEl.hidden=true;
      bPlay.disabled=true; bAgain.disabled=true; hasRec=false;
      timerEl.innerHTML="&nbsp;";
      const c=card.querySelector(".sp-confirm"); if(c) c.remove();
    }

    /* ---- TTS ---- */
    function speak(text){
      if(!("speechSynthesis" in window) || !text){
        note("🔊 Lee el modelo en voz alta. <span class='nl'>geen TTS in deze browser — lees hardop.</span>","");
        return;
      }
      try{
        speechSynthesis.cancel();
        const u = new SpeechSynthesisUtterance(text);
        u.lang="es-ES"; u.rate=0.95;
        speechSynthesis.speak(u);
      }catch(e){}
    }

    /* ---- huidig item ---- */
    let idx=0, item=null, phase=0;

    function speakText(){
      if(mode==="substitution") return composed(item);
      if(mode==="voicemessage") return item.model || "";
      return item.text || "";
    }
    function composed(it){
      const fr = conf.frame || "{}";
      const fills = (it.fills||[]).slice();
      let i=0;
      return fr.replace(/___|\{\}/g, ()=> (i<fills.length ? fills[i++] : "…"));
    }

    /* ---- stage per modus ---- */
    function renderStage(){
      stageEl.className="sp-stage m-"+mode;
      if(mode==="repeat"){
        stageEl.innerHTML =
          (item.cue?'<div class="sp-cue">'+esc(item.cue)+'</div>':'')+
          '<div class="sp-target">'+esc(item.text)+'</div>'+
          (item.sub?'<div class="sp-sub">'+esc(item.sub)+'</div>':'');
        bListen.style.display="";
      } else if(mode==="shadowing"){
        stageEl.innerHTML =
          '<div class="sp-phases" id="spPhases"></div>'+
          '<div class="sp-target" id="spShadow"></div>'+
          (item.sub?'<div class="sp-sub">'+esc(item.sub)+'</div>':'');
        const ph = stageEl.querySelector("#spPhases");
        phases.forEach((p,i)=>{
          const b=el("button","sp-phase"+(i===phase?" on":""), esc(p)); b.type="button";
          b.addEventListener("click",()=>{ phase=i; paintPhases(); renderShadow(); });
          ph.appendChild(b);
        });
        renderShadow();
        bListen.style.display="";
      } else if(mode==="substitution"){
        stageEl.innerHTML =
          '<div class="sp-cue">'+esc(conf.frameLabel||"Modelo")+'</div>'+
          '<div class="sp-target">'+frameHtml(item)+'</div>'+
          (item.sub?'<div class="sp-sub">'+esc(item.sub)+'</div>':'');
        bListen.style.display="";
      } else if(mode==="voicemessage"){
        const blocks = (item.blocks||[]).map(b=>'<li>'+esc(b)+'</li>').join("");
        stageEl.innerHTML =
          '<div class="sp-ficha">'+
            '<div class="sp-frow"><span class="sp-fk">Para</span><span class="sp-fv">'+esc(item.to||"")+'</span></div>'+
            '<div class="sp-frow"><span class="sp-fk">Situación</span><span class="sp-fv">'+esc(item.situation||"")+'</span></div>'+
            '<div class="sp-frow"><span class="sp-fk">Objetivo</span><span class="sp-fv">'+esc(item.goal||"")+'</span></div>'+
          '</div>'+
          (blocks?'<div class="sp-need"><span class="sp-needlbl">Incluye:</span><ul>'+blocks+'</ul></div>':'')+
          (item.sub?'<div class="sp-sub">'+esc(item.sub)+'</div>':'');
        bListen.style.display = item.model ? "" : "none";
      } else {
        stageEl.innerHTML='<div class="sp-target">'+esc(item.text||"")+'</div>';
        bListen.style.display="";
      }
    }
    function paintPhases(){
      stageEl.querySelectorAll(".sp-phase").forEach((b,i)=>b.classList.toggle("on",i===phase));
    }
    function renderShadow(){
      const t = stageEl.querySelector("#spShadow"); if(!t) return;
      const words = String(item.text||"").split(/\s+/);
      if(phase===0){ t.innerHTML = esc(item.text); }
      else if(phase===1){
        const keys = (item.keywords && item.keywords.length)
          ? item.keywords
          : words.filter(w=>w.replace(/[.,¡!¿?]/g,"").length>4);
        t.innerHTML = '<span class="sp-keys">'+keys.map(esc).join(" · ")+'</span>';
      }
      else if(phase===2){ t.innerHTML = '<span class="sp-hidden">'+words.map(()=>"•").join(" ")+'</span>'; }
      else { t.innerHTML = '<span class="sp-own">Di tu propia versión →</span>'; }
    }
    function frameHtml(it){
      const fr = conf.frame || "{}";
      const fills = (it.fills||[]).slice();
      let i=0, out="";
      const parts = fr.split(/___|\{\}/);
      parts.forEach((p,j)=>{
        out += esc(p);
        if(j < parts.length-1){
          const f = i<fills.length ? fills[i++] : "…";
          out += '<span class="sp-slot">'+esc(f)+'</span>';
        }
      });
      return out;
    }

    /* ---- laden / vooruit ---- */
    function load(){
      if(idx >= items.length){ api.finish(); return; }
      item = items[idx]; phase=0;
      countEl.textContent = (idx+1)+" / "+items.length;
      resetRec();
      moods.forEach(b=>b.classList.remove("picked"));
      renderStage();
      if(micDead){ micFallback(); }
      else { note("Escucha ▶, repite y luego grábate ⏺. <span class='nl'>luister, zeg na, neem jezelf op.</span>",""); }
    }
    bListen.addEventListener("click", ()=>{ speak(speakText()); });

    moods.forEach(b=>{
      b.addEventListener("click", ()=>{
        moods.forEach(x=>x.classList.remove("picked"));
        b.classList.add("picked");
        const m = +b.dataset.m;
        // reflectie-tip afhankelijk van zelfscore
        const tip = m>=2
          ? (item.tip || "¡Bien! Grábalo otra vez más rápido y sin mirar. <span class='nl'>nog eens, sneller en zonder te kijken.</span>")
          : "Escucha el modelo de nuevo, fíjate en el ritmo y vuelve a grabarte. <span class='nl'>beluister het model opnieuw, let op ritme, en herneem.</span>";
        note(tip, m>=2?"ok":"");
        api.judge(true, {tag:item.tag || mode, stimulus:speakText() || item.goal || item.to || "opname"});
        api.tick();
        setTimeout(()=>{ idx++; load(); }, api.calm?250:700);
      });
    });

    /* ---- opruimen ---- */
    api._cleanup = function(){
      stopRecording();
      stopTimer();
      if(stream){ try{ stream.getTracks().forEach(t=>t.stop()); }catch(e){} stream=null; }
      if(blobUrl){ URL.revokeObjectURL(blobUrl); blobUrl=null; }
      try{ audioEl.pause(); }catch(e){}
      if("speechSynthesis" in window){ try{ speechSynthesis.cancel(); }catch(e){} }
    };

    // micDead → load() toont automatisch de vriendelijke melding + fallback-knop
    load();

    function esc(s){ return String(s).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])); }
  }
};
