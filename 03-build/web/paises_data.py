# -*- coding: utf-8 -*-
# ============================================================================
#  paises_data.py  —  GEDEELDE databron voor de interactieve cultura-kaart
#  (mundo hispano) in ALLE C5-hubs (U0..U8).
#
#  Wat dit levert per land op de kaart = een INFORMATIEFICHE met:
#    • vaste velden (ALTIJD gelijk):  vlag · naam · capital · población ·
#      moneda · gentilicio · idioma(s) · «¿Sabías que…?» (coole weetjes)
#    • één THEMA-feit dat MEEVERANDERT met de unidad (U5=comida, U2=familia,
#      U4=música, U7=lugar/vivienda, U8=viaje, …).
#
#  Eén bron → alle hubs. `patch_maps.py` bakt de per-unit INFO + de render
#  in elke gen_u<N>_web.py; daarna gewoon de hub herbouwen.
# ============================================================================

# ---- 1 · VASTE FICHE per land (identiek op elke kaart) --------------------
#   pob = población (afgerond) · mon = moneda · gen = gentilicio ·
#   idi = idioma(s) · cool = lijst weetjes (personen/architectuur/geschiedenis)
PAISES = {
 "MEX": {"fl":"🇲🇽","n":"México","cap":"Ciudad de México","pob":"~130 mln","mon":"peso mexicano","gen":"mexicano/a","idi":"español (+ náhuatl, maya y 66 lenguas más)",
   "cool":["los aztecas fundaron Tenochtitlan (hoy CDMX) en 1325","Frida Kahlo y Diego Rivera, pintores","pirámides de Teotihuacán y Chichén Itzá (mayas)"]},
 "ESP": {"fl":"🇪🇸","n":"España","cap":"Madrid","pob":"~48 mln","mon":"euro","gen":"español/a","idi":"español (+ catalán, gallego, euskera)",
   "cool":["la Sagrada Familia de Gaudí, aún en obras","la Alhambra de Granada, arquitectura árabe","Picasso, Velázquez y el Prado"]},
 "COL": {"fl":"🇨🇴","n":"Colombia","cap":"Bogotá","pob":"~52 mln","mon":"peso colombiano","gen":"colombiano/a","idi":"español (+ 65 lenguas indígenas)",
   "cool":["Gabriel García Márquez, Nobel del «realismo mágico»","Shakira y Karol G","Cartagena, ciudad amurallada colonial"]},
 "PER": {"fl":"🇵🇪","n":"Perú","cap":"Lima","pob":"~34 mln","mon":"sol","gen":"peruano/a","idi":"español, quechua y aymara",
   "cool":["Machu Picchu, ciudad inca en los Andes","el imperio inca tuvo su capital en Cusco","las misteriosas líneas de Nazca"]},
 "ARG": {"fl":"🇦🇷","n":"Argentina","cap":"Buenos Aires","pob":"~46 mln","mon":"peso argentino","gen":"argentino/a","idi":"español (voseo: «vos tenés»)",
   "cool":["Lionel Messi y Diego Maradona (fútbol)","el tango nació en Buenos Aires","la Patagonia y el glaciar Perito Moreno"]},
 "VEN": {"fl":"🇻🇪","n":"Venezuela","cap":"Caracas","pob":"~28 mln","mon":"bolívar","gen":"venezolano/a","idi":"español (+ lenguas indígenas)",
   "cool":["el Salto Ángel, la cascada más alta del mundo (979 m)","Simón Bolívar, «el Libertador»","tierra de muchas Miss Universo"]},
 "CHL": {"fl":"🇨🇱","n":"Chile","cap":"Santiago","pob":"~20 mln","mon":"peso chileno","gen":"chileno/a","idi":"español (+ mapudungun)",
   "cool":["el desierto de Atacama, el más seco del mundo","Pablo Neruda y Gabriela Mistral, poetas Nobel","la isla de Pascua y sus moáis"]},
 "ECU": {"fl":"🇪🇨","n":"Ecuador","cap":"Quito","pob":"~18 mln","mon":"dólar estadounidense","gen":"ecuatoriano/a","idi":"español y quechua (kichwa)",
   "cool":["las islas Galápagos, donde estudió Darwin","«la mitad del mundo»: la línea del ecuador","Quito, primer Patrimonio de la Humanidad (1978)"]},
 "GTM": {"fl":"🇬🇹","n":"Guatemala","cap":"Ciudad de Guatemala","pob":"~18 mln","mon":"quetzal","gen":"guatemalteco/a","idi":"español (+ 20 lenguas mayas)",
   "cool":["Tikal, gran ciudad maya en la selva","Rigoberta Menchú, Nobel de la Paz","el lago de Atitlán entre volcanes"]},
 "CUB": {"fl":"🇨🇺","n":"Cuba","cap":"La Habana","pob":"~11 mln","mon":"peso cubano","gen":"cubano/a","idi":"español",
   "cool":["La Habana Vieja y sus coches clásicos","cuna del son, la salsa y la rumba","José Martí, héroe nacional"]},
 "BOL": {"fl":"🇧🇴","n":"Bolivia","cap":"Sucre / La Paz","pob":"~12 mln","mon":"boliviano","gen":"boliviano/a","idi":"español, quechua, aymara, guaraní (37 oficiales)",
   "cool":["el Salar de Uyuni, el mayor salar del mundo","el lago Titicaca, el lago navegable más alto","Tiwanaku, cultura anterior a los incas"]},
 "DOM": {"fl":"🇩🇴","n":"República Dominicana","cap":"Santo Domingo","pob":"~11 mln","mon":"peso dominicano","gen":"dominicano/a","idi":"español",
   "cool":["la primera catedral y universidad de América","cuna del merengue y la bachata","Óscar de la Renta, diseñador"]},
 "HND": {"fl":"🇭🇳","n":"Honduras","cap":"Tegucigalpa","pob":"~10 mln","mon":"lempira","gen":"hondureño/a","idi":"español (+ garífuna, miskito)",
   "cool":["Copán, ciudad maya de estelas famosas","las islas de la Bahía, paraíso del buceo","«Honduras» significa «profundidades»"]},
 "PRY": {"fl":"🇵🇾","n":"Paraguay","cap":"Asunción","pob":"~7 mln","mon":"guaraní","gen":"paraguayo/a","idi":"español y guaraní (bilingüe)",
   "cool":["país oficialmente bilingüe (español + guaraní)","la represa de Itaipú, una de las mayores del mundo","las misiones jesuíticas, Patrimonio de la Humanidad"]},
 "NIC": {"fl":"🇳🇮","n":"Nicaragua","cap":"Managua","pob":"~7 mln","mon":"córdoba","gen":"nicaragüense","idi":"español (+ miskito en la costa)",
   "cool":["«tierra de lagos y volcanes»","Rubén Darío, padre del modernismo","la isla de Ometepe, con dos volcanes"]},
 "SLV": {"fl":"🇸🇻","n":"El Salvador","cap":"San Salvador","pob":"~6 mln","mon":"dólar estadounidense","gen":"salvadoreño/a","idi":"español (+ náhuat)",
   "cool":["«el pulgarcito de América»: el más pequeño","las pupusas, plato nacional","playas famosas para el surf en el Pacífico"]},
 "CRI": {"fl":"🇨🇷","n":"Costa Rica","cap":"San José","pob":"~5 mln","mon":"colón","gen":"costarricense","idi":"español",
   "cool":["sin ejército desde 1948","«Pura Vida» y una enorme biodiversidad","líder mundial en energía renovable"]},
 "PAN": {"fl":"🇵🇦","n":"Panamá","cap":"Ciudad de Panamá","pob":"~4 mln","mon":"balboa / dólar","gen":"panameño/a","idi":"español",
   "cool":["el Canal de Panamá une dos océanos","el sombrero «panamá» es en realidad ecuatoriano","el Darién, de gran biodiversidad"]},
 "URY": {"fl":"🇺🇾","n":"Uruguay","cap":"Montevideo","pob":"~3 mln","mon":"peso uruguayo","gen":"uruguayo/a","idi":"español",
   "cool":["José «Pepe» Mujica, expresidente humilde","el mate y las playas de Punta del Este","ganó la primera Copa del Mundo (1930)"]},
 "PRI": {"fl":"🇵🇷","n":"Puerto Rico","cap":"San Juan","pob":"~3 mln","mon":"dólar estadounidense","gen":"puertorriqueño/a","idi":"español e inglés",
   "cool":["Bad Bunny y el reguetón","el Viejo San Juan, colonial y colorido","El Yunque, bosque tropical lluvioso"]},
 "GNQ": {"fl":"🇬🇶","n":"Guinea Ecuatorial","cap":"Malabo","pob":"~1,7 mln","mon":"franco CFA","gen":"ecuatoguineano/a","idi":"español, francés y portugués",
   "cool":["el único país hispanohablante de África","antigua colonia española (hasta 1968)","la isla de Bioko y la selva ecuatorial"]},
 "USA": {"fl":"🇺🇸","n":"Estados Unidos","cap":"Washington D.C.","pob":"~60 mln hispanos","mon":"dólar estadounidense","gen":"estadounidense","idi":"inglés; el español es la 2ª lengua",
   "cool":["~60 mln de hispanos: la 2ª lengua más hablada","Miami, Los Ángeles y Nueva York, muy hispanas","Sonia Sotomayor, jueza del Tribunal Supremo"]},
}

