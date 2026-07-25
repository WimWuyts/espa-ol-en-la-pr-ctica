/* Classificeren: lees de stimulus, tik de juiste categorie/persoon.
   Dekt vervoeging→persoon, ser/estar, por/para, geslacht, tilde, b/v … */
window.MotorTemplates = window.MotorTemplates || {};
window.MotorTemplates.classify = {
  init(api){
    const cfg = api.config;
    const cats = (cfg.classify && cfg.classify.categories) || [];
    const rounds = (cfg.options && cfg.options.rounds) || 20;
    const el = api.el, shade = api.shade;
    api.setTarget(rounds);

    const root = api.root; root.innerHTML="";
    const card = el("div","cl-card");
    card.innerHTML='<div class="cl-eye">'+esc(cfg.classify.prompt||"Kies")+'</div>'+
      '<div class="cl-form" id="clForm">…</div><div class="cl-sub" id="clSub">&nbsp;</div>'+
      '<div class="cl-fb" id="clFb">&nbsp;</div>';
    root.appendChild(card);

    const lanes = el("div","cl-lanes");
    lanes.style.gridTemplateColumns = "repeat("+Math.min(cats.length,3)+",1fr)";
    const laneEls = cats.map((c,i)=>{
      const b=el("button","cl-lane"); b.type="button";
      const ink = isDark(c.glaze) ? "#16233D" : "#FBF6E9";
      b.style.background="linear-gradient(180deg,"+shade(c.glaze,1.12)+","+shade(c.glaze,.84)+")";
      b.style.color=ink;
      b.innerHTML=c.label+(i<9?"<small>"+(i+1)+"</small>":"");
      b.addEventListener("click",()=>choose(i));
      lanes.appendChild(b);
      return b;
    });
    root.appendChild(lanes);

    let cur=null, locked=false, n=0;
    const formEl=card.querySelector("#clForm"), subEl=card.querySelector("#clSub"), fbEl=card.querySelector("#clFb");

    function load(){
      if(n>=rounds){ api.finish(); return; }
      cur=api.next(); locked=false;
      laneEls.forEach(b=>b.classList.remove("flash-g","flash-b","reveal"));
      fbEl.textContent="\u00a0"; fbEl.className="cl-fb";
      formEl.textContent=cur.stimulus;
      subEl.innerHTML = (cfg.options && cfg.options.hint===false) ? "&nbsp;" : (cur.sub? esc(cur.sub) : "&nbsp;");
    }
    function choose(i){
      if(locked||!cur) return; locked=true;
      const catId=cats[i].id;
      const answer = Array.isArray(cur.answer)?cur.answer:[cur.answer];
      const ok = answer.indexOf(catId)>=0;
      api.judge(ok,{tag:cur.tag,stimulus:cur.stimulus,chosen:catId,correct:answer,sub:cur.sub});
      n++; api.tick();
      if(ok){
        laneEls[i].classList.add("flash-g"); card.classList.remove("bad"); card.classList.add("good");
        fbEl.textContent="¡correcto!"; fbEl.className="cl-fb g";
        setTimeout(()=>{card.classList.remove("good");load();}, api.calm?200:420);
      }else{
        laneEls[i].classList.add("flash-b"); card.classList.remove("good"); card.classList.add("bad");
        answer.forEach(a=>{ const j=cats.findIndex(c=>c.id===a); if(j>=0) laneEls[j].classList.add("reveal"); });
        const goed = answer.map(a=>{const c=cats.find(x=>x.id===a);return c?c.label.replace(/<[^>]+>/g," ").trim():a;}).join(" / ");
        fbEl.innerHTML="→ "+esc(goed); fbEl.className="cl-fb b";
        setTimeout(()=>{card.classList.remove("bad");load();}, api.calm?400:900);
      }
    }

    /* toetsen 1..9 */
    function onKey(e){
      if(e.key>="1"&&e.key<="9"){ const i=parseInt(e.key,10)-1; if(i<cats.length){e.preventDefault();choose(i);} }
    }
    document.addEventListener("keydown",onKey);
    api._cleanup = ()=>document.removeEventListener("keydown",onKey);

    load();

    function esc(s){ return String(s).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])); }
    function isDark(hex){ const n=parseInt(hex.slice(1),16); const r=(n>>16)&255,g=(n>>8)&255,b=n&255;
      return (0.299*r+0.587*g+0.114*b) > 176; }
  }
};
