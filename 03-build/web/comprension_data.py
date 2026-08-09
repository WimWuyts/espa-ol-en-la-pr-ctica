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
 8: {
   "tipo": "un mensaje · mi horario del sábado",
   "contexto_nl": "Nuria stuurt haar zaterdagplanning door in de klasgroep.",
   "texto": [
     ["", "¡Hola! Este es mi horario del sábado."],
     ["", "Por la mañana estudio español a las diez y media."],
     ["", "A la una y cuarto como con mi familia. ¡Siempre comemos tarde!"],
     ["", "Por la tarde, a las cinco, juego al fútbol con mis amigos."],
     ["", "Y por la noche, a las nueve menos cuarto, vemos una película. ¿Quieres quedar el domingo?"],
   ],
   "global": [
     {"q": "¿De qué día habla Nuria?", "opts": ["Del lunes", "Del sábado", "Del domingo"], "a": 1},
     {"q": "¿A qué hora estudia español?", "opts": ["A las diez y media", "A la una y cuarto", "A las cinco"], "a": 0},
   ],
   "detalle": [
     {"q": "Nuria come a la una y cuarto.", "vf": True},
     {"q": "Juega al fútbol por la mañana.", "vf": False},
     {"q": "Ve una película a las nueve menos cuarto.", "vf": True},
     {"q": "Quiere quedar el lunes.", "vf": False},
   ],
   "transfer": "¿Y tú? ¿Cuál es tu horario del sábado? ¿A qué hora comes?",
   "glosario": [["el horario", "het (uur)schema"], ["y media", "half (…+30)"], ["menos cuarto", "kwart voor"], ["por la mañana/tarde/noche", "'s ochtends/'s middags/'s avonds"], ["¿quieres quedar?", "wil je afspreken?"]],
 },
 9: {
   "tipo": "un mensaje · mis planes del finde",
   "contexto_nl": "Iker stuurt zijn weekendplannen naar de klasgroep.",
   "texto": [
     ["", "¡Hola! Este finde tengo muchos planes."],
     ["", "El sábado por la mañana tengo que estudiar, pero por la tarde voy a jugar al fútbol."],
     ["", "Por la noche vamos a ver una película en casa de Marta."],
     ["", "El domingo tengo que pasear al perro y después voy a quedar con mis primos."],
     ["", "¡Ah! Y el lunes tengo que trabajar. ¿Y tú? ¿Qué vas a hacer?"],
   ],
   "global": [
     {"q": "¿De qué habla Iker?", "opts": ["De sus clases", "De sus planes del finde", "De su familia"], "a": 1},
     {"q": "¿Qué va a hacer el sábado por la tarde?", "opts": ["Estudiar", "Jugar al fútbol", "Pasear al perro"], "a": 1},
   ],
   "detalle": [
     {"q": "El sábado por la mañana tiene que estudiar.", "vf": True},
     {"q": "Van a ver una película en casa de Marta.", "vf": True},
     {"q": "El domingo va a quedar con sus amigas.", "vf": False},
     {"q": "El lunes no tiene que trabajar.", "vf": False},
   ],
   "transfer": "¿Y tú? ¿Qué vas a hacer este finde? ¿Qué tienes que hacer?",
   "glosario": [["el finde", "het weekend (informeel)"], ["voy a + inf.", "ik ga … (plan)"], ["tengo que + inf.", "ik moet …"], ["vamos a ver", "we gaan kijken"], ["después", "daarna"]],
 },
 10: {
   "tipo": "una nota en la cocina · ¿quién hace qué?",
   "contexto_nl": "Een briefje op de koelkast: de taken van het huis verdeeld.",
   "texto": [
     ["", "¡Hola, familia! Esta semana hay que ayudar más en casa."],
     ["", "Yo sé cocinar, así que yo preparo la comida."],
     ["", "Ana tiene que pasar la aspiradora en el salón y ordenar su habitación."],
     ["", "Luis sabe planchar muy bien, pero esta semana tiene que fregar los platos."],
     ["", "Y papá va a limpiar el polvo. ¡Gracias a todos! Mamá"],
   ],
   "global": [
     {"q": "¿Qué es este texto?", "opts": ["Una carta de un hotel", "Una nota sobre las tareas de casa", "Un menú"], "a": 1},
     {"q": "¿Quién sabe cocinar?", "opts": ["Mamá", "Ana", "Luis"], "a": 0},
   ],
   "detalle": [
     {"q": "Ana tiene que pasar la aspiradora.", "vf": True},
     {"q": "Luis sabe planchar bien.", "vf": True},
     {"q": "Esta semana Luis tiene que planchar.", "vf": False},
     {"q": "Papá va a limpiar el polvo.", "vf": True},
   ],
   "transfer": "¿Y en tu casa? ¿Quién hace qué? ¿Qué sabes hacer tú?",
   "glosario": [["hay que + inf.", "men moet / er moet …"], ["sé cocinar", "ik kan koken"], ["pasar la aspiradora", "stofzuigen"], ["fregar los platos", "de vaat doen"], ["limpiar el polvo", "afstoffen"]],
 },

 # ── U11 · De compras / la ropa ────────────────────────────────────────────
 11: {
   "tipo": "dos anuncios de vacaciones",
   "contexto_nl": "Twee vakantieadvertenties: waar, met welk vervoer en welk weer?",
   "texto": [
     ["", "☀️ CANARIAS · 7 noches"],
     ["", "Vuelo en avión desde Madrid. Hotel cerca de la playa."],
     ["", "Siempre hace buen tiempo: entre 22 y 26 grados todo el año."],
     ["", "Actividades: submarinismo, bici y excursiones a la montaña."],
     ["", "❄️ ÁVILA · fin de semana"],
     ["", "En tren o en coche, a hora y media de Madrid."],
     ["", "En invierno hace mucho frío y a veces nieva. Lleva abrigo."],
     ["", "Perfecto para pasear por el pueblo y comer con la familia."],
   ],
   "global": [
     {"q": "¿Qué son estos textos?", "opts": ["Dos anuncios de vacaciones", "Dos cartas", "Un menú"], "a": 0},
     {"q": "¿Dónde hace más calor?", "opts": ["En Canarias", "En Ávila", "En los dos"], "a": 0},
   ],
   "detalle": [
     {"q": "A Canarias se va en avión.", "vf": True},
     {"q": "En Ávila hace calor en invierno.", "vf": False},
     {"q": "En Canarias se puede hacer submarinismo.", "vf": True},
     {"q": "Ávila está lejos de Madrid.", "vf": False},
   ],
   "transfer": "¿Y tú? ¿Adónde prefieres ir: a la playa o a la montaña? ¿Por qué?",
   "glosario": [["el vuelo", "de vlucht"], ["los grados", "de graden"],
                ["a veces nieva", "soms sneeuwt het"], ["el abrigo", "de jas"],
                ["pasear", "wandelen"]],
 },
 12: {
   "tipo": "el parte del tiempo de una app",
   "contexto_nl": "Het weerbericht van een app, voor vier steden.",
   "texto": [
     ["", "EL TIEMPO HOY · lunes 14"],
     ["", "Madrid: hace sol y calor, 34 grados. ¡Qué calor!"],
     ["", "Bilbao: está nublado y llueve por la tarde, 19 grados."],
     ["", "Bariloche: en invierno nieva mucho en la montaña, 2 grados."],
     ["", "Cartagena: hace buen tiempo, 31 grados, pero hace mucho viento."],
   ],
   "global": [
     {"q": "¿Qué es este texto?", "opts": ["Un horario", "El parte del tiempo", "Un anuncio"], "a": 1},
     {"q": "¿Dónde hace más calor?", "opts": ["En Madrid", "En Bilbao", "En Bariloche"], "a": 0},
   ],
   "detalle": [
     {"q": "En Bilbao llueve por la tarde.", "vf": True},
     {"q": "En Bariloche hace calor.", "vf": False},
     {"q": "En Cartagena hace viento.", "vf": True},
     {"q": "En Madrid está nublado.", "vf": False},
   ],
   "transfer": "¿Y hoy en tu ciudad? ¿Qué tiempo hace? ¿Cuál es tu estación favorita?",
   "glosario": [["hace sol", "het is zonnig"], ["está nublado", "het is bewolkt"],
                ["llueve", "het regent"], ["nieva", "het sneeuwt"],
                ["hace viento", "het waait"]],
 },
 # ── U13 · En el hotel / viajar ────────────────────────────────────────────
 13: {
   "tipo": "la confirmación de una reserva",
   "contexto_nl": "De bevestigingsmail van een hotelreservering.",
   "texto": [
     ["", "HOTEL PLAZA MAYOR · Confirmación de reserva nº 4471"],
     ["", "Habitación doble con baño, para dos noches: 15 y 16 de agosto."],
     ["", "Precio: 78 € por noche, desayuno incluido."],
     ["", "La habitación está en el tercer piso. Hay ascensor y wifi gratis."],
     ["", "La entrada es a partir de las 14:00 y la salida antes de las 12:00."],
   ],
   "global": [
     {"q": "¿Qué es este texto?", "opts": ["Un billete de tren", "Una confirmación de hotel", "Un menú"], "a": 1},
     {"q": "¿Cuántas noches son?", "opts": ["Una", "Dos", "Tres"], "a": 1},
   ],
   "detalle": [
     {"q": "El desayuno está incluido.", "vf": True},
     {"q": "La habitación está en el primer piso.", "vf": False},
     {"q": "Hay wifi gratis.", "vf": True},
     {"q": "Se puede entrar a las once de la mañana.", "vf": False},
   ],
   "transfer": "¿Y tú? ¿Qué necesitas en un hotel? Escribe tres cosas importantes para ti.",
   "glosario": [["la reserva", "de reservering"], ["la habitación doble", "de tweepersoonskamer"],
                ["el desayuno incluido", "ontbijt inbegrepen"], ["el ascensor", "de lift"],
                ["gratis", "gratis"]],
 },
 # ── U14 · Repaso · Mi mundo hispano ───────────────────────────────────────
 14: {
   "tipo": "cuatro postales de cuatro países",
   "contexto_nl": "Vier korte kaartjes uit vier landen — alles van het jaar komt terug.",
   "texto": [
     ["Ana", "¡Hola desde Sevilla! Hace mucho calor. Por la mañana visito la catedral y por la tarde tomo un helado. ¡Qué bonito!"],
     ["Nico", "Estoy en Ciudad de México. Hoy voy al mercado: hay fruta, ropa y flores. Tengo que comprar un regalo."],
     ["Alba", "Cartagena es increíble. Mi habitación está cerca del mar. Sé nadar, así que voy a la playa todos los días."],
     ["Iván", "Aquí en Bariloche nieva. Llevo abrigo y bufanda. En invierno hay que llevar ropa de abrigo."],
   ],
   "global": [
     {"q": "¿Qué son estos textos?", "opts": ["Cuatro postales", "Un menú", "Un horario"], "a": 0},
     {"q": "¿Quién está en México?", "opts": ["Ana", "Nico", "Alba"], "a": 1},
   ],
   "detalle": [
     {"q": "En Sevilla hace frío.", "vf": False},
     {"q": "Nico tiene que comprar un regalo.", "vf": True},
     {"q": "Alba sabe nadar.", "vf": True},
     {"q": "En Bariloche hace sol y calor.", "vf": False},
   ],
   "transfer": "Escribe tu propia postal: ¿dónde estás, qué tiempo hace y qué haces hoy?",
   "glosario": [["visito", "ik bezoek"], ["el regalo", "het cadeau"],
                ["sé nadar", "ik kan zwemmen"], ["el abrigo", "de jas"],
                ["la bufanda", "de sjaal"]],
 },
}

