/* Arcade-skin «mollenmeppen» (mole): dunne skin op de classify-judge.
   De stimulus staat bovenaan; elke categorie is een HOL. Mep het hol met de
   juiste categorie vóór de tijdbalk leeg is. Mollen wippen op voor de sfeer;
   klik = die categorie kiezen. Timeout = mis. Hergebruikt elk classify-pakket. */
window.MotorTemplates = window.MotorTemplates || {};
window.MotorTemplates.mole = {
  init(api){
    const cfg=api.config, el=api.el, shade=api.shade;
    const cats=(cfg.classify&&cfg.classify.categories)||[];
    const root=api.root; root.innerHTML="";
    const rounds=(cfg.options&&cfg.options.rounds)||16;
    api.setTarget(rounds);

    const wrap=el("div","mo-wrap");
    const head=el("div","mo-head");
    head.innerHTML='<div class="mo-eye">¡Aporrea el topo correcto! · <span class="nl">mep het juiste hol</span></div>'+
      '<div class="mo-stim" id="moStim">…</div><div class="mo-sub" id="moSub">&nbsp;</div>'+
      '<div class="mo-timebar"><span id="moTime"></span></div>';
    const stimEl=head.querySelector("#moStim"), subEl=head.querySelector("#moSub"), timeEl=head.querySelector("#moTime");
    const holes=el("div","mo-holes");
    const n=cats.length; const cols=n<=4?2:3;
    holes.style.gridTemplateColumns="repeat("+cols+",1fr)";
    const holeEls=[];
    cats.forEach((c,i)=>{
      const h=el("div","mo-hole"); h.dataset.col=i;
      const mole=el("div","mo-mole");
      mole.style.background="linear-gradient(180deg,"+shade(c.glaze,1.15)+","+shade(c.glaze,.8)+")";
      if(isLight(c.glaze)) mole.classList.add("ink-d");
      mole.innerHTML='<span class="mo-face">•‿•</span><span class="mo-lbl">'+c.label+'</span>';
      h.appendChild(el("div","mo-dirt"));
      h.appendChild(mole);
      h.addEventListener("click",()=>choose(i));
      holes.appendChild(h); holeEls.push({h,mole});
    });
    wrap.appendChild(head); wrap.appendChild(holes);
    root.appendChild(wrap);

    let cur=null, done=0, over=false, tId=null, bobId=null, tLeft=0, tMax=0;

    function bob(){
      // laat willekeurige mollen op/neer wippen voor de sfeer
      holeEls.forEach((o,i)=>{ if(Math.random()<0.5) o.mole.classList.toggle("up", Math.random()<0.6); });
      // zorg dat het juiste hol regelmatig omhoog staat zodat het speelbaar blijft
      if(cur){ const right=correctCol(cur); if(right>=0 && Math.random()<0.7) holeEls[right].mole.classList.add("up"); }
    }
    function correctCol(item){
      const ans=Array.isArray(item.answer)?item.answer:[item.answer];
      return cats.findIndex(c=>ans.indexOf(c.id)>=0);
    }
    function spawn(){
      if(over) return;
      cur=api.next();
      stimEl.textContent=cur.stimulus;
      subEl.innerHTML=(cfg.options&&cfg.options.hint===false)?"&nbsp;":(cur.sub?esc(cur.sub):"&nbsp;");
      holeEls.forEach(o=>o.mole.classList.remove("up","hit","miss"));
      tMax=Math.max(1800, 4200 - done*140); tLeft=tMax;
      timeEl.style.width="100%";
      bob();
    }
    function choose(col){
      if(over||!cur) return;
      const item=cur; cur=null;
      const ans=Array.isArray(item.answer)?item.answer:[item.answer];
      const ok=ans.indexOf(cats[col].id)>=0;
      holeEls[col].mole.classList.add("up",ok?"hit":"miss");
      if(!ok){ const r=correctCol(item); if(r>=0) holeEls[r].mole.classList.add("up","reveal"); }
      api.judge(ok,{tag:item.tag,stimulus:item.stimulus,chosen:cats[col].id,correct:ans,sub:item.sub});
      done++; api.tick();
      if(done>=rounds){ setTimeout(end,450); return; }
      setTimeout(spawn, 480);
    }
    function timeout(){
      if(over||!cur) return;
      const item=cur; cur=null;
      const ans=Array.isArray(item.answer)?item.answer:[item.answer];
      const r=correctCol(item); if(r>=0) holeEls[r].mole.classList.add("up","reveal");
      api.judge(false,{tag:item.tag,stimulus:item.stimulus,chosen:"—(te traag)",correct:ans,sub:item.sub});
      done++; api.tick();
      if(done>=rounds){ setTimeout(end,450); return; }
      setTimeout(spawn, 480);
    }
    function tick(){
      if(over||!cur) return;
      tLeft-=100;
      timeEl.style.width=Math.max(0,(tLeft/tMax*100))+"%";
      if(tLeft<=0) timeout();
    }
    function end(){ over=true; clearInterval(tId); clearInterval(bobId); api.finish(); }

    tId=setInterval(tick,100);
    bobId=setInterval(bob,650);
    api._cleanup=()=>{ over=true; clearInterval(tId); clearInterval(bobId); };
    spawn();

    function esc(s){ return String(s).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])); }
    function isLight(hex){ const n=parseInt(hex.slice(1),16); return (0.299*((n>>16)&255)+0.587*((n>>8)&255)+0.114*(n&255))>176; }
  }
};
