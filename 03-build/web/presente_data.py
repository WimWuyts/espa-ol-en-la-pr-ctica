#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""De honderd invulvormen op het presente de indicativo (C5 U1 §3.3).

De auteur leverde deze reeks aan als extra oefenstof bij het presente
regular. Ze staat hier als gegevens, niet als opmaak: de gedrukte bundel
(`gen_u1_print.py`) en de digitale pagina (`gen_u1_web.py`) putten allebei
uit dít bestand, zodat papier en scherm niet uit elkaar kunnen lopen.

Alle honderd vormen zijn nagerekend tegen de uitgangen van het presente
regular (-ar · -er · -ir, met leer → leo/lees/…): ze kloppen alle honderd.
Geen enkel werkwoord verandert van stamklinker — dat is met opzet, want
de bota (e→ie, o→ue, e→i) komt pas in U3.

SUELTAS = [(titel_es, steun_nl, [(nr, zin_met_{}, infinitivo, antwoord), …]), …]
TEXTOS  = [(titel_es, steun_nl, tekst_met_{}, [(nr, infinitivo, antwoord), …]), …]
"""

SUELTAS = [
    ("El instituto, el tiempo libre y el día a día",
     "school, vrije tijd en het dagelijkse leven", [
      (1, "Yo {} español con mi compañero de clase.", "hablar", "hablo"),
      (2, "Tú {} vocabulario después de la cena.", "estudiar", "estudias"),
      (3, "Laura {} en la biblioteca los miércoles.", "trabajar", "trabaja"),
      (4, "Nosotros {} al instituto cada mañana.", "caminar", "caminamos"),
      (5, "Vosotros {} una presentación sobre Chile.", "preparar", "preparáis"),
      (6, "Mis amigos {} música española en el autobús.", "escuchar", "escuchan"),
      (7, "Yo {} una ensalada en la cafetería.", "comer", "como"),
      (8, "Tú {} agua durante el entrenamiento.", "beber", "bebes"),
      (9, "El profesor {} la regla con un ejemplo.", "explicar", "explica"),
      (10, "Mi hermana y yo {} nuevas palabras con tarjetas.", "aprender", "aprendemos"),
      (11, "Vosotras {} un correo a vuestra profesora.", "escribir", "escribís"),
      (12, "Los alumnos {} sus cuadernos al principio de la clase.", "abrir", "abren"),
      (13, "Usted {} a Madrid por trabajo.", "viajar", "viaja"),
      (14, "Yo {} muchos mensajes del grupo.", "recibir", "recibo"),
      (15, "Miguel {} fruta en el mercado local.", "vender", "vende"),
      (16, "Nosotros {} el material de dibujo.", "compartir", "compartimos"),
      (17, "Tú {} cinco kilómetros los domingos.", "correr", "corres"),
      (18, "Ellas {} un museo de arte moderno.", "visitar", "visitan"),
      (19, "Vosotros {} el menú antes de entrar en el restaurante.", "leer", "leéis"),
      (20, "Mi padre {} arroz con verduras los viernes.", "cocinar", "cocina"),
     ]),
    ("La ciudad, la vivienda y el aprendizaje",
     "de stad, wonen en leren", [
      (21, "La bibliotecaria {} los libros por tema.", "ordenar", "ordena"),
      (22, "Ustedes {} a las preguntas del formulario.", "responder", "responden"),
      (23, "Yo {} mi escritorio antes de estudiar.", "limpiar", "limpio"),
      (24, "Tú {} pan en la tienda del barrio.", "comprar", "compras"),
      (25, "Ana y Pablo {} cerca de la estación.", "vivir", "viven"),
      (26, "Nosotros {} el texto después de la explicación.", "comprender", "comprendemos"),
      (27, "Él {} personajes para un cómic.", "dibujar", "dibuja"),
      (28, "Vosotras {} a un taller de fotografía.", "asistir", "asistís"),
      (29, "Los músicos {} cada tarde en el centro cultural.", "practicar", "practican"),
      (30, "Usted {} su dirección en este espacio.", "escribir", "escribe"),
      (31, "Yo {} una mochila más resistente.", "necesitar", "necesito"),
      (32, "Tú {} a tu hermano con los deberes.", "ayudar", "ayudas"),
      (33, "El autobús {} por el centro de la ciudad.", "circular", "circula"),
      (34, "Nosotros {} las escaleras hasta el tercer piso.", "subir", "subimos"),
      (35, "Vosotros {} las terminaciones de los verbos regulares.", "aprender", "aprendéis"),
      (36, "Las tiendas {} productos de la región.", "vender", "venden"),
      (37, "Yo {} una serie en español con subtítulos.", "mirar", "miro"),
      (38, "Tú {} la ventana durante el descanso.", "abrir", "abres"),
      (39, "El equipo {} en el polideportivo municipal.", "entrenar", "entrena"),
      (40, "Mis abuelos {} una revista cada mes.", "recibir", "reciben"),
     ]),
    ("La salud, la cultura, el trabajo y la naturaleza",
     "gezondheid, cultuur, werk en natuur", [
      (41, "Nosotros {} salsa en la fiesta del colegio.", "bailar", "bailamos"),
      (42, "Vosotras {} chocolate caliente en invierno.", "beber", "bebéis"),
      (43, "La médica {} a cada paciente con atención.", "examinar", "examina"),
      (44, "Ustedes {} en una zona muy tranquila.", "vivir", "viven"),
      (45, "Yo {} mis planes en una agenda.", "escribir", "escribo"),
      (46, "Tú {} las instrucciones del juego.", "comprender", "comprendes"),
      (47, "La familia {} una comida especial para el domingo.", "preparar", "prepara"),
      (48, "Nosotros {} a una charla sobre el medio ambiente.", "asistir", "asistimos"),
      (49, "Vosotros {} con los vecinos durante la reunión.", "hablar", "habláis"),
      (50, "Los turistas {} la catedral y la plaza mayor.", "visitar", "visitan"),
      (51, "Yo {} del transporte público para el trayecto al trabajo.", "depender", "dependo"),
      (52, "Tú {} la tarta en ocho partes iguales.", "dividir", "divides"),
      (53, "Mi vecino {} bicicletas en su garaje.", "reparar", "repara"),
      (54, "Nosotros {} terminar el proyecto esta semana.", "prometer", "prometemos"),
      (55, "Vosotras {} fotografías del viaje con la clase.", "compartir", "compartís"),
      (56, "Los científicos {} las aves desde una torre.", "observar", "observan"),
      (57, "Usted {} español para la comunicación con sus clientes.", "aprender", "aprende"),
      (58, "Yo {} los sábados en una tienda de deportes.", "trabajar", "trabajo"),
      (59, "Tú {} una notificación cada vez que llega un paquete.", "recibir", "recibes"),
      (60, "Los niños {} mapas imaginarios en el patio.", "dibujar", "dibujan"),
     ]),
]

TEXTOS = [
    ("Una mañana en el instituto", "een ochtend op school",
     "Cada mañana, Clara {} temprano al instituto. Antes de la primera clase, ella {} sus libros y su tableta. Sus compañeros {} en el pasillo. En la clase de ciencias, todos {} un experimento. Al final, Clara {} un breve resumen.",
     [(61, "llegar", "llega"), (62, "organizar", "organiza"), (63, "esperar", "esperan"), (64, "observar", "observan"), (65, "escribir", "escribe")]),
    ("El desayuno en familia", "het familieontbijt",
     "Los domingos, mi madre {} un desayuno especial. Yo {} la fruta, y mi hermano {} zumo de naranja. Mis abuelos {} pan con tomate. Durante el desayuno, todos {} sobre la semana.",
     [(66, "preparar", "prepara"), (67, "cortar", "corto"), (68, "beber", "bebe"), (69, "comer", "comen"), (70, "conversar", "conversan")]),
    ("Una tarde de deporte", "een sportieve namiddag",
     "Los sábados, mis amigos y yo {} atletismo. Ana {} en la piscina, mientras yo {} en la pista. Vosotros {} con el grupo juvenil. El entrenador {} nuestro progreso.",
     [(71, "practicar", "practicamos"), (72, "nadar", "nada"), (73, "correr", "corro"), (74, "entrenar", "entrenáis"), (75, "observar", "observa")]),
    ("Un viaje en tren", "een treinreis",
     "Este sábado, yo {} a Toledo con mi prima. Ella {} los billetes por internet. En la estación, nosotros {} al tren con tiempo. Durante el trayecto, mi prima {} una guía y yo {} mensajes a mi familia.",
     [(76, "viajar", "viajo"), (77, "comprar", "compra"), (78, "subir", "subimos"), (79, "leer", "lee"), (80, "escribir", "escribo")]),
    ("Un proyecto para el barrio", "een project voor de buurt",
     "Los alumnos {} en un proyecto para mejorar el barrio. La profesora {} las tareas y nosotros {} el parque en cuatro zonas. Vosotros {} carteles informativos. Al final, el ayuntamiento {} un informe con los resultados.",
     [(81, "participar", "participan"), (82, "explicar", "explica"), (83, "dividir", "dividimos"), (84, "preparar", "preparáis"), (85, "recibir", "recibe")]),
    ("Trabajar en una cafetería", "werken in een café",
     "Cada tarde, Lucía {} en una pequeña cafetería. Primero, ella {} las mesas. Los clientes {} café o té, y su compañero Dani {} la barra. Al final de la jornada, Lucía y Dani {} el local.",
     [(86, "trabajar", "trabaja"), (87, "preparar", "prepara"), (88, "beber", "beben"), (89, "limpiar", "limpia"), (90, "ordenar", "ordenan")]),
    ("Trabajar juntos en línea", "online samenwerken",
     "Por la tarde, yo {} el ordenador para un trabajo en grupo. Tú {} las ideas principales. Nosotros {} un documento en línea y vosotros {} a los comentarios. Después, la profesora {} nuestra versión final.",
     [(91, "usar", "uso"), (92, "escribir", "escribes"), (93, "compartir", "compartimos"), (94, "responder", "respondéis"), (95, "revisar", "revisa")]),
    ("El festival de verano", "het zomerfestival",
     "En agosto, el pueblo {} un festival de verano. Los músicos {} en la plaza y la gente {} delante del escenario. Los niños {} helado. Al final de la noche, mi familia y yo {} juntos a casa.",
     [(96, "celebrar", "celebra"), (97, "tocar", "tocan"), (98, "bailar", "baila"), (99, "comer", "comen"), (100, "caminar", "caminamos")]),
]

CLAVE = {n: a for _t, _n, it in SUELTAS for n, _q, _i, a in it}
CLAVE.update({n: a for _t, _n, _c, hs in TEXTOS for n, _i, a in hs})

