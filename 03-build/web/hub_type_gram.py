#!/usr/bin/env python3
"""Getypte grammatica-drills voor het paneel «Gramática» van elke hub.

Waar `hub_type_sets` de woordenschat automatisch uit `u<N>_vocab.json` haalt, is
grammatica per unit anders: de items worden hier met de hand geschreven en
nagerekend. Dit bestand is de enige plaats waar dat gebeurt — de generatoren
roepen alleen `js(cursus, unit)` aan en krijgen niets terug zolang een unit nog
niet is uitgeschreven. Zo kan de bouw unit per unit aangroeien zonder dat er
ooit nog aan de zeventien generatoren geraakt moet worden.

Beleid:
  * `accents:'strict'` bij werkwoordsvormen en bij de tilde-regel zelf — daar ís
    het accent de leerstof (hablo ≠ habló, cafe ≠ café).
  * `accents:'soft'` bij lidwoorden en losse woordenschatvormen.
  * Elke set bevat de klassieke cloze uit CLAUDE.md §14bis: de leerling vult
    zelf de correcte vorm in, zonder keuzelijst.
  * Scope III-Spa-d: presente de indicativo. Géén futuro simple, condicional of
    subjuntivo — ook niet als afleider.
"""
import json

# --------------------------------------------------------------------------- #
#  Slots — worden in het paneel Gramática gezet, ná de bestaande oefeningen.
# --------------------------------------------------------------------------- #
SLOTS_HTML = """    <h3 class="subh">✍️ Escribe tú — la gramática sin opciones</h3>
    <p class="lead">Geen keuzelijst: je <b>schrijft</b> de vorm zelf. <span class="gloss">Bij
    werkwoorden en bij de tilde tellen de accenten mee — dat ís hier de leerstof.</span></p>
    <div class="card ex escribe" id="gt_1"></div>
    <div class="card ex escribe" id="gt_2"></div>
    <div class="card ex escribe" id="gt_3"></div>
"""

# --------------------------------------------------------------------------- #
#  De sets, per (cursus, unit). Slot 1-2-3 in volgorde van de leerladder.
# --------------------------------------------------------------------------- #
SETS = {}

SETS[("C5", 0)] = [
    dict(title="Escribe la palabra con tilde", accents="strict",
         desc="Het woord staat er zónder accent. Schrijf het <b>juist</b>: met tilde als de regel "
              "het vraagt, zonder als ze dat niet doet.",
         items=[
             {"q": "cafe", "ans": "café", "hint": "c___", "why": "aguda op klinker → tilde"},
             {"q": "casa", "ans": "casa", "hint": "c___", "why": "llana op klinker → géén tilde"},
             {"q": "adios", "ans": "adiós", "hint": "a____", "why": "aguda op -s → tilde"},
             {"q": "Mexico", "ans": "México", "hint": "M_____", "why": "esdrújula → altijd tilde"},
             {"q": "musica", "ans": "música", "hint": "m_____", "why": "esdrújula → altijd tilde"},
             {"q": "lunes", "ans": "lunes", "hint": "l____", "why": "llana op -s → géén tilde"},
             {"q": "jamon", "ans": "jamón", "hint": "j____", "why": "aguda op -n → tilde"},
             {"q": "arbol", "ans": "árbol", "hint": "á____", "why": "llana op -l → tilde"},
             {"q": "telefono", "ans": "teléfono", "hint": "t_______", "why": "esdrújula → altijd tilde"},
             {"q": "reloj", "ans": "reloj", "hint": "r____", "why": "aguda op -j → géén tilde"},
             {"q": "silaba", "ans": "sílaba", "hint": "s_____", "why": "esdrújula → altijd tilde"},
             {"q": "Peru", "ans": "Perú", "hint": "P___", "why": "aguda op klinker → tilde"},
         ]),
    dict(title="¿el o la? — escribe el artículo", accents="soft",
         desc="Schrijf het lidwoord voluit. Let op de valstrikken: niet elk woord op <b>-a</b> is "
              "vrouwelijk, en niet elk woord op <b>-o</b> is mannelijk.",
         items=[
             {"q": "___ mapa", "ans": "el", "why": "el mapa — valstrik: -a maar masculino"},
             {"q": "___ casa", "ans": "la", "why": "la casa"},
             {"q": "___ problema", "ans": "el", "why": "-ma (Grieks) → masculino"},
             {"q": "___ ciudad", "ans": "la", "why": "-dad → femenino"},
             {"q": "___ día", "ans": "el", "why": "el día — valstrik"},
             {"q": "___ mano", "ans": "la", "why": "la mano — valstrik: -o maar femenino"},
             {"q": "___ idioma", "ans": "el", "why": "-ma → masculino"},
             {"q": "___ letra", "ans": "la", "why": "la letra"},
             {"q": "___ país", "ans": "el", "why": "el país"},
             {"q": "___ sílaba", "ans": "la", "why": "la sílaba"},
             {"q": "___ número", "ans": "el", "why": "el número"},
             {"q": "___ clase", "ans": "la", "why": "la clase"},
         ]),
    dict(title="Escribe el número en letras", accents="strict",
         desc="Schrijf het getal voluit. De accenten van <b>dieciséis</b> en <b>veintidós</b> "
              "horen erbij.",
         items=[
             {"q": "0 =", "ans": "cero", "hint": "c___"},
             {"q": "5 =", "ans": "cinco", "hint": "c____"},
             {"q": "11 =", "ans": "once", "hint": "o___"},
             {"q": "13 =", "ans": "trece", "hint": "t____"},
             {"q": "15 =", "ans": "quince", "hint": "q_____"},
             {"q": "16 =", "ans": "dieciséis", "hint": "d________", "why": "16–29 = één woord, met tilde"},
             {"q": "20 =", "ans": "veinte", "hint": "v_____"},
             {"q": "21 =", "ans": "veintiuno", "hint": "v________", "why": "één woord"},
             {"q": "22 =", "ans": "veintidós", "hint": "v________", "why": "aguda op -s → tilde"},
             {"q": "30 =", "ans": "treinta", "hint": "t______"},
             {"q": "45 =", "ans": "cuarenta y cinco", "hint": "c_______ y c____", "why": "vanaf 31 met «y»"},
             {"q": "100 =", "ans": "cien", "hint": "c___", "why": "100 alleen = cien"},
         ]),
]

SETS[("C5", 1)] = [
    dict(title="El presente regular — rellena el verbo", accents="strict",
         desc="De klassieke invuloefening: schrijf het werkwoord tussen haakjes in de juiste vorm. "
              "Alle werkwoorden hier zijn <b>regelmatig</b> — je hoeft niets uit het hoofd te "
              "kennen, alleen de uitgang te kiezen.",
         items=[
             {"q": "Yo ___ (hablar) español en clase.", "ans": "hablo", "hint": "h____", "why": "-ar · yo → -o"},
             {"q": "Tú ___ (estudiar) en Madrid.", "ans": "estudias", "hint": "e_______", "why": "-ar · tú → -as"},
             {"q": "Lucía ___ (vivir) en Sevilla.", "ans": "vive", "hint": "v___", "why": "-ir · ella → -e"},
             {"q": "Nosotros ___ (comer) en casa.", "ans": "comemos", "hint": "c______", "why": "-er · nosotros → -emos"},
             {"q": "Los alumnos ___ (escribir) un mensaje.", "ans": "escriben", "hint": "e_______", "why": "-ir · ellos → -en"},
             {"q": "Yo ___ (aprender) español este año.", "ans": "aprendo", "hint": "a______", "why": "-er · yo → -o"},
             {"q": "¿Tú ___ (trabajar) los sábados?", "ans": "trabajas", "hint": "t_______", "why": "-ar · tú → -as"},
             {"q": "Diego ___ (escuchar) música.", "ans": "escucha", "hint": "e______", "why": "-ar · él → -a"},
             {"q": "Nosotros ___ (leer) un libro.", "ans": "leemos", "hint": "l_____", "why": "-er · nosotros → -emos"},
             {"q": "Mis amigos ___ (bailar) muy bien.", "ans": "bailan", "hint": "b_____", "why": "-ar · ellos → -an"},
             {"q": "¿Dónde ___ (vivir) tú?", "ans": "vives", "hint": "v____", "why": "-ir · tú → -es"},
             {"q": "Nina ___ (beber) agua.", "ans": "bebe", "hint": "b___", "why": "-er · ella → -e"},
         ]),
    dict(title="¿ser o tener? — escribe la forma", accents="strict",
         desc="Let op de valstrik voor Nederlandstaligen: je <b>bent</b> geen vijftien in het "
              "Spaans, je <b>hebt</b> vijftien jaar — <i>tengo quince años</i>.",
         items=[
             {"q": "Yo ___ quince años.", "ans": "tengo", "why": "leeftijd → tener, nooit ser"},
             {"q": "Lucía ___ de Sevilla.", "ans": "es", "why": "herkomst → ser"},
             {"q": "Nosotros ___ estudiantes.", "ans": "somos", "why": "identiteit → ser"},
             {"q": "Diego ___ dieciséis años.", "ans": "tiene", "why": "leeftijd → tener"},
             {"q": "¿Cuántos años ___ tú?", "ans": "tienes", "why": "leeftijd vragen → tener"},
             {"q": "Tú ___ muy simpático.", "ans": "eres", "why": "eigenschap → ser"},
             {"q": "Mis padres ___ belgas.", "ans": "son", "why": "nationaliteit → ser"},
             {"q": "Yo ___ de Bélgica.", "ans": "soy", "why": "herkomst → ser"},
             {"q": "¿___ (tú) hermanos?", "ans": "tienes", "why": "bezit → tener"},
             {"q": "Valen ___ colombiana.", "ans": "es", "why": "nationaliteit → ser"},
             {"q": "Nosotros ___ catorce años.", "ans": "tenemos", "why": "leeftijd → tener"},
             {"q": "Ustedes ___ profesores.", "ans": "son", "why": "beroep → ser"},
         ]),
    dict(title="Las palabras interrogativas — escribe la pregunta", accents="strict",
         desc="Vul het vraagwoord in. <b>Elk vraagwoord draagt een accent</b> — dat is geen "
              "versiering maar het verschil tussen een vraag en een gewone zin.",
         items=[
             {"q": "¿___ te llamas? — Me llamo Nina.", "ans": "Cómo", "hint": "C___", "why": "cómo = hoe"},
             {"q": "¿De ___ eres? — Soy de Madrid.", "ans": "dónde", "hint": "d____", "why": "de dónde = waarvandaan"},
             {"q": "¿___ años tienes? — Tengo quince.", "ans": "Cuántos", "hint": "C______", "why": "cuántos = hoeveel (mv.)"},
             {"q": "¿___ es tu profesora? — La señora Ruiz.", "ans": "Quién", "hint": "Q____", "why": "quién = wie"},
             {"q": "¿___ estudias? — Español.", "ans": "Qué", "hint": "Q__", "why": "qué = wat"},
             {"q": "¿___ es tu cumpleaños? — En mayo.", "ans": "Cuándo", "hint": "C_____", "why": "cuándo = wanneer"},
             {"q": "¿___ vives? — En Sevilla.", "ans": "Dónde", "hint": "D____", "why": "dónde = waar"},
             {"q": "¿___ hermanos tienes? — Dos.", "ans": "Cuántos", "hint": "C______", "why": "cuántos hermanos"},
             {"q": "¿___ tal? — Bien, gracias.", "ans": "Qué", "hint": "Q__", "why": "¿Qué tal? = hoe gaat het?"},
             {"q": "¿___ se dice «mochila» en neerlandés?", "ans": "Cómo", "hint": "C___", "why": "cómo se dice = hoe zeg je"},
             {"q": "¿___ son ellos? — Son mis primos.", "ans": "Quiénes", "hint": "Q______", "why": "meervoud van quién"},
             {"q": "¿___ es tu número de teléfono?", "ans": "Cuál", "hint": "C___", "why": "cuál = welk(e), bij een keuze uit veel"},
         ]),
]