# ---- 2 · THEMA-feit per unidad (verandert mee met de unit) -----------------
#   sleutel = thema-code ; per land één kort feit in dat thema.
TEMAS = {
 "simbolo": {  # U0 · ¡Empezamos! (mundo hispano)
  "MEX":"el águila sobre el nopal, en la bandera","ESP":"el sol y «¡hola!» como saludo","COL":"el cóndor y el grano de café",
  "PER":"el sol inca y la llama","ARG":"el sol de mayo en la bandera","VEN":"las siete estrellas de la bandera",
  "CHL":"la estrella solitaria de la bandera","ECU":"el cóndor de los Andes","GTM":"el quetzal, ave nacional",
  "CUB":"la estrella solitaria y la palma real","BOL":"el cóndor y la bandera wiphala","DOM":"la única bandera del mundo con una Biblia",
  "HND":"las cinco estrellas de Centroamérica","PRY":"la única bandera distinta por cada lado","NIC":"el arco iris en el escudo nacional",
  "SLV":"un volcán en el paisaje nacional","CRI":"«Pura Vida», saludo y lema del país","PAN":"las dos estrellas y el Canal",
  "URY":"el sol de mayo, como Argentina","PRI":"la rana coquí, símbolo de la isla","GNQ":"la única nación hispana de África","USA":"la mezcla de banderas hispanas en las calles"},
 "persona": {  # U1 · ¿Quién eres?
  "MEX":"Frida Kahlo, pintora","ESP":"Rafael Nadal, tenista","COL":"Shakira, cantante","PER":"Mario Vargas Llosa, Nobel de Literatura",
  "ARG":"Lionel Messi, futbolista","VEN":"Simón Bolívar, «el Libertador»","CHL":"Pablo Neruda, poeta Nobel","ECU":"Oswaldo Guayasamín, pintor",
  "GTM":"Rigoberta Menchú, Nobel de la Paz","CUB":"José Martí, poeta y héroe","BOL":"Adela Zamudio, poeta y feminista","DOM":"Juan Luis Guerra, músico",
  "HND":"David Suazo, futbolista","PRY":"José Luis Chilavert, portero legendario","NIC":"Rubén Darío, poeta","SLV":"Óscar Romero, arzobispo y santo",
  "CRI":"Óscar Arias, Nobel de la Paz","PAN":"Rubén Blades, músico y actor","URY":"Luis Suárez, futbolista","PRI":"Roberto Clemente, béisbol",
  "GNQ":"Donato Ndongo, escritor","USA":"Sonia Sotomayor, jueza"},
 "familia": {  # U2 · Mi gente
  "MEX":"a los 15 años se celebra la quinceañera","ESP":"se llevan dos apellidos (padre y madre)","COL":"la familia extensa es muy unida",
  "PER":"muchos apellidos tienen raíces quechuas","ARG":"el domingo es día de asado en familia","VEN":"en Navidad se reúnen con hallacas",
  "CHL":"existe el «Día de la Familia»","ECU":"familias grandes, muchas kichwas","GTM":"las familias mayas transmiten su idioma en casa",
  "CUB":"varias generaciones viven juntas","BOL":"la «cholita» y la pollera, herencia familiar","DOM":"la familia se reúne los domingos con música",
  "HND":"familias numerosas y muy unidas","PRY":"en casa la familia habla guaraní","NIC":"la familia celebra «la Purísima»",
  "SLV":"muchas familias tienen parientes en EE. UU.","CRI":"entre familia y amigos se dice «mae»","PAN":"familias diversas por el Canal (todo el mundo)",
  "URY":"el mate se comparte en familia","PRI":"la familia mezcla lo taíno, africano y español","GNQ":"familias con lenguas fang y bubi en casa","USA":"familias hispanas bilingües (español + inglés)"},
 "rutina": {  # U3 · El tiempo vuela (horarios/ritmo)
  "MEX":"se almuerza fuerte a las 14–15 h","ESP":"se come a las 14 h y se cena a las 21–22 h","COL":"el «tinto» (café) acompaña todo el día",
  "PER":"«la hora peruana»: llegar un poco tarde","ARG":"la cena puede ser a las 22 h","VEN":"un cafecito («guayoyo») a media mañana",
  "CHL":"«las onces», la merienda de la tarde","ECU":"el almuerzo es la comida principal","GTM":"el día empieza temprano, con el sol",
  "CUB":"vida en la calle y música por la tarde","BOL":"en la altura, el ritmo es más pausado","DOM":"la música suena desde temprano",
  "HND":"jornada temprana por el calor","PRY":"siesta al mediodía por el calor","NIC":"vida tranquila: todo está «tuani»",
  "SLV":"pupusas por la noche, en las pupuserías","CRI":"ritmo «pura vida», sin prisa","PAN":"la capital no duerme: ritmo financiero",
  "URY":"el mate acompaña toda la jornada","PRI":"el día acaba con música «plena»","GNQ":"el ritmo tropical marca el día","USA":"horarios tempranos: se cena a las 18–19 h"},
 "musica": {  # U4 · Me gusta (música)
  "MEX":"el mariachi y el corrido","ESP":"el flamenco y el pop de Rosalía","COL":"la cumbia, el vallenato y el reguetón","PER":"el huayno andino y la música criolla",
  "ARG":"el tango y el rock nacional","VEN":"el joropo y la gaita","CHL":"la cueca, baile nacional","ECU":"el pasillo, canción típica",
  "GTM":"la marimba, instrumento nacional","CUB":"el son, la salsa y la rumba","BOL":"música andina con charango y zampoña","DOM":"el merengue y la bachata",
  "HND":"la punta garífuna","PRY":"el arpa paraguaya y la guarania","NIC":"el son nica y la marimba","SLV":"la cumbia y las «xuc»",
  "CRI":"el calypso y la música guanacasteca","PAN":"la salsa de Rubén Blades y el tamborito","URY":"el candombe con tambores","PRI":"el reguetón y la salsa",
  "GNQ":"ritmos africanos y el «malamba»","USA":"el latin pop y el hip-hop en español"},
 "comida": {  # U5 · ¡Ñam!
  "MEX":"los tacos, el guacamole y el mole (base de maíz)","ESP":"la paella, las tapas y la tortilla de patatas","COL":"la arepa, la bandeja paisa y el café",
  "PER":"el ceviche y el lomo saltado (cocina de fama mundial)","ARG":"el asado, las empanadas y el dulce de leche","VEN":"la arepa y el pabellón criollo",
  "CHL":"las empanadas de pino y el pastel de choclo","ECU":"el ceviche de camarón y el encebollado","GTM":"el pepián y los tamales",
  "CUB":"«moros y cristianos» (arroz y frijoles) y la ropa vieja","BOL":"la salteña y el silpancho","DOM":"«la bandera»: arroz, habichuelas y carne",
  "HND":"las baleadas (tortilla con frijoles)","PRY":"la sopa paraguaya y la chipa","NIC":"el gallo pinto y el nacatamal",
  "SLV":"las pupusas, plato nacional","CRI":"el gallo pinto y el «casado»","PAN":"el sancocho y el arroz con pollo",
  "URY":"el asado y el chivito","PRI":"el mofongo y el arroz con gandules","GNQ":"el pescado con yuca y plátano","USA":"la comida tex-mex y los burritos (fusión latina)"},
 "compras": {  # U6 · De tiendas
  "MEX":"los mercados y «tianguis»; se regatea","ESP":"los mercados y las rebajas de enero y julio","COL":"las plazas de mercado y las flores",
  "PER":"los mercados andinos y los textiles","ARG":"las ferias y los productos de cuero","VEN":"los mercados populares y las «buhonerías»",
  "CHL":"la «feria libre» de frutas y verduras","ECU":"el mercado de Otavalo, textiles indígenas","GTM":"el mercado de Chichicastenango, muy colorido",
  "CUB":"el mercado agrícola y los puros","BOL":"el «Mercado de las Brujas» en La Paz","DOM":"los «colmados» de barrio",
  "HND":"los mercados de artesanía","PRY":"el ñandutí, encaje típico","NIC":"las hamacas de Masaya","SLV":"la artesanía de La Palma",
  "CRI":"las carretas pintadas a mano","PAN":"las «molas», textiles del pueblo guna","URY":"la feria de Tristán Narvaja","PRI":"la artesanía y los «vejigantes»",
  "GNQ":"los mercados de pescado y yuca","USA":"los supermercados y las tiendas latinas"},
 "lugar": {  # U7 · Mi casa y mi barrio
  "MEX":"las casas coloridas de Guanajuato","ESP":"los pisos y los patios andaluces","COL":"los balcones floridos de Cartagena","PER":"los barrios coloniales del Cusco",
  "ARG":"el barrio de La Boca, con casas de colores","VEN":"los «ranchos» en las colinas de Caracas","CHL":"las casas de colores de Valparaíso","ECU":"el centro histórico de Quito",
  "GTM":"Antigua, ciudad colonial entre volcanes","CUB":"los edificios coloniales de La Habana Vieja","BOL":"las casas de adobe del Altiplano","DOM":"la Zona Colonial de Santo Domingo",
  "HND":"las casas de madera de las islas","PRY":"las casas con galería y patio","NIC":"Granada, ciudad colonial junto al lago","SLV":"los pueblos de la Ruta de las Flores",
  "CRI":"las casas con jardín, «pura vida»","PAN":"el Casco Viejo de la capital","URY":"la Ciudad Vieja de Montevideo","PRI":"las casas de colores del Viejo San Juan",
  "GNQ":"Malabo y su arquitectura colonial","USA":"barrios latinos como «Little Havana» (Miami)"},
 "clima": {  # C4·U11 · El tiempo y los gustos (¿qué tiempo hace?)
  "MEX":"en la costa hace calor todo el año; en el DF hace fresco por la altura","ESP":"cuatro estaciones: en verano hace mucho calor, en invierno nieva en el norte",
  "COL":"no hay estaciones: cada ciudad tiene «su» clima según la altura","PER":"en la costa casi nunca llueve; Lima vive bajo una niebla gris",
  "ARG":"las estaciones están al revés: en enero hace calor y es verano","VEN":"calor tropical: solo hay «temporada seca» y «temporada de lluvias»",
  "CHL":"del desierto más seco del mundo al hielo de la Patagonia","ECU":"en la mitad del mundo el día dura 12 horas siempre",
  "GTM":"«el país de la eterna primavera»: 20 °C casi todo el año","CUB":"calor y huracanes entre junio y noviembre",
  "BOL":"en La Paz, a 3.600 m, hace frío por la noche todo el año","DOM":"sol y 28 °C casi siempre; llueve fuerte pero poco tiempo",
  "HND":"calor en la costa, fresco en las montañas","PRY":"en verano se pasa de 40 °C; por eso la siesta",
  "NIC":"el país de «lagos y volcanes», con calor húmedo","SLV":"dos estaciones: seca (verano) y lluviosa (invierno)",
  "CRI":"«invierno» significa temporada de lluvias, no frío","PAN":"llueve casi todos los días entre mayo y noviembre",
  "URY":"viento del Atlántico; en julio hace frío y húmedo","PRI":"clima de isla: 27 °C, brisa del mar y huracanes",
  "GNQ":"calor ecuatorial y lluvia casi todo el año","USA":"del frío de Chicago al calor de Miami, en el mismo idioma"},
 "viaje": {  # U8 · ¿Qué has hecho?
  "MEX":"Chichén Itzá y las playas de Cancún","ESP":"la Sagrada Familia y la Alhambra","COL":"Cartagena y el Eje Cafetero","PER":"Machu Picchu, maravilla del mundo",
  "ARG":"las cataratas del Iguazú y la Patagonia","VEN":"el Salto Ángel, la cascada más alta","CHL":"el desierto de Atacama y la isla de Pascua","ECU":"las islas Galápagos",
  "GTM":"Tikal, ciudad maya en la selva","CUB":"La Habana y las playas de Varadero","BOL":"el Salar de Uyuni","DOM":"Punta Cana y sus playas",
  "HND":"las ruinas mayas de Copán","PRY":"las misiones jesuíticas","NIC":"la isla de Ometepe y sus volcanes","SLV":"la Ruta de las Flores y el surf",
  "CRI":"los volcanes y los parques nacionales","PAN":"el Canal de Panamá","URY":"Punta del Este y Colonia del Sacramento","PRI":"el Viejo San Juan y El Yunque",
  "GNQ":"la isla de Bioko y sus playas","USA":"Miami, Los Ángeles y el suroeste hispano"},
}

