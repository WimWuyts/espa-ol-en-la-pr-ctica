// C4 · Unidad 1 «Presentaciones» — Word (.docx) via docx-js.
// Bladspiegel (CLAUDE.md §13): elke hoofdsectie nieuwe pagina, gevarieerde composities,
// efficiënt gevulde pagina's (geen leeg omkaderd blad), echte antwoordruimte, adem.
const fs = require("fs");
const D = require("docx");
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType,
        BorderStyle, ShadingType, AlignmentType, PageBreak, HeightRule, VerticalAlign } = D;

// ---- huisstijl (C4-rood) ----
const RED="D64550", REDD="A8323B", TINT="FBEAEC", CREMA="F6F1EC", INK="20242E",
      MUT="6A6E78", LINE="E7E1DF", BLUE="2563EB", ORA="EA7317", OKG="1E9E74", WARN="DC2626", WHITE="FFFFFF";
const HEAD="Bricolage Grotesque", BODY="Inter";
const TW=9740;
const NB={ style:BorderStyle.NONE, size:0, color:"FFFFFF" };
const noBorders={ top:NB,bottom:NB,left:NB,right:NB,insideHorizontal:NB,insideVertical:NB };

// ---- helpers ----
const r=(t,o={})=>new TextRun({ text:t, font:o.font||BODY, size:o.size||21, bold:!!o.bold,
  italics:!!o.italics, color:o.color||INK, break:o.break });
const p=(children,o={})=>new Paragraph({ children:Array.isArray(children)?children:[children],
  alignment:o.align, spacing:{ before:o.before!=null?o.before:0, after:o.after!=null?o.after:80, line:o.line },
  shading:o.fill?{ type:ShadingType.CLEAR, color:"auto", fill:o.fill }:undefined,
  border:o.border, keepNext:o.keepNext, indent:o.indent });
const spacer=(h=120)=>new Paragraph({ children:[], spacing:{ after:h } });
const pageBreak=()=>new Paragraph({ children:[new PageBreak()] });

const se=(t)=>p([r(t,{size:16,bold:true,color:MUT})],{after:20,keepNext:true});
const H2=(t)=>p([r(t,{font:HEAD,size:30,bold:true,color:REDD})],
  {after:120,keepNext:true,border:{bottom:{style:BorderStyle.SINGLE,size:18,color:TINT,space:3}}});
const H3=(t)=>p([r(t,{font:HEAD,size:24,bold:true,color:INK})],{before:120,after:60,keepNext:true});

const bd=(c=LINE,s=4)=>({style:BorderStyle.SINGLE,size:s,color:c});
const cellBorders=(c=LINE)=>({top:bd(c),bottom:bd(c),left:bd(c),right:bd(c)});
function cell(children,w,o={}){
  return new TableCell({ width:{size:w,type:WidthType.DXA},
    children:Array.isArray(children)?children:[children],
    shading:o.fill?{type:ShadingType.CLEAR,color:"auto",fill:o.fill}:undefined,
    verticalAlign:o.valign||VerticalAlign.CENTER,
    borders:o.borders||cellBorders(o.bc||LINE),
    margins:{top:o.mt!=null?o.mt:40,bottom:o.mb!=null?o.mb:40,left:90,right:90} });
}
function table(rows,widths){ return new Table({ columnWidths:widths, width:{size:TW,type:WidthType.DXA}, rows }); }
const tcp=(t,o={})=>p([r(t,o)],{after:0,align:o.align}); // tight cell paragraph

// gap-fill onderstreping
const blank=(n=14)=>r(" ".repeat(0)+ "_".repeat(n), {color:MUT});

// ---- CONTENT ----
const kids=[];