SETS[("C5", 2)] = [
    dict(title="El verbo «tener» — rellena", accents="strict",
         desc="De klassieke invuloefening met het werkwoord van deze unidad. <b>tener</b> is "
              "onregelmatig: de <i>e</i> van de stam wordt <b>ie</b> — behalve bij "
              "<i>nosotros</i> en <i>vosotros</i>.",
         items=[
             {"q": "Yo ___ dos hermanos.", "ans": "tengo", "hint": "t____", "why": "yo → tengo (met -g-)"},
             {"q": "Mi abuela ___ setenta años.", "ans": "tiene", "hint": "t____", "why": "ella → tiene (e → ie)"},
             {"q": "¿Cuántos primos ___ tú?", "ans": "tienes", "hint": "t_____", "why": "tú → tienes (e → ie)"},
             {"q": "Nosotros ___ una mascota.", "ans": "tenemos", "hint": "t______", "why": "nosotros → tenemos, zónder ie"},
             {"q": "Mis padres ___ tres hijos.", "ans": "tienen", "hint": "t_____", "why": "ellos → tienen"},
             {"q": "Lucía ___ el pelo rizado.", "ans": "tiene", "hint": "t____", "why": "ella → tiene"},
             {"q": "Yo no ___ hermanas.", "ans": "tengo", "hint": "t____", "why": "yo → tengo"},
             {"q": "¿Vosotros ___ abuelos en Sevilla?", "ans": "tenéis", "hint": "t_____",
              "why": "vosotros → tenéis, zónder ie maar mét tilde"},
             {"q": "Mi tío ___ barba.", "ans": "tiene", "hint": "t____", "why": "él → tiene"},
             {"q": "Tú ___ los ojos verdes.", "ans": "tienes", "hint": "t_____", "why": "tú → tienes"},
             {"q": "Mis primas ___ el pelo largo.", "ans": "tienen", "hint": "t_____", "why": "ellas → tienen"},
             {"q": "Nosotras ___ una familia grande.", "ans": "tenemos", "hint": "t______", "why": "nosotras → tenemos"},
         ]),
    dict(title="Los posesivos — ¿mi, tu, su o nuestro?", accents="soft",
         desc="Schrijf het bezittelijk voornaamwoord voluit. <b>De vorm richt zich naar het "
              "díng, niet naar de bezitter</b>: <i>mis hermanas</i> (meervoud) · "
              "<i>nuestra casa</i> (vrouwelijk).",
         items=[
             {"q": "___ (yo) hermano se llama Pablo.", "ans": "mi", "why": "één ding → mi"},
             {"q": "___ (yo) hermanas son mayores.", "ans": "mis", "why": "meervoud ding → mis"},
             {"q": "¿Cómo se llama ___ (tú) madre?", "ans": "tu", "why": "één ding → tu (zonder tilde!)"},
             {"q": "___ (tú) abuelos viven en Cádiz.", "ans": "tus", "why": "meervoud → tus"},
             {"q": "Lucía habla de ___ (ella) prima.", "ans": "su", "why": "su = zijn/haar/hun — één vorm"},
             {"q": "Diego enseña una foto de ___ (él) tíos.", "ans": "sus", "why": "meervoud ding → sus"},
             {"q": "___ (nosotros) casa está en Sevilla.", "ans": "nuestra", "why": "la casa → nuestra"},
             {"q": "___ (nosotros) padres trabajan mucho.", "ans": "nuestros", "why": "los padres → nuestros"},
             {"q": "___ (nosotros) abuelo tiene ochenta años.", "ans": "nuestro", "why": "el abuelo → nuestro"},
             {"q": "___ (nosotros) primas son de Cádiz.", "ans": "nuestras", "why": "las primas → nuestras"},
             {"q": "¿Es ___ (tú) mascota?", "ans": "tu", "why": "la mascota, één ding → tu"},
             {"q": "Mis abuelos y ___ (ellos) hijos viven juntos.", "ans": "sus", "why": "los hijos → sus"},
         ]),
    dict(title="Los adjetivos — escribe la forma que concuerda", accents="strict",
         desc="Schrijf het bijvoeglijk naamwoord tussen haakjes in de vorm die <b>overeenkomt</b>: "
              "mannelijk of vrouwelijk, enkelvoud of meervoud. Let op de tildes — die horen bij "
              "het woord.",
         items=[
             {"q": "Mi hermana es muy ___ (simpático).", "ans": "simpática", "hint": "s________",
              "why": "vrouwelijk enkelvoud, tilde blijft"},
             {"q": "Mis primos son ___ (gracioso).", "ans": "graciosos", "hint": "g________", "why": "mannelijk meervoud"},
             {"q": "Lucía tiene el pelo ___ (rizado).", "ans": "rizado", "hint": "r_____",
              "why": "valstrik: het gaat over «el pelo», niet over Lucía"},
             {"q": "Mi abuelo tiene los ojos ___ (verde).", "ans": "verdes", "hint": "v_____",
              "why": "-e → alleen +s in het meervoud"},
             {"q": "Mis hermanas son ___ (rubio).", "ans": "rubias", "hint": "r_____", "why": "vrouwelijk meervoud"},
             {"q": "Diego es ___ (moreno).", "ans": "moreno", "hint": "m_____", "why": "mannelijk enkelvoud"},
             {"q": "Mi tía es ___ (trabajador).", "ans": "trabajadora", "hint": "t__________",
              "why": "-dor krijgt wél een -a: trabajadora"},
             {"q": "Los abuelos son muy ___ (hablador).", "ans": "habladores", "hint": "h_________",
              "why": "-dor → -dores in het meervoud"},
             {"q": "Mi madre y mi tía son ___ (inteligente).", "ans": "inteligentes", "hint": "i___________",
              "why": "-e → +s, geen -a"},
             {"q": "Mi primo tiene el pelo ___ (corto).", "ans": "corto", "hint": "c____", "why": "el pelo → mannelijk enkelvoud"},
             {"q": "Mi hermana es ___ (tímido).", "ans": "tímida", "hint": "t_____", "why": "esdrújula → tilde blijft staan"},
             {"q": "Mis padres son ___ (alegre).", "ans": "alegres", "hint": "a______", "why": "-e → +s"},
         ]),
]

SETS[("C5", 3)] = [
    dict(title="Los verbos reflexivos — rellena", accents="strict",
         desc="Bij een reflexief werkwoord horen er <b>twee woorden</b> in het gat: eerst het "
              "pronombre, dan de vorm — <i>me levanto</i>, niet <i>levanto</i>. Let op: bij "
              "<i>nosotros</i> verandert de stam níét.",
         items=[
             {"q": "Yo ___ (despertarse) a las siete.", "ans": "me despierto", "hint": "m_ d________",
              "why": "yo → me · e → ie"},
             {"q": "Pau ___ (levantarse) muy temprano.", "ans": "se levanta", "hint": "s_ l______",
              "why": "él → se · regelmatig"},
             {"q": "Nosotros ___ (ducharse) por la mañana.", "ans": "nos duchamos", "hint": "n__ d_______",
              "why": "nosotros → nos"},
             {"q": "¿A qué hora ___ (acostarse) tú?", "ans": "te acuestas", "hint": "t_ a_______",
              "why": "tú → te · o → ue"},
             {"q": "Mis hermanas ___ (vestirse) rápido.", "ans": "se visten", "hint": "s_ v_____",
              "why": "ellas → se · e → i"},
             {"q": "Yo ___ (lavarse) las manos antes de comer.", "ans": "me lavo", "hint": "m_ l___",
              "why": "yo → me · regelmatig"},
             {"q": "Tú ___ (peinarse) delante del espejo.", "ans": "te peinas", "hint": "t_ p_____",
              "why": "tú → te"},
             {"q": "Nosotras ___ (acostarse) a las once.", "ans": "nos acostamos", "hint": "n__ a________",
              "why": "nosotras → nos · géén o → ue"},
             {"q": "Mi padre ___ (despertarse) con el móvil.", "ans": "se despierta", "hint": "s_ d________",
              "why": "él → se · e → ie"},
             {"q": "¿Vosotros ___ (levantarse) tarde los domingos?", "ans": "os levantáis",
              "hint": "o_ l________", "why": "vosotros → os · levantáis mét tilde"},
             {"q": "Los niños ___ (ducharse) por la noche.", "ans": "se duchan", "hint": "s_ d_____",
              "why": "ellos → se"},
             {"q": "Yo ___ (vestirse) en dos minutos.", "ans": "me visto", "hint": "m_ v____",
              "why": "yo → me · e → i"},
         ]),
    dict(title="Presente irregular — el cambio de raíz", accents="strict",
         desc="De klinker in de <b>stam</b> verandert — maar <b>nooit</b> bij <i>nosotros</i> en "
              "<i>vosotros</i>. Drie soorten: <b>o → ue</b> · <b>e → ie</b> · <b>e → i</b> "
              "(en <i>jugar</i> doet u → ue).",
         items=[
             {"q": "Yo ___ (dormir) ocho horas.", "ans": "duermo", "hint": "d_____", "why": "o → ue"},
             {"q": "La clase ___ (empezar) a las nueve.", "ans": "empieza", "hint": "e______", "why": "e → ie"},
             {"q": "Nosotros ___ (poder) ir contigo.", "ans": "podemos", "hint": "p______",
              "why": "valstrik: bij nosotros géén o → ue"},
             {"q": "¿Qué ___ (querer) tú?", "ans": "quieres", "hint": "q______", "why": "e → ie"},
             {"q": "Pau ___ (volver) a casa a las seis.", "ans": "vuelve", "hint": "v_____", "why": "o → ue"},
             {"q": "Yo ___ (pedir) un café.", "ans": "pido", "hint": "p___", "why": "e → i"},
             {"q": "Mis amigos ___ (jugar) al baloncesto.", "ans": "juegan", "hint": "j_____", "why": "u → ue"},
             {"q": "Nosotras ___ (dormir) poco entre semana.", "ans": "dormimos", "hint": "d_______",
              "why": "valstrik: nosotras houdt de o"},
             {"q": "¿Tú ___ (preferir) el té o el café?", "ans": "prefieres", "hint": "p________", "why": "e → ie"},
             {"q": "Yo ___ (almorzar) en el instituto.", "ans": "almuerzo", "hint": "a_______", "why": "o → ue"},
             {"q": "El camarero ___ (repetir) el pedido.", "ans": "repite", "hint": "r_____", "why": "e → i"},
             {"q": "Vosotros ___ (querer) salir, ¿verdad?", "ans": "queréis", "hint": "q______",
              "why": "vosotros houdt de e — mét tilde"},
         ]),
    dict(title="hacer · ir · salir — los tres del día", accents="strict",
         desc="Drie werkwoorden die je elke dag nodig hebt, en alle drie onregelmatig. Twee "
              "hebben een rare <b>yo</b>-vorm (<i>hago</i>, <i>salgo</i>); <i>ir</i> is helemaal "
              "eigenzinnig.",
         items=[
             {"q": "Yo ___ (hacer) los deberes por la tarde.", "ans": "hago", "hint": "h___",
              "why": "yo hago — met -g-"},
             {"q": "¿Qué ___ (hacer) tú los sábados?", "ans": "haces", "hint": "h____", "why": "tú haces, normaal"},
             {"q": "Nosotros ___ (hacer) deporte dos veces por semana.", "ans": "hacemos", "hint": "h______"},
             {"q": "Mis padres ___ (hacer) la compra el viernes.", "ans": "hacen", "hint": "h____"},
             {"q": "Yo ___ (ir) al instituto en bici.", "ans": "voy", "hint": "v__", "why": "ir → voy"},
             {"q": "¿Adónde ___ (ir) tú ahora?", "ans": "vas", "hint": "v__"},
             {"q": "Pau ___ (ir) al gimnasio los lunes.", "ans": "va", "hint": "v_"},
             {"q": "Nosotras ___ (ir) al cine el fin de semana.", "ans": "vamos", "hint": "v____"},
             {"q": "Yo ___ (salir) de casa a las ocho.", "ans": "salgo", "hint": "s____",
              "why": "yo salgo — met -g-"},
             {"q": "¿A qué hora ___ (salir) vosotros?", "ans": "salís", "hint": "s____",
              "why": "salís mét tilde"},
             {"q": "Mi hermana ___ (salir) con sus amigas.", "ans": "sale", "hint": "s___"},
             {"q": "Ellos ___ (ir) a la playa en verano.", "ans": "van", "hint": "v__"},
         ]),
]

