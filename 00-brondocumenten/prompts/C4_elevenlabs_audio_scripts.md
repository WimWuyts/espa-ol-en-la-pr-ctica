# C4 — ElevenLabs-scripts voor de luisterfragmenten (met audio tags)

> **Model:** gebruik **Eleven v3** (alpha) — dat is het model dat de `[audio tags]` interpreteert
> (in v2/Turbo worden ze letterlijk voorgelezen → niet gebruiken). In de UI: «Text to Dialogue» of het
> v3-tekstvak. **Voice:** kies per spreker een **Spaanse of meertalige** stem (anders klinkt het met een
> Engels accent). **Settings voor A1:** Stability ≈ *Natural*, **Speed ≈ 0.9** (rustig, duidelijk).
>
> **Audio tags** die je hier ziet (Engelse descriptors, tussen `[ ]`): `[cheerful]`, `[warmly]`,
> `[friendly]`, `[politely]`, `[a little tired]`, `[a bit nervous]`, `[sweetly]`, `[curious]`,
> `[proud]`, `[pause]`. Hou ze licht — te veel emotie schaadt de A1-verstaanbaarheid.
>
> **Bestandsnaam & plek (BELANGRIJK):** exporteer per unit **één mp3** en noem hem
> `C4_U<n>_audio.mp3`, in map `03-build/web/componentes/audio/`. Dan bedt de pagina hem automatisch in
> (▶ Reproducir + 🐢 Lento + transcript). Bij unit met meerdere dialoogjes: alles in **één** mp3, met de
> `[pause]`-markeringen ertussen.

---

## U1 · «3 personas se presentan»  (3 korte monologen — 3 stemmen)
**Stemmen:** Ana = jonge vrouw · Diego = jonge man · Sofía = jonge vrouw (ander dan Ana).
```
Ana: [cheerful] Hola. Me llamo Ana. Soy estudiante. [happy] Estoy muy bien.
[pause]
Diego: [friendly] Buenos días. Yo soy Diego. Encantado. [a little tired] Estoy un poco cansado.
[pause]
Sofía: [warmly] Hola, me llamo Sofía. ¿Qué tal? Yo estoy bien, gracias.
```

## U2 · «3 mini-diálogos de saludo»  (3 dialoogjes)
**Stemmen:** Ana = jonge vrouw · Marta = vrouw · Luis = jonge man · Sr. López = oudere man ·
Nieta = meisje/jonge vrouw · Abuela = oudere vrouw.
```
Ana: [cheerful] Buenos días, Marta. ¿Qué tal?
Marta: [warmly] Buenos días. Estoy muy bien, gracias. ¿Y tú?
Ana: [friendly] Bien también. ¡Hasta luego!
[pause]
Luis: [politely] Buenas tardes, señor López. ¿Cómo está usted?
Sr. López: [a little tired] Buenas tardes. Estoy un poco cansado, la verdad.
Luis: [kindly] Vaya. ¡Adiós!
[pause]
Nieta: [sweetly] ¡Buenas noches, abuela!
Abuela: [warmly] Buenas noches, cariño. ¿Cómo estás?
Nieta: [a bit nervous] Bien, pero un poco nerviosa. Hasta mañana.
```

## U3 · «entrevista en la calle»  (1 verslaggever + 2 mensen)
**Stemmen:** Reportero = duidelijke stem (m/v) · Chica = jonge vrouw · Chico = jonge man.
```
Reportero: [friendly] ¡Hola! [curious] ¿De dónde eres?
Chica: [cheerful] Hola. Soy de Colombia, de Bogotá.
Reportero: [curious] ¡Qué bien! ¿Y qué idiomas hablas?
Chica: Hablo español y un poco de inglés.
Reportero: [friendly] Gracias. Y tú, ¿de dónde eres?
Chico: [calm] Yo soy de España. Soy español y hablo español y francés.
```