// ===== PAGINA 1 · HERO + doelen =====
kids.push(p([r("C4 · LA RUTA · EL DESPEGUE · PARADA 1",{color:WHITE,size:16,bold:true})],{fill:RED,after:0,before:60}));
kids.push(p([r("Presentaciones",{font:HEAD,size:56,bold:true,color:WHITE})],{fill:RED,after:0}));
kids.push(p([r("Je eerste Spaans: groeten, jezelf voorstellen en afscheid nemen. ",{color:WHITE,size:22}),
             r("Survival in Spanish.",{color:WHITE,size:22,italics:true})],{fill:RED,after:0,before:0}));
kids.push(p([r("¡Hola! ¿Cómo te llamas?",{font:HEAD,size:24,bold:true,color:WHITE})],{fill:REDD,after:0,before:60}));
kids.push(spacer(200));
kids.push(se("AL FINAL DE ESTA UNIDAD · OP HET EINDE VAN DEZE LES"));
const obj=[
  ["Saludar y despedirte","groeten en afscheid nemen"],
  ["Decir tu nombre y de dónde eres","zeggen hoe je heet en waar je vandaan komt"],
  ["Preguntar el nombre a otra persona","iemand naar zijn naam vragen"],
  ["Distinguir -o/-a y tú/usted","man/vrouw & informeel/beleefd"],
];
const objRows=[];
for(let i=0;i<obj.length;i+=2){
  const mk=(j)=> obj[j]? cell([tcp("✓ ",{color:OKG,bold:true}), // placeholder
      ],4870):cell([tcp("")],4870);
  // build two cells this row
  const c=[];
  for(let k=0;k<2;k++){ const it=obj[i+k];
    c.push(it? cell([ new Paragraph({children:[r("✓  ",{color:OKG,bold:true,size:22}),r(it[0],{bold:true}),],spacing:{after:10}}),
                      new Paragraph({children:[r(it[1],{color:MUT,size:18,italics:true})],spacing:{after:0}}) ],4870,{fill:CREMA,bc:LINE})
             : cell([tcp("")],4870,{borders:noBorders}) ); }
  objRows.push(new TableRow({children:c}));
}
kids.push(table(objRows,[4870,4870]));
kids.push(spacer(140));
kids.push(p([r("🎒  ¡Vamos! We beginnen te reizen. ",{font:HEAD,bold:true,color:REDD,size:22}),
             r("In deze survival-les leer je de taal die je meteen nodig hebt. Luister, spreek na, en probeer het zelf.",{size:20})],
            {fill:TINT,before:0,after:0}));

// ===== PAGINA 2 · §1 ESCUCHA =====
kids.push(pageBreak());
kids.push(se("§1 · ¡ESCUCHA!"));
kids.push(H2("Bekijk de scène en lees mee"));
kids.push(p([r("🎬  Sitcom · Episodio 1. ",{bold:true,color:REDD}),
   r("Bekijk de aflevering online op de digitale hub (tabblad Escucha). Luister eerst zónder te lezen; daarna lees je mee. De ",{}),
   r("vetgedrukte",{bold:true}), r(" woorden zijn chunks om mee te nemen.",{})],{fill:TINT,after:60}));
kids.push(p([r("Online: ",{size:18,color:MUT}), r("hub · Escucha  ·  video: youtu.be/yvPI-4JGdyo",{size:18,color:REDD,bold:true})],{after:120}));

const COL={ "María":RED,"Julio":BLUE,"Fernando":"7C4DE0","Josefina":OKG };
const CH=["Hola","¿Cómo estás?","Bien","encantada","Encantado","¿Cómo te llamas?","me llamo","Yo soy","soy",
  "hasta luego","Adiós","Vale","¿Cómo está usted?","Igualmente","Encantado de conocerla","Me llamo","Muchas gracias","De nada","Bienvenida","Perdona"];
