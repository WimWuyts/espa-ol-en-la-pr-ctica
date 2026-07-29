# -*- coding: utf-8 -*-
"""Warme, kleurrijke emoji-iconen voor de C5-flashcards (U0–U5).

Vervangt de grijze Lucide-lijniconen op de flashcard-voorkant door één
passende kleur-emoji, in de geest van de Materiales-lessen van de auteur
(bv. 🍳🥔🍅 · eetmomenten 🌅🍽️🍪🌙 · familia 👵👦 · flags voor landen).

Keuzevolgorde in emoji_for(word, grp):
  1) WORD_EMOJI[core]     — genormaliseerd kernwoord (lidwoord/haakjes/pijl weg)
  2) WORD_EMOJI[raw]      — ruwe kleine-letter string (voor vaste chunks)
  3) KEYWORD_EMOJI        — substring-treffer op de ruwe string (kleine, veilige set)
  4) GROUP_EMOJI[grp]     — fallback per vocab-groep → élk woord krijgt iets relevants
  5) DEFAULT (🔤)

Doel: <10% valt terug op DEFAULT.
"""
import re

DEFAULT = "🔤"

# ---------------------------------------------------------------------------
# Landen → vlaggen (U0 «mundo hispano» + U1 pais/mundo). Sleutels genormaliseerd
# (kleine letters, mét accenten; lidwoord weggestript zoals _norm dat doet).
# ---------------------------------------------------------------------------
COUNTRY = {
 "bélgica":"🇧🇪","españa":"🇪🇸","méxico":"🇲🇽","colombia":"🇨🇴","perú":"🇵🇪",
 "argentina":"🇦🇷","chile":"🇨🇱","venezuela":"🇻🇪","ecuador":"🇪🇨","cuba":"🇨🇺",
 "guatemala":"🇬🇹","bolivia":"🇧🇴","honduras":"🇭🇳","paraguay":"🇵🇾",
 "el salvador":"🇸🇻","salvador":"🇸🇻","nicaragua":"🇳🇮","costa rica":"🇨🇷",
 "panamá":"🇵🇦","uruguay":"🇺🇾","república dominicana":"🇩🇴","puerto rico":"🇵🇷",
 "guinea ecuatorial":"🇬🇶","francia":"🇫🇷","alemania":"🇩🇪","países bajos":"🇳🇱",
 "italia":"🇮🇹","portugal":"🇵🇹","reino unido":"🇬🇧","estados unidos":"🇺🇸",
 "canadá":"🇨🇦","brasil":"🇧🇷","marruecos":"🇲🇦","china":"🇨🇳","japón":"🇯🇵",
 "india":"🇮🇳","rusia":"🇷🇺","turquía":"🇹🇷","egipto":"🇪🇬","nigeria":"🇳🇬",
 "sudáfrica":"🇿🇦","australia":"🇦🇺","suecia":"🇸🇪","suiza":"🇨🇭","grecia":"🇬🇷",
 "polonia":"🇵🇱","austria":"🇦🇹","corea del sur":"🇰🇷",
}

