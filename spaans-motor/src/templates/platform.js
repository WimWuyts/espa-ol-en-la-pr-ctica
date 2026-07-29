/* Arcade-skin «platformer» (platform): dunne skin op de classify-judge, met
   POSITIONELE input (het personage beweegt, i.p.v. tikken). De stimulus staat
   boven; onderaan staan deuren (categorieën). Loop met ← → naar de juiste deur
   en ga erin met ↑ / spatie. Juist = punt; fout = de juiste deur licht op.
   Deuren wisselen per beurt van plaats (labels geschud). Hergebruikt elk
   classify-pakket via api.next(). */
window.MotorTemplates = window.MotorTemplates || {};
window.MotorTemplates.platform = {
  init(api){
    const cfg=api.config, el=api.el, shade=api.shade;
    const cats=(cfg.classify&&cfg.classify.categories)||[];
    const root=api.root; root.innerHTML="";
    const rounds=(cfg.options&&cfg.options.rounds)||14;
    api.setTarget(rounds);

    const wrap=el("div","pf-wrap");
    const head=el("div","pf-head");
    head.innerHTML='<div class="pf-eye">Corre a la puerta correcta · <span class="nl">loop naar de juiste deur</span></div>'+
      '<div class="pf-stim" id="pfStim">…</div><div class="pf-sub" id="pfSub">&nbsp;</div>';
    const scene=el("div","pf-scene");
    const doorsRow=el("div","pf-doors");
    const ground=el("div","pf-ground");
    const hero=el("div","pf-hero"); hero.innerHTML='<span class="pf-face">◕‿◕</span>';
    scene.appendChild(doorsRow); scene.appendChild(ground); scene.appendChild(hero);
    const tip=el("div","pf-tip","← → lopen · ↑ / spatie = naar binnen · of tik een deur");
    wrap.appendChild(head); wrap.appendChild(scene); wrap.appendChild(tip);
    root.appendChild(wrap);
    const stimEl=head.querySelector("#pfStim"), subEl=head.querySelector("#pfSub");

    let cur=null, order=[], doorEls=[], heroLane=0, done=0, over=false, busy=false;

    function correctCol(item){ const ans=Array.isArray(item.answer)?item.answer:[item.answer]; return cats.findIndex(c=>ans.indexOf(c.id)>=0); }
    function shuffle(a){ for(let i=a.length-1;i>0;i--){const j=(Math.random()*(i+1))|0;[a[i],a[j]]=[a[j],a[i]];} return a; }

    function spawn(){
      if(over) return;
      cur=api.next(); busy=false;
      stimEl.textContent=cur.stimulus;
      subEl.innerHTML=(cfg.options&&cfg.options.hint===false)?"&nbsp;":(cur.sub?esc(cur.sub):"&nbsp;");
      order=shuffle(cats.map((c,i)=>i));           // wisselende deurvolgorde
      doorsRow.innerHTML=""; doorEls=[];
      order.forEach((ci,pos)=>{
        const c=cats[ci];
        const d=el("div","pf-door"); d.dataset.lane=pos;
        d.style.background="linear-gradient(180deg,"+shade(c.glaze,1.12)+","+shade(c.glaze,.82)+")";
        if(isLight(c.glaze)) d.classList.add("ink-d");
        d.innerHTML='<span class="pf-arch"></span><span class="pf-dl">'+c.label+'</span>';
        d.addEventListener("click",()=>{ heroLane=pos; placeHero(); enter(); });
        doorsRow.appendChild(d); doorEls.push(d);
      });
      heroLane=Math.min(order.length-1, order.length>>1);
      placeHero(true);
    }
    function placeHero(instant){
      const n=order.length; if(!n) return;
      hero.style.transition=instant?"none":"left .16s ease";
      hero.style.left=((heroLane+0.5)/n*100)+"%";
      doorEls.forEach((d,i)=>d.classList.toggle("near",i===heroLane));
    }
    function move(d){ if(over||busy||!cur) return; const n=order.length; heroLane=Math.max(0,Math.min(n-1,heroLane+d)); placeHero(); }
    function enter(){
      if(over||busy||!cur) return;
      busy=true;
      hero.classList.add("jump");
      const ci=order[heroLane], item=cur;
      const ans=Array.isArray(item.answer)?item.answer:[item.answer];
      const ok=ans.indexOf(cats[ci].id)>=0;
      const d=doorEls[heroLane]; d.classList.add(ok?"hit":"miss");
      if(!ok){ const rp=order.indexOf(correctCol(item)); if(rp>=0) doorEls[rp].classList.add("reveal"); }
      api.judge(ok,{tag:item.tag,stimulus:item.stimulus,chosen:cats[ci].id,correct:ans,sub:item.sub});
      cur=null; done++; api.tick();
      setTimeout(()=>hero.classList.remove("jump"),320);
      if(done>=rounds){ setTimeout(end,520); return; }
      setTimeout(spawn, ok?520:950);
    }
    function end(){ over=true; api.finish(); }

    function onKey(e){
      if(over||!cur) return;
      const k=e.key;
      if(k==="ArrowLeft"){e.preventDefault();move(-1);}
      else if(k==="ArrowRight"){e.preventDefault();move(1);}
      else if(k==="ArrowUp"||k===" "||k==="Enter"){e.preventDefault();enter();}
      else if(k>="1"&&k<="9"){const i=+k-1; if(i<order.length){e.preventDefault();heroLane=i;placeHero();enter();}}
    }
    document.addEventListener("keydown",onKey);
    api._cleanup=()=>{ over=true; document.removeEventListener("keydown",onKey); };
    spawn();

    function esc(s){ return String(s).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])); }
    function isLight(hex){ const n=parseInt(hex.slice(1),16); return (0.299*((n>>16)&255)+0.587*((n>>8)&255)+0.114*(n&255))>176; }
  }
};