function scene(title, lines){
  const out=[ p([r(title,{font:HEAD,size:22,bold:true,color:REDD})],{before:80,after:40,keepNext:true}) ];
  for(const [sp,txt] of lines){
    // split txt on chunks → bold
    const runs=[ new TextRun({ text:sp+"   ", bold:true, color:COL[sp]||REDD, font:HEAD, size:20 }) ];
    let rest=txt, guard=0;
    // simple bolding: wrap known chunks
    const parts=[]; let idx=0;
    // build regex
    const rx=new RegExp("("+CH.sort((a,b)=>b.length-a.length).map(c=>c.replace(/[.*+?^${}()|[\]\\]/g,"\\$&")).join("|")+")","i");
    let s=txt;
    while(s.length){ const m=s.match(rx); if(!m){ parts.push([s,false]); break; }
      const i=m.index; if(i>0) parts.push([s.slice(0,i),false]); parts.push([m[0],true]); s=s.slice(i+m[0].length); if(++guard>40)break; }
    for(const [t,b] of parts) runs.push(r(t,{size:21,bold:b}));
    out.push(new Paragraph({ children:runs, spacing:{after:40}, indent:{left:0} }));
  }
  return out;
}
kids.push(...scene("Escena 1 · Julio y María se despiertan",[
  ["María","Hola. ¿Cómo estás?"],["Julio","Bien. ¿Cómo te llamas?"],
  ["María","Bueno, encantada. Yo me llamo María."],["Julio","Encantado. Yo soy Julio. Perdona, pero me voy al trabajo."],
  ["María","Vale."],["Julio","Bueno, hasta luego."],["María","Adiós."],
]));
kids.push(...scene("Escena 2 · En la academia",[
  ["Fernando","Ella es Josefina, la secretaria."],["Josefina","Hola, encantada. ¿Y tú cómo te llamas?"],
  ["María","Me llamo María."],["Fernando","Julio, os presento: María, la nueva profesora."],
  ["María","¿Cómo está usted?"],["Julio","Encantado de conocerla."],["María","Igualmente."],
  ["María","Muchas gracias, Fernando."],["Fernando","De nada. ¡Bienvenida a la academia!"],
]));
kids.push(p([r("¡Ojo!  ",{bold:true,color:WARN}),
   r("encantado (jongen) / encantada (meisje). Zeg ",{}), r("me llamo…",{italics:true}), r(", niet «yo soy me llamo».",{})],
   {before:80,fill:TINT}));

// ===== PAGINA 3 · SUENA BIEN + §2 KIT =====
kids.push(pageBreak());
kids.push(se("SUENA BIEN · PRONUNCIACIÓN"));
kids.push(H2("De 5 klinkers & de klemtoon"));
kids.push(p([r("Spaanse klinkers zijn ",{}),r("kort en zuiver",{bold:true}),r(" — altijd dezelfde klank. Oefen ze online: luister en spreek na.",{})],{after:80}));
const voc=[["a","als in ‘bal’","casa"],["e","als in ‘bed’","mesa"],["i","als in ‘kiwi’","sí"],["o","als in ‘pot’","hola"],["u","als in ‘boek’","tú"]];
kids.push(table([ new TableRow({children:voc.map(v=>cell([
    new Paragraph({children:[r(v[0],{font:HEAD,bold:true,color:REDD,size:40})],alignment:AlignmentType.CENTER,spacing:{after:10}}),
    new Paragraph({children:[r(v[1],{size:16,color:MUT})],alignment:AlignmentType.CENTER,spacing:{after:0}}),
    new Paragraph({children:[r(v[2],{bold:true,size:20})],alignment:AlignmentType.CENTER,spacing:{after:0}}),
  ],1948,{fill:WHITE,mt:80,mb:80}))}) ],[1948,1948,1948,1948,1948]));
kids.push(p([r("¡Ojo!  ",{bold:true,color:WARN}),r("e blijft /e/ en o blijft /o/ — géén Nederlandse «ei/ou»-glijder (denk: a·e·i·o·oe).",{})],{before:80,fill:TINT}));
kids.push(p([r("La sílaba tónica",{font:HEAD,bold:true,color:REDD}),r(" — waar ligt de klemtoon?  ",{}),
  r("HO",{bold:true,color:RED}),r("·la · me·",{}),r("LLA",{bold:true,color:RED}),r("·mo · en·can·",{}),
  r("TA",{bold:true,color:RED}),r("·do · a·",{}),r("DIÓS",{bold:true,color:RED}),r(" · ",{}),r("GRA",{bold:true,color:RED}),r("·cias",{})],{before:80,after:60}));