# ---- 3 · Welke thema-laag hoort bij welke unidad --------------------------
#   (code, label-met-emoji dat vóór het themafeit komt)
UNIT_TEMA = {
 0: ("simbolo", "🌎 Símbolo"),
 1: ("persona", "⭐ Alguien de aquí"),
 2: ("familia", "👪 En familia"),
 3: ("rutina",  "🕐 El ritmo del día"),
 4: ("musica",  "🎵 Música"),
 5: ("comida",  "🍽️ En la mesa"),
 6: ("compras", "🛍️ De compras"),
 7: ("lugar",   "🏙️ Un lugar"),
 8: ("viaje",   "✈️ Para visitar"),
}

# ---- 4 · La Ruta: welke parada is bezocht in welke unidad -----------------
#   code: (start-unit, rango-label, korte NL beschrijving)
PARADAS = {
 "ESP": (0, "U0–U4", "Madrid · Sevilla · Barcelona · València"),
 "MEX": (5, "U5–U6", "CDMX · los mercados (Diego)"),
 "COL": (7, "U7",    "Cartagena (Valen)"),
 "PER": (8, "U8",    "Cusco · Machu Picchu (Nina)"),
}

import json

def _nl_for(code, unit, paradas):
    """La-Ruta-note (NL/ES) voor een parada-land, afhankelijk van de unidad."""
    if code not in paradas:
        return ""
    start, rango, desc = paradas[code]
    if unit < start:
        return ""  # nog niet bezocht
    # huidige parada = grootste start <= unit
    cur = max((c for c,(s,_,_) in paradas.items() if s <= unit), key=lambda c: paradas[c][0])
    if code == cur:
        return f"★ ¡Estás aquí! Parada {rango} · {desc}"
    return f"Parada anterior ({rango}) · {desc}"

