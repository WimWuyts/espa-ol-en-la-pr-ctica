/* Genereert twee voorstel-catalogi (NT2 + Engels) voor de spaans-motor.
   Per thema een spelset verdeeld over de templates + arcade-rotatie, zodat de
   volledige leerlijn gedekt is (receptief→productief, vocab+grammatica+skills). */
import { writeFileSync } from "node:fs";

const ARCADE = ["tetris","belt","mole","bubble","snake","platform","tower","pinball"];
let arc = 0;
const nextArcade = () => ARCADE[(arc++) % ARCADE.length];

/* per thematype een vaste, gevarieerde spelset (naam-sjablonen).
   type: phon | func | vocab | gram  */
function gamesFor(t){
  const g=[];
  const A=nextArcade();
  if(t.type==="phon"){
    g.push(["tap", "Tik de juiste klank/klemtoon — "+t.name]);
    g.push(["classify", "Sorteer: "+t.focus]);
    g.push(["cloze", "Welke schrijfwijze? — "+t.name]);
    g.push(["speak", "Uitspraak-shadow — "+t.name]);
    g.push([A, "Arcade: "+t.focus]);
  } else if(t.type==="func"){
    g.push(["match", "Koppel situatie ↔ zin — "+t.name]);
    g.push(["order", "Zet de dialoog op volgorde — "+t.name]);
    g.push(["sim", "Mini-simulatie (chat) — "+t.name]);
    g.push(["speak", "Spraakbericht / rollenspel — "+t.name]);
    g.push(["type", "Schrijf de zin — "+t.name]);
  } else if(t.type==="vocab"){
    g.push(["match", "Woord ↔ betekenis — "+t.name]);
    g.push(["memory", "Memory — "+t.name]);
    g.push(["type", "Schrijf het woord — "+t.name]);
    g.push(["point", "Wijs aan op de scène — "+t.name]);
    g.push([A, "Arcade woordenschat — "+t.name]);
    g.push(["speak", "Zeg het — "+t.name]);
  } else { // gram
    g.push(["classify", "Sorteer de vorm/regel — "+t.name]);
    g.push(["cloze", "Vul de juiste vorm in — "+t.name]);
    g.push(["type", "Schrijf/vervoeg — "+t.name]);
    g.push(["order", "Bouw de zin — "+t.name]);
    g.push([A, "Arcade grammatica — "+t.name]);
    g.push(["speak", "Zeg de vorm hardop — "+t.name]);
  }
  return g.map(([tpl,title])=>({tpl,title,sub:t.focus}));
}

function build(themes, tag){
  const rows=[];
  arc=0;
  themes.forEach(t=>{
    gamesFor(t).forEach(gm=>{
      rows.push({course:tag, unit:t.level, theme:t.name, tpl:gm.tpl, title:gm.title, sub:gm.sub});
    });
  });
  return rows;
}

