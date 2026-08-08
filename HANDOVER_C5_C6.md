# HANDOVER — bouw C5 (groen) + C6 (blauw) volledig af

> **Dit bestand is de enige referentie die een nieuwe chat nodig heeft om de hele cursus voor
> het 5de (C5) en 6de (C6) jaar te bouwen, exact zoals de goedgekeurde golden sample Unidad 0.**
> Lees óók `CLAUDE.md` (projectgeheugen) — die wordt automatisch ingeladen en bevat alle bindende specs (§13–§18).

---

## 0 · Wat is de opdracht

Bouw **unit per unit** de volledige cursus af:
- **C5 «El día a día» (groen)** — `01-cursussen/05-a1/` — U0 is klaar (golden sample); **bouw U1 → U8**.
- **C6 «Historias y mundos» (blauw)** — `01-cursussen/06-clean/` — **bouw U0 → U8**.

Elke unit levert **4 formaten** met identieke, uitgeverswaardige layout: **PDF · HTML · PowerPoint (2 decks) · (motor-spellen ingebed in HTML)**. C4 (rood) en C6+ (paars) worden in **andere** chats gebouwd; niet hier.

**Werkbranch:** `claude/spanish-course-development-jx25ay`. Commit-berichten in het Nederlands. Niet naar een andere branch pushen.

---

## 1 · De golden sample U0 = de norm (LOCKED 2026-07-26)

Alles hieronder is bij U0 vastgelegd en **moet identiek** bij elke volgende unit. Referentiebestanden:

| Formaat | Bestand | Generator |
|---|---|---|
| PDF (print) | `03-build/pdf/C5_U0.pdf` | ← `01-cursussen/05-a1/U0/U0.html` via Chromium |
| Bewerkbare cursus | `01-cursussen/05-a1/U0/U0.html` | (editbar-injectie, zie §3) |
| HTML-hub (digitaal) | `03-build/web/U0_web.html` | `03-build/web/gen_u0_web.py` |
| PowerPoint docente | `03-build/pptx/C5_U0_docente.pptx` | `03-build/pptx/gen_u0_docente.py` |
| PowerPoint alumno | `03-build/pptx/C5_U0_alumno.pptx` | idem (`build()`-modes) |
| Conjugador (cursus-tool) | `03-build/web/Conjugador.html` | `03-build/web/gen_conjugador.py` |

**Aanpak per nieuwe unit:** kopieer de U0-generator naar `gen_u<N>_web.py` / `gen_u<N>_docente.py`, wissel enkel het **per-unit config-blok** (§5) en de content (§2). Niets aan de layout/pijplijn/tokens veranderen.

---

## 2 · Content = één bron (single source)

Per unit een contentbron: `01-cursussen/<cursus>/U<N>/U<N>_bron.md` (+ optioneel `_parts/*.md` en `_html/*.html` fragmenten). Daaruit worden alle formaten gevoed. **Álle lopende tekst = Spaans-eerst met Nederlandse steun** (ook verteltekst, ¡Ojo!-kaders, grammatica-uitleg). Nooit een tekstblok enkel in het Nederlands.

Vaste sectiestructuur (CLAUDE.md §6): `§0 ¡Ponte al día!` → `§1…§N` → `Taller de lengua` → `Cultura` → `Tarea final` (genummerde pasos) → `Repaso` (spiekkaart + semáforo, res­t = online) → `§V Vocabulario` (tabel Español·NL·ERK·Ejemplo + oefenladder).

---

## 3 · Pijplijn per formaat — EXACTE parameters

### 3a · PDF (print) + bewerkbare laag
- **Bron = één HTML-bestand** `U<N>.html` met **inline `<style>`**, fonts lokaal/base64, **alle SVG's inline**.
- **Bindende `@page`/layout (uit U0.html — niet wijzigen):**
  ```css
  @page{ size:A4; margin:12mm 0; }
  @page:first{ margin:0 0 12mm 0; }   /* hero-bleed op p1 */
  .page{ padding:0 15mm; }            /* horizontale marge van de content */
  .sec{ break-before:page; }          /* elke hoofdsectie op nieuwe pagina */
  ```
  Print-hygiëne: `print-color-adjust:exact`, `thead` herhaalt, weesregel-preventie (`break-after:avoid` op koppen), `break-inside:avoid` op coherente blokken. **Nooit** een sectiekop onderaan een pagina; **nooit** een kader/tabel doorgesneden over de paginagrens.