SETS[("C5", 4)] = [
    dict(title="Gustar al revés — escribe el pronombre y la forma", accents="strict",
         desc="Bij <i>gustar</i> is de persoon niet het onderwerp: het <b>ding</b> is dat. "
              "Schrijf allebei de woorden. Eén ding of een infinitivo → <b>gusta</b> · "
              "meerdere dingen → <b>gustan</b>.",
         items=[
             {"q": "A mí ___ la playa.", "ans": "me gusta", "hint": "m_ g____", "why": "één ding → gusta"},
             {"q": "A ti ___ los videojuegos.", "ans": "te gustan", "hint": "t_ g_____", "why": "meervoud → gustan"},
             {"q": "A Lucía ___ nadar en el mar.", "ans": "le gusta", "hint": "l_ g____",
              "why": "infinitivo telt als enkelvoud"},
             {"q": "A nosotros ___ las series españolas.", "ans": "nos gustan", "hint": "n__ g_____"},
             {"q": "A mis padres ___ la paella.", "ans": "les gusta", "hint": "l__ g____",
              "why": "twee personen → les, maar la paella → gusta"},
             {"q": "A mí ___ las canciones de ese grupo.", "ans": "me gustan", "hint": "m_ g_____"},
             {"q": "¿___ el cine? (a ti)", "ans": "te gusta", "hint": "t_ g____"},
             {"q": "A mi hermano ___ los deportes de playa.", "ans": "le gustan", "hint": "l_ g_____"},
             {"q": "A nosotras ___ bailar y cantar.", "ans": "nos gusta", "hint": "n__ g____",
              "why": "twee infinitivos blijven toch «gusta»"},
             {"q": "A vosotros ___ la horchata, ¿verdad?", "ans": "os gusta", "hint": "o_ g____",
              "why": "vosotros → os"},
             {"q": "A Diego y a Nina ___ los conciertos.", "ans": "les gustan", "hint": "l__ g_____"},
             {"q": "A mí no ___ nada el fútbol.", "ans": "me gusta", "hint": "m_ g____",
              "why": "ook ontkennend blijft de bouw hetzelfde"},
         ]),
    dict(title="Reaccionar — también · tampoco · a mí sí · a mí no", accents="strict",
         desc="Vier korte reacties, en de keuze hangt af van <b>twee</b> dingen: is de zin van de "
              "ander positief of negatief, en ben jij het eens of niet? "
              "<b>ook</b> na iets positiefs = <i>también</i> · <b>ook niet</b> na iets negatiefs "
              "= <i>tampoco</i>.",
         items=[
             {"q": "— Me gusta la playa. — A mí ___. (jij ook)", "ans": "también", "hint": "t______"},
             {"q": "— No me gusta el fútbol. — A mí ___. (jij ook niet)", "ans": "tampoco", "hint": "t______"},
             {"q": "— Me encanta bailar. — A mí ___. (jij niet)", "ans": "no", "hint": "n_",
              "why": "positief + jij oneens → a mí no"},
             {"q": "— No me gustan los videojuegos. — A mí ___. (jij wél)", "ans": "sí", "hint": "s_",
              "why": "negatief + jij oneens → a mí sí"},
             {"q": "— Me interesa la música latina. — A mí ___. (jij ook)", "ans": "también", "hint": "t______"},
             {"q": "— No me gusta madrugar. — A mí ___. (jij ook niet)", "ans": "tampoco", "hint": "t______"},
             {"q": "— Odio las series largas. — Yo ___. (jij ook)", "ans": "también", "hint": "t______",
              "why": "odiar is een gewoon werkwoord → yo también"},
             {"q": "— Me gustan las Fallas. — A mí ___. (jij niet)", "ans": "no", "hint": "n_"},
             {"q": "— No como carne. — Yo ___. (jij ook niet)", "ans": "tampoco", "hint": "t______"},
             {"q": "— Prefiero el mar. — Yo ___. (jij ook)", "ans": "también", "hint": "t______"},
             {"q": "— No me gusta esta canción. — A mí ___. (jij wél)", "ans": "sí", "hint": "s_"},
             {"q": "— Me aburre el baloncesto. — A mí ___. (jij ook)", "ans": "también", "hint": "t______"},
         ]),
    dict(title="Proponer un plan — querer · poder + infinitivo", accents="strict",
         desc="Twee werkwoorden met een klinkerwissel (<b>e → ie</b> en <b>o → ue</b>) plus een "
              "infinitivo die je <b>niet</b> vervoegt. Bij <i>nosotros</i> blijft de stam gewoon.",
         items=[
             {"q": "Yo ___ (querer) ir a la playa.", "ans": "quiero", "hint": "q_____", "why": "e → ie"},
             {"q": "¿Tú ___ (poder) salir el sábado?", "ans": "puedes", "hint": "p_____", "why": "o → ue"},
             {"q": "Nosotros ___ (querer) quedar a las seis.", "ans": "queremos", "hint": "q_______",
              "why": "valstrik: nosotros houdt de e"},
             {"q": "Diego no ___ (poder) venir hoy.", "ans": "puede", "hint": "p____"},
             {"q": "Mis amigas ___ (querer) ver la película.", "ans": "quieren", "hint": "q______"},
             {"q": "¿___ (querer) tú tocar la guitarra conmigo?", "ans": "Quieres", "hint": "Q______"},
             {"q": "Yo ___ (poder) quedar después de clase.", "ans": "puedo", "hint": "p____"},
             {"q": "Nosotras ___ (poder) ir en bici.", "ans": "podemos", "hint": "p______",
              "why": "valstrik: nosotras houdt de o"},
             {"q": "¿Vosotros ___ (querer) escuchar mi playlist?", "ans": "queréis", "hint": "q______",
              "why": "vosotros houdt de e — mét tilde"},
             {"q": "Nina ___ (querer) aprender a nadar.", "ans": "quiere", "hint": "q_____"},
             {"q": "Ellos no ___ (poder) jugar al baloncesto los lunes.", "ans": "pueden", "hint": "p_____"},
             {"q": "¿A qué hora ___ (poder) quedar nosotros?", "ans": "podemos", "hint": "p______"},
         ]),
]

SETS[("C5", 5)] = [
    dict(title="Voy a comer — ir a + infinitivo", accents="strict",
         desc="Zo praat je over straks: de vorm van <i>ir</i>, dan <b>a</b>, dan de infinitivo "
              "die je <b>niet</b> vervoegt. Schrijf alle drie de stukken.",
         items=[
             {"q": "Hoy yo ___ (probar) el guacamole.", "ans": "voy a probar", "hint": "v__ a p_____",
              "why": "yo → voy a + infinitivo"},
             {"q": "Nosotros ___ (reservar) una mesa para cuatro.", "ans": "vamos a reservar",
              "hint": "v____ a r_______", "why": "nosotros → vamos a"},
             {"q": "¿Tú ___ (pedir) el menú del día?", "ans": "vas a pedir", "hint": "v__ a p____",
              "why": "tú → vas a"},
             {"q": "Diego ___ (tomar) un zumo de naranja.", "ans": "va a tomar", "hint": "v_ a t____"},
             {"q": "Mis amigos ___ (comer) tacos en el mercado.", "ans": "van a comer",
              "hint": "v__ a c____"},
             {"q": "Yo no ___ (tomar) postre.", "ans": "voy a tomar", "hint": "v__ a t____"},
             {"q": "¿Vosotros ___ (pagar) con tarjeta?", "ans": "vais a pagar", "hint": "v___ a p____",
              "why": "vosotros → vais a"},
             {"q": "El camarero ___ (traer) la cuenta.", "ans": "va a traer", "hint": "v_ a t____"},
             {"q": "Nosotras ___ (compartir) una ración de churros.", "ans": "vamos a compartir",
              "hint": "v____ a c________"},
             {"q": "Mañana yo ___ (cocinar) para toda la familia.", "ans": "voy a cocinar",
              "hint": "v__ a c______"},
             {"q": "¿Qué ___ (tomar) usted de primer plato?", "ans": "va a tomar", "hint": "v_ a t____",
              "why": "usted → va a"},
             {"q": "Ellas ___ (beber) agua con limón.", "ans": "van a beber", "hint": "v__ a b____"},
         ]),
    dict(title="Cantidades — mucho · mucha · muchos · muchas", accents="strict",
         desc="<b>mucho</b> past zich aan bij het woord erna: <i>mucha sal</i> · <i>muchos "
              "tomates</i>. Maar vóór een <b>werkwoord</b> verandert het nooit: <i>como "
              "mucho</i>. <b>Un poco de</b> blijft altijd hetzelfde.",
         items=[
             {"q": "En esta sopa hay ___ (mucho) sal.", "ans": "mucha", "hint": "m____",
              "why": "la sal → mucha"},
             {"q": "Como ___ (mucho) fruta por la mañana.", "ans": "mucha", "hint": "m____",
              "why": "la fruta → mucha"},
             {"q": "Hay ___ (mucho) tomates en la ensalada.", "ans": "muchos", "hint": "m_____",
              "why": "los tomates → muchos"},
             {"q": "Bebo ___ (mucho) agua.", "ans": "mucha", "hint": "m____",
              "why": "el agua is femenino: mucha agua"},
             {"q": "En México hay ___ (mucho) salsas diferentes.", "ans": "muchas", "hint": "m_____"},
             {"q": "Mi hermano come ___ (mucho).", "ans": "mucho", "hint": "m____",
              "why": "na een werkwoord verandert het niet"},
             {"q": "Hay ___ (poco) leche en la nevera.", "ans": "poca", "hint": "p___",
              "why": "la leche → poca"},
             {"q": "¿Me pone ___ azúcar, por favor? (een beetje)", "ans": "un poco de",
              "hint": "u_ p___ d_", "why": "vaste uitdrukking: un poco de — verandert nooit"},
             {"q": "Tengo ___ (poco) tiempo para cocinar.", "ans": "poco", "hint": "p___",
              "why": "el tiempo → poco"},
             {"q": "El pollo tiene ___ (mucho) ajo.", "ans": "mucho", "hint": "m____",
              "why": "el ajo → mucho"},
             {"q": "En el mercado venden ___ (mucho) frutas tropicales.", "ans": "muchas",
              "hint": "m_____"},
             {"q": "Este plato tiene ___ (poco) verduras.", "ans": "pocas", "hint": "p____",
              "why": "las verduras → pocas"},
         ]),
    dict(title="Lo · la · los · las — no repitas la palabra", accents="soft",
         desc="Je hebt het gerecht al genoemd; nu vervang je het door één woordje. Het komt "
              "overeen in geslacht en getal en staat <b>vóór</b> het werkwoord — <i>¿La "
              "cuenta? La traigo.</i>",
         items=[
             {"q": "¿La cuenta? Ahora ___ traigo.", "ans": "la", "why": "la cuenta → la"},
             {"q": "¿El menú? ___ tenemos aquí.", "ans": "lo", "why": "el menú → lo"},
             {"q": "¿Los churros? ___ comemos con chocolate.", "ans": "los", "why": "los churros → los"},
             {"q": "¿Las fresas? ___ compro en el mercado.", "ans": "las", "why": "las fresas → las"},
             {"q": "¿El pescado? No ___ como nunca.", "ans": "lo", "why": "el pescado → lo"},
             {"q": "¿La sopa? ___ prefiero caliente.", "ans": "la", "why": "la sopa → la"},
             {"q": "¿Los tacos? ___ pedimos con carne.", "ans": "los", "why": "los tacos → los"},
             {"q": "¿La propina? ___ dejamos en la mesa.", "ans": "la", "why": "la propina → la"},
             {"q": "¿El café? ___ tomo sin azúcar.", "ans": "lo", "why": "el café → lo"},
             {"q": "¿Las servilletas? ___ pongo yo.", "ans": "las", "why": "las servilletas → las"},
             {"q": "¿El guacamole? ___ hago con aguacate y limón.", "ans": "lo", "why": "el guacamole → lo"},
             {"q": "¿Las patatas? ___ quiero fritas.", "ans": "las", "why": "las patatas → las"},
         ]),
]

