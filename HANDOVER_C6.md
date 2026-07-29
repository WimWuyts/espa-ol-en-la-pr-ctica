# HANDOVER — Bouw C6 (6de jaar · blauw) EXACT zoals C5

> **Doel van dit document:** één verse chat moet hiermee de **volledige cursus C6** kunnen bouwen, **identiek qua proces en kwaliteit** aan de C5-cursus die al in deze repo staat. C6 leeft in **dezelfde monorepo** (`01-cursussen/06-clean/`) en **hergebruikt alle gedeelde infrastructuur** van C5 — enkel de **cursuskleur (blauw)** en de **content** verschillen.
>
> **Lees óók `CLAUDE.md`** (projectgeheugen, wordt automatisch ingeladen) — dat bevat álle bindende specs (§13–§18, §14ter reservoir/cocktail). Dit document is de *werkwijze-samenvatting* + de C6-specifieke invulling + de geleerde lessen.

---

## 0 · DE ALLEREERSTE REGEL — meld welk model je nodig hebt

**Bindend, elke bouwstap:** vóór je iets bouwt, **vertel je de gebruiker expliciet welk model je nodig hebt** en waarom. De gebruiker zet het model dan goed (hij werkt standaard op **Opus**). Gebruik deze verdeling:

| Taak | Model | Waarom |
|---|---|---|
| **Unit bouwen** (print/hub/pptx/games volgens het U5-sjabloon) | **Opus** (of Sonnet als werkpaard bij kostbewaking) | correctheid Spaans + valstrikken + lege-pagina-controle tellen |
| **Batch print+pptx over meerdere units** | **Opus + ultracode** (Workflow-tool) | deterministische fan-out per unit + adversariële verificatie |
| **Brede mechanische verificatie** (tellingen, cross-format, spelling-scan, coverage) | **Fable** | snel & goedkoop, hoog volume |
| **Zwaarste redenering** (leerplan/didactiek, lastige content, gap-analyse) | **Opus** | diepste redeneren |

Zeg het telkens zó: *«Voor deze [unit-build / audit / workflow] heb ik **[model]** nodig — zet je me daarop? (ultracode aan/uit)».* Nooit stil beginnen zonder de modelmelding.

---

## 1 · Wat C6 is (kader)

- **C6 «Historias y mundos», 6de jaar, kleur BLAUW.** Volgt hetzelfde leerplan III-Spa-d als C5. Niveau: **A2 → aanzet B1**. Bouwt door op C5.
- **9 units:** U0 ¡De vuelta! (heropstart/brug) → U1 … → U8. Titels/paradas: zie `00-brondocumenten/outlines/Outline_Jaar6_A2-B1.md` (leidend) + `CLAUDE.md §12`.
- **La Ruta C6 «Historias y mundos»** (provisoir): Argentina/Buenos Aires (U1) · leyenda Meso-Amerika (U2) · Chile/Patagonia (U3) · España/Cuba (U4) · dos ciudades (U5) · digitaal/pan-hispano (U6) · Costa Rica (U7) · Amazonía/globaal (U8).
- **Cast:** dezelfde 4 tieners + Tú, **+ Mateo (Buenos Aires 🇦🇷, voseo)** die pas vanaf C6 meedoet (biografieën).
- **Leerplan-scope C6 (HARD):** nieuw t.o.v. C5 = **indefinido · imperfecto · contrast indefinido/imperfecto · por/para · volledig pronomensysteem (le/les · se lo) · comparativos + betrekkelijke bijzin *que* · imperativo · mening met INDICATIVO**. **GÉÉN futuro simple, GÉÉN condicional, GÉÉN subjuntivo** — ook niet impliciet. Scan elke unit hierop.

---

## 2 · Gedeelde infrastructuur die AL bestaat (hergebruiken, niet heruitvinden)

Alles hieronder staat al in de repo en is **cursus-overstijgend** — C6 gebruikt het één-op-één:

