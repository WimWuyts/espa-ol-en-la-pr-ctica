/* Koppelen: verbind woord met vertaling (of vorm met infinitief, land met nationaliteit…).
   Content levert pairs:[{a,b}]. Bij >8 paren wordt in blokjes gewerkt. */
window.MotorTemplates = window.MotorTemplates || {};
window.MotorTemplates.match = {
  init(api){
    const cfg=api.config, el=api.el;
    const all=(cfg.match&&cfg.match.pairs)||[];
    const CHUNK=(cfg.options&&cfg.options.chunk)||6;
    api.setTarget(all.length);

    const root=api.root; root.innerHTML="";
    const wrap=el("div","mm-wrap");
    wrap.appendChild(el("p","mm-hint", esc(cfg.match&&cfg.match.prompt || "Verbind elk woord met de juiste vertaling")));
    const cols=el("div","mm-cols");
    const colL=el("div","mm-col"), colR=el("div","mm-col");
    cols.appendChild(colL); cols.appendChild(colR); wrap.appendChild(cols); root.appendChild(wrap);

    const palette=["#C4402C","#E0A22F","#2E8E68","#3D74D6","#8B5E9E","#6E6249"];
    let queue = shuffle(all.slice());
    let done=0, block=[], selL=null, selR=null, busy=false;

    function nextBlock(){
      colL.innerHTML=""; colR.innerHTML=""; selL=selR=null;
      block = queue.splice(0,CHUNK);
      if(!block.length){ api.finish(); return; }
      const left = block.map((p,i)=>({p,i}));
      const right = shuffle(block.map((p,i)=>({p,i})));
      left.forEach(o=> colL.appendChild(cell(o.p.a,"L",o.i)));
      right.forEach(o=> colR.appendChild(cell(o.p.b,"R",o.i)));
    }
    function cell(txt,side,idx){
      const c=el("button","mm-cell",esc(txt)); c.type="button";
      c.dataset.idx=idx; c.dataset.side=side;
      c.addEventListener("click",()=>pick(c,side,idx));
      return c;
    }
    function pick(c,side,idx){
      if(busy||c.classList.contains("done"))return;
      if(side==="L"){ if(selL)selL.classList.remove("sel"); selL=c; c.classList.add("sel"); }
      else{ if(selR)selR.classList.remove("sel"); selR=c; c.classList.add("sel"); }
      if(selL&&selR) evaluate();
    }
    function evaluate(){
      busy=true;
      const li=+selL.dataset.idx, ri=+selR.dataset.idx;
      const ok = li===ri;
      const pair = block[li];
      api.judge(ok,{tag:"koppel",stimulus:pair.a,chosen: block[ri].b, correct:[pair.b]});
      if(ok){
        const col=palette[done%palette.length];
        [selL,selR].forEach(c=>{ c.classList.remove("sel"); c.classList.add("done");
          c.style.background="linear-gradient(180deg,"+api.shade(col,1.1)+","+api.shade(col,.85)+")"; });
        done++; api.tick(); selL=selR=null; busy=false;
        if(colL.querySelectorAll(".mm-cell:not(.done)").length===0) setTimeout(nextBlock, 260);
      }else{
        const a=selL,b=selR;
        a.classList.add("wrong"); b.classList.add("wrong");
        setTimeout(()=>{ a.classList.remove("sel","wrong"); b.classList.remove("sel","wrong"); selL=selR=null; busy=false; }, 550);
      }
    }
    nextBlock();

    function shuffle(a){ for(let i=a.length-1;i>0;i--){const j=(Math.random()*(i+1))|0;[a[i],a[j]]=[a[j],a[i]];} return a; }
    function esc(s){ return String(s).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])); }
  }
};
