<!--
FUENTE ÚNICA · C5 (5de jaar · A1-kern) · Unidad 1 «¿Quién eres?»
Content-autoriteit (§2 HANDOVER). Hieruit worden de 4 formaten gevoed:
 · print/PDF  → gen_u1_print.py  → U1.html → C5_U1.pdf
 · HTML-hub   → gen_u1_web.py    → 03-build/web/U1_web.html (18 spellen ingebed)
 · PowerPoint → gen_u1_docente.py→ C5_U1_docente.pptx + C5_U1_alumno.ppsx
 · motor      → spaans-motor/make_u1_games.py → 18 spellen (es-u1-*)
Cursuskleur = groen (#1E9E74). Instructietaal Spaans-eerst met Nederlandse steun.
-->

# C5 · Unidad 1 «¿Quién eres?» — Fuente única 🟢

> **La Ruta — parada 1: Madrid** 🇪🇸 · gastvrouw **Lucía**.
> **Streefniveau:** A1-kern. **Tarea final:** *Mi pasaporte* (communicatief reis-artefact).

## 1 · Per-unit config (§5 HANDOVER)
- **cursus/unit:** C5 (groen) · U1 «¿Quién eres?»
- **parada:** Madrid (España) · **gastheer-cast:** Lucía (Sevilla)
- **tarea final:** *Mi pasaporte* — afzender = jij · ontvanger = de klas/Lucía · doel = jezelf voorstellen · situatie = aankomst in Madrid · resultaat = ingevuld paspoort + gesproken/geschreven voorstelling.

## 2 · Sectiestructuur (vaste §6-volgorde)
`Opener + leeswijzer` → `§0 ¡Ponte al día!` (repaso U0: saludos · deletrear · números) → `§1 Tus datos personales` (woordenschat + presentarse) → `§2 El verbo SER + pronombres` → `§3 El presente regular -ar/-er/-ir` → `§4 Preguntar: interrogativos + género/número + artículos` → `Taller de lengua` (mayúsculas/minúsculas + conectores y/e·o/u·porque) → `Cultura` (Madrid · los dos apellidos · tú/usted) → `Tarea final Mi pasaporte` (5 pasos + rúbrica) → `Repaso` (spiekkaart + semáforo; rest online) → `§V Vocabulario` (tabellen + oefenladder online).

## 3 · Grammatica (alles A1, binnen C5-plafond)
`ser` (irregular) · pronombres personales sujeto · presente regular -ar/-er/-ir · palabras interrogativas · género/número + artículos (el/la/los/las · un/una). Route per blok: context → observeren → patroon → compacte regla → oefenen met steunafbouw → communiceren.

## 4 · Valstrikken voor Nederlandstaligen 🔴
- **Leeftijd = `tener`**, niet `ser`: *Tengo 15 años* (niet ~~soy 15~~). Kernvalstrik.
- **Nationaliteiten/talen met kleine letter**: *belga, español* (landen/steden mét hoofdletter).
- **`¿Cuál?` vs `¿Qué?`** vóór *ser* + gegeven: *¿Cuál es tu nombre?*
- **`el` idioma / `el` día / `el` mapa** (op -a, tóch mannelijk) · **`la` mano** (op -o, vrouwelijk).
- **`e`** i.p.v. *y* vóór i-/hi-: *español e inglés* · **`u`** i.p.v. *o* vóór o-/ho-.
- **want én omdat = `porque`** (één woord!) · «dus» = *así que / por eso*, niet *luego*.
- **`vivir`** = wonen én leven (hier meestal wonen) · **`la dirección`** = adres (false friend).

## 5 · Woordenschat → `u1_vocab.json`
Groepen: `datos` (kern-productief) · `ficha` (receptief formulier) · `interrog` (vraagwoorden) · `saludos` (recyclen U0) · `pais` (álle Spaanstalige landen + gentilicios) · `mundo` (~25 grootste wereldlanden + gentilicios). Curatie landen = beslissing auteur 2026-07-26. Productief klein (eigen wereld + Spanje-focus), rest receptief (kaart/flashcards).

## 6 · LPD-codes (III-Spa-d, afgeleid uit het leerplan)
- **LPD 3** — doelgericht spreken/schrijven met steun (presentarse, ficha, perfil).
- **LPD 4** — doelgericht deelnemen aan mondelinge interactie (kennismaken, vragen stellen).
- **LPD 1 / 2** — onderwerp/hoofdgedachte + relevante info bij lezen/beluisteren (ficha, luisterfragment).
- **LPD 7** — eerder/nieuwverworven woordenschat inzetten (datos, landen).
- **LPD 8** — inzicht in het taalsysteem toepassen (ser, presente, género, interrogativos).
- **LPD 9** — strategieën inzetten (lengua de clase, steunafbouw).
- **LPD 5** — kenmerkende aspecten van de doeltaalcultuur (los dos apellidos, tú/usted, Madrid).

## 7 · Motor-spellen (18 · receptief→productief · 9 speltypes)
`match` país↔nacionalidad · `memory` datos ES↔NL · `memory` bandera↔país · `classify` ser/tener · `classify` ser→persona · `classify` -ar/-er/-ir · `classify` género el/la (generator) · `classify` mayúscula/minúscula · `cloze` interrogativos · `cloze` un/una · `cloze` ¿qué verbo? · `tetris` presente regular (generator) · `tap` sílaba tónica datos · `order` presentación · **`point` caza de mayúsculas** (nieuw component) · **`point` señala el mundo hispano** (nieuw) · `match` pregunta↔respuesta · **`sim` ¡Preséntate!** (nieuw component, vrije productie met bouwsteen-check).
Nieuwe motor-templates gebouwd: `point` (klik-het-doel/foutenjacht) en `sim` (gestuurde/vrije productie). Grammaticale vormen (ser, presente, género) nagerekend/geverifieerd of via generator.

## 8 · Kruisverwijzingen (§16, bindend)
PDF ↔ HTML-hub (QR's → juiste anker) ↔ PowerPoint («zie dia …»). Repaso/inoefenen = online (spellen + zelfcorrectie). Conjugador = aparte cursus-tool (niet in de unit).

## 9 · Build-commando's
```
python3 spaans-motor/make_u1_games.py && (cd spaans-motor && node build.mjs)   # 18 spellen
python3 01-cursussen/05-a1/U1/gen_u1_print.py                                   # U1.html
CHROME --headless --print-to-pdf=03-build/pdf/C5_U1.pdf --no-pdf-header-footer file://.../U1.html
python3 03-build/web/gen_u1_web.py                                              # U1_web.html
(cd 03-build/pptx && python3 gen_u1_docente.py)                                 # 2 decks
```
