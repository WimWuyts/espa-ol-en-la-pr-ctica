// Rekent de presente-vormen van alle motor-werkwoorden voor (hergebruikt de motor-engine,
// dus 'nagerekend', geen giswerk) → 03-build/web/verbos_es.json.
// Run: node 03-build/web/extract_verbos.mjs
import fs from 'fs';
global.window = {};
const R = '/home/user/espa-ol-en-la-pr-ctica';
eval(fs.readFileSync(R+'/spaans-motor/src/data.verbos.es.js','utf8'));
eval(fs.readFileSync(R+'/spaans-motor/src/data.verbos.extra.js','utf8'));
eval(fs.readFileSync(R+'/spaans-motor/src/generators.js','utf8'));
// base eerst, dan extra → dedup op infinitief (base wint bij botsing)
const verbs = [].concat(window.MotorData.esVerbos, window.MotorData.esVerbosExtra||[]);
const CLS = {reg:'regelmatig',ie:'klankwissel e→ie',ue:'klankwissel o→ue',i:'klankwissel e→i',uue:'klankwissel u→ue',irr:'onregelmatig'};
const seen = new Set(), out = [];
let dupes = 0;
for (const v of verbs) {
  if (seen.has(v.i)) { dupes++; continue; } seen.add(v.i);
  out.push({inf:v.i, nl:v.n, type:CLS[window.MotorGen.verboClase(v)]||'onregelmatig', forms:window.MotorGen.verboConjugar(v)});
}
out.sort((a,b)=>a.inf.localeCompare(b.inf,'es'));
fs.writeFileSync(R+'/03-build/web/verbos_es.json', JSON.stringify(out));
console.log('geschreven:', out.length, 'werkwoorden → 03-build/web/verbos_es.json ('+dupes+' dubbele infinitieven overgeslagen)');
