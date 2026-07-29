/* Arcade-skin «snake»: dunne skin op de classify-judge, met écht andere
   interactie (STUREN i.p.v. tikken). De stimulus staat boven; op het bord
   liggen voedseltegels (één per categorie). Stuur de slang (pijltjes/WASD/
   vegen) naar het voedsel met de JUISTE categorie. Juist = groeien + punt;
   fout = de juiste tegel licht op. Randen lopen door (wrap); tegen jezelf
   botsen kost lengte, geen game-over (leervriendelijk). Hergebruikt elk
   classify-pakket via api.next(). */
window.MotorTemplates = window.MotorTemplates || {};
window.MotorTemplates.snake = {
  init(api){
    const cfg=api.config, el=api.el, shade=api.shade;
    const cats=(cfg.classify&&cfg.classify.categories)||[];
    const root=api.root; root.innerHTML="";
    const rounds=(cfg.options&&cfg.options.rounds)||14;
    api.setTarget(rounds);
    const N=Math.max(11, cats.length+7);

    const wrap=el("div","sn-wrap");
    const head=el("div","sn-head");
    head.innerHTML='<div class="sn-eye">Lleva la serpiente a la categoría correcta · <span class="nl">stuur naar de juiste tegel</span></div>'+
      '<div class="sn-stim" id="snStim">…</div><div class="sn-sub" id="snSub">&nbsp;</div>';
    const legend=el("div","sn-legend");
    cats.forEach(c=>{ const t=el("span","sn-leg"); t.innerHTML='<i style="background:'+c.glaze+'"></i>'+c.label; legend.appendChild(t); });
    const boardWrap=el("div","sn-boardwrap");
    const board=el("div","sn-board");
    board.style.gridTemplateColumns="repeat("+N+",1fr)";
    const cells=[];
    for(let i=0;i<N*N;i++){ const c=el("div","sn-cell"); board.appendChild(c); cells.push(c); }
    boardWrap.appendChild(board);
    const tip=el("div","sn-tip","← ↑ ↓ → · WASD · of veeg");
    wrap.appendChild(head); wrap.appendChild(legend); wrap.appendChild(boardWrap); wrap.appendChild(tip);
    root.appendChild(wrap);
    const stimEl=head.querySelector("#snStim"), subEl=head.querySelector("#snSub");

    let snake=[{x:(N>>1),y:(N>>1)}], dir={x:1,y:0}, pend=null, foods=[], cur=null, done=0, over=false, timer=null;

    function idx(x,y){ return y*N+x; }
    function occupied(x,y){ return snake.some(s=>s.x===x&&s.y===y) || foods.some(f=>f.x===x&&f.y===y); }
    function placeFoods(){
      foods=[];
      cats.forEach((c,ci)=>{
        let x,y,tries=0;
        do{ x=(Math.random()*N)|0; y=(Math.random()*N)|0; tries++; }while(occupied(x,y)&&tries<200);
        foods.push({x,y,col:ci,label:shortLabel(c.label)});
      });
    }
    function shortLabel(lbl){ const s=String(lbl).replace(/<[^>]+>/g,"").trim(); return s.length<=6?s:s.slice(0,5)+"…"; }
    function correctCol(item){ const ans=Array.isArray(item.answer)?item.answer:[item.answer]; return cats.findIndex(c=>ans.indexOf(c.id)>=0); }

    function spawn(){
      if(over) return;
      cur=api.next();
      stimEl.textContent=cur.stimulus;
      subEl.innerHTML=(cfg.options&&cfg.options.hint===false)?"&nbsp;":(cur.sub?esc(cur.sub):"&nbsp;");
      placeFoods(); paint();
    }
    function paint(){
      cells.forEach(c=>{ c.className="sn-cell"; c.textContent=""; c.style.background=""; c.style.color=""; });
      foods.forEach(f=>{ const c=cells[idx(f.x,f.y)]; c.classList.add("food");
        c.style.background="linear-gradient(180deg,"+shade(cats[f.col].glaze,1.12)+","+shade(cats[f.col].glaze,.82)+")";
        if(isLight(cats[f.col].glaze)) c.style.color="#12264A"; else c.style.color="#F3ECDB";
        c.textContent=f.label; });
      snake.forEach((s,i)=>{ const c=cells[idx(s.x,s.y)]; c.classList.add(i===0?"shead":"sbody"); });
    }
    function setDir(x,y){
      if(over) return;
      if(x===-dir.x && y===-dir.y) return; // geen ommekeer
      pend={x,y};
    }
    function step(){
      if(over||!cur) return;
      if(pend){ dir=pend; pend=null; }
      let hx=(snake[0].x+dir.x+N)%N, hy=(snake[0].y+dir.y+N)%N;
      // eigen staart: kost lengte, geen einde
      if(snake.some((s,i)=>i>0 && s.x===hx&&s.y===hy)){
        if(snake.length>3) snake=snake.slice(0,3);
        api.sfx.bad();
      }
      const nh={x:hx,y:hy};
      const fi=foods.findIndex(f=>f.x===hx&&f.y===hy);
      snake.unshift(nh);
      if(fi>=0){
        const f=foods[fi], item=cur;
        const ans=Array.isArray(item.answer)?item.answer:[item.answer];
        const ok=ans.indexOf(cats[f.col].id)>=0;
        api.judge(ok,{tag:item.tag,stimulus:item.stimulus,chosen:cats[f.col].id,correct:ans,sub:item.sub});
        cur=null; done++; api.tick();
        if(!ok){ snake.pop(); const r=correctCol(item); if(r>=0){ const rc=cells[idx(foods[r].x,foods[r].y)]; rc.classList.add("reveal"); } }
        // bij juist: groei (staart NIET poppen)
        foods=[]; paint();
        if(done>=rounds){ setTimeout(end, ok?260:650); return; }
        setTimeout(()=>{ if(!over) spawn(); }, ok?260:650);
        return;
      } else {
        snake.pop(); // gewone stap
      }
      paint();
    }
    function end(){ over=true; clearInterval(timer); api.finish(); }

    function onKey(e){
      const k=e.key.toLowerCase();
      if(k==="arrowleft"||k==="a"){e.preventDefault();setDir(-1,0);}
      else if(k==="arrowright"||k==="d"){e.preventDefault();setDir(1,0);}
      else if(k==="arrowup"||k==="w"){e.preventDefault();setDir(0,-1);}
      else if(k==="arrowdown"||k==="s"){e.preventDefault();setDir(0,1);}
    }
    document.addEventListener("keydown",onKey);
    // vegen
    let tx=0,ty=0;
    function ts(e){ const t=e.touches[0]; tx=t.clientX; ty=t.clientY; }
    function te(e){ const t=e.changedTouches[0], dx=t.clientX-tx, dy=t.clientY-ty;
      if(Math.abs(dx)<20&&Math.abs(dy)<20) return;
      if(Math.abs(dx)>Math.abs(dy)) setDir(dx>0?1:-1,0); else setDir(0,dy>0?1:-1); }
    board.addEventListener("touchstart",ts,{passive:true});
    board.addEventListener("touchend",te,{passive:true});

    api._cleanup=()=>{ over=true; clearInterval(timer); document.removeEventListener("keydown",onKey);
      board.removeEventListener("touchstart",ts); board.removeEventListener("touchend",te); };

    spawn();
    timer=setInterval(step, api.calm?360:260);

    function esc(s){ return String(s).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])); }
    function isLight(hex){ const n=parseInt(hex.slice(1),16); return (0.299*((n>>16)&255)+0.587*((n>>8)&255)+0.114*(n&255))>176; }
  }
};
