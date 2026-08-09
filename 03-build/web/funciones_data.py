#!/usr/bin/env python3
# C4 — GEDEELDE datalaag «funciones comunicativas» (doorlopende, groeiende ruggengraat).
# Elke functie is uit de sitcom-fragmenten afgeleid en groeit doorheen de units (uptrade + recycling).
# Bron van waarheid voor: het banco-component (gen_c4_funciones.py) én matrix C (docentdossier).

# Elke functie: id · es (label) · nl (steun) · cefr (A1-descriptor) · code (C4-doelcode, docentenpagina) ·
#   exp = {unit: [exponentes]} — de formules die per unit worden aangebracht/uitgebreid.
# intro-unit = min(exp). Een latere exp-key bij een bestaande functie = «subió de nivel» (uptrade).
FUNCIONES = [
 {"id":"F01","es":"Saludar y despedirse","nl":"groeten en afscheid nemen",
  "cefr":"A1 · establecer contacto social","code":"C4-GE-1",
  "exp":{1:["Hola","Adiós","Hasta luego"],
         2:["Buenos días / tardes / noches","¡Buenas!","Hasta mañana","¡Nos vemos!"]}},
 {"id":"F02","es":"Presentarse y presentar a alguien","nl":"jezelf/iemand voorstellen",
  "cefr":"A1 · presentarse","code":"C4-SP-1",
  "exp":{1:["Me llamo…","(Yo) soy…","Encantado/a"],
         3:["Soy de… (país)","Soy español/a · mexicano/a · belga"],
         4:["Esta es mi madre","Este es mi padre","Es mi hermano/a"]}},
 {"id":"F03","es":"Pedir y dar información personal","nl":"persoonlijke info vragen & geven",
  "cefr":"A1 · dar y pedir datos personales","code":"C4-GE-1",
  "exp":{1:["¿Cómo te llamas?","¿Y tú?"],
         3:["¿De dónde eres?","¿De qué país?","¿Qué idiomas hablas?"]}},
 {"id":"F04","es":"Reaccionar con cortesía","nl":"beleefd reageren",
  "cefr":"A1 · fórmulas de cortesía","code":"C4-GE-2",
  "exp":{2:["Por favor","Gracias · Muchas gracias","De nada","Perdona"]}},
 {"id":"F05","es":"Preguntar y decir cómo estoy","nl":"vragen/zeggen hoe het gaat",
  "cefr":"A1 · preguntar/expresar el estado","code":"C4-GE-1",
  "exp":{2:["¿Qué tal? · ¿Cómo estás?","Estoy bien / cansado-a / ocupado-a","Regular"],
         7:["Estamos todos bien / tranquilos","¿Estáis bien?","estar = toestand · ser = wie/wat je bent"]}},
 {"id":"F06","es":"Pedir algo","nl":"iets vragen/bestellen",
  "cefr":"A1 · peticiones básicas","code":"C4-GE-3",
  "exp":{3:["…, por favor","¿Me da…?"],
         14:["Yo quiero…","Para mí, …","Yo prefiero algo dulce","La cuenta, por favor"]}},
 {"id":"F07","es":"Contar (números 0–20)","nl":"tellen",
  "cefr":"A1 · números","code":"C4-WS-1",
  "exp":{3:["uno · dos · tres · cinco","diez · veinte"],
         8:["las horas: la una · las doce","y media · y cuarto · menos cuarto","en veinte minutos"],
         13:["los precios: dos con veinte · uno con ochenta","un kilo · medio kilo · una lata",
             "el euro y los céntimos"]}},
 {"id":"F08","es":"Gestionar la comprensión","nl":"om verduidelijking vragen (luisterstrategie)",
  "cefr":"A1 · estrategias de comprensión","code":"C4-STR-1",
  "exp":{1:["¿Cómo?","Otra vez, por favor"],
         2:["¿Puedes repetir?"],
         3:["Más despacio, por favor","No entiendo"],
         8:["¿Sí? · No te oigo (nada)","¿Puedes hablar más despacio?"]}},
 {"id":"F09","es":"Hablar de la familia","nl":"over je familie praten",
  "cefr":"A1 · la familia y la posesión","code":"C4-WS-1",
  "exp":{4:["mi madre · mi padre","mi hermano/a · mi abuelo/a","el tío / la tía","la hermana de María (de + nombre)"]}},
 {"id":"F10","es":"Describir a alguien","nl":"iemand beschrijven (fysiek & karakter)",
  "cefr":"A1 · descripción de personas","code":"C4-SP-2",
  "exp":{4:["es alto/a · bajo/a · guapo/a","es simpático/a · divertido/a · inteligente","es muy… · un poco…"],
         12:["tiene los ojos azules","está fuerte · está cansado (ahora)",
             "lleva una chaqueta negra","es guapo (siempre) ↔ está fuerte (ahora)"]}},
 {"id":"F11","es":"Identificar objetos","nl":"voorwerpen benoemen (¿qué es esto?)",
  "cefr":"A1 · identificar cosas","code":"C4-WS-1",
  "exp":{5:["¿Qué es esto?","Esto es un/una…","Esto son… (meervoud)","un libro · una mesa (el/la)"]}},
 {"id":"F12","es":"Decir qué hay y para qué sirve","nl":"zeggen wat er is / waarvoor iets dient",
  "cefr":"A1 · existencia y función","code":"C4-WS-1",
  "exp":{5:["¿Hay…? · (No) hay…","Sí que hay…","… que sirve para + infinitivo","sirve para abrir · beber · descansar"]}},
 {"id":"F13","es":"Ubicar cosas · decir dónde está","nl":"situeren: zeggen waar iets is",
  "cefr":"A1 · localización en el espacio","code":"C4-TS-3",
  "exp":{6:["¿Dónde está…? · está en…","encima de · debajo de · dentro de","al lado de · delante de · detrás de","Hay … en la cocina · del (de+el)"]}},
 {"id":"F14","es":"Pedir y dar permiso","nl":"om toestemming vragen / geven",
  "cefr":"A1 · pedir/dar permiso","code":"C4-GE-2",
  "exp":{6:["¿Puedo…? · ¿Puedes…?","Sí, puedes… · Aquí no","puedes ir fuera","¿Puedo fumar? · ¿Puedes venir?"]}},
 {"id":"F15","es":"Hablar del trabajo","nl":"over je werk/beroep praten",
  "cefr":"A1 · profesión y lugar de trabajo","code":"C4-SP-1",
  "exp":{7:["¿A qué te dedicas? · ¿En qué trabajas?","Soy profesor/a · escritor/a · actriz","Trabajo en una tienda · una oficina","ser + profesión (zonder un/una)"]}},
 {"id":"F16","es":"Especular y adivinar","nl":"gissen & vermoedens uiten",
  "cefr":"A1 · expresar hipótesis sencillas","code":"C4-STR-1",
  "exp":{7:["Puede ser… (escritora)","¿Trabaja en una tienda?","Creo que es…","¡Ya lo sé! · ¿O algo parecido?"]}},
 {"id":"F17","es":"Decir y preguntar la hora","nl":"de tijd vragen & zeggen",
  "cefr":"A1 · la hora y los días","code":"C4-WS-1",
  "exp":{8:["¿Qué hora es? · Es la una · Son las ocho","y media · y cuarto · menos cuarto · en punto",
            "¿A qué hora? · a las doce","el lunes · los lunes · el fin de semana"]}},
 {"id":"F18","es":"Quedar con alguien","nl":"een afspraak maken",
  "cefr":"A1 · concertar una cita","code":"C4-GE-3",
  "exp":{8:["¿Quieres quedar (esta noche)?","Quedamos a las… · en mi casa","Más tarde · ahora mismo no puedo",
            "Es un poco pronto · un poco tarde","Hasta ahora · te veo en veinte minutos"],
         9:["¿Quedamos para ir al cine?","No puedo. Tengo que…","¿Y esta tarde? ¿Y mañana?"]}},
 {"id":"F19","es":"Hablar de planes","nl":"over plannen praten (ir a + inf.)",
  "cefr":"A1 · expresar planes e intenciones","code":"C4-TS-4",
  "exp":{9:["Voy a + infinitivo (voy a preparar café)","Vamos a dormir un poquito más","El domingo voy a quedar con amigas",
            "¿Vamos a pasear?"]}},
 {"id":"F20","es":"Expresar obligación","nl":"zeggen wat je moet doen (tener que + inf.)",
  "cefr":"A1 · expresar obligación","code":"C4-TS-3",
  "exp":{9:["Tengo que + infinitivo (tengo que trabajar)","Tengo cosas que hacer","¿Tienes que hacer algo?",
            "tengo hambre · tengo sueño (tener + naamwoord)"],
         10:["Hay que + infinitivo (algemeen: hay que limpiar)","No tienes que molestarte"]}},
 {"id":"F21","es":"Ofrecer y pedir ayuda","nl":"hulp aanbieden & vragen",
  "cefr":"A1 · ofrecer/pedir ayuda","code":"C4-GE-3",
  "exp":{10:["Yo te ayudo · ¿Te ayudo?","¿Qué tengo que hacer?","No es molestia","Déjame, lo hago yo"]}},
 {"id":"F22","es":"Decir lo que sé hacer","nl":"zeggen wat je kunt/weet te doen (saber + inf.)",
  "cefr":"A1 · expresar habilidad","code":"C4-SP-2",
  "exp":{10:["Sé + infinitivo (sé pasar la aspiradora)","¿Sabes…? · ¿Sabes cómo funciona?",
             "Sabemos… (nosotros)","Claro que sé"]}},

 {"id":"F23","es":"Comprar: preguntar precio, talla y cantidad","nl":"kopen: prijs, maat en hoeveelheid",
  "cefr":"A1 · transacción de compra","code":"C4-SP-1",
  "exp":{12:["¿Cuánto cuesta?","¿Qué talla lleva?","¿La tiene en azul?",
             "Me queda ancho/estrecho","Me queda bien"],
         13:["¿Cuánto cuestan los tomates?","Un kilo, por favor","Es una oferta",
             "Es caro/barato","¿Dónde venden…?"]}},
 {"id":"F24","es":"Hablar del tiempo que hace","nl":"over het weer praten",
  "cefr":"A1 · describir el entorno","code":"C4-WS-1",
  "exp":{11:["Hace sol / frío / calor","Está nublado","Llueve","Nieva","¿Qué tiempo hace?"]}},
 {"id":"F25","es":"Reaccionar con una exclamación","nl":"reageren met een uitroep",
  "cefr":"A1 · expresar una reacción","code":"C4-GE-2",
  "exp":{11:["¡Qué frío!","¡Qué calor!","¡Qué bonito!"],
         14:["¡Qué rico!","¡Qué tensión!","¡Qué bien!"]}},

 # F26 (hotel) stond hier voor U13. De aflevering blijkt over de markt te gaan
 # en er is in geen van de veertien video's een hotelscène, dus de functie hoort
 # nergens: ze zou in het repertoire staan als iets dat de leerling geleerd
 # heeft, terwijl er geen les bij hoort. Het reserveren zelf komt in C5 terug.
 # {"id":"F26","es":"Reservar y registrarse en un hotel", … zie git-geschiedenis}

 {"id":"F27","es":"Decir lo que te gusta y con qué frecuencia","nl":"zeggen wat je graag doet",
  "cefr":"A1 · expresar gustos y preferencias","code":"C4-SP-2",
  "exp":{11:["Me gusta / te gusta / le gusta","Me encanta…","No soporto…","Prefiero…",
             "siempre · a menudo · a veces · casi nunca · nunca"]}},
 {"id":"F28","es":"Hablar de cómo te sientes","nl":"zeggen hoe jij je voelt",
  "cefr":"A1 · sensaciones físicas","code":"C4-GE-2",
  "exp":{11:["Tengo frío / calor","Tengo hambre / sueño","Estoy cansado/a"],
         13:["Estoy enfermo/a","No tienes muy buen aspecto","Tienes que cuidarte"]}},

 {"id":"F29","es":"Hablar de la rutina diaria","nl":"over je dagelijkse routine praten",
  "cefr":"A1 · acciones habituales (verbos reflexivos)","code":"C4-TS-4",
  "exp":{12:["Me levanto · me ducho · me peino","Te duchas · te peinas",
             "Se afeita","Vosotros os ducháis","Me pongo la chaqueta"]}},
 {"id":"F30","es":"Preguntar y dar la razón","nl":"naar de reden vragen en ze geven",
  "cefr":"A1 · causa y consecuencia","code":"C4-TS-3",
  "exp":{13:["¿Por qué…?","Porque…","Por eso…","No lo sé"]}},
 {"id":"F31","es":"Desenvolverse en un restaurante","nl":"je redden in een restaurant",
  "cefr":"A1 · transacción de restaurante","code":"C4-SP-1",
  "exp":{14:["Mesa para cuatro, por favor","¿Quiere algo de beber?",
             "De primero… · de segundo… · de postre…","Les recomiendo…",
             "La cuenta, por favor"]}},
 {"id":"F32","es":"Mostrar acuerdo y desacuerdo","nl":"het eens of oneens zijn",
  "cefr":"A1 · expresar (des)acuerdo","code":"C4-GE-2",
  "exp":{14:["Yo también","Yo tampoco","Yo sí","Yo no","Exacto"]}},
 {"id":"F33","es":"Valorar la comida y las personas","nl":"eten en mensen beoordelen",
  "cefr":"A1 · valorar con el superlativo","code":"C4-SP-2",
  "exp":{14:["Está buenísimo/a","Es guapísimo/a","Son simpatiquísimos",
             "Está muy bueno","¡Qué rico!"]}},
]
FMAP={f["id"]:f for f in FUNCIONES}