def info_block_js(unit, unit_tema=None, paradas=None):
    """Bouw de JS-tekst `const INFO={...};` voor deze unidad (thema meegebakken).

    Meerdere cursussen delen PAISES + TEMAS (landgegevens + themafeiten).
    Elke cursus geeft z'n eigen mapping mee:
      • unit_tema : {unit_nr: (thema_key, "🔖 Label")}  — welke themalaag per unit
                    (thema_key moet in TEMAS bestaan; voeg gerust nieuwe thema's
                     toe aan TEMAS voor cursus-eigen categorieën).
      • paradas   : {code: (start_unit, "rango", "NL-beschrijving")} — de route.
    Zonder argumenten = C5-standaard (UNIT_TEMA / PARADAS hieronder).
    """
    ut = unit_tema if unit_tema is not None else UNIT_TEMA
    pr = paradas   if paradas   is not None else PARADAS
    tema_key, tema_label = ut[unit]
    tmap = TEMAS.get(tema_key, {})
    out = {}
    for code, d in PAISES.items():
        cool = " · ".join(d["cool"])
        tema = tmap.get(code, "")
        tema_full = (tema_label + ": " + tema) if tema else ""
        out[code] = {
            "fl": d["fl"], "n": d["n"], "cap": d["cap"], "pob": d["pob"],
            "mon": d["mon"], "gen": d["gen"], "idi": d["idi"],
            "cool": cool, "tema": tema_full,
            "star": 1 if (code in pr and pr[code][0] <= unit) else 0,
            "nl": _nl_for(code, unit, pr),
        }
    return "const INFO=" + json.dumps(out, ensure_ascii=False) + ";"

