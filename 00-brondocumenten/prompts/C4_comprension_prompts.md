# C4 — NotebookLM-prompts voor lees- & luisteroefeningen (U1–U3, plak-klaar)

> **Gebruik:** open NotebookLM, plak één volledig prompt-blok hieronder, kopieer de JSON-output
> terug (of geef ze aan Claude). Elk blok is **zelfstandig** en vraagt de output in een **vast
> JSON-format** dat rechtstreeks in `03-build/web/comprension_data.py` past (LECTURA/AUDIO).
>
> **Waarom JSON + antwoordsleutels:** de oefeningen op de pagina zijn zelfcorrigerend — daarvoor is
> per vraag het juiste antwoord nodig. Vraag NotebookLM dus altijd om de "a"-index en om V/F-stellingen.
> Krijg je toch losse prose terug? Geen probleem — plak ze bij Claude, die normaliseert ze.

---

## UNIDAD 1 · Presentaciones

### 📖 Lezen — WhatsApp-chat  *(U1-lezen is al ingevuld; gebruik dit enkel om te hergenereren)*
```
Je bent leraar Spaans en maakt leesmateriaal voor Vlaamse tieners (14–16) op niveau A1/pre-A1.
Thema: Presentaciones. Regels: enkel presente en vaste formules; GEEN verleden/toekomst/subjuntivo;
korte zinnen. Gebruik UITSLUITEND deze woordenschat (+ hooguit enkele internationale cognaten):
Hola · ¿Cómo estás? · Bien, gracias · ¿Cómo te llamas? · Me llamo… · (Yo) soy… · ¿De dónde eres? ·
Soy de… (una ciudad) · Encantado/a · Gracias · Adiós · Hasta luego.

Schrijf een WhatsApp-chat van 6–8 berichten tussen twee tieners die elkaar leren kennen.

Antwoord UITSLUITEND met geldige JSON, exact deze sleutels en niets erbuiten. Vragen in het SPAANS.
{
  "TEXTO": [["Spreker","zin ES"]],
  "CONTEXTO_NL": "één zin Nederlandse situering",
  "GLOBAL": [{"q":"vraag ES","opts":["a","b","c"],"a":0}],
  "DETALLE": [{"q":"STELLING ES (bewering, geen vraag)","vf":true}],
  "TRANSFER": "een open ¿y tú?-vraag in het Spaans",
  "GLOSARIO": [["es","nl"]]
}
GLOBAL = precies 2 meerkeuzevragen; "a" = index (0–2) van het juiste antwoord.
DETALLE = precies 4 waar/niet-waar-STELLINGEN met vf:true of vf:false. GLOSARIO = max 8 woorden.
```

### 🎧 Luisteren — 3 personas se presentan
```
Je bent leraar Spaans en maakt luistermateriaal voor Vlaamse tieners (14–16) op niveau A1/pre-A1.
Thema: Presentaciones. Regels: enkel presente/vaste vormen; korte zinnen. Gebruik UITSLUITEND:
Hola · Buenos días · Me llamo… · (Yo) soy… · Encantado/a · ¿Qué tal? · Estoy bien / un poco cansado-a ·
estudiante · gracias (+ cognaten).

Schrijf een KORT luister-script: 3 mensen stellen zich elk in 2 zinnen voor. Langzaam, heel eenvoudig;
korte pauzes met «…».

Antwoord UITSLUITEND met geldige JSON, exact deze sleutels. Vragen in het SPAANS.
{
  "TIPO": "3 personas se presentan",
  "GUION": [["Spreker","zin ES"]],
  "TAREA_NL": "de luistertaak in één zin (NL)",
  "PREGUNTAS": [{"q":"vraag ES","opts":["a","b","c"],"a":0}],
  "GLOSARIO": [["es","nl"]],
  "RALLENTADO": ["woord1","woord2","woord3"]
}
PREGUNTAS = precies 4, van globaal → detail; "a" = index (0–2) van het juiste antwoord.
```

---

## UNIDAD 2 · Saludos y cortesía

