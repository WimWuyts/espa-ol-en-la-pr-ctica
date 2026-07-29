# HANDOVER — Bouw C6+ (6de jaar · vervolg · PAARS) EXACT zoals C5

> **Doel:** één verse chat moet hiermee de **volledige cursus C6+** kunnen bouwen, **identiek qua proces en kwaliteit** aan de C5-cursus in deze repo. C6+ leeft in **dezelfde monorepo** (`01-cursussen/06-vervolg/`) en **hergebruikt alle gedeelde infrastructuur** — enkel de **cursuskleur (paars)** en de **content** verschillen.
>
> **Verhouding wát ↔ hóé:** dit document legt het **HÓÉ** vast (proces, pijplijn, cocktail-aanpak, kwaliteitsregels). Het **WÁT** — de gap-analyse, welke hiaten je invult, het unit-plan van C6+ — **is in de C6+-chat beslist**; neem dat plan daar over. Deze handover dicteert de inhoud niet, ze zorgt dat je die inhoud op exact dezelfde manier bouwt als C5.
>
> **Lees óók `CLAUDE.md`** (projectgeheugen, automatisch ingeladen) — bevat álle bindende specs (§13–§18, §14ter reservoir/cocktail).

---

## 0 · DE ALLEREERSTE REGEL — meld welk model je nodig hebt

**Bindend, elke bouwstap:** vóór je iets bouwt, **vertel de gebruiker expliciet welk model je nodig hebt** en waarom. Hij zet het model dan goed (hij werkt standaard op **Opus**).

| Taak | Model | Waarom |
|---|---|---|
| **Unit bouwen** (print/hub/pptx/games volgens het U5-sjabloon) | **Opus** (of Sonnet als werkpaard bij kostbewaking) | correctheid Spaans + valstrikken + lege-pagina-controle tellen |
| **Gap-analyse / batch print+pptx over meerdere units** | **Opus + ultracode** (Workflow-tool) | deterministische fan-out + adversariële verificatie |
| **Brede mechanische verificatie** (tellingen, cross-format, coverage) | **Fable** | snel & goedkoop, hoog volume |
| **Zwaarste redenering** (leerplan/didactiek, gap-analyse-oordelen) | **Opus** | diepste redeneren |

Zeg het telkens: *«Voor deze [gap-analyse / unit-build / audit / workflow] heb ik **[model]** nodig — zet je me daarop? (ultracode aan/uit)».* Nooit stil beginnen zonder de modelmelding.

---

## 1 · Wat C6+ is (kader)

- **C6+ «Vervolg op *Español en la práctica*», 6de jaar, huidige cohorte, kleur PAARS.** De **moeilijkste** cursus: geen schone start maar een **vervolg** dat **hiaten invult** en zoveel mogelijk van **outlines 5 én 6** alsnog binnenhaalt.
- **Eindpunt = gelijk aan C6** (A2 → aanzet B1), maar via een **ander vertrekpunt** (waar *Español en la práctica* eindigde).
- **Werkwijze (uit CLAUDE.md §3):** (1) *Español en la práctica* **analyseren** → (2) **gap-analyse** t.o.v. leerplan + outlines 5 & 6 → (3) cursus bouwen die de hiaten invult/inoefent. **Deze stappen + het resulterende unit-plan zijn in de C6+-chat beslist — volg dat plan.**
- **Bronnen:** oude cursus in `00-brondocumenten/espanol-en-la-practica/`; gap-analyse in `00-brondocumenten/gap-analyse/`; outlines in `00-brondocumenten/outlines/` (jaar 5 én 6).
- **Leerplan-scope (HARD, zelfde als C5/C6):** **GÉÉN futuro simple, GÉÉN condicional, GÉÉN subjuntivo** — ook niet impliciet. «Aanzet B1» = A2 stevig consolideren, geen nieuwe wijs/tijd. Scan elke unit hierop.
- **Cast:** dezelfde 4 tieners + Tú (+ Mateo, voseo, waar biografieën passen).

---

## 2 · Gedeelde infrastructuur die AL bestaat (hergebruiken)

C6+ gebruikt cursus-overstijgend alles wat C5 gebruikte:

