/* data.verbos.extra.js — UITBREIDING van de Conjugador-database.
   ~680 extra frequente Spaanse infinitieven bovenop data.verbos.es.js (324),
   samen ~1000. Zelfde tag-schema:
     {i,n}                 → regelmatig (default)
     c:"ie|ue|i|uue|ie2|hue" → klankwissel in de sterke stam
     o:"zco|zo|ger|guir|uir" → orthografische yo-wijziging
     yo:"..."              → expliciete yo-vorm (yo-onregelmatig)
     pres:[6 vormen]       → volledig onregelmatig / accentverschuiving (i→í, u→ú)
     irr:true              → markeer als 'onregelmatig' in de sorteerspellen
   Presente wordt NAGEREKEND door window.MotorGen.verboConjugar — nooit vrij gegenereerd.
   Samenstellingen erven het gedrag van hun basiswerkwoord. */
window.MotorData = window.MotorData || {};

/* helper: [inf, nl] → {i,n}  (regelmatig) */
const XR = list => list.map(p => ({i:p[0], n:p[1]}));

/* ===================== 1 · REGELMATIG ===================== */
const XREG = XR([
  /* -ar */
  ["quedar","blijven"],["acercar","naderbrengen"],["lograr","bereiken"],["alcanzar","bereiken"],
  ["retirar","terugtrekken"],["girar","draaien"],["fijar","vastmaken"],["firmar","ondertekenen"],
  ["citar","citeren"],["generar","genereren"],["provocar","uitlokken"],["representar","voorstellen"],
  ["significar","betekenen"],["identificar","identificeren"],["justificar","rechtvaardigen"],["verificar","verifiëren"],
  ["aplicar","toepassen"],["implicar","impliceren"],["educar","opvoeden"],["clasificar","indelen"],
  ["modificar","wijzigen"],["dominar","beheersen"],["determinar","bepalen"],["eliminar","elimineren"],
  ["examinar","onderzoeken"],["combinar","combineren"],["coordinar","coördineren"],["abandonar","verlaten"],
  ["mencionar","vermelden"],["relacionar","in verband brengen"],["seleccionar","selecteren"],["proporcionar","verschaffen"],
  ["presionar","drukken"],["diseñar","ontwerpen"],["engañar","bedriegen"],["bañar","baden"],
  ["nombrar","noemen"],["alegrar","verheugen"],["integrar","integreren"],["recuperar","herstellen"],
  ["operar","opereren"],["liberar","bevrijden"],["colaborar","samenwerken"],["elaborar","uitwerken"],
  ["adorar","aanbidden"],["ignorar","negeren"],["explorar","verkennen"],["apuntar","aanwijzen/noteren"],
  ["juntar","samenvoegen"],["alimentar","voeden"],["experimentar","ervaren"],["lamentar","betreuren"],
  ["orientar","oriënteren"],["aguantar","verdragen"],["plantar","planten"],["faltar","ontbreken"],
  ["insultar","beledigen"],["adaptar","aanpassen"],["captar","opvangen"],["optar","opteren"],
  ["apartar","afzonderen"],["transportar","vervoeren"],["soportar","verdragen"],["aportar","bijdragen"],
  ["ejecutar","uitvoeren"],["dudar","twijfelen"],["admirar","bewonderen"],["inspirar","inspireren"],
  ["suspirar","zuchten"],["estirar","uitrekken"],["disparar","schieten"],["declarar","verklaren"],
  ["aclarar","verduidelijken"],["asegurar","verzekeren"],["asustar","bang maken"],["atar","binden"],
  ["aterrizar","landen"],["besar","kussen"],["borrar","uitwissen"],["chocar","botsen"],
  ["conservar","bewaren"],["criticar","bekritiseren"],["cruzar","oversteken"],["culpar","beschuldigen"],
  ["curar","genezen"],["dañar","beschadigen"],["destacar","opvallen"],["empujar","duwen"],
  ["encargar","belasten/opdragen"],["enfrentar","confronteren"],["entrenar","trainen"],["equivocar","vergissen"],
  ["estrenar","voor het eerst gebruiken"],["fabricar","fabriceren"],["fallar","mislukken"],["fascinar","fascineren"],
  ["frenar","remmen"],["fumar","roken"],["golpear","slaan"],["grabar","opnemen"],
  ["heredar","erven"],["iniciar","beginnen"],["instalar","installeren"],["interpretar","vertolken"],
  ["juzgar","oordelen"],["lanzar","werpen"],["lastimar","bezeren"],["localizar","lokaliseren"],
  ["madrugar","vroeg opstaan"],["masticar","kauwen"],["molestar","storen"],["motivar","motiveren"],
  ["navegar","varen/surfen"],["negociar","onderhandelen"],["ocupar","bezetten"],["pasear","wandelen"],
  ["patinar","schaatsen"],["pescar","vissen"],["pronunciar","uitspreken"],["protestar","protesteren"],
  ["reclamar","opeisen"],["rechazar","afwijzen"],["reflejar","weerspiegelen"],["relajar","ontspannen"],
  ["repasar","herhalen"],["rescatar","redden"],["retrasar","vertragen"],["rezar","bidden"],
  ["rodear","omringen"],["solucionar","oplossen"],["sospechar","vermoeden"],["subrayar","onderstrepen"],
  ["sujetar","vasthouden"],["sumar","optellen"],["tapar","bedekken"],["telefonear","telefoneren"],
  ["traicionar","verraden"],["trasladar","overbrengen"],["triunfar","zegevieren"],["valorar","waarderen"],
  ["vigilar","bewaken"],["vincular","verbinden"],["arrancar","starten/uittrekken"],["arrastrar","slepen"],
  ["abrazar","omhelzen"],["gozar","genieten"],["amenazar","bedreigen"],["avanzar","vooruitgaan"],
  ["analizar","analyseren"],["cargar","laden"],["tragar","slikken"],["vengar","wreken"],
  ["acostumbrar","wennen"],["andar","lopen/gaan"],["aprovechar","benutten"],["asociar","associëren"],
  ["bloquear","blokkeren"],["bromear","grappen maken"],["calmar","kalmeren"],["cansar","vermoeien"],
  ["conquistar","veroveren"],["contagiar","besmetten"],["contaminar","vervuilen"],["decorar","versieren"],
  ["depositar","storten"],["derramar","morsen"],["derribar","neerhalen"],["deslizar","glijden"],
  ["despegar","opstijgen/losmaken"],["disgustar","tegenstaan"],["divorciar","scheiden"],["duplicar","verdubbelen"],
  ["elevar","verheffen"],["emocionar","ontroeren"],["enojar","boos maken"],["ensayar","repeteren"],
  ["ensuciar","vuil maken"],["enterar","op de hoogte brengen"],["entrevistar","interviewen"],["escalar","beklimmen"],
  ["evaporar","verdampen"],["exagerar","overdrijven"],["exclamar","uitroepen"],["fastidiar","vervelen"],
  ["festejar","vieren"],["financiar","financieren"],["flotar","drijven"],["fomentar","bevorderen"],
  ["formular","formuleren"],["fracasar","mislukken"],["frotar","wrijven"],["gestionar","beheren"],
  ["gustar","bevallen"],["halar","trekken"],["hallar","aantreffen"],["ilustrar","illustreren"],
  ["impresionar","imponeren"],["incorporar","opnemen"],["influenciar","beïnvloeden"],["ingresar","binnentreden/storten"],
  ["intercambiar","uitwisselen"],["investigar","onderzoeken"],["jubilar","pensioneren"],["ligar","versieren/binden"],
  ["maquillar","opmaken"],["maravillar","verbazen"],["marchar","marcheren/vertrekken"],["marear","duizelig maken"],
  ["memorizar","memoriseren"],["mimar","verwennen"],["multiplicar","vermenigvuldigen"],["ocasionar","veroorzaken"],
  ["ondear","wapperen"],["pausar","pauzeren"],["pelar","pellen"],["penetrar","binnendringen"],
  ["perjudicar","schaden"],["pesar","wegen"],["planchar","strijken"],["planear","plannen"],
  ["posar","poseren"],["postular","zich kandidaat stellen"],["premiar","belonen"],["procesar","verwerken"],
  ["procurar","proberen te"],["profundizar","verdiepen"],["prolongar","verlengen"],["promocionar","promoten"],
  ["pronosticar","voorspellen"],["proyectar","projecteren"],["quejar","klagen"],["rascar","krabben"],
  ["rasgar","scheuren"],["realzar","benadrukken"],["rebajar","verlagen"],["recargar","opladen"],
  ["recopilar","verzamelen"],["rectificar","rechtzetten"],["reflexionar","nadenken"],["regular","reguleren"],
  ["reinar","heersen"],["relatar","vertellen"],["rematar","afmaken"],["remar","roeien"],
  ["remolcar","slepen"],["renunciar","afzien/ontslag nemen"],["reposar","rusten"],["reprochar","verwijten"],
  ["resbalar","uitglijden"],["respaldar","steunen"],["restar","aftrekken"],["restaurar","restaureren"],
  ["retratar","portretteren"],["rifar","verloten"],["saborear","proeven/savoureren"],["sancionar","bestraffen"],
  ["saquear","plunderen"],["sazonar","kruiden"],["secuestrar","ontvoeren"],["silbar","fluiten"],
  ["simbolizar","symboliseren"],["simular","simuleren"],["sobrar","overblijven"],["sollozar","snikken"],
  ["sonrojar","doen blozen"],["subastar","veilen"],["sudar","zweten"],["suministrar","leveren"],
  ["susurrar","fluisteren"],["tallar","beeldhouwen"],["tararear","neuriën"],["teclear","typen"],
  ["timar","oplichten"],["titular","betitelen"],["tolerar","tolereren"],["torturar","martelen"],
  ["trabar","vastzetten"],["tramitar","afhandelen"],["transformar","transformeren"],["trasnochar","doorwaken"],
  ["trazar","tekenen/schetsen"],["tumbar","omvergooien"],["untar","insmeren"],["vacilar","aarzelen"],
  ["vagar","dwalen"],["velar","waken"],["vendar","verbinden (wonde)"],["ventilar","luchten"],
  ["veranear","de zomer doorbrengen"],["vociferar","brullen"],["zarpar","uitvaren"],["asfaltar","asfalteren"],
  /* -er regelmatig */
  ["conceder","toestaan"],["proceder","overgaan tot"],["exceder","overschrijden"],["acceder","toegang krijgen"],
  ["suceder","gebeuren/opvolgen"],["corresponder","overeenkomen/beantwoorden"],["emprender","ondernemen"],["pretender","beogen"],
  ["ceder","afstaan/toegeven"],["comprometer","verplichten/compromitteren"],["someter","onderwerpen"],["reprender","berispen"],
  ["absorber","absorberen"],["poseer","bezitten"],["proveer","voorzien"],["leer","lezen"],
  ["creer","geloven"],["releer","herlezen"],["suspender","schorsen/zakken"],["tejer","weven/breien"],
  /* -ir regelmatig */
  ["acudir","toesnellen/opdagen"],["aludir","zinspelen"],["eludir","ontwijken"],["emitir","uitzenden"],
  ["omitir","weglaten"],["difundir","verspreiden"],["confundir","verwarren"],["fundir","smelten/versmelten"],
  ["hundir","doen zinken"],["aplaudir","applaudisseren"],["recurrir","zijn toevlucht nemen"],["concurrir","samenkomen"],
  ["incurrir","vervallen in"],["debatir","debatteren"],["combatir","bestrijden"],["exhibir","tentoonstellen"],
  ["inhibir","remmen"],["inscribir","inschrijven"],["prescribir","voorschrijven"],["suscribir","ondertekenen/abonneren"],
  ["transcribir","overschrijven"],["escurrir","uitdruipen"],["pulir","polijsten"],["nutrir","voeden"],
  ["prescindir","afzien van"],["transmitir","uitzenden"],["aturdir","verdoven"],["cundir","zich verspreiden"]
]).filter(v => !/2$/.test(v.i));