- **Render-commando** (Chromium staat op `/opt/pw-browsers/chromium-*/chrome-linux/chrome`):
  ```
  CHROME --headless --no-sandbox --disable-gpu --print-to-pdf=out.pdf --no-pdf-header-footer "file://<abs>/U<N>.html"
  ```
- **Bewerkbare laag** (auteur bewerkt zelf tekst → identieke PDF): injecteer in `U<N>.html`, vóór `</body>`, de **editbar** + script (zie het blok in `01-cursussen/05-a1/U0/U0.html`, zoek `class="editbar"`). Het maakt een curated set tekst-selectors `contenteditable`, met knoppen **Bewerken / Opslaan als PDF / Bewaar**, verborgen in print via `@media print{ .editbar{display:none} }`. Idem aanpak in de HTML-hub.

### 3b · HTML-hub (digitaal)
- Generator `gen_u<N>_web.py` (kopie van `gen_u0_web.py`). Produceert **één standalone bestand** met base64-fonts.
- Bevat: flashcards (alle woorden, ES↔NL, TTS), woordenschat-zoek, **visuele grammatica** (context→noticing→regel→toepassen), **veel oefeningen** geordend receptief→gestuurd→productief (met steun-afbouw), **de 17+ motor-arcade-spellen base64 INGEBED** (openen in modal → werken offline), **interactieve kaart** (klik land → vlag+landcode+info; uit `build_map.py`, paden getagd `class="spa" data-c="ISO"`), interactief abecedario (TTS), editbar.
- **BINDEND (auteur 2026-07-26) — flashcard-icoon:** élke flashcard krijgt een **consistent Lucide-lijnicoon** op de **voorkant, boven het woord** (34px, cursusgroen `var(--gd)`, grijswaarden-veilig, `aria-hidden`). Gedeelde module `02-huisstijl/beeld/generators/vocab_icons.py` (`icon_svg(word, grp)` → WORD_ICON → KEYWORD → GROUP-fallback; nooit leeg). Importeer in élke `gen_u<N>_web.py` en render in de flashcard-voorkant. **Zelfde stijl/plaatsing over álle units.**
- **BINDEND (auteur 2026-07-26) — Cultura-panel unit-eigen:** het Cultura-panel mag NIET 4× dezelfde «mundo hispano»-kaart tonen. Kop = **het unit-eigen culturele aspect**; bovenaan 1–2 `.card`-cultuurblokken (kop `h3` + `p`, **Spaans-eerst + NL**, met Lucide-icoon), samengevat uit de print-`U<N>.html` Cultura-sectie; **daarna** de klikbare kaart onder de subkop **«La Ruta · ¿dónde estamos?»**. Cultuur-kaarten binnen editbar-bereik.
- **Kruisverwijzingen**: QR's op print → naar deze hub op het juiste anker.
- **Géén** werkwoordsvervoeging/conjugador in de unit-hub — dat is een **aparte cursus-tool** (§4).

### 3c · PowerPoint (2 decks) — GEANIMEERD format (LOCKED)
- Generator `gen_u<N>_docente.py`, `build(mode,out)` → **docente `.pptx`** (oplossingen + spreker-notities) + **alumno `.pptx`** (leerling drukt **F5** voor de diavoorstelling). **NB:** lever de alumno NIET als `.ppsx` — dat slideshow-contenttype wordt door PowerPoint geweigerd («kan niet worden gelezen»). `to_ppsx()` blijft in de engine maar wordt niet meer voor levering gebruikt.
- **Klik-animaties** via geïnjecteerde `<p:timing>` (verschijnen-bij-klik). **Geen kioskmodus.** De decks openen zonder reparatievraag; die kwam van een dubbele `<a:effectLst>` in `_soft_shadow()`, niet van de animaties (opgelost 2026-08-05, zie `03-build/pptx/repara_effectlst.py`).
- Diamaster-layouts + regels: CLAUDE.md §16 (TITLE·LESSON_MENU·VOCABULARY·GRAMMAR·READING·LISTENING·SPEAKING·WRITING·QUIZ·FEEDBACK·CULTURE·FINAL_MISSION·TEACHER_NOTES), noodroute-hyperlinks, echte cast-avatars, huisstijl, ≥20 dia's.
- Echte cast-avatar-PNG's: `03-build/pptx/assets/` (gerenderd via `03-build/pptx/render_avatars.py` uit `cast_gen.py`).

