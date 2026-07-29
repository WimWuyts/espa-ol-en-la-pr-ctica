# C6+ · «¡Español en la práctica! · vervolg» — versie 1 (compleet) 🟣

De **paarse vervolgcursus** voor de **huidige 6de-jaarcohorte** (D-finaliteit, III-Spa-d). Pikt op waar *Español en la práctica* eindigde en haalt de leerplandoelen + outlines 5 & 6 alsnog binnen. Eindpunt = gelijk aan C6 (A2 → aanzet B1), via een ander vertrekpunt.

**Rode draad — La Ruta:** één doorlopende reis over de Spaanstalige wereld. Elke unit = een nieuwe *parada*.
**España → México → Colombia → Argentina → Perú → Costa Rica** (fin de la ruta).

## De 8 unidades

| Unit | Titel | Parada | Kerngrammatica | Cast |
|---|---|---|---|---|
| **U0** | ¡Volvemos! | el mundo hispano · España | diagnose-repaso (presente, género, getallen) | Lucía |
| **U1** | El día a día | España | reflexieve ww. · ser/estar · gustar + OI | Lucía |
| **U2** | Aquí vivo | Cartagena 🇨🇴 | hay/estar + voorzetsels · OD-pron. (lo/la) | Valen |
| **U3** | Conectados | CDMX 🇲🇽 | ir a + inf. · acabar de · OI-pron. · creo que | Diego |
| **U4** | De viaje | Chile 🇨🇱 | pretérito perfecto compuesto · por/para | (reis) |
| **U5** | Érase una vez | Buenos Aires 🇦🇷 | pretérito indefinido · OD+OI (se lo) | Mateo (voseo) |
| **U6** | Cuando era pequeño | Cusco 🇵🇪 | imperfecto · contraste indef./imperf. · comparativos + que | Nina |
| **U7** | ¡Opina y cuídate! | Costa Rica 🇨🇷 | imperativo (tú) + pronombres · opinar/argumentar + conectores | cast-finale |

**Harde scope-grens (leerplan):** géén futuro simple · géén condicional · géén subjuntivo — ook niet in U7 (imperativo enkel afirmativo tú; mening met indicativo).

## Vier formaten per unit (één bron → 4 formaten)

Elke unit levert, in identieke uitgeverswaardige huisstijl (paars):

1. **Print-PDF** (`C6plus_U<N>.pdf`) — ± 40–50 p, ~28–35 genummerde oefeningen, div-balans 0, elke §/subsectie op een nieuwe bladzijde.
2. **Bewerkbare HTML-laag** (`C6plus_U<N>_BEWERKBAAR.html`) — «Bewerken» · «Opslaan als PDF» · «Bewaar».
3. **HTML-hub** (`C6plus_U<N>_web.html`) — 7 tabbladen, flip cards, visueel-interactieve grammatica, 12 motor-spellen, 100+ zelfcorrigerende oefeningen «↻ otra serie», opname-componenten, klikbare kaart (parada ★), TTS.
4. **PowerPoint ×2** (`_docente.pptx` + `_alumno.pptx`) — 20–21 dia's, klik-onthul-didactiek, 4 vaardigheden, paars (geen groen-lek).

Motor-spellen worden gebouwd uit `spaans-motor/` (8 templates: memory·match·classify·cloze·tetris·order·point·speak).

## Bron & werkwijze (per unit)
1. **Cocktail-receta** (`U<N>_cocktail.md`) — bewuste reservoir-keuze (variatie, `coverage.md`).
2. **Gecureerde vocab** (`u<N>_vocab.json`).
3. Print-generator → HTML → PDF (Chromium) · motor-games · hub (`patch_maps_c6plus.py` bakt de kaart-fiche in) · PowerPoint.
4. **Harde verificatie** (div-balans, bladspiegel, hub-tabs + kaartklik + JS-errors, pptx groen-lek).
5. **coverage.md** bijwerken · **LEESMIJ.md** + **`C6plus_U<N>_ENTREGA.zip`**.

## Regenereren (voorbeeld U<N>)
```
python3 01-cursussen/06-vervolg/U<N>/gen_c6plus_u<N>_print.py         # → PDF (Chromium)
python3 spaans-motor/make_c6plus_u<N>_games.py && node spaans-motor/build.mjs
python3 03-build/web/patch_maps_c6plus.py                            # kaart-fiche (idempotent, U0–U7)
python3 03-build/web/gen_c6plus_u<N>_web.py                          # → 03-build/web/C6plus_U<N>_web.html
python3 03-build/pptx/gen_c6plus_u<N>_docente.py                     # → docente/alumno .pptx
```

## Status
**Versie 1 compleet:** U0–U7 gebouwd, geverifieerd en geleverd (4 formaten). Reservoir-dekking: zie `02-huisstijl/reservoir/coverage.md`. De voor P1–P2 gebouwde onderdelen gaan later rechtstreeks naar de blauwe C6.