/* ===================== 2 · KLANKWISSEL e→ie (c:"ie") ===================== */
const XIE = [
  {i:"apretar",n:"aandrukken",c:"ie"},{i:"atravesar",n:"oversteken",c:"ie"},{i:"confesar",n:"bekennen",c:"ie"},
  {i:"tropezar",n:"struikelen",c:"ie"},{i:"quebrar",n:"breken",c:"ie"},{i:"sembrar",n:"zaaien",c:"ie"},
  {i:"acertar",n:"raden/juist hebben",c:"ie"},{i:"concertar",n:"afspreken",c:"ie"},{i:"reventar",n:"barsten",c:"ie"},
  {i:"merendar",n:"vieruurtje eten",c:"ie"},{i:"arrendar",n:"verhuren",c:"ie"},{i:"manifestar",n:"uiten",c:"ie"},
  {i:"cegar",n:"verblinden",c:"ie"},{i:"regar",n:"besproeien",c:"ie"},{i:"fregar",n:"schrobben",c:"ie"},
  {i:"plegar",n:"vouwen",c:"ie"},{i:"segar",n:"maaien",c:"ie"},{i:"helar",n:"bevriezen",c:"ie"},
  {i:"temblar",n:"beven",c:"ie"},{i:"tender",n:"uithangen/spreiden",c:"ie"},{i:"extender",n:"uitbreiden",c:"ie"},
  {i:"atender",n:"bedienen/verzorgen",c:"ie"},{i:"descender",n:"dalen",c:"ie"},{i:"ascender",n:"stijgen",c:"ie"},
  {i:"verter",n:"gieten",c:"ie"},{i:"cerner",n:"ziften",c:"ie"},{i:"consentir",n:"toestaan",c:"ie"},
  {i:"presentir",n:"voorvoelen",c:"ie"},{i:"resentir",n:"kwalijk nemen",c:"ie"},{i:"invertir",n:"investeren/omkeren",c:"ie"},
  {i:"sugerir",n:"suggereren",c:"ie"},{i:"digerir",n:"verteren",c:"ie"},{i:"referir",n:"verwijzen/vertellen",c:"ie"},
  {i:"transferir",n:"overdragen",c:"ie"},{i:"requerir",n:"vereisen",c:"ie"},{i:"adherir",n:"aanhangen",c:"ie"},
  {i:"diferir",n:"verschillen/uitstellen",c:"ie"},{i:"inferir",n:"afleiden",c:"ie"},{i:"subvertir",n:"ondermijnen",c:"ie"}
];

