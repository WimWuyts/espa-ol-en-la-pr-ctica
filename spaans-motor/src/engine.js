/* ============================================================
   MOTOR — gedeelde kern. Sjabloon-onafhankelijk.
   Een sjabloon rendert ALLEEN het speelveld en meldt per beurt
   goed/fout via api.judge(). De motor doet de rest:
   score, streak, niveau, adaptieve keuze, foutenlog, resultaten,
   geluid, instellingen, toegankelijkheid.
   ============================================================ */
(function(){
"use strict";

const CALM = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

/* ---------- geluid ---------- */
function makeAudio(on){
  let AC=null;
  function ac(){ if(!AC && on){ try{AC=new (window.AudioContext||window.webkitAudioContext)();}catch(e){}} return AC; }
  function beep(f,d,type,vol,to){ if(!on)return; const a=ac(); if(!a)return;
    const o=a.createOscillator(),g=a.createGain(); o.type=type||"triangle";
    o.frequency.setValueAtTime(f,a.currentTime);
    if(to) o.frequency.exponentialRampToValueAtTime(to,a.currentTime+d);
    g.gain.setValueAtTime(vol||.16,a.currentTime);
    g.gain.exponentialRampToValueAtTime(.0008,a.currentTime+d);
    o.connect(g);g.connect(a.destination);o.start();o.stop(a.currentTime+d); }
  function noise(d,vol){ if(!on)return; const a=ac(); if(!a)return;
    const n=Math.floor(a.sampleRate*d),buf=a.createBuffer(1,n,a.sampleRate),dt=buf.getChannelData(0);
    for(let i=0;i<n;i++)dt[i]=(Math.random()*2-1)*(1-i/n);
    const s=a.createBufferSource();s.buffer=buf;
    const fl=a.createBiquadFilter();fl.type="lowpass";fl.frequency.value=900;
    const g=a.createGain();g.gain.value=vol||.18;
    s.connect(fl);fl.connect(g);g.connect(a.destination);s.start(); }
  return {
    unlock:ac,
    setOn(v){on=v;},
    ok(){ beep(740,.08,"triangle",.16); setTimeout(()=>beep(1108,.13,"triangle",.14),60); },
    bad(){ noise(.22,.24); beep(150,.28,"sawtooth",.12,70); },
    move(){ beep(620,.04,"square",.05); },
    win(){ [523,659,784,1046,1319].forEach((f,i)=>setTimeout(()=>beep(f,.16,"triangle",.15),i*62)); }
  };
}

/* ---------- helpers ---------- */
function el(tag,cls,html){ const e=document.createElement(tag); if(cls)e.className=cls; if(html!=null)e.innerHTML=html; return e; }
function shade(hex,f){ const n=parseInt(hex.slice(1),16);
  const r=Math.max(0,Math.min(255,Math.round(((n>>16)&255)*f)));
  const g=Math.max(0,Math.min(255,Math.round(((n>>8)&255)*f)));
  const b=Math.max(0,Math.min(255,Math.round((n&255)*f)));
  return "rgb("+r+","+g+","+b+")"; }

/* ---------- adaptieve toevoer ----------
   Trekt K kandidaten en kiest die met de zwakste tag. Werkt zowel voor
   generatoren (source.make) als voor vaste itemlijsten (source.items). */
function makeFeeder(source, tagStats){
  const draw = source.make ? source.make
             : () => source.items[(Math.random()*source.items.length)|0];
  return function next(){
    let best=null, bestScore=Infinity;
    for(let i=0;i<4;i++){
      const it = draw();
      const st = tagStats[it.tag] || {ok:0,bad:0};
      const acc = (st.ok+1)/(st.ok+st.bad+2);      // laag = zwak → voorrang
      const score = acc + Math.random()*0.5;
      if(score<bestScore){ bestScore=score; best=it; }
    }
    return best;
  };
}

/* ============================================================
   MOUNT
   ============================================================ */
function mount(app, cfg){
  cfg.options = cfg.options || {};
  const audio = makeAudio(cfg.options.audio !== false);

  /* ---- schil bouwen ---- */
  app.innerHTML = "";
  const header = el("header","mt");
  const titleWrap = el("div");
  titleWrap.appendChild(el("h1",null, esc(cfg.title||"Oefening")));
  if(cfg.subtitle) titleWrap.appendChild(el("p","tag", esc(cfg.subtitle)));
  header.appendChild(titleWrap);
  header.appendChild(el("div","sp"));
  const bAgain = el("button","mt-btn","Opnieuw"); bAgain.type="button";
  header.appendChild(bAgain);
  /* confidence-betting (opt-in): ×2 punten én ×2 straf wanneer je zeker bent */
  let bBet=null;
  if(cfg.options.confidence){
    bBet=el("button","mt-btn bet","🎲 ×1"); bBet.type="button";
    bBet.title="Apuesta: dobla los puntos… y el riesgo";
    header.appendChild(bBet);
  }
  app.appendChild(header);

  const wrap = el("div","mt-wrap");
  const fieldCol = el("div");
  const field = el("div","mt-field");
  fieldCol.appendChild(field);
  wrap.appendChild(fieldCol);

  const panel = el("div","mt-panel");
  const sScore = statBox(panel,"Punten","0");
  const sStreak = statBox(panel,"Reeks","0");
  const sProg = statBox(panel,"Voortgang","–");
  wrap.appendChild(panel);
  app.appendChild(wrap);

  /* ---- resultatenoverlay ---- */
  const ov = el("div","mt-ov");
  ov.innerHTML =
    '<div class="mt-sheet"><h2>Klaar</h2><p class="sub" id="mtRSub"></p>'+
    '<div class="mt-rgrid">'+
      '<div class="mt-rcell"><div class="rk">Punten</div><div class="rv" id="mtRScore">0</div></div>'+
      '<div class="mt-rcell"><div class="rk">Juist</div><div class="rv" id="mtRAcc">–</div></div>'+
      '<div class="mt-rcell"><div class="rk">Beste reeks</div><div class="rv" id="mtRBest">0</div></div>'+
    '</div>'+
    '<div class="mt-grp" id="mtRBarsWrap"><label id="mtRBarsLbl">Per categorie</label><div id="mtRBars"></div></div>'+
    '<div class="mt-grp" id="mtRMisWrap"><label>Waar het misging</label><ul class="mt-mis" id="mtRMis"></ul></div>'+
    '<button class="mt-go" id="mtRAgain" type="button">Opnieuw</button></div>';
  app.appendChild(ov);

  /* ---- staat ---- */
  const S = { score:0, streak:0, best:0, level:1, ok:0, total:0, tagStats:{}, log:[], done:0, target:0, bet:1 };
  if(bBet){ bBet.addEventListener("click", ()=>{
    S.bet = S.bet===1 ? 2 : 1;
    bBet.textContent = "🎲 ×"+S.bet; bBet.classList.toggle("on", S.bet===2);
    audio.move();
  }); }

  function statBox(parent,k,v){
    const b=el("div","mt-stat"); b.innerHTML='<span class="k">'+k+'</span><span class="v">'+v+'</span>';
    parent.appendChild(b); return b.querySelector(".v");
  }
  function esc(s){ return String(s).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])); }

  function hud(){
    sScore.textContent=S.score;
    sStreak.textContent=S.streak; sStreak.classList.toggle("hot",S.streak>=5);
    sProg.textContent = S.target ? (S.done+"/"+S.target) : "–";
  }

  /* label voor een tag (categorie of persoon) t.b.v. resultaten */
  function tagLabel(tag){
    if(cfg._tagLabel){ const l=cfg._tagLabel(tag); if(l) return l; }
    if(cfg.classify && cfg.classify.categories){
      const c=cfg.classify.categories.find(x=>x.id===tag); if(c) return c.label.replace(/<[^>]+>/g," ").trim();
    }
    return tag;
  }

  /* ---- API voor het sjabloon ---- */
  const feeder = cfg._source ? makeFeeder(cfg._source, S.tagStats) : null;

  const api = {
    root: field,
    config: cfg,
    calm: CALM,
    sfx: audio,
    el, shade,
    categories: (cfg.classify && cfg.classify.categories) || [],

    /* volgende stimulus (adaptief) — enkel voor stimulus→antwoord-sjablonen */
    next(){ return feeder ? feeder() : null; },

    /* aantal beurten instellen (voor voortgang + einde) */
    setTarget(n){ S.target=n; hud(); },
    tick(){ S.done++; hud(); },

    /* losse puntenbonus (bv. tetris-lijn); telt niet mee in juist% */
    bonus(n){ S.score += (n|0); hud(); },

    /* kern: één beoordeling. meta = {tag, stimulus, chosen, correct[], sub} */
    judge(ok, meta){
      meta = meta || {};
      S.total++;
      const tag = meta.tag || "_";
      const st = S.tagStats[tag] || (S.tagStats[tag]={ok:0,bad:0});
      const bet = S.bet||1;
      if(ok){
        S.ok++; st.ok++; S.streak++; if(S.streak>S.best)S.best=S.streak;
        S.score += (10 + Math.min(50,S.streak*3)) * bet;
        if(S.ok % 10 === 0) S.level++;
        audio.ok();
      }else{
        st.bad++; S.streak=0; S.score=Math.max(0,S.score-5*bet);
        audio.bad();
        if(meta.stimulus){
          S.log.push({ stimulus:meta.stimulus, sub:meta.sub||"",
            juist:(meta.correct||[]).map(tagLabel).join(" / "),
            gekozen: meta.chosen!=null ? tagLabel(meta.chosen) : "" });
        }
      }
      hud();
      return { ok, streak:S.streak };
    },

    finish(){ showResults(); }
  };

  function showResults(){
    const acc = S.total ? Math.round(S.ok/S.total*100) : 0;
    ov.querySelector("#mtRScore").textContent=S.score;
    ov.querySelector("#mtRAcc").textContent=acc+"%";
    ov.querySelector("#mtRBest").textContent=S.best;
    ov.querySelector("#mtRSub").textContent =
      acc>=90 ? "Strak werk." : acc>=70 ? "Degelijk." : "Nog eens oefenen loont.";

    /* balken per tag (alleen tonen als er >1 tag is) */
    const tags = Object.keys(S.tagStats);
    const barsWrap = ov.querySelector("#mtRBarsWrap");
    const bars = ov.querySelector("#mtRBars"); bars.innerHTML="";
    if(tags.length>1){
      barsWrap.style.display="";
      const palette=["#C4402C","#E0A22F","#2E8E68","#3D74D6","#8B5E9E","#6E6249"];
      tags.forEach((t,i)=>{
        const s=S.tagStats[t], tot=s.ok+s.bad, pct=tot?Math.round(s.ok/tot*100):0;
        const row=el("div","mt-bar");
        row.innerHTML='<span class="bl">'+esc(tagLabel(t))+'</span>'+
          '<span class="bt"><span class="bf" style="width:'+pct+'%;background:'+palette[i%palette.length]+'"></span></span>'+
          '<span class="bn">'+pct+'%</span>';
        bars.appendChild(row);
      });
    } else barsWrap.style.display="none";

    /* laatste fouten */
    const misWrap=ov.querySelector("#mtRMisWrap");
    const ul=ov.querySelector("#mtRMis"); ul.innerHTML="";
    const last=S.log.slice(-8).reverse();
    misWrap.style.display = last.length ? "" : "none";
    last.forEach(m=>{
      const li=el("li");
      li.innerHTML="<b>"+esc(m.stimulus)+"</b> <span class='ok'>"+esc(m.juist)+"</span>"+
        (m.gekozen?" <em>jij: "+esc(m.gekozen)+"</em>":"")+
        (m.sub?" <span style='color:#8A7F66;font-size:12px'>("+esc(m.sub)+")</span>":"");
      ul.appendChild(li);
    });
    if(acc>=90) audio.win();
    ov.classList.add("on");

    /* meta-laag: voortgang persisteren (streak · heatmap · spellen) */
    if(window.MotorFeatures && window.MotorFeatures.recordFinish){
      const tagLabels={}; Object.keys(S.tagStats).forEach(t=>{ tagLabels[t]=tagLabel(t); });
      window.MotorFeatures.recordFinish({
        id: cfg.id,
        title: String(cfg.title||"").replace(/<[^>]+>/g,"").trim(),
        ok: S.ok, total: S.total, tagStats: S.tagStats, tagLabels: tagLabels
      });
    }
  }

  /* ---- start / herstart ---- */
  function reset(){
    S.score=0;S.streak=0;S.best=0;S.level=1;S.ok=0;S.total=0;S.tagStats={};S.log=[];S.done=0;S.target=0;
    if(api._cleanup){ api._cleanup(); api._cleanup=null; }
    ov.classList.remove("on"); field.innerHTML=""; hud();
    const tpl = window.MotorTemplates && window.MotorTemplates[cfg.template];
    if(!tpl){ field.innerHTML="<p style='color:#C4402C'>Onbekend sjabloon: "+esc(cfg.template)+"</p>"; return; }
    tpl.init(api);
  }
  bAgain.addEventListener("click", ()=>{ audio.unlock(); reset(); });
  ov.querySelector("#mtRAgain").addEventListener("click", ()=>{ audio.unlock(); reset(); });

  /* eerste tik ontgrendelt geluid op mobiel */
  app.addEventListener("pointerdown", ()=>audio.unlock(), {once:true});

  reset();
}

window.Motor = { mount };
})();