SETS[("C5", 8)] = [
    dict(title="El pretérito perfecto — haber + participio", accents="strict",
         desc="De tijd van «wat heb je vandaag gedaan». Schrijf <b>allebei</b> de woorden: "
              "de vorm van <i>haber</i> (he · has · ha · hemos · habéis · han) en het "
              "participio: <b>-ar → -ado</b> · <b>-er/-ir → -ido</b>.",
         items=[
             {"q": "Hoy yo ___ (visitar) las ruinas.", "ans": "he visitado", "hint": "h_ v_______",
              "why": "yo → he + -ado"},
             {"q": "¿Tú ___ (subir) alguna vez a los Andes?", "ans": "has subido", "hint": "h__ s_____",
              "why": "tú → has · -ir → -ido"},
             {"q": "Nina ___ (sacar) cien fotos esta mañana.", "ans": "ha sacado", "hint": "h_ s_____"},
             {"q": "Nosotros ___ (comer) en el mercado de Cusco.", "ans": "hemos comido",
              "hint": "h____ c_____", "why": "nosotros → hemos"},
             {"q": "Mis padres ___ (perder) el tren.", "ans": "han perdido", "hint": "h__ p______"},
             {"q": "Yo todavía no ___ (comprar) los recuerdos.", "ans": "he comprado",
              "hint": "h_ c_______"},
             {"q": "¿Vosotros ___ (dormir) bien esta noche?", "ans": "habéis dormido",
              "hint": "h_____ d______", "why": "vosotros → habéis, mét tilde"},
             {"q": "Esta semana ___ (llover) todos los días.", "ans": "ha llovido", "hint": "h_ l______",
              "why": "weerwerkwoorden staan altijd in de derde persoon"},
             {"q": "Yo ___ (aprender) tres palabras en quechua.", "ans": "he aprendido",
              "hint": "h_ a________"},
             {"q": "Nosotras ___ (viajar) en autobús hasta Aguas Calientes.", "ans": "hemos viajado",
              "hint": "h____ v______"},
             {"q": "El guía ___ (explicar) la historia de la ciudad.", "ans": "ha explicado",
              "hint": "h_ e________"},
             {"q": "Ellos ___ (beber) mate de coca.", "ans": "han bebido", "hint": "h__ b_____"},
         ]),
    dict(title="Los participios irregulares", accents="strict",
         desc="Acht werkwoorden weigeren de gewone uitgang — precies de acht die op de "
              "vocabulariolijst van deze unidad staan. Schrijf <b>alleen</b> het participio.",
         items=[
             {"q": "hacer → he ___", "ans": "hecho", "hint": "h____", "why": "hacer → hecho"},
             {"q": "ver → he ___", "ans": "visto", "hint": "v____", "why": "ver → visto"},
             {"q": "decir → he ___", "ans": "dicho", "hint": "d____", "why": "decir → dicho"},
             {"q": "escribir → he ___", "ans": "escrito", "hint": "e______", "why": "escribir → escrito"},
             {"q": "volver → he ___", "ans": "vuelto", "hint": "v_____", "why": "volver → vuelto"},
             {"q": "poner → he ___", "ans": "puesto", "hint": "p_____", "why": "poner → puesto"},
             {"q": "abrir → he ___", "ans": "abierto", "hint": "a______", "why": "abrir → abierto"},
             {"q": "romper → he ___", "ans": "roto", "hint": "r___", "why": "romper → roto"},
             {"q": "viajar → he ___", "ans": "viajado", "hint": "v______",
              "why": "valstrik: viajar is gewoon regelmatig"},
             {"q": "subir → he ___", "ans": "subido", "hint": "s_____",
              "why": "valstrik: subir is gewoon regelmatig"},
             {"q": "leer → he ___", "ans": "leído", "hint": "l____",
              "why": "leer → leído, met een tilde op de i"},
             {"q": "traer → he ___", "ans": "traído", "hint": "t_____",
              "why": "traer → traído, ook met tilde"},
         ]),
    dict(title="Marcadores — ya · todavía no · nunca · alguna vez", accents="strict",
         desc="Vier woorden die zeggen <b>waar je staat</b> in een reeks ervaringen. "
              "<b>ya</b> = al · <b>todavía no</b> = nog niet · <b>nunca</b> = nooit · "
              "<b>alguna vez</b> = ooit (alleen in een vraag).",
         items=[
             {"q": "— ¿Has visto Machu Picchu? — Sí, ___ lo he visto.", "ans": "ya",
              "why": "bevestigend en afgevinkt → ya"},
             {"q": "— ¿Has subido a la montaña? — No, ___ ___ he subido.", "ans": "todavía no",
              "why": "nog niet, maar het kan nog → todavía no"},
             {"q": "¿Has viajado ___ ___ en barco?", "ans": "alguna vez",
              "why": "in een vraag naar ervaring → alguna vez"},
             {"q": "Yo ___ he comido cuy. (nooit)", "ans": "nunca"},
             {"q": "— ¿Habéis hecho las maletas? — Sí, ___ están listas.", "ans": "ya"},
             {"q": "Mi hermano ___ ha visto la nieve. (nooit)", "ans": "nunca"},
             {"q": "— ¿Has escrito la postal? — No, ___ ___ la he escrito.", "ans": "todavía no"},
             {"q": "¿Has estado ___ ___ en Perú?", "ans": "alguna vez"},
             {"q": "El tren ___ ha salido: son las nueve y cinco.", "ans": "ya"},
             {"q": "Nosotros ___ hemos perdido una maleta. (nooit)", "ans": "nunca"},
             {"q": "— ¿Ha llegado el guía? — No, ___ ___ ha llegado.", "ans": "todavía no"},
             {"q": "¿Habéis probado ___ ___ la comida andina?", "ans": "alguna vez"},
         ]),
]

SETS[("C5", 7)] = [
    dict(title="¿hay o está(n)? — escribe la forma", accents="strict",
         desc="<b>hay</b> als het iets nieuws of ongeteld is (un · dos · mucho) · "
              "<b>está / están</b> als het al bepaald is (el · la · mi · este). De tilde op "
              "<i>está</i> hoort erbij.",
         items=[
             {"q": "En mi barrio ___ una panadería muy buena.", "ans": "hay", "why": "una → hay"},
             {"q": "La panadería ___ enfrente del banco.", "ans": "está",
              "why": "la panadería → está, mét tilde"},
             {"q": "En el salón ___ dos sofás y una alfombra.", "ans": "hay", "why": "dos → hay"},
             {"q": "Mis zapatos ___ debajo de la cama.", "ans": "están", "why": "mis zapatos → están"},
             {"q": "¿Dónde ___ el museo?", "ans": "está", "why": "el museo → está"},
             {"q": "Cerca de la plaza ___ un parque grande.", "ans": "hay", "why": "un → hay"},
             {"q": "El espejo ___ encima del armario.", "ans": "está", "why": "el espejo → está"},
             {"q": "En mi calle no ___ semáforos.", "ans": "hay", "why": "ontkend onbepaald → hay"},
             {"q": "Las sillas ___ alrededor de la mesa.", "ans": "están", "why": "las sillas → están"},
             {"q": "¿Cuántas habitaciones ___ en tu piso?", "ans": "hay", "why": "cuántas → tellen → hay"},
             {"q": "La estación ___ lejos de aquí.", "ans": "está", "why": "la estación → está"},
             {"q": "En la esquina ___ una farmacia de guardia.", "ans": "hay", "why": "una → hay"},
         ]),
    dict(title="El imperativo — explica el camino", accents="strict",
         desc="De <b>tú</b>-vorm van het bevel is meestal gewoon de <i>él</i>-vorm van het "
              "presente: <i>sigue</i>, <i>gira</i>, <i>cruza</i>. Acht werkwoorden zijn kort en "
              "onregelmatig: <b>ve · haz · pon · ten · sal · di · ven · sé</b>.",
         items=[
             {"q": "___ (seguir) todo recto hasta la plaza.", "ans": "Sigue", "hint": "S____",
              "why": "seguir → sigue (e → i)"},
             {"q": "___ (girar) a la derecha en el semáforo.", "ans": "Gira", "hint": "G___"},
             {"q": "___ (cruzar) la calle por el paso de peatones.", "ans": "Cruza", "hint": "C____"},
             {"q": "___ (tomar) la segunda calle a la izquierda.", "ans": "Toma", "hint": "T___"},
             {"q": "___ (bajar) en la parada del museo.", "ans": "Baja", "hint": "B___"},
             {"q": "___ (subir) por la escalera, el ascensor no funciona.", "ans": "Sube", "hint": "S___"},
             {"q": "___ (ir) hasta el final de la calle.", "ans": "Ve", "hint": "V_",
              "why": "ir → ve, onregelmatig en kort"},
             {"q": "___ (hacer) lo que dice el mapa.", "ans": "Haz", "hint": "H__",
              "why": "hacer → haz"},
             {"q": "___ (salir) del metro por la puerta norte.", "ans": "Sal", "hint": "S__",
              "why": "salir → sal"},
             {"q": "___ (decir) mi nombre en la recepción.", "ans": "Di", "hint": "D_",
              "why": "decir → di"},
             {"q": "___ (venir) a mi casa después de clase.", "ans": "Ven", "hint": "V__",
              "why": "venir → ven"},
             {"q": "___ (coger) el autobús número doce.", "ans": "Coge", "hint": "C___",
              "why": "coger → coge, regelmatig"},
         ]),
    dict(title="Los ordinales — primero o primer", accents="strict",
         desc="<b>primero</b> en <b>tercero</b> verliezen hun <b>-o</b> vlak vóór een "
              "mannelijk enkelvoudig woord: <i>el <b>primer</b> piso</i>, maar <i>la "
              "<b>primera</b> calle</i>. Alle andere ordinales veranderen alleen van "
              "geslacht.",
         items=[
             {"q": "Vivo en el ___ (primero) piso.", "ans": "primer", "hint": "p_____",
              "why": "vóór mannelijk enkelvoud → primer"},
             {"q": "Es la ___ (primero) calle a la derecha.", "ans": "primera", "hint": "p______",
              "why": "la calle → primera, volledig"},
             {"q": "El museo está en la ___ (tercero) planta.", "ans": "tercera", "hint": "t______"},
             {"q": "Toma la ___ (segundo) calle a la izquierda.", "ans": "segunda", "hint": "s______"},
             {"q": "Mi abuela vive en el ___ (tercero) piso.", "ans": "tercer", "hint": "t_____",
              "why": "vóór mannelijk enkelvoud → tercer"},
             {"q": "Es el ___ (cuarto) edificio de la calle.", "ans": "cuarto", "hint": "c_____",
              "why": "cuarto verliest niets"},
             {"q": "Gira en el ___ (primero) semáforo.", "ans": "primer", "hint": "p_____"},
             {"q": "Es la ___ (quinto) puerta del pasillo.", "ans": "quinta", "hint": "q_____"},
             {"q": "El ascensor sube hasta el ___ (décimo) piso.", "ans": "décimo", "hint": "d_____",
              "why": "décimo houdt zijn tilde"},
             {"q": "Es el ___ (segundo) día que vengo aquí.", "ans": "segundo", "hint": "s______"},
             {"q": "Baja en la ___ (sexto) parada.", "ans": "sexta", "hint": "s____"},
             {"q": "Mi clase está en el ___ (primero) pasillo a la izquierda.", "ans": "primer",
              "hint": "p_____"},
         ]),
]

SETS[("C5", 6)] = [
    dict(title="Acabar de + infinitivo — net gebeurd", accents="strict",
         desc="«Ik heb net…» zeg je met <b>acabar de</b> + infinitivo. Je vervoegt alleen "
              "<i>acabar</i>; het tweede werkwoord blijft in de infinitivo staan.",
         items=[
             {"q": "Yo ___ (acabar) de comprar unos vaqueros.", "ans": "acabo", "hint": "a____",
              "why": "yo → acabo de + infinitivo"},
             {"q": "Lucía ___ (acabar) de probarse el vestido.", "ans": "acaba", "hint": "a____"},
             {"q": "Nosotros ___ (acabar) de pagar en la caja.", "ans": "acabamos", "hint": "a_______"},
             {"q": "¿Tú ___ (acabar) de ver el escaparate?", "ans": "acabas", "hint": "a_____"},
             {"q": "Mis amigas ___ (acabar) de entrar en la zapatería.", "ans": "acaban", "hint": "a_____"},
             {"q": "Yo ___ (acabar) de encontrar mi talla.", "ans": "acabo", "hint": "a____"},
             {"q": "El dependiente ___ (acabar) de abrir la tienda.", "ans": "acaba", "hint": "a____"},
             {"q": "¿Vosotros ___ (acabar) de llegar al centro comercial?", "ans": "acabáis",
              "hint": "a______", "why": "vosotros → acabáis, mét tilde"},
             {"q": "Nosotras ___ (acabar) de ver las rebajas.", "ans": "acabamos", "hint": "a_______"},
             {"q": "Ellos ___ (acabar) de salir del probador.", "ans": "acaban", "hint": "a_____"},
             {"q": "Yo ___ (acabar) de gastar todo mi dinero.", "ans": "acabo", "hint": "a____"},
             {"q": "Diego ___ (acabar) de regatear en el tianguis.", "ans": "acaba", "hint": "a____"},
         ]),
    dict(title="Este · ese · aquel — ¿cerca o lejos?", accents="soft",
         desc="Drie afstanden: <b>este</b> hier bij mij · <b>ese</b> daar bij jou · "
              "<b>aquel</b> ginder, ver van ons allebei. En het komt overeen met het kledingstuk: "
              "<i>esta falda</i>, <i>estos zapatos</i>.",
         items=[
             {"q": "___ camiseta que tengo en la mano me gusta. (hier)", "ans": "Esta", "hint": "E___"},
             {"q": "___ zapatos que llevas tú son bonitos. (daar bij jou)", "ans": "Esos", "hint": "E___"},
             {"q": "___ abrigo del escaparate es carísimo. (ginder)", "ans": "Aquel", "hint": "A____"},
             {"q": "¿Cuánto cuestan ___ botas de aquí?", "ans": "estas", "hint": "e____"},
             {"q": "___ falda que tienes ahí es de rayas. (daar bij jou)", "ans": "Esa", "hint": "E__"},
             {"q": "___ pantalones que llevo puestos son de algodón. (hier)", "ans": "Estos",
              "hint": "E____"},
             {"q": "___ tienda del final de la calle vende ropa de segunda mano. (ginder)",
              "ans": "Aquella", "hint": "A______", "why": "la tienda → aquella"},
             {"q": "___ sombrero que llevas puesto te queda bien. (daar bij jou)", "ans": "Ese",
              "hint": "E__", "why": "el sombrero, bij jou → ese"},
             {"q": "___ sandalias de allá son las más baratas.", "ans": "Aquellas", "hint": "A_______"},
             {"q": "¿Te gusta ___ vestido que tengo aquí?", "ans": "este", "hint": "e___"},
             {"q": "___ gafas de sol que llevas son geniales.", "ans": "Esas", "hint": "E___"},
             {"q": "___ jersey de aquí es de lana.", "ans": "Este", "hint": "E___",
              "why": "el jersey → este"},
         ]),
    dict(title="Concordancia — el color y la prenda", accents="strict",
         desc="Het kleurwoord richt zich naar het kledingstuk. Let op de drie soorten: "
              "<b>-o/-a</b> verandert (rojo → roja) · <b>-e</b> en medeklinker krijgen alleen "
              "een <b>-s</b> (verde → verdes) · <b>rosa</b>, <b>naranja</b> en <b>lila</b> "
              "veranderen <b>nooit</b>.",
         items=[
             {"q": "una camiseta ___ (rojo)", "ans": "roja", "hint": "r___", "why": "la camiseta → roja"},
             {"q": "unos zapatos ___ (negro)", "ans": "negros", "hint": "n_____", "why": "los zapatos → negros"},
             {"q": "una falda ___ (verde)", "ans": "verde", "hint": "v____", "why": "-e verandert niet"},
             {"q": "unos calcetines ___ (blanco)", "ans": "blancos", "hint": "b______"},
             {"q": "dos camisas ___ (azul)", "ans": "azules", "hint": "a_____",
              "why": "medeklinker → alleen +es in het meervoud"},
             {"q": "una chaqueta ___ (marrón)", "ans": "marrón", "hint": "m_____",
              "why": "enkelvoud blijft marrón, mét tilde"},
             {"q": "unas botas ___ (marrón)", "ans": "marrones", "hint": "m_______",
              "why": "meervoud verliest de tilde: marrones"},
             {"q": "una sudadera ___ (rosa)", "ans": "rosa", "hint": "r___", "why": "rosa verandert nooit"},
             {"q": "unas zapatillas ___ (naranja)", "ans": "naranja", "hint": "n______",
              "why": "naranja verandert nooit, ook niet in het meervoud"},
             {"q": "un vestido ___ (morado)", "ans": "morado", "hint": "m_____"},
             {"q": "unos pantalones ___ (gris)", "ans": "grises", "hint": "g_____"},
             {"q": "una bufanda ___ (amarillo)", "ans": "amarilla", "hint": "a_______"},
         ]),
]

