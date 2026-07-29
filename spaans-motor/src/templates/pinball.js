/* Arcade-skin «pinball» (flipper): dunne skin op de classify-judge, met
   REFLEX/timing-input (echt andere vaardigheid). De bal (stimulus) valt; onderaan
   twee flippers (← rechts-in, → links-in of tik de helft van het veld). Flip de
   bal naar het categorie-DOEL bovenaan dat bij de stimulus past. Bal raakt het
   juiste doel = punt; verkeerd doel of de bal valt eruit = mis. 1–9 = toegankelijke
   directe keuze (zonder fysica). Hergebruikt elk classify-pakket via api.next(). */
window.MotorTemplates = window.MotorTemplates || {};
window.MotorTemplates.pinball = {
  init(api){
    const cfg=api.config, el=api.el, shade=api.shade;
    const cats=(cfg.classify&&cfg.classify.categories)||[];
    const root=api.root; root.innerHTML="";
    const rounds=(cfg.options&&cfg.options.rounds)||14;
    api.setTarget(rounds);

    const wrap=el("div","pb-wrap");
    const head=el("div","pb-head");
    head.innerHTML='<div class="pb-eye">Empuja la bola al objetivo correcto · <span class="nl">flip naar het juiste doel</span></div>'+
      '<div class="pb-stim" id="pbStim">…</div><div class="pb-sub" id="pbSub">&nbsp;</div>';
    const field=el("div","pb-field");
    const targets=el("div","pb-targets");
    cats.forEach((c,i)=>{
      const t=el("div","pb-target"); t.dataset.col=i;
      t.style.background="linear-gradient(180deg,"+shade(c.glaze,1.14)+","+shade(c.glaze,.82)+")";
      if(isLight(c.glaze)) t.classList.add("ink-d");
      t.innerHTML='<span class="pb-tl">'+c.label+'</span>'+(i<9?'<small>'+(i+1)+'</small>':'');
      targets.appendChild(t);
    });
    const ball=el("div","pb-ball");
    const flipL=el("div","pb-flip l"); const flipR=el("div","pb-flip r");
    field.appendChild(targets); field.appendChild(ball); field.appendChild(flipL); field.appendChild(flipR);
    const tip=el("div","pb-tip","← / → = flippers (of tik links/rechts) · 1–"+Math.min(cats.length,9)+" = kiezen");
    wrap.appendChild(head); wrap.appendChild(field); wrap.appendChild(tip);
    root.appendChild(wrap);
    const stimEl=head.querySelector("#pbStim"), subEl=head.querySelector("#pbSub");

    let cur=null, done=0, over=false, raf=null, last=0, busy=false;
    let W=0,H=0,R=13, x=0,y=0,vx=0,vy=0;
    const G=0.16, BAND=46, FLIPH=64;

    function measure(){ const r=field.getBoundingClientRect(); W=r.width; H=r.height; }
    function correctCol(item){ const ans=Array.isArray(item.answer)?item.answer:[item.answer]; return cats.findIndex(c=>ans.indexOf(c.id)>=0); }

    function spawn(){
      if(over) return;
      cur=api.next(); busy=false;
      stimEl.textContent=cur.stimulus;
      subEl.innerHTML=(cfg.options&&cfg.options.hint===false)?"&nbsp;":(cur.sub?esc(cur.sub):"&nbsp;");
      measure();
      x=W*(0.35+Math.random()*0.3); y=H*0.46; vx=(Math.random()*2-1)*1.4; vy=0.6;
      ball.style.display="flex"; ball.textContent="●"; drawBall();
    }
    function drawBall(){ ball.style.left=x+"px"; ball.style.top=y+"px"; }
    function flip(side){
      if(over||busy||!cur) return;
      const fEl=side<0?flipL:flipR;
      fEl.classList.add("on"); setTimeout(()=>fEl.classList.remove("on"),130);
      // impuls als de bal laag genoeg is en aan de juiste kant
      if(y > H-FLIPH-R*2){
        const onSide = side<0 ? (x < W*0.52) : (x > W*0.48);
        if(onSide){
          vy = -Math.max(4.2, Math.abs(vy)*0.6+4.2);
          vx += side<0 ? 2.6 : -2.6;   // naar het midden/omhoog duwen
          api.sfx.move();
        }
      }
    }
    function hit(col){
      if(over||!cur||busy) return;
      busy=true;
      const item=cur;
      const ans=Array.isArray(item.answer)?item.answer:[item.answer];
      const ok = col>=0 && ans.indexOf(cats[col].id)>=0;
      if(col>=0){ const tEl=targets.querySelector('.pb-target[data-col="'+col+'"]'); if(tEl){ tEl.classList.add(ok?"lit":"miss"); setTimeout(()=>tEl.classList.remove("lit","miss"),500);} }
      if(!ok){ const r=correctCol(item); const rc=targets.querySelector('.pb-target[data-col="'+r+'"]'); if(rc){ rc.classList.add("reveal"); setTimeout(()=>rc.classList.remove("reveal"),700);} }
      api.judge(ok,{tag:item.tag,stimulus:item.stimulus,chosen:col>=0?cats[col].id:"—(bal eruit)",correct:ans,sub:item.sub});
      ball.style.display="none";
      done++; api.tick();
      if(done>=rounds){ setTimeout(()=>end(),560); return; }
      setTimeout(spawn, 460);
    }
    function loop(t){
      if(over) return;
      if(!last) last=t; const dtf=Math.min(2.4,(t-last)/16.7); last=t;
      if(cur&&!busy){
        vy+=G*dtf; x+=vx*dtf*2; y+=vy*dtf*2;
        if(x<R){ x=R; vx=-vx*0.78; } else if(x>W-R){ x=W-R; vx=-vx*0.78; }
        if(y<=BAND+R){ // bovenaan → doelzone
          const n=cats.length, zi=Math.max(0,Math.min(n-1,Math.floor(x/(W/n))));
          hit(zi);
        } else if(y>H+R){ // eruit gevallen (drain)
          hit(-1);
        } else drawBall();
      }
      raf=requestAnimationFrame(loop);
    }
    function end(){ over=true; if(raf)cancelAnimationFrame(raf); api.finish(); }

    function onKey(e){
      if(over||!cur) return;
      const k=e.key;
      if(k==="ArrowLeft"){e.preventDefault();flip(-1);}
      else if(k==="ArrowRight"){e.preventDefault();flip(1);}
      else if(k>="1"&&k<="9"){const i=+k-1; if(i<cats.length){e.preventDefault();hit(i);}}
    }
    document.addEventListener("keydown",onKey);
    function onTap(e){ const r=field.getBoundingClientRect(); flip((e.clientX-r.left) < r.width/2 ? -1 : 1); }
    field.addEventListener("pointerdown",onTap);
    const onResize=()=>measure();
    window.addEventListener("resize",onResize);
    api._cleanup=()=>{ over=true; if(raf)cancelAnimationFrame(raf); document.removeEventListener("keydown",onKey);
      field.removeEventListener("pointerdown",onTap); window.removeEventListener("resize",onResize); };

    requestAnimationFrame(()=>{ last=0; measure(); spawn(); raf=requestAnimationFrame(loop); });

    function esc(s){ return String(s).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])); }
    function isLight(hex){ const n=parseInt(hex.slice(1),16); return (0.299*((n>>16)&255)+0.587*((n>>8)&255)+0.114*(n&255))>176; }
  }
};