/* ===================== 3 · KLANKWISSEL o→ue (c:"ue") ===================== */
const XUE = [
  {i:"apostar",n:"wedden",c:"ue"},{i:"demostrar",n:"aantonen",c:"ue"},{i:"descontar",n:"aftrekken/korting geven",c:"ue"},
  {i:"tronar",n:"donderen",c:"ue"},{i:"volcar",n:"omkantelen",c:"ue"},{i:"rodar",n:"rollen/rijden",c:"ue"},
  {i:"soltar",n:"loslaten",c:"ue"},{i:"resolver",n:"oplossen",c:"ue"},{i:"devolver",n:"teruggeven",c:"ue"},
  {i:"envolver",n:"inpakken",c:"ue"},{i:"disolver",n:"oplossen (in vloeistof)",c:"ue"},{i:"remover",n:"roeren/verwijderen",c:"ue"},
  {i:"promover",n:"bevorderen",c:"ue"},{i:"conmover",n:"ontroeren",c:"ue"},{i:"soler",n:"gewoonlijk doen",c:"ue"},
  {i:"reforzar",n:"versterken",c:"ue"},{i:"esforzar",n:"zich inspannen",c:"ue"},{i:"comprobar",n:"nagaan",c:"ue"},
  {i:"reprobar",n:"afkeuren/buizen",c:"ue"},{i:"poblar",n:"bevolken",c:"ue"},{i:"renovar",n:"vernieuwen",c:"ue"},
  {i:"trocar",n:"ruilen",c:"ue"},{i:"tostar",n:"roosteren",c:"ue"},{i:"consolar",n:"troosten",c:"ue"},
  {i:"resonar",n:"weerklinken",c:"ue"},{i:"colar",n:"zeven/filteren",c:"ue"},{i:"descolgar",n:"afhaken/opnemen (telefoon)",c:"ue"},
  {i:"cocer",n:"koken (in water)",c:"ue",o:"zo"},{i:"torcer",n:"verdraaien",c:"ue",o:"zo"}
];

