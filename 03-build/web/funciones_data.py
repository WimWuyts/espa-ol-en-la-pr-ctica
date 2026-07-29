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
  "exp":{2:["¿Qué tal? · ¿Cómo estás?","Estoy bien / cansado-a / ocupado-a","Regular"]}},
 {"id":"F06","es":"Pedir algo","nl":"iets vragen/bestellen",
  "cefr":"A1 · peticiones básicas","code":"C4-GE-3",
  "exp":{3:["…, por favor","¿Me da…?"]}},
 {"id":"F07","es":"Contar (números 0–20)","nl":"tellen",
  "cefr":"A1 · números","code":"C4-WS-1",
  "exp":{3:["uno · dos · tres · cinco","diez · veinte"]}},
 {"id":"F08","es":"Gestionar la comprensión","nl":"om verduidelijking vragen (luisterstrategie)",
  "cefr":"A1 · estrategias de comprensión","code":"C4-STR-1",
  "exp":{1:["¿Cómo?","Otra vez, por favor"],
         2:["¿Puedes repetir?"],
         3:["Más despacio, por favor","No entiendo"]}},
 {"id":"F09","es":"Hablar de la familia","nl":"over je familie praten",
  "cefr":"A1 · la familia y la posesión","code":"C4-WS-1",
  "exp":{4:["mi madre · mi padre","mi hermano/a · mi abuelo/a","el tío / la tía","la hermana de María (de + nombre)"]}},
 {"id":"F10","es":"Describir a alguien","nl":"iemand beschrijven (fysiek & karakter)",
  "cefr":"A1 · descripción de personas","code":"C4-SP-2",
  "exp":{4:["es alto/a · bajo/a · guapo/a","es simpático/a · divertido/a · inteligente","es muy… · un poco…"]}},
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
}
# welke functies de eindtaak van elke unit combineert (afzender·ontvanger·doel — recycling zichtbaar).
TAREA_FUN={1:["F01","F02","F03"],2:["F01","F05","F04"],3:["F02","F03","F08"],4:["F09","F10","F02"],5:["F11","F12","F10"],6:["F13","F12","F14"]}
TAREA_TITEL={1:"Mi presentación",2:"Un día de saludos",3:"Mi mapa · ¿de dónde eres?",4:"Mi árbol de familia",5:"Diccionario de la clase",6:"Plano de mi casa"}

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