# ---------------------------------------------------------------------------
# WORD_EMOJI — per kernwoord één specifieke, herkenbare emoji.
# ---------------------------------------------------------------------------
WORD_EMOJI = {
 # ---- U0 · alfabeto / ortografía ----
 "alfabeto":"🔤","abecedario":"🔤","letra":"🔡","deletrear":"🔤","vocal":"🅰️",
 "consonante":"🅱️","sílaba":"🔉","sílaba tónica":"🔊","tilde":"〰️","acento":"〰️",
 "sombrero":"🎩","aguda":"🔚","llana":"↔️","esdrújula":"⏮️","monosílabo":"1️⃣",
 "mayúscula":"🔠","minúscula":"🔡","diéresis":"👀","dígrafo":"🔗","arroba":"📧",
 "guion":"➖","con tilde":"〰️","con be":"🔤",
 # ---- U0 · números ----
 "10 diez":"🔟","20 veinte":"🔢","30 treinta":"🔢","número":"🔢","contar":"🔢",
 "cero":"0️⃣","cien":"💯","dieciséis":"🔢","treinta y cinco":"🔢",
 "edad":"🎂","tener … años":"🎂","cuántos años tienes":"🎂",
 # ---- U0 · saludos / clase ----
 "hola":"👋","buenos días":"🌅","buenas tardes":"🌇","buenas noches":"🌙",
 "qué tal":"🙂","cómo estás":"🙂","adiós":"👋","hasta luego":"👋","hasta mañana":"👋",
 "chao":"👋","me llamo":"🙋","soy":"🙋","cómo te llamas":"🙋","y tú":"🙋",
 "encantado":"🤝","mucho gusto":"🤝","este es":"👉","soy de":"📍","por favor":"🙏",
 "cómo se dice":"💬","qué significa":"💬","no entiendo":"🤔","puedes repetir":"🔁",
 "más despacio":"🐢","no sé":"🤷","cómo se escribe":"✍️","tengo una pregunta":"🙋",
 # ---- U0 · mundo hispano ----
 "mundo hispano":"🌍","país":"🗺️","lengua":"🗣️","idioma":"🗣️","español":"🇪🇸",
 "castellano":"🇪🇸","hispanohablante":"🗣️","cognado":"🪟","ruta":"🗺️","parada":"🚏",
 # ---- U1 · datos ----
 "nombre":"📛","apellido":"📛","llamarse":"🙋","ser":"🟰","vivir":"🏠",
 "nacionalidad":"🛂","dirección":"📫","correo electrónico":"📧","teléfono":"📱",
 "ciudad":"🏙️","hablar":"🗣️","estudiar":"📚","trabajar":"💼","aprender":"🎓",
 # ---- U1 · ficha ----
 "fecha de nacimiento":"📅","lugar de nacimiento":"📍","código postal":"📮",
 "curso":"🏫","firma":"✍️","rellenar":"📝","documento de identidad":"🪪",
 # ---- U1 · interrogativos ----
 "cómo":"❓","de dónde":"📍","dónde":"📍","cuántos años":"🎂","cuál":"❓",
 "quién":"🙋","qué":"❓","gracias":"🙏",
 # ---- U2 · familia ----
 "familia":"👪","padre":"👨","papá":"👨","madre":"👩","mamá":"👩","padres":"👫",
 "hermano":"👦","hermana":"👧","abuelo":"👴","abuela":"👵","abuelos":"👵",
 "tío":"👨","tía":"👩","primo":"👦","prima":"👧","hijo":"👦","hija":"👧",
 "nieto":"👶","marido":"💑","mascota":"🐶","mayor":"👵","menor":"👶",
 "casado":"💍","soltero":"🙋",
 # ---- U2 · físico ----
 "alto":"📏","bajo":"📏","delgado":"🧍","gordito":"🧍","guapo":"😍","joven":"🧒",
 "moreno":"🧑","rubio":"👱","pelirrojo":"👩‍🦰","pelo":"💇","largo":"📏","corto":"✂️",
 "liso":"💇","rizado":"👩‍🦱","ojos":"👀","barba":"🧔","gafas":"👓",
 # ---- U2 · colores ----
 "marrón":"🟤","negro":"⚫","castaño":"🟤","azul":"🔵","verde":"🟢","gris":"🌫️",
 # ---- U2 · carácter ----
 "simpático":"😊","antipático":"😒","majo":"😊","tímido":"😳","gracioso":"😄",
 "trabajador":"💪","inteligente":"🧠","hablador":"🗣️","tranquilo":"😌","alegre":"😃",
 # ---- U2 · cuerpo ----
 "cabeza":"👤","cara":"😊","nariz":"👃","boca":"👄","mano":"✋",
 # ---- U2 · útil ----
 "este":"👉","ese":"👉","tener":"🤲","estar":"📍","se llama":"🏷️","cuántos":"🔢",
 "también":"➕","pero":"↔️",
 # ---- U3 · hora ----
 "qué hora es":"🕐","hora":"🕐","es la una":"🕐","son las dos":"🕑","y media":"🕧",
 "y cuarto":"🕐","menos cuarto":"🕐","en punto":"⏰","mediodía":"🌞","medianoche":"🌙",
 "de la mañana":"🌅","de la tarde":"🌇","de la noche":"🌙","a qué hora":"⏰",
 "a las":"🕐","reloj":"⏰","temprano":"🌅","tarde":"🌆",
 # ---- U3 · rutina ----
 "rutina":"🔁","despertarse":"⏰","levantarse":"🧍","ducharse":"🚿","lavarse":"🧼",
 "vestirse":"👕","peinarse":"💇","desayunar":"🥐","almorzar":"🍽️","cenar":"🍽️",
 "acostarse":"🛌","hacer los deberes":"📝","ir al instituto":"🏫","descansar":"😴",
 "por la mañana":"🌅","por la tarde":"🌇","por la noche":"🌙",
 # ---- U3 · verbos ----
 "empezar":"▶️","querer":"❤️","preferir":"👍","poder":"💪","dormir":"😴",
 "volver":"🔙","pedir":"🙋","jugar":"🎮","hacer":"🔨","ir":"🚶","salir":"🚪",
 # ---- U3/U4 · frecuencia ----
 "siempre":"♾️","normalmente":"📊","a menudo":"🔁","a veces":"🔀","casi nunca":"🚫",
 "nunca":"⛔","todos los días":"📅","una vez por semana":"📆","fin de semana":"🎉",
 "los fines de semana":"🎉",
 # ---- U3 · tiempo (días/meses/estaciones) ----
 "el lunes":"📅","el martes":"📅","el miércoles":"📅","el jueves":"📅",
 "el viernes":"📅","el sábado":"📅","el domingo":"📅","lunes":"📅","martes":"📅",
 "miércoles":"📅","jueves":"📅","viernes":"📅","sábado":"📅","domingo":"📅",
 "enero":"🗓️","abril":"🗓️","julio":"🗓️","octubre":"🗓️",
 "primavera":"🌸","verano":"☀️","otoño":"🍂","invierno":"❄️","hoy":"📆",
 # ---- U4 · opinar ----
 "gustar":"👍","encantar":"😍","interesar":"🤔","odiar":"😡","me gusta":"👍",
 "tampoco":"🙅","a mí sí":"🙋","por qué":"❓","porque":"❓",
 # ---- U4 · ocio ----
 "deporte":"🏅","fútbol":"⚽","baloncesto":"🏀","nadar":"🏊","bailar":"💃",
 "videojuego":"🎮","leer":"📖","playa":"🏖️","tiempo libre":"🛋️","salir con amigos":"👯",
 # ---- U4 · música ----
 "música":"🎵","canción":"🎶","cantante":"🎤","grupo":"🎸","escuchar música":"🎧",
 "tocar":"🎸","película":"🎬","serie":"📺","cine":"🎥","artista":"🎨","favorito":"⭐",
 # ---- U4 · sentimientos ----
 "divertido":"😄","aburrido":"😑","genial":"😎","interesante":"🤔","emocionante":"😲",
 "relajante":"😌","me pone contento":"😊","me aburre":"😒",
 # ---- U4 · planes ----
 "quedar":"🤝","quieres":"🙋","por qué no":"💡","vale":"👍","plan":"📋",
 # ---- U4 · València ----
 "valència":"🌆","costa":"🏖️","mar":"🌊","paella":"🥘","fallas":"🎆","horchata":"🥛",
 # ---- U5 · comida ----
 "pan":"🍞","huevos":"🥚","queso":"🧀","carne":"🥩","pollo":"🍗","pescado":"🐟",
 "arroz":"🍚","pasta":"🍝","sopa":"🍲","bocadillo":"🥪","jamón":"🍖",
 # ---- U5 · fruta ----
 "manzana":"🍎","plátano":"🍌","naranja":"🍊","fresa":"🍓","uvas":"🍇",
 "limón":"🍋","piña":"🍍",
 # ---- U5 · verdura ----
 "lechuga":"🥬","tomate":"🍅","patata":"🥔","cebolla":"🧅","ajo":"🧄",
 "maíz":"🌽","pimiento":"🫑",
 # ---- U5 · bebida ----
 "agua":"💧","leche":"🥛","zumo":"🧃","café":"☕","té":"🍵","refresco":"🥤",
 # ---- U5 · mesa ----
 "plato":"🍽️","vaso":"🥛","tenedor":"🍴","cuchillo":"🔪","cuchara":"🥄",
 "sal":"🧂","servilleta":"🧻",
 # ---- U5 · restaurante ----
 "carta":"📜","menú":"📋","camarero":"🤵","cuenta":"🧾","propina":"💰",
 "primer plato":"🥗","segundo plato":"🍖","postre":"🍰","reservar":"📅",
 # ---- U5 · cantidades ----
 "mucho":"📈","poco":"📉","un poco de":"🤏","un kilo de":"⚖️",
 "una botella de":"🍾","un paquete de":"📦",
 # ---- U5 · cortesía ----
 "qué va a tomar":"🍽️","me pone":"🙏","para mí":"🙋","me trae":"🤲",
 "que aproveche":"😋","rico":"😋","picante":"🌶️",
 # ---- U5 · méxico ----
 "taco":"🌮","guacamole":"🥑","elote":"🌽","salsa":"🥫","aguacate":"🥑",
 "arepa":"🫓","ceviche":"🦐","churros":"🍩",
}
# vlaggen erin mengen (WORD wint van GROUP)
WORD_EMOJI.update(COUNTRY)

