# C4 — NotebookLM-prompts voor lees- & luisteroefeningen (U1–U3, uitbreidbaar)

> **Doel:** per unit een korte **leestekst** + een kort **luister-script** genereren op **A1/pre-A1**,
> in een **vast format** dat rechtstreeks in `03-build/web/comprension_data.py` past → tab
> «📖 Lee y escucha» + print-blok + (later) PPT-dia's.
>
> **Werkwijze:** open NotebookLM, plak één prompt hieronder, kopieer de output terug (of geef ze aan
> Claude). Voor het **geluid**: het script speelt standaard via browser-TTS in de pagina; wil je
> natuurlijker geluid, spreek het in of gebruik een AI-TTS-mp3 (dan embedden we die).
> **Niveau-regels (altijd):** enkel presente en vaste formules · géén verleden/toekomst/subjuntivo ·
> korte zinnen · enkel de woordenschat van de unit + enkele internationale cognaten.

---

## Vast uitvoerformat (BELANGRIJK — zo plugt het in de pagina)

**Lezen** →
```
TEXTO: [["Spreker of leeg","zin ES"], ...]
CONTEXTO_NL: "één zin Nederlandse situering"
GLOBAL: [{"q":"vraag ES","opts":["a","b","c"],"a":0}]        (2 meerkeuze, globaal begrip)
DETALLE: [{"q":"stelling ES","vf":true}]                      (4 waar/niet-waar)
TRANSFER: "één open ¿y tú?-vraag ES"
GLOSARIO: [["es","nl"]]                                        (max 8 lastige woorden)
```
**Luisteren** →
```
TIPO: "korte omschrijving"
GUION: [["Spreker","zin ES"], ...]
TAREA_NL: "de luistertaak in één zin"
PREGUNTAS: [{"q":"vraag ES","opts":["a","b","c"],"a":0}]      (4 vragen, globaal → detail)
GLOSARIO: [["es","nl"]]
RALLENTADO: ["woord1","woord2","woord3"]                       (traag/duidelijk uit te spreken)
```

---

## UNIDAD 1 · Presentaciones

### 📖 Lezen — WhatsApp-chat
```
Je bent leraar Spaans en maakt leesmateriaal voor Vlaamse tieners (14–16), niveau A1/pre-A1.
Thema: Presentaciones (jezelf voorstellen). Enkel presente/vaste vormen; korte zinnen.
Gebruik UITSLUITEND: Hola · ¿Cómo te llamas? · Me llamo… · (Yo) soy… · Encantado/a · ¿Cómo estás? ·
Bien / Muy bien · Gracias · ¡Bienvenido/a! · Adiós · Hasta luego (+ enkele cognaten).
Schrijf een WhatsApp-chat van 6–8 berichten tussen twee tieners die elkaar leren kennen.
Lever daarna EXACT in het vaste leesformat (TEXTO / CONTEXTO_NL / GLOBAL / DETALLE / TRANSFER / GLOSARIO).
```
### 🎧 Luisteren — 3 personas se presentan
```
Zelfde rol/niveau/regels. Thema: Presentaciones.
Woordenschat: Hola · Buenos días · Me llamo… · Yo soy… · Encantado/a · ¿Qué tal? · Estoy bien /
un poco cansado-a · estudiante · gracias.
Schrijf een KORT luister-script: 3 mensen stellen zich elk in 2 zinnen voor, langzaam en heel eenvoudig.
Pauzes met «…». Lever EXACT in het vaste luisterformat (TIPO / GUION / TAREA_NL / PREGUNTAS / GLOSARIO / RALLENTADO).
```

## UNIDAD 2 · Saludos y cortesía

### 📖 Lezen — muro de notas (3 dagmomenten)
```
Je bent leraar Spaans, materiaal voor Vlaamse tieners (14–16), A1/pre-A1. Enkel presente/vaste vormen.
Thema: Saludos y cortesía. Gebruik UITSLUITEND: Buenos días / Buenas tardes / Buenas noches · ¡Buenas! ·
¿Qué tal? · ¿Cómo estás? · Estoy bien / cansado-a / ocupado-a / nervioso-a · Regular · Por favor ·
Gracias · De nada · Adiós · Hasta luego / Hasta mañana (+ cognaten).
Schrijf 3 korte notas/berichten (elk 2 zinnen) op 3 momenten: mañana, tarde, noche — telkens een groet
+ hoe iemand zich voelt. Lever EXACT in het vaste leesformat.
```
### 🎧 Luisteren — 3 mini-diálogos de saludo
```
Zelfde rol/niveau/regels. Thema: Saludos y cortesía. Woordenschat: idem als hierboven.
Schrijf 3 heel korte dialoogjes (elk 3 beurten) op 3 momenten van de dag: mensen groeten elkaar,
vragen hoe het gaat en nemen afscheid. Langzaam, A1, pauzes met «…».
Lever EXACT in het vaste luisterformat. In PREGUNTAS: minstens één vraag «¿mañana, tarde o noche?»
en één «¿cómo está?».
```

## UNIDAD 3 · Nacionalidades y países

### 📖 Lezen — 3 fichas / foro internacional
```
Je bent leraar Spaans, materiaal voor Vlaamse tieners (14–16), A1/pre-A1. Enkel presente/vaste vormen.
Thema: Nacionalidades y países. Gebruik UITSLUITEND: Me llamo… · Soy de + país (España, México,
Colombia, Argentina, Bélgica…) · Soy español/a · mexicano/a · belga · argentino/a · colombiano/a ·
Hablo español / neerlandés / francés / inglés · un poco · ¿Qué idiomas hablas? (+ cognaten).
Schrijf 3 korte fichas (elk 3 zinnen) van tieners uit verschillende landen (of een kort forobericht per
persoon): naam, land van herkomst, nationaliteit en talen. Lever EXACT in het vaste leesformat.
Zorg dat DETALLE minstens één vraag over gentilicio (♂/♀) en één over idioma bevat.
```
### 🎧 Luisteren — entrevista en la calle
```
Zelfde rol/niveau/regels. Thema: Nacionalidades y países. Woordenschat: idem als hierboven +
números 0–20.
Schrijf een kort «entrevista en la calle»-script (4–5 beurten): een verslaggever vraagt 2 mensen
waar ze vandaan komen en welke talen ze spreken. Langzaam, A1, pauzes met «…».
Lever EXACT in het vaste luisterformat. TAREA_NL = «Vul de tabel in: país · nacionalidad · idioma».
PREGUNTAS: van globaal (¿cuántas personas?) naar detail (¿de dónde es la segunda persona?).
```

---

## Uitbreiden naar U4+
Kopieer een unit-blok, vervang thema + woordenschat (uit de Kit van die unit) + de tekstsoort
(kies telkens een **andere** soort dan de vorige units → variatie). Plak de output in
`comprension_data.py` onder `LECTURA[<unit>]` / `AUDIO[<unit>]`.