### 3d · Motor-spellen (azulejo-stijl, LOCKED)
- `spaans-motor/` — elk spel = één standalone offline HTML. Sjablonen: `classify · match · tetris · cloze · tap · order · memory`. Generatoren `conjugation/gender/verbo` (nagerekend). Content in `spaans-motor/content/es-u<N>-*.json`, build: `cd spaans-motor && node build.mjs`.
- Per thema **10–15 gevarieerde spellen** (receptief→productief). **Stijl blijft azulejo** (donker tegelthema) — bewust contrast met de cursuskleur; NIET omkleuren.
- Titels in content: géén `<span>` (engine escapet titels → letterlijk).

### 3e · Conjugador (cursus-niveau tool, APART — niet per unit)
- `03-build/web/gen_conjugador.py` + database `03-build/web/verbos_es.json` (vormen **nagerekend via de motor-engine**, `03-build/web/extract_verbos.mjs`, die `spaans-motor/src/generators.js::presente()` hergebruikt — **nooit zelf vervoegen**).
- Drie tabs: **Opzoeken** (zie vervoeging, chips beperkt tot veelgebruikte + zoeken) · **Zelf vervoegen** (persona + infinitivo + context → leerling vervoegt, met hint/afbouw) · **Alle werkwoorden** (volledige tabel) + free-text-veld (élk getypt werkwoord, regelmatig-fallback met ⚠️). **Enkel presente** (leerplan: geen futuro/condicional/subjuntivo). Wordt uitgebreid naar **~1000** werkwoorden.

---

## 4 · Huisstijl & tokens (single source)

- Tokens: `02-huisstijl/tokens/tokens.json` + `tokens.css`. Fonts: koppen **Bricolage Grotesque**, tekst **Inter**, notities **Caveat** (in `02-huisstijl/fonts/`, ingebed in álle formaten).
- **Print-CSS-kit (bindend):** `02-huisstijl/templates/cursus-print.css`.
- **Cursuskleur = enige variabele per cursus** — wissel `--g / --gd / --gt`:
  - **C5 groen:** `--g:#1E9E74 · --gd:#157355 · --gt:#E4F4EE`
  - **C6 blauw:** kies de blauw-tokens uit `tokens.json` (zelfde rol/structuur).
- **Twee kleurlagen:** (1) cursus-/unitkleur voor navigatie; (2) functionele taalsemantiek (blauw=persoon · oranje=werkwoord · groen=voorwerp · paars=tijd · turquoise=plaats · rood=waarschuwing · geel=strategie). Kleur nooit enige informatiedrager.

---

## 5 · Per-unit config (dit is het énige dat per unit verandert)

Vul per unit dit blok in (afgeleid uit CLAUDE.md §12 La Ruta + het leerplan):

```
cursus         : C5 (groen)  |  C6 (blauw)
unit-nr / titel: U<N> · «…»
parada         : <plaats/land>  (La Ruta-tabel §12)
gastheer-cast  : Lucía(Sevilla) | Diego(CDMX) | Valen(Cartagena) | Nina(Cusco) | Mateo(BsAs, vanaf C6)
secties        : §0…§V (vaste structuur §2)
tarea final    : <communicatief reis-artefact> (afzender·ontvanger·doel·situatie·resultaat)
LPD-codes      : <III-Spa-d codes, zelf afgeleid uit 00-brondocumenten/leerplan/>
vocab          : U<N>-woordenlijst → JSON (ES·NL·soort·ejemplo)
spellen        : 10–15 motor-spellen op de unit-woordenschat/grammatica
```

**La Ruta — C5 (VASTGELEGD):** U0 España · U1 Madrid (Mi pasaporte) · U2 Andalucía/Sevilla (Álbum de familia) · U3 Barcelona (Un día en mi vida) · U4 València/costa (Mi playlist) · U5 México/CDMX (La carta) · U6 México/mercados (Abre tu tienda) · U7 Colombia/Cartagena (Mapa de mi barrio) · U8 Perú/Cusco·Machu Picchu (Diario de viaje).
Grammatica-plafond C5: t.e.m. **perfecto compuesto**.