# ---------------------------------------------------------------------------
# KEYWORD_EMOJI — kleine, veilige substring-set (vangt U0-chunks zonder grp).
# ---------------------------------------------------------------------------
KEYWORD_EMOJI = {
 "gracias":"🙏",
 "años":"🎂",
 "se dice":"💬",
 "llam":"🙋",
}

# ---------------------------------------------------------------------------
# GROUP_EMOJI — fallback per vocab-groep → élk woord krijgt iets relevants.
# ---------------------------------------------------------------------------
GROUP_EMOJI = {
 "datos":"📋","ficha":"🪪","interrog":"❓","saludos":"👋","pais":"🏳️","mundo":"🌍",
 "familia":"👪","fisico":"🧑","colores":"🎨","caracter":"😊","cuerpo":"🧑","util":"🔤",
 "hora":"🕐","rutina":"🔁","verbos":"🔤","frecuencia":"📅","tiempo":"🗓️",
 "opinar":"💭","ocio":"🎮","musica":"🎵","sentim":"😀","planes":"📆","valencia":"🏖️",
 "comida":"🍽️","fruta":"🍓","verdura":"🥕","bebida":"🥤","mesa":"🍴",
 "restaurante":"🍽️","cantidades":"⚖️","cortesia":"🙏","mexico":"🌮",
 # ---- C6+·U1 «El día a día» ----
 "calendario":"📅","conectores":"🔗","gustar":"👍","sentimientos":"😊",
 # ---- C6+·U2 «Aquí vivo» ----
 "casa":"🏠","muebles":"🛋️","habitaciones":"🚪","preposiciones":"📍","barrio":"🏙️",
 "ciudad":"🌆","direcciones":"🧭","movimiento":"🚶","lugares":"🏬",
 # ---- C6+·U3 «Conectados» ----
 "dispositivos":"📱","internet":"🌐","digital":"📲","comunicar":"💬","adjmedia":"⭐",
 # ---- C6+·U4 «De viaje» ----
 "transporte":"✈️","alojamiento":"🏨","viaje":"🧳","experiencias":"📸","porpara":"🎯",
 # ---- C6+·U5 «Érase una vez» ----
 "biografia":"👤","logros":"🏆","persona":"🎭","indefinido":"⏳","odoi":"🔁","relato":"📖",
 # ---- C6+·U6 «Cuando era pequeño» ----
 "infancia":"🧸","escuela":"🏫","antesahora":"🔄","comparar":"⚖️","relativo":"🔗",
 # ---- C6+·U7 «¡Opina y cuídate!» ----
 "salud":"💪","consejos":"🥗","medioambiente":"🌍","imperativo":"🗣️",
}