/* ===================== 4 · KLANKWISSEL e→i (c:"i", -ir) ===================== */
const XI = [
  {i:"proseguir",n:"voortzetten",c:"i",o:"guir"},{i:"regir",n:"regeren/gelden",c:"i",o:"ger"},
  {i:"concebir",n:"bevatten/zwanger worden",c:"i"},{i:"derretir",n:"smelten",c:"i"},
  {i:"teñir",n:"verven",c:"i"},{i:"ceñir",n:"omgorden",c:"i"},{i:"reñir",n:"ruziën/berispen",c:"i"},
  {i:"desvestir",n:"uitkleden",c:"i"},{i:"expedir",n:"verzenden/afgeven",c:"i"},
  {i:"investir",n:"bekleden (met ambt)",c:"i"},{i:"desteñir",n:"verkleuren",c:"i"}
];

/* ===================== 5 · yo -zco  (-ecer/-ocer/-ucir) ===================== */
const XZCO = [
  ["establecer","vestigen"],["padecer","lijden"],["permanecer","blijven"],["desaparecer","verdwijnen"],
  ["carecer","ontberen"],["fortalecer","versterken"],["favorecer","begunstigen"],["enriquecer","verrijken"],
  ["envejecer","verouderen"],["amanecer","dag worden"],["anochecer","donker worden"],["florecer","bloeien"],
  ["reconocer","herkennen"],["desconocer","niet kennen"],["renacer","herboren worden"],["complacer","behagen"],
  ["lucir","schitteren/uitkomen"],["relucir","glanzen"],["introducir","invoeren"],["reproducir","reproduceren"],
  ["seducir","verleiden"],["deducir","afleiden"],["inducir","aanzetten"],["abastecer","bevoorraden"],
  ["compadecer","medelijden hebben"],["entristecer","bedroeven"],["endurecer","verharden"],["oscurecer","verduisteren"],
  ["aborrecer","verafschuwen"],["restablecer","herstellen"],["estremecer","doen huiveren"],["humedecer","bevochtigen"],
  ["palidecer","verbleken"],["enloquecer","gek maken"],["ennoblecer","veredelen"]
].map(p=>({i:p[0],n:p[1],o:"zco",irr:true}));

