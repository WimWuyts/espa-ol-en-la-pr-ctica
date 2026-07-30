/* Typen (type): PRODUCTIEVE laag. De leerling TYPT het antwoord i.p.v. te
   kiezen/klikken. Dekt V3·V4·G4·G5·G6 uit de grid (escribe-la-palabra,
   gentilicio, concordancia-typen, verbo-cloze-libre, transforma, número en
   letras, reconstruye la frase, build-a-sentence).

   Twee modi (cfg.type.mode):
   - "closed" (default, P-gesloten/goud): één of enkele juiste oplossingen →
     auto-check via normalisatie (spaties/hoofdletters/leestekens-tolerant en
     — tenzij accentSensitive — accent-tolerant, mét behoud van ñ).
   - "open" (P-halfopen): vrijere productie (mini-zin) → STRUCTUURcheck
     (bevat elk verplicht element uit `must`?) + «onthul modelo» ter
     zelfcorrectie. Geen valse belofte van perfecte correctie.

   Content (cfg.type):
     prompt?, mode?, accentSensitive?(false), items:[{
        stimulus,            // de opgave (mag ___ gat en **markering** bevatten)
        answer|answers,      // closed: string of array aanvaarde antwoorden
        must,                // open: array verplichte tokens (structuurcheck)
        model,               // open: modeloplossing om te onthullen
        hint,                // optionele letterhint (bv. "e_ p____")
        tag, sub             // categorie + korte toelichting
     }]

   Iteratie identiek aan cloze: geschudde pool, `options.rounds` rondes. */
