/* Arcade-skin «sorteerband» (belt): dunne skin op de classify-judge.
   De stimulus rijdt op een lopende band naar het einde; stuur hem naar de
   juiste bak (categorie) vóór hij van de band valt. Tik de bak / pijltjes+spatie
   / 1–9. Op tijd in de juiste bak = punt; verkeerde bak of van de band = mis.
   Hergebruikt ELK classify-pakket (ook met generator) via api.next(). */
window.MotorTemplates = window.MotorTemplates || {};
window.MotorTemplates.belt = {
  init(api){
    const cfg=api.config, el=api.el, shade=api.shade;
    const cats=(cfg.classify&&cfg.classify.categories)||[];
    const COLS=cats.length;
    const root=api.root; root.innerHTML="";
    const rounds=(cfg.options&&cfg.options.rounds)||16;
    api.setTarget(rounds);

    const wrap=el("div","bl-wrap");
    const track=el("div","bl-track");
    const tile=el("div","bl-tile"); tile.style.display="none";
    const goal=el("div","bl-goal"); // rand waar hij afvalt
    track.appendChild(goal); track.appendChild(tile);
    const sub=el("div","bl-sub","&nbsp;");
    const bins=el("div","bl-bins"); bins.style.gridTemplateColumns="repeat("+COLS+",1fr)";
    cats.forEach((c,i)=>{
      const b=el("div","bl-bin"); b.dataset.col=i;
      b.style.background="linear-gradient(180deg,"+shade(c.glaze,1.12)+","+shade(c.glaze,.82)+")";
      if(isLight(c.glaze)) b.classList.add("ink-d");
      b.innerHTML='<span class="bl-bl">'+c.label+'</span>'+(i<9?'<small>'+(i+1)+'</small>':'');
      b.addEventListener("click",()=>choose(i));
      bins.appendChild(b);
    });
    const tip=el("div","bl-tip","tik de juiste bak · of ← → + spatie · of 1–"+Math.min(COLS,9));
    wrap.appendChild(track); wrap.appendChild(sub); wrap.appendChild(bins); wrap.appendChild(tip);
    root.appendChild(wrap);

    let cur=null, pos=0, aim=0, done=0, over=false, raf=null, last=0, speed=0.018;

    function spawn(){
      if(over) return;
      cur=api.next(); pos=0; aim=Math.max(0,Math.min(COLS-1, COLS>>1));
      tile.textContent=cur.stimulus;
      tile.style.display="flex";
      const fs=Math.max(11,Math.min(22,(track.clientWidth*0.5)/Math.max(4,String(cur.stimulus).length)));
      tile.style.fontSize=fs+"px";
      sub.innerHTML=(cfg.options&&cfg.options.hint===false)?"&nbsp;":(cur.sub?esc(cur.sub):"&nbsp;");
      paintAim(); place();
      speed=0.014+Math.min(0.03, done*0.0016);
    }
    function paintAim(){ bins.querySelectorAll(".bl-bin").forEach((b,i)=>b.classList.toggle("aim",i===aim)); }
    function place(){
      tile.style.left=(6+pos*88)+"%";
    }
    function loop(t){
      if(over){ return; }
      if(!last) last=t;
      const dt=Math.min(50,t-last); last=t;
      if(cur){
        pos+=speed*(dt/16.7);
        if(pos>=1){ resolve(-1); }  // van de band → mis
        else place();
      }
      raf=requestAnimationFrame(loop);
    }
    function choose(col){ if(over||!cur) return; aim=col; paintAim(); resolve(col); }
    function resolve(col){
      if(!cur) return;
      const item=cur; cur=null; tile.style.display="none";
      const ans=Array.isArray(item.answer)?item.answer:[item.answer];
      const ok = col>=0 && ans.indexOf(cats[col].id)>=0;
      api.judge(ok,{tag:item.tag,stimulus:item.stimulus,chosen:col>=0?cats[col].id:"—(afgevallen)",correct:ans,sub:item.sub});
      done++; api.tick();
      if(col>=0){ const b=bins.querySelector('.bl-bin[data-col="'+col+'"]'); if(b){ b.classList.add(ok?"hit":"miss"); setTimeout(()=>b.classList.remove("hit","miss"),300); } }
      if(done>=rounds){ end(); return; }
      setTimeout(spawn, 260);
    }
    function end(){ over=true; if(raf)cancelAnimationFrame(raf); api.finish(); }

    function onKey(e){
      if(over||!cur) return;
      if(e.key==="ArrowLeft"){e.preventDefault();aim=Math.max(0,aim-1);paintAim();}
      else if(e.key==="ArrowRight"){e.preventDefault();aim=Math.min(COLS-1,aim+1);paintAim();}
      else if(e.key===" "||e.key==="Enter"){e.preventDefault();resolve(aim);}
      else if(e.key>="1"&&e.key<="9"){const i=+e.key-1;if(i<COLS){e.preventDefault();choose(i);}}
    }
    document.addEventListener("keydown",onKey);
    api._cleanup=()=>{ over=true; if(raf)cancelAnimationFrame(raf); document.removeEventListener("keydown",onKey); };

    requestAnimationFrame(t=>{ last=0; spawn(); raf=requestAnimationFrame(loop); });

    function esc(s){ return String(s).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])); }
    function isLight(hex){ const n=parseInt(hex.slice(1),16); return (0.299*((n>>16)&255)+0.587*((n>>8)&255)+0.114*(n&255))>176; }
  }
};