SETS[("C6+", 1)] = [
    dict(title="Los verbos reflexivos — rellena", accents="strict",
         desc="Vergeet het <b>pronombre</b> niet: bij een reflexief werkwoord horen er twee "
              "woorden in het gat — <i>me levanto</i>, niet <i>levanto</i>.",
         items=[
             {"q": "Yo ___ (levantarse) a las siete.", "ans": "me levanto", "hint": "m_ l______", "why": "yo → me"},
             {"q": "Diego ___ (ducharse) por la mañana.", "ans": "se ducha", "hint": "s_ d____", "why": "él → se"},
             {"q": "Nosotros ___ (acostarse) a las once.", "ans": "nos acostamos", "hint": "n__ a________",
              "why": "nosotros → nos · en géén o→ue bij nosotros"},
             {"q": "¿A qué hora ___ (despertarse) tú?", "ans": "te despiertas", "hint": "t_ d_________", "why": "tú → te · e→ie"},
             {"q": "Lucía ___ (vestirse) rápido.", "ans": "se viste", "hint": "s_ v____", "why": "e→i"},
             {"q": "Yo ___ (despertarse) muy temprano.", "ans": "me despierto", "hint": "m_ d________", "why": "e→ie"},
             {"q": "Mis hermanos ___ (peinarse) delante del espejo.", "ans": "se peinan", "hint": "s_ p_____", "why": "ellos → se"},
             {"q": "Nosotros ___ (lavarse) las manos.", "ans": "nos lavamos", "hint": "n__ l______", "why": "regelmatig"},
             {"q": "Nina ___ (acostarse) tarde.", "ans": "se acuesta", "hint": "s_ a______", "why": "o→ue"},
             {"q": "¿Tú ___ (afeitarse) todos los días?", "ans": "te afeitas", "hint": "t_ a______", "why": "tú → te"},
             {"q": "Yo ___ (llamarse) Valen.", "ans": "me llamo", "hint": "m_ l____", "why": "llamarse is ook reflexief"},
             {"q": "Los niños ___ (dormirse) en el sofá.", "ans": "se duermen", "hint": "s_ d______", "why": "o→ue"},
         ]),
    dict(title="El verbo gustar — ¿gusta o gustan?", accents="strict",
         desc="Bij <i>gustar</i> is het onderwerp niet de persoon maar het <b>ding</b>. Schrijf het "
              "pronombre én de juiste vorm: <i>me gusta el libro</i> · <i>me gustan los libros</i>.",
         items=[
             {"q": "A mí ___ el chocolate.", "ans": "me gusta", "hint": "m_ g____", "why": "één ding → gusta"},
             {"q": "A ti ___ los deportes.", "ans": "te gustan", "hint": "t_ g_____", "why": "meervoud → gustan"},
             {"q": "A Lucía ___ bailar.", "ans": "le gusta", "hint": "l_ g____", "why": "infinitivo telt als enkelvoud"},
             {"q": "A nosotros ___ las películas españolas.", "ans": "nos gustan", "hint": "n__ g_____", "why": "meervoud → gustan"},
             {"q": "A Diego y a Nina ___ la música.", "ans": "les gusta", "hint": "l__ g____", "why": "twee personen → les, maar la música → gusta"},
             {"q": "A mí ___ los libros de aventuras.", "ans": "me gustan", "hint": "m_ g_____", "why": "meervoud → gustan"},
             {"q": "¿___ el español? (a ti)", "ans": "te gusta", "hint": "t_ g____", "why": "el español → gusta"},
             {"q": "A mi hermana ___ los perros.", "ans": "le gustan", "hint": "l_ g_____", "why": "één persoon, meervoud ding"},
             {"q": "A nosotros ___ el fútbol.", "ans": "nos gusta", "hint": "n__ g____", "why": "enkelvoud → gusta"},
             {"q": "A mis padres ___ viajar.", "ans": "les gusta", "hint": "l__ g____", "why": "infinitivo → gusta"},
             {"q": "A ti ___ las matemáticas.", "ans": "te gustan", "hint": "t_ g_____", "why": "meervoud → gustan"},
             {"q": "A mí no ___ madrugar.", "ans": "me gusta", "hint": "m_ g____", "why": "infinitivo → gusta"},
         ]),
    dict(title="La hora — escríbela en letras", accents="soft",
         desc="Schrijf het uur voluit. Eén uur is <b>es la una</b>, alle andere uren zijn "
              "<b>son las…</b> — dat verschil is de hele oefening.",
         items=[
             {"q": "3:00 →", "ans": "Son las tres", "hint": "S__ l__ t___"},
             {"q": "1:00 →", "ans": "Es la una", "hint": "E_ l_ u__", "why": "enkelvoud: es la una"},
             {"q": "3:15 →", "ans": "Son las tres y cuarto", "hint": "S__ l__ t___ y c_____"},
             {"q": "5:30 →", "ans": "Son las cinco y media", "hint": "S__ l__ c____ y m____"},
             {"q": "8:45 →", "ans": "Son las nueve menos cuarto", "hint": "S__ l__ n____ m____ c_____",
              "why": "vanaf 31 minuten reken je terug naar het volgende uur"},
             {"q": "2:10 →", "ans": "Son las dos y diez", "hint": "S__ l__ d__ y d___"},
             {"q": "7:50 →", "ans": "Son las ocho menos diez", "hint": "S__ l__ o___ m____ d___"},
             {"q": "12:00 →", "ans": "Son las doce", "hint": "S__ l__ d___"},
             {"q": "6:20 →", "ans": "Son las seis y veinte", "hint": "S__ l__ s___ y v_____"},
             {"q": "10:40 →", "ans": "Son las once menos veinte", "hint": "S__ l__ o___ m____ v_____"},
             {"q": "1:30 →", "ans": "Es la una y media", "hint": "E_ l_ u__ y m____", "why": "één uur blijft «es la»"},
             {"q": "4:05 →", "ans": "Son las cuatro y cinco", "hint": "S__ l__ c_____ y c____"},
         ]),
]

SETS[("C6+", 2)] = [
    dict(title="¿hay o está(n)? — escribe la forma", accents="strict",
         desc="<b>hay</b> bij iets nieuws of ongeteld (un · dos · mucho) · <b>está / están</b> "
              "bij iets bepaalds (el · la · mi · este). Let op de tilde: <i>está</i> zónder "
              "accent bestaat niet in deze betekenis.",
         items=[
             {"q": "En mi barrio ___ una farmacia.", "ans": "hay", "why": "una → onbepaald → hay"},
             {"q": "La farmacia ___ al lado del banco.", "ans": "está", "why": "la farmacia → bepaald → está (mét tilde)"},
             {"q": "En el salón ___ dos sofás.", "ans": "hay", "why": "dos → geteld → hay"},
             {"q": "Mis libros ___ en la estantería.", "ans": "están", "why": "mis libros, meervoud bepaald → están"},
             {"q": "¿Dónde ___ el supermercado?", "ans": "está", "why": "el supermercado → está"},
             {"q": "Cerca de mi casa ___ un parque muy grande.", "ans": "hay", "why": "un → hay"},
             {"q": "La cocina ___ a la derecha del pasillo.", "ans": "está", "why": "la cocina → está"},
             {"q": "En la plaza ___ mucha gente.", "ans": "hay", "why": "mucha → ongeteld → hay"},
             {"q": "El espejo ___ encima del armario.", "ans": "está", "why": "el espejo → está"},
             {"q": "En mi calle no ___ semáforos.", "ans": "hay", "why": "ontkend onbepaald → hay"},
             {"q": "Las sillas ___ debajo de la mesa.", "ans": "están", "why": "las sillas → están"},
             {"q": "¿Cuántas habitaciones ___ en tu piso?", "ans": "hay", "why": "cuántas → tellen → hay"},
         ]),
    dict(title="Estar + gerundio — ¿qué está pasando?", accents="strict",
         desc="Schrijf <b>allebei</b> de woorden: de vorm van <i>estar</i> én het gerundio. "
              "-ar → <b>-ando</b> · -er/-ir → <b>-iendo</b>. Vier zijn onregelmatig: leyendo, "
              "durmiendo, pidiendo, diciendo.",
         items=[
             {"q": "Mamá ___ (cocinar) en la cocina.", "ans": "está cocinando", "hint": "e___ c________",
              "why": "-ar → -ando"},
             {"q": "Yo ___ (comer) en la terraza.", "ans": "estoy comiendo", "hint": "e____ c_______",
              "why": "-er → -iendo"},
             {"q": "Valen ___ (escribir) un mensaje.", "ans": "está escribiendo", "hint": "e___ e__________",
              "why": "-ir → -iendo"},
             {"q": "Nosotros ___ (ver) la tele en el salón.", "ans": "estamos viendo", "hint": "e______ v_____",
              "why": "ver → viendo"},
             {"q": "Mis hermanos ___ (jugar) en el jardín.", "ans": "están jugando", "hint": "e____ j______",
              "why": "ellos → están"},
             {"q": "¿Qué ___ (hacer) tú?", "ans": "estás haciendo", "hint": "e____ h_______",
              "why": "tú → estás (mét tilde)"},
             {"q": "El abuelo ___ (dormir) en el sofá.", "ans": "está durmiendo", "hint": "e___ d________",
              "why": "onregelmatig: o → u"},
             {"q": "Yo ___ (leer) un libro.", "ans": "estoy leyendo", "hint": "e____ l______",
              "why": "onregelmatig: leer → leyendo"},
             {"q": "Papá ___ (limpiar) el baño.", "ans": "está limpiando", "hint": "e___ l________",
              "why": "-ar → -ando"},
             {"q": "Nosotras ___ (subir) la escalera.", "ans": "estamos subiendo", "hint": "e______ s_______",
              "why": "-ir → -iendo"},
             {"q": "Los vecinos ___ (pedir) silencio.", "ans": "están pidiendo", "hint": "e____ p_______",
              "why": "onregelmatig: e → i"},
             {"q": "¿Vosotros ___ (buscar) la parada?", "ans": "estáis buscando", "hint": "e_____ b_______",
              "why": "vosotros → estáis (mét tilde)"},
         ]),
    dict(title="Los pronombres lo · la · los · las", accents="soft",
         desc="Vervang het <b>lijdend voorwerp</b> door één woordje. Het komt overeen in "
              "geslacht en getal, en het staat <b>vóór</b> het werkwoord — anders dan in het "
              "Nederlands, waar het erachter kan staan.",
         items=[
             {"q": "¿Ves la plaza? — Sí, ___ veo.", "ans": "la", "why": "la plaza → la"},
             {"q": "¿Compras el pan? — Sí, ___ compro.", "ans": "lo", "why": "el pan → lo"},
             {"q": "¿Tienes las llaves? — Sí, ___ tengo.", "ans": "las", "why": "las llaves → las"},
             {"q": "¿Conoces a mis vecinos? — Sí, ___ conozco.", "ans": "los", "why": "mis vecinos (m. mv.) → los"},
             {"q": "¿Dónde pongo el sofá? — ___ pones aquí.", "ans": "lo", "why": "el sofá → lo"},
             {"q": "¿Limpias la cocina hoy? — No, ___ limpio mañana.", "ans": "la", "why": "la cocina → la"},
             {"q": "¿Necesitas los muebles? — No, no ___ necesito.", "ans": "los", "why": "los muebles → los"},
             {"q": "¿Abres las ventanas? — Sí, ___ abro.", "ans": "las", "why": "las ventanas → las"},
             {"q": "¿Buscas la farmacia? — Sí, ___ busco.", "ans": "la", "why": "la farmacia → la"},
             {"q": "¿Coges el autobús? — Sí, ___ cojo en la esquina.", "ans": "lo", "why": "el autobús → lo"},
             {"q": "¿Ordenas tu habitación? — Sí, ___ ordeno los sábados.", "ans": "la", "why": "la habitación → la"},
             {"q": "¿Ves a Valen y a Nina? — Sí, ___ veo en el parque.", "ans": "las", "why": "twee meisjes → las"},
         ]),
]

