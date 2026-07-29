/* ============================================================
   MOTOR-FEATURES — meta-laag (plan §4-D). Eén keer bouwen, overal inzetbaar.
   Volledig offline, dependency-vrij, veilig als localStorage ontbreekt.

   Bevat:
   - Store          : persistente voortgang (dagen, tags, spellen, can-do)
   - recordFinish() : de engine roept dit aan op het einde van elk spel
   - mountStreak()  : streak-kalender-widget (speel elke dag)
   - mountHeatmap() : fouten-/beheersings-heatmap per tag
   - mountCanDo()   : zelfscan met can-do-uitspraken (persistent)
   - Leitner        : spaced-repetition doosjes (1-5) voor een itempool
   ============================================================ */
(function(){
"use strict";
var KEY="motor:v1";

function today(){ try{ return new Date().toISOString().slice(0,10); }catch(e){ return "0000-00-00"; } }
function load(){
  try{ return JSON.parse(localStorage.getItem(KEY)) || {}; }catch(e){ return {}; }
}
function save(d){
  try{ localStorage.setItem(KEY, JSON.stringify(d)); return true; }catch(e){ return false; }
}
function base(d){
  d.days=d.days||{}; d.tags=d.tags||{}; d.games=d.games||{}; d.cando=d.cando||{}; d.leitner=d.leitner||{};
  return d;
}

/* --- de engine roept dit aan bij showResults --- */
function recordFinish(sum){
  try{
    sum=sum||{};
    var d=base(load()), t=today();
    var day=d.days[t]||(d.days[t]={plays:0,ok:0,total:0});
    day.plays++; day.ok+=(sum.ok|0); day.total+=(sum.total|0);
    var ts=sum.tagStats||{}, tl=sum.tagLabels||{};
    for(var tag in ts){ if(!ts.hasOwnProperty(tag)) continue;
      var g=d.tags[tag]||(d.tags[tag]={ok:0,bad:0});
      g.ok+=(ts[tag].ok|0); g.bad+=(ts[tag].bad|0);
      if(tl[tag]) g.label=tl[tag];
    }
    if(sum.id){
      var acc=sum.total? Math.round(sum.ok/sum.total*100):0;
      var ge=d.games[sum.id]||(d.games[sum.id]={plays:0,best:0,last:0});
      ge.plays++; ge.last=acc; if(acc>ge.best) ge.best=acc; if(sum.title) ge.title=sum.title;
    }
    save(d);
  }catch(e){}
}

/* --- streak: opeenvolgende dagen met minstens één spel, eindigend vandaag --- */
function streakCount(days){
  var n=0, dt;
  try{ dt=new Date(today()+"T00:00:00"); }catch(e){ return 0; }
  for(var i=0;i<400;i++){
    var key=dt.toISOString().slice(0,10);
    if(days[key] && days[key].plays>0){ n++; dt.setDate(dt.getDate()-1); }
    else if(i===0){ dt.setDate(dt.getDate()-1); } // vandaag nog niet gespeeld → kijk of gisteren telde
    else break;
  }
  return n;
}
function mountStreak(elm){
  if(!elm) return;
  var d=base(load()), days=d.days, n=streakCount(days);
  var html='<div class="mf-h"><span class="mf-fire">🔥</span> Racha: <b>'+n+'</b> día'+(n===1?"":"s")+
    ' <span class="mf-nl">· dagen na elkaar</span></div><div class="mf-cal">';
  var dt; try{ dt=new Date(today()+"T00:00:00"); }catch(e){ dt=null; }
  var cells=[];
  for(var i=13;i>=0;i--){
    var key="—", played=false, lbl="";
    if(dt){ var c=new Date(dt); c.setDate(c.getDate()-i); key=c.toISOString().slice(0,10);
      played=!!(days[key]&&days[key].plays>0); lbl=key.slice(5); }
    cells.push('<span class="mf-day'+(played?" on":"")+(i===0?" today":"")+'" title="'+key+'">'+
      '<i></i><em>'+lbl+'</em></span>');
  }
  html+=cells.join("")+'</div>';
  elm.innerHTML=html;
}

/* --- heatmap: beheersing per tag (groen=sterk, rood=zwak) --- */
function mountHeatmap(elm){
  if(!elm) return;
  var d=base(load()), tags=d.tags, keys=Object.keys(tags);
  if(!keys.length){ elm.innerHTML='<div class="mf-empty">Speel een spel om je beheersing per thema te zien.</div>'; return; }
  keys.sort(function(a,b){ return acc(tags[a])-acc(tags[b]); }); // zwakste eerst
  function acc(g){ var t=g.ok+g.bad; return t? g.ok/t : 0; }
  var rows=keys.slice(0,24).map(function(k){
    var g=tags[k], t=g.ok+g.bad, p=t?Math.round(g.ok/t*100):0;
    var col = p>=80?"#2E8E68": p>=55?"#E0A22F": "#C4402C";
    var name=(g.label||k).replace(/<[^>]+>/g," ").trim();
    return '<div class="mf-hrow"><span class="mf-hl">'+esc(name)+'</span>'+
      '<span class="mf-ht"><span class="mf-hf" style="width:'+p+'%;background:'+col+'"></span></span>'+
      '<span class="mf-hn">'+p+'%</span></div>';
  }).join("");
  elm.innerHTML='<div class="mf-h">Tu dominio por tema <span class="mf-nl">· beheersing per thema</span></div>'+rows;
}

/* --- can-do zelfscan (persistent) --- */
function mountCanDo(elm, items, poolId){
  if(!elm) return;
  items=items||[];
  poolId=poolId||"generic";
  var d=base(load()), store=d.cando;
  var html='<div class="mf-h">Puedo… <span class="mf-nl">· wat kan ik al?</span></div><ul class="mf-cando">';
  items.forEach(function(it,i){
    var id=poolId+":"+(it.id||i);
    var on=!!store[id];
    html+='<li class="mf-ci'+(on?" on":"")+'" data-id="'+esc(id)+'">'+
      '<button type="button" class="mf-cbtn" aria-pressed="'+on+'">'+
      '<span class="mf-cbox">'+(on?"✓":"")+'</span>'+
      '<span class="mf-clbl">'+esc(it.label||String(it))+'</span></button></li>';
  });
  html+='</ul>';
  elm.innerHTML=html;
  elm.querySelectorAll(".mf-ci").forEach(function(li){
    li.querySelector(".mf-cbtn").addEventListener("click",function(){
      var d2=base(load()), id=li.dataset.id, on=!d2.cando[id];
      d2.cando[id]=on; save(d2);
      li.classList.toggle("on",on);
      li.querySelector(".mf-cbox").textContent=on?"✓":"";
      li.querySelector(".mf-cbtn").setAttribute("aria-pressed",on);
    });
  });
}

/* --- Leitner-doosjes: spaced repetition (1=zwak … 5=beheerst) ---
   Herbruikbaar door een template/feeder: kies vaker uit lage doosjes.
   key = stabiele item-identiteit (bv. de stimulus-tekst). */
function Leitner(poolId){
  this.poolId=poolId||"pool";
  var d=base(load());
  this.boxes=(d.leitner[this.poolId]||(d.leitner[this.poolId]={}));
}
Leitner.prototype.box=function(k){ return this.boxes[k]||1; };
Leitner.prototype.promote=function(k){ this.boxes[k]=Math.min(5,(this.boxes[k]||1)+1); this._save(); };
Leitner.prototype.demote=function(k){ this.boxes[k]=1; this._save(); };
Leitner.prototype.register=function(k,ok){ ok?this.promote(k):this.demote(k); };
/* gewicht voor de adaptieve trekking: laag doosje = hoog gewicht (vaker) */
Leitner.prototype.weight=function(k){ return 6-this.box(k); };
Leitner.prototype._save=function(){ var d=base(load()); d.leitner[this.poolId]=this.boxes; save(d); };

function esc(s){ return String(s).replace(/[&<>]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;"}[c];}); }
function reset(){ try{ localStorage.removeItem(KEY); }catch(e){} }

window.MotorFeatures = {
  recordFinish: recordFinish,
  mountStreak: mountStreak,
  mountHeatmap: mountHeatmap,
  mountCanDo: mountCanDo,
  Leitner: Leitner,
  reset: reset,
  _load: load
};
})();
