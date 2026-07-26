/* Aanwijzen (tap / point): een woord verschijnt in stukken (lettergrepen of
   letters); tik het JUISTE stuk — de sílaba tónica, de letter met de tilde …
   Content: tap.items:[{parts:[...], answer:index|[indices], tag, sub}].
   answer = index (0-based) van het juiste stuk, of een array van indices. */
window.MotorTemplates = window.MotorTemplates || {};
window.MotorTemplates.tap = {
  init(api){
    const cfg = api.config, el = api.el;
    const conf = cfg.tap || {};
    const pool = (conf.items || []).slice();
    const rounds = (cfg.options && cfg.options.rounds) || pool.length;
    api.setTarget(Math.min(rounds, pool.length) || pool.length);
    const joiner = conf.joiner != null ? conf.joiner : "·";

    const root = api.root; root.innerHTML = "";
    const card = el("div","tp-card");
    card.innerHTML =
      '<div class="tp-eye">'+esc(conf.prompt||"Tik het juiste deel")+'</div>'+
      '<div class="tp-word" id="tpWord"></div>'+
      '<div class="tp-sub" id="tpSub">&nbsp;</div>'+
      '<div class="tp-fb" id="tpFb">&nbsp;</div>';
    root.appendChild(card);

    const wordEl = card.querySelector("#tpWord");
    const subEl  = card.querySelector("#tpSub");
    const fbEl   = card.querySelector("#tpFb");

    let queue = shuffle(pool.slice()).slice(0, rounds);
    let idx = 0, cur = null, locked = false, chips = [];

    function answers(){ return Array.isArray(cur.answer)?cur.answer:[cur.answer]; }

    function load(){
      if(idx >= queue.length){ api.finish(); return; }
      cur = queue[idx]; locked = false;
      wordEl.innerHTML = ""; chips = [];
      fbEl.textContent = " "; fbEl.className = "tp-fb"; card.classList.remove("good","bad");
      const parts = cur.parts || [];
      parts.forEach((p,i)=>{
        const c = el("button","tp-chip", esc(p)); c.type="button"; c.dataset.i = i;
        c.addEventListener("click",()=>choose(i,c));
        wordEl.appendChild(c);
        if(i < parts.length-1){ const sp = el("span","tp-join", esc(joiner)); wordEl.appendChild(sp); }
        chips.push(c);
      });
      subEl.innerHTML = (cfg.options && cfg.options.hint===false) ? "&nbsp;" : (cur.sub ? esc(cur.sub) : "&nbsp;");
    }
    function choose(i,c){
      if(locked) return; locked = true;
      const ans = answers();
      const ok = ans.indexOf(i) >= 0;
      const correctTxt = ans.map(a=>cur.parts[a]).join(" / ");
      api.judge(ok,{tag:cur.tag||"_", stimulus:(cur.parts||[]).join(joiner), chosen:cur.parts[i], correct:[correctTxt], sub:cur.sub});
      idx++; api.tick();
      if(ok){
        c.classList.add("hit"); card.classList.add("good");
        fbEl.textContent = "¡correcto!"; fbEl.className = "tp-fb g";
        setTimeout(load, api.calm?200:460);
      }else{
        c.classList.add("miss"); card.classList.add("bad");
        ans.forEach(a=>{ if(chips[a]) chips[a].classList.add("reveal"); });
        fbEl.innerHTML = "→ "+esc(correctTxt); fbEl.className = "tp-fb b";
        setTimeout(load, api.calm?450:1000);
      }
    }

    function onKey(e){
      if(e.key>="1" && e.key<="9"){ const i=+e.key-1; if(i<chips.length){ e.preventDefault(); if(!locked) choose(i, chips[i]); } }
    }
    document.addEventListener("keydown", onKey);
    api._cleanup = ()=>document.removeEventListener("keydown", onKey);

    load();

    function esc(s){ return String(s).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])); }
    function shuffle(a){ for(let i=a.length-1;i>0;i--){const j=(Math.random()*(i+1))|0;[a[i],a[j]]=[a[j],a[i]];} return a; }
  }
};