SETS[("C6+", 7)] = [
    dict(title="El imperativo — da un consejo", accents="strict",
         desc="De <b>tú</b>-vorm van het bevel is meestal de <i>él</i>-vorm van het presente: "
              "<i>come</i>, <i>bebe</i>, <i>recicla</i>. Acht werkwoorden zijn kort en "
              "onregelmatig: <b>ve · haz · pon · ten · sal · di · ven · sé</b>.",
         items=[
             {"q": "___ (comer) más fruta y menos azúcar.", "ans": "Come", "hint": "C___"},
             {"q": "___ (beber) dos litros de agua al día.", "ans": "Bebe", "hint": "B___"},
             {"q": "___ (reciclar) el papel y el plástico.", "ans": "Recicla", "hint": "R______"},
             {"q": "___ (hacer) deporte tres veces por semana.", "ans": "Haz", "hint": "H__",
              "why": "hacer → haz"},
             {"q": "___ (dormir) ocho horas.", "ans": "Duerme", "hint": "D_____", "why": "o → ue"},
             {"q": "___ (apagar) la luz cuando sales.", "ans": "Apaga", "hint": "A____"},
             {"q": "___ (ser) constante: un poco cada día.", "ans": "Sé", "hint": "S_",
              "why": "ser → sé, mét tilde"},
             {"q": "___ (salir) a caminar después de comer.", "ans": "Sal", "hint": "S__",
              "why": "salir → sal"},
             {"q": "___ (decir) que no al estrés.", "ans": "Di", "hint": "D_", "why": "decir → di"},
             {"q": "___ (venir) al instituto en bici.", "ans": "Ven", "hint": "V__",
              "why": "venir → ven"},
             {"q": "___ (proteger) los árboles del barrio.", "ans": "Protege", "hint": "P______"},
             {"q": "___ (evitar) las botellas de plástico.", "ans": "Evita", "hint": "E____"},
         ]),
    dict(title="El imperativo + pronombre — ¡y la tilde!", accents="strict",
         desc="Het pronombre plakt <b>achteraan</b> vast. Daardoor schuift de klemtoon en "
              "moet er vaak een <b>tilde</b> bij: <i>cuida</i> + <i>te</i> → <b>cuídate</b>. "
              "Bij een woord van één lettergreep hoeft het niet: <i>haz</i> + <i>lo</i> → "
              "<b>hazlo</b>.",
         items=[
             {"q": "cuidar + te → ___", "ans": "cuídate", "hint": "c______",
              "why": "esdrújula → tilde"},
             {"q": "mover + te → ___", "ans": "muévete", "hint": "m______",
              "why": "o → ue én esdrújula → tilde"},
             {"q": "reciclar + lo → ___", "ans": "recíclalo", "hint": "r________",
              "why": "sobresdrújula → altijd tilde"},
             {"q": "beber + la (el agua) → ___", "ans": "bébela", "hint": "b_____"},
             {"q": "comer + lo → ___", "ans": "cómelo", "hint": "c_____"},
             {"q": "hacer + lo → ___", "ans": "hazlo", "hint": "h____",
              "why": "haz is één lettergreep → hazlo, llana op klinker, géén tilde"},
             {"q": "decir + me → ___", "ans": "dime", "hint": "d___",
              "why": "di is één lettergreep → dime, géén tilde"},
             {"q": "poner + lo → ___", "ans": "ponlo", "hint": "p____", "why": "pon → ponlo, géén tilde"},
             {"q": "relajar + te → ___", "ans": "relájate", "hint": "r_______"},
             {"q": "lavar + te (las manos) → ___", "ans": "lávate", "hint": "l_____"},
             {"q": "evitar + lo → ___", "ans": "evítalo", "hint": "e______"},
             {"q": "ahorrar + la (el agua) → ___", "ans": "ahórrala", "hint": "a_______"},
         ]),
    dict(title="Los conectores — une tus argumentos", accents="soft",
         desc="Vier verbindingswoorden met elk hun eigen werk: <b>porque</b> geeft de reden · "
              "<b>por eso</b> het gevolg · <b>además</b> voegt toe · <b>sin embargo</b> zet er "
              "iets tegenover. En let op de klassieke valstrik: «dus» is <b>por eso</b> of "
              "<b>así que</b>, nooit <i>luego</i>.",
         items=[
             {"q": "Reciclo ___ quiero cuidar el planeta.", "ans": "porque", "why": "reden → porque"},
             {"q": "No hay autobús; ___ voy en bici.", "ans": "por eso", "why": "gevolg → por eso"},
             {"q": "El deporte es sano. ___, te ayuda a dormir mejor.", "ans": "Además",
              "why": "extra argument → además"},
             {"q": "Comer sano cuesta tiempo. ___, es más barato a la larga.", "ans": "Sin embargo",
              "why": "tegenstelling → sin embargo"},
             {"q": "Bebo mucha agua ___ hace calor.", "ans": "porque"},
             {"q": "Tengo mucho estrés; ___ voy a caminar cada tarde.", "ans": "por eso"},
             {"q": "El plástico contamina. ___, tarda cientos de años en desaparecer.",
              "ans": "Además"},
             {"q": "Me gusta la carne. ___, como menos que antes.", "ans": "Sin embargo"},
             {"q": "Por un lado es cómodo; ___ otro lado, es caro.", "ans": "por",
              "why": "vaste tweeling: por un lado… por otro lado…"},
             {"q": "No fumo ___ es malo para la salud.", "ans": "porque"},
             {"q": "La ciudad tiene mucho tráfico; ___ el aire está contaminado.", "ans": "por eso"},
             {"q": "Apago la luz al salir. ___, desenchufo el cargador.", "ans": "Además"},
         ]),
]

SETS[("C6+", 6)] = [
    dict(title="El imperfecto — cómo era antes", accents="strict",
         desc="De tijd van «vroeger deed ik». <b>-ar</b> → -aba · <b>-er/-ir</b> → -ía. "
              "De -ía-vormen dragen <b>allemaal</b> een tilde. Slechts drie werkwoorden zijn "
              "onregelmatig: ser, ir en ver.",
         items=[
             {"q": "De pequeño yo ___ (jugar) en el patio.", "ans": "jugaba", "hint": "j_____",
              "why": "-ar → -aba"},
             {"q": "Mi abuela ___ (vivir) en un pueblo cerca de Cusco.", "ans": "vivía",
              "hint": "v____", "why": "-ir → -ía, mét tilde"},
             {"q": "Nosotros ___ (ir) a la casa de campo cada verano.", "ans": "íbamos",
              "hint": "í_____", "why": "ir is onregelmatig: iba, ibas… íbamos mét tilde"},
             {"q": "¿Tú ___ (tener) muchos juguetes?", "ans": "tenías", "hint": "t_____"},
             {"q": "Mis primos ___ (ser) mis mejores amigos.", "ans": "eran", "hint": "e___",
              "why": "ser is onregelmatig: era, eras, era, éramos, erais, eran"},
             {"q": "Yo ___ (ver) dibujos animados los sábados.", "ans": "veía", "hint": "v___",
              "why": "ver is onregelmatig: veía"},
             {"q": "En la escuela ___ (haber) un árbol enorme.", "ans": "había", "hint": "h____",
              "why": "hay → había, altijd enkelvoud"},
             {"q": "Nosotras ___ (soler) merendar en casa de la vecina.", "ans": "solíamos",
              "hint": "s_______", "why": "soler + infinitivo = «placht te»"},
             {"q": "Mi maestro siempre ___ (contar) historias.", "ans": "contaba", "hint": "c______",
              "why": "in het imperfecto géén klinkerwissel"},
             {"q": "¿Vosotros ___ (ir) al recreo juntos?", "ans": "ibais", "hint": "i____"},
             {"q": "Yo ___ (ser) muy tímido de pequeño.", "ans": "era", "hint": "e__"},
             {"q": "Mis abuelos ___ (cuidar) a los animales.", "ans": "cuidaban", "hint": "c_______"},
         ]),
    dict(title="Indefinido o imperfecto — ¿qué pasó, cómo era?", accents="strict",
         desc="Twee verledens naast elkaar. <b>Indefinido</b> = wat er gebeurde, één keer, "
              "af. <b>Imperfecto</b> = het decor: hoe het was, wat gewoonte was. Let op de "
              "signaalwoorden: <i>un día · de repente · ayer</i> ↔ <i>siempre · todos los días · "
              "antes</i>.",
         items=[
             {"q": "Todos los días yo ___ (ir) a la escuela a pie.", "ans": "iba", "hint": "i__",
              "why": "todos los días → gewoonte → imperfecto"},
             {"q": "Un día ___ (perder, yo) la mochila en el autobús.", "ans": "perdí", "hint": "p____",
              "why": "un día → één keer → indefinido"},
             {"q": "Antes mi pueblo ___ (ser) muy tranquilo.", "ans": "era", "hint": "e__",
              "why": "antes → decor → imperfecto"},
             {"q": "En 2019 nosotros ___ (mudarse) a la ciudad.", "ans": "nos mudamos",
              "hint": "n__ m______", "why": "jaartal → afgesloten → indefinido"},
             {"q": "De repente ___ (empezar) a llover.", "ans": "empezó", "hint": "e_____",
              "why": "de repente → indefinido"},
             {"q": "Mi abuelo siempre ___ (llevar) sombrero.", "ans": "llevaba", "hint": "l______",
              "why": "siempre → gewoonte → imperfecto"},
             {"q": "Ayer yo ___ (ver) a mi antigua maestra.", "ans": "vi", "hint": "v_",
              "why": "ayer → indefinido"},
             {"q": "Cuando ___ (tener, yo) diez años, vivía en Cusco.", "ans": "tenía", "hint": "t____",
              "why": "leeftijd als decor → imperfecto"},
             {"q": "El año pasado ellos ___ (visitar) Machu Picchu.", "ans": "visitaron",
              "hint": "v________", "why": "el año pasado → indefinido"},
             {"q": "Antes no ___ (haber) internet en el pueblo.", "ans": "había", "hint": "h____",
              "why": "antes → imperfecto"},
             {"q": "Aquella tarde ___ (llegar) una carta.", "ans": "llegó", "hint": "l____",
              "why": "aquella tarde → één moment → indefinido"},
             {"q": "Los domingos mi familia ___ (comer) en casa de los abuelos.", "ans": "comía",
              "hint": "c____", "why": "los domingos → gewoonte → imperfecto"},
         ]),
    dict(title="Comparar — más · menos · tan · mejor", accents="soft",
         desc="Drie bouwsels: <b>más/menos … que</b> (meer/minder dan) · <b>tan … como</b> "
              "(even … als) · en vier woorden die hun eigen vorm hebben: "
              "<b>mejor · peor · mayor · menor</b> — daar zeg je nooit «más bueno».",
         items=[
             {"q": "Cusco es ___ alto ___ Lima.", "ans": "más que", "why": "más + adjectief + que"},
             {"q": "Mi pueblo es ___ grande ___ la ciudad.", "ans": "menos que",
              "why": "menos + adjectief + que"},
             {"q": "Ahora soy ___ alto ___ mi hermano. (even)", "ans": "tan como",
              "why": "tan + adjectief + como"},
             {"q": "Este juguete es ___ que el otro. (beter)", "ans": "mejor",
              "why": "nooit «más bueno»"},
             {"q": "El tiempo de hoy es ___ que el de ayer. (slechter)", "ans": "peor",
              "why": "nooit «más malo»"},
             {"q": "Mi hermana es ___ que yo: tiene veinte años. (ouder)", "ans": "mayor",
              "why": "over leeftijd: mayor, niet «más viejo»"},
             {"q": "Mi primo es ___ que yo: tiene ocho años. (jonger)", "ans": "menor"},
             {"q": "Antes había ___ coches ___ ahora.", "ans": "menos que"},
             {"q": "Esta escuela es ___ antigua ___ la mía. (even)", "ans": "tan como"},
             {"q": "El campo es ___ tranquilo ___ la ciudad.", "ans": "más que"},
             {"q": "Machu Picchu es el lugar ___ visitado del país. (het meest)", "ans": "más",
              "why": "el/la más + adjectief = de -ste"},
             {"q": "Mi abuela cocina ___ que nadie. (beter)", "ans": "mejor"},
         ]),
]