| Wat | Pad |
|---|---|
| **Reservoir-catalogus** (453 plukbare items WV/LAY/GT/PPT/VS/VG/SK/DS) | `02-huisstijl/reservoir/reservoir.json` + `reservoir_index.md` |
| **Dekkings-grootboek** (item × unit) | `02-huisstijl/reservoir/coverage.md` — **voeg C6-kolommen toe** |
| **Parels** uit het vorige project | `02-huisstijl/reservoir/PARELS_materiales.md` (check welke voor C6-thema's passen) |
| **Vorige lessen + master-vocab** | `00-brondocumenten/materiales-vorig-project/` (o.a. `Cursus_Spaans_Woordenschat_Master_v8.xlsx`, kolom *Unidad de introducción* → filter **`J6`** voor C6-kandidaten; + `C4_U1_bandasonora-model.html`) |
| **Emoji-flashcard-module** | `02-huisstijl/beeld/generators/vocab_emoji.py` (`emoji_for(word, grp)`) — breid additief uit voor C6-woorden |
| **Cast/mascotte-generator** | `02-huisstijl/beeld/generators/cast_gen.py` (voeg Mateo toe waar nodig) |
| **Print-CSS-kit** | `02-huisstijl/templates/cursus-print.css` |
| **Fonts** (base64 embed) | `02-huisstijl/fonts/` (Bricolage Grotesque · Inter · Caveat) |
| **Motor-engine** (offline spellen) | `spaans-motor/` (templates classify·match·memory·cloze·tap·order·tetris·point·sim·speak; `node build.mjs`) |
| **Kaart** (Natural Earth) | `02-huisstijl/beeld/generators/mundo_map_real.svg` |

**Toolchain (staat klaar):** Chromium op `/opt/pw-browsers/chromium-*/chrome-linux/chrome`; Python-pakketten `python-pptx`, `pymupdf`, `openpyxl` geïnstalleerd; `node` voor de motor.

**Cursuskleur C6 = blauw.** De **enige token-wissel** t.o.v. C5-groen: `--g:#2E77C2 · --gd:#1E5691 · --gt:#E5EFF9` (uit `02-huisstijl/tokens/tokens.json`, sleutel `c6`). Verder niets aan layout/helpers/CSS wijzigen.

---

## 3 · DE REFERENTIE-UNIT = C5·U5 «¡Ñam!» (GELOCKT)

**Elke C6-unit wordt gebouwd door de U5-generatoren te kopiëren en enkel content + kleur te wisselen.** U5 is de goedgekeurde norm van het reservoir/cocktail-tijdperk. Referentiebestanden:

| Formaat | U5-referentie |
|---|---|
| Print (PDF) + bewerkbare laag | `01-cursussen/05-a1/U5/gen_u5_print.py` → `U5.html` → PDF |
| HTML-hub | `03-build/web/gen_u5_web.py` → `U5_web.html` |
| PowerPoint (2 decks) | `03-build/pptx/gen_u5_docente.py` (importeert engine uit `gen_u0_docente.py`) |
| Motor-spellen | `spaans-motor/make_u5_games.py` → `content/es-u5-*.json` |
| Cocktail-receta | `01-cursussen/05-a1/U5/U5_cocktail.md` |

---

## 4 · De 4 formaten + exacte pijplijn (per unit)

Maak per C6-unit (naamgeving spiegelt C5, map `01-cursussen/06-clean/U<N>/`):

1. **PDF + bewerkbare laag** — `gen_u<N>_print.py` (kopie van `gen_u5_print.py`, content + blauw-tokens gewisseld) → schrijft `U<N>.html` (mét **editbar**: Bewerken / Opslaan als PDF / Bewaar). Render:
   `CHROME --headless --no-sandbox --disable-gpu --no-pdf-header-footer --print-to-pdf=03-build/pdf/C6_U<N>.pdf "file://…/U<N>.html"`
2. **HTML-hub** — `03-build/web/gen_u<N>_web.py` (kopie van `gen_u5_web.py`) → `03-build/web/U<N>_web.html`.
3. **PowerPoint** — `03-build/pptx/gen_u<N>_docente.py` (kopie van `gen_u5_docente.py`) → `C6_U<N>_docente.pptx` **+** `C6_U<N>_alumno.pptx` (**alumno = `.pptx`, NOOIT `.ppsx`**).
4. **Motor-spellen** — `spaans-motor/make_u<N>_games.py` → `content/es-c6u<N>-*.json` → `cd spaans-motor && node build.mjs` → embed in de hub.

> **Levering:** een PDF wordt **altijd samen met zijn bewerkbare `U<N>.html`-laag** afgeleverd. Nooit enkel de platte PDF.

---

## 5 · Reservoir & cocktail-workflow (VERPLICHT vóór élke unit)

Exact zoals `CLAUDE.md §14ter`:
1. **Cocktail-receta** `01-cursussen/06-clean/U<N>/U<N>_cocktail.md` schrijven: per cursusonderdeel expliciet **reservoir-IDs** kiezen — **raadpleeg `coverage.md` en kies bewust onder-gebruikte items** (variatie meetbaar laten groeien over C5 **én** C6).
2. **Quota (harde ondergrens per unit):** ≥1 luisterdialoog (script + TTS + begripstaak) · ≥1 rijke Lectura · ≥2 opname-oefeningen · ≥1 traditionele cloze-werkwoord (vormen nagerekend) · een **traditionele oefenbatterij** (gap-fill·substitutie·matching·dictee·ordenen) **naast** de visuele grammatica.
3. **HTML-HUB oefenrijkdom:** **≥100 interactieve oefeningen** met **meerdere reeksen per oefening** (elke game trekt uit pool ≥12 → «↻ otra serie») + inline zelfcorrigerende grammaticatools/drills náást de **10–20** motor-games.
4. **Master-vocab cureren** uit de `J6`-pool (+ aanvullen; het is een kandidatenpool, geen wet — forceer de aantallen niet).
5. **Parels inweven** waar een C6-thema matcht.
6. Na de build: **`coverage.md` bijwerken** met de exact gebruikte IDs (C6-kolommen).

---

## 6 · Huisstijl-musts (het U5-model — niet-onderhandelbaar)

- **Emoji-flashcards:** élke flashcard een kleur-emoji (Materiales-stijl) via `vocab_emoji.py` — **geen grijze Lucide-lijniconen**.
- **Ruta-kaart discreet:** klein (`max-width:360px`, onder «📍 La Ruta») vanaf U1; **groot enkel in U0**.
- **Cultura unit-eigen:** kop = het unit-eigen culturele aspect + 2–3 cultuurkaarten (Spaans-eerst + NL + emoji), waar mogelijk uit `materiales-vorig-project`. **Niet** 4× dezelfde kaart.
- **VISUEEL-EERST grammatica** (machine/blocks/agree/tree/mirror/fmu/scaffold/zoom/xray) **+ traditionele oefenbatterij** ernaast. Nooit «tekstblok + tabel + rij invuloefeningen».
- **Volle antwoordruimte** (wcols/wbox/wl/wtab); **nooit oplossingen op de leerlingpagina**.
- **Sectienummering zonder gat**; **elke hoofdsectie op nieuwe pagina**.
- **PowerPoint:** 2 decks, alumno als `.pptx`, ≥20 dia's, klik-onthul-animaties, **4 vaardigheden**, print↔HTML-kruisverwijzingen.
- **Kruisverwijzingen** print ↔ hub (QR → juiste anker) ↔ pptx.
- **Tellingen kloppen** (bv. «N spellen» in print/pptx = het echte aantal games in de hub).

---

## 7 · GEEN LEGE PAGINA'S — de gevoeligste regel (verificatie verplicht)

De auteur is zeer gevoelig voor lege/halflege pagina's. **Vertrouw niet op één inkt-drempel** (0,06 is te mild — een halflege pagina met een tabel haalt 0,08 en "slaagt" ten onrechte).
- **HTML:** simuleer een **echte klik** op elk subnav-tabblad (script dat na load de knop `.click()`-t), screenshot **elk** paneel en **lees de PNG's** — bevestig dat élk paneel vol staat (geen `emptyHosts`). JS-geïnjecteerde panelen (Lectura/Hablar) renderen pas op klik — een force-CSS-weergave misleidt, dus altijd via een echte klik testen.
- **Print:** meet met pymupdf de inkt-vulling per pagina **én** render de dunste pagina('s) als PNG en **kijk ernaar**. Los halflege pagina's op met extra oefening of een mee-vloeiende route-note — nooit een los slot-kader dat alleen op een pagina spilt. *(De «Mis palabras»-schrijftabel-slotpagina is de geaccepteerde U5-norm ~0,09 vulling; die mag.)*

---

## 8 · Subagent-orkestratie — de GELEERDE LESSEN (belangrijk)

- **Eén bouwer per unit, STRIKT SYNCHROON.** Instrueer elke bouw-subagent expliciet: **«doe alles zelf, synchroon; spawn GEEN sub-agents; geen background; geen git».** Subagents die denken dat ze naar «achtergrond-build-agents» delegeren, **stoppen te vroeg en leveren niets** — dat is meermaals misgegaan. De hoofdchat doet alle git.
- **Batch over meerdere units = ultracode (Workflow-tool).** Patroon dat werkte voor de U0–U4 print/pptx-upgrade: `pipeline(units, buildAgent, verifyAgent)` — per unit een bouwer gevolgd door een **adversariële verificatie-agent** met een `StructuredOutput`-verdict (PASS/FAIL + issues). Model inheriten (Opus). Agents die verschillende units raken = verschillende bestanden → geen worktree nodig; gedeelde bestanden (`coverage.md`, motor-`index.html`) **achteraf consolideren** in de hoofdchat (parallelle edits clobberen elkaar).
- **Verificatie is adversarieel en meet echt** (geen «ziet er goed uit»): paginatelling, inkt/vulling, `.anum`-telling, `python-pptx` opent beide decks, `<p:timing>`-animaties aanwezig, 4 vaardigheden, parels aanwezig, geen stale tellingen.
- **Golden sample eerst:** bouw **eerst C6·U0 (of U1) volledig**, laat de auteur goedkeuren en **lock** die als C6-referentie (net als C5·U5), vóór je opschaalt.

---

## 9 · Git & levering

- **Werkbranch:** vraag de auteur de C6-branchnaam (in C5 was dat `claude/spanish-course-c5-c6-cadm4g`; C6 kan een eigen branch krijgen). Commit-berichten in het Nederlands, kort en beschrijvend.
- **`03-build/*` is gitignored** → build-outputs met **`git add -f`** forceren. Push: `git push -u origin <branch>` met exponentiële back-off bij netwerkfouten.
- **Levering per unit** = zip met: `C6_U<N>_cursus.pdf` · `C6_U<N>_cursus_BEWERKBAAR.html` · `C6_U<N>_digitale-hub.html` · `C6_U<N>_PowerPoint_DOCENTE.pptx` · `C6_U<N>_PowerPoint_ALUMNO.pptx` + een LEESMIJ.
- **Werkende versies:** dit zijn klasversies. Verifieer dat beide pptx openen (structureel — LibreOffice/PowerPoint rendert niet in de sandbox; check via `python-pptx` + zip-integriteit) en dat de PDF volledig rendert.

---

## 10 · Werkvolgorde (samengevat)

1. **Modelmelding** (§0) → gebruiker zet model.
2. **Kopieer** de U5-generatoren naar C6·U<N>, wissel blauw-tokens + content.
3. **Cocktail-receta** schrijven (reservoir plukken, quota, master-`J6`-vocab cureren, parels).
4. **Bouw** de 4 formaten (§4), synchroon.
5. **Verifieer** hard (§7 geen lege pagina's · §6 tellingen · werkende pptx).
6. **Coverage bijwerken**, commit + push, **lever de zip**.
7. **U0/U1 eerst laten goedkeuren + locken**, dan de rest (evt. via ultracode-batch).

> **In één zin:** C6 = C5's pijplijn, U5 als sjabloon, reservoir/cocktail-workflow, blauw i.p.v. groen, C6-leerstof (indefinido/imperfecto/… — géén subjuntivo), geen lege pagina's, werkende `.pptx`, en **de chat meldt telkens welk model hij nodig heeft**.
