/* De 300 frequentste Spaanse infinitieven, getagd op presente-klasse.
   c = klasse: reg | ie | ue | i | uue | ie2(adquirir) | hue(oler)
   o = orthografische yo-wijziging: ger | zco | zo | guir | uir
   yo = expliciete yo-vorm | pres = volledige 6 vormen (echt onregelmatig)
   irr = markeer als 'onregelmatig' in het sorteerspel (eigen yo-onregelmatigheid)
   Presente wordt nagerekend uit deze tags — nooit vrij gegenereerd. */
window.MotorData = window.MotorData || {};

const R = (t,list)=>list.map(p=>({i:p[0],n:p[1],c:"reg"}));  // regelmatig

const REG = [].concat(
  R("ar",[
    ["hablar","spreken"],["trabajar","werken"],["estudiar","studeren"],["escuchar","luisteren"],
    ["comprar","kopen"],["bailar","dansen"],["cantar","zingen"],["viajar","reizen"],
    ["tomar","nemen"],["mirar","kijken"],["llamar","bellen"],["cocinar","koken"],
    ["descansar","rusten"],["nadar","zwemmen"],["visitar","bezoeken"],["ayudar","helpen"],
    ["llevar","dragen"],["necesitar","nodig hebben"],["esperar","wachten"],["caminar","wandelen"],
    ["desayunar","ontbijten"],["cenar","avondeten"],["terminar","eindigen"],["llegar","aankomen"],
    ["buscar","zoeken"],["pagar","betalen"],["practicar","oefenen"],["usar","gebruiken"],
    ["entrar","binnengaan"],["dejar","laten"],["pasar","passeren"],["tratar","behandelen"],
    ["mandar","sturen"],["presentar","voorstellen"],["considerar","overwegen"],["crear","creëren"],
    ["formar","vormen"],["desarrollar","ontwikkelen"],["realizar","verwezenlijken"],["utilizar","gebruiken"],
    ["aceptar","aanvaarden"],["expresar","uitdrukken"],["preparar","voorbereiden"],["ganar","winnen"],
    ["gastar","uitgeven"],["cambiar","veranderen"],["preguntar","vragen"],["contestar","antwoorden"],
    ["explicar","uitleggen"],["indicar","aanwijzen"],["dedicar","wijden"],["sacar","eruit halen"],
    ["tocar","aanraken"],["acabar","afmaken"],["echar","gooien"],["saltar","springen"],
    ["señalar","aanduiden"],["apoyar","steunen"],["bajar","zakken"],["celebrar","vieren"],
    ["comentar","becommentariëren"],["disfrutar","genieten"],["durar","duren"],["enseñar","onderwijzen"],
    ["evitar","vermijden"],["funcionar","functioneren"],["guardar","bewaren"],["imaginar","zich voorstellen"],
    ["importar","belang hebben"],["informar","informeren"],["intentar","proberen"],["invitar","uitnodigen"],
    ["limpiar","schoonmaken"],["llorar","huilen"],["luchar","vechten"],["marcar","markeren"],
    ["mejorar","verbeteren"],["mezclar","mengen"],["notar","opmerken"],["observar","observeren"],
    ["olvidar","vergeten"],["ordenar","ordenen"],["organizar","organiseren"],["parar","stoppen"],
    ["participar","deelnemen"],["pintar","schilderen"],["prestar","lenen"],["quitar","weghalen"],
    ["regresar","terugkeren"],["reservar","reserveren"],["respetar","respecteren"],["resultar","blijken"],
    ["saludar","groeten"],["separar","scheiden"],["superar","overwinnen"],["tardar","talmen"],
    ["viajar2","reizen"],["arreglar","herstellen"],["aumentar","verhogen"],["bastar","volstaan"],
    ["dibujar","tekenen"],["descargar","downloaden"],["escapar","ontsnappen"],["felicitar","feliciteren"],
    ["acompañar","vergezellen"],["adivinar","raden"],["alquilar","huren"],["amar","beminnen"],
    ["apagar","uitzetten"],["atacar","aanvallen"],["avisar","verwittigen"],["calcular","berekenen"],
    ["callar","zwijgen"],["cazar","jagen"],["cobrar","innen"],["colocar","plaatsen"],
    ["comparar","vergelijken"],["completar","voltooien"],["comunicar","communiceren"],["consultar","raadplegen"],
    ["contratar","aanwerven"],["controlar","controleren"],["copiar","kopiëren"],["cortar","snijden"],
    ["cuidar","verzorgen"],["desear","wensen"],["disculpar","verontschuldigen"],["doblar","vouwen"],
    ["enamorar","verliefd maken"],["encantar","betoveren"],["entregar","overhandigen"],["gritar","schreeuwen"],
    ["lavar","wassen"],["levantar","optillen"],["llenar","vullen"],["manejar","hanteren"],
    ["matar","doden"],["montar","opstijgen"],["obligar","verplichten"],["odiar","haten"],
    ["opinar","van mening zijn"],["pegar","plakken"],["perdonar","vergeven"],["preocupar","verontrusten"],
    ["publicar","publiceren"],["quemar","verbranden"],["regalar","cadeau geven"],["reparar","herstellen"],
    ["respirar","ademen"],["revisar","nakijken"],["secar","drogen"],["tirar","gooien"],
    ["votar","stemmen"],["cumplir","voldoen aan"]
  ]),
  R("er",[
    ["comer","eten"],["beber","drinken"],["aprender","leren"],["correr","rennen"],
    ["vender","verkopen"],["comprender","begrijpen"],["responder","antwoorden"],["deber","moeten"],
    ["temer","vrezen"],["meter","stoppen in"],["romper","breken"],["barrer","vegen"],
    ["sorprender","verrassen"],["depender","afhangen"],["prometer","beloven"],["esconder","verbergen"],
    ["aprender2","leren"],["coser","naaien"],["toser","hoesten"],["comprender2","begrijpen"]
  ]),
  R("ir",[
    ["vivir","wonen"],["subir","omhooggaan"],["recibir","ontvangen"],["decidir","beslissen"],
    ["compartir","delen"],["escribir","schrijven"],["abrir","openen"],["descubrir","ontdekken"],
    ["cubrir","bedekken"],["permitir","toelaten"],["existir","bestaan"],["ocurrir","gebeuren"],
    ["sufrir","lijden"],["discutir","bespreken"],["admitir","toegeven"],["describir","beschrijven"],
    ["dividir","delen"],["unir","verenigen"],["añadir","toevoegen"],["asistir","bijwonen"],
    ["insistir","aandringen"],["resistir","weerstaan"],["partir","vertrekken"],["imprimir","afdrukken"]
  ])
).filter(v=>!/2$/.test(v.i)); // dubbels met suffix '2' eruit