SETS[("C6+", 5)] = [
    dict(title="El pretérito indefinido regular", accents="strict",
         desc="Hier ís het accent de leerstof: <b>hablo</b> (nu, ik) tegenover <b>habló</b> "
              "(toen, hij). De <i>yo</i>- en de <i>él</i>-vorm dragen allebei een tilde — "
              "vergeet je die, dan verandert de betekenis.",
         items=[
             {"q": "Yo ___ (hablar) con ella ayer.", "ans": "hablé", "hint": "h____",
              "why": "-ar · yo → -é, mét tilde"},
             {"q": "Ella ___ (nacer) en Buenos Aires.", "ans": "nació", "hint": "n____",
              "why": "-er · ella → -ió, mét tilde"},
             {"q": "Nosotros ___ (escribir) una carta.", "ans": "escribimos", "hint": "e_________",
              "why": "-ir · nosotros → -imos, zónder tilde"},
             {"q": "¿Tú ___ (estudiar) en Córdoba?", "ans": "estudiaste", "hint": "e_________",
              "why": "-ar · tú → -aste"},
             {"q": "Mis abuelos ___ (mudarse) en 1970.", "ans": "se mudaron", "hint": "s_ m______",
              "why": "reflexief: pronombre vóór het werkwoord"},
             {"q": "Él ___ (ganar) el premio el año pasado.", "ans": "ganó", "hint": "g___",
              "why": "-ar · él → -ó, mét tilde"},
             {"q": "Yo ___ (comer) en su casa.", "ans": "comí", "hint": "c___",
              "why": "-er · yo → -í, mét tilde"},
             {"q": "Ellas ___ (pintar) el mural juntas.", "ans": "pintaron", "hint": "p_______"},
             {"q": "¿Vosotros ___ (vivir) allí mucho tiempo?", "ans": "vivisteis", "hint": "v________",
              "why": "-ir · vosotros → -isteis"},
             {"q": "El escritor ___ (morir) hace dos años.", "ans": "murió", "hint": "m____",
              "why": "morir: o → u in de derde persoon"},
             {"q": "Nosotras ___ (crecer) en el mismo barrio.", "ans": "crecimos", "hint": "c_______"},
             {"q": "Yo ___ (crear) mi primer dibujo a los seis años.", "ans": "creé", "hint": "c___",
              "why": "crear · yo → creé, twee e's en een tilde"},
         ]),
    dict(title="Los pretéritos fuertes — irregulares", accents="strict",
         desc="Negen werkwoorden bouwen hun eigen stam en nemen <b>andere uitgangen</b>. "
              "Het opvallendste: hier staat er <b>géén</b> tilde op de yo- en de él-vorm — "
              "<i>tuve</i>, <i>tuvo</i>, niet <i>tuvé</i>.",
         items=[
             {"q": "Ella ___ (ser) la primera mujer en ganarlo.", "ans": "fue", "hint": "f__",
              "why": "ser en ir hebben dezelfde vorm: fue"},
             {"q": "Yo ___ (tener) mucha suerte.", "ans": "tuve", "hint": "t___",
              "why": "tuve — géén tilde"},
             {"q": "Él ___ (hacer) su mejor obra en Buenos Aires.", "ans": "hizo", "hint": "h___",
              "why": "hacer → hizo, met een z"},
             {"q": "Nosotros ___ (estar) allí dos años.", "ans": "estuvimos", "hint": "e________"},
             {"q": "Ella ___ (decir) la verdad.", "ans": "dijo", "hint": "d___", "why": "decir → dijo"},
             {"q": "Ellos ___ (venir) desde Italia.", "ans": "vinieron", "hint": "v_______"},
             {"q": "Yo no ___ (poder) terminarlo.", "ans": "pude", "hint": "p___", "why": "poder → pude"},
             {"q": "El museo le ___ (dar) un premio.", "ans": "dio", "hint": "d__",
              "why": "dar → dio, géén tilde"},
             {"q": "¿___ (ver) tú la exposición?", "ans": "Viste", "hint": "V____",
              "why": "ver → vi, viste, vio — allemaal zonder tilde"},
             {"q": "Nosotras ___ (ir) al concierto.", "ans": "fuimos", "hint": "f_____",
              "why": "ir en ser: fuimos"},
             {"q": "Ella ___ (poner) su nombre en el cuadro.", "ans": "puso", "hint": "p___"},
             {"q": "Ellos ___ (traer) la música de su país.", "ans": "trajeron", "hint": "t_______",
              "why": "traer → traj- + -eron, zónder i"},
         ]),
    dict(title="Se lo · se la — dos pronombres seguidos", accents="soft",
         desc="Twee voornaamwoorden na elkaar: eerst aan wíe, dan wát. Vóór <i>lo/la/los/las</i> "
              "wordt <b>le</b> en <b>les</b> altijd <b>se</b> — <i>le lo</i> bestaat niet.",
         items=[
             {"q": "¿El libro a María? ___ ___ di ayer.", "ans": "se lo", "why": "le + lo → se lo"},
             {"q": "¿La carta a sus padres? ___ ___ mandó por correo.", "ans": "se la",
              "why": "les + la → se la"},
             {"q": "¿Los cuadros al museo? ___ ___ regaló en 1980.", "ans": "se los",
              "why": "le + los → se los"},
             {"q": "¿Las fotos a nosotros? ___ ___ enseñó anteayer.", "ans": "nos las",
              "why": "aan ons → nos, blijft nos"},
             {"q": "¿El secreto a mí? ___ ___ contó de repente.", "ans": "me lo", "why": "aan mij → me"},
             {"q": "¿La historia a ti? ___ ___ conté yo.", "ans": "te la", "why": "aan jou → te"},
             {"q": "¿El premio a la científica? ___ ___ dieron en Estocolmo.", "ans": "se lo",
              "why": "le + lo → se lo"},
             {"q": "¿Las llaves a sus hermanos? ___ ___ dejó en la mesa.", "ans": "se las",
              "why": "les + las → se las"},
             {"q": "¿La canción a su madre? ___ ___ compuso para su cumpleaños.", "ans": "se la",
              "why": "le + la → se la"},
             {"q": "¿Los apuntes a mí? ___ ___ prestó el lunes.", "ans": "me los", "why": "aan mij → me"},
             {"q": "¿El cuadro a vosotros? ___ ___ vendió barato.", "ans": "os lo", "why": "aan jullie → os"},
             {"q": "¿La verdad a ellos? ___ ___ dijo al final.", "ans": "se la", "why": "les + la → se la"},
         ]),
]

SETS[("C6+", 4)] = [
    dict(title="El pretérito perfecto — haber + participio", accents="strict",
         desc="Schrijf <b>allebei</b> de woorden: de vorm van <i>haber</i> (he · has · ha · "
              "hemos · habéis · han) en het participio. Bij <i>-ar</i> wordt dat <b>-ado</b>, "
              "bij <i>-er</i> en <i>-ir</i> <b>-ido</b>.",
         items=[
             {"q": "Yo ___ (visitar) el desierto de Atacama.", "ans": "he visitado",
              "hint": "h_ v_______", "why": "yo → he + -ado"},
             {"q": "¿Tú ___ (viajar) alguna vez en barco?", "ans": "has viajado",
              "hint": "h__ v______", "why": "tú → has"},
             {"q": "Nina ___ (perder) el tren.", "ans": "ha perdido", "hint": "h_ p______",
              "why": "-er → -ido"},
             {"q": "Nosotros ___ (reservar) dos noches.", "ans": "hemos reservado",
              "hint": "h____ r________", "why": "nosotros → hemos"},
             {"q": "Mis padres ___ (alquilar) un coche.", "ans": "han alquilado",
              "hint": "h__ a________", "why": "ellos → han"},
             {"q": "Yo todavía no ___ (subir) a la montaña.", "ans": "he subido", "hint": "h_ s_____",
              "why": "-ir → -ido"},
             {"q": "¿Vosotros ___ (comer) ya?", "ans": "habéis comido", "hint": "h_____ c_____",
              "why": "vosotros → habéis, mét tilde"},
             {"q": "El vuelo ___ (salir) con retraso.", "ans": "ha salido", "hint": "h_ s_____"},
             {"q": "Yo ___ (sacar) muchas fotos.", "ans": "he sacado", "hint": "h_ s_____"},
             {"q": "Nosotras ___ (quedarse) tres días en Valparaíso.", "ans": "nos hemos quedado",
              "hint": "n__ h____ q______",
              "why": "reflexief: het pronombre komt vóór haber"},
             {"q": "Ellos ___ (probar) el pescado del sur.", "ans": "han probado", "hint": "h__ p______"},
             {"q": "¿___ (estar) tú en Chile alguna vez?", "ans": "Has estado", "hint": "H__ e_____"},
         ]),
    dict(title="Los participios irregulares", accents="strict",
         desc="Acht werkwoorden weigeren de gewone uitgang. Schrijf het <b>participio</b> — "
              "alleen dat woord, niet de hele vorm.",
         items=[
             {"q": "hacer → he ___", "ans": "hecho", "hint": "h____", "why": "hacer → hecho"},
             {"q": "ver → he ___", "ans": "visto", "hint": "v____", "why": "ver → visto"},
             {"q": "escribir → he ___", "ans": "escrito", "hint": "e______", "why": "escribir → escrito"},
             {"q": "volver → he ___", "ans": "vuelto", "hint": "v_____", "why": "volver → vuelto"},
             {"q": "poner → he ___", "ans": "puesto", "hint": "p_____", "why": "poner → puesto"},
             {"q": "decir → he ___", "ans": "dicho", "hint": "d____", "why": "decir → dicho"},
             {"q": "abrir → he ___", "ans": "abierto", "hint": "a______", "why": "abrir → abierto"},
             {"q": "romper → he ___", "ans": "roto", "hint": "r___", "why": "romper → roto"},
             {"q": "comer → he ___", "ans": "comido", "hint": "c_____", "why": "valstrik: comer is regelmatig"},
             {"q": "vivir → he ___", "ans": "vivido", "hint": "v_____", "why": "valstrik: vivir is regelmatig"},
             {"q": "descubrir → he ___", "ans": "descubierto", "hint": "d__________",
              "why": "als abrir → descubierto"},
             {"q": "devolver → he ___", "ans": "devuelto", "hint": "d_______", "why": "als volver → devuelto"},
         ]),
    dict(title="¿por o para? — escribe la preposición", accents="soft",
         desc="Een korte vuistregel: <b>para</b> kijkt vooruit (doel, bestemming, ontvanger, "
              "deadline) · <b>por</b> kijkt naar de weg ernaartoe (reden, ruil, middel, "
              "doorheen, tijdsduur).",
         items=[
             {"q": "Este billete es ___ ti.", "ans": "para", "why": "ontvanger → para"},
             {"q": "Vamos a Santiago ___ avión.", "ans": "por", "why": "middel → por"},
             {"q": "Salimos ___ la montaña mañana.", "ans": "para", "why": "bestemming → para"},
             {"q": "Nos quedamos ___ dos noches.", "ans": "por", "why": "tijdsduur → por"},
             {"q": "Estudio español ___ viajar.", "ans": "para", "why": "doel + infinitivo → para"},
             {"q": "Gracias ___ las fotos.", "ans": "por", "why": "reden/dank → por"},
             {"q": "El tren pasa ___ el desierto.", "ans": "por", "why": "doorheen → por"},
             {"q": "La reserva es ___ el viernes.", "ans": "para", "why": "deadline → para"},
             {"q": "He pagado veinte euros ___ la habitación.", "ans": "por", "why": "ruil/prijs → por"},
             {"q": "Este regalo es ___ mi hermana.", "ans": "para", "why": "ontvanger → para"},
             {"q": "Andamos ___ la playa todas las tardes.", "ans": "por", "why": "doorheen/langs → por"},
             {"q": "¿___ qué has venido a Chile?", "ans": "Por", "why": "«¿por qué?» = waarom — reden"},
         ]),
]