/* ===================== 6 · yo -uir  (-uir) ===================== */
const XUIR = [
  ["distribuir","verdelen"],["constituir","vormen"],["instituir","instellen"],["atribuir","toeschrijven"],
  ["disminuir","verminderen"],["excluir","uitsluiten"],["retribuir","vergoeden"],["intuir","aanvoelen"],
  ["fluir","vloeien"],["afluir","toestromen"],["diluir","verdunnen"],["imbuir","doordringen"],
  ["reconstruir","heropbouwen"],["obstruir","versperren"],["instruir","onderrichten"],["restituir","teruggeven"],
  ["recluir","opsluiten"]
].map(p=>({i:p[0],n:p[1],o:"uir",irr:true}));

/* ===================== 7 · yo -jo  (-ger/-gir zonder klankwissel) ===================== */
const XGER = [
  ["encoger","krimpen"],["acoger","opvangen"],["sumergir","onderdompelen"],["surgir","ontstaan"],
  ["fingir","veinzen"],["afligir","bedroeven"],["infligir","toebrengen"],["resurgir","heropleven"],
  ["urgir","dringend zijn"],["rugir","brullen"],["mugir","loeien"],["crujir","kraken"]
].map(p=>({i:p[0],n:p[1],o:"ger",irr:true}));

/* ===================== 8 · yo -zo  (-cer/-cir na medeklinker) ===================== */
const XZO = [
  ["ejercer","uitoefenen"],["mecer","wiegen"],["esparcir","verstrooien"],["fruncir","fronsen"],
  ["zurcir","stoppen (kleding)"],["uncir","inspannen (dier)"]
].map(p=>({i:p[0],n:p[1],o:"zo",irr:true}));