### 📖 Lezen — 3 notas/mensajes (mañana · tarde · noche)
```
Je bent leraar Spaans en maakt leesmateriaal voor Vlaamse tieners (14–16) op niveau A1/pre-A1.
Thema: Saludos y cortesía. Regels: enkel presente en vaste formules; GEEN verleden/toekomst; korte zinnen.
Gebruik UITSLUITEND: Buenos días / Buenas tardes / Buenas noches · ¡Buenas! · ¿Qué tal? · ¿Cómo estás? ·
Estoy bien / cansado-a / ocupado-a / nervioso-a · Regular · Por favor · Gracias · De nada ·
Adiós · Hasta luego / Hasta mañana (+ cognaten).

Schrijf 3 korte notas/berichten van elk 2 zinnen, op 3 momenten van de dag (mañana, tarde, noche):
telkens een gepaste groet + hoe iemand zich voelt.

Antwoord UITSLUITEND met geldige JSON, exact deze sleutels en niets erbuiten. Vragen in het SPAANS.
{
  "TEXTO": [["Spreker of \"\"","zin ES"]],
  "CONTEXTO_NL": "één zin Nederlandse situering",
  "GLOBAL": [{"q":"vraag ES","opts":["a","b","c"],"a":0}],
  "DETALLE": [{"q":"STELLING ES (bewering, geen vraag)","vf":true}],
  "TRANSFER": "een open ¿y tú?-vraag in het Spaans",
  "GLOSARIO": [["es","nl"]]
}
GLOBAL = precies 2 meerkeuzevragen; "a" = index van het juiste antwoord.
DETALLE = precies 4 waar/niet-waar-STELLINGEN (vf). Minstens één stelling over het moment van de dag.
GLOSARIO = max 8 woorden.
```

### 🎧 Luisteren — 3 mini-diálogos de saludo
```
Je bent leraar Spaans en maakt luistermateriaal voor Vlaamse tieners (14–16) op niveau A1/pre-A1.
Thema: Saludos y cortesía. Regels: enkel presente/vaste vormen; korte zinnen. Gebruik UITSLUITEND:
Buenos días / Buenas tardes / Buenas noches · ¡Buenas! · ¿Qué tal? · ¿Cómo estás? ·
Estoy bien / cansado-a / ocupado-a · Por favor · Gracias · De nada · Adiós · Hasta luego (+ cognaten).

Schrijf 3 heel korte dialoogjes van elk 3 beurten, op 3 momenten van de dag: mensen groeten elkaar,
vragen hoe het gaat en nemen afscheid. Langzaam, A1; pauzes met «…».

Antwoord UITSLUITEND met geldige JSON, exact deze sleutels. Vragen in het SPAANS.
{
  "TIPO": "3 mini-diálogos de saludo",
  "GUION": [["Spreker","zin ES"]],
  "TAREA_NL": "de luistertaak in één zin (NL)",
  "PREGUNTAS": [{"q":"vraag ES","opts":["a","b","c"],"a":0}],
  "GLOSARIO": [["es","nl"]],
  "RALLENTADO": ["woord1","woord2","woord3"]
}
PREGUNTAS = precies 4; neem minstens één «¿mañana, tarde o noche?» en één «¿cómo está?». "a" = index.
```

---

## UNIDAD 3 · Nacionalidades y países

### 📖 Lezen — 3 fichas van een foro internacional
```
Je bent leraar Spaans en maakt leesmateriaal voor Vlaamse tieners (14–16) op niveau A1/pre-A1.
Thema: Nacionalidades y países. Regels: enkel presente en vaste formules; GEEN verleden/toekomst; korte zinnen.
Gebruik UITSLUITEND: Me llamo… · Soy de + país (España, México, Colombia, Argentina, Bélgica…) ·
Soy español/a · mexicano/a · belga · argentino/a · colombiano/a · Hablo español / neerlandés / francés / inglés ·
un poco · ¿Qué idiomas hablas? (+ cognaten). Schrijf de nationaliteit/taal met KLEINE letter.

Schrijf 3 korte forumberichten (fichas) van elk 3 zinnen: tieners uit verschillende landen stellen zich voor
(naam, land van herkomst, nationaliteit, talen).

Antwoord UITSLUITEND met geldige JSON, exact deze sleutels en niets erbuiten. Vragen in het SPAANS.
{
  "TEXTO": [["Naam of \"\"","zin ES"]],
  "CONTEXTO_NL": "één zin Nederlandse situering",
  "GLOBAL": [{"q":"vraag ES","opts":["a","b","c"],"a":0}],
  "DETALLE": [{"q":"STELLING ES (bewering, geen vraag)","vf":true}],
  "TRANSFER": "een open ¿y tú?-vraag in het Spaans",
  "GLOSARIO": [["es","nl"]]
}
GLOBAL = precies 2 meerkeuzevragen; "a" = index. DETALLE = precies 4 waar/niet-waar-STELLINGEN (vf),
met minstens één over de gentilicio (♂/♀) en één over een idioma. GLOSARIO = max 8 woorden.
```

