/* Generatoren — leveren geverifieerde items aan de sjablonen.
   Elke generator geeft { make(): item, tagLabel(tag): string }.
   Een item = { stimulus, answer, tag, sub }.
   answer mag een array zijn (meerdere juiste categorieën, bv. yo=él bij imperfecto).
   Taalkundige juistheid komt HIER vandaan, nooit uit vrije generatie. */
window.MotorGen = window.MotorGen || {};

/* ---------- vervoegingsmotor (nagerekend) ---------- */
(function(){
  function stripAcc(s){ return s.normalize("NFD").replace(/[\u0300-\u036f]/g,""); }
  const vtype = inf => stripAcc(inf.slice(-2));
  const vstem = inf => inf.slice(0,-2);
  const END = {
    pres:{ar:["o","as","a","amos","áis","an"],er:["o","es","e","emos","éis","en"],ir:["o","es","e","imos","ís","en"]},
    indef:{ar:["é","aste","ó","amos","asteis","aron"],er:["í","iste","ió","imos","isteis","ieron"],ir:["í","iste","ió","imos","isteis","ieron"]},
    imperf:{ar:["aba","abas","aba","ábamos","abais","aban"],er:["ía","ías","ía","íamos","íais","ían"],ir:["ía","ías","ía","íamos","íais","ían"]},
    fut:["é","ás","á","emos","éis","án"],
    cond:["ía","ías","ía","íamos","íais","ían"]
  };
  const HABER=["he","has","ha","hemos","habéis","han"];
  function participio(v){
    if(v.part) return v.part;
    const t=vtype(v.i),s=vstem(v.i);
    if(t==="ar") return s+"ado";
    return /[aeo]$/.test(s)?s+"ído":s+"ido";
  }
  function conjugate(v,tense){
    if(tense==="perf"){const p=participio(v);return HABER.map(h=>h+" "+p);}
    if(v[tense]) return v[tense].slice();
    const t=vtype(v.i),s=vstem(v.i);
    if(tense==="fut"||tense==="cond"){const base=v.fs||v.i;return END[tense].map(e=>base+e);}
    const out=END[tense][t].map(e=>s+e);
    if(tense==="indef"&&t==="ar"){
      if(/c$/.test(s)) out[0]=s.slice(0,-1)+"qué";
      else if(/g$/.test(s)) out[0]=s+"ué";
      else if(/z$/.test(s)) out[0]=s.slice(0,-1)+"cé";
    }
    return out;
  }
  function isIrregular(v,tense){
    if(tense==="perf") return !!v.part;
    if(tense==="fut"||tense==="cond") return !!v.fs && !v.fsReg;
    return !!v[tense];
  }
  const PERS=["yo","tu","el","nos","vos","ellos"];
  const IDX={yo:0,tu:1,el:2,nos:3,vos:4,ellos:5};
  const MIX=["pres","indef","imperf","fut"];

  window.MotorGen.conjugation = function(opts){
    opts = opts || {};
    const persons = (opts.persons||PERS).map(p=>IDX[p]);
    const verbs = window.MotorData.es.verbs.filter(v=>{
      const t = opts.tense==="mix" ? "pres" : opts.tense;
      const irr = isIrregular(v,t);
      if(opts.pool==="reg") return !irr;
      if(opts.pool==="irr") return irr;
      return true;
    });
    function make(){
      let tense = opts.tense==="mix" ? MIX[(Math.random()*MIX.length)|0] : opts.tense;
      let pool = verbs;
      if(!pool.length){ pool = window.MotorData.es.verbs; }
      const v = pool[(Math.random()*pool.length)|0];
      const forms = conjugate(v,tense);
      const pick = persons[(Math.random()*persons.length)|0];
      const form = forms[pick];
      // alle personen (binnen de actieve set) met dezelfde vorm = allemaal juist
      const ans = [];
      persons.forEach(pi=>{ if(forms[pi]===form) ans.push(PERS[pi]); });
      return { stimulus:form, answer:ans, tag:PERS[pick], sub:v.i+" · "+v.n };
    }
    return { make, tagLabel:t=>t };
  };
})();

/* ---------- geslacht van zelfstandige naamwoorden ---------- */
window.MotorGen.gender = function(opts){
  opts = opts || {};
  const nouns = window.MotorData.es.nouns.filter(x=> opts.trapsOnly ? x.trap : true);
  function make(){
    const x = nouns[(Math.random()*nouns.length)|0];
    return { stimulus:"___ "+x.w, answer:x.g, tag:x.g, sub:x.n };
  }
  return { make, tagLabel:t=> t==="m" ? "masculino" : "femenino" };
};

