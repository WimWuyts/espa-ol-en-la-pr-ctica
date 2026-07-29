/* Arcade-skin «bubbelschieter» (bubble): dunne skin op de classify-judge.
   Categorie-bubbels drijven bovenaan; onderaan een kanon met de stimulus.
   Tik de juiste bubbel → de stimulus vliegt erheen en de bubbel knapt.
   Juist = punt; fout = de juiste bubbel licht op. Accuratesse i.p.v. tempo
   (variatie t.o.v. band/mol). Hergebruikt elk classify-pakket. */
window.MotorTemplates = window.MotorTemplates || {};
window.MotorTemplates.bubble = {
  init(api){
    const cfg=api.config, el=api.el, shade=api.shade;
    const cats=(cfg.classify&&cfg.classify.categories)||[];
    const root=api.root; root.innerHTML="";
    const rounds=(cfg.options&&cfg.options.rounds)||16;
    api.setTarget(rounds);

    const wrap=el("div","bu-wrap");
    const sky=el("div","bu-sky");
    const bubbleEls=[];
    cats.forEach((c,i)=>{
      const b=el("div","bu-bub"); b.dataset.col=i;
      b.style.background="radial-gradient(circle at 34% 30%, rgba(255,255,255,.75), "+shade(c.glaze,1.05)+" 42%, "+shade(c.glaze,.72)+")";
      if(isLight(c.glaze)) b.classList.add("ink-d");
      b.innerHTML='<span>'+c.label+'</span>'+(i<9?'<small>'+(i+1)+'</small>':'');
      b.style.animationDelay=(i*0.4)+"s";
      b.addEventListener("click",()=>shoot(i));
      sky.appendChild(b); bubbleEls.push(b);
    });
    const cannon=el("div","bu-cannon");
    cannon.innerHTML='<div class="bu-sub" id="buSub">&nbsp;</div><div class="bu-ammo" id="buAmmo">…</div><div class="bu-base"></div>';
    const projectile=el("div","bu-proj"); projectile.style.display="none";
    const tip=el("div","bu-tip","tik de bubbel met de juiste categorie");
    wrap.appendChild(sky); wrap.appendChild(cannon); wrap.appendChild(projectile); wrap.appendChild(tip);
    root.appendChild(wrap);

    const ammoEl=cannon.querySelector("#buAmmo"), subEl=cannon.querySelector("#buSub");
    let cur=null, done=0, over=false, busy=false;

    function spawn(){
      if(over) return;
      cur=api.next(); busy=false;
      ammoEl.textContent=cur.stimulus;
      const fs=Math.max(12,Math.min(22,220/Math.max(4,String(cur.stimulus).length)));
      ammoEl.style.fontSize=fs+"px";
      subEl.innerHTML=(cfg.options&&cfg.options.hint===false)?"&nbsp;":(cur.sub?esc(cur.sub):"&nbsp;");
      bubbleEls.forEach(b=>b.classList.remove("pop","reveal","miss"));
    }
    function correctCol(item){ const ans=Array.isArray(item.answer)?item.answer:[item.answer]; return cats.findIndex(c=>ans.indexOf(c.id)>=0); }

    function shoot(col){
      if(over||!cur||busy) return;
      busy=true;
      const item=cur;
      const ans=Array.isArray(item.answer)?item.answer:[item.answer];
      const ok=ans.indexOf(cats[col].id)>=0;
      // projectiel-animatie van kanon → doelbubbel
      const wr=wrap.getBoundingClientRect(), tb=bubbleEls[col].getBoundingClientRect(), am=ammoEl.getBoundingClientRect();
      projectile.textContent=item.stimulus;
      projectile.style.fontSize=ammoEl.style.fontSize;
      projectile.style.display="flex";
      projectile.style.left=(am.left-wr.left+am.width/2)+"px";
      projectile.style.top=(am.top-wr.top+am.height/2)+"px";
      ammoEl.textContent="";
      requestAnimationFrame(()=>{
        projectile.style.transition="left .32s ease, top .32s ease";
        projectile.style.left=(tb.left-wr.left+tb.width/2)+"px";
        projectile.style.top=(tb.top-wr.top+tb.height/2)+"px";
      });
      setTimeout(()=>{
        projectile.style.display="none"; projectile.style.transition="";
        bubbleEls[col].classList.add(ok?"pop":"miss");
        if(!ok){ const r=correctCol(item); if(r>=0) bubbleEls[r].classList.add("reveal"); }
        api.judge(ok,{tag:item.tag,stimulus:item.stimulus,chosen:cats[col].id,correct:ans,sub:item.sub});
        cur=null; done++; api.tick();
        if(done>=rounds){ setTimeout(end,520); return; }
        setTimeout(spawn, ok?420:900);
      },340);
    }
    function end(){ over=true; api.finish(); }

    function onKey(e){
      if(over||!cur||busy) return;
      if(e.key>="1"&&e.key<="9"){const i=+e.key-1;if(i<cats.length){e.preventDefault();shoot(i);}}
    }
    document.addEventListener("keydown",onKey);
    api._cleanup=()=>{ over=true; document.removeEventListener("keydown",onKey); };
    spawn();

    function esc(s){ return String(s).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])); }
    function isLight(hex){ const n=parseInt(hex.slice(1),16); return (0.299*((n>>16)&255)+0.587*((n>>8)&255)+0.114*(n&255))>176; }
  }
};
