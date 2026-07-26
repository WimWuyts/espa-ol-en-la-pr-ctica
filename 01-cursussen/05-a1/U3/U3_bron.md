<!--
FUENTE ÚNICA · C5 (5de jaar · A1-kern) · Unidad 3 «El tiempo vuela»
Content-autoriteit (§2 HANDOVER). Hieruit worden de 4 formaten gevoed:
 · print/PDF  → gen_u3_print.py  → U3.html → C5_U3.pdf
 · HTML-hub   → gen_u3_web.py    → 03-build/web/U3_web.html (24 spellen ingebed)
 · PowerPoint → gen_u3_docente.py→ C5_U3_docente.pptx + C5_U3_alumno.pptx
 · motor      → spaans-motor/make_u3_games.py → 24 spellen (es-u3-*)
Cursuskleur = groen (#1E9E74). Instructietaal Spaans-eerst met Nederlandse steun.
-->

# C5 · Unidad 3 «El tiempo vuela» — Fuente única 🟢

> **La Ruta — parada 3: Barcelona** 🇪🇸 · gastvrouw **Lucía** + haar Barcelona-vriend **Pau** (catalán).
> **Streefniveau:** A1-kern → eerste A2. **Tarea final:** *Un día en mi vida* (vlog of tekst over je dag).

## 1 · Per-unit config (§5 HANDOVER)
- **cursus/unit:** C5 (groen) · U3 «El tiempo vuela»
- **parada:** Barcelona (España) · **gastheer-cast:** Lucía (Sevilla) + Pau (Barcelona, catalán, enkel in tekst)
- **tarea final:** *Un día en mi vida* — afzender = jij · ontvanger = de klas/Lucía · doel = je dagindeling vertellen · situatie = een dag meelopen in Barcelona · resultaat = vlog/tekst met genummerde pasos + horario.

## 2 · Sectiestructuur (vaste §6-volgorde)
`Opener + leeswijzer` → `§0 ¡Ponte al día!` (repaso U0–U1: números · presente regular · ser/tener) → `§1 La hora` (¿Qué hora es? · y media/cuarto/menos · ¿A qué hora? · de la mañana/tarde/noche) → `§2 Mi rutina + verbos reflexivos` (me/te/se + levantarse, ducharse…) → `§3 Presente irregular con cambio de raíz` (o→ue · e→ie · e→i + hacer/ir/salir) → `§4 Frecuencia + días/meses/estaciones` → `§5 Lectura «El día de Pau»` → `Taller de lengua` (conectores temporales primero/después/luego + ortografía de la hora) → `Cultura` (el horario español vs. België) → `Tarea final Un día en mi vida` (5 pasos + rúbrica) → `Repaso` (spiekkaart + semáforo; rest online) → `§V Vocabulario` (tabellen + oefenladder online).

## 3 · Grammatica (alles A1→eerste A2, binnen C5-plafond; GEEN futuro/condicional/subjuntivo)
`la hora` (ser + las…) · `verbos reflexivos` (me/te/se/nos/os/se) · `presente irregular` cambio de raíz o→ue (poder, dormir, volver, acostarse, almorzar), e→ie (querer, empezar, preferir, despertarse), e→i (pedir, vestirse), u→ue (jugar) + `hacer` (hago) · `ir` (voy) · `salir` (salgo) · `adverbios de frecuencia`. Route per blok: context → observeren → patroon → compacte regla → oefenen met steunafbouw → communiceren.

## 4 · Valstrikken voor Nederlandstaligen 🔴
- **Es la una** (enkelvoud, 1 u) vs. **Son las dos/tres…** (meervoud). Kernvalstrik.
- **Reflexief pronomen vóór het werkwoord:** *me levanto* (niet ~~levanto me~~), *me acuesto*.
- **Stamwissel enkel in de gestreste vorm:** *puedo/puedes/puede/podemos/podéis/pueden* — **nosotros/vosotros NIET** (podemos, dormimos, queremos).
- **jugar → juego** (u→ue, uitzondering).
- **hacer → hago · salir → salgo** (enkel yo onregelmatig).
- **de la mañana/tarde/noche** = bij een concreet uur · **por la mañana/tarde/noche** = een deel van de dag (geen uur).
- **días/meses met kleine letter** (lunes, enero), landen mét hoofdletter — recyclen U1-regel.

## 5 · Woordenschat → `u3_vocab.json`
Groepen: `hora` (klokvocabulaire) · `rutina` (reflexieve dagacties + dagdelen) · `verbos` (onregelmatige presente/stamwissel) · `frecuencia` (frequentiebijwoorden) · `tiempo` (días/meses/estaciones). Productief klein (eigen dag), rest receptief (flashcards/kaart).

## 6 · LPD-codes (III-Spa-d, afgeleid uit het leerplan)
- **LPD 3** — doelgericht spreken/schrijven met steun (mijn dag, horario).
- **LPD 4** — mondelinge interactie (naar tijd/routine vragen, afspreken).
- **LPD 1 / 2** — onderwerp/hoofdgedachte + relevante info (horario, routineprofiel).
- **LPD 7** — woordenschat inzetten (hora, rutina, frecuencia, tiempo).
- **LPD 8** — taalsysteem (la hora, reflexivos, presente irregular).
- **LPD 9** — strategieën (steunafbouw, lengua de clase).
- **LPD 5** — doeltaalcultuur (el horario español, las comidas, la siesta).

## 7 · Motor-spellen (24 · receptief→productief · 10 speltypes)
`match` hora↔reloj · `memory` rutina ES↔NL · `memory` verbo↔betekenis · `classify` reflexivo/no-reflexivo · `classify` cambio de raíz (ie/ue/i) · `classify` de/por · `classify` día vs mes · `cloze` la hora · `cloze` verbo reflexivo · `cloze` presente irregular · `cloze` frecuencia · `tetris` presente irregular (generator, stamwissel) · `tap` sílaba tónica rutina · `order` mi rutina · `order` mi día · `point` caza del reflexivo · `point` señala la mañana · `sim` describe tu día · `speak` escucha y repite la hora · `speak` shadowing rutina · `speak` carrusel: mi día · `speak` mensaje de voz · `speak` describe la rutina de Pau. Grammaticale vormen (presente irregular) nagerekend via de motor-generator (`verbo`, classes ie/ue/i/uue).

## 8 · Kruisverwijzingen (§16, bindend)
PDF ↔ HTML-hub (QR's → juiste anker) ↔ PowerPoint («zie dia …»). Repaso/inoefenen = online. Conjugador = aparte cursus-tool (niet in de unit).

## 9 · Build-commando's
```
python3 spaans-motor/make_u3_games.py && (cd spaans-motor && node build.mjs)   # 24 spellen
python3 01-cursussen/05-a1/U3/gen_u3_print.py                                   # U3.html
CHROME --headless --print-to-pdf=03-build/pdf/C5_U3.pdf --no-pdf-header-footer file://.../U3.html
python3 03-build/web/gen_u3_web.py                                              # U3_web.html
(cd 03-build/pptx && python3 gen_u3_docente.py)                                 # 2 decks
```