| Wat | Pad |
|---|---|
| **Reservoir-catalogus** (453 plukbare items) | `02-huisstijl/reservoir/reservoir.json` + `reservoir_index.md` |
| **Dekkings-grootboek** | `02-huisstijl/reservoir/coverage.md` — **voeg C6+-kolommen toe** |
| **Parels** vorig project | `02-huisstijl/reservoir/PARELS_materiales.md` |
| **Vorige lessen + master-vocab** | `00-brondocumenten/materiales-vorig-project/` (`Cursus_Spaans_Woordenschat_Master_v8.xlsx` = kandidatenpool) |
| **Emoji-flashcards** | `02-huisstijl/beeld/generators/vocab_emoji.py` (additief uitbreiden) |
| **Cast/mascotte** | `02-huisstijl/beeld/generators/cast_gen.py` |
| **Print-CSS-kit** | `02-huisstijl/templates/cursus-print.css` |
| **Fonts** | `02-huisstijl/fonts/` (Bricolage Grotesque · Inter · Caveat) |
| **Motor-engine** | `spaans-motor/` (`node build.mjs`) |
| **Kaart** | `02-huisstijl/beeld/generators/mundo_map_real.svg` |

**Toolchain:** Chromium op `/opt/pw-browsers/chromium-*/chrome-linux/chrome`; `python-pptx`/`pymupdf`/`openpyxl` geïnstalleerd; `node` voor de motor.

**Cursuskleur C6+ = paars.** Enige token-wissel t.o.v. C5-groen: `--g:#7C56A9 · --gd:#5B3E83 · --gt:#EEE8F5` (uit `02-huisstijl/tokens/tokens.json`, sleutel `c6plus`). Verder niets aan layout/helpers/CSS wijzigen.

---

## 3 · DE REFERENTIE-UNIT = C5·U5 «¡Ñam!» (GELOCKT)

Elke C6+-unit wordt gebouwd door de U5-generatoren te kopiëren en enkel content + kleur te wisselen:

| Formaat | U5-referentie |
|---|---|
| Print (PDF) + editlaag | `01-cursussen/05-a1/U5/gen_u5_print.py` → `U5.html` → PDF |
| HTML-hub | `03-build/web/gen_u5_web.py` → `U5_web.html` |
| PowerPoint (2 decks) | `03-build/pptx/gen_u5_docente.py` (engine uit `gen_u0_docente.py`) |
| Motor-spellen | `spaans-motor/make_u5_games.py` |
| Cocktail-receta | `01-cursussen/05-a1/U5/U5_cocktail.md` |

---

## 4 · De 4 formaten + pijplijn (per unit; map `01-cursussen/06-vervolg/U<N>/`)

1. **PDF + bewerkbare laag** — `gen_u<N>_print.py` (kopie van `gen_u5_print.py`, content + paars-tokens) → `U<N>.html` (mét editbar Bewerken/Opslaan als PDF/Bewaar). Render: `CHROME --headless --no-sandbox --disable-gpu --no-pdf-header-footer --print-to-pdf=03-build/pdf/C6plus_U<N>.pdf "file://…/U<N>.html"`.
2. **HTML-hub** — `03-build/web/gen_u<N>_web.py` → `03-build/web/U<N>_web.html`.
3. **PowerPoint** — `03-build/pptx/gen_u<N>_docente.py` → `C6plus_U<N>_docente.pptx` **+** `C6plus_U<N>_alumno.pptx` (**alumno = `.pptx`, NOOIT `.ppsx`**).
4. **Motor** — `make_u<N>_games.py` → `content/es-c6plus-u<N>-*.json` → `node build.mjs` → embed in de hub.

> Een PDF wordt **altijd samen met zijn bewerkbare `U<N>.html`-laag** afgeleverd.

---

## 5 · Reservoir & cocktail-workflow (VERPLICHT vóór élke unit)

Zoals `CLAUDE.md §14ter`. **Lees vóór élke unit de drie cocktail-documenten:** `reservoir_index.md` · `coverage.md` · de `U<N>_cocktail.md` die je schrijft.
1. **Cocktail-receta** `01-cursussen/06-vervolg/U<N>/U<N>_cocktail.md`: per cursusonderdeel expliciet reservoir-IDs kiezen — **bewust onder-gebruikte** (raadpleeg `coverage.md`), variatie meetbaar over C5+C6+C6+.
2. **Quota (hard):** ≥1 luisterdialoog · ≥1 rijke Lectura · ≥2 opname · ≥1 traditionele cloze-werkwoord · traditionele oefenbatterij (gap-fill·substitutie·matching·dictee·ordenen) **naast** de visuele grammatica · HTML-hub **≥100 interactieve oefeningen met meerdere reeksen** + **10–20** motor-games.
3. **Master-vocab cureren** uit de pool (+ aanvullen; kandidatenpool, geen wet).
4. **Parels inweven** waar het thema matcht.
5. Na de build: **`coverage.md` bijwerken** (C6+-kolommen).

---

## 6 · Huisstijl-musts (het U5-model)