kids.push(p([r("Repite · spreek na:  ",{font:HEAD,bold:true,color:REDD}),
  r("Hola · Buenos días · Me llamo · Encantado · Muchas gracias",{bold:true})],{after:0,fill:CREMA}));

// §2 KIT (vloeit door naar p.4)
kids.push(p([],{after:160}));
kids.push(se("§2 · KIT DE SUPERVIVENCIA"));
kids.push(H2("De taal die je écht nodig hebt"));
kids.push(p([r("Vink ☐ af telkens je een uitdrukking vlot kunt ",{size:19,color:MUT}),r("naspreken",{size:19,color:MUT,bold:true}),r(".",{size:19,color:MUT})],{after:100}));
function kitTable(titel, items){
  const rows=[ new TableRow({tableHeader:true,children:[
    cell([tcp("Español",{size:16,bold:true,color:REDD})],3600,{fill:TINT}),
    cell([tcp("Nederlands",{size:16,bold:true,color:REDD})],4640,{fill:TINT}),
    cell([tcp("🔊 na",{size:16,bold:true,color:REDD,align:AlignmentType.CENTER})],1500,{fill:TINT}),
  ]}) ];
  for(const [es,nl] of items) rows.push(new TableRow({children:[
    cell([tcp(es,{bold:true})],3600), cell([tcp(nl,{italics:true,color:MUT})],4640),
    cell([tcp("☐",{align:AlignmentType.CENTER})],1500) ]}));
  return [ H3(titel), table(rows,[3600,4640,1500]), spacer(120) ];
}
kids.push(...kitTable("Saludar · begroeten",[["¡Hola!","Hallo"],["Buenos días","Goedemorgen"],["Buenas tardes","Goedemiddag"],["¿Qué tal?","Hoe gaat het?"],["¿Cómo estás?","Hoe gaat het? (jij)"],["¿Cómo está usted?","… met u?"]]));
kids.push(...kitTable("Presentarse · jezelf voorstellen",[["Me llamo…","Ik heet…"],["Yo soy…","Ik ben…"],["Soy de…","Ik kom uit…"],["Encantado / Encantada","Aangenaam (m/v)"],["Igualmente","Insgelijks"]]));
kids.push(...kitTable("Preguntar & responder",[["¿Cómo te llamas?","Hoe heet je?"],["¿Y tú?","En jij?"],["¿De dónde eres?","Waar kom je vandaan?"],["Bien, ¿y tú?","Goed, en jij?"],["Muy bien","Heel goed"]]));
kids.push(...kitTable("Cortesía & despedirse",[["Por favor","Alsjeblieft"],["(Muchas) gracias","(Hartelijk) dank"],["De nada","Graag gedaan"],["Perdona","Sorry"],["Adiós · Hasta luego","Dag · Tot straks"],["Vale · ¡Nos vemos!","Oké · We zien elkaar!"]]));