# ¿Qué hacen con el idioma? — noticing uit de scène van elke unit (cita → función-id).
NOTICING={
 1:[("«¡Hola! ¿Qué tal?»","F01"),("«Me llamo…»","F02"),("«¿Cómo te llamas?»","F03"),("«¿Cómo? Otra vez.»","F08")],
 2:[("«Buenos días. / Buenas tardes.»","F01"),("«¿Cómo estás?»","F05"),("«Estoy ocupada / cansada.»","F05"),("«Adiós. Hasta luego.»","F01")],
 3:[("«Buenas noches.»","F01"),("«¿De dónde eres? ¿De qué país?»","F03"),("«Soy de Argelia. Eres argelina.»","F02"),
    ("«¿Habla usted francés?»","F03"),("«Dinero, por favor.»","F06"),("«Uno, dos, tres… veinte.»","F07")],
 4:[("«Esta es mi madre.»","F02"),("«Es muy elegante, pero un poco gorda.»","F10"),("«Paula es la hermana de María.»","F09"),
    ("«El tío Fermín, el guapo de la familia.»","F09"),("«Es muy alto y muy fuerte.»","F10")],
 5:[("«¿Qué es esto?»","F11"),("«Esto es un sofá.»","F11"),("«Sirve para descansar.»","F12"),
    ("«¿Hay un ordenador?»","F12"),("«Esto son mis llaves.»","F11")],
 6:[("«Hay cosas encima de las sillas.»","F13"),("«Debajo de la cama.»","F13"),("«Dentro del frigorífico…»","F13"),
    ("«¿Puedo fumar?»","F14"),("«Aquí no, pero puedes ir fuera.»","F14")],
 7:[("«Puede ser escritora.»","F16"),("«¿Trabaja en una tienda?»","F16"),("«Es profesora.»","F15"),
    ("«Yo trabajo aquí, tú trabajas aquí.»","F15"),("«Estamos todos bien.»","F05")],
 8:[("«¿Qué hora es? ¿Las ocho y media?»","F17"),("«¿A qué hora? Mejor a las doce.»","F17"),
    ("«¿Quieres quedar esta noche?»","F18"),("«Quedamos en mi casa.»","F18"),
    ("«No te oigo nada. ¿Puedes hablar más despacio?»","F08"),("«Te veo en veinte minutos.»","F07")],
 9:[("«Voy a preparar café.»","F19"),("«Vamos a dormir un poquito más.»","F19"),
    ("«Tengo que pasear al perro.»","F20"),("«Tengo cosas que hacer.»","F20"),
    ("«¿Quedamos para ir al cine?»","F18"),("«Tengo sueño. ¿No tienes sueño?»","F20")],
 10:[("«Yo te ayudo.»","F21"),("«¿Qué tengo que hacer?»","F21"),("«No es molestia.»","F21"),
     ("«Hay que limpiar esto.»","F20"),("«¿Sabes pasar la aspiradora?»","F22"),
     ("«Los hombres también sabemos pasar la aspiradora.»","F22")],

 11:[("«Siempre hace buen tiempo en Canarias.»","F24"),
     ("«Pero hace un frío… Nunca hace ese frío en Madrid.»","F24"),
     ("«Me gusta hacer submarinismo.»","F27"),
     ("«A ella también le gusta hacer submarinismo.»","F27"),
     ("«Casi nunca voy a la ópera.»","F27"),
     ("«Voy al gimnasio tres veces por semana.»","F27"),
     ("«¡Qué bien!»","F25"),
     ("«A mí me gusta más el frío.»","F27")],
 12:[("«Paul lleva una chaqueta negra, buena.»","F10"),
     ("«Yo, en cambio, llevo un jersey verde, barato.»","F10"),
     ("«Paul es alto y yo no.»","F10"),
     ("«Paul está fuerte.»","F10"),
     ("«¿Paul se afeita?»","F29"),
     ("«La gente por las mañanas se ducha, se peina.»","F29"),
     ("«Vosotros os ducháis, os peináis.»","F29"),
     ("«A Paul la ropa le queda muy bien.»","F23")],
 13:[("«¿Cuánto cuestan los tomates?»","F23"),
     ("«Dos con veinte el kilo.»","F07"),
     ("«Es una oferta, son baratas.»","F23"),
     ("«¿Dónde venden pescado fresco?»","F23"),
     ("«Estoy enfermo, por eso no voy a la academia.»","F30"),
     ("«¿Por qué? No lo sé.»","F30"),
     ("«No tienes muy buen aspecto.»","F28")],
 14:[("«Mesa para cuatro. Esa, si puede ser.»","F31"),
     ("«¿Quieren algo de beber mientras miran el menú?»","F31"),
     ("«De carne les recomiendo el cordero.»","F31"),
     ("«Yo también estoy encantada.»","F32"),
     ("«Yo tampoco quiero vino.»","F32"),
     ("«Yo prefiero algo dulce.»","F06"),
     ("«Paella, excelente, y calamares buenísimos.»","F33"),
     ("«Tarta de chocolate, ¡qué rica!»","F25")],
}
# welke functies de eindtaak van elke unit combineert (afzender·ontvanger·doel — recycling zichtbaar).
TAREA_FUN={1:["F01","F02","F03"],2:["F01","F05","F04"],3:["F02","F03","F08"],4:["F09","F10","F02"],5:["F11","F12","F10"],6:["F13","F12","F14"],7:["F15","F16","F03"],8:["F17","F18","F07"],9:["F19","F20","F18"],10:["F21","F22","F20"],11:["F24","F27","F28"],12:["F10","F29","F23"],13:["F23","F07","F30"],14:["F31","F06","F32","F33"]}
TAREA_TITEL={1:"Mi presentación",2:"Un día de saludos",3:"Mi mapa · ¿de dónde eres?",4:"Mi árbol de familia",5:"Diccionario de la clase",6:"Plano de mi casa",7:"¿Quién soy? · adivina",8:"Mi horario",9:"Mi finde",10:"¿Quién hace qué?",11:"El tiempo y mis vacaciones",12:"El desfile de la clase",13:"Mi lista de la compra",14:"La cena del año"}

def funciones_hasta(unit):
    """Alle functies met intro-unit <= unit (het cumulatieve repertoire tot hier)."""
    return [f for f in FUNCIONES if min(f["exp"]) <= unit]
def intro_unit(f): return min(f["exp"])
def status(f, unit):
    """'nueva' (deze unit geïntroduceerd) · 'nivel' (bestaande functie kreeg er deze unit bij) · ''."""
    iu=intro_unit(f)
    if iu==unit: return "nueva"
    if unit in f["exp"] and iu<unit: return "nivel"
    return ""

if __name__=="__main__":
    for u in (1,2,3):
        fs=funciones_hasta(u)
        nuevas=[f["id"] for f in fs if status(f,u)=="nueva"]
        nivel=[f["id"] for f in fs if status(f,u)=="nivel"]
        print(f"U{u}: {len(fs)} functies in repertoire · nuevas={nuevas} · subieron de nivel={nivel}")
