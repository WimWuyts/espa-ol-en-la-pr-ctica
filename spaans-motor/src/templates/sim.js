/* Simulatie / vrije productie (sim): een communicatieve mini-taak (chat, perfil,
   presentación). De leerling BOUWT een boodschap — tikt bouwsteen-chips of typt
   zelf — en laat ze nakijken met een ZACHTE check: zijn de verplichte bouwstenen
   aanwezig? (keyword/structuur, nooit vrije spelling strikt afkeuren.) Toont daarna
   een modelantwoord. Realiseert het «vrij produceren»-uiteinde van de ladder (§14).
   Content: sim.rounds:[{scenario, tag, sub?, frame?, need:[{re,label}], bank:[...], model, min?}]. */
window.MotorTemplates = window.MotorTemplates || {};
window.MotorTemplates.sim = {
  init(api){
    const cfg = api.config, el = api.el;
    const conf = cfg.sim || {};
    const rounds = shuffle((conf.rounds || []).slice());
    api.setTarget(rounds.length);

    const root = api.root; root.innerHTML = "";
    const card = el("div","sm-card");
    card.innerHTML =
      '<div class="sm-eye" id="smEye"></div>'+
      '<div class="sm-scn" id="smScn"></div>'+
      '<div class="sm-need" id="smNeed"></div>'+
      '<textarea class="sm-ta" id="smTa" rows="3" placeholder="Escribe aquí… (tik een chip of typ zelf)"></textarea>'+
      '<div class="sm-bank" id="smBank"></div>'+
      '<div class="sm-row"><button class="sm-btn" id="smCheck" type="button">Comprobar</button>'+
      '<button class="sm-btn ghost" id="smClear" type="button">Borrar</button></div>'+
      '<div class="sm-fb" id="smFb">&nbsp;</div>'+
      '<div class="sm-model" id="smModel"></div>';
    root.appendChild(card);

    const eyeEl=card.querySelector("#smEye"), scnEl=card.querySelector("#smScn"),
      needEl=card.querySelector("#smNeed"), ta=card.querySelector("#smTa"),
      bankEl=card.querySelector("#smBank"), fbEl=card.querySelector("#smFb"),
      modelEl=card.querySelector("#smModel"),
      bCheck=card.querySelector("#smCheck"), bClear=card.querySelector("#smClear");

    let ri=0, round=null, locked=false;

    function norm(s){ return String(s).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g,""); }

    function load(){
      if(ri >= rounds.length){ api.finish(); return; }
      round = rounds[ri]; locked=false;
      eyeEl.textContent = conf.prompt || "Tarea comunicativa";
      scnEl.innerHTML = esc(round.scenario||"") + (round.sub?'<span class="sm-hint"> · '+esc(round.sub)+'</span>':"");
      ta.value = round.frame ? round.frame : "";
      fbEl.textContent=" "; fbEl.className="sm-fb"; modelEl.style.display="none"; modelEl.innerHTML="";
      card.classList.remove("good","bad");
      // verplichte bouwstenen als checklist
      needEl.innerHTML = (round.need||[]).map((n,i)=>'<span class="sm-chk" data-i="'+i+'">◻ '+esc(n.label)+'</span>').join("");
      // woordbank
      bankEl.innerHTML="";
      (round.bank||[]).forEach(w=>{
        const b=el("button","sm-chip", esc(w)); b.type="button";
        b.addEventListener("click",()=>{ if(locked)return; ta.value=(ta.value+(ta.value&&!/\s$/.test(ta.value)?" ":"")+w+" "); ta.focus(); api.sfx.move(); });
        bankEl.appendChild(b);
      });
      ta.focus();
    }
    function markChecklist(txt){
      let hitAll=true;
      (round.need||[]).forEach((n,i)=>{
        const re = new RegExp(norm(n.re));
        const ok = re.test(norm(txt));
        if(!ok) hitAll=false;
        const c=needEl.querySelector('.sm-chk[data-i="'+i+'"]');
        if(c){ c.classList.toggle("ok",ok); c.textContent=(ok?"☑ ":"◻ ")+n.label; }
      });
      return hitAll;
    }
    function check(){
      if(locked) return;
      const txt=ta.value.trim();
      const words = txt ? txt.split(/\s+/).length : 0;
      const minW = round.min || 6;
      const hitAll = markChecklist(txt);
      const ok = hitAll && words>=minW;
      locked=true;
      api.judge(ok,{tag:round.tag||"sim", stimulus:round.scenario||"",
        chosen: ok?"":"(faltan bloques)", correct:[(round.need||[]).map(n=>n.label).join(", ")], sub:round.sub});
      if(ok){ card.classList.add("good"); fbEl.textContent="¡bien! Tienes todos los bloques."; fbEl.className="sm-fb g"; api.sfx.ok(); }
      else { card.classList.add("bad");
        fbEl.innerHTML = words<minW ? "→ un poco más largo (mín. "+minW+" palabras)" : "→ faltan bloques (mira la lista ◻)";
        fbEl.className="sm-fb b"; api.sfx.bad(); }
      if(round.model){ modelEl.style.display="block"; modelEl.innerHTML='<b>Modelo:</b> '+esc(round.model); }
      ri++; api.tick();
      setTimeout(()=>{ bCheck.textContent="Siguiente"; bCheck.onclick=()=>{ bCheck.textContent="Comprobar"; bCheck.onclick=check; load(); }; }, 50);
    }
    bCheck.onclick=check;
    bClear.onclick=()=>{ if(!locked) ta.value=""; ta.focus(); };
    ta.addEventListener("input",()=>{ if(!locked) markChecklist(ta.value); });

    load();
    function esc(s){ return String(s).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])); }
    function shuffle(a){ for(let i=a.length-1;i>0;i--){const j=(Math.random()*(i+1))|0;[a[i],a[j]]=[a[j],a[i]];} return a; }
  }
};
