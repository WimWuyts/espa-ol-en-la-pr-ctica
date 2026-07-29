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
 1: {  # ── DEMO (U1) — vervang gerust door NotebookLM-output ──
   "tipo": "Chat de WhatsApp · presentaciones",
   "contexto_nl": "Lucía is nieuw op school en chat met Tom.",
   "texto": [
     ["Lucía", "¡Hola! Me llamo Lucía. ¿Cómo te llamas?"],
     ["Tom", "Hola. Yo soy Tom. Encantado."],
     ["Lucía", "Encantada, Tom. ¿Cómo estás?"],
     ["Tom", "Muy bien, gracias. ¿Y tú?"],
     ["Lucía", "Bien también. Soy la nueva estudiante."],
     ["Tom", "¡Bienvenida! Hasta luego, Lucía."],
     ["Lucía", "¡Adiós! Hasta luego."],
   ],
   "global": [
     {"q": "¿Cómo se llama la chica?", "opts": ["Lucía", "Tom", "Ana"], "a": 0},
     {"q": "¿Cómo está Tom?", "opts": ["Muy bien", "Cansado", "Enfermo"], "a": 0},
   ],
   "detalle": [
     {"q": "Tom es la nueva estudiante.", "vf": False},
     {"q": "Lucía dice «encantada».", "vf": True},
     {"q": "Tom dice «¡bienvenida!».", "vf": True},
     {"q": "Lucía está mal.", "vf": False},
   ],
   "transfer": "¿Y tú? ¿Cómo te llamas y cómo estás?",
   "glosario": [["la nueva estudiante", "de nieuwe leerling"], ["¡Bienvenida!", "Welkom!"], ["también", "ook"]],
 },
 2: None,
 3: None,
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
}

def has(unit):
    return bool(LECTURA.get(unit)) or bool(AUDIO.get(unit))

if __name__ == "__main__":
    for u in (1, 2, 3):
        l = "lectura ✓" if LECTURA.get(u) else "lectura —"
        a = "audio ✓" if AUDIO.get(u) else "audio —"
        print(f"U{u}: {l} · {a}")