_ARTICLES = ("el ", "la ", "los ", "las ", "un ", "una ", "unos ", "unas ", "mi ", "al ")


def _norm(word):
    """Kernwoord: kleine letters, haakjes/pijl/schuine streep/lidwoord weg."""
    s = (word or "").strip().lower()
    s = re.sub(r"\([^)]*\)", "", s)          # (metáfora…) / (e→ie) weg
    # «el/la cantante», «el/la camarero/a» → dubbel-lidwoord vooraan weg
    s = re.sub(r"^(el|la|los|las|un|una)/(el|la|los|las|un|una)\s+", "", s)
    s = s.replace("«", "|").replace("»", "|")
    for sep in ["→", "/", "·", "|", ",", ";"]:
        if sep in s:
            parts = [p.strip() for p in s.split(sep) if p.strip()]
            if parts:
                s = parts[0]
    s = s.replace("…", "").strip()
    s = s.strip(" ¿?¡!.:·-")
    for art in _ARTICLES:
        if s.startswith(art):
            s = s[len(art):]
            break
    return s.strip()


def emoji_for(word, grp=""):
    """Geef één passende kleur-emoji voor een woord (met optionele groep)."""
    grp = (grp or "").strip()
    if not word:
        return GROUP_EMOJI.get(grp, DEFAULT)
    raw = word.strip().lower()
    core = _norm(word)
    if core in WORD_EMOJI:
        return WORD_EMOJI[core]
    if raw in WORD_EMOJI:
        return WORD_EMOJI[raw]
    for kw, e in KEYWORD_EMOJI.items():
        if kw in raw:
            return e
    if grp in GROUP_EMOJI:
        return GROUP_EMOJI[grp]
    return DEFAULT


