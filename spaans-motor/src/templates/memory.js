/* Memoria (kaartparen / concentration): draai twee kaartjes om en zoek de
   paren (Spaans ↔ Nederlands, cifra ↔ letra …). Content: memory.pairs:[{a,b}].
   options.pairs = aantal paren per bord (default 6 → 12 kaartjes). */
window.MotorTemplates = window.MotorTemplates || {};
window.MotorTemplates.memory = {
  init(api){
    const cfg = api.config, el = api.el;
    const conf = cfg.memory || {};
    const all = (conf.pairs || []).slice();
    const PER = (cfg.options && cfg.options.pairs) || 6;
    api.setTarget(all.length);

    const root = api.root; root.innerHTML = "";
    const wrap = el("div","my-wrap");
    wrap.appendChild(el("p","my-hint", esc(conf.prompt || "Zoek de paren")));
    const grid = el("div","my-grid"); wrap.appendChild(grid);
    root.appendChild(wrap);

    let queue = shuffle(all.slice());
    let first = null, busy = false, boardLeft = 0;

    function nextBoard(){
      grid.innerHTML = ""; first = null; busy = false;
      const block = queue.splice(0, PER);
      if(!block.length){ api.finish(); return; }
      boardLeft = block.length;
      const cards = [];
      block.forEach((p,i)=>{
        cards.push({pid:i, side:"a", txt:p.a, mate:p.b});
        cards.push({pid:i, side:"b", txt:p.b, mate:p.a});
      });
      grid.style.gridTemplateColumns = "repeat("+colsFor(cards.length)+",1fr)";
      shuffle(cards).forEach(c=>{
        const b = el("button","my-card");
        b.type = "button";
        b.innerHTML = '<span class="my-face my-back">?</span><span class="my-face my-front">'+esc(c.txt)+'</span>';
        b.dataset.pid = c.pid; b.dataset.side = c.side;
        b._card = c;
        b.addEventListener("click",()=>flip(b));
        grid.appendChild(b);
      });
    }
    function colsFor(n){ return n<=8?2:n<=12?3:4; }

    function flip(b){
      if(busy || b.classList.contains("done") || b.classList.contains("up")) return;
      b.classList.add("up"); api.sfx.move();
      if(!first){ first = b; return; }
      busy = true;
      const ok = first.dataset.pid === b.dataset.pid && first.dataset.side !== b.dataset.side;
      api.judge(ok,{tag:"memoria", stimulus:first._card.txt, chosen:b._card.txt, correct:[first._card.mate]});
      if(ok){
        const a=first, c=b;
        setTimeout(()=>{ a.classList.add("done"); c.classList.add("done"); first=null; busy=false;
          boardLeft--; api.tick();
          if(boardLeft<=0) setTimeout(nextBoard, 340);
        }, 260);
      }else{
        const a=first, c=b;
        c.classList.add("bad"); a.classList.add("bad");
        setTimeout(()=>{ a.classList.remove("up","bad"); c.classList.remove("up","bad"); first=null; busy=false; }, 760);
      }
    }

    nextBoard();

    function esc(s){ return String(s).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])); }
    function shuffle(a){ for(let i=a.length-1;i>0;i--){const j=(Math.random()*(i+1))|0;[a[i],a[j]]=[a[j],a[i]];} return a; }
  }
};