/* ===================== 9 · yo -go / andere yo-onregelmatig ===================== */
const XYO = [
  /* -tener (c:ie, yo ...tengo) */
  {i:"retener",n:"behouden",c:"ie",yo:"retengo"},{i:"sostener",n:"steunen/volhouden",c:"ie",yo:"sostengo"},
  {i:"entretener",n:"vermaken",c:"ie",yo:"entretengo"},{i:"abstener",n:"zich onthouden",c:"ie",yo:"abstengo"},
  {i:"atener",n:"zich houden aan",c:"ie",yo:"atengo"},
  /* -poner (yo ...pongo) */
  {i:"imponer",n:"opleggen",yo:"impongo",irr:true},{i:"exponer",n:"blootstellen/uiteenzetten",yo:"expongo",irr:true},
  {i:"disponer",n:"beschikken",yo:"dispongo",irr:true},{i:"oponer",n:"tegenwerpen",yo:"opongo",irr:true},
  {i:"posponer",n:"uitstellen",yo:"pospongo",irr:true},{i:"reponer",n:"aanvullen/terugplaatsen",yo:"repongo",irr:true},
  {i:"descomponer",n:"ontbinden/defect maken",yo:"descompongo",irr:true},{i:"superponer",n:"over elkaar leggen",yo:"superpongo",irr:true},
  {i:"presuponer",n:"vooronderstellen",yo:"presupongo",irr:true},
  /* -venir (c:ie, yo ...vengo) */
  {i:"intervenir",n:"tussenkomen",c:"ie",yo:"intervengo"},{i:"provenir",n:"voortkomen",c:"ie",yo:"provengo"},
  {i:"sobrevenir",n:"overkomen",c:"ie",yo:"sobrevengo"},{i:"contravenir",n:"overtreden",c:"ie",yo:"contravengo"},
  /* -decir (c:i, yo ...digo) */
  {i:"contradecir",n:"tegenspreken",c:"i",yo:"contradigo"},{i:"bendecir",n:"zegenen",c:"i",yo:"bendigo"},
  {i:"maldecir",n:"vervloeken",c:"i",yo:"maldigo"},{i:"desdecir",n:"herroepen",c:"i",yo:"desdigo"},
  /* -traer (yo ...traigo) */
  {i:"distraer",n:"afleiden",yo:"distraigo",irr:true},{i:"contraer",n:"samentrekken/aangaan",yo:"contraigo",irr:true},
  {i:"extraer",n:"uittrekken",yo:"extraigo",irr:true},{i:"sustraer",n:"onttrekken/aftrekken",yo:"sustraigo",irr:true},
  {i:"retraer",n:"terugtrekken",yo:"retraigo",irr:true},{i:"abstraer",n:"abstraheren",yo:"abstraigo",irr:true},
  /* -hacer (yo ...hago) */
  {i:"rehacer",n:"overdoen",yo:"rehago",irr:true},{i:"satisfacer",n:"voldoen/bevredigen",yo:"satisfago",irr:true},
  {i:"contrahacer",n:"namaken",yo:"contrahago",irr:true},
  /* -salir / -valer (yo ...go) */
  {i:"sobresalir",n:"uitsteken/uitblinken",yo:"sobresalgo",irr:true},{i:"equivaler",n:"gelijkstaan aan",yo:"equivalgo",irr:true},
  /* -caer (yo ...caigo) */
  {i:"recaer",n:"terugvallen/hervallen",yo:"recaigo",irr:true},{i:"decaer",n:"verzwakken/vervallen",yo:"decaigo",irr:true},
  /* -guir zonder klankwissel (yo ...go) */
  {i:"extinguir",n:"doven/uitsterven",o:"guir",irr:true},
  /* asir */
  {i:"asir",n:"vastgrijpen",yo:"asgo",irr:true}
];

/* ===================== 10 · ACCENTVERSCHUIVING i→í (pres expliciet) ===================== */
const XACC_I = [
  ["enviar","versturen","enví","envi"],["confiar","vertrouwen","confí","confi"],["guiar","gidsen/leiden","guí","gui"],
  ["variar","variëren","varí","vari"],["criar","grootbrengen","crí","cri"],["enfriar","afkoelen","enfrí","enfri"],
  ["espiar","bespieden","espí","espi"],["ampliar","uitbreiden","amplí","ampli"],["fiar","op krediet geven","fí","fi"],
  ["desviar","afleiden/omleiden","desví","desvi"],["esquiar","skiën","esquí","esqui"],["fotografiar","fotograferen","fotografí","fotografi"],
  ["rociar","besprenkelen","rocí","roci"],["desafiar","uitdagen","desafí","desafi"],["averiar","defect maken","averí","averi"],
  ["resfriar","verkouden maken","resfrí","resfri"]
].map(p=>({i:p[0],n:p[1],pres:[p[2]+"o",p[2]+"as",p[2]+"a",p[3]+"amos",p[3]+"áis",p[2]+"an"]}));