# --------------------------------------------------------------------------
# Zelftest / dekkingsrapport:  python3 vocab_emoji.py
# --------------------------------------------------------------------------
if __name__ == "__main__":
    import json, os
    ROOT = "/home/user/espa-ol-en-la-pr-ctica"
    tot_w = tot_word = tot_kw = tot_grp = tot_def = 0
    for u in range(6):
        d = json.load(open(f"{ROOT}/01-cursussen/05-a1/U{u}/u{u}_vocab.json", encoding="utf-8"))
        nw = nword = nkw = ngrp = ndef = 0
        defaults = []
        for v in d:
            es, grp = v.get("es", ""), v.get("grp", "")
            raw = es.strip().lower(); core = _norm(es)
            e = emoji_for(es, grp)
            nw += 1
            if core in WORD_EMOJI or raw in WORD_EMOJI:
                nword += 1
            elif any(kw in raw for kw in KEYWORD_EMOJI):
                nkw += 1
            elif grp in GROUP_EMOJI:
                ngrp += 1
            else:
                ndef += 1; defaults.append(es)
        tot_w += nw; tot_word += nword; tot_kw += nkw; tot_grp += ngrp; tot_def += ndef
        print(f"U{u}: {nw} woorden | WORD {nword} | KEYWORD {nkw} | GROUP {ngrp} | DEFAULT {ndef}")
        if defaults:
            print("     default:", defaults)
    pct = 100.0 * tot_def / tot_w if tot_w else 0
    print(f"TOTAAL: {tot_w} | specifiek(WORD+KEYWORD) {tot_word+tot_kw} | GROUP {tot_grp} | DEFAULT {tot_def} ({pct:.1f}%)")
