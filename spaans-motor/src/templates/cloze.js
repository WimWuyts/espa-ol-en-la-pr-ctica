/* Invullen (cloze / meerkeuze): lees de zin of het woord met een gat en tik
   de juiste optie. Elk item heeft ZIJN EIGEN opties (anders dan classify, waar
   de categorieën vast zijn). Dekt: ¿lleva tilde?, b/v, h muda, ge/gi/gue,
   welke schrijfwijze is juist … Content levert cloze.items:[{stimulus,options,answer,tag,sub}].
   answer = de juiste optiestring (of array als er meer juist zijn). */
window.MotorTemplates = window.MotorTemplates || {};
window.MotorTemplates.cloze = {
  init(api){
    const cfg = api.config, el = api.el, shade = api.shade;
    const conf = cfg.cloze || {};
    const pool = (conf.items || []).slice();
    const rounds = (cfg.options && cfg.options.rounds) || pool.length;
    api.setTarget(Math.min(rounds, pool.length) || pool.length);

    const root = api.root; root.innerHTML = "";
    const card = el("div","cz-card");
    card.innerHTML =
      '<div class="cz-eye">'+esc(conf.prompt||"Kies het juiste")+'</div>'+
      '<div class="cz-stim" id="czStim">…</div>'+
      '<div class="cz-sub" id="czSub">&nbsp;</div>'+
      '<div class="cz-fb" id="czFb">&nbsp;</div>';
    root.appendChild(card);
    const opts = el("div","cz-opts"); root.appendChild(opts);

    const stimEl = card.querySelector("#czStim");
    const subEl  = card.querySelector("#czSub");
    const fbEl   = card.querySelector("#czFb");

    let queue = shuffle(pool.slice()).slice(0, rounds);
    let idx = 0, cur = null, locked = false, btns = [];

    function load(){
      if(idx >= queue.length){ api.finish(); return; }
      cur = queue[idx]; locked = false;
      opts.innerHTML = ""; btns = [];
      fbEl.textContent = " "; fbEl.className = "cz-fb";
      card.classList.remove("good","bad");
      stimEl.innerHTML = fmt(cur.stimulus);
      subEl.innerHTML  = (cfg.options && cfg.options.hint===false) ? "&nbsp;" : (cur.sub ? esc(cur.sub) : "&nbsp;");
      const choices = shuffle((cur.options||[]).slice());
      const palette = ["#2E8E68","#3D74D6","#8B5E9E","#E0A22F","#C4402C"];
      choices.forEach((opt,i)=>{
        const b = el("button","cz-opt");
        b.type = "button";
        const col = palette[i % palette.length];
        b.style.setProperty("--oc", col);
        b.innerHTML = fmt(opt)+(i<9?'<small>'+(i+1)+'</small>':'');
        b.addEventListener("click",()=>choose(opt,b));
        opts.appendChild(b);
        btns.push({el:b, opt});
      });
    }
    function answers(){ return Array.isArray(cur.answer)?cur.answer:[cur.answer]; }
    function choose(opt,b){
      if(locked) return; locked = true;
      const ans = answers();
      const ok = ans.indexOf(opt) >= 0;
      api.judge(ok,{tag:cur.tag||"_", stimulus:strip(cur.stimulus), chosen:opt, correct:ans, sub:cur.sub});
      idx++; api.tick();
      if(ok){
        b.classList.add("hit"); card.classList.add("good");
        fbEl.textContent = "¡correcto!"; fbEl.className = "cz-fb g";
        setTimeout(load, api.calm?200:460);
      }else{
        b.classList.add("miss"); card.classList.add("bad");
        btns.forEach(x=>{ if(ans.indexOf(x.opt)>=0) x.el.classList.add("reveal"); });
        fbEl.innerHTML = "→ "+fmt(ans.join(" / ")); fbEl.className = "cz-fb b";
        setTimeout(load, api.calm?450:1000);
      }
    }

    function onKey(e){
      if(e.key>="1" && e.key<="9"){ const i=+e.key-1; if(i<btns.length){ e.preventDefault(); if(!locked) choose(btns[i].opt, btns[i].el); } }
    }
    document.addEventListener("keydown", onKey);
    api._cleanup = ()=>document.removeEventListener("keydown", onKey);

    load();

    /* ___ wordt een gat-streep; **x** wordt gemarkeerd (accentletter) */
    function fmt(s){
      return esc(String(s))
        .replace(/___+/g, '<span class="cz-gap"></span>')
        .replace(/\*\*(.+?)\*\*/g, '<b class="cz-mark">$1</b>');
    }
    function strip(s){ return String(s).replace(/\*\*/g,"").replace(/___+/g,"___"); }
    function esc(s){ return String(s).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])); }
    function shuffle(a){ for(let i=a.length-1;i>0;i--){const j=(Math.random()*(i+1))|0;[a[i],a[j]]=[a[j],a[i]];} return a; }
  }
};