/* ===================== 11 · ACCENTVERSCHUIVING u→ú (pres expliciet) ===================== */
const XACC_U = [
  ["continuar","voortzetten","continú","continu"],["actuar","handelen","actú","actu"],["situar","situeren","sitú","situ"],
  ["evaluar","evalueren","evalú","evalu"],["graduar","afstuderen/regelen","gradú","gradu"],["acentuar","accentueren","acentú","acentu"],
  ["efectuar","uitvoeren","efectú","efectu"],["insinuar","insinueren","insinú","insinu"],["habituar","gewennen","habitú","habitu"],
  ["exceptuar","uitzonderen","exceptú","exceptu"],["perpetuar","vereeuwigen","perpetú","perpetu"],["atenuar","verzachten","atenú","atenu"]
].map(p=>({i:p[0],n:p[1],pres:[p[2]+"o",p[2]+"as",p[2]+"a",p[3]+"amos",p[3]+"áis",p[2]+"an"]}));

/* ===================== 12 · overige expliciete onregelmatigheden ===================== */
const XSPEC = [
  {i:"vaciar",n:"leegmaken",pres:["vacío","vacías","vacía","vaciamos","vaciáis","vacían"]},
  {i:"reunir",n:"verzamelen/bijeenbrengen",pres:["reúno","reúnes","reúne","reunimos","reunís","reúnen"]},
  {i:"prohibir",n:"verbieden",pres:["prohíbo","prohíbes","prohíbe","prohibimos","prohibís","prohíben"]},
  {i:"freír",n:"bakken/frituren",pres:["frío","fríes","fríe","freímos","freís","fríen"]},
  {i:"aislar",n:"isoleren",pres:["aíslo","aíslas","aísla","aislamos","aisláis","aíslan"]},
  {i:"rehusar",n:"weigeren",pres:["rehúso","rehúsas","rehúsa","rehusamos","rehusáis","rehúsan"]},
  {i:"avergonzar",n:"beschamen",pres:["avergüenzo","avergüenzas","avergüenza","avergonzamos","avergonzáis","avergüenzan"]}
];

