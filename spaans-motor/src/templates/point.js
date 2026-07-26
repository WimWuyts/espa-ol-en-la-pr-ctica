/* Aanwijzen (point / locate): een prompt + een set doelen (tegels). Tik het/de
   juiste doel(en). Dekt: foutenjacht (klik het foute woord), señala (klik het
   land/woord dat past), zoek-de-uitzondering. Content:
   point.rounds:[{prompt?, tag, sub?, mode:"one"|"all", targets:[{label, hit:true}]}].
   - mode "one" (default): precies één doel is juist; één tik beslist de ronde.
   - mode "all": tik ALLE juiste doelen (en géén afleider); ronde eindigt als alle
     juiste geraakt zijn of bij een misklik. Eén judge per ronde. */
window.MotorTemplates = window.MotorTemplates || {};
window.MotorTemplates.point = {
  init(api){
    const cfg = api.config, el = api.el;
    const conf = cfg.point || {};
    const rounds = shuffle((conf.rounds || []).slice());
    api.setTarget(rounds.length);

    const root = api.root; root.innerHTML = "";
    const card = el("div","pt-card");
    card.innerHTML =
      '<div class="pt-eye" id="ptEye"></div>'+
      '<div class="pt-sub" id="ptSub">&nbsp;</div>'+
      '<div class="pt-grid" id="ptGrid"></div>'+
      '<div class="pt-fb" id="ptFb">&nbsp;</div>';
    root.appendChild(card);

    const eyeEl = card.querySelector("#ptEye");
    const subEl = card.querySelector("#ptSub");
    const gridEl = card.querySelector("#ptGrid");
    const fbEl = card.querySelector("#ptFb");

    let ri = 0, round = null, mode = "one", needed = 0, hitCount = 0, locked = false;

    function load(){
      if(ri >= rounds.length){ api.finish(); return; }
      round = rounds[ri];
      mode = round.mode || conf.mode || "one";
      const targets = shuffle((round.targets||[]).slice());
      needed = targets.filter(t=>t.hit).length;
      hitCount = 0; locked = false;
      eyeEl.textContent = round.prompt || conf.prompt || "Tik het juiste doel";
      subEl.innerHTML = round.sub ? esc(round.sub) : "&nbsp;";
      fbEl.textContent = " "; fbEl.className = "pt-fb";
      card.classList.remove("bad");
      gridEl.innerHTML = "";
      targets.forEach(t=>{
        const b = el("button","pt-tgt", esc(t.label)); b.type="button";
        b.addEventListener("click",()=>tap(t,b));
        gridEl.appendChild(b);
      });
    }
    function endRound(ok, correctLabels){
      locked = true;
      api.judge(ok,{tag:round.tag||"point", stimulus:round.prompt||conf.prompt||"",
        chosen: ok?"":"", correct:[correctLabels], sub:round.sub});
      if(ok){ fbEl.textContent="¡correcto!"; fbEl.className="pt-fb g"; api.sfx.ok(); }
      else { card.classList.add("bad"); fbEl.innerHTML="→ "+esc(correctLabels); fbEl.className="pt-fb b"; }
      ri++; api.tick();
      setTimeout(load, api.calm?350:950);
    }
    function correctList(){ return (round.targets||[]).filter(t=>t.hit).map(t=>t.label).join(" · "); }
    function tap(t,b){
      if(locked || b.classList.contains("done")) return;
      if(mode === "one"){
        if(t.hit){ b.classList.add("hit"); endRound(true, correctList()); }
        else {
          b.classList.add("miss"); api.sfx.bad();
          // toon het juiste doel
          gridEl.querySelectorAll(".pt-tgt").forEach(x=>{});
          const right = round.targets.find(x=>x.hit);
          endRound(false, right?right.label:correctList());
        }
      } else { // mode all
        if(t.hit){
          b.classList.add("hit","done"); api.sfx.move(); hitCount++;
          if(hitCount >= needed) endRound(true, correctList());
        } else {
          b.classList.add("miss"); api.sfx.bad();
          endRound(false, correctList());
        }
      }
    }

    load();
    function esc(s){ return String(s).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])); }
    function shuffle(a){ for(let i=a.length-1;i>0;i--){const j=(Math.random()*(i+1))|0;[a[i],a[j]]=[a[j],a[i]];} return a; }
  }
};