/* ===================== NT2 (Nederlands als tweede taal) ===================== */
const NL = [
  // --- A1 ---
  {level:"A1", type:"phon",  name:"Klanken & alfabet",         focus:"lange/korte klinker, ij/ei, ui/eu, g/ch"},
  {level:"A1", type:"func",  name:"Begroeten & voorstellen",   focus:"hallo, hoe heet je?, tot ziens"},
  {level:"A1", type:"vocab", name:"Persoonlijke gegevens",     focus:"naam, leeftijd, land, adres"},
  {level:"A1", type:"vocab", name:"Getallen & de klok",        focus:"1–100, hoe laat is het?"},
  {level:"A1", type:"gram",  name:"Lidwoorden de/het",         focus:"de-woord of het-woord"},
  {level:"A1", type:"gram",  name:"Meervoud (-en/-s)",         focus:"regelmatig + onregelmatig meervoud"},
  {level:"A1", type:"gram",  name:"Tegenwoordige tijd (regelmatig)", focus:"ik werk, jij werkt, hij werkt"},
  {level:"A1", type:"gram",  name:"zijn & hebben",             focus:"ben/bent/is · heb/hebt/heeft"},
  {level:"A1", type:"gram",  name:"Bezittelijk vnw",           focus:"mijn, jouw, zijn, haar, ons"},
  {level:"A1", type:"gram",  name:"Persoonlijk vnw",           focus:"ik/jij/hij · onderwerp"},
  {level:"A1", type:"vocab", name:"Familie",                   focus:"vader, moeder, broer, zus, oma"},
  {level:"A1", type:"vocab", name:"Eten & drinken",            focus:"brood, kaas, water, koffie"},
  {level:"A1", type:"vocab", name:"Kleuren & kleding",         focus:"rood, blauw · jas, broek, schoenen"},
  {level:"A1", type:"vocab", name:"Het huis & de kamers",      focus:"keuken, slaapkamer, badkamer"},
  {level:"A1", type:"vocab", name:"Dagen, maanden, seizoenen", focus:"maandag, januari, lente"},
  // --- A2 ---
  {level:"A2", type:"gram",  name:"Perfectum (hebben/zijn)",   focus:"ik heb gewerkt · ik ben gegaan"},
  {level:"A2", type:"gram",  name:"Voltooid deelwoord",        focus:"ge- + stam + -t/-d/-en"},
  {level:"A2", type:"gram",  name:"Scheidbare werkwoorden",    focus:"opstaan → ik sta op"},
  {level:"A2", type:"gram",  name:"Modale werkwoorden",        focus:"kunnen, moeten, willen, mogen"},
  {level:"A2", type:"gram",  name:"Woordvolgorde (inversie)",  focus:"morgen ga ik…"},
  {level:"A2", type:"gram",  name:"Bijzin: omdat/dat/als",     focus:"werkwoord naar het einde"},
  {level:"A2", type:"gram",  name:"want vs omdat (valstrik)",  focus:"hoofdzin vs bijzin-volgorde"},
  {level:"A2", type:"gram",  name:"Trappen van vergelijking",  focus:"groot–groter–grootst"},
  {level:"A2", type:"gram",  name:"Voorzetsels van plaats",    focus:"op, onder, naast, tussen, achter"},
  {level:"A2", type:"gram",  name:"Imperatief",                focus:"kijk!, wacht even, ga zitten"},
  {level:"A2", type:"gram",  name:"Het woordje «er»",          focus:"er is/zijn · er + voorzetsel"},
  {level:"A2", type:"vocab", name:"Beroepen & werk",           focus:"bakker, dokter, op kantoor"},
  {level:"A2", type:"func",  name:"Boodschappen & winkelen",   focus:"hoeveel kost het? · afrekenen"},
  {level:"A2", type:"vocab", name:"Reizen & vervoer",          focus:"trein, station, kaartje, overstappen"},
  {level:"A2", type:"vocab", name:"Gezondheid & lichaam",      focus:"hoofdpijn, arm, been · bij de dokter"},
  {level:"A2", type:"vocab", name:"Het weer",                  focus:"het regent, zonnig, graden"},
  // --- B1 ---
  {level:"B1", type:"gram",  name:"Imperfectum",               focus:"werkte / ging · verhaal in het verleden"},
  {level:"B1", type:"gram",  name:"Perfectum vs imperfectum",  focus:"wanneer welke verleden tijd?"},
  {level:"B1", type:"gram",  name:"Relatieve zinnen (die/dat)",focus:"de man die… · het boek dat…"},
  {level:"B1", type:"gram",  name:"Bijzinnen (hoewel/terwijl/zodat)", focus:"conjuncties + eindpositie werkwoord"},
  {level:"B1", type:"gram",  name:"Passief (worden)",          focus:"het wordt gemaakt"},
  {level:"B1", type:"gram",  name:"Conditioneel (zou)",        focus:"ik zou graag… · beleefdheid"},
  {level:"B1", type:"gram",  name:"Voorzetselvoorwerp",        focus:"houden van, wachten op, denken aan"},
  {level:"B1", type:"func",  name:"Formeel vs informeel (u/jij)", focus:"register kiezen"},
  {level:"B1", type:"gram",  name:"Connectoren & tekststructuur", focus:"daardoor, bovendien, ten slotte"},
  {level:"B1", type:"func",  name:"Mening & argumenteren",     focus:"ik vind dat… · ik ben het (niet) eens"},
];