SETS[("C6+", 3)] = [
    dict(title="Ir a + infinitivo — el futuro próximo", accents="strict",
         desc="Schrijf <b>alle drie</b> de stukken: de vorm van <i>ir</i>, het woordje "
              "<b>a</b> en de infinitivo. In het Spaans van deze cursus is dit dé manier om "
              "over morgen te praten — de <i>futuro simple</i> komt hier niet aan te pas.",
         items=[
             {"q": "Mañana yo ___ (subir) una foto nueva.", "ans": "voy a subir", "hint": "v__ a s____",
              "why": "yo → voy a + infinitivo"},
             {"q": "Este fin de semana nosotros ___ (quedar) en el centro.", "ans": "vamos a quedar",
              "hint": "v____ a q_____", "why": "nosotros → vamos a"},
             {"q": "¿Tú ___ (contestar) el mensaje?", "ans": "vas a contestar", "hint": "v__ a c________",
              "why": "tú → vas a"},
             {"q": "Diego ___ (apagar) el móvil a las diez.", "ans": "va a apagar", "hint": "v_ a a_____",
              "why": "él → va a"},
             {"q": "Mis amigos ___ (hacer) una videollamada.", "ans": "van a hacer", "hint": "v__ a h____",
              "why": "ellos → van a"},
             {"q": "Luego yo ___ (descargar) la aplicación.", "ans": "voy a descargar", "hint": "v__ a d________"},
             {"q": "¿Vosotros ___ (publicar) el vídeo?", "ans": "vais a publicar", "hint": "v___ a p_______",
              "why": "vosotros → vais a"},
             {"q": "El próximo mes nosotras ___ (cambiar) de contraseña.", "ans": "vamos a cambiar",
              "hint": "v____ a c______"},
             {"q": "Nina ___ (seguir) a tres cuentas nuevas.", "ans": "va a seguir", "hint": "v_ a s_____"},
             {"q": "Pronto yo ___ (conectarse) a la wifi del instituto.", "ans": "voy a conectarme",
              "hint": "v__ a c_________", "why": "reflexief: het pronombre hangt aan de infinitivo"},
             {"q": "¿Cuándo ___ (llamar) tú a tus abuelos?", "ans": "vas a llamar", "hint": "v__ a l_____"},
             {"q": "Ellos no ___ (compartir) la foto.", "ans": "van a compartir", "hint": "v__ a c________"},
         ]),
    dict(title="Los pronombres le · les — ¿a quién?", accents="soft",
         desc="<b>le</b> = aan één persoon · <b>les</b> = aan meerdere. Het staat <b>vóór</b> het "
              "vervoegde werkwoord. Let op de valstrik: het gaat over aan wíe, niet over wát — "
              "<i>le escribo un mensaje</i> (aan hem/haar).",
         items=[
             {"q": "___ escribo un mensaje a mi hermana.", "ans": "le", "why": "één persoon → le"},
             {"q": "___ mando fotos a mis primos.", "ans": "les", "why": "meerdere → les"},
             {"q": "¿Qué ___ regalas a tu padre?", "ans": "le", "why": "één persoon → le"},
             {"q": "___ contamos la noticia a nuestros amigos.", "ans": "les", "why": "meerdere → les"},
             {"q": "La profesora ___ pregunta la contraseña a Diego.", "ans": "le", "why": "aan Diego → le"},
             {"q": "___ enseño la app a mis abuelos.", "ans": "les", "why": "meerdere → les"},
             {"q": "Nina ___ contesta al mensaje de Valen.", "ans": "le", "why": "aan Valen → le"},
             {"q": "¿___ dices la verdad a tus padres?", "ans": "les", "why": "meerdere → les"},
             {"q": "Yo ___ llamo a mi tía todos los domingos.", "ans": "le", "why": "aan één tante → le"},
             {"q": "El profesor ___ manda los deberes a los alumnos.", "ans": "les", "why": "meerdere → les"},
             {"q": "___ compartimos el vídeo a Mateo.", "ans": "le", "why": "aan Mateo → le"},
             {"q": "¿Por qué no ___ respondes a tus amigas?", "ans": "les", "why": "meerdere → les"},
         ]),
    dict(title="Creo que… · acabar de… — escribe la frase", accents="strict",
         desc="Twee bouwsels naast elkaar. <b>Creo que</b> + de gewóne tijd — nooit iets anders. "
              "<b>Acabar de</b> + infinitivo = «net gedaan hebben»: je vervoegt <i>acabar</i>, "
              "niet het tweede werkwoord.",
         items=[
             {"q": "Creo que las redes ___ (ser) útiles.", "ans": "son", "hint": "s__",
              "why": "creo que + indicativo, gewoon presente"},
             {"q": "Pienso que tú ___ (tener) razón.", "ans": "tienes", "hint": "t_____"},
             {"q": "Me parece que la app no ___ (funcionar).", "ans": "funciona", "hint": "f_______"},
             {"q": "Creo que nosotros ___ (pasar) mucho tiempo en la pantalla.", "ans": "pasamos",
              "hint": "p______"},
             {"q": "Creo que la wifi del instituto ___ (ir) muy lenta.", "ans": "va", "hint": "v_",
              "why": "ir is onregelmatig: ella va"},
             {"q": "Pienso que mis padres ___ (exagerar) un poco.", "ans": "exageran", "hint": "e_______"},
             {"q": "Yo ___ (acabar) de subir la foto.", "ans": "acabo", "hint": "a____",
              "why": "je vervoegt acabar: acabo de subir"},
             {"q": "Diego ___ (acabar) de llamarme.", "ans": "acaba", "hint": "a____"},
             {"q": "Nosotros ___ (acabar) de conectarnos a la wifi.", "ans": "acabamos", "hint": "a_______"},
             {"q": "¿Tú ___ (acabar) de descargar la aplicación?", "ans": "acabas", "hint": "a_____"},
             {"q": "Mis amigas ___ (acabar) de publicar el vídeo.", "ans": "acaban", "hint": "a_____"},
             {"q": "En mi opinión, el móvil ___ (poder) ser adictivo.", "ans": "puede", "hint": "p____",
              "why": "poder: o → ue"},
         ]),
]

SETS[("C6+", 0)] = [
    dict(title="El presente — rellena el verbo", accents="strict",
         desc="De klassieke invuloefening: schrijf het werkwoord tussen haakjes in de juiste vorm "
              "van het <b>presente</b>. Accenten tellen mee.",
         items=[
             {"q": "Yo ___ (hablar) español en clase.", "ans": "hablo", "hint": "h____", "why": "-ar, yo → -o"},
             {"q": "Nosotros ___ (comer) a las dos.", "ans": "comemos", "hint": "c______", "why": "-er, nosotros → -emos"},
             {"q": "Diego ___ (vivir) en México.", "ans": "vive", "hint": "v___", "why": "-ir, él → -e"},
             {"q": "¿Tú ___ (estudiar) francés?", "ans": "estudias", "hint": "e_______", "why": "-ar, tú → -as"},
             {"q": "Ellos ___ (escribir) un mensaje.", "ans": "escriben", "hint": "e_______", "why": "-ir, ellos → -en"},
             {"q": "Yo ___ (ser) de Bélgica.", "ans": "soy", "hint": "s__", "why": "ser is onregelmatig"},
             {"q": "Valen ___ (tener) quince años.", "ans": "tiene", "hint": "t____", "why": "tener: e → ie"},
             {"q": "Nosotros ___ (ir) al instituto.", "ans": "vamos", "hint": "v____", "why": "ir is onregelmatig"},
             {"q": "¿Qué ___ (hacer) tú los sábados?", "ans": "haces", "hint": "h____", "why": "hacer: yo hago, tú haces"},
             {"q": "Mis amigos ___ (venir) a las seis.", "ans": "vienen", "hint": "v_____", "why": "venir: e → ie"},
             {"q": "La profesora ___ (dar) los deberes.", "ans": "da", "hint": "d_", "why": "dar: yo doy, ella da"},
             {"q": "Yo ___ (estar) en casa.", "ans": "estoy", "hint": "e____", "why": "estar is onregelmatig"},
         ]),
    dict(title="¿ser o estar? — escribe la forma", accents="strict",
         desc="Geen keuze tussen twee knoppen: schrijf de <b>vorm</b> zelf. Denk aan wat je zegt — "
              "wie of wat iets ís (ser), of waar en hoe iets ís (estar).",
         items=[
             {"q": "Lucía ___ de Sevilla.", "ans": "es", "why": "herkomst → ser"},
             {"q": "Hoy yo ___ cansado.", "ans": "estoy", "why": "gevoel/toestand → estar"},
             {"q": "Nosotros ___ estudiantes.", "ans": "somos", "why": "identiteit → ser"},
             {"q": "El libro ___ encima de la mesa.", "ans": "está", "why": "plaats → estar (mét tilde)"},
             {"q": "Diego y Nina ___ simpáticos.", "ans": "son", "why": "eigenschap → ser"},
             {"q": "¿Dónde ___ tú?", "ans": "estás", "why": "plaats → estar (mét tilde)"},
             {"q": "Madrid ___ en España.", "ans": "está", "why": "plaats → estar"},
             {"q": "Yo ___ belga.", "ans": "soy", "why": "nationaliteit → ser"},
             {"q": "La ventana ___ abierta.", "ans": "está", "why": "toestand → estar"},
             {"q": "¿Ustedes ___ de Colombia?", "ans": "son", "why": "herkomst → ser"},
             {"q": "Mi madre ___ profesora.", "ans": "es", "why": "beroep → ser"},
             {"q": "Los niños ___ en el parque.", "ans": "están", "why": "plaats → estar (mét tilde)"},
         ]),
    dict(title="Concordancia — escribe la forma correcta", accents="strict",
         desc="Schrijf het woord tussen haakjes in de vorm die <b>overeenkomt</b> met het onderwerp: "
              "mannelijk of vrouwelijk, enkelvoud of meervoud.",
         items=[
             {"q": "Nina es del Perú. Es ___ (peruano).", "ans": "peruana", "hint": "p______", "why": "vrouwelijk enkelvoud"},
             {"q": "Diego es de México. Es ___ (mexicano).", "ans": "mexicano", "hint": "m_______", "why": "mannelijk enkelvoud"},
             {"q": "Lucía y su hermana son ___ (español).", "ans": "españolas", "hint": "e________", "why": "vrouwelijk meervoud"},
             {"q": "Los chicos son ___ (colombiano).", "ans": "colombianos", "hint": "c__________", "why": "mannelijk meervoud"},
             {"q": "La casa es ___ (bonito).", "ans": "bonita", "hint": "b_____", "why": "la casa → -a"},
             {"q": "Los libros son ___ (interesante).", "ans": "interesantes", "hint": "i___________", "why": "-e → alleen +s in het meervoud"},
             {"q": "Mi amiga es ___ (belga).", "ans": "belga", "hint": "b____", "why": "belga verandert niet van vorm"},
             {"q": "Las ciudades son ___ (grande).", "ans": "grandes", "hint": "g______", "why": "-e → +s"},
             {"q": "El profesor es ___ (simpático).", "ans": "simpático", "hint": "s________", "why": "mannelijk enkelvoud, mét tilde"},
             {"q": "Las profesoras son ___ (simpático).", "ans": "simpáticas", "hint": "s_________", "why": "vrouwelijk meervoud, mét tilde"},
             {"q": "Valen es ___ (alto).", "ans": "alta", "hint": "a___", "why": "Valen is een meisje → -a"},
             {"q": "Mis primos son ___ (argentino).", "ans": "argentinos", "hint": "a_________", "why": "mannelijk meervoud"},
         ]),
]


# --------------------------------------------------------------------------- #
def controla():
    """De pista moet bij het antwoord passen.

    Een `hint` is de eerste letter van elk woord plus een liggend streepje per
    ontbrekende letter. Klopt de lengte niet, dan telt de leerling streepjes die
    er niet toe doen en raakt hij het antwoord juist kwijt — dat is erger dan
    géén pista. Laat het hier falen, niet in de klas.
    """
    for (course, unit), sets in SETS.items():
        assert len(sets) == 3, ("%s U%d: %d drills, verwacht 3" % (course, unit, len(sets)))
        for s in sets:
            assert len(s["items"]) == 12, (course, unit, s["title"], len(s["items"]))
            for it in s["items"]:
                h, a = it.get("hint"), it["ans"]
                if not h:
                    continue
                assert len(h) == len(a) and all(
                    c == "_" or c.lower() == d.lower() for c, d in zip(h, a)), (
                    course, unit, s["title"], a, h)


controla()


def heeft(course, unit):
    return (course, unit) in SETS


def js(course, unit, per=12):
    """JS-blok met de getypte grammatica-drills; leeg als de unit nog niet af is."""
    sets = SETS.get((course, unit))
    if not sets:
        return ""
    out = ["function buildGramType(){"]
    for i, s in enumerate(sets[:3], 1):
        out.append(" buildType('gt_%d',{title:%s,desc:%s,accents:'%s',perBlock:%d,expect:%d,items:%s});"
                   % (i, json.dumps(s["title"], ensure_ascii=False),
                      json.dumps(s["desc"], ensure_ascii=False), s.get("accents", "soft"),
                      per, len(s["items"]), json.dumps(s["items"], ensure_ascii=False)))
    out.append("}")
    out.append("buildGramType();")
    return "\n".join(out) + "\n"


def slots(course, unit):
    """Alleen slots plaatsen als er ook inhoud voor is — geen lege kaders."""
    return SLOTS_HTML if heeft(course, unit) else ""


if __name__ == "__main__":
    for (c, u), sets in sorted(SETS.items()):
        n = sum(len(s["items"]) for s in sets)
        print("%-4s U%d  %d drills · %d typvelden  (%s)"
              % (c, u, len(sets), n, " · ".join(s["title"] for s in sets)))
