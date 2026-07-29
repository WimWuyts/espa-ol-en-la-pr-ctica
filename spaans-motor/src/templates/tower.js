/* Arcade-skin «torenverdediging» (tower): dunne skin op de classify-judge, met
   LEVENS + tijdsdruk (defense-jas). Een vijand (de stimulus) marcheert naar je
   basis; tik de TOREN (categorie) die bij de stimulus past om hem neer te halen
   vóór hij aankomt. Juiste toren = punt; verkeerde toren of de vijand bereikt de
   basis = mis + −1 leven. Levens op → einde. Hergebruikt elk classify-pakket. */
window.MotorTemplates = window.MotorTemplates || {};
window.MotorTemplates.tower = {
  init(api){
    const cfg=api.config, el=api.el, shade=api.shade;
    const cats=(cfg.classify&&cfg.classify.categories)||[];
    const root=api.root; root.innerHTML="";
    const rounds=(cfg.options&&cfg.options.rounds)||16;
    let lives=(cfg.options&&cfg.options.lives)||5;
    api.setTarget(rounds);

    const wrap=el("div","tw-wrap");
    const hpbar=el("div","tw-hp"); hpbar.id="twHp";
    const lane=el("div","tw-lane");
    const enemy=el("div","tw-enemy"); enemy.style.display="none";
    const base=el("div","tw-base"); base.innerHTML='<span>🏰</span>';
    lane.appendChild(base); lane.appendChild(enemy);
    const sub=el("div","tw-sub","&nbsp;");
    const turrets=el("div","tw-turrets"); turrets.style.gridTemplateColumns="repeat("+cats.length+",1fr)";
    cats.forEach((c,i)=>{
      const t=el("div","tw-turret"); t.dataset.col=i;
      t.style.background="linear-gradient(180deg,"+shade(c.glaze,1.12)+","+shade(c.glaze,.8)+")";
      if(isLight(c.glaze)) t.classList.add("ink-d");
      t.innerHTML='<span class="tw-cannon"></span><span class="tw-tl">'+c.label+'</span>'+(i<9?'<small>'+(i+1)+'</small>':'');
      t.addEventListener("click",()=>fire(i));
      turrets.appendChild(t);
    });
    const tip=el("div","tw-tip","tik de juiste toren · of 1–"+Math.min(cats.length,9));
    wrap.appendChild(hpbar); wrap.appendChild(lane); wrap.appendChild(sub); wrap.appendChild(turrets); wrap.appendChild(tip);
    root.appendChild(wrap);

    let cur=null, pos=0, done=0, over=false, raf=null, last=0, speed=0.012, busy=false;

    function renderHp(){ hpbar.innerHTML='<span class="tw-hpk">Base</span> '+"❤".repeat(Math.max(0,lives))+'<span class="tw-hp0">'+"♡".repeat(Math.max(0,5-lives))+'</span>'; }
    function correctCol(item){ const ans=Array.isArray(item.answer)?item.answer:[item.answer]; return cats.findIndex(c=>ans.indexOf(c.id)>=0); }

    function spawn(){
      if(over) return;
      cur=api.next(); pos=0; busy=false;
      enemy.textContent=cur.stimulus;
      const fs=Math.max(11,Math.min(20,200/Math.max(4,String(cur.stimulus).length)));
      enemy.style.fontSize=fs+"px"; enemy.style.display="flex";
      sub.innerHTML=(cfg.options&&cfg.options.hint===false)?"&nbsp;":(cur.sub?esc(cur.sub):"&nbsp;");
      speed=0.010+Math.min(0.02, done*0.0012);
      place();
    }
    function place(){ enemy.style.top=(4+pos*72)+"%"; }
    function loop(t){
      if(over) return;
      if(!last) last=t; const dt=Math.min(50,t-last); last=t;
      if(cur&&!busy){
        pos+=speed*(dt/16.7);
        if(pos>=1){ reach(); } else place();
      }
      raf=requestAnimationFrame(loop);
    }
    function fire(col){
      if(over||!cur||busy) return;
      busy=true;
      const item=cur;
      const ans=Array.isArray(item.answer)?item.answer:[item.answer];
      const ok=ans.indexOf(cats[col].id)>=0;
      const tEl=turrets.querySelector('.tw-turret[data-col="'+col+'"]'); if(tEl){ tEl.classList.add("shoot"); setTimeout(()=>tEl.classList.remove("shoot"),260); }
      if(ok){ enemy.classList.add("boom"); }
      else { enemy.classList.add("pass"); lives--; renderHp(); const r=correctCol(item); const rc=turrets.querySelector('.tw-turret[data-col="'+r+'"]'); if(rc) rc.classList.add("reveal"),setTimeout(()=>rc.classList.remove("reveal"),700); }
      api.judge(ok,{tag:item.tag,stimulus:item.stimulus,chosen:cats[col].id,correct:ans,sub:item.sub});
      resolve();
    }
    function reach(){
      if(over||!cur||busy) return;
      busy=true;
      const item=cur;
      const ans=Array.isArray(item.answer)?item.answer:[item.answer];
      enemy.classList.add("pass"); lives--; renderHp();
      api.judge(false,{tag:item.tag,stimulus:item.stimulus,chosen:"—(basis bereikt)",correct:ans,sub:item.sub});
      resolve();
    }
    function resolve(){
      done++; api.tick();
      setTimeout(()=>{ enemy.style.display="none"; enemy.className="tw-enemy"; }, 300);
      if(lives<=0){ setTimeout(()=>end(true),400); return; }
      if(done>=rounds){ setTimeout(()=>end(false),400); return; }
      setTimeout(spawn, 420);
    }
    function end(dead){ over=true; if(raf)cancelAnimationFrame(raf); api.finish(); }

    function onKey(e){
      if(over||!cur||busy) return;
      if(e.key>="1"&&e.key<="9"){const i=+e.key-1; if(i<cats.length){e.preventDefault();fire(i);}}
    }
    document.addEventListener("keydown",onKey);
    api._cleanup=()=>{ over=true; if(raf)cancelAnimationFrame(raf); document.removeEventListener("keydown",onKey); };

    renderHp();
    requestAnimationFrame(()=>{ last=0; spawn(); raf=requestAnimationFrame(loop); });

    function esc(s){ return String(s).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])); }
    function isLight(hex){ const n=parseInt(hex.slice(1),16); return (0.299*((n>>16)&255)+0.587*((n>>8)&255)+0.114*(n&255))>176; }
  }
};