/* ===================== 13 · SUPPLEMENT (naar ~1000) ===================== */
const XSUP_REG = XR([
  /* -ar */
  ["acariciar","strelen"],["agrupar","groeperen"],["ahorrar","sparen"],["anotar","noteren"],
  ["arriesgar","riskeren"],["atormentar","kwellen"],["brindar","toosten/bieden"],["calificar","beoordelen"],
  ["castigar","straffen"],["cavar","graven"],["cepillar","borstelen"],["circular","circuleren"],
  ["coleccionar","verzamelen"],["congelar","invriezen"],["contactar","contacteren"],["cultivar","verbouwen"],
  ["decepcionar","teleurstellen"],["demandar","eisen/aanklagen"],["denunciar","aangeven"],["descifrar","ontcijferen"],
  ["despachar","afhandelen"],["destinar","bestemmen"],["dictar","dicteren"],["disfrazar","vermommen"],
  ["divulgar","verspreiden"],["donar","doneren"],["embarcar","inschepen"],["empeñar","verpanden"],
  ["encajar","passen/inpassen"],["envidiar","benijden"],["escanear","scannen"],["estimar","schatten/waarderen"],
  ["estimular","stimuleren"],["extrañar","missen"],["facturar","factureren"],["figurar","voorkomen"],
  ["filmar","filmen"],["filtrar","filteren"],["fundar","stichten"],["humillar","vernederen"],
  ["igualar","gelijkmaken"],["implantar","implanteren"],["impulsar","aandrijven"],["inaugurar","inhuldigen"],
  ["inclinar","neigen/buigen"],["indignar","verontwaardigen"],["inquietar","verontrusten"],["inspeccionar","inspecteren"],
  ["inundar","overstromen"],["inventar","uitvinden"],["invocar","aanroepen"],["jalar","trekken"],
  ["ladrar","blaffen"],["matricular","inschrijven"],["nivelar","nivelleren"],["obsequiar","schenken"],
  ["parpadear","knipperen"],["perforar","doorboren"],["pisar","betreden/trappen"],["portar","dragen"],
  ["precisar","preciseren/nodig hebben"],["predicar","preken"],["presenciar","bijwonen"],["privar","beroven"],
  ["propagar","voortplanten"],["prosperar","gedijen"],["purificar","zuiveren"],["ratificar","bekrachtigen"],
  ["reciclar","recycleren"],["recolectar","oogsten"],["reformar","hervormen"],["registrar","registreren"],
  ["remediar","verhelpen"],["retar","uitdagen"],["revelar","onthullen/ontwikkelen"],["roncar","snurken"],
  ["sobornar","omkopen"],["sofocar","verstikken/blussen"],["tasar","taxeren"],["tornar","terugkeren/maken"],
  ["traficar","handelen (illegaal)"],["trepar","klimmen"],["vacunar","inenten"],["validar","valideren"],
  /* -er */
  ["prender","aansteken/vastpakken"],["atrever","durven"],["corromper","corrumperen"],["lamer","likken"],
  ["embeber","doordrenken"],
  /* -ir */
  ["presumir","opscheppen/vermoeden"],["gruñir","grommen"],["engullir","schrokken"],["bullir","borrelen"],
  ["evadir","ontwijken"],["invadir","binnenvallen"],["subsistir","voortbestaan"],["persistir","volharden"],
  ["desistir","afzien"],["consistir","bestaan uit"],["coincidir","samenvallen"],["residir","wonen/zetelen"],
  ["presidir","voorzitten"],["disuadir","afraden"]
]);
const XSUP_IE = [
  {i:"enterrar",n:"begraven",c:"ie"},{i:"desterrar",n:"verbannen",c:"ie"},{i:"encomendar",n:"toevertrouwen",c:"ie"},
  {i:"asentar",n:"neerzetten/vastleggen",c:"ie"},{i:"recalentar",n:"opnieuw opwarmen",c:"ie"},{i:"sosegar",n:"kalmeren",c:"ie"},
  {i:"tentar",n:"verleiden/betasten",c:"ie"},{i:"remendar",n:"verstellen",c:"ie"},{i:"escarmentar",n:"lesje leren",c:"ie"}
];
const XSUP_UE = [
  {i:"recostar",n:"laten leunen",c:"ue"},{i:"moler",n:"malen",c:"ue"},{i:"soldar",n:"lassen",c:"ue"},
  {i:"revolver",n:"omroeren/doorwoelen",c:"ue"},{i:"repoblar",n:"herbevolken",c:"ue"},{i:"sobrevolar",n:"overvliegen",c:"ue"},
  {i:"engrosar",n:"aandikken/aangroeien",c:"ue"},{i:"denostar",n:"beschimpen",c:"ue"},{i:"recontar",n:"hertellen",c:"ue"}
];
const XSUP_I = [
  {i:"embestir",n:"aanvallen/stormen",c:"i"},{i:"colegir",n:"afleiden/concluderen",c:"i",o:"ger"}
];
const XSUP_ZCO = [
  ["comparecer","verschijnen"],["acontecer","gebeuren"],["enrojecer","rood worden/blozen"],["resplandecer","stralen"],
  ["prevalecer","overheersen"],["empobrecer","verarmen"],["adormecer","in slaap wiegen"],["guarnecer","garneren/versterken"]
].map(p=>({i:p[0],n:p[1],o:"zco",irr:true}));
const XSUP_YO = [
  {i:"interponer",n:"tussenplaatsen",yo:"interpongo",irr:true},{i:"anteponer",n:"vooropstellen",yo:"antepongo",irr:true},
  {i:"contraponer",n:"tegenover stellen",yo:"contrapongo",irr:true},{i:"transponer",n:"verplaatsen/omzetten",yo:"transpongo",irr:true},
  {i:"sobreponer",n:"overheen leggen",yo:"sobrepongo",irr:true},{i:"yuxtaponer",n:"naast elkaar plaatsen",yo:"yuxtapongo",irr:true}
];
const XSUP_UIR = [
  ["destituir","afzetten"],["prostituir","prostitueren"],["inmiscuir","zich inmengen"]
].map(p=>({i:p[0],n:p[1],o:"uir",irr:true}));

/* ===================== samenvoegen ===================== */
window.MotorData.esVerbosExtra = [].concat(
  XREG, XIE, XUE, XI, XZCO, XUIR, XGER, XZO, XYO, XACC_I, XACC_U, XSPEC,
  XSUP_REG, XSUP_IE, XSUP_UE, XSUP_I, XSUP_ZCO, XSUP_YO, XSUP_UIR
);