# ---- 5 · De render (identiek voor alle units) -----------------------------
#   toont de VOLLEDIGE fiche: koptekst + vaste velden + themafeit + weetjes.
RENDER_JS = (
 "box.innerHTML='<h3>'+d.fl+' '+d.n+' <span style=\"font-size:13px;color:var(--mut);font-weight:400\">('+c+')</span>'+(d.star?' ★':'')+'</h3>'"
 "+'<div class=\"mrow\"><b>🏛️ Capital:</b> '+d.cap+'</div>'"
 "+'<div class=\"mrow\"><b>👥 Población:</b> '+d.pob+'</div>'"
 "+'<div class=\"mrow\"><b>💰 Moneda:</b> '+d.mon+'</div>'"
 "+'<div class=\"mrow\"><b>🗣️ Gentilicio:</b> '+d.gen+'</div>'"
 "+'<div class=\"mrow\"><b>🌐 Idioma:</b> '+d.idi+'</div>'"
 "+(d.tema?'<div style=\"margin-top:8px;padding:8px 11px;background:rgba(255,255,255,.7);border-left:4px solid var(--gd);border-radius:7px;font-weight:600;color:var(--gd)\">'+d.tema+'</div>':'')"
 "+(d.cool?'<div style=\"margin-top:8px;font-size:13px;line-height:1.5\"><b>💡 ¿Sabías que…?</b> '+d.cool+'</div>':'')"
 "+(d.nl?'<div class=\"gloss\" style=\"margin-top:6px\">'+d.nl+'</div>':'');"
)

if __name__ == "__main__":
    # zelftest
    for u in range(9):
        js = info_block_js(u)
        assert js.startswith("const INFO=") and js.endswith(";")
        assert "MEX" in js and "GNQ" in js
    print("paises_data OK ·", len(PAISES), "landen · 9 thema's ·", 9*len(PAISES), "themafeiten")
    print("voorbeeld U5/MEX tema:", TEMAS["comida"]["MEX"])