**La Ruta — C6 (provisoir, §12):** Argentina/BsAs · leyenda Meso-Amerika · Chile/Patagonia · España/Cuba · dos ciudades · digitaal/pan-hispano · Costa Rica · Amazonía/globaal. Nieuw in C6: indefinido · imperfecto · contrast · por/para · volledig pronomensysteem · comparativos + betrekkelijke `que` · imperativo · mening met **indicativo**. **Harde grens (leerplan):** géén futuro/condicional/subjuntivo, ook niet in C6.

---

## 6 · Didactiek (bindend — CLAUDE.md §14)

Receptief→productief · **retrieval vóór herlezen** · **steun-afbouw** (model → woordenbank → beginletter/zinsframe → cue → geen steun) · vijf fasen (herkennen→onderscheiden→ophalen→gestuurd→vrij) · **antwoordruimte in print** (type-correcte schrijfruimte; nooit oplossingen op de leerlingpagina) · **repaso = online** (print = enkel spiekkaart + semáforo) · communicatieve eindtaken · geïntegreerde vaardigheden · **VARIATIE key** (>200 werkvormen bestaan; geen herhaling).

---

## 7 · Beslissingen die in deze sessie definitief werden (LOCKED)

1. Motor-spellen **azulejo-stijl behouden** (contrast). Niet omkleuren.
2. Audio = **browser-TTS** voorlopig (geen eigen opnames).
3. **Conjugador = aparte cursus-tool**, ~1000 werkwoorden, 2 lagen, enkel presente. Werkwoordsvervoeging **niet** in de units.
4. **PowerPoint = geanimeerd format** (klik-animaties), 2 decks, geen kiosk. Opent zonder reparatievraag.
5. **Bewerkbare laag** op zowel PDF-cursus (`U<N>.html`) als HTML-hub (contenteditable + Opslaan-als-PDF + Bewaar).
6. **Kaart = échte geografie** (Natural Earth), **klikbaar** in HTML, met **vlaggen + landcodes**.
7. QR's op print → naar de HTML-hub (niet rechtstreeks YouTube/PPTX).

### 7bis · Audioscripts — waar ze staan (2026-08-04)

Alle gesproken tekst van C5 en C6+ staat in **twee databronnen**, met hetzelfde
`guion`-formaat (`{who, es, nl}`):

| Bron | Wat | Aantal |
|---|---|---|
| `03-build/web/escucha_data.py` | het lange luisterfragment per unit (zesdelige begripsladder) | 17 |
| `03-build/web/escucha_corta_data.py` | de korte audiotaken per unit (de `audiorow`-blokken met QR: microdictado, klankreeks, mini-dialoog, weerbericht, wegbeschrijving…) | 44 |

- **Antwoordsleutels** zitten in het veld `clave` — die horen in het
  docentendossier en de hub-zelfcorrectie, **nooit** op de leerlingpagina.
- Het veld `etiqueta` bevat het etiket **letterlijk zoals het in de printunit
  staat** («Audio 3.2 · Microdictado · 0:40»), zodat print en audio bij de
  hosting-sweep één-op-één te matchen zijn.
- Twee blokken hebben bewust **geen script en geen mp3**: de Rosalía-fragmenten
  (`C5-U4-AUD-04`, `C6P-U1-AUD-03`). Bestaande muziek — extern afspelen, tekst
  niet overnemen.
- Renderen: `ELEVENLABS_API_KEY=… python3 03-build/web/gen_audio_elevenlabs.py C5 3`
  (voegt lange + korte fragmenten samen; `--dry` toont wat er zou komen,
  `--solo cortos` beperkt tot de korte taken). Het mp3-pad komt uit het
  `audio`-veld van het fragment zelf, hetzelfde veld dat de hub gebruikt.
- Enkele `nota`-velden melden een **mismatch met de gedrukte oefening** (o.a.
  «zes zinnen» tegenover een rooster met vier rijen in C5 U1 en U4, en drie
  tegenover vier steden in C5 U8). Bij een herbouw van die units mee rechtzetten.

---

## 8 · Build-commando's (samengevat)