- **Emoji-flashcards** via `vocab_emoji.py` (geen grijze lijniconen).
- **Ruta-kaart discreet** (klein vanaf U1, groot enkel U0).
- **Cultura unit-eigen** (kop + 2–3 kaarten Spaans-eerst + NL + emoji), niet 4× dezelfde kaart.
- **VISUEEL-EERST grammatica + traditionele oefenbatterij ernaast.**
- **Volle antwoordruimte**; **nooit oplossingen op de leerlingpagina**; **sectienummering zonder gat**; elke hoofdsectie op nieuwe pagina.
- **PowerPoint:** 2 decks, alumno `.pptx`, ≥20 dia's, klik-onthul-animaties, **4 vaardigheden**, kruisverwijzingen print↔hub↔pptx.
- **Tellingen kloppen** (bv. «N spellen» = echt aantal games).

---

## 7 · GEEN LEGE PAGINA'S — de gevoeligste regel (verificatie verplicht)

Vertrouw **niet** op één inkt-drempel.
- **HTML:** simuleer een **echte klik** op elk subnav-tabblad (script dat na load de knop `.click()`-t), screenshot élk paneel en **lees de PNG's** (geen `emptyHosts`). JS-geïnjecteerde panelen (Lectura/Hablar) renderen pas op klik → force-CSS misleidt; test altijd via een echte klik.
- **Print:** meet inkt/vulling per pagina met pymupdf **én** render de dunste pagina('s) en **kijk ernaar**. Halflege pagina's oplossen met extra oefening of mee-vloeiende route-note. *(De «Mis palabras»-schrijftabel-slotpagina ~0,09 is de geaccepteerde U5-norm.)*

---

## 8 · Subagent-orkestratie — de GELEERDE LESSEN

- **Eén bouwer per unit, STRIKT SYNCHROON.** Instrueer expliciet: **«doe alles zelf, synchroon; spawn GEEN sub-agents; geen background; geen git».** Delegerende subagents stoppen te vroeg en leveren niets. De hoofdchat doet alle git.
- **Batch/gap-analyse over meerdere units = ultracode (Workflow-tool):** `pipeline(units, buildAgent, verifyAgent)` — per unit een bouwer + een **adversariële verificatie** met `StructuredOutput`-verdict (PASS/FAIL + issues). Model inheriten (Opus). Verschillende units = verschillende bestanden → geen worktree; gedeelde bestanden (`coverage.md`, motor-`index.html`) **achteraf consolideren** in de hoofdchat.
- **Verificatie meet echt** (paginatelling, vulling, `.anum`, `python-pptx` opent beide decks, `<p:timing>`, 4 vaardigheden, geen stale tellingen).
- **Golden sample eerst:** bouw eerst één C6+-unit volledig, laat goedkeuren, **lock** die als C6+-referentie, vóór je opschaalt.

---

## 9 · Git & levering

- **Werkbranch:** vraag de auteur de C6+-branchnaam. Commit-berichten in het Nederlands.
- **`03-build/*` is gitignored** → build-outputs met **`git add -f`**. Push met exponentiële back-off.
- **Levering per unit** = zip met `C6plus_U<N>_cursus.pdf` · `..._cursus_BEWERKBAAR.html` · `..._digitale-hub.html` · `..._PowerPoint_DOCENTE.pptx` · `..._PowerPoint_ALUMNO.pptx` + LEESMIJ.
- **Werkende versies** (klasgebruik): beide pptx openen (structureel via `python-pptx` + zip-integriteit; LibreOffice/PowerPoint rendert niet in de sandbox), PDF rendert volledig.

---

## 10 · Werkvolgorde (samengevat)

1. **Modelmelding** (§0) → gebruiker zet model.
2. **Neem het C6+-plan over** dat in de C6+-chat beslist is (gap-analyse + welke hiaten/units). Vul `00-brondocumenten/espanol-en-la-practica/` + `00-brondocumenten/gap-analyse/` waar nodig aan.
3. **Kopieer** de U5-generatoren → C6+·U<N>, wissel paars-tokens + content.
4. **Cocktail-receta** (reservoir plukken, quota, master-vocab cureren, parels) — lees de drie cocktail-documenten.
5. **Bouw** de 4 formaten, synchroon.
6. **Verifieer hard** (§7 geen lege pagina's · §6 tellingen · werkende pptx).
7. **Coverage bijwerken**, commit + push, **lever de zip**.
8. **Eerste unit laten goedkeuren + locken**, dan de rest (evt. ultracode-batch).

> **In één zin:** C6+ = C5's pijplijn, U5 als sjabloon, reservoir/cocktail-workflow, **paars** i.p.v. groen, inhoud = het **in de C6+-chat besliste gap-analyse-plan** (hiaten van *Español en la práctica* invullen richting A2→B1, géén subjuntivo), geen lege pagina's, werkende `.pptx`, en **de chat meldt telkens welk model hij nodig heeft**.