/* ---------- werkwoordengenerator (presente) ----------
   Voedt alle tien de spelideeën. Modi:
     "person" → welke persoon hoort bij deze vorm  (classify / tetris)
     "clase"  → welke presente-klasse heeft dit werkwoord (classify / tetris)
   opts.classes filtert de werkwoorden (bv. ["ie","ue","i","uue"] = enkel cambio vocálico).
   Presente wordt nagerekend; expliciete onregelmatige vormen krijgen voorrang. */
(function(){
  const PERS=["yo","tu","el","nos","vos","ellos"];
  const IDX={yo:0,tu:1,el:2,nos:3,vos:4,ellos:5};
  function repl(s,f,t){ const i=s.lastIndexOf(f); return i<0?s:s.slice(0,i)+t+s.slice(i+1); }
  function strongStem(stem,c){
    if(!c||c==="reg") return stem;
    if(c==="ie") return repl(stem,"e","ie");
    if(c==="ue") return repl(stem,"o","ue");
    if(c==="i")  return repl(stem,"e","i");
    if(c==="uue")return repl(stem,"u","ue");
    if(c==="ie2")return repl(stem,"i","ie");
    if(c==="hue")return repl(stem,"o","hue");
    return stem;
  }
  function presente(v){
    if(v.pres) return v.pres.slice();
    const t=v.i.slice(-2), stem=v.i.slice(0,-2);
    const E = t==="ar"?["o","as","a","amos","áis","an"]
            : t==="er"?["o","es","e","emos","éis","en"]
            :          ["o","es","e","imos","ís","en"];
    const strong=strongStem(stem,v.c);
    const uir=v.o==="uir";
    const f=[];
    for(let p=0;p<6;p++){
      const stressed=!(p===3||p===4);
      let s = stressed?strong:stem;
      if(uir) s = stressed? stem+"y" : stem;
      f.push(s+E[p]);
    }
    // yo-vorm
    if(v.yo){ f[0]=v.yo; }
    else if(v.o){
      const b=(v.c&&v.c!=="reg")?strong:stem;
      if(v.o==="ger")  f[0]=b.replace(/g$/,"j")+"o";
      else if(v.o==="zco") f[0]=b.replace(/c$/,"zc")+"o";
      else if(v.o==="zo")  f[0]=b.replace(/c$/,"z")+"o";
      else if(v.o==="guir")f[0]=b.replace(/gu$/,"g")+"o";
      /* uir: yo is al 'stem+y+o' uit de lus */
    }
    return f;
  }
  function clase(v){
    if(v.c==="ie") return "ie";
    if(v.c==="ue") return "ue";
    if(v.c==="i")  return "i";
    if(v.c==="uue")return "uue";
    if(v.pres||v.yo||v.irr||v.c==="ie2"||v.c==="hue") return "irr";
    return "reg";
  }

  function pool(opts){
    const all=window.MotorData.esVerbos;
    if(opts && opts.classes && opts.classes.length){
      const set=new Set(opts.classes);
      return all.filter(v=>set.has(clase(v)));
    }
    return all;
  }

  window.MotorGen.verbo = function(opts){
    opts=opts||{}; const mode=opts.mode||"person";
    const verbs=pool(opts);
    const persons=(opts.persons||PERS).map(p=>IDX[p]);

    function makePerson(){
      const v=verbs[(Math.random()*verbs.length)|0];
      const forms=presente(v);
      const pick=persons[(Math.random()*persons.length)|0];
      const form=forms[pick];
      const ans=[]; persons.forEach(pi=>{ if(forms[pi]===form) ans.push(PERS[pi]); });
      return { stimulus:form, answer:ans, tag:PERS[pick], sub:v.i+" · "+v.n };
    }
    function makeClase(){
      const v=verbs[(Math.random()*verbs.length)|0];
      const k=clase(v);
      return { stimulus:v.i, answer:k, tag:k, sub:v.n };
    }
    const CL={reg:"regular",ie:"e→ie",ue:"o→ue",i:"e→i",uue:"u→ue",irr:"onregelmatig"};
    return {
      make: mode==="clase"?makeClase:makePerson,
      tagLabel: t => mode==="clase" ? (CL[t]||t) : t
    };
  };

  /* helpers voor toekomstige sjablonen (intruso, paradigma, cloze, memoria) */
  window.MotorGen.verboConjugar = presente;
  window.MotorGen.verboClase = clase;
})();