```
# PDF
python3 03-build/web/... (indien generator) ; daarna:
CHROME --headless --no-sandbox --disable-gpu --print-to-pdf=03-build/pdf/C5_U<N>.pdf --no-pdf-header-footer "file://.../U<N>.html"
# HTML-hub
python3 03-build/web/gen_u<N>_web.py
# PowerPoint (beide decks)
python3 03-build/pptx/gen_u<N>_docente.py
# Motor-spellen
cd spaans-motor && node build.mjs
# Conjugador (cursus-tool, 1x)
node 03-build/web/extract_verbos.mjs && python3 03-build/web/gen_conjugador.py
```
CHROME = `/opt/pw-browsers/chromium-*/chrome-linux/chrome`. Verifieer visueel met `--screenshot` en `--dump-dom` (in deze sandbox is er geen LibreOffice/PowerPoint — PPTX enkel via XML-structuur verifiëren).

---

## 9 · QA-checklist per unit (vóór opleveren)

- [ ] **OEFENDICHTHEID = golden sample U0** (≈45–50 oefeningen · ≈50 p print). Fijnmazige §x.1–x.3-cycli · ≈4 oefeningen per subsectie over de 5 fasen met steunafbouw · **Tarea comunicativa ná élke sectie** · volle antwoordruimte-set (`wcols`/`wbox`/`wl`/`wtab`) · meerdere audio-QR · rijk beeld ín de secties · werkvorm-variatie uit de 100 werkvormen (geen herhaling). **Zie CLAUDE.md §14 «OEFENDICHTHEID».** Vergelijk expliciet met `C5_U0.pdf` vóór oplevering.
- [ ] 4 formaten gegenereerd; cursuskleur correct (C5 groen / C6 blauw).
- [ ] Spaans-eerst + NL-steun overal; geen NL-only tekstblok.
- [ ] Print-hygiëne: geen weesregel-koppen, geen doorgesneden kaders, elke hoofdsectie op nieuwe pagina, kleuren printen.
- [ ] Bladspiegel efficiënt gevuld (geen halflege pagina's, geen bladvullende lege omranding), composities variëren.
- [ ] Antwoordruimte type-correct; geen oplossingen op leerlingpagina.
- [ ] HTML: spellen openen & werken, kaart klikbaar, editbar werkt (breed bereik: hero/koppen/inhoudskaarten), TTS in Chrome/Edge, **opname-oefeningen** (inline MediaRecorder in de hub), **Lectura-panel**.
- [ ] **Traditionele cloze-werkwoordsoefening** aanwezig in de cursus (§14bis) + als motor-spel op de hub.
- [ ] **Leessectie (Lectura)** aanwezig in de cursus (§14bis) — visuele tekstintro → voorspellen → scannen → V/F+bewijs → productieve reactie.
- [ ] Games gekozen **in functie van de leerstof** + **variatie** (put uit >100 motor-oefentypes; geen speltype 2× met dezelfde jas). Ontbreekt een geschikt speltype → **motor-sjabloon bijbouwen**.
- [ ] PPTX: 2 decks, **beide `.pptx`** (alumno NIET als `.ppsx` — dat weigert PowerPoint), echte avatars, ≥20 dia's, animaties aanwezig, vier vaardigheden gedekt, print↔HTML-kruisverwijzing.
- [ ] **Getallen/tellingen kloppen** (bv. «N spellen» in print = werkelijk aantal games in de hub).
- [ ] **§0-repaso klopt met de vorige unit** (haal enkel op wat écht is aangeleerd — verifieer tegen `U<N-1>_bron.md`).
- [ ] LPD-codes ingevuld; eindtaak communicatief.
- [ ] **LEVERING:** PDF **altijd samen met** de bewerkbare `U<N>.html`-laag; alumno-deck als `.pptx`; HTML-hub; motor-spellen. Nooit enkel de platte PDF.
- [ ] Commit + push op de werkbranch; deliver.

---

## 10 · Openstaand / elders

- **Conjugador ~1000 werkwoorden** — een agent breidt `verbos_es.json` uit (frequentielijst + correcte tagging); daarna `gen_conjugador.py` opnieuw draaien.
- **C4 (rood) & C6+ (paars)** — brainstorm in de brainstormchat; bouw in aparte chats.
- **profedeele / arche-ele-links** — auteur levert; komen in de Extra-tab van de hub.
- **AI-tutor (#100)** — online component op een LLM-API; apart te regelen.