/* ===================== Engels (voor Nederlandstaligen) ===================== */
const EN = [
  // --- A1 ---
  {level:"A1", type:"phon",  name:"Sounds & alphabet",         focus:"th, /æ/ vs /e/, silent letters, spelling"},
  {level:"A1", type:"func",  name:"Greetings & introductions", focus:"hello, what's your name?, goodbye"},
  {level:"A1", type:"vocab", name:"Personal information",      focus:"name, age, country, address"},
  {level:"A1", type:"vocab", name:"Numbers & the clock",       focus:"1–100, what time is it?"},
  {level:"A1", type:"gram",  name:"Articles a/an/the",         focus:"a car, an apple, the sun"},
  {level:"A1", type:"gram",  name:"Plurals (regular/irregular)", focus:"cats, boxes, children, feet"},
  {level:"A1", type:"gram",  name:"to be (am/is/are)",         focus:"I am, she is, they are"},
  {level:"A1", type:"gram",  name:"Present simple",            focus:"I play, he plays (3rd person -s)"},
  {level:"A1", type:"gram",  name:"have got",                  focus:"I've got, has she got…?"},
  {level:"A1", type:"gram",  name:"Subject pronouns & this/that", focus:"I/you/he · this, that, these, those"},
  {level:"A1", type:"vocab", name:"Family",                    focus:"father, mother, brother, sister"},
  {level:"A1", type:"vocab", name:"Food & drink",              focus:"bread, cheese, water, coffee"},
  {level:"A1", type:"vocab", name:"Colours & clothes",         focus:"red, blue · coat, trousers, shoes"},
  {level:"A1", type:"vocab", name:"The house & rooms",         focus:"kitchen, bedroom, bathroom"},
  {level:"A1", type:"vocab", name:"Days, months, seasons",     focus:"Monday, January, spring"},
  // --- A2 ---
  {level:"A2", type:"gram",  name:"Present continuous",        focus:"I am working right now"},
  {level:"A2", type:"gram",  name:"Present simple vs continuous", focus:"always vs now"},
  {level:"A2", type:"gram",  name:"Past simple: to be & regular", focus:"was/were · worked, played"},
  {level:"A2", type:"gram",  name:"Past simple: irregular verbs", focus:"go→went, see→saw, buy→bought"},
  {level:"A2", type:"gram",  name:"Comparatives & superlatives", focus:"bigger, the biggest, more…"},
  {level:"A2", type:"gram",  name:"can / could",               focus:"ability & permission"},
  {level:"A2", type:"gram",  name:"some / any / much / many",  focus:"countable vs uncountable"},
  {level:"A2", type:"gram",  name:"Prepositions (place/time)", focus:"in, on, at, under, next to"},
  {level:"A2", type:"gram",  name:"Question words",            focus:"who, what, where, when, why, how"},
  {level:"A2", type:"gram",  name:"going to (future)",         focus:"plans & predictions"},
  {level:"A2", type:"gram",  name:"Adverbs of frequency",      focus:"always, usually, never · position"},
  {level:"A2", type:"vocab", name:"Jobs & work",               focus:"nurse, engineer, at the office"},
  {level:"A2", type:"func",  name:"Shopping",                  focus:"how much is it? · paying"},
  {level:"A2", type:"vocab", name:"Travel & transport",        focus:"train, station, ticket, change"},
  {level:"A2", type:"vocab", name:"Health & body",             focus:"headache, arm, leg · at the doctor's"},
  {level:"A2", type:"vocab", name:"The weather",               focus:"it's raining, sunny, degrees"},
  // --- B1 ---
  {level:"B1", type:"gram",  name:"Present perfect",           focus:"I have seen · ever/never/just/yet"},
  {level:"B1", type:"gram",  name:"Present perfect vs past simple", focus:"finished vs unfinished time"},
  {level:"B1", type:"gram",  name:"Past continuous",           focus:"I was working when…"},
  {level:"B1", type:"gram",  name:"will & first conditional",  focus:"if + present, will + infinitive"},
  {level:"B1", type:"gram",  name:"Second conditional",        focus:"if I were… I would…"},
  {level:"B1", type:"gram",  name:"Relative clauses",          focus:"who, which, that, whose"},
  {level:"B1", type:"gram",  name:"Passive voice",             focus:"it is made · it was built"},
  {level:"B1", type:"gram",  name:"Modals: should/must/have to", focus:"advice & obligation"},
  {level:"B1", type:"gram",  name:"Phrasal verbs",             focus:"get up, look for, turn off"},
  {level:"B1", type:"func",  name:"Opinions & connectors",     focus:"I think that… · however, although"},
  // --- B2 ---
  {level:"B2", type:"gram",  name:"Perfect tenses (all)",      focus:"past/future perfect contrast"},
  {level:"B2", type:"gram",  name:"Third & mixed conditionals",focus:"if I had known…"},
  {level:"B2", type:"gram",  name:"Reported speech",           focus:"he said (that) he was…"},
  {level:"B2", type:"vocab", name:"Collocations & word formation", focus:"make/do · -ment, -tion, un-"},
  {level:"B2", type:"func",  name:"Formal vs informal register", focus:"emails, requests, tone"},
];

const nl = build(NL, "NT2");
const en = build(EN, "EN");
writeFileSync(process.env.SCRATCH+"/nl_catalog.json", JSON.stringify(nl));
writeFileSync(process.env.SCRATCH+"/en_catalog.json", JSON.stringify(en));
console.log("NT2:", nl.length, "spellen over", NL.length, "thema's");
console.log("EN :", en.length, "spellen over", EN.length, "thema's");