// ===== §4 GRAMÁTICA =====
kids.push(pageBreak());
kids.push(se("§4 · GRAMÁTICA EN LA PRÁCTICA"));
kids.push(H2("Kort en functioneel"));
function verbTable(tag, rows){
  const head=new TableRow({tableHeader:true,children:[
    cell([tcp(tag,{bold:true,color:WHITE,size:18})],2200,{fill:RED}),
    cell([tcp("",{})],1600,{fill:RED}), cell([tcp("",{})],2400,{fill:RED}), cell([tcp("",{})],3540,{fill:RED}) ]});
  const body=rows.map(([a,b,c,d])=>new TableRow({children:[
    cell([tcp(a,{color:BLUE,bold:true})],2200), cell([tcp(b,{color:ORA,bold:true,font:HEAD})],1600),
    cell([tcp(c,{})],2400), cell([tcp(d,{italics:true,color:MUT})],3540) ]}));
  return table([head,...body],[2200,1600,2400,3540]);
}
kids.push(H3("ser · zijn (wie je bent)"));
kids.push(verbTable("ser",[["yo","soy","ik ben","Yo soy Ana."],["tú","eres","jij bent","¿Eres Leo?"],["él/ella/usted","es","hij/zij is · u bent","Ella es María."]]));
kids.push(spacer(120));
kids.push(H3("llamarse · heten (hoe je heet)"));
kids.push(verbTable("llamarse",[["(yo) me","llamo","ik heet","Me llamo Sara."],["(tú) te","llamas","jij heet","¿Cómo te llamas?"],["(usted) se","llama","u heet","¿Cómo se llama usted?"]]));
kids.push(spacer(140));
kids.push(H3("-o / -a · man of vrouw"));
kids.push(table([ new TableRow({children:[
   cell([ new Paragraph({children:[r("♂ Un chico dice…",{font:HEAD,bold:true,color:"1E40AF"})],spacing:{after:30}}),
          new Paragraph({children:[r("Encantado · Bienvenido",{bold:true,color:"1E40AF",size:22})]}) ],4870,{fill:"E8F0FE"}),
   cell([ new Paragraph({children:[r("♀ Una chica dice…",{font:HEAD,bold:true,color:"9D174D"})],spacing:{after:30}}),
          new Paragraph({children:[r("Encantada · Bienvenida",{bold:true,color:"9D174D",size:22})]}) ],4870,{fill:"FCE7F0"}) ]}) ],[4870,4870]));
kids.push(spacer(120));
kids.push(p([r("tú ↔ usted.  ",{font:HEAD,bold:true,color:REDD}),
  r("Met vrienden/klasgenoten: ",{}),r("tú",{bold:true,color:ORA}),r("  (¿Cómo estás? · ¿Cómo te llamas?). Formeel, met een onbekende volwassene: ",{}),
  r("usted",{bold:true,color:ORA}),r("  (¿Cómo está usted? · ¿Cómo se llama?).",{})],{after:120}));
kids.push(p([r("Mini-oefening. ",{bold:true,color:REDD}),r("Vul aan met ",{}),r("ser",{italics:true}),r(" of ",{}),r("llamarse",{italics:true}),r(":",{})],{fill:CREMA,after:0}));
const miniRuns=[ r("1. Yo "),blank(10),r(" de Belgica.    2. Como "),blank(8),r(" llamas?    3. Me "),blank(8),r(" nombre.    4. Ella "),blank(8),r(" profesora.") ];
kids.push(p(miniRuns,{before:60,line:360}));

// ===== §3 PRÁCTICA =====
kids.push(pageBreak());
kids.push(se("§3 · PRÁCTICA"));
kids.push(H2("Oefen op papier — online verbeter je alles"));
// ① Clasifica
kids.push(H3("①  Clasifica las expresiones"));
kids.push(p([r("Schrijf elke uitdrukking in de juiste kolom (+ één eigen woord). ",{size:19}),
  r("Hola · Adiós · Gracias · ¿Cómo te llamas? · Hasta luego · De nada · Buenos días · Encantado",{size:18,italics:true,color:MUT})],{after:80}));
const catHead=new TableRow({tableHeader:true,children:["Saludar","Preguntar","Cortesía","Despedirse"].map(t=>
  cell([tcp(t,{bold:true,color:REDD,size:16,align:AlignmentType.CENTER})],2435,{fill:TINT}))});