### 🎧 Luisteren — entrevista en la calle
```
Je bent leraar Spaans en maakt luistermateriaal voor Vlaamse tieners (14–16) op niveau A1/pre-A1.
Thema: Nacionalidades y países. Regels: enkel presente/vaste vormen; korte zinnen. Gebruik UITSLUITEND:
¿De dónde eres? · Soy de + país · Soy español/a · mexicano/a · belga · Hablo español / neerlandés / francés ·
un poco · ¿Qué idiomas hablas? · números 0–20 (+ cognaten).

Schrijf een kort «entrevista en la calle»-script van 4–5 beurten: een verslaggever vraagt 2 mensen
waar ze vandaan komen en welke talen ze spreken. Langzaam, A1; pauzes met «…».

Antwoord UITSLUITEND met geldige JSON, exact deze sleutels. Vragen in het SPAANS.
{
  "TIPO": "entrevista en la calle",
  "GUION": [["Spreker","zin ES"]],
  "TAREA_NL": "Vul de tabel in: país · nacionalidad · idioma",
  "PREGUNTAS": [{"q":"vraag ES","opts":["a","b","c"],"a":0}],
  "GLOSARIO": [["es","nl"]],
  "RALLENTADO": ["woord1","woord2","woord3"]
}
PREGUNTAS = precies 4, van globaal (¿cuántas personas?) → detail (¿de dónde es la segunda persona?). "a" = index.
```

---

## UNIDAD 4 · La familia

### 📖 Lezen — una descripción de una foto de familia
```
Je bent leraar Spaans en maakt leesmateriaal voor Vlaamse tieners (14–16) op niveau A1/pre-A1.
Thema: La familia. Regels: enkel presente en vaste formules; GEEN verleden/toekomst; korte zinnen.
Gebruik UITSLUITEND: mi madre / mi padre · mi hermano/a · mi abuelo/a · el tío / la tía ·
Esta es… / Este es… · Se llama… · es alto/a · bajo/a · guapo/a · delgado/a · simpático/a ·
divertido/a · amable · inteligente · muy… · un poco… · vive en… (+ cognaten). Nationaliteit/adjectief klein.

Schrijf een korte tekst (5–6 zinnen) waarin een tiener een foto van zijn/haar familie beschrijft:
wie het zijn (relación + naam) en hoe ze zijn (1–2 adjectieven per persoon).

Antwoord UITSLUITEND met geldige JSON, exact deze sleutels en niets erbuiten. Vragen in het SPAANS.
{
  "TEXTO": [["\"\"","zin ES"]],
  "CONTEXTO_NL": "één zin Nederlandse situering",
  "GLOBAL": [{"q":"vraag ES","opts":["a","b","c"],"a":0}],
  "DETALLE": [{"q":"STELLING ES (bewering, geen vraag)","vf":true}],
  "TRANSFER": "een open ¿y tú?-vraag in het Spaans (over je eigen familie)",
  "GLOSARIO": [["es","nl"]]
}
GLOBAL = precies 2 MC ("a"=index). DETALLE = precies 4 waar/niet-waar-STELLINGEN (vf), met minstens
één over een familielid (relación) en één over een adjectief. GLOSARIO = max 8 woorden.
```

### 🎧 Luisteren — alguien describe a su familia
```
Je bent leraar Spaans en maakt luistermateriaal voor Vlaamse tieners (14–16) op niveau A1/pre-A1.
Thema: La familia. Regels: enkel presente/vaste vormen; korte zinnen. Gebruik UITSLUITEND:
mi madre / mi padre · mi hermano/a · mi abuela · Se llama… · es alto/a · guapo/a · simpático/a ·
divertido/a · inteligente · amable · muy… · un poco… · vive en… (+ cognaten).

Schrijf een KORT monoloog-script: een tiener beschrijft 3 familieleden (elk 2 zinnen: wie + hoe).
Langzaam, heel eenvoudig; korte pauzes met «…».

Antwoord UITSLUITEND met geldige JSON, exact deze sleutels. Vragen in het SPAANS.
{
  "TIPO": "alguien describe a su familia",
  "GUION": [["Spreker","zin ES"]],
  "TAREA_NL": "Vul de fiche in: wie + hoe is elke persoon?",
  "PREGUNTAS": [{"q":"vraag ES","opts":["a","b","c"],"a":0}],
  "GLOSARIO": [["es","nl"]],
  "RALLENTADO": ["woord1","woord2","woord3"]
}
PREGUNTAS = precies 4, van globaal (¿de cuántas personas habla?) → detail (¿cómo es el/la…?). "a" = index.
```

---

## Uitbreiden naar U4+
Kopieer een unit-blok, vervang thema + woordenschat (uit de Kit van die unit) + de tekstsoort (kies telkens
een **andere** soort dan de vorige units → variatie). Plak de JSON in `comprension_data.py` onder
`LECTURA[<unit>]` / `AUDIO[<unit>]` (of geef ze aan Claude).