AUDIO = {
 1: {  # ── DEMO (U1) ──
   "audio": "audio/C4_U1.mp3",
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
   "audio": "audio/C4_U2.mp3",
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
   "audio": "audio/C4_U3.mp3",
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
   "audio": "audio/C4_U4.mp3",
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
   "audio": "audio/C4_U5.mp3",
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
   "audio": "audio/C4_U6.mp3",
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
   "audio": "audio/C4_U7.mp3",
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
 8: {
   "audio": "audio/C4_U8.mp3",
   "tipo": "quedar por teléfono · ¿a qué hora?",
   "guion": [
     ["Elena", "¿Sí? Hola, Tomás."],
     ["Tomás", "Hola, Elena. ¿Quieres quedar esta tarde?"],
     ["Elena", "Sí, vale. ¿A qué hora?"],
     ["Tomás", "¿A las seis? ¿O es un poco pronto?"],
     ["Elena", "A las seis no puedo. Mejor a las siete y media."],
     ["Tomás", "Perfecto. Quedamos en el cine. ¡Hasta luego!"],
   ],
   "tarea_nl": "Luister: op welk uur spreken ze af, en waar?",
   "preguntas": [
     {"q": "¿Cuándo quieren quedar?", "opts": ["Esta mañana", "Esta tarde", "El domingo"], "a": 1},
     {"q": "¿A qué hora quedan al final?", "opts": ["A las seis", "A las siete y media", "A las ocho"], "a": 1},
     {"q": "¿Dónde quedan?", "opts": ["En el cine", "En casa de Elena", "En un restaurante"], "a": 0},
   ],
   "glosario": [["¿quieres quedar?", "wil je afspreken?"], ["¿a qué hora?", "hoe laat?"], ["un poco pronto", "een beetje vroeg"], ["y media", "half (…+30)"]],
   "rallentado": ["a qué hora", "a las siete y media", "quedamos en el cine"],
 },
 9: {
   "audio": "audio/C4_U9.mp3",
   "tipo": "planes · ¿qué vas a hacer?",
   "guion": [
     ["Lucas", "¿Qué vas a hacer este finde?"],
     ["Alba", "El sábado voy a ir a un concierto. ¿Vienes?"],
     ["Lucas", "No puedo. Tengo que trabajar en la tienda."],
     ["Alba", "¡Qué pena! ¿Y el domingo?"],
     ["Lucas", "El domingo tengo que estudiar por la mañana, pero por la tarde estoy libre."],
     ["Alba", "Perfecto. Vamos a tomar algo el domingo por la tarde."],
   ],
   "tarea_nl": "Luister: wat gaat elk doen, en wat moet elk doen?",
   "preguntas": [
     {"q": "¿Qué va a hacer Alba el sábado?", "opts": ["Trabajar", "Ir a un concierto", "Estudiar"], "a": 1},
     {"q": "¿Por qué no puede Lucas el sábado?", "opts": ["Tiene que trabajar", "Tiene que estudiar", "Está enfermo"], "a": 0},
     {"q": "¿Cuándo van a tomar algo?", "opts": ["El sábado por la noche", "El domingo por la mañana", "El domingo por la tarde"], "a": 2},
   ],
   "glosario": [["¿qué vas a hacer?", "wat ga je doen?"], ["tengo que trabajar", "ik moet werken"], ["¡qué pena!", "wat jammer!"], ["estoy libre", "ik ben vrij"], ["vamos a tomar algo", "we gaan iets drinken"]],
   "rallentado": ["qué vas a hacer", "tengo que trabajar", "vamos a tomar algo"],
 },
 10: {
   "audio": "audio/C4_U10.mp3",
   "tipo": "repartir las tareas · ¿me ayudas?",
   "guion": [
     ["Rosa", "¡Qué desorden! Hay que limpiar la cocina."],
     ["Iván", "Yo te ayudo. ¿Qué tengo que hacer?"],
     ["Rosa", "¿Sabes pasar la aspiradora?"],
     ["Iván", "Claro que sé. Y también sé fregar los platos."],
     ["Rosa", "Perfecto. Entonces yo limpio el polvo y ordeno los armarios."],
     ["Iván", "Vale. ¡Así terminamos rápido!"],
   ],
   "tarea_nl": "Luister: wie doet welke taak?",
   "preguntas": [
     {"q": "¿Qué hay que limpiar?", "opts": ["El salón", "La cocina", "El baño"], "a": 1},
     {"q": "¿Qué sabe hacer Iván?", "opts": ["Cocinar y planchar", "Pasar la aspiradora y fregar", "Solo ordenar"], "a": 1},
     {"q": "¿Qué va a hacer Rosa?", "opts": ["Fregar los platos", "Limpiar el polvo y ordenar", "Pasar la aspiradora"], "a": 1},
   ],
   "glosario": [["hay que limpiar", "er moet gepoetst worden"], ["yo te ayudo", "ik help je"], ["¿sabes…?", "kan je…?"], ["fregar los platos", "de vaat doen"], ["ordenar los armarios", "de kasten opruimen"]],
   "rallentado": ["hay que limpiar", "yo te ayudo", "sabes pasar la aspiradora"],
 },

 11: {
   "audio": "audio/C4_U11.mp3",
   "tipo": "dos amigos hablan de las vacaciones",
   "guion": [
     ["Ana", "¿Adónde vas de vacaciones este año?"],
     ["Nico", "Voy a la playa, a Canarias. Siempre hace buen tiempo."],
     ["Ana", "¡Qué bien! ¿Y vas en avión?"],
     ["Nico", "Sí, en avión. Me encanta el mar. ¿Y tú?"],
     ["Ana", "Yo prefiero la montaña. No soporto el calor."],
     ["Nico", "¿Vas a menudo?"],
     ["Ana", "Todos los años. Y en invierno voy tres veces."],
   ],
   "tarea_nl": "Luister: waar gaat elk van beiden heen, met welk vervoer en waarom?",
   "preguntas": [
     {"q": "¿Adónde va Nico?", "opts": ["A la montaña", "A la playa", "Al pueblo"], "a": 1},
     {"q": "¿Cómo viaja Nico?", "opts": ["En tren", "En coche", "En avión"], "a": 2},
     {"q": "¿Por qué prefiere Ana la montaña?", "opts": ["Porque no soporta el calor", "Porque es barato", "Porque hay mar"], "a": 0},
   ],
   "glosario": [["me encanta", "ik vind het geweldig"], ["no soporto", "ik kan niet tegen"],
                ["prefiero", "ik verkies"], ["todos los años", "elk jaar"]],
   "rallentado": ["hace buen tiempo", "me encanta", "no soporto el calor"],
 },
 12: {
   "audio": "audio/C4_U12.mp3",
   "tipo": "dos amigos hablan del tiempo y de los planes",
   "guion": [
     ["Lucas", "¡Qué frío hace hoy! ¿Vas a salir?"],
     ["Elena", "No sé. Está nublado y creo que va a llover."],
     ["Lucas", "Pues en verano aquí hace muchísimo calor."],
     ["Elena", "Sí, pero mi estación favorita es el otoño."],
     ["Lucas", "¿El otoño? ¿Por qué?"],
     ["Elena", "Porque no hace ni frío ni calor. ¡Es perfecto!"],
   ],
   "tarea_nl": "Luister: welk weer, welk seizoen en waarom?",
   "preguntas": [
     {"q": "¿Qué tiempo hace hoy?", "opts": ["Hace sol", "Hace frío y está nublado", "Nieva"], "a": 1},
     {"q": "¿Cuál es la estación favorita de Elena?", "opts": ["El verano", "El invierno", "El otoño"], "a": 2},
     {"q": "¿Por qué le gusta?", "opts": ["Porque hace calor", "Porque no hace ni frío ni calor", "Porque llueve"], "a": 1},
   ],
   "glosario": [["¡qué frío!", "wat koud!"], ["está nublado", "het is bewolkt"],
                ["la estación", "het seizoen"], ["ni… ni…", "noch… noch…"]],
   "rallentado": ["¡qué frío hace!", "está nublado", "mi estación favorita"],
 },
 13: {
   "audio": "audio/C4_U13.mp3",
   "tipo": "en la recepción del hotel",
   "guion": [
     ["Tomás", "Buenas tardes. Tengo una reserva a nombre de Tomás Vidal."],
     ["Recepcionista", "Buenas tardes. Sí, una habitación doble para dos noches."],
     ["Tomás", "Exacto. ¿El desayuno está incluido?"],
     ["Recepcionista", "Sí, de siete a diez, en el primer piso."],
     ["Tomás", "Perfecto. ¿Y hay wifi en la habitación?"],
     ["Recepcionista", "Sí, gratis. Aquí tiene la llave: habitación trescientos dos."],
   ],
   "tarea_nl": "Luister: welke kamer, hoeveel nachten en wat is inbegrepen?",
   "preguntas": [
     {"q": "¿Qué tipo de habitación es?", "opts": ["Individual", "Doble", "Triple"], "a": 1},
     {"q": "¿A qué hora es el desayuno?", "opts": ["De seis a nueve", "De siete a diez", "De ocho a once"], "a": 1},
     {"q": "¿Cuál es el número de la habitación?", "opts": ["302", "203", "320"], "a": 0},
   ],
   "glosario": [["la reserva", "de reservering"], ["incluido", "inbegrepen"],
                ["la llave", "de sleutel"], ["gratis", "gratis"]],
   "rallentado": ["tengo una reserva", "el desayuno está incluido", "aquí tiene la llave"],
 },
 14: {
   "audio": "audio/C4_U14.mp3",
   "tipo": "cuatro personas se presentan · repaso del año",
   "guion": [
     ["Ana", "Hola, me llamo Ana, soy de Sevilla y tengo dieciséis años."],
     ["Nico", "Yo soy Nico, soy mexicano. Vivo en una casa cerca del mercado."],
     ["Alba", "Me llamo Alba, soy colombiana y sé nadar muy bien."],
     ["Iván", "Yo soy Iván, argentino. En invierno tengo que llevar abrigo."],
     ["Ana", "¿Y tú? ¿Cómo te llamas y de dónde eres?"],
     ["Nico", "¡Ahora te toca a ti!"],
   ],
   "tarea_nl": "Luister: wie is wie? Noteer naam, land en één detail.",
   "preguntas": [
     {"q": "¿De dónde es Ana?", "opts": ["De México", "De Sevilla", "De Colombia"], "a": 1},
     {"q": "¿Qué sabe hacer Alba?", "opts": ["Cocinar", "Nadar", "Planchar"], "a": 1},
     {"q": "¿Qué tiene que llevar Iván en invierno?", "opts": ["Una camiseta", "Un abrigo", "Zapatillas"], "a": 1},
   ],
   "glosario": [["soy de…", "ik kom uit…"], ["cerca de", "dicht bij"],
                ["sé nadar", "ik kan zwemmen"], ["tengo que llevar", "ik moet dragen"]],
   "rallentado": ["me llamo", "soy de", "tengo que llevar"],
 },
}

def has(unit):
    return bool(LECTURA.get(unit)) or bool(AUDIO.get(unit))

if __name__ == "__main__":
    for u in (1, 2, 3):
        l = "lectura ✓" if LECTURA.get(u) else "lectura —"
        a = "audio ✓" if AUDIO.get(u) else "audio —"
        print(f"U{u}: {l} · {a}")