## U4 · «alguien describe a su familia»  (1 monoloog — Pablo)
**Stem:** Pablo = jonge man.
```
Pablo: [warmly] Hola. En mi familia somos cuatro.
[pause]
Pablo: Mi madre se llama Marta. [proud] Es muy amable y un poco elegante.
[pause]
Pablo: Mi padre se llama Jorge. Es alto y muy fuerte.
[pause]
Pablo: [cheerful] Y mi hermano Leo es pequeño, pero muy divertido.
```

## U5 · «una visita a la habitación»  (1 dialoog — Ana toont haar kamer aan Nico)
**Stemmen:** Ana = jonge vrouw · Nico = jonge man.
*(Komt exact overeen met `AUDIO[5]` in `comprension_data.py` → voorwerpen benoemen · hay/no hay · sirve para.)*
```
Ana: [cheerful] Mira, esta es mi habitación.
[pause]
Ana: Aquí hay una cama y una mesa pequeña.
Nico: [curious] ¿Y qué es esto?
Ana: [friendly] Esto es una guitarra. Sirve para tocar música.
Nico: [impressed] ¡Qué bien! ¿Hay un ordenador?
Ana: [calm] No, no hay ordenador, pero hay muchos libros.
```

## U6 · «¿dónde está?»  (1 dialoog — Marta zoekt haar spullen, Pablo helpt)
**Stemmen:** Marta = jonge vrouw · Pablo = jonge man.
*(Komt exact overeen met `AUDIO[6]` in `comprension_data.py` → preposiciones de lugar · hay/está.)*
```
Marta: [a bit stressed] ¿Dónde está mi bolso? No lo encuentro.
Pablo: [helpful] ¿Está en la cocina?
Marta: No, en la cocina no hay nada.
Pablo: [pointing] Mira, está aquí, encima del sofá.
Marta: [relieved] ¡Ah! Y las llaves, ¿dónde están?
Pablo: Debajo de la mesa, al lado de tu libro.
```

## U7 · «una entrevista · ¿en qué trabajas?»  (1 dialoog — Sofía interviewt Óscar)
**Stemmen:** Sofía = jonge vrouw · Óscar = jonge man.
*(Komt exact overeen met `AUDIO[7]` in `comprension_data.py` → profesiones · trabajo en · estoy contento.)*
```
Sofía: [friendly] Hola, Óscar. ¿A qué te dedicas?
Óscar: [relaxed] Soy dependiente. Trabajo en una tienda de música.
Sofía: [impressed] ¡Qué bien! ¿Y estás contento?
Óscar: [cheerful] Sí, estoy muy contento. ¿Y tú? ¿En qué trabajas?
Sofía: Soy estudiante, pero los sábados trabajo en una oficina.
Óscar: [laughing] ¡Trabajamos mucho los dos!
```

## U8 · «quedar por teléfono»  (1 telefoondialoog — Elena & Tomás)
**Stemmen:** Elena = jonge vrouw · Tomás = jonge man.
*(Komt exact overeen met `AUDIO[8]` in `comprension_data.py` → la hora · ¿a qué hora? · quedar.)*
*Tip: zet bij ElevenLabs eventueel een licht «telefoon»-effect op beide stemmen — dat past bij de scène.*
```
Elena: [picking up the phone] ¿Sí? Hola, Tomás.
Tomás: [cheerful] Hola, Elena. ¿Quieres quedar esta tarde?
Elena: Sí, vale. ¿A qué hora?
Tomás: [suggesting] ¿A las seis? ¿O es un poco pronto?
Elena: [thinking] A las seis no puedo. Mejor a las siete y media.
Tomás: [happy] Perfecto. Quedamos en el cine. ¡Hasta luego!
```

---

## Nadat je de mp3's hebt
Zet ze als `C4_U1_audio.mp3` … `C4_U8_audio.mp3` in `03-build/web/componentes/audio/` (of stuur ze mij).
Dan draai ik `gen_c4_comprension.py` + de hubs opnieuw → de audio zit meteen in de «🎧 Escucha»-tab,
met een traag-knop en het transcript. Voor volgende units lever ik telkens hetzelfde: script + tags + stemmen.
