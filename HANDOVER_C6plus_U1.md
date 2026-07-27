# OVERGANGSPROMPT — Bouw C6+ · Unidad 1 «El día a día» (IN DEZE CHAT)

> Plak deze prompt in een **verse chat**. Werkbranch = **`claude/spanish-course-c6plus`** (bevat de gelockte U0-golden-sample + alle gedeelde infra). Bouw **U1** exact zoals **U0** gebouwd is. **Alles in deze chat, stap voor stap, zelf** — géén nieuwe chats/sessies/triggers/subagents. Model: **Opus**.

## 0 · Meld je model
Vóór je bouwt: zeg kort dat je **Opus** nodig hebt (Spaanse correctheid + layout-/lege-pagina-controle). Mechanisch nakijken mag op een sneller model.

## 1 · Wat U1 is (uit de C6+-outline)
**U1 «El día a día»** — dagelijks leven, routine, smaken. **Kerngrammatica:** ① **reflexieve werkwoorden** (levantarse, ducharse, llamarse…) · ② **ser vs estar — het contrast** (echte systeem; in U0 enkel soy/estoy diagnostisch) · ③ **gustar + OI** (me/te/le gusta(n)). **P3-seed (mening):** *me gusta… **porque***. U1 = start van de **A2-motor** (bouwt op U0's presente/género/países-basis).
**Leerplan-scope (HARD):** géén futuro simple / condicional / subjuntivo.
**Kleur = paars** (`c6plus`): `--g:#7C56A9 · --gd:#5B3E83 · --gt:#EEE8F5`.

## 2 · Referentie = C6+·U0 (GELOCKT) — kopieer en wissel content
| Formaat | U0-referentie (kopieer → U1, wissel content, behoud alles) |
|---|---|
| Print (PDF + editlaag) | `01-cursussen/06-vervolg/U0/gen_u0_print.py` → `U0.html` → PDF |
| HTML-hub | `03-build/web/gen_c6plus_u0_web.py` → `C6plus_U0_web.html` |
| PowerPoint (2 decks) | `03-build/pptx/gen_c6plus_u0_docente.py` (engine = `gen_u0_docente`, paars-override) |
| Motor-games | `spaans-motor/make_c6plus_u0_games.py` (slug-prefix `es-c6plus-u1-`) |
| Cocktail-receta | `01-cursussen/06-vervolg/U0/U0_cocktail.md` |
Gedeeld & klaar: `02-huisstijl/reservoir/` · `02-huisstijl/templates/cursus-print.css` · `02-huisstijl/beeld/generators/` (cast_gen, vocab_emoji) · `02-huisstijl/fonts/` · `spaans-motor/`.
U1 leeft in `01-cursussen/06-vervolg/U1/`. Output-namen: `C6plus_U1*`.

## 3 · GEBRUIK de oude cursus + het reservoir (BINDEND — de auteur wil dit expliciet)
- **Oude cursus:** `00-brondocumenten/materiales-vorig-project/Unidad_*.pdf`. Voor U1-thema's (routine, reflexieven, gustar, ser/estar) zit relevant materiaal vooral in **Unidad_3 (dagindeling/uur), Unidad_4 (gustos/vrije tijd) en Unidad_2 (estar, descripción)** — extraheer de tekst (`fitz`), **neem relevante oefeningen over** en gebruik de **échte LPD-codes** eruit (niet zelf verzinnen).
- **Reservoir:** instantiëer **echte werkvormen** (WV-/VG-/GT-/SK-…) als concrete oefeningen, niet enkel ID's citeren. Lees vooraf `reservoir_index.md` + `coverage.md`; kies bewust **onder-gebruikte** items; werk `coverage.md` bij met een **C6+·U1-rij**.
- **Cocktail-receta** `01-cursussen/06-vervolg/U1/U1_cocktail.md` schrijven vóór je bouwt.

## 4 · Kwaliteitsregels = het U0-niveau (inclusief de U0-lessen)
- **Werkwoorden/grammatica = de basis → véél inoefening.** Splits de kerngrammatica in **§x.1/§x.2/§x.3** met een echte drillbatterij per deel: cloze · substitutietabel · transformatieketting · matching (subject↔vorm) · foutenkliniek · vraag-antwoord-spiegel · dictado · vrije productie. U0 haalde **44 genummerde oefeningen** — houd dat niveau.
- **Elke paragraaf op een nieuwe bladzijde (BINDEND, auteur):** élke § én subsectie = `<div class="parada sec">` (break-before:page). Zo start geen sectiekop onderaan.
- **Globale oefeningenteller** `AN()` gebruiken (doorlopende nummering zonder gaten).
- **Quota per unit (hard):** ≥1 luisterdialoog · ≥1 rijke Lectura · ≥2 opname-oefeningen · ≥1 traditionele werkwoord-cloze · traditionele oefenbatterij náást de visuele grammatica · HTML-hub **≥100 interactieve oefeningen** met «otra serie» + **10–20 motor-games** (≥8 types) · 4 vaardigheden in print én PowerPoint.
- **Volle antwoordruimte**; nooit oplossingen op de leerlingpagina; geen bouw-jargon (reservoir-ID's) in leerlingtekst; emoji-flashcards; ruta-kaart discreet.

## 5 · VERIFICATIE (BINDEND — dit ging bij U0 mis)
- **Layout/HTML-hygiëne:** controleer **`div-balans == 0`** (open `<div>` = sluit `</div>`). **Let op flex-helpers** zoals `.guide` (`display:flex`): een niet-gesloten div maakt alle volgende blokken flex-kinderen op één rij → kapotte smalle-kolom-layout. Meet dit vóór je oplevert.
- **Print bladspiegel:** meet de vulling per pagina (tekst-max-y) **én kijk** naar de dunste pagina's + een contactblad. Elke paragraaf begint bovenaan (mag deels leeg zijn — dat is de auteurskeuze); geen kapotte/afgesneden tabellen.
- **HTML-hub:** simuleer een **echte klik** op elk subnav-tabblad (of laad via `#hash`), screenshot en **bekijk** elk paneel (geen lege panelen; JS-panelen renderen pas op klik).
- **PowerPoint:** beide `.pptx` openen via `python-pptx` + zip-integriteit; paars toegepast (geen groene cursuskleur-lek; functioneel-groen F_OBJ mag); ≥20 dia's, klik-onthul-animaties, 4 vaardigheden, hyperlink-menu. **Alumno = `.pptx`, nooit `.ppsx`.**

## 6 · Levering & git
- `03-build/*` is deels gitignored → outputs met **`git add -f`**. Gebruik **unieke bestandsnamen** (`gen_c6plus_u1_*`, `C6plus_U1_*`, `make_c6plus_u1_games.py`) zodat je géén U0-/C5-bestanden overschrijft (bij U0 clashte `U0_web.html`/`make_u0_games.py` met C5 — vermijd dat).
- Commit-berichten in het Nederlands; push met exponentiële back-off naar `claude/spanish-course-c6plus`.
- Lever per unit een **zip** met de 4 formaten (PDF + `_BEWERKBAAR.html` · digitale-hub · PowerPoint DOCENTE + ALUMNO) + **LEESMIJ**.

## 7 · Werkvolgorde (samengevat)
1. Modelmelding (Opus). 2. Lees de outline (U1-regel) + de 3 cocktail-documenten + relevante oude-cursus-PDF's. 3. Schrijf `U1_cocktail.md` (reservoir-IDs + oude-cursus-oefeningen + LPD). 4. Cureer `u1_vocab.json` uit de master-pool. 5. Kopieer de U0-generatoren → U1, wissel content. 6. Bouw de 4 formaten, synchroon. 7. **Verifieer hard** (§5). 8. Coverage bijwerken, commit + push, lever de zip. 9. Laat goedkeuren.

> **In één zin:** U1 = U0's pijplijn, U0 als sjabloon, paars, inhoud = **routine/gustos · reflexieven · ser/estar-contrast · gustar+OI · me gusta…porque**, met **veel werkwoord-/grammatica-inoefening** (oude-cursus-oefeningen + reservoir, échte LPD-codes), **elke paragraaf op een nieuwe bladzijde**, div-balans==0, geen lege hub-panelen, werkende `.pptx` — géén futuro/condicional/subjuntivo.