const SPECIAL = [
  /* echt onregelmatig */
  {i:"ser",n:"zijn",pres:["soy","eres","es","somos","sois","son"]},
  {i:"estar",n:"zijn (toestand)",pres:["estoy","estás","está","estamos","estáis","están"]},
  {i:"ir",n:"gaan",pres:["voy","vas","va","vamos","vais","van"]},
  {i:"haber",n:"hebben (hulpww.)",pres:["he","has","ha","hemos","habéis","han"]},
  {i:"oír",n:"horen",pres:["oigo","oyes","oye","oímos","oís","oyen"]},
  {i:"reír",n:"lachen",pres:["río","ríes","ríe","reímos","reís","ríen"]},
  {i:"sonreír",n:"glimlachen",pres:["sonrío","sonríes","sonríe","sonreímos","sonreís","sonríen"]},
  {i:"ver",n:"zien",pres:["veo","ves","ve","vemos","veis","ven"]},
  /* yo-onregelmatig (+ soms klasse) */
  {i:"tener",n:"hebben",c:"ie",yo:"tengo"},{i:"venir",n:"komen",c:"ie",yo:"vengo"},
  {i:"decir",n:"zeggen",c:"i",yo:"digo"},
  {i:"hacer",n:"doen/maken",yo:"hago",irr:true},{i:"poner",n:"zetten",yo:"pongo",irr:true},
  {i:"salir",n:"buitengaan",yo:"salgo",irr:true},{i:"traer",n:"brengen",yo:"traigo",irr:true},
  {i:"caer",n:"vallen",yo:"caigo",irr:true},{i:"valer",n:"waard zijn",yo:"valgo",irr:true},
  {i:"caber",n:"passen",yo:"quepo",irr:true},{i:"saber",n:"weten",yo:"sé",irr:true},
  {i:"dar",n:"geven",pres:["doy","das","da","damos","dais","dan"]},
  {i:"mantener",n:"onderhouden",c:"ie",yo:"mantengo"},{i:"obtener",n:"verkrijgen",c:"ie",yo:"obtengo"},
  {i:"contener",n:"bevatten",c:"ie",yo:"contengo"},{i:"detener",n:"tegenhouden",c:"ie",yo:"detengo"},
  {i:"proponer",n:"voorstellen",yo:"propongo",irr:true},{i:"suponer",n:"veronderstellen",yo:"supongo",irr:true},
  {i:"componer",n:"samenstellen",yo:"compongo",irr:true},{i:"deshacer",n:"ongedaan maken",yo:"deshago",irr:true},
  {i:"convenir",n:"passen/afspreken",c:"ie",yo:"convengo"},{i:"prevenir",n:"voorkomen",c:"ie",yo:"prevengo"},
  {i:"atraer",n:"aantrekken",yo:"atraigo",irr:true},{i:"predecir",n:"voorspellen",c:"i",yo:"predigo"},

  /* e→ie */
  {i:"pensar",n:"denken",c:"ie"},{i:"empezar",n:"beginnen",c:"ie"},{i:"comenzar",n:"beginnen",c:"ie"},
  {i:"entender",n:"begrijpen",c:"ie"},{i:"perder",n:"verliezen",c:"ie"},{i:"querer",n:"willen",c:"ie"},
  {i:"cerrar",n:"sluiten",c:"ie"},{i:"sentar",n:"doen zitten",c:"ie"},{i:"despertar",n:"wekken",c:"ie"},
  {i:"calentar",n:"opwarmen",c:"ie"},{i:"recomendar",n:"aanraden",c:"ie"},{i:"encender",n:"aansteken",c:"ie"},
  {i:"defender",n:"verdedigen",c:"ie"},{i:"gobernar",n:"besturen",c:"ie"},{i:"nevar",n:"sneeuwen",c:"ie"},
  {i:"negar",n:"ontkennen",c:"ie"},{i:"sentir",n:"voelen",c:"ie"},{i:"preferir",n:"verkiezen",c:"ie"},
  {i:"mentir",n:"liegen",c:"ie"},{i:"divertir",n:"vermaken",c:"ie"},{i:"convertir",n:"omzetten",c:"ie"},
  {i:"advertir",n:"waarschuwen",c:"ie"},{i:"hervir",n:"koken (vloeistof)",c:"ie"},{i:"herir",n:"verwonden",c:"ie"},

  /* o→ue */
  {i:"contar",n:"tellen/vertellen",c:"ue"},{i:"encontrar",n:"vinden",c:"ue"},{i:"mostrar",n:"tonen",c:"ue"},
  {i:"recordar",n:"herinneren",c:"ue"},{i:"acordar",n:"afspreken",c:"ue"},{i:"costar",n:"kosten",c:"ue"},
  {i:"volar",n:"vliegen",c:"ue"},{i:"soñar",n:"dromen",c:"ue"},{i:"sonar",n:"klinken",c:"ue"},
  {i:"probar",n:"proberen",c:"ue"},{i:"aprobar",n:"slagen",c:"ue"},{i:"almorzar",n:"lunchen",c:"ue"},
  {i:"acostar",n:"naar bed brengen",c:"ue"},{i:"volver",n:"terugkeren",c:"ue"},{i:"mover",n:"bewegen",c:"ue"},
  {i:"morder",n:"bijten",c:"ue"},{i:"doler",n:"pijn doen",c:"ue"},{i:"llover",n:"regenen",c:"ue"},
  {i:"poder",n:"kunnen",c:"ue"},{i:"dormir",n:"slapen",c:"ue"},{i:"morir",n:"sterven",c:"ue"},
  {i:"colgar",n:"ophangen",c:"ue"},{i:"rogar",n:"smeken",c:"ue"},{i:"forzar",n:"forceren",c:"ue"},
  {i:"oler",n:"ruiken",c:"hue"},

  /* e→i (alleen -ir) */
  {i:"pedir",n:"vragen/bestellen",c:"i"},{i:"servir",n:"dienen",c:"i"},{i:"repetir",n:"herhalen",c:"i"},
  {i:"medir",n:"meten",c:"i"},{i:"competir",n:"wedijveren",c:"i"},{i:"despedir",n:"afscheid nemen",c:"i"},
  {i:"impedir",n:"beletten",c:"i"},{i:"vestir",n:"kleden",c:"i"},{i:"gemir",n:"kreunen",c:"i"},
  {i:"rendir",n:"opbrengen",c:"i"},{i:"seguir",n:"volgen",c:"i",o:"guir"},{i:"conseguir",n:"verkrijgen",c:"i",o:"guir"},
  {i:"perseguir",n:"achtervolgen",c:"i",o:"guir"},{i:"elegir",n:"kiezen",c:"i",o:"ger"},{i:"corregir",n:"verbeteren",c:"i",o:"ger"},

  /* u→ue */
  {i:"jugar",n:"spelen",c:"uue"},
  /* i→ie */
  {i:"adquirir",n:"verwerven",c:"ie2",irr:true},

  /* orthografische yo (regelmatig behalve yo-spelling → getagd als onregelmatig) */
  {i:"conocer",n:"kennen",o:"zco",irr:true},{i:"parecer",n:"lijken",o:"zco",irr:true},
  {i:"aparecer",n:"verschijnen",o:"zco",irr:true},{i:"ofrecer",n:"aanbieden",o:"zco",irr:true},
  {i:"agradecer",n:"bedanken",o:"zco",irr:true},{i:"crecer",n:"groeien",o:"zco",irr:true},
  {i:"nacer",n:"geboren worden",o:"zco",irr:true},{i:"obedecer",n:"gehoorzamen",o:"zco",irr:true},
  {i:"pertenecer",n:"toebehoren",o:"zco",irr:true},{i:"merecer",n:"verdienen",o:"zco",irr:true},
  {i:"conducir",n:"besturen",o:"zco",irr:true},{i:"producir",n:"produceren",o:"zco",irr:true},
  {i:"traducir",n:"vertalen",o:"zco",irr:true},{i:"reducir",n:"verminderen",o:"zco",irr:true},
  {i:"vencer",n:"verslaan",o:"zo",irr:true},{i:"convencer",n:"overtuigen",o:"zo",irr:true},
  {i:"coger",n:"pakken",o:"ger",irr:true},{i:"recoger",n:"oprapen",o:"ger",irr:true},
  {i:"escoger",n:"uitkiezen",o:"ger",irr:true},{i:"proteger",n:"beschermen",o:"ger",irr:true},
  {i:"dirigir",n:"leiden",o:"ger",irr:true},{i:"exigir",n:"eisen",o:"ger",irr:true},
  {i:"distinguir",n:"onderscheiden",o:"guir",irr:true},
  {i:"construir",n:"bouwen",o:"uir",irr:true},{i:"destruir",n:"vernietigen",o:"uir",irr:true},
  {i:"incluir",n:"insluiten",o:"uir",irr:true},{i:"concluir",n:"besluiten",o:"uir",irr:true},
  {i:"huir",n:"vluchten",o:"uir",irr:true},{i:"contribuir",n:"bijdragen",o:"uir",irr:true},
  {i:"influir",n:"beïnvloeden",o:"uir",irr:true},{i:"sustituir",n:"vervangen",o:"uir",irr:true}
];

window.MotorData.esVerbos = REG.concat(SPECIAL);
