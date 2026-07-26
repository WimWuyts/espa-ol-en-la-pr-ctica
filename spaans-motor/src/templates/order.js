/* Volgorde (order / sequence): een reeks tegels staat door elkaar; tik ze in
   de juiste volgorde (klein→groot, alfabetisch, chronologisch …). Elke tegel
   heeft een `key` die de juiste volgorde bepaalt (oplopend). Content:
   order.rounds:[{prompt?, tag, sub?, items:[{label,key}]}].
   Judge één keer per ronde: juist = de hele ronde zonder misklik gelegd. */
window.MotorTemplates = window.MotorTemplates || {};
window.MotorTemplates.order = {
  init(api){
    const cfg = api.config, el = api.el;
    const conf = cfg.order || {};
    const rounds = shuffle((conf.rounds || []).slice());
    api.setTarget(rounds.length);

    const root = api.root; root.innerHTML = "";
    const card = el("div","or-card");
    card.innerHTML =
      '<div class="or-eye" id="orEye"></div>'+
      '<div class="or-slots" id="orSlots"></div>'+
      '<div class="or-bank" id="orBank"></div>'+
      '<div class="or-fb" id="orFb">&nbsp;</div>';
    root.appendChild(card);

    const eyeEl = card.querySelector("#orEye");
    const slotsEl = card.querySelector("#orSlots");
    const bankEl = card.querySelector("#orBank");
    const fbEl = card.querySelector("#orFb");

    let ri = 0, round = null, sorted = [], nextPos = 0, mistakes = 0, locked = false;

    function loadRound(){
      if(ri >= rounds.length){ api.finish(); return; }
      round = rounds[ri];
      sorted = (round.items||[]).slice().sort((a,b)=>a.key-b.key);
      nextPos = 0; mistakes = 0; locked = false;
      eyeEl.textContent = round.prompt || conf.prompt || "Tik in de juiste volgorde";
      fbEl.textContent = " "; fbEl.className = "or-fb"; card.classList.remove("bad");
      slotsEl.innerHTML = ""; bankEl.innerHTML = "";
      sorted.forEach((_,i)=>{ const s = el("div","or-slot"); s.innerHTML = '<span class="or-n">'+(i+1)+'</span>'; s.dataset.pos = i; slotsEl.appendChild(s); });
      shuffle(round.items.slice()).forEach(it=>{
        const b = el("button","or-chip", esc(it.label)); b.type="button";
        b.dataset.key = it.key;
        b.addEventListener("click",()=>tap(it,b));
        bankEl.appendChild(b);
      });
    }
    function tap(it,b){
      if(locked || b.classList.contains("used")) return;
      const expected = sorted[nextPos];
      if(it.key === expected.key){
        b.classList.add("used");
        const slot = slotsEl.querySelector('.or-slot[data-pos="'+nextPos+'"]');
        slot.classList.add("filled");
        slot.insertAdjacentHTML("beforeend",'<span class="or-lab">'+esc(it.label)+'</span>');
        api.sfx.move();
        nextPos++;
        if(nextPos >= sorted.length) finishRound();
      }else{
        mistakes++;
        b.classList.remove("shake"); void b.offsetWidth; b.classList.add("shake");
        api.sfx.bad();
        fbEl.innerHTML = "→ eerst: <b>"+esc(expected.label)+"</b>"; fbEl.className = "or-fb b";
      }
    }
    function finishRound(){
      locked = true;
      const ok = mistakes === 0;
      api.judge(ok,{tag:round.tag||"orden", stimulus:sorted.map(x=>x.label).join(" · "),
        chosen: ok?"":"("+mistakes+" fout)", correct:[sorted.map(x=>x.label).join(" · ")], sub:round.sub});
      if(ok){ fbEl.textContent = "¡perfecto!"; fbEl.className = "or-fb g"; api.sfx.ok(); }
      else { card.classList.add("bad"); }
      ri++; api.tick();
      setTimeout(loadRound, api.calm?300:800);
    }

    loadRound();

    function esc(s){ return String(s).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])); }
    function shuffle(a){ for(let i=a.length-1;i>0;i--){const j=(Math.random()*(i+1))|0;[a[i],a[j]]=[a[j],a[i]];} return a; }
  }
};
