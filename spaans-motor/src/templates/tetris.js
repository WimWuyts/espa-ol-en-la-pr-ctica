/* Tetris-sjabloon: sorteer-faller. Kolommen = categorieën uit cfg.classify.
   Stimulus valt; stuur ze naar de juiste kolom (tik kolom / pijltjes / 1-9).
   Juist = schone tegel; fout = gebarsten tegel (vult je bord). Volle rij = weg.
   Bord vol → einde. Hergebruikt ELK classify-pakket, ook met generator. */
window.MotorTemplates = window.MotorTemplates || {};
window.MotorTemplates.tetris = {
  init(api){
    const cfg=api.config, el=api.el, shade=api.shade;
    const cats=(cfg.classify&&cfg.classify.categories)||[];
    const COLS=cats.length, ROWS=(cfg.options&&cfg.options.rows)||9;
    const START=(cfg.options&&cfg.options.speed)||1050;
    const root=api.root; root.innerHTML="";

    const wrap=el("div","tx-wrap");
    const head=el("div","tx-head"); head.style.gridTemplateColumns="repeat("+COLS+",1fr)";
    cats.forEach((c,i)=>{
      const h=el("div","tx-h"); h.dataset.col=i;
      h.style.background="linear-gradient(180deg,"+shade(c.glaze,1.12)+","+shade(c.glaze,.84)+")";
      if(isLight(c.glaze)) h.classList.add("ink-d");
      h.innerHTML=c.label+(i<9?"<small>"+(i+1)+"</small>":"");
      h.addEventListener("click",()=>drop(i));
      head.appendChild(h);
    });
    const grid=el("div","tx-grid"); grid.style.gridTemplateColumns="repeat("+COLS+",1fr)";
    const cells=[];
    for(let i=0;i<ROWS*COLS;i++){ const c=el("div","tx-cell"); grid.appendChild(c); cells.push(c); }
    const active=el("div","tx-active"); active.style.display="none"; grid.appendChild(active);
    const sub=el("div","tx-sub","&nbsp;");
    const meta=el("div","tx-meta"); meta.innerHTML='<span>Lijnen <b class="m" id="txL">0</b></span><span>Niveau <b class="m" id="txN">1</b></span>';
    const tip=el("div","tx-tip","tik de kolom · of pijltjes + spatie · of 1–"+Math.min(COLS,9));
    wrap.appendChild(head); wrap.appendChild(grid); wrap.appendChild(meta); wrap.appendChild(sub); wrap.appendChild(tip);
    root.appendChild(wrap);

    /* staat */
    const board=Array.from({length:ROWS},()=>new Array(COLS).fill(null));
    const height=new Array(COLS).fill(0);
    let cur=null, lines=0, drops=0, over=false, timer=null, cw=0, chh=0;

    function measure(){ const c0=cells[0].getBoundingClientRect(), g=grid.getBoundingClientRect();
      cw=cells[1]?(cells[1].getBoundingClientRect().left-c0.left):c0.width+4;
      chh=(cells[COLS]?(cells[COLS].getBoundingClientRect().top-c0.top):c0.height+4);
      active.style.width=c0.width+"px"; active.style.height=c0.height+"px";
      active.style.fontSize=Math.max(10,Math.min(20, (c0.width*1.7)/Math.max(4,curLen())))+"px";
    }
    function curLen(){ return cur? String(cur.item.stimulus).length : 6; }
    function place(){ if(!cur){active.style.display="none";return;}
      const base=cells[0].getBoundingClientRect(), g=grid.getBoundingClientRect();
      const x=(cells[cur.col].getBoundingClientRect().left)-g.left+grid.clientLeft;
      const r=cur.row<0?0:cur.row;
      const y=(cells[r*COLS+cur.col].getBoundingClientRect().top)-g.top+grid.clientTop + (cur.row<0?-chh:0);
      active.style.left=x+"px"; active.style.top=y+"px"; active.style.display="flex";
    }
    function paint(){
      for(let r=0;r<ROWS;r++)for(let c=0;c<COLS;c++){
        const cell=cells[r*COLS+c], b=board[r][c];
        cell.className="tx-cell";
        if(b){ cell.classList.add("on"); if(!b.ok)cell.classList.add("crack");
          cell.style.background="linear-gradient(180deg,"+shade(b.glaze,1.1)+","+shade(b.glaze,.82)+")"; }
        else cell.style.background="";
      }
    }
    function floor(col){ return ROWS-1-height[col]; }

    function spawn(){
      if(over) return;
      cur={ col:(COLS>>1), row:-1, item:api.next() };
      active.textContent=cur.item.stimulus;
      sub.innerHTML = (cfg.options&&cfg.options.hint===false)?"&nbsp;":(cur.item.sub?esc(cur.item.sub):"&nbsp;");
      measure(); place();
    }
    function step(){
      if(over||!cur) return;
      const fr=floor(cur.col);
      if(cur.row>=fr){ lock(); return; }
      cur.row++; place();
    }
    function moveCol(d){ if(over||!cur)return; const n=cur.col+d; if(n>=0&&n<COLS){cur.col=n;place();} }
    function drop(col){ if(over||!cur)return; if(col!=null)cur.col=col; cur.row=floor(cur.col); place(); lock(); }

    function lock(){
      const col=cur.col, fr=floor(col);
      if(fr<0){ end(); return; }
      const ans=Array.isArray(cur.item.answer)?cur.item.answer:[cur.item.answer];
      const ok=ans.indexOf(cats[col].id)>=0;
      board[fr][col]={glaze:cats[col].glaze, ok}; height[col]++;
      api.judge(ok,{tag:cur.item.tag,stimulus:cur.item.stimulus,chosen:cats[col].id,correct:ans,sub:cur.item.sub});
      cur=null; active.style.display="none";
      paint(); clearLines(); drops++;
      if(height.some(h=>h>=ROWS)){ end(); return; }
      retime();
      setTimeout(spawn, 70);
    }
    function clearLines(){
      let cleared=0;
      for(let r=ROWS-1;r>=0;r--){
        let full=true; for(let c=0;c<COLS;c++) if(!board[r][c]){full=false;break;}
        if(full){ cleared++;
          for(let c=0;c<COLS;c++) cells[r*COLS+c].classList.add("clear");
          for(let rr=r; rr>0; rr--) board[rr]=board[rr-1].slice();
          board[0]=new Array(COLS).fill(null); r++;
        }
      }
      if(cleared){
        for(let c=0;c<COLS;c++){ let h=0; for(let r=0;r<ROWS;r++) if(board[r][c])h++; height[c]=h; }
        lines+=cleared; document.getElementById("txL").textContent=lines;
        api.bonus(cleared*cleared*25); api.sfx.win();
        setTimeout(paint, 120);
      }
    }
    function level(){ return 1+Math.floor(drops/8); }
    function retime(){ const n=level(); document.getElementById("txN").textContent=n;
      clearInterval(timer); timer=setInterval(step, Math.max(340, START - (n-1)*80)); }
    function end(){ over=true; clearInterval(timer); api.finish(); }

    function onKey(e){
      if(over||!cur) return;
      if(e.key==="ArrowLeft"){e.preventDefault();moveCol(-1);}
      else if(e.key==="ArrowRight"){e.preventDefault();moveCol(1);}
      else if(e.key===" "||e.key==="ArrowDown"){e.preventDefault();drop(null);}
      else if(e.key>="1"&&e.key<="9"){const i=+e.key-1; if(i<COLS){e.preventDefault();drop(i);}}
    }
    document.addEventListener("keydown",onKey);
    grid.addEventListener("click",e=>{ if(!cur)return; const g=grid.getBoundingClientRect();
      const i=Math.max(0,Math.min(COLS-1,Math.floor((e.clientX-g.left)/(g.width/COLS)))); drop(i); });
    const onResize=()=>{ measure(); place(); };
    window.addEventListener("resize",onResize);
    api._cleanup=()=>{ clearInterval(timer); document.removeEventListener("keydown",onKey); window.removeEventListener("resize",onResize); };

    paint();
    requestAnimationFrame(()=>{ spawn(); retime(); });

    function esc(s){ return String(s).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])); }
    function isLight(hex){ const n=parseInt(hex.slice(1),16); return (0.299*((n>>16)&255)+0.587*((n>>8)&255)+0.114*(n&255))>176; }
  }
};