const catBody=new TableRow({height:{value:2000,rule:HeightRule.ATLEAST},children:[0,1,2,3].map(()=>cell([tcp("")],2435,{valign:VerticalAlign.TOP}))});
kids.push(table([catHead,catBody],[2435,2435,2435,2435]));
kids.push(spacer(140));
// ② Relaciona
kids.push(H3("②  Relaciona · verbind met een lijn"));
const L=["1. ¡Hola!","2. ¿Cómo te llamas?","3. De nada","4. Hasta luego","5. Encantada"];
const Rr=["a. graag gedaan","b. tot straks","c. hallo","d. aangenaam","e. hoe heet je?"];
const relRows=L.map((l,i)=>new TableRow({children:[ cell([tcp(l,{bold:true})],4870), cell([tcp(Rr[i],{color:MUT})],4870) ]}));
kids.push(table(relRows,[4870,4870]));
kids.push(spacer(140));
// ③ Completa
kids.push(H3("③  Completa el diálogo"));
kids.push(p([r("— ¡Hola! ¿Cómo "),blank(8),r(" llamas?")],{line:360,after:20}));
kids.push(p([r("— Me "),blank(8),r(" Ana. ¿Y "),blank(6),r("?")],{line:360,after:20}));
kids.push(p([r("— Yo "),blank(8),r(" Leo. "),blank(8),r(" de Madrid.")],{line:360,after:20}));
kids.push(p([r("— ¡"),blank(10),r("! Hasta "),blank(8),r(".")],{line:360,after:120}));
// ④ Ordena
kids.push(H3("④  Ordena la conversación (1–5)"));
["Yo soy Leo. Encantado.","¡Hola! ¿Cómo te llamas?","¡Hasta luego!","Me llamo Ana. ¿Y tú?","Igualmente. ¡Adiós!"].forEach(s=>
  kids.push(p([r("____  "),r(s)],{line:340,after:20})));
kids.push(spacer(80));
// ⑤ -o/-a
kids.push(H3("⑤  ¿-o o -a?  (♂ -o / ♀ -a)"));
kids.push(p([r("1. (chico) Encantad"),blank(3),r("     2. (chica) Encantad"),blank(3),r("     3. (chica) Bienvenid"),blank(3),r("     4. (chico) Bienvenid"),blank(3)],{line:360,after:120}));
// ⑥ Preséntate — schrijfvlak
kids.push(H3("⑥  Preséntate por escrito"));
kids.push(p([r("Stel jezelf voor in 3–4 zinnen: groet, naam, herkomst, afscheid.",{size:19,color:MUT})],{after:60}));
kids.push(table([ new TableRow({height:{value:1900,rule:HeightRule.ATLEAST},children:[cell([tcp("")],TW,{valign:VerticalAlign.TOP,fill:"FFFFFF"})]}) ],[TW]));

// ===== §5 TAREA + MÚSICA + REPASO =====
kids.push(pageBreak());
kids.push(se("§5 · TAREA FINAL"));
kids.push(H2("El carné de la clase"));
kids.push(p([r("Maak je klaskaartje en stel je mondeling voor aan 3 klasgenoten. Vraag hun naam en herkomst, en noteer ze — ",{}),
   r("sin leer del papel",{italics:true}),r(" (zonder van het blad af te lezen).",{})],{fill:TINT,after:120}));
// carné
kids.push(H3("Mi carné"));
const carne=[["Me llamo",""],["Soy de",""],["Mi emoji / dibujo",""]];
kids.push(table(carne.map(([a])=>new TableRow({height:{value:520,rule:HeightRule.ATLEAST},children:[
  cell([tcp(a,{bold:true})],2600,{fill:CREMA}), cell([tcp("")],7140) ]})),[2600,7140]));
kids.push(spacer(140));
kids.push(H3("3 compañeros"));
const compHead=new TableRow({tableHeader:true,children:[
  cell([tcp("#",{bold:true,color:REDD,size:16,align:AlignmentType.CENTER})],740,{fill:TINT}),
  cell([tcp("¿Cómo te llamas?",{bold:true,color:REDD,size:16})],4500,{fill:TINT}),
  cell([tcp("¿De dónde eres?",{bold:true,color:REDD,size:16})],4500,{fill:TINT}) ]});