window.MotorTemplates = window.MotorTemplates || {};
window.MotorTemplates.type = {
  init(api){
    const cfg = api.config, el = api.el;
    const conf = cfg.type || {};
    const mode = conf.mode === "open" ? "open" : "closed";
    const accentSensitive = !!conf.accentSensitive;
    const pool = (conf.items || []).slice();
    /* Series: `options.series` rondes van `options.rounds` items.
       Elke ronde trekt VERSE items zolang de pool het toelaat; is de pool op,
       dan wordt hij opnieuw geschud (herhaling = retrieval, geen bug). */
    const perRound = (cfg.options && cfg.options.rounds) || pool.length;
    const series = Math.max(1, (cfg.options && cfg.options.series) || 1);
    const total = Math.min(perRound * series, Math.max(perRound, pool.length * series));
    api.setTarget(total);

    const root = api.root; root.innerHTML = "";
    const card = el("div","ty-card");
    card.innerHTML =
      '<div class="ty-eye">'+esc(conf.prompt || (mode==="open"?"Escribe una frase":"Escribe la respuesta"))+'</div>'+
      '<div class="ty-stim" id="tyStim">…</div>'+
      '<div class="ty-sub" id="tySub">&nbsp;</div>'+
      '<div class="ty-hint" id="tyHint"></div>'+
      '<div class="ty-inrow">'+
        '<input class="ty-in" id="tyIn" type="text" autocomplete="off" autocapitalize="off" '+
          'autocorrect="off" spellcheck="false" inputmode="text" '+
          'aria-label="Typ je antwoord" placeholder="escribe aquí…">'+
        '<button class="ty-go" id="tyGo" type="button">✓</button>'+
      '</div>'+
      '<div class="ty-acc" id="tyAcc" aria-hidden="true"></div>'+
      '<div class="ty-fb" id="tyFb">&nbsp;</div>'+
      '<div class="ty-extra" id="tyExtra"></div>';
    root.appendChild(card);

    const stimEl = card.querySelector("#tyStim");
    const subEl  = card.querySelector("#tySub");
    const hintEl = card.querySelector("#tyHint");
    const inEl   = card.querySelector("#tyIn");
    const goEl   = card.querySelector("#tyGo");
    const accEl  = card.querySelector("#tyAcc");
    const fbEl   = card.querySelector("#tyFb");
    const extraEl= card.querySelector("#tyExtra");

    /* accentknoppen: snel á é í ó ú ñ ü ¿ ¡ invoegen (mobiel/AZERTY-vriendelijk) */
    const ACCENTS = ["á","é","í","ó","ú","ñ","ü","¿","¡"];
    ACCENTS.forEach(ch=>{
      const b = el("button","ty-accbtn", ch); b.type="button"; b.tabIndex=-1;
      b.addEventListener("click",()=>{ insertAtCursor(inEl, ch); inEl.focus(); });
      accEl.appendChild(b);
    });

    /* bouw de volledige wachtrij: per ronde verse items, pool herschudden als hij op is */
    let queue = [], rest = shuffle(pool.slice());
    for(let s = 0; s < series; s++){
      for(let i = 0; i < perRound; i++){
        if(!rest.length) rest = shuffle(pool.slice());
        queue.push(rest.shift());
      }
    }
    const roundOf = i => Math.floor(i / perRound) + 1;   // 1-based rondenummer

    let idx = 0, cur = null, locked = false, shownRound = 1;

    function load(){
      if(idx >= queue.length){ api.finish(); return; }
      /* nieuwe ronde begonnen? → kort tussenscherm */
      if(series > 1 && roundOf(idx) !== shownRound && idx % perRound === 0){
        shownRound = roundOf(idx);
        showBreak(shownRound);
        return;
      }
      cur = queue[idx]; locked = false;
      card.classList.remove("good","bad");
      stimEl.innerHTML = fmt(cur.stimulus);
      subEl.innerHTML  = cur.sub ? esc(cur.sub) : "&nbsp;";
      const showHint = cur.hint && !(cfg.options && cfg.options.hint===false);
      hintEl.innerHTML = showHint ? '<span class="ty-hk">pista</span> '+fmt(cur.hint) : "";
      hintEl.style.display = showHint ? "" : "none";
      fbEl.textContent = " "; fbEl.className = "ty-fb";
      extraEl.innerHTML = ""; extraEl.className = "ty-extra";
      inEl.value = ""; inEl.disabled = false; goEl.disabled = false;
      inEl.classList.remove("ok","no");
      inEl.focus();
    }

    /* ---- normalisatie & vergelijking ---- */
    function norm(s){
      s = String(s).toLowerCase().trim().replace(/\s+/g," ");
      s = s.replace(/[.,;:!¡¿?"'«»…]/g,"").trim();
      if(!accentSensitive){
        // strip klemtoon-accenten op klinkers, maar BEHOUD ñ (año ≠ ano)
        s = s.replace(/á/g,"a").replace(/é/g,"e").replace(/í/g,"i")
             .replace(/ó/g,"o").replace(/ú/g,"u").replace(/ü/g,"u");
      }
      return s;
    }
    function accepted(){
      let a = cur.answers || cur.answer || cur.model || "";
      if(!Array.isArray(a)) a = [a];
      return a.filter(x=>x!=null && String(x).length);
    }
    function isCorrectClosed(val){
      const n = norm(val);
      if(!n) return false;
      return accepted().some(a => norm(a) === n);
    }
    function missingTokens(val){
      const n = " "+norm(val)+" ";
      return (cur.must || []).filter(tok => n.indexOf(" "+norm(tok)+" ") < 0 && n.indexOf(norm(tok)) < 0);
    }

    function submit(){
      if(locked) return;
      const val = inEl.value;
      if(!val.trim()){ inEl.focus(); return; }
      locked = true; inEl.disabled = true; goEl.disabled = true;
      idx++; api.tick();
      if(mode === "closed"){
        const ok = isCorrectClosed(val);
        api.judge(ok,{tag:cur.tag||"_", stimulus:strip(cur.stimulus), chosen:val, correct:accepted(), sub:cur.sub});
        if(ok){
          card.classList.add("good"); inEl.classList.add("ok");
          fbEl.textContent = "¡correcto!"; fbEl.className = "ty-fb g";
          next(api.calm?260:620);
        }else{
          card.classList.add("bad"); inEl.classList.add("no");
          fbEl.innerHTML = "→ <b>"+esc(accepted()[0])+"</b>"+
            (accepted().length>1 ? ' <span class="ty-alt">('+esc(accepted().slice(1).join(" / "))+')</span>' : "");
          fbEl.className = "ty-fb b";
          next(api.calm?700:1500);
        }
      } else {
        // open: structuurcheck + onthul modelo
        const miss = missingTokens(val);
        const structOk = miss.length === 0;
        api.judge(structOk,{tag:cur.tag||"_", stimulus:strip(cur.stimulus), chosen:val,
          correct:(cur.must||[]).length?["incluye: "+(cur.must||[]).join(" + ")]:[cur.model||""], sub:cur.sub});
        if(structOk){
          card.classList.add("good"); inEl.classList.add("ok");
          fbEl.textContent = "¡bien construido!"; fbEl.className = "ty-fb g";
        }else{
          card.classList.add("bad"); inEl.classList.add("no");
          fbEl.innerHTML = 'Falta: <b>'+esc(miss.join(", "))+'</b> <span class="nl">(nog opnemen)</span>';
          fbEl.className = "ty-fb b";
        }
        // modeloplossing onthullen ter zelfcorrectie
        if(cur.model){
          const rev = el("button","ty-reveal","👁 Ver modelo"); rev.type="button";
          rev.addEventListener("click",()=>{
            rev.outerHTML = '<div class="ty-model"><span class="ty-mk">modelo</span> '+esc(cur.model)+'</div>';
          });
          extraEl.appendChild(rev);
        }
        const cont = el("button","ty-cont", idx>=queue.length ? "Ver resultado →" : "Siguiente →"); cont.type="button";
        cont.addEventListener("click",()=>{ next(0); });
        extraEl.appendChild(cont);
      }
    }
    function next(delay){ setTimeout(load, delay); }

    /* tussenscherm tussen twee rondes: even ademen, dan door */
    function showBreak(n){
      stimEl.innerHTML = '<span class="ty-round">Ronda '+n+' / '+series+'</span>';
      subEl.innerHTML = "&nbsp;"; hintEl.style.display="none";
      fbEl.textContent = " "; fbEl.className="ty-fb";
      inEl.value=""; inEl.disabled=true; goEl.disabled=true;
      inEl.classList.remove("ok","no");
      extraEl.innerHTML="";
      const b = el("button","ty-cont","Empezar ronda "+n+" →"); b.type="button";
      b.addEventListener("click", ()=>{ shownRound = n; extraEl.innerHTML=""; load(); });
      extraEl.appendChild(b);
      b.focus();
    }

    goEl.addEventListener("click", submit);
    function onKey(e){
      if(e.key === "Enter"){
        e.preventDefault();
        if(locked){ // in open-modus met continue-knop: Enter = door
          const c = extraEl.querySelector(".ty-cont"); if(c) c.click();
        } else submit();
      }
    }
    inEl.addEventListener("keydown", onKey);
    api._cleanup = ()=>{ inEl.removeEventListener("keydown", onKey); };

    load();

    /* ---- helpers ---- */
    function insertAtCursor(input, text){
      const s = input.selectionStart|0, e = input.selectionEnd|0, v = input.value;
      input.value = v.slice(0,s) + text + v.slice(e);
      const p = s + text.length; input.setSelectionRange(p,p);
    }
    function fmt(s){
      return esc(String(s))
        .replace(/___+/g, '<span class="ty-gap"></span>')
        .replace(/\*\*(.+?)\*\*/g, '<b class="ty-mark">$1</b>');
    }
    function strip(s){ return String(s).replace(/\*\*/g,"").replace(/___+/g,"___"); }
    function esc(s){ return String(s).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])); }
    function shuffle(a){ for(let i=a.length-1;i>0;i--){const j=(Math.random()*(i+1))|0;[a[i],a[j]]=[a[j],a[i]];} return a; }
  }
};
