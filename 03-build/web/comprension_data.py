#!/usr/bin/env python3
# C4 — GEDEELDE datalaag «Lee y escucha» (leesvaardigheid + 2e luisterfragment per unit).
# Vul LECTURA[unit] / AUDIO[unit] met NotebookLM-output volgens het vaste format
# (zie 00-brondocumenten/prompts/C4_comprension_prompts.md). None = nog te genereren
# → de pagina toont dan een nette «binnenkort»-plek en print/PPT slaan het over.
#
# LECTURA[unit] = {tipo, contexto_nl, texto:[[spreker|"",zin]], global:[{q,opts,a}],
#                  detalle:[{q,vf}], transfer, glosario:[[es,nl]]}
# AUDIO[unit]   = {tipo, guion:[[spreker,zin]], tarea_nl, preguntas:[{q,opts,a}],
#                  glosario:[[es,nl]], rallentado:[...]}

LECTURA = {
 1: {  # ── NotebookLM-output (auteur), genormaliseerd naar het vaste format ──
   "tipo": "Chat de WhatsApp · presentaciones",
   "contexto_nl": "Sofía en Mateo sturen elkaar voor het eerst een WhatsApp-berichtje om kennis te maken.",
   "texto": [
     ["Sofía", "¡Hola! ¿Cómo estás?"],
     ["Mateo", "¡Hola! Bien, gracias. ¿Cómo te llamas?"],
     ["Sofía", "Me llamo Sofía. ¿Y tú?"],
     ["Mateo", "Yo soy Mateo. ¿De dónde eres?"],
     ["Sofía", "Soy de Bruselas. ¿Y tú?"],
     ["Mateo", "Soy de Madrid. ¡Encantado!"],
     ["Sofía", "¡Encantada! Adiós."],
     ["Mateo", "Hasta luego."],
   ],
   "global": [
     {"q": "¿De qué hablan Sofía y Mateo?", "opts": ["De sus aficiones y el colegio", "De su nombre y de dónde son", "De sus planes para el finde"], "a": 1},
     {"q": "¿Cómo está Mateo?", "opts": ["Bien", "Cansado", "Enfermo"], "a": 0},
   ],
   "detalle": [
     {"q": "Sofía es de Madrid.", "vf": False},
     {"q": "Mateo es de Madrid.", "vf": True},
     {"q": "Mateo está bien.", "vf": True},
     {"q": "Sofía dice «encantada».", "vf": True},
   ],
   "transfer": "¿Y tú? Preséntate: ¿cómo te llamas y de dónde eres?",
   "glosario": [["¿De dónde eres?", "Waar kom je vandaan?"], ["Soy de…", "Ik kom uit…"], ["Encantado/a", "Aangenaam"], ["Hasta luego", "Tot ziens"]],
 },
 2: {
   "tipo": "3 notas · saludos por el día",
   "contexto_nl": "Drie korte briefjes op drie momenten van de dag.",
   "texto": [
     ["", "🌅 Nota de Pablo: «¡Buenos días, mamá! Estoy bien, pero un poco cansado. ¡Hasta luego!»"],
     ["", "☀️ Nota de Sara: «Buenas tardes, Luis. ¿Qué tal? Yo estoy muy ocupada hoy. Gracias por todo.»"],
     ["", "🌙 Nota de Elena: «Buenas noches, papá. Estoy bien, pero un poco nerviosa. ¡Hasta mañana!»"],
   ],
   "global": [
     {"q": "¿Cuántas notas hay?", "opts": ["Dos", "Tres", "Cuatro"], "a": 1},
     {"q": "¿Cuándo escribe Elena?", "opts": ["Por la mañana", "Por la tarde", "Por la noche"], "a": 2},
   ],
   "detalle": [
     {"q": "Pablo está muy cansado.", "vf": False},
     {"q": "Sara está ocupada.", "vf": True},
     {"q": "Elena está un poco nerviosa.", "vf": True},
     {"q": "Sara escribe por la mañana.", "vf": False},
   ],
   "transfer": "¿Y tú? ¿Cómo estás hoy?",
   "glosario": [["un poco cansado", "een beetje moe"], ["ocupada", "druk"], ["nerviosa", "nerveus"], ["Hasta mañana", "tot morgen"]],
 },
 3: {
   "tipo": "3 fichas · foro internacional",
   "contexto_nl": "Drie tieners stellen zich voor op een internationaal forum.",
   "texto": [
     ["Mateo", "¡Hola! Me llamo Mateo. Soy de México y soy mexicano. Hablo español e inglés."],
     ["Lien", "Hola, soy Lien. Soy de Bélgica, soy belga. Hablo neerlandés, francés y un poco de español."],
     ["Sofía", "¡Hola a todos! Me llamo Sofía. Soy de Argentina, soy argentina. Hablo español y estudio francés."],
   ],
   "global": [
     {"q": "¿De qué país es Lien?", "opts": ["De México", "De Bélgica", "De Argentina"], "a": 1},
     {"q": "¿Quién habla tres idiomas?", "opts": ["Mateo", "Lien", "Sofía"], "a": 1},
   ],
   "detalle": [
     {"q": "Mateo es mexicano.", "vf": True},
     {"q": "Lien es española.", "vf": False},
     {"q": "Sofía habla español.", "vf": True},
     {"q": "Mateo habla francés.", "vf": False},
   ],
   "transfer": "¿Y tú? ¿De dónde eres y qué idiomas hablas?",
   "glosario": [["Soy de…", "Ik kom uit…"], ["belga", "Belgisch"], ["neerlandés", "Nederlands"], ["estudio", "ik leer/studeer"]],
 },
 4: {
   "tipo": "descripción de una foto de familia",
   "contexto_nl": "Een tiener beschrijft een foto van zijn familie.",
   "texto": [
     ["", "Esta es una foto de mi familia. Esta es mi madre. Se llama Carmen. Es alta y muy simpática."],
     ["", "Este es mi padre. Se llama Luis. Es un poco bajo, pero muy divertido."],
     ["", "Y esta es mi hermana, Ana. Es delgada y muy inteligente. ¡Es mi familia!"],
   ],
   "global": [
     {"q": "¿A quién describe el texto?", "opts": ["A sus amigos", "A su familia", "A su clase"], "a": 1},
     {"q": "¿Cómo se llama la madre?", "opts": ["Carmen", "Ana", "Luis"], "a": 0},
   ],
   "detalle": [
     {"q": "La madre es alta y simpática.", "vf": True},
     {"q": "El padre es muy alto.", "vf": False},
     {"q": "Ana es la hermana.", "vf": True},
     {"q": "Ana es inteligente.", "vf": True},
   ],
   "transfer": "¿Y tú? Describe a una persona de tu familia.",
   "glosario": [["Esta es mi madre", "dit is mijn moeder"], ["alta", "lang"], ["un poco bajo", "een beetje klein"], ["delgada", "slank"]],
 },
 5: {
   "tipo": "un mensaje · ¿qué hay en mi habitación?",
   "contexto_nl": "Leo stuurt een berichtje over zijn kamer.",
   "texto": [
     ["", "¡Hola! Esta es mi habitación. Hay una mesa, una silla y una cama."],
     ["", "En la mesa hay un ordenador y muchos libros. Sirven para estudiar."],
     ["", "También hay una ventana grande. Sirve para mirar la luna. ¡Me gusta mi habitación!"],
   ],
   "global": [
     {"q": "¿Qué describe Leo?", "opts": ["Su clase", "Su habitación", "Su mochila"], "a": 1},
     {"q": "¿Qué hay en la mesa?", "opts": ["Un sofá", "Un ordenador y libros", "Una televisión"], "a": 1},
   ],
   "detalle": [
     {"q": "Hay una cama en la habitación.", "vf": True},
     {"q": "No hay ventana.", "vf": False},
     {"q": "Los libros sirven para estudiar.", "vf": True},
     {"q": "La ventana es pequeña.", "vf": False},
   ],
   "transfer": "¿Y tú? ¿Qué hay en tu habitación?",
   "glosario": [["hay", "er is/zijn"], ["la ventana", "het raam"], ["sirven para", "dienen om"], ["Me gusta", "ik vind leuk"]],
 },
 6: {
   "tipo": "un mensaje · ¿cómo es mi casa?",
   "contexto_nl": "Sara beschrijft haar huis en waar de dingen staan.",
   "texto": [
     ["", "¡Hola! Esta es mi casa. Hay una cocina, un salón, un dormitorio y un cuarto de baño."],
     ["", "En la cocina hay un frigorífico. Dentro del frigorífico hay leche y fruta."],
     ["", "En el salón hay un sofá y una mesa. Encima de la mesa hay un libro y, debajo de la mesa, está mi bolso."],
     ["", "El gato está al lado de la ventana. ¡Me gusta mucho mi casa!"],
   ],
   "global": [
     {"q": "¿Qué describe Sara?", "opts": ["Su clase", "Su casa", "Su mochila"], "a": 1},
     {"q": "¿Dónde está el bolso?", "opts": ["Encima de la mesa", "Debajo de la mesa", "En la cocina"], "a": 1},
   ],
   "detalle": [
     {"q": "La casa tiene cuatro habitaciones.", "vf": True},
     {"q": "Dentro del frigorífico hay leche.", "vf": True},
     {"q": "El gato está encima de la mesa.", "vf": False},
     {"q": "No hay sofá en el salón.", "vf": False},
   ],
   "transfer": "¿Y tú? ¿Cómo es tu casa? ¿Qué hay en cada habitación?",
   "glosario": [["la cocina", "de keuken"], ["el frigorífico", "de koelkast"], ["encima de", "op/boven"], ["debajo de", "onder"], ["al lado de", "naast"]],
 },
 7: {
   "tipo": "un perfil · ¿a qué se dedican?",
   "contexto_nl": "Een klasblog stelt drie mensen en hun werk voor.",
   "texto": [
     ["", "¡Hola! Somos tres amigos y trabajamos en la misma calle."],
     ["", "Yo soy profesora. Trabajo en una academia de idiomas y estoy muy contenta."],
     ["", "Marco es dependiente. Trabaja en una tienda de ropa, pero hoy está cansado."],
     ["", "Y Elena es escritora. Trabaja en casa y también trabaja en una oficina los lunes."],
   ],
   "global": [
     {"q": "¿Cuántas personas se presentan?", "opts": ["Dos", "Tres", "Cuatro"], "a": 1},
     {"q": "¿Dónde trabaja la profesora?", "opts": ["En una tienda", "En una academia", "En una oficina"], "a": 1},
   ],
   "detalle": [
     {"q": "Marco trabaja en una tienda de ropa.", "vf": True},
     {"q": "Marco está muy contento hoy.", "vf": False},
     {"q": "Elena es actriz.", "vf": False},
     {"q": "Elena también trabaja en una oficina.", "vf": True},
   ],
   "transfer": "¿Y tú? ¿A qué te dedicas? (estudiante cuenta ook!) ¿Y tus padres?",
   "glosario": [["¿a qué se dedican?", "wat doen ze (voor werk)?"], ["la academia", "de (taal)school"], ["el/la dependiente/a", "de winkelbediende"], ["está cansado", "hij is moe"]],
 },
}