const compBody=[1,2,3].map(n=>new TableRow({height:{value:560,rule:HeightRule.ATLEAST},children:[
  cell([tcp(String(n),{align:AlignmentType.CENTER,color:MUT})],740), cell([tcp("")],4500), cell([tcp("")],4500) ]}));
kids.push(table([compHead,...compBody],[740,4500,4500]));
kids.push(p([r("🏁 Klaar als… ",{bold:true,color:REDD}),r("je jezelf vlot voorstelt zónder af te lezen, de juiste vorm (-o/-a) gebruikt en 3 namen genoteerd hebt.",{})],{before:120,fill:CREMA}));

// Música
kids.push(spacer(200));
kids.push(se("CULTURA · BANDA SONORA"));
kids.push(H2("Leer Spaans via muziek"));
kids.push(p([r("Het nummer bij deze les: ",{}),r("Aitana · «6 de febrero»",{bold:true}),r("  en  ",{}),r("Manu Chao · «Me gustas tú»",{bold:true}),
  r(". Luister mee op de klas-playlist (Spotify) en vul de tekst aan in LyricsTraining — alles op de digitale hub.",{})],{after:0}));

// Repaso
kids.push(spacer(200));
kids.push(se("REPASO · LO ESENCIAL"));
kids.push(H2("Wat je nu kunt"));
kids.push(p([r("Zo groet & stel je je voor:  ",{bold:true,color:REDD}),
  r("¡Hola! Me llamo ___. Soy de ___. Encantad_. ¿Y tú, cómo te llamas?",{})],{fill:TINT,after:60}));
kids.push(p([r("Onthou:  ",{bold:true,color:REDD}),r("ser = soy · eres · es   |   llamarse = me/te/se + llamo/llamas/llama   |   -o = ♂ · -a = ♀   |   tú = vriend · usted = beleefd",{})],{after:120}));
const semHead=new TableRow({tableHeader:true,children:[
  cell([tcp("Puedo… · Ik kan…",{bold:true,color:REDD,size:16})],6740,{fill:TINT}),
  cell([tcp("🟢",{align:AlignmentType.CENTER})],1000,{fill:TINT}),
  cell([tcp("🟡",{align:AlignmentType.CENTER})],1000,{fill:TINT}),
  cell([tcp("🔴",{align:AlignmentType.CENTER})],1000,{fill:TINT}) ]});
const semItems=["groeten en afscheid nemen","mezelf voorstellen (naam + herkomst)","iemand naar zijn naam vragen","-o/-a en tú/usted juist kiezen"];
const semBody=semItems.map(it=>new TableRow({height:{value:440,rule:HeightRule.ATLEAST},children:[
  cell([tcp(it)],6740), cell([tcp("☐",{align:AlignmentType.CENTER})],1000), cell([tcp("☐",{align:AlignmentType.CENTER})],1000), cell([tcp("☐",{align:AlignmentType.CENTER})],1000) ]}));
kids.push(table([semHead,...semBody],[6740,1000,1000,1000]));
kids.push(p([r("🎮 Repasa jugando (online): oefen alles met spelletjes, flashcards en audio op de digitale hub.",{size:19,italics:true,color:MUT})],{before:120}));

// ---- document ----
const doc=new Document({
  creator:"C4 · Welcome to Spanish",
  title:"Unidad 1 · Presentaciones",
  styles:{ default:{ document:{ run:{ font:BODY, size:21, color:INK } } } },
  sections:[{
    properties:{ page:{ size:{ width:11906, height:16838 }, margin:{ top:1080, bottom:1080, left:1080, right:1080 } } },
    children:kids
  }]
});
Packer.toBuffer(doc).then(buf=>{ fs.writeFileSync(__dirname+"/C4_U1.docx", buf); console.log("C4_U1.docx geschreven:", buf.length, "bytes"); });
