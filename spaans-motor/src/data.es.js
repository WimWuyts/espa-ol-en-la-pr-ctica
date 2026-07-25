/* Geverifieerde Spaanse dataset. Wordt bij de build ingelijmd in elk spel
   dat een generator gebruikt. Werkwoorden: onregelmatige vormen expliciet
   uitgeschreven, regelmatige via de vervoegingsmotor. */
window.MotorData = window.MotorData || {};
window.MotorData.es = {
  verbs: [
    /* regelmatig -ar */
    {i:"hablar",n:"spreken"},{i:"trabajar",n:"werken"},{i:"estudiar",n:"studeren"},
    {i:"escuchar",n:"luisteren"},{i:"comprar",n:"kopen"},{i:"bailar",n:"dansen"},
    {i:"cantar",n:"zingen"},{i:"viajar",n:"reizen"},{i:"tomar",n:"nemen, drinken"},
    {i:"mirar",n:"kijken"},{i:"llamar",n:"bellen, noemen"},{i:"cocinar",n:"koken"},
    {i:"descansar",n:"rusten"},{i:"nadar",n:"zwemmen"},{i:"visitar",n:"bezoeken"},
    {i:"ayudar",n:"helpen"},{i:"llevar",n:"dragen, meenemen"},{i:"necesitar",n:"nodig hebben"},
    {i:"esperar",n:"wachten, hopen"},{i:"caminar",n:"wandelen"},{i:"desayunar",n:"ontbijten"},
    {i:"cenar",n:"avondeten eten"},{i:"terminar",n:"eindigen"},{i:"llegar",n:"aankomen"},
    {i:"buscar",n:"zoeken"},{i:"pagar",n:"betalen"},{i:"practicar",n:"oefenen"},
    /* regelmatig -er */
    {i:"comer",n:"eten"},{i:"beber",n:"drinken"},{i:"aprender",n:"leren"},
    {i:"correr",n:"lopen, rennen"},{i:"vender",n:"verkopen"},{i:"comprender",n:"begrijpen"},
    {i:"responder",n:"antwoorden"},
    /* regelmatig -ir */
    {i:"vivir",n:"wonen, leven"},{i:"subir",n:"omhooggaan"},{i:"recibir",n:"ontvangen"},
    {i:"decidir",n:"beslissen"},{i:"compartir",n:"delen"},
    /* onregelmatig */
    {i:"ser",n:"zijn",pres:["soy","eres","es","somos","sois","son"],indef:["fui","fuiste","fue","fuimos","fuisteis","fueron"],imperf:["era","eras","era","éramos","erais","eran"]},
    {i:"estar",n:"zijn (toestand)",pres:["estoy","estás","está","estamos","estáis","están"],indef:["estuve","estuviste","estuvo","estuvimos","estuvisteis","estuvieron"]},
    {i:"ir",n:"gaan",pres:["voy","vas","va","vamos","vais","van"],indef:["fui","fuiste","fue","fuimos","fuisteis","fueron"],imperf:["iba","ibas","iba","íbamos","ibais","iban"]},
    {i:"tener",n:"hebben",pres:["tengo","tienes","tiene","tenemos","tenéis","tienen"],indef:["tuve","tuviste","tuvo","tuvimos","tuvisteis","tuvieron"],fs:"tendr"},
    {i:"hacer",n:"doen, maken",pres:["hago","haces","hace","hacemos","hacéis","hacen"],indef:["hice","hiciste","hizo","hicimos","hicisteis","hicieron"],fs:"har",part:"hecho"},
    {i:"poder",n:"kunnen",pres:["puedo","puedes","puede","podemos","podéis","pueden"],indef:["pude","pudiste","pudo","pudimos","pudisteis","pudieron"],fs:"podr"},
    {i:"querer",n:"willen, houden van",pres:["quiero","quieres","quiere","queremos","queréis","quieren"],indef:["quise","quisiste","quiso","quisimos","quisisteis","quisieron"],fs:"querr"},
    {i:"venir",n:"komen",pres:["vengo","vienes","viene","venimos","venís","vienen"],indef:["vine","viniste","vino","vinimos","vinisteis","vinieron"],fs:"vendr"},
    {i:"decir",n:"zeggen",pres:["digo","dices","dice","decimos","decís","dicen"],indef:["dije","dijiste","dijo","dijimos","dijisteis","dijeron"],fs:"dir",part:"dicho"},
    {i:"poner",n:"zetten, leggen",pres:["pongo","pones","pone","ponemos","ponéis","ponen"],indef:["puse","pusiste","puso","pusimos","pusisteis","pusieron"],fs:"pondr",part:"puesto"},
    {i:"salir",n:"buitengaan, vertrekken",pres:["salgo","sales","sale","salimos","salís","salen"],fs:"saldr"},
    {i:"saber",n:"weten, kunnen",pres:["sé","sabes","sabe","sabemos","sabéis","saben"],indef:["supe","supiste","supo","supimos","supisteis","supieron"],fs:"sabr"},
    {i:"dar",n:"geven",pres:["doy","das","da","damos","dais","dan"],indef:["di","diste","dio","dimos","disteis","dieron"]},
    {i:"ver",n:"zien",pres:["veo","ves","ve","vemos","veis","ven"],indef:["vi","viste","vio","vimos","visteis","vieron"],imperf:["veía","veías","veía","veíamos","veíais","veían"],part:"visto"},
    {i:"conocer",n:"kennen",pres:["conozco","conoces","conoce","conocemos","conocéis","conocen"]},
    {i:"jugar",n:"spelen",pres:["juego","juegas","juega","jugamos","jugáis","juegan"]},
    {i:"dormir",n:"slapen",pres:["duermo","duermes","duerme","dormimos","dormís","duermen"],indef:["dormí","dormiste","durmió","dormimos","dormisteis","durmieron"]},
    {i:"pedir",n:"vragen, bestellen",pres:["pido","pides","pide","pedimos","pedís","piden"],indef:["pedí","pediste","pidió","pedimos","pedisteis","pidieron"]},
    {i:"empezar",n:"beginnen",pres:["empiezo","empiezas","empieza","empezamos","empezáis","empiezan"]},
    {i:"volver",n:"terugkeren",pres:["vuelvo","vuelves","vuelve","volvemos","volvéis","vuelven"],part:"vuelto"},
    {i:"pensar",n:"denken",pres:["pienso","piensas","piensa","pensamos","pensáis","piensan"]},
    {i:"entender",n:"begrijpen",pres:["entiendo","entiendes","entiende","entendemos","entendéis","entienden"]},
    {i:"preferir",n:"liever hebben",pres:["prefiero","prefieres","prefiere","preferimos","preferís","prefieren"],indef:["preferí","preferiste","prefirió","preferimos","preferisteis","prefirieron"]},
    {i:"cerrar",n:"sluiten",pres:["cierro","cierras","cierra","cerramos","cerráis","cierran"]},
    {i:"encontrar",n:"vinden, tegenkomen",pres:["encuentro","encuentras","encuentra","encontramos","encontráis","encuentran"]},
    {i:"sentir",n:"voelen, spijtig vinden",pres:["siento","sientes","siente","sentimos","sentís","sienten"],indef:["sentí","sentiste","sintió","sentimos","sentisteis","sintieron"]},
    {i:"seguir",n:"volgen, verdergaan",pres:["sigo","sigues","sigue","seguimos","seguís","siguen"],indef:["seguí","seguiste","siguió","seguimos","seguisteis","siguieron"]},
    {i:"oír",n:"horen",pres:["oigo","oyes","oye","oímos","oís","oyen"],indef:["oí","oíste","oyó","oímos","oísteis","oyeron"],fs:"oir",fsReg:true},
    {i:"traer",n:"brengen",pres:["traigo","traes","trae","traemos","traéis","traen"],indef:["traje","trajiste","trajo","trajimos","trajisteis","trajeron"]},
    {i:"leer",n:"lezen",indef:["leí","leíste","leyó","leímos","leísteis","leyeron"]},
    {i:"escribir",n:"schrijven",part:"escrito"},
    {i:"abrir",n:"openen",part:"abierto"}
  ],
  /* Zelfstandige naamwoorden met lidwoord. m/f, incl. valstrikken. */
  nouns: [
    {w:"casa",g:"f",n:"huis"},{w:"libro",g:"m",n:"boek"},{w:"mesa",g:"f",n:"tafel"},
    {w:"perro",g:"m",n:"hond"},{w:"ciudad",g:"f",n:"stad"},{w:"coche",g:"m",n:"auto"},
    {w:"escuela",g:"f",n:"school"},{w:"amigo",g:"m",n:"vriend"},{w:"ventana",g:"f",n:"raam"},
    {w:"teléfono",g:"m",n:"telefoon"},{w:"puerta",g:"f",n:"deur"},{w:"gato",g:"m",n:"kat"},
    {w:"silla",g:"f",n:"stoel"},{w:"hermano",g:"m",n:"broer"},{w:"familia",g:"f",n:"gezin"},
    {w:"trabajo",g:"m",n:"werk"},{w:"comida",g:"f",n:"eten"},{w:"país",g:"m",n:"land"},
    {w:"universidad",g:"f",n:"universiteit"},{w:"pan",g:"m",n:"brood"},{w:"leche",g:"f",n:"melk"},
    {w:"árbol",g:"m",n:"boom"},{w:"flor",g:"f",n:"bloem"},{w:"sol",g:"m",n:"zon"},
    /* valstrikken op -a/-o */
    {w:"problema",g:"m",n:"probleem",trap:true},{w:"día",g:"m",n:"dag",trap:true},
    {w:"mapa",g:"m",n:"kaart",trap:true},{w:"programa",g:"m",n:"programma",trap:true},
    {w:"idioma",g:"m",n:"taal",trap:true},{w:"clima",g:"m",n:"klimaat",trap:true},
    {w:"mano",g:"f",n:"hand",trap:true},{w:"foto",g:"f",n:"foto",trap:true},
    {w:"moto",g:"f",n:"motor",trap:true},
    /* -ción / -dad zijn f */
    {w:"canción",g:"f",n:"lied"},{w:"estación",g:"f",n:"station"},
    {w:"habitación",g:"f",n:"kamer"},{w:"verdad",g:"f",n:"waarheid"}
  ]
};
