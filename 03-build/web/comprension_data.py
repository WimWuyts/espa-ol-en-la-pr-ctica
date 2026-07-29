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
 2: None,
 3: None,
 4: None,
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
 2: None,
 3: None,
 4: None,
}

def has(unit):
    return bool(LECTURA.get(unit)) or bool(AUDIO.get(unit))

if __name__ == "__main__":
    for u in (1, 2, 3):
        l = "lectura ✓" if LECTURA.get(u) else "lectura —"
        a = "audio ✓" if AUDIO.get(u) else "audio —"
        print(f"U{u}: {l} · {a}")