AUDIO = {
 1: {  # ── DEMO (U1) ──
   "tipo": "3 personas se presentan",
   "guion": [
     ["Ana", "¡Hola! Me llamo Ana. Soy estudiante. Estoy muy bien."],
     ["Diego", "Buenos días. Yo soy Diego. Encantado. Estoy un poco cansado."],
     ["Sofía", "Hola, me llamo Sofía. ¿Qué tal? Yo estoy bien, gracias."],
   ],
   "tarea_nl": "Vul de ficha in: hoe heet elke persoon en hoe voelt die zich?",
   "preguntas": [
     {"q": "¿Cuántas personas hablan?", "opts": ["Dos", "Tres", "Cuatro"], "a": 1},
     {"q": "¿Cómo se llama la primera persona?", "opts": ["Ana", "Diego", "Sofía"], "a": 0},
     {"q": "¿Cómo está Diego?", "opts": ["Un poco cansado", "Enfermo", "Ocupado"], "a": 0},
     {"q": "¿Quién está muy bien?", "opts": ["Ana", "Diego", "Sofía"], "a": 0},
   ],
   "glosario": [["estudiante", "leerling/student"], ["un poco", "een beetje"]],
   "rallentado": ["me llamo", "encantado", "estudiante"],
 },
 2: {
   "tipo": "3 mini-diálogos de saludo",
   "guion": [
     ["Ana", "Buenos días, Marta. ¿Qué tal?"], ["Marta", "Buenos días. Estoy muy bien, gracias. ¿Y tú?"], ["Ana", "Bien también. ¡Hasta luego!"],
     ["Luis", "Buenas tardes, señor López. ¿Cómo está usted?"], ["Sr. López", "Buenas tardes. Estoy un poco cansado, la verdad."], ["Luis", "Vaya. ¡Adiós!"],
     ["Nieta", "¡Buenas noches, abuela!"], ["Abuela", "Buenas noches, cariño. ¿Cómo estás?"], ["Nieta", "Bien, pero un poco nerviosa. Hasta mañana."],
   ],
   "tarea_nl": "Luister naar 3 gesprekjes: welk moment van de dag, en hoe voelt de persoon zich?",
   "preguntas": [
     {"q": "¿Cuántos diálogos hay?", "opts": ["Dos", "Tres", "Cuatro"], "a": 1},
     {"q": "El primer diálogo es…", "opts": ["por la mañana", "por la tarde", "por la noche"], "a": 0},
     {"q": "¿Cómo está el señor López?", "opts": ["muy bien", "un poco cansado", "nervioso"], "a": 1},
     {"q": "En el tercer diálogo, ¿con quién habla la chica?", "opts": ["con su madre", "con su abuela", "con un amigo"], "a": 1},
   ],
   "glosario": [["¿Qué tal?", "hoe gaat het?"], ["un poco cansado", "een beetje moe"], ["cariño", "schat/lieverd"], ["la verdad", "eerlijk gezegd"]],
   "rallentado": ["buenas tardes", "cansado", "hasta mañana"],
 },
 3: {
   "tipo": "entrevista en la calle",
   "guion": [
     ["Reportero", "¡Hola! ¿De dónde eres?"], ["Chica", "Hola. Soy de Colombia, de Bogotá."],
     ["Reportero", "¡Qué bien! ¿Y qué idiomas hablas?"], ["Chica", "Hablo español y un poco de inglés."],
     ["Reportero", "Gracias. Y tú, ¿de dónde eres?"], ["Chico", "Yo soy de España. Soy español y hablo español y francés."],
   ],
   "tarea_nl": "Vul de tabel in: país · nacionalidad · idioma van elke persoon.",
   "preguntas": [
     {"q": "¿Cuántas personas responden?", "opts": ["Una", "Dos", "Tres"], "a": 1},
     {"q": "¿De dónde es la primera persona?", "opts": ["De España", "De Colombia", "De México"], "a": 1},
     {"q": "¿Qué idiomas habla la chica?", "opts": ["español e inglés", "español y francés", "solo español"], "a": 0},
     {"q": "El chico es…", "opts": ["colombiano", "español", "argentino"], "a": 1},
   ],
   "glosario": [["¿De dónde eres?", "Waar kom je vandaan?"], ["un poco de inglés", "een beetje Engels"], ["los idiomas", "de talen"]],
   "rallentado": ["de dónde eres", "español", "francés"],
 },
 4: {
   "tipo": "alguien describe a su familia",
   "guion": [
     ["Pablo", "Hola. En mi familia somos cuatro."],
     ["Pablo", "Mi madre se llama Marta. Es muy amable y un poco elegante."],
     ["Pablo", "Mi padre se llama Jorge. Es alto y muy fuerte."],
     ["Pablo", "Y mi hermano Leo es pequeño, pero muy divertido."],
   ],
   "tarea_nl": "Vul de fiche in: wie is elke persoon en hoe is die?",
   "preguntas": [
     {"q": "¿A cuántas personas describe Pablo?", "opts": ["A dos", "A tres", "A cuatro"], "a": 1},
     {"q": "¿Cómo es la madre?", "opts": ["amable", "alta", "fuerte"], "a": 0},
     {"q": "¿Quién es alto y fuerte?", "opts": ["la madre", "el padre", "el hermano"], "a": 1},
     {"q": "El hermano Leo es…", "opts": ["grande", "pequeño", "elegante"], "a": 1},
   ],
   "glosario": [["somos cuatro", "we zijn met vier"], ["amable", "vriendelijk"], ["fuerte", "sterk"], ["pequeño", "klein"]],
   "rallentado": ["mi madre", "amable", "divertido"],
 },
 5: {
   "tipo": "una visita a la habitación",
   "guion": [
     ["Ana", "Mira, esta es mi habitación."],
     ["Ana", "Aquí hay una cama y una mesa pequeña."],
     ["Nico", "¿Y qué es esto?"],
     ["Ana", "Esto es una guitarra. Sirve para tocar música."],
     ["Nico", "¡Qué bien! ¿Hay un ordenador?"],
     ["Ana", "No, no hay ordenador, pero hay muchos libros."],
   ],
   "tarea_nl": "Luister: welke voorwerpen zijn er in de kamer?",
   "preguntas": [
     {"q": "¿De qué habitación hablan?", "opts": ["De la clase", "De la habitación de Ana", "De la cocina"], "a": 1},
     {"q": "¿Qué objeto enseña Ana?", "opts": ["Un ordenador", "Una guitarra", "Una televisión"], "a": 1},
     {"q": "¿Para qué sirve la guitarra?", "opts": ["Para estudiar", "Para tocar música", "Para descansar"], "a": 1},
     {"q": "¿Hay un ordenador?", "opts": ["Sí", "No", "No se sabe"], "a": 1},
   ],
   "glosario": [["hay", "er is/zijn"], ["la guitarra", "de gitaar"], ["Sirve para tocar", "dient om te spelen"], ["muchos libros", "veel boeken"]],
   "rallentado": ["esto es", "guitarra", "no hay ordenador"],
 },
 6: {
   "tipo": "¿dónde está? · buscar cosas en casa",
   "guion": [
     ["Marta", "¿Dónde está mi bolso? No lo encuentro."],
     ["Pablo", "¿Está en la cocina?"],
     ["Marta", "No, en la cocina no hay nada."],
     ["Pablo", "Mira, está aquí, encima del sofá."],
     ["Marta", "¡Ah! Y las llaves, ¿dónde están?"],
     ["Pablo", "Debajo de la mesa, al lado de tu libro."],
   ],
   "tarea_nl": "Luister: waar staan de spullen (bolso, llaves)?",
   "preguntas": [
     {"q": "¿Qué busca Marta primero?", "opts": ["Las llaves", "Su bolso", "Un libro"], "a": 1},
     {"q": "¿Dónde está el bolso?", "opts": ["En la cocina", "Encima del sofá", "Debajo de la mesa"], "a": 1},
     {"q": "¿Dónde están las llaves?", "opts": ["Encima del sofá", "Debajo de la mesa", "En la ventana"], "a": 1},
   ],
   "glosario": [["¿dónde está?", "waar is?"], ["encima del sofá", "boven op de bank"], ["debajo de la mesa", "onder de tafel"], ["las llaves", "de sleutels"]],
   "rallentado": ["dónde está", "encima del sofá", "debajo de la mesa"],
 },
 7: {
   "tipo": "una entrevista · ¿en qué trabajas?",
   "guion": [
     ["Sofía", "Hola, Óscar. ¿A qué te dedicas?"],
     ["Óscar", "Soy dependiente. Trabajo en una tienda de música."],
     ["Sofía", "¡Qué bien! ¿Y estás contento?"],
     ["Óscar", "Sí, estoy muy contento. ¿Y tú? ¿En qué trabajas?"],
     ["Sofía", "Soy estudiante, pero los sábados trabajo en una oficina."],
     ["Óscar", "¡Trabajamos mucho los dos!"],
   ],
   "tarea_nl": "Luister: welk beroep heeft elk, en waar werken ze?",
   "preguntas": [
     {"q": "¿A qué se dedica Óscar?", "opts": ["Es profesor", "Es dependiente", "Es escritor"], "a": 1},
     {"q": "¿Dónde trabaja Óscar?", "opts": ["En una tienda de música", "En una academia", "En un teatro"], "a": 0},
     {"q": "¿Qué hace Sofía los sábados?", "opts": ["Estudia en casa", "Trabaja en una oficina", "Trabaja en una tienda"], "a": 1},
   ],
   "glosario": [["¿a qué te dedicas?", "wat doe je (voor werk)?"], ["el/la dependiente/a", "de winkelbediende"], ["estoy contento/a", "ik ben blij"], ["los sábados", "op zaterdag"]],
   "rallentado": ["a qué te dedicas", "trabajo en una tienda", "estoy muy contento"],
 },
}

def has(unit):
    return bool(LECTURA.get(unit)) or bool(AUDIO.get(unit))

if __name__ == "__main__":
    for u in (1, 2, 3):
        l = "lectura ✓" if LECTURA.get(u) else "lectura —"
        a = "audio ✓" if AUDIO.get(u) else "audio —"
        print(f"U{u}: {l} · {a}")
