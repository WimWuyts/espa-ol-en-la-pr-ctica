# CLAUDE.md — Proyecto «Español en la práctica» (cursusontwikkeling Spaans)

> Dit bestand is het **projectgeheugen**. Claude leest het bij elke sessie automatisch in.
> Bijwerken mag altijd — gewoon zeggen wat er moet veranderen, of zelf typen (Nederlands is prima).

---

## 1 · Wie & context

- **Auteur/leerkracht:** leraar Spaans, doorstroomfinaliteit (D-finaliteit), België (Vlaanderen), Katholiek Onderwijs Vlaanderen.
- **Richtingen & uren:**
  - **2de graad — 4 Moderne talen:** 1 lesuur/week (50 min).
  - **3de graad — 5 Economie-wetenschappen / Moderne talen:** 1 lesuur/week (50 min).
  - **3de graad — 6 Economie-wetenschappen / Moderne talen:** 1 lesuur/week (50 min).
- **Kernspanning van het project:** veel **zij-instromers** in het 5de jaar → de 5de-cursus moet vanaf nul werken, én de 4de-cursus mag geen leerplandoelen van het 5de "opgebruiken" (anders zitten de eigen leerlingen in het 5de te wachten).

## 2 · Het leerplan (bindend kader)

- **Leerplan:** Spaans **III-Spa-d**, 3de graad D-finaliteit, Katholiek Onderwijs Vlaanderen.
- **Versie:** januari 2024 · **D/2024/13.758/220**. Online fiche: <https://pro.katholiekonderwijs.vlaanderen/iii-spa-d> (login vereist).
- **Bestand in repo:** `00-brondocumenten/leerplan/`.
- **Richtniveau (ERK):** **A2** als richtsnoer over de **hele 3de graad** (4 graaduren = 5de + 6de samen). Het generieke leerplan "Vierde vreemde taal" mikt op A1+; Spaans ligt dus ietsje hoger.
- **Uitgangspunt leerplan:** Spaans is **nieuw** in de 3de graad, **geen voorkennis** verondersteld (heterogene beginsituatie is normaal).
- **Vier componenten:** (1) Communicatie — receptief/productief/interactief, mondeling + schriftelijk · (2) Identiteit in diversiteit · (3) Literatuur · (4) Taalsysteem & taalgebruik **ten dienste van** de communicatie (grammatica is functioneel, niet doel op zich).
- **Harde scope-grens (uit de outlines, conform leerplan):** **géén** futuro simple, **géén** condicional, **géén** subjuntivo — ook niet in het 6de. "Aanzet B1" = A2 stevig consolideren, niet nieuwe wijs/tijd introduceren.

## 3 · De vier cursussen

**De namen liggen vast (auteur 2026-08-02).** Ze horen zo geschreven te worden
in álle formaten, de website en de communicatie:

| Code | **Naam** | Jaar / doelgroep | Rol | Niveau | Kleur |
|------|----------|------------------|-----|--------|-------|
| **C4** | **¡Bienvenidos al español!** | 4 Moderne talen | **buiten** leerplan, videogedreven introductie | pre-A1 → A1-mechaniek | **Rood** |
| **C5** | **Español en la práctica** | 5de jaar | Kerncursus, **volgt leerplan** | A1-kern + eerste A2 | **Groen** |
| **C6** | **Más español en la práctica** | 6de jaar (nieuwe cohorte) | «Clean» vervolg op C5, **volgt leerplan** | A2 → aanzet B1 | **Blauw** |
| **C6+** | **Más español en la práctica · edición única** | 6de jaar (huidige cohorte) | Vervolg op de óude cursus — vult hiaten, haalt outlines 5 & 6 alsnog binnen | A2 → aanzet B1 | **Paars** |

**Twee schrijfwijzen voor C4, bewust:** `¡Bienvenidos al español!` waar de naam
zelfstandig staat (titelpagina, website, portaal), en `«Bienvenidos al español»`
binnen lopende tekst en als naam van de fictieve *academia* in de cursus — een
uitroepteken tussen guillemets leest zwaar.

**C6+ heet «edición única»** omdat die cursus één keer gegeven wordt, voor de
huidige zesdes: zij komen uit de oude cursus en krijgen een eenmalig traject dat
de hiaten opvult. Het is een bijzondere editie, geen mindere versie — vandaar
*única* en niet *especial* of *puente*.

> **Let op — één woord, twee betekenissen.** *Español en la práctica* is de naam
> van **C5**, maar in `00-brondocumenten/` verwijst diezelfde titel naar de
> **óude cursus** van de auteur (de bron voor de gap-analyse van C6+). Die
> mappen zijn daarom bij het hernoemen bewust niet aangeraakt.

### C4 — «¡Bienvenidos al español!» (4 MT)
- **Bron:** 14 videolessen (Vimeo-downloads, in `00-brondocumenten/videos-jaar4/`). Video's zijn de **leidraad**.
- **Doel:** communicatieve **chunks**, **uitspraak- en accentregels**, **basiswoordenschat**. Grammatica **louter functioneel**.
- **Ontwerpprincipe (belangrijk):** leer vooral **automatismen/meta-vaardigheden** aan (klank–schriftbeeld, accent, hoogfrequente chunks, luister-/leerstrategieën) die het 5de **versnellen** zonder de leerplan-*inhoud* van het 5de formeel af te vinken. Zo krijgt de eigen 4de-leerling een **voorsprong in de mechaniek**, terwijl de leerplanstof in het 5de voor iedereen (ook zij-instromers) nieuw blijft.
- **Overlap met C5:** bewust **zo klein mogelijk** houden. Bij twijfel: een thema/functie wél aanraken in C4, maar de leerplandoel-afvinking in C5 laten.
- **LEERDOELEN & EVALUATIE (BINDEND, vervangt het ontbrekende leerplan):** `01-cursussen/04-welcome/C4_LEERDOELEN_EVALUATIE.md` (+ PDF in `03-build/web/print/`). Bevat de can-do's met **doelcodes** (`C4-MEC/STR/LU/LE/SP/GE/SC/WS/TS/CU/AT`), de 14-thema-tabel, de **toetsmatrix + rubrics**, en de harde **C5-afbakening** (géén vervoeging-als-systeem, géén verleden/futuro/condicional/subjuntivo). **Zet de doelcodes op de docentenpagina van elke unit** (zoals LPD's in C5), niet op de leerlingpagina.
- **BLADSPIEGEL C4 (BESLIST 2026-07-26):** §14 blijft strikt — **elke hoofdsectie start op een nieuwe bladzijde** — én §13 «geen halflege pagina's» geldt onverkort. Verzoening voor de lichtere C4: **elke sectie wordt verríjkt tot ze een volle bladzijde vult** (min. ~90 % bladvulling; geen sectie op 30–50 %). Verrijken = échte, nuttige inhoud toevoegen (extra oefening met antwoordruimte, model-dialoog, noticing-kader, cognaten-warm-up, luistertaak, mini-auto-test…), nooit opvulling. **Meet elke print-unit** (sectiehoogte t.o.v. ~273 mm A4-bladhoogte) vóór levering. Geldt voor **PDF én Word**.
- **SPREIDING & VARIATIE — reservoirsysteem C4 (BINDEND):** `01-cursussen/04-welcome/reservoir/` — zelfde reservoir-pool als C5 (453 items) met een **C4-filter** (systeem-grammaticaitems = ✗ → C5). Drie documenten: **`C4_coverage.md`** (dekkings-grootboek reservoir×14 thema's + **uitspraak-spreidingsmatrix A** (klanken verdeeld over U1–U14) + **chunk-recycling matrix B**), **`C4_reservoir_index.md`** (de plukvijver + 7 spreidingsregels), **`C4_cocktail_TEMPLATE.md`** (+ `U<N>_cocktail.md` per unit). **Bij elke nieuwe unit: eerst de cocktail invullen (nieuwe IDs, matrix A+B), na de build `C4_coverage.md` bijwerken.**

### C5 — «Español en la práctica», kerncursus (5de) → `00-brondocumenten/outlines/Outline_Jaar5*.md`
- 9 unidades (U0 ¡Empezamos! → U8 ¿Qué has hecho?). Mascotte **Solecito**.
- Streefniveau: **A1-kern + eerste A2-structuren** (t.e.m. perfecto compuesto).

### C6 — «Más español en la práctica» (6de, clean) → `00-brondocumenten/outlines/Outline_Jaar6*.md`
- 9 unidades (U0 ¡De vuelta! → U8 Nuestro mundo). Bouwt door op C5.
- Nieuw in C6: indefinido · imperfecto · contrast · por/para · volledig pronomensysteem · comparativos + betrekkelijke bijzin *que* · imperativo · mening met **indicativo**.

### C6+ — «Más español en la práctica · edición única» (6de, huidige cohorte)
- **De moeilijkste.** Werkwijze: (1) *Español en la práctica* **analyseren** → (2) **gap-analyse** t.o.v. leerplan + outlines 5 & 6 → (3) cursus bouwen die de **hiaten** invult en zoveel mogelijk van beide outlines alsnog aanleert/inoefent.
- **Eindpunt = gelijk aan C6** (A2 → aanzet B1), maar via een ander vertrekpunt.
- Oude cursus komt in `00-brondocumenten/espanol-en-la-practica/`; gap-analyse in `00-brondocumenten/gap-analyse/`.

## 4 · Instructietaal & register

- **Español primero, con apoyo en neerlandés — CONSEQUENT OVERAL.** Álle lopende tekst staat in het **Spaans** met **Nederlandse vertaling/steun** eronder of ernaast — óók de **verbindende verteltekst** (bv. *Este año viajamos de España, cruzando el océano, a México…* + NL-vertaling), de **¡Ojo!/valstrik-kaders** (eerst Spaans, dan Nederlands) en de **grammatica-uitleg** (Spaanse, visuele uitleg + Nederlandse steun). **Nooit een tekstblok enkel in het Nederlands** (enkel korte technische metataal mag NL waar nodig). Glossen/vertalingen kort en herkenbaar.
- **Doelgroep:** tieners (14–18). Toon: warm, motiverend, activerend; leerplan-conform "veilig klimaat, leren uit fouten".
- Vaste valstrikken voor Nederlandstaligen expliciet benoemen (bv. *want* én *omdat* = **porque**; *dus* = **así que / por eso**, niet *luego*).

## 5 · Output & formaten (per cursusonderdeel)

Elke unit/les levert **vier formaten met een identieke, uitgeverswaardige layout**:

1. **Word** (`.docx`) — mooie, professionele layout (voorkeur van de auteur boven kale PDF).
2. **PDF** — zelfde layout, print-klaar.
3. **PowerPoint** (`.pptx`) — zelfde huisstijl, voor klassikaal gebruik.
4. **Interactieve HTML** — standalone; zelfcorrigerende oefeningen, flashcards, audio, ingebedde video.

**Principe: één bron, meerdere formaten.** Content wordt **één keer** gestructureerd geschreven (Markdown/gestructureerde data als bron van waarheid) en daaruit worden de vier formaten gegenereerd, zodat ze consistent blijven.

## 6 · Huisstijl (identiek over álle cursussen)

- **Layout:** doorheen de vier cursussen **≈ identiek** (zelfde sjabloon, zelfde sectie-opbouw), telkens met **één dominante hoofdkleur** per cursus:
  - C4 = **Rood** · C5 = **Groen** · C6 = **Blauw** · C6+ = **Paars**.
- **Vaste sectiestructuur per unit** (uit de outlines):
  `§0 ¡Ponte al día!` (repaso) → `§1…§N` inhoud → `Taller de lengua` (ortografía + conectoren) → `Cultura` → `Tarea final` (genummerde pasos) → `Repaso` («Lo esencial de un vistazo» + semáforo) → `§V Vocabulario` (tabellen Español · Nederlands · ERK · Ejemplo + oefenladder).
- **Huisstijl-richting (BESLIST 2026-07-25):** we ontwerpen een **nieuwe, frisse, uitgeverswaardige huisstijl van nul** (eigen fonts, eigen beeldtaal/mascotte, eigen componenten). De oude C5-elementen (Fredoka/Nunito, mascotte Solecito, MUNDO-collage, `illus.py`) zijn **referentie, geen verplichting**. Wél behouden: **één gedeeld sjabloon** met per cursus **één dominante hoofdkleur** (C4 rood · C5 groen · C6 blauw · C6+ paars).
- **Tokens (BESLIST 2026-07-25):** `02-huisstijl/tokens/tokens.json` (single source of truth) + `tokens.css`. **Fonts = Richting 1:** koppen **Bricolage Grotesque**, tekst **Inter**, notities **Caveat** (alle SIL OFL 1.1, ingebed in álle formaten). **Kleurenpalet goedgekeurd:** vier cursuskleuren als één familie + warme neutralen. Fonts lokaal in `02-huisstijl/fonts/`.
- **Bindende ontwerpspecs (zie §13):** `02-huisstijl/richtlijnen/VISUEEL_ONTWERPSYSTEEM_HUISSTIJL.md` + `VISUELE_WOORDENSCHAT_EN_GRAMMATICA.md`. **Gouden regel: variatie.**

## 7 · Repo-structuur

```
/CLAUDE.md                     ← dit bestand (projectgeheugen)
/README.md                     ← korte projectuitleg
/00-brondocumenten/            ← ALLE bronmateriaal (niet in de chat, wél hier)
    leerplan/                  ← III-Spa-d (docx/pdf)
    outlines/                  ← leerlijnen jaar 5 & 6
    espanol-en-la-practica/    ← de oude cursus (voor C6+)
    gap-analyse/               ← analyse oud vs. leerplan/outlines
    videos-jaar4/              ← 14 Vimeo-downloads (leidraad C4)
/01-cursussen/
    04-welcome/                ← C4  (rood)
    05-a1/                     ← C5  (groen)
    06-clean/                  ← C6  (blauw)
    06-vervolg/                ← C6+ (paars)
/02-huisstijl/                 ← gedeelde templates, kleurtokens, fonts, componenten
/03-build/                     ← gegenereerde output (Word/PDF/PPTX/HTML)
/spaans-motor/                 ← gamification-motor (leerstof → offline HTML-spellen)
```

## 8 · Werkwijze (afgesproken volgorde)

1. **Setup** — CLAUDE.md + mappen + brondocumenten (← nu bezig).
2. **Analyse** — leerplan + *Español en la práctica* + outlines → **gap-analyse** (voor C6+).
3. **Golden sample** — **eerst één volledige voorbeeld-unit** in álle formaten (Word/PDF/PPTX/HTML) bouwen en laten goedkeuren, vóór we opschalen. Zo staat de layout/toon vast.
4. **Productie** — cursus per cursus, unit per unit.

## 9 · Bronmateriaal & externe content

- **Bewaren in de repo** (`00-brondocumenten/`), niet in de chat. De repo is blijvend; de chatcontext niet.
- **Materiaal aanleveren — drie kanalen:** (a) **in de repo** committen (documenten, blijvend); (b) **in de chat** uploaden (snel, maar tijdelijk); (c) in een **Google Drive-map** zetten — Claude heeft in dit project toegang tot Google Drive en kan er **rechtstreeks uit lezen**. Een naar Drive gesynchroniseerde map op de pc werkt dus als "gedeelde map".
- **Online materiaal verwerken:** Claude kan pagina's ophalen (WebFetch/WebSearch) en er **eigen** oefeningen op maken. **Auteursrecht:** liever linken + originele afgeleide oefeningen dan letterlijk overnemen.
- **Video's:** in de interactieve HTML native inbedden; in Word/PDF als QR/link.

## 10 · Openstaande beslissingen (bijwerken naarmate ze vastliggen)

- [x] Huisstijl: **nieuwe, frisse, uitgeverswaardige look van nul** (oude Solecito/Fredoka/Nunito niet verplicht). — beslist 2026-07-25
- [x] **Rode draad = «La Ruta»** (doorlopende reis over de kaart van de Spaanstalige wereld; elke unit = een nieuwe *parada*, de kaart groeit mee van C4 → C5 → C6). **C6+** volgt dezelfde route maar pikt op waar *Español en la práctica* eindigde (ná gap-analyse). — beslist 2026-07-25. Uitwerking: zie **§12**.
- [x] Fonts + kleurenpalet vastgelegd als tokens (Richting 1; `02-huisstijl/tokens/`). — beslist 2026-07-25
- [x] Reisgezel-mascotte = **«La mochila viajera»**; de klas kiest de naam. Tekenstijl (AI ↔ vector) nog te bepalen. — 2026-07-25
- [x] Beeld-aanpak: **AI-personages** (cast «Estilo Exploración», via Drive) · AI-foto's · flat-vector iconen/kaarten/mockups (Claude) · SVG→PNG voor print (zie §15). — 2026-07-25 (personages bijgesteld: flat-vector → AI)
- [x] Toolchain voor de "één bron → 4 formaten"-generatie — **VASTGELEGD bij golden sample U0** (zie `HANDOVER_C5_C6.md` §3 + §8). — 2026-07-26
- [x] **Bestaand C5-materiaal (sjbespanol.netlify.app, U0–U6 afgewerkt): geïmporteerd als
  brónmateriaal, niet als cursus.** De bestanden staan in
  `00-brondocumenten/materiales-vorig-project/` (`Unidad_0_v1.pdf`…`Unidad_6_v1.pdf` +
  `index_u0.html`…`index_u6.html`). De keuze was: die zeven units overnemen, of C5 opnieuw
  bouwen in de nieuwe huisstijl. Het is het tweede geworden — C5 U0–U8 zijn van nul
  opgebouwd. Het oude materiaal is wél uitgemijnd en blijft dat doen: de parels
  (`02-huisstijl/reservoir/PARELS_materiales.md`), de woordenschatpool
  (`Cursus_Spaans_Woordenschat_Master_v8.xlsx`) en de emoji-stijl van de flashcards
  (`vocab_emoji.py`). — vastgesteld 2026-08-08, achteraf: de vraag was al beantwoord door
  wat er gebouwd is.

### U5 «¡Ñam!» = GELOCKT (2026-07-26) — norm voor het reservoir/cocktail-tijdperk
U5 is door de auteur goedgekeurd en vastgezet als **referentie-unit voor de nieuwe pijplijn** (na §14ter). Wat U5 vastlegt voor U6–U8 (en de latere U0–U4-tweak): **cocktail-receta → reservoir plukken → coverage bijwerken**; **flashcard-iconen = Materiales-emoji-stijl** (`vocab_emoji.py`); **ruta-kaart discreet** (klein vanaf U1, groot enkel U0); **Cultura verrijkt** (unit-eigen kaarten uit `materiales-vorig-project`, niet enkel de kaart); **HTML-hub ≥100 interactieve oefeningen** met meerdere reeksen per oefening (§14ter); **master-vocab als kandidatenpool**. Niet meer aan U5 raken zonder expliciete vraag.

### GOLDEN SAMPLE U0 = GELOCKT (2026-07-26) → productieregels in `HANDOVER_C5_C6.md`
U0 (C5) is goedgekeurd en vastgezet als norm voor álle volgende units. **Bij automatische generering (U1, U2, … en C6) exact dezelfde parameters/pijplijn hanteren als U0.** De volledige productiehandleiding staat in **`HANDOVER_C5_C6.md`** (lees dit vóór je een unit bouwt). Nieuw gelockte beslissingen deze sessie:
- [x] **4 formaten per unit** = PDF (+ bewerkbare `U<N>.html`-laag) · HTML-hub (bewerkbaar) · PowerPoint 2 decks (docente `.pptx` + alumno `.pptx`) · motor-spellen ingebed in de hub.
- [x] **Bewerkbare laag** (contenteditable + «Opslaan als PDF»/«Bewaar») op PDF-cursus én HTML-hub. — 2026-07-26
- [x] **LEVERING — BINDEND (auteur 2026-07-26):** een PDF wordt **standaard samen met zijn bewerkbare `U<N>.html`-laag** afgeleverd (de PDF zelf is niet bewerkbaar; de HTML-laag is de bewerkbare versie mét «Opslaan als PDF»). Nooit enkel de platte PDF sturen. De HTML-hub is even goed bewerkbaar (breed `contenteditable`-bereik: hero, koppen, inhoudskaarten cultura/extra/lectura).
- [x] **PowerPoint alumno = `.pptx` (NIET `.ppsx`) — BINDEND (auteur 2026-07-26):** het `.ppsx`-slideshow-contenttype wordt door strikte lezers/PowerPoint geweigerd («kan niet worden gelezen»). Lever de leerlingversie als gewone **`.pptx`** (identieke dia's + klik-onthul-animaties; leerling drukt **F5** voor de diavoorstelling). `to_ppsx()` niet meer gebruiken voor levering.
- [x] **PowerPoint = geanimeerd format** (verschijnen-bij-klik via `<p:timing>`). Geen kiosk. 2 decks (docente + alumno, beide `.pptx`). — 2026-07-26
- [x] **De «Repareren»-melding was géén bijwerking van de animaties** (dat stond hier eerder ten onrechte). Oorzaak: `shp.shadow.inherit = False` liet een lege `<a:effectLst/>` achter en `_soft_shadow()` hing er een tweede naast — twee stuks in één `<p:spPr>`, wat het schema verbiedt. De `<p:timing>`-blokken waren altijd al in orde. Opgelost in de elf generatoren; bestaande decks te herstellen met `03-build/pptx/repara_effectlst.py` (werkt op de XML, heeft geen python-pptx nodig). — 2026-08-05
- [x] **Motor-spellen = azulejo-stijl behouden** (contrast, niet omkleuren). — 2026-07-26
- [x] **Audio = browser-TTS** voorlopig (geen eigen opnames). — 2026-07-26 · **VERVANGEN
  2026-08-09:** alle **73 luisterfragmenten zijn ingesproken** met acht Castiliaanse
  stemmen (`voces.py` + `gen_audio_castellano.py`), omgezet naar **MP3** met
  `wav_a_mp3.js` (114 MB → 21 MB, 5,4×) en **ingebakken in de digitale pagina's**
  van alle drie de cursussen (`hub_audio.py`). De browserstem blijft alleen nog
  als terugval waar een opname zou ontbreken.
- [x] **GELUID IN DE PAGINA, NIET ERNAAST (auteur 2026-08-09).** De hubs dragen hun
  eigen audio als data-URL. Reden: een aparte audiomap moet mee geüpload worden én op
  de juiste plaats belanden — vergeet dat en élke luisteroefening valt stil zonder dat
  iemand het merkt; en een leerling die de pagina bewaart, hield een pagina zónder
  geluid over. Kosten: 16 van de 17 C5/C6+-pagina's staan op 2,4–3,3 MB, C5 U0 op
  7,8 MB (tien fragmenten, negen minuten). C4 lag al zo. **Nagerekend in een echte
  browser:** alle geteste fragmenten decoderen met de juiste speelduur.
- [x] **Conjugador = aparte cursus-tool** (`03-build/web/Conjugador.html`), enkel presente, ~1000 werkwoorden (nagerekend via motor-engine), 2 lagen (opzoeken + zelf vervoegen). **Werkwoordsvervoeging hoort NIET in de units.** — 2026-07-26
- [x] **Kaart = échte geografie (Natural Earth), klikbaar in HTML, met vlaggen + landcodes.** — 2026-07-26
- [x] **QR's op print → naar de HTML-hub** (niet rechtstreeks YouTube/PPTX). — 2026-07-26

### C4 IS VOLLEDIG (2026-08-08) — U11–U14 gebouwd, alles in één bouwketen
De veertien thema's staan er. Wat er deze ronde bijkwam en veranderde:
- [x] **C4 draait mee in `03-build/construir.py`** — onderdelen → hub → print → cijfers →
  bouwtaal → Lucide → bladspiegel → PDF → bladzijdenummers + bladwijzers. Het thema per
  unit (voor de banda sonora) staat nu in `C4_TEMA` in dat script i.p.v. in hand-getypte
  regels. De unitlijst van álle drie de cursussen staat op één plaats: `enlaces.unidades()`.
- [x] **QR-codes echt** — ze wezen naar het verzonnen `hablacon-ene.local`; nu naar de
  gehoste hub + het juiste tabblad, via `enlaces.py`. `segno` bestaat hier niet: ze draaien
  op onze eigen encoder (`qr_codigo.py`), dezelfde als C5/C6+. **100 codes in de repo,
  98 naar een specifieke oefening.**
- [x] **Luisterfragmenten ingesproken** — `comprension_data.AUDIO` (10 dialogen, U1–U10) en
  `escena_data.py` (4 scènes, U11–U14) met de acht Castiliaanse stemmen. Ingebed als
  data-URL, want de C4-hub moet standalone blijven. **De sitcom-transcripten blijven bij de
  video**: echte acteurs vervang je niet door synthese.
- [x] **U11–U14: video's én transcripten binnen** (auteur 2026-08-09). De vier
  afleveringen staan in Google Drive en zijn **ingebouwd** — zelfde `/preview`-kader
  als U8–U10, met zichtbare terugvallink. Deelrechten nagekeken: alle vier `role=reader /
  type=anyone`. De ID's staan in **`escena_data.VIDEO`**. De transcripten volgden
  dezelfde dag; de vier units draaien nu op de échte tekst.
  **Aflevering 15 bestaat ook** (`1OMxB9gRZ9LdYYDGOl5_JiiGEAkXPsxfi`) maar C4 heeft
  veertien thema's, dus die blijft ongebruikt.
- [x] **DE VIDEO IS DE LEIDRAAD — vier thema's bijgesteld (2026-08-09).** De
  oorspronkelijke themalijst bleek bij álle vier de laatste afleveringen iets anders te
  voorspellen dan er in beeld gezegd wordt. Nu: **U11 el tiempo** (was «ropa») ·
  **U12 la ropa y los colores** (was «tiempo») · **U13 en el mercado** (was «hotel») ·
  **U14 en el restaurante** (was «repaso»). Woordenschat, grammatica, oefeningen,
  cultura, banda sonora, leestekst, luisterfragment, eindtaak en de funciones-matrix zijn
  meeverhuisd. Wat níet meeschoof is de **klankfocus** (matrix A): die ligt vast zodat
  elke klank precies één keer aan de beurt komt — alleen de voorbeeldwoorden komen nu uit
  de nieuwe scène. **Er is geen hotelunit meer**; `F26` is daarom uit de functielijst
  gehaald (reserveren komt in C5 terug) en `F23` (winkelen) is uit de parkeerstand: intro
  in U12 (talla/precio), uptrade in U13 (kilo/oferta). Nieuw: `F29` rutina · `F30` razón ·
  `F31` restaurante · `F32` acuerdo · `F33` valorar.
- [x] **Sprekerslabels hersteld in aflevering 11 en 13.** In de aangeleverde transcripten
  stonden regels op de verkeerde naam. Bij 11 bevestigde de auteur dat (de ober troost
  Julio, niet omgekeerd); bij 13 wees het bewijs in de tekst zelf op dezelfde
  verschuiving — María zegt daar «no soy vegetariano» — en is ze op dezelfde manier
  hersteld. Beide staan gedocumenteerd in de kop van `escena_data.py`.
- [x] **Géén ingesproken scène meer waar er een video is.** Zolang het transcript
  ontbrak werd de eigen scène gesynthetiseerd; nu de aflevering er is, ís de video de
  opname — echte acteurs vervang je niet. `gen_audio_castellano.fragmentos()` slaat units
  in `escena_data.VIDEO` over, net als `gen_c4_escena.audio_datos()`. Het enige
  gesynthetiseerde fragment per unit is dat bij de leestekst.
- [x] **U14 sluit het jaar af.** De laatste unit heeft een slotbladzijde
  (`gen_c4_pdf.cierre()`): de veertien parada's met per parada één can-do en een semáforo,
  een «¿Y ahora?»-brug naar C5 en «mi frase del año». Alleen `max(PORTADA)` krijgt ze.
- [x] **Gedeelde generatoren voor U11–U14**: `gen_c4_escena.py` · `gen_c4_kit.py` ·
  `gen_c4_practica.py` · `gen_c4_hub.py` · `gen_c4_pdf.py`, gevoed uit `escena_data.py` en
  `kit_data.py`. Vier bijna-identieke kopieën zouden vier plaatsen opleveren waar een
  verbetering apart moet.
- [x] **BLADSPIEGEL — U11–U14 wijken bewust af.** De C4-regel («elke sectie een blad,
  verrijkt tot ze het vult») werkt in U1–U10 omdat die secties met de hand op maat zijn
  gemaakt. Gegenereerde secties hebben wisselende lengte, en elke gedwongen breuk kostte
  gemeten een halve bladzijde (81–83 % vulling). Nu opent alléén de scène een nieuw blad;
  de rest vloeit door. **Resultaat: 11 bladzijden per unit, 89–91 % — gelijk aan U1–U10.**
- [x] **Bladspiegel-nabewerking respecteert C4**: `bladspiegel.py` zet in C4 géén `major`
  meer, want de generator beslist dat zelf. Het legt er alleen de ankers voor de bladwijzers.
- [x] **PowerPoints U11–U14 (2026-08-09).** `python-pptx` staat niet meer in de bouwomgeving
  en PyPI is geblokkeerd, dus die weg is dicht. `03-build/pptx/gen_c4_ppt.cjs` bouwt ze met
  **pptxgenjs** (via `git clone`, want npm is óók dicht) — een .pptx is een zip met XML, en
  welke taal die schrijft maakt het bestand niets uit. Docente 17 dia's, alumno 15 (zonder
  de oplossingsdia's). Gevoed uit dezelfde gegevens als hub en print. **Beperking:
  LibreOffice kan in deze sandbox géén enkele .pptx openen** — ook de eerder met python-pptx
  gebouwde niet — dus ze zijn structureel nagerekend (zip, XML, alle verwijzingen) en op
  inhoud, niet visueel gerenderd.
- [x] **C4 IS COMPLEET: 14 units × 4 formaten** — print-PDF · digitale hub · PowerPoint
  (docente + alumno) · ingesproken audio.

### GOLDEN SAMPLE C4 · U1 «Presentaciones» = GELOCKT (2026-07-26) → productieregels in `HANDOVER_C4.md`
U1 (C4) is goedgekeurd en vastgezet als norm voor álle C4-units (U2–U14). **Bij het bouwen van U2… exact dezelfde parameters/pijplijn als U1.** Volledige handleiding: **`HANDOVER_C4.md`** (lees dit vóór je een C4-unit bouwt). Gelockt voor C4:
- [x] **4 formaten** = HTML-hub (tabbladen, srcdoc-iframes, offline) · print-PDF (+ bewerkbare `U<N>.html`-laag/editbar) · PowerPoint 2 decks (docente `.pptx` + alumno `.ppsx`, geanimeerd) · muziek-/motor-componenten. **Print-formaat = PDF** (Word bouwbaar maar in sandbox niet te renderen → PDF primeert, §18).
- [x] **Bladspiegel C4 = elke sectie verrijkt tot volle pagina** (§13/§14-verzoening; **meet elke unit**, streef 85–99 % vulling, géén 30–50 %-pagina's).
- [x] **Uitspraaklaag «Suena bien» in elke unit** volgens **matrix A** (`C4_coverage.md`): één klankfocus + acentuación per unit, telkens andere werkvorm.
- [x] **Video** = YouTube-embed (`youtube-nocookie`) met juiste `allow`-permissies (ook gedelegeerd in de hub-iframe) + zichtbare fallback-link.
- [x] **Reservoir/cocktail-workflow** (`01-cursussen/04-welcome/reservoir/`): eerst `U<N>_cocktail.md` invullen (nieuwe IDs + matrix A+B), na de build coverage bijwerken.
- [x] **Geen bouw-jargon/metaberichten op de leerlingpagina's.**
- [x] **Doelcodes** (uit `C4_LEERDOELEN_EVALUATIE.md`) op de **docentenpagina** van elke unit.
- [~] **Funciones-comunicativas-laag (PROTOTYPE, ter validatie 2026-07-27):** een doorlopende,
  gráduaal groeiende ruggengraat van communicatieve functies, vertrekkend uit de sitcom-fragmenten.
  = **matrix C** naast matrix A (klanken) en B (chunks). Bron: `03-build/web/funciones_data.py`
  (catalogus F01–F08 + noticing per unit + eindtaak-tags) → component `gen_c4_funciones.py` →
  tab «🗣️ Funciones» in elke hub (video-noticing «¿Qué hacen con el idioma?» + cumulatief banco met
  exponentes-per-unit + semáforo + «esta unidad añade» nieuw/nivel+). Docentdossier + matrix C:
  `01-cursussen/04-welcome/reservoir/C4_funciones_matrix.md`. Retroactief op U1–U3. **Nog te
  bevestigen:** ook in print («Lo que ya sé decir»-spiekkaart) + PPT (funciones-dia), en doortrekken U4+.

## 11 · Git & werkafspraken

- **Werkbranch:** `claude/spanish-course-development-jx25ay`. Niet naar een andere branch pushen zonder toestemming.
- Commit-berichten: kort en beschrijvend, in het Nederlands.
- Alle vier de cursussen leven in **deze** ene repo (monorepo), gedeelde huisstijl in `02-huisstijl/`.

## 12 · De rode draad — «La Ruta» (verhaallijn over alle cursussen)

**Concept:** één doorlopende **reis over de kaart van de Spaanstalige wereld**. Elke unit is een nieuwe **parada** (halte/etappe); een groeiende **mapa de la ruta** verbindt de units, de jaren én de cursussen. De kaart is het vaste visuele anker (hero + terugkerend element in elke unit) en vervangt de oude MUNDO-collage van C5.

**Waarom deze:** sluit naadloos aan bij de outlines (reizen, cultura, biografieën, leyendas, de Spaanstalige wereld), draagt de leerplan-component *Identiteit in diversiteit*, en de niveaugroei zit al ingebakken in de route.

**Route per cursus (etappes):**

| Cursus | Etappe-naam (werktitel) | Wereld-focus | Taal-/niveaulaag |
|--------|-------------------------|--------------|------------------|
| **C4** 🔴 | *El despegue* — vertrek & eerste contact | "leren klinken als": klanken, accent, chunks | pre-A1 mechaniek (afhankelijk van de video's) |
| **C5** 🟢 | *El día a día* — settelen, het hier-en-nu | Spanje + eerste stappen LatAm; dagelijks leven | A1-kern + eerste A2 (t.e.m. perfecto compuesto) |
| **C6** 🔵 | *Historias y mundos* — dieper & het verleden in | breder LatAm; verhalen, geschiedenis, actualiteit | A2 → aanzet B1 (indefinido/imperfecto passen bij verhalen) |
| **C6+** 🟣 | dezelfde route, **ander vertrekpunt** | pikt op waar *Español en la práctica* eindigde | A2 → aanzet B1 (na gap-analyse) |

**Mechaniek per unit:** elke unit opent met "waar zijn we op de ruta" (kaartje + bestemming), de `Cultura`-sectie verankert de *parada* in een echte plek/land, en de `Tarea final` is telkens een concreet reis-artefact (postal, reisblog, vlog, presentatie…). Zo is de reis niet enkel decor, maar ook de motor van de eindtaken.

### C5 «El día a día» — de paradas (VASTGELEGD 2026-07-25)

Boog: **España (U0–U4) → «el charco» → México (U5–U6) → Colombia (U7) → Perú (U8)**.

| Unit | Parada | Tarea final |
|---|---|---|
| U0 ¡Empezamos! | *El mundo hispano* → **España** | Tarjeta de embarque |
| U1 ¿Quién eres? | **Madrid** | Mi pasaporte |
| U2 Mi gente | **Andalucía (Sevilla)** | Álbum de familia |
| U3 El tiempo vuela | **Barcelona** | Un día en mi vida |
| U4 Me gusta | **València / la costa** | Mi playlist |
| U5 ¡Ñam! | **México (CDMX)** | La carta |
| U6 De tiendas | **México — mercados** | Abre tu tienda |
| U7 Mi casa y mi barrio | **Colombia (Cartagena)** | Mapa de mi barrio |
| U8 ¿Qué has hecho? | **Perú (Cusco · Machu Picchu)** | Diario de viaje |

### C6 «Historias y mundos» — paradas (provisoir)

Argentina/Buenos Aires (U1) · leyenda Meso-Amerika (U2) · Chile/Patagonia (U3) · España/Cuba (U4) · dos ciudades (U5) · digitaal/pan-hispano (U6) · Costa Rica (U7) · Amazonía/globaal (U8). **C4** = de vertrekhal vóór de reis (definitief ná de video's).

**Kaarten (BINDEND):** de *mapa de la ruta* is het vaste visuele anker en wordt **prachtig gerenderd** — een eigen, verzorgde SVG-kaartstijl (geen generieke clipart of ruwe outline-maps). Elke unit opent met "waar zijn we op de ruta" (kaartje + bestemming); de kaart groeit mee van C4 → C5 → C6.

### De cast — «la gente de la ruta» (VASTGELEGD 2026-07-25, namen provisoir)

Kerncast van 4 tieners **+ de reiziger = de leerling** (Vlaams «tú»-perspectief → draagt de NL-valstrikken):
- **Lucía** — Sevilla 🇪🇸 (familie/U2 · andaluz)
- **Diego** — CDMX 🇲🇽 (eten & markt/U5–U6 · mexicano)
- **Valen** (Valentina) — Cartagena 🇨🇴 (wonen & barrio/U7 · costeño)
- **Nina** — Cusco 🇵🇪 (reizen & natuur/U8 · andino)
- **Mateo** — Buenos Aires 🇦🇷 (**vanaf C6**: biografieën · voseo)

Fictieve namen (echte figuren zoals Frida/García Márquez blijven voor *Cultura*). Elk personage = eigen **avatar-accentkleur**, geharmoniseerd met het palet en bewust **losgekoppeld** van de functionele taalkleuren én de cursuskleur. Elke *parada* kan zijn lokale castlid als gastheer hebben.

**Nog te beslissen:** de **mascotte** (reisgezel) — richting «gekoppeld aan de leerling» (nu in bespreking).

## 13 · Ontwerpsysteem & componenten (BINDEND)

De volledige visuele aanpak ligt vast in twee specs in `02-huisstijl/richtlijnen/`:
- **`VISUEEL_ONTWERPSYSTEEM_HUISSTIJL.md`** — het uitgeefsysteem: paginatypes, grid, navigatie (tabs/kop-voet/sectielabels), iconen, beeldbibliotheek, pagina-composities (A–H), micro-elementen, componentenbibliotheek, technische exportregels, visuele audit, bouwvolgorde.
- **`VISUELE_WOORDENSCHAT_EN_GRAMMATICA.md`** — hoe woordenschat en grammatica worden gepresenteerd (elk ~20–35 visuele patronen + herbruikbare componenten + dubbele-pagina-blueprints).

**Reikwijdte (belangrijk):** deze principes gelden voor **álle vier de cursussen** (C4·C5·C6·C6+) én voor **álle formaten** binnen elke cursus: **Word, PDF, PowerPoint en HTML** (+ latere digitale varianten). Specifieke richtlijnen voor de webpagina's/digitale varianten volgen **later**.

**Kernafspraken die elke build moet respecteren:**
- **Gouden regel = VARIATIE.** Geen Word-uitstraling, geen opeenvolgende tekstblokken, geen rij identieke kaders, geen uniforme pagina's. Samenhang komt uit het *designsysteem*, niet uit identieke lay-outs.
- **Beeld = iconen + foto's gecombineerd** (afgesproken): hedendaagse stedelijke fotografie + terugkerende personages/uitsnedes + één consistente lijniconenset. Geen clipart/emoji/3D-mix.
- **Woordenschat** = visueel netwerk (scène, clusters, chips, collocaties, families, communicatieve toepassing) — **nooit** enkel een tweetalige lijst.
- **Grammatica-route:** context → observeren → patroon herkennen → compacte regel → gecontroleerd oefenen → communiceren. **Nooit** enkel een grote tabel; elke grammaticaspread eindigt communicatief.
- **Twee kleurlagen, allebei consequent:** (1) **cursus-/unitkleur** voor navigatie & huisstijl (C4 rood · C5 groen · C6 blauw · C6+ paars); (2) **functionele kleursemantiek** voor taal (blauw=onderwerp/persoon · oranje=werkwoord · groen=voorwerp · paars=tijd · turquoise=plaats · rood=ontkenning/waarschuwing · geel=strategie). Kleur is nooit de énige informatiedrager (ook label/vorm/icoon).
- **Print én digitaal uit één bron.** Print moet volledig bruikbaar zijn zónder interactie; toegankelijkheid (alt-tekst, contrast, grijswaarden) is vereist.
- **Build-hygiëne (BINDEND, uit U0-audit 2026-07-26):** (1) **geen sectiekop onderaan een pagina** (weesregel: kop blijft bij zijn tekst) · (2) **alle formaten printbaar** (kleuren printen, veilige marges, geen afgesneden content over paginagrenzen) · (3) **niet te dicht** — adem zoals de opener, witruimte is bewust · (4) **visuele variatie via micro-elementen** (nummerbadges, tijd-/werkvormlabels, moeilijkheidssterren, QR-audiokaart, personage-als-gids, sectiescheiders) i.p.v. rijen identieke blokken — zie `02-huisstijl/richtlijnen/50_VISUELE_LAYOUTELEMENTEN.md` · (5) **geen bouw-jargon op de leerlingpagina** (Engelse componentnamen enkel in broncode/docentendossier).
- **Bladspiegel (BINDEND):** de te vermijden fout is een **bladvullende decoratieve rand/kader met een halflege pagina erbinnen** (mooi bedoelde omranding rond het hele blad, daarbinnen een halve pagina leeg — en dat telkens opnieuw). **Vul de bladspiegel efficiënt:** content loopt door tot de pagina goed en evenwichtig gevuld is, zónder te overladen. **Variërende composities** (nooit 2× dezelfde paginavorm). Witruimte is een **bewuste** ontwerpkeuze, nooit restruimte binnen een lege omranding. Functionele componenten (chat, clusters, kaarten) mogen wél — de pagina zélf is geen grote lege kader. Geen halflege pagina's, geen uniforme herhaling.
- **Bouwvolgorde (uit de spec):** designsysteem → kleur → typografie → grid → navigatie → iconen → **componentenbibliotheek** → paginatemplates → **één prototype-unit** → PDF-export → **visuele audit** → correctie → **pas dán** productie van de rest. = onze «golden sample»-stap.
- **Rolverdeling:** Claude + latere **subagents** beslissen de concrete invulling per onderdeel per cursus, binnen deze specs. Bij twijfel wint *variatie* + de visuele audit uit de spec.

## 14 · Didactieksysteem (BINDEND)

Naast de twee *visuele* specs (§13) zijn er twee *didactische* specs in `02-huisstijl/richtlijnen/`:
- **`VIER_VAARDIGHEDEN_GEINTEGREERD.md`** — hoe lezen · luisteren · schrijven · spreken worden **aangebracht én ingeoefend**; geïntegreerde vaardigheidsketens; interactieve HTML-spreekcomponenten.
- **`INOEFENEN_WOORDENSCHAT_GRAMMATICA_100_WERKVORMEN.md`** — 50 + 50 werkvormen van **receptief → productief** + zeven ontwerpregels.

**Reikwijdte:** idem §13 — alle vier cursussen, alle vier formaten. **Variatie** geldt óók in Word/PDF, niet enkel in HTML.

**Kernafspraken die elke build moet respecteren:**
- **Vaardigheidsbeweging (elke skill):** oriënteren → receptief verwerken → gericht analyseren → gestuurd reageren → zelfstandig produceren → transfer → feedback & herneming.
- **Woordenschat & grammatica — vijf fasen:** herkennen → onderscheiden → ophalen → gestuurd produceren → vrij produceren. **Retrieval vóór herlezen.**
- **Steun altijd zichtbaar afbouwen:** model → woordenbank → beginletters/zinsframe → inhoudelijke cue → geen steun. (Een oefening is pas productief als het antwoord niet volledig te kopiëren valt.)
- **Betekenis vóór vorm · productie begint klein · ophalen vóór opnieuw tonen · feedback leidt tot nieuwe productie.**
- **Spreiding & recycling verplicht:** een woord/structuur keert later terug — in een andere vaardigheid, met een ander personage, in een nieuwe tekstsoort, zonder waarschuwing.
- **Vaardigheden zijn geïntegreerd** (8 ketens: lezen→spreken, luisteren→schrijven, … → volledige eindtaak). Niet vier gescheiden hoofdstukken.
- **Receptieve vs. productieve beheersing apart** (statusladder 0–5).
- **Elke eindtaak is communicatief:** afzender · ontvanger · doel · situatie · resultaat. Nooit "gebruik 10 woorden en 5 werkwoorden".
- **Spreken = ook interactie** (beurt nemen, verduidelijken, zichzelf herstellen). Veel spreekwerkvormen worden interactieve HTML-componenten (recorder, shadowing, info-gap, vertakkende dialoog…); **print blijft volledig bruikbaar zónder interactie**.
- **Gedeelde componentensets:** de componentlijsten uit álle vier de specs (visueel + didactisch) vormen samen één bibliotheek, één keer te bouwen bij de golden sample.
- **ANTWOORDRUIMTE — BINDEND (auteur 2026-07-26):** élke goede oefening krijgt **voldoende, type-correcte schrijfruimte** in het boek; de leerling schrijft écht op papier. **Nooit oplossingen/antwoordsleutels op de leerlingpagina** (die horen in het docentendossier + de HTML-zelfcorrectie). Notatiewijze per oefentype:
  - *Classificeren/sorteren* → schrijf-kolommen (`.wcols`) met kop per categorie + geruite vlakken + rij «je eigen woord».
  - *Invullen in woord/zin (gap-fill)* → schrijflijn (`.wl`) op de juiste plek, lengte ~ verwacht antwoord.
  - *Woorden/zinnen schrijven, dictee, reconstrueren* → genummerde regels, elk een `.wl full`/`.wl lg` (één per item).
  - *Tabel invullen* → `.wtab` met hoge rijen + `.wl` per cel.
  - *Meerkeuze / markeer wat je hoort* → ☐-vakjes per optie + korte `.wl` om te noteren/verbeteren.
  - *Vrije productie (voorstellen, mini-tekst, eigen zin)* → geruit schrijfvlak (`.wbox`), maat naar lengte.
  - *Transformeren/herschrijven* → gegeven → `.wl` voor de herschrijving (twee kolommen of regel-per-regel).
  - *Spreken/interactie (paar)* → notitielijn(en) voor eigen antwoord/afspraak + ☐ «gedaan», of een mini-invulframe; print blijft bruikbaar zónder opname.
- **Paginaovergangen — BINDEND (auteur 2026-07-26, HERZIEN NA METING 2026-08-08):**
  de oorspronkelijke regel «élke hoofdsectie start op een nieuwe bladzijde»
  (`.sec{break-before:page}`) botste frontaal met de bladspiegelregel hieronder,
  en de meting wees uit dat zíj de hoofdschuldige was: over de zeventien units
  stond **198 van de 856 bladzijden halfleeg** (in C6+ U1 één op de drie), en de
  gemiddelde vulling was 76 %. Een sectie van vier regels kreeg een eigen blad.
  **De regel nu:** een nieuwe bladzijde is voor de **mijlpalen** — Taller de
  lengua, Cultura, Tarea final, Repaso en §V Vocabulario (`.sec.major`). De
  genummerde inhoudssecties **vloeien door** en worden herkenbaar gemaakt door
  hun bovenmarge en de gekleurde parada-lijn; §0 ¡Ponte al día! sluit aan op de
  opener, samen precies één bladzijde. Onveranderd blijft: **geen sectiekop
  onderaan** (`.sec{break-inside:avoid;break-after:avoid}` — het sec-blok is
  alleen de kop) en **geen kader/tabel doorgesneden of «ghost»** over de
  paginagrens. Nieuw: `break-inside:avoid` geldt **alleen voor blokken die op
  een blad passen** — op een blok van 300–500 mm levert het een lege bladzijde
  óf een snee op; grote blokken (`.act`, `.reto`, `.lectura`, `table`) breken
  met `box-decoration-break:clone`, zodat beide helften hun volledige omranding
  houden. **Al het breukgedrag staat op één plaats**
  (`02-huisstijl/templates/cursus-print.css`, blok `@bladspiegel`); generatoren
  mogen die selectoren niet overschrijven. Nabewerking + meting:
  `03-build/web/bladspiegel.py` en `03-build/medir_bladspiegel.py`.
  **Resultaat: 856 → 721 bladzijden, vulling 76 % → 87 %, halflege bladzijden
  198 → 56.**
- **OEFENDICHTHEID — BINDEND (auteur 2026-07-26, na U0↔U1-vergelijking):** élke unit haalt de **dichtheid van de golden sample U0** (≈50 p print · ≈45–50 oefeningen). Dit is de norm voor **álle** units en **álle** formaten, telkens met **unit-eigen mechanismen en visuals** (geen kopie van U0's fonetiek-oefeningen, wél hetzelfde *niveau*). Concreet, per unit:
  - **Fijnmazige leercyclus per kernpunt:** splits elke grammatica-/woordenschatstap in **§x.1/§x.2/§x.3** met de volle route *context → observeren → patroon → compacte regla → oefenen (steun afbouwt) → communiceren* (niet één regla + 2 oefeningen).
  - **≈4 oefeningen per subsectie**, geordend over de **vijf fasen** (herkennen → onderscheiden → ophalen → gestuurd produceren → vrij produceren), elk met expliciet **steunniveau** (MODELO → BANCO → MARCO/LETRA → PISTA → SIN AYUDA).
  - **Eén «Tarea comunicativa» ná élke hoofdsectie** (afzender·ontvanger·doel·situatie·resultaat) — bovenop de eind-Tarea.
  - **Volle antwoordruimte-set** (§14-notatie): `wcols` (sorteer/classificeer-schrijfkolommen), `wbox` (geruit schrijfvlak), `wl`/`wl full/lg/md/sm`, `wtab`. Nooit enkel losse schrijflijnen.
  - **Rijk beeld ín de secties** (niet enkel de opener): gelabelde scène/ficha·carné, chat-/mockup-bubbels, personage-kaarten, substitutietabel, transformatieketting, overeenkomst-pijlen, beslisboom, país-cluster, semantische ladder — kies per unit uit `VISUELE_WOORDENSCHAT_EN_GRAMMATICA.md`.
  - **VISUEEL-EERST — BINDEND (auteur 2026-07-26, ronde 3):** grammatica en woordenschat worden **NOOIT** als «tekstblok + regla-tabel + rij invuloefeningen» aangeboden. **Grammatica = visueel proces:** context → *observatie-kader* met gemarkeerd patroon → visuele component (**werkwoord-machine** infinitivo→raíz→terminación→forma · **bouwstroken** · **overeenkomst-kaart** · **beslisboom** · **vraag-antwoord-spiegel** · **vorm-betekenis-gebruik-kaart** · **zichtbare steiger** modelo→marco→clave→solo · **zoom** un/el · **röntgen** van een zin) → compacte regla → oefenen → communiceren. **Woordenschat = visueel netwerk:** gelabelde scène/ficha · **clusters** · **collocaties** · **woordfamilies** · **semantische ladders** · **tegenstellingsparen** · **«Mis palabras»** (persoonlijk vak). Componentnamen: zie `VISUELE_WOORDENSCHAT_EN_GRAMMATICA.md` (GrammarMachine/BuildingBlocks/AgreementMap/DecisionTree/QuestionMirror/FormMeaningUse/Scaffold/Zoom + VocabularyCluster/Collocation/Family/Scale/Pair/PersonalList). Herbruikbare CSS/helpers staan in `gen_u1_print.py` — hergebruik en breid uit per unit.
  - **GEEN echt lege pagina's — BINDEND:** meet na de build de vulling per pagina; een sectie-slotblok (guide/verwijzing) mag **nooit** alleen op een pagina spillen. Los op met extra oefeningen én een **mee-vloeiende** online-verwijzing (`.route-note`, niet `break-inside:avoid`), niet met een los `guide`-kader op het einde.
  - **Meer audio-QR-luisterkaarten** (meerdere per unit), elk → HTML-hub-anker.
  - **Werkvorm-variatie is verplicht:** put uit de **100 werkvormen** (`INOEFENEN_…100_WERKVORMEN.md`); **geen werkvorm twee keer** binnen een unit met dezelfde jas.
  - **§V Vocabulario** krijgt in print grote thematabellen **+ een korte oefenladder** (naast de online-repaso).

## 14bis · Reservoir, variatie & vaardigheden — BINDEND (auteur 2026-07-26, ronde 4)

De vier didactische/visuele specs + de 100 werkvormen + de 25 HTML-grammaticatools + de 50 layout-ideeën + de PowerPoint-50 vormen samen één **reservoir**. **Elke unit combineert bewust verschillende ideeën/werkvormen uit het reservoir (variatie); inoefening staat centraal.** Bindend per unit:
- **Traditionele cloze-werkwoordsoefening (VERPLICHT):** elke unit bevat minstens één klassieke **cloze** waarin de leerling **correcte werkwoordsvormen** invult (gap-fill in zinnen). Vormen nagerekend (motor/generator of geverifieerd).
- **TWEE LECTURA'S PER UNIT, ÉÉN VOLLEDIGE ROUTE — BINDEND (2026-08-08):** elke unit
  heeft twee leesteksten, en dat blijft zo: één om lezen te *leren*, één om te
  *lezen*. Wat wél fout was: ze legden allebei dezelfde route af. Voorspellen en
  juist/fout-met-bewijs stonden in álle zestien units twee keer, met een andere
  tekst maar dezelfde beweging. **De regel nu:** `§N · Lectura 1` (unit-eigen,
  in de inhoudelijke lijn) draagt de volledige route — voorspellen, scannen,
  juist/fout met bewijs, betekenis uit context, reactie. `§N · Lectura 2` (het
  gedeelde blok `print_bloques.lectura_print`, vóór de Escucha) is een
  *transfer*-tekst: leesdoel → tekst → scannen → betekenis uit context →
  reactie, ± 12 min in plaats van 20. Juist/fout-met-bewijs bij die tweede tekst
  staat op de hub, mét zelfcorrectie en bewijsveld; de print verwijst ernaar.
  *Betekenis uit context blijft* in Lectura 2 — in C6+ komt die stap nergens
  anders voor. Een unit met maar één leestekst (C5 U0) roept
  `lectura_print(..., sola=True)` en houdt de volledige route.
  **Resultaat: 721 → 706 bladzijden, 56 → 45 halflege.**
- **Leesvaardigheid in de cursus (print):** elke unit heeft een echte **leessectie (Lectura)** volgens `VIER_VAARDIGHEDEN_GEINTEGREERD.md §1`: visuele tekstintroductie (tekstsoort·afzender·ontvanger·leesdoel) → authentieke microtekst (chat·perfil·ficha·mensaje·anuncio) → *voorspellen* → globaal begrip → **scannen** → **juist/fout + bewijs** (evidence) → betekenis uit context → **productieve reactie**. Recycleert de unit-woordenschat/grammatica.
- **Vaardigheden geïntegreerd (leerlijnen):** elke unit realiseert meerdere van de **8 vaardigheidsketens** (lezen→spreken, lezen→schrijven, luisteren→spreken, luisteren→schrijven, schrijven→spreken, spreken→schrijven, lezen+luisteren→bemiddelen, volledige eindtaak). Niet vier gescheiden blokken: een tekst leidt tot een gesprek, een luisterfragment tot schrijven, enz. Beweging per skill: oriënteren → receptief → analyseren → gestuurd → zelfstandig → transfer → feedback & herneming.
- **HTML-pagina — opname-oefeningen (VERPLICHT):** de digitale pagina bevat **spreek-/opnamecomponenten** waar de leerling **zichzelf opneemt** (MediaRecorder: opnemen → terugluisteren → heropnemen), volgens `VIER_VAARDIGHEDEN §4.2`: **ListenRepeatRecorder · ShadowingPlayer · SubstitutionCarousel · VoiceMessageTask · SpeakingSelfAssessment/RecordReflectRetry**. Deze worden als **motor-templates** gebouwd (nieuw sjabloon `speak` = record+playback, offline; TTS-model optioneel). Web Speech-**herkenning** vereist internet → optioneel, nooit als enige beoordeling; **begrijpelijkheid/boodschap/interactie** blijven de criteria.
- **Motor-variatie op de HTML (BINDEND):** ook op de digitale pagina telkens **variatie** via de motor; ontbreekt een speltype, dan **bouw je het bij** (nieuw sjabloon). Reservoir voor speltypes: `spaans-motor/BRAINSTORM_100_SPELVORMEN.md` + `PLAN_100_SPELVORMEN.md`.
- **PowerPoint:** put uit `INTERACTIEVE_POWERPOINT_50_IDEEEN.md`; dek naast woordenschat/grammatica ook **lezen · luisteren · spreken · schrijven** af, met de klik-onthul-didactiek en noodroute.
- **Geen werkvorm-/component-herhaling met dezelfde jas binnen één unit; over units heen recyclen (spreiding) mét variatie.**

## 14ter · Reservoir & cocktail-workflow — BINDEND (auteur 2026-07-26, ronde 5)

De richtlijnen zijn **geen proza om te "kennen" maar een plukvijver om uit te putten.** Ze staan geïndexeerd in **`02-huisstijl/reservoir/`**:
- **`reservoir.json`** — 453 geïndexeerde items met ID: **WV-** (100 werkvormen) · **LAY-** (50 layout) · **GT-** (25 interactieve grammaticatools) · **PPT-** (50 PowerPoint) · **VS-** (23 woordenschat-patronen) · **VG-** (35 grammatica-patronen) · **SK-** (120 vaardigheidscomponenten/ketens) · **DS-** (50 designcomponenten). Elk record = `{id, domein, naam, omschrijving, formaat, vaardigheid, fase, bron}`.
- **`reservoir_index.md`** — mensleesbare pluklijst per domein.
- **`coverage.md`** — dekkings-grootboek (item × unit). **Doel: tegen U8 is het merendeel van de 453 items érgens gebruikt.**
- **`PARELS_materiales.md`** — door de auteur aangeduide **must-reuse-parels** uit het vorige project (`00-brondocumenten/materiales-vorig-project/`): voetbaltruitjes «equipación» (U6), familia via Rosalía-árbol (U2), leestekst LatAm-supersterren (U4), canción «La Perla» (U4).

**Woordenschat = kandidatenpool, geen wet:** `00-brondocumenten/materiales-vorig-project/Cursus_Spaans_Woordenschat_Master_v8.xlsx` (kolom *Unidad de introducción*) is een **voorlopige** synthese uit het vorige project. Cureer per unit uit die pool (gestuurd door outline-thema + leerplan), forceer de aantallen niet, en **verbeter/vul de lijst onderweg aan**.

**VERPLICHTE workflow vóór élke unit (nieuw én tweak):**
1. **Cocktail-receta** `01-cursussen/05-a1/U<N>/U<N>_cocktail.md` schrijven: per cursusonderdeel (§0, elke grammatica-sectie, vocab, Taller, Cultura, Lectura, Tarea, Repaso, hub-games, PowerPoint) **expliciet reservoir-IDs kiezen** — bewust de **nog niet/weinig gebruikte** (raadpleeg `coverage.md`), zodat variatie meetbaar groeit i.p.v. dezelfde jas.
2. **Quota halen** (harde ondergrens per unit): ≥1 **luisterdialoog** (script + TTS op de hub + begripstaak in print) · ≥1 **rijke leestekst** (Lectura) · ≥2 **opname-oefeningen** · ≥1 **traditionele cloze-werkwoord** · ≥8 **verschillende** motor-speltypes · een echte **"traditionele" oefenbatterij** (gap-fill · substitutie · matching · dictee · ordenen) **naast** de visuele grammatica (= de klassieke "cursus-feeling" + het moderne visuele).
   - **HTML-HUB — OEFENRIJKDOM (BINDEND, auteur 2026-07-26):** de digitale pagina bevat **≥100 interactieve oefeningen** totaal, met **meerdere reeksen/rondes per oefening** (elke game trekt uit een pool van ≥12 items zodat herspelen nieuwe reeksen geeft — nooit één kort rondje). Naast de **10–20 motor-games** ook **zelfcorrigerende grammaticatools** (GT-reservoir: vervoegingscirkel · patroonzoeker · bouwstenen-sleep · schuifregelaar…) én **drills** (V/F, matching, gap-fill met feedback) in de vocab-/grammatica-/lectura-panelen. **Brede reservoir-dekking**: put uit zoveel mogelijk verschillende GT-/WV-/SK-items — geen 3× dezelfde jas.
3. **Master-vocab cureren** uit de pool + aanvullen.
4. **Parels inweven** waar de doel-unit matcht (zie `PARELS_materiales.md`).
5. Na de build: **`coverage.md` bijwerken** met de exact gebruikte IDs.

**Traditioneel × modern (BINDEND):** elke unit combineert de visueel-eerste grammatica (§14) mét een klassieke oefenbatterij en echte vaardigheidsteksten (luisterdialoog, leestekst) in de stijl van de eigen eerdere lessen (`materiales-vorig-project` = ijkpunt voor de "cursus-feeling"). De visuele innovatie vervángt de traditionele invulling niet — ze staan naast elkaar.

## 15 · Beeld & asset-pijplijn (BESLIST 2026-07-25)

- **BESLIST 2026-07-26 — Claude bouwt de VOLLEDIGE beeldlaag in flat-vector (code).** De AI-fotoroute (ChatGPT/DALL·E) blokkeerde bij de auteur; daarom tekent Claude **alles zelf in code** — geen externe tool nodig, alles bewerkbaar en print-perfect. Bron = de generatoren in `02-huisstijl/beeld/generators/` (`cast_gen.py`, `build_svgs.py`, `assets2.py`, `build_map.py`). Stijl = warm flat-vector (zie de gerenderde staalkaart): **concrete items, geen kale blokken of abstracte figuren.**
- **Cast (flat-vector, VASTGELEGD):** Lucía (Sevilla, lang haar+bloem, koraal) · Diego (CDMX, kort haar, blauw) · Valen (Cartagena, krullen, turquoise) · Nina (Cusco, vlechten, oker) · **Tú** (neutrale avatar, streepjesrand) · **Mateo** (BsAs, vanaf C6). Elk = eigen accentkleur; busten + circulaire avatars + poses/emoties uit dezelfde generator.
- **Mochila-mascotte:** flat-vector rugzak met gezichtje (kompas/kaart/ster-varianten). De klas kiest de naam.
- **Kaarten = ECHTE geografie (BINDEND, auteur 2026-07-26):** géén gestileerde/abstracte kaart. De *mapa del mundo hispano* wordt gerenderd uit **Natural Earth** (public domain, `ne_110m_admin_0_countries.geojson`) via `build_map.py` — equirectangular, alle Spaanstalige landen opgelicht, paradas met cast-avatars. Zelfde aanpak voor latere kaarten.
- **Foto's / scènes:** **niet vereist** — vervangen door eigen vector-illustratie. Wil de auteur tóch echte foto's van plekken, dan levert hij rechtenvrije foto's (Unsplash/Pexels) aan; Claude plaatst ze. De Drive-map «Estilo Exploración» blijft optioneel/aanvullend, niet blokkerend.
- **Iconen: Lucide — nu in de repo** (`02-huisstijl/vendor/lucide/`). 1766 iconen als
  één `lucide.json` (enkel de tekenpaden), plus `iconos.py` dat er inline SVG van maakt
  in onze eigen maten en kleuren — een icoon erft `currentColor` en kleurt dus mee met
  de cursuskleur. **Licentie = ISC**, niet MIT: dat gold alleen voor de van Feather
  afgeleide deelverzameling. De licentie staat verbatim naast de iconen.
  `BADGE` in `iconos.py` vertaalt de 26 emoji die nú in de cursus staan naar hun
  tegenhanger. **Op de digitale pagina toegepast** (auteur 2026-08-08): de interface —
  de negen tabbladen, de knoppen, goed/fout, geluid, transcript, de bewerkbalk — draait
  op Lucide via `03-build/web/hub_iconos.py` (CSS-maskers, dus ze kleuren mee met de knop
  waarin ze staan) en de nabewerking `hub_post_iconos.py`. **De woordkaartjes houden hun
  kleur-emoji** (`vocab_emoji.py`, vastgelegd bij U5): een woordkaart toont een díng, en
  daar is kleur een geheugensteun. De regel die daaruit volgt en die overal geldt:
  **een icoon is interface, een emoji is betekenis.** **In print óók toegepast**
  (auteur 2026-08-08): `03-build/web/print_iconos.py` zet na de bouw 3026 interface-emoji
  om naar inline Lucide-SVG in alle 27 print-units (C4 · C5 · C6+), met `currentColor`
  zodat een icoon in een groene badge groen wordt. De twee tegenlijsten staan in
  `iconos.py`: **`BADGE`** (42 emoji die interface zijn → icoon) en **`NO_TRADUCIR`**
  (typografie die blijft). Onaangeroerd blijven: de **woordkaartjes** en §V-tabellen,
  het **semáforo**, de **vlaggen**, de **familieleden**, alle **voorwerp-emoji**, en wat
  géén emoji is maar typografie (★☆ moeilijkheid · ☐ aankruisvak · → in een keten ·
  ①②③ stappen). Kosten: 816 → 819 bladzijden.
- **Mockups (chat/ficha/ticket/menu/bingo/poster/profiel…), infographics, spot-illustraties, kleurvlakken:** vector (SVG), in huis gebouwd (zie `assets2.py`).
- **Technische pijplijn:** SVG = bron → **300 dpi PNG** voor Word/PDF (python-docx plaatst PNG kraakhelder), **SVG** rechtstreeks in HTML. Foto's als hoge-resolutie JPEG/PNG.
- **Altijd:** alt-tekst bij elk beeld · **grijswaarden-veilig** · kleur nooit als enige informatiedrager (ook label/vorm/icoon).

## 16 · PowerPoint · HTML · gamification-motor (BINDEND — in opbouw)

**PowerPoint** — spec: `02-huisstijl/richtlijnen/INTERACTIEVE_POWERPOINT_50_IDEEEN.md`.
- **Interactief**, in **huisstijl**, met **avatars** waar nodig. Twee uitvoerversies: **docent `.pptx`** (vrije navigatie, presenter view, oplossingen) + **leerling `.ppsx`** (kioskmodus, beperkte navigatie, ingebouwde feedback).
- Vaste diamaster-layouts (TITLE · LESSON_MENU · VOCABULARY · GRAMMAR · READING · LISTENING · SPEAKING · WRITING · QUIZ · FEEDBACK · CULTURE · FINAL_MISSION · TEACHER_NOTES), vaste objectnamen, drie lagen (CONTENT/INTERACTION/TEACHER), altijd een **noodroute** (toon oplossing / sla over / terug). Eerst de **kernset van 15** functies.
- Didactiek = dezelfde beweging (context → begrijpen → opmerken → oefenen met afbouw → produceren → feedback → hernemen).

**Onderlinge verwijzingen (BINDEND):** cursus (Word/PDF) ↔ **PowerPoint** én cursus ↔ **HTML** kruisverwijzen (bv. «zie dia 12» / «oefen online: …»), met consistente iconen/kleuren.

**HTML — architectuur (BINDEND):**
- **Visuele/interactieve grammatica (BINDEND, auteur 2026-07-26):** de kerngrammatica wordt op de HTML-pagina **visueel én interactief** uitgelegd volgens `02-huisstijl/richtlijnen/25_VISUELE_INTERACTIEVE_GRAMMATICATOOLS_HTML.md` (25 werkvormen + vaste opbouw context→noticing→ontdekken→visualiseren→regel→toepassen→produceren + herbruikbare componenten). Uitgangspunt: **eerst betekenis/patroon ontdekken, dan regel**; kleurcodering = de functionele taalsemantiek uit §13; verklarende feedback; toegankelijk (toetsenbord, geen kleur-alleen).
- **Repaso = online (BESLIST 2026-07-26):** het herhalings-/inoefenwerk (recordar sin pista, gemengde quiz, drills) staat **op de digitale pagina** met spellen + zelfcorrectie, niet meer als drills in print. Print-repaso = enkel **spiekkaart (SummaryQuadrant) + semáforo** + een «Repasa jugando (online)»-verwijzing. Houdt de printunit korter en minder repetitief.
- **4 hoofdtabbladen** — één per cursus (C4·C5·C6·C6+). Per tab: een **overzicht van de unidades** van die cursus.
- **Per cursus, achteraan:** een **«Conjugador» (werkwoordengenerator)** + de **woordenschat als naslagwerk** met correcte **unit/LPD-verwijzingen** en een **zoekfunctie**.
- **Flip cards voor ÁLLE woorden per unidad:** toggle **ES→NL / NL→ES**; voorkant = Spaans woord **+ voorbeeldzin**, achterkant = vertaling **+ (eventueel) afbeelding/icoon**. Verzorgde iconen (Lucide; vorige versie had mooie icoontjes → aanhouden).
- **Kruisverwijzingen** cursus ↔ HTML ↔ PowerPoint; huisstijl overal; motor-spellen (10–15/thema) ingebed per unidad.
- **QR-codes op print (PDF/Word)** verwijzen naar de **digitale HTML-pagina** (de hub met audio, spellen, flip cards én de Extra-links profedeele/arche-ele), op het juiste ankerpunt — **niet** rechtstreeks naar YouTube/PPTX.
- **Tab «Extra» (extern bronnenmateriaal) per onderdeel:** grammatica → **profedeele-YouTube**-embed; grammatica/woordenschat → **arche-ele-Genially**-link (indien bestaand). *Toegangsbeperking:* websearch werkt, willekeurige pagina's ophalen niet → verificatie mogelijk handmatig (auteur levert links).

**Gamification-motor — `spaans-motor`** (door auteur gebouwd via claude.ai; getest: bouwt offline met Node, geen internet):
- Dependency-vrij: elk spel = **één standalone offline HTML**. Gedeelde `engine.js` (score, streak, **adaptief**, foutenlog, resultaten, geluid); **generatoren** (vervoeging/geslacht, *nagerekend* — nooit zelf vervoegen); `SKILL.md` routeert leerstof → sjabloon → bouwt.
- **Huidige sjablonen: `classify`, `match`, `tetris`** + generatoren `conjugation`/`gender`/`verbo` (324 werkwoorden) + 8 voorbeeldspellen. **NB: geen 100 kant-en-klare speltypes** — «100» was ambitie; de motor is wél **uitbreidbaar** (nieuwe sjablonen `cloze`/`order`/`point`/… pluggen in).
- **Doel:** per webpagina/thema **10–15 gevarieerde spellen** die woordenschat/grammatica inoefenen volgens de principes (receptief→productief, spreiding). → vergt eerst **uitbreiding van de sjablonenset** voor voldoende variatie.
- **Plaatsing (BESLIST 2026-07-25):** in deze monorepo → **`spaans-motor/`** (met eigen README/SKILL/build).
- **100 spelvormen (brainstorm auteur):** `spaans-motor/BRAINSTORM_100_SPELVORMEN.md` → te **distilleren tot ~15–20 herbruikbare templates** (plan komt in `spaans-motor/PLAN_100_SPELVORMEN.md`). Claude kiest per leerstof de juiste template en integreert het spel in de unit-HTML (spreiding, receptief→productief). Veel ideeën = dezelfde judge-logica met een andere «jas» (arcade-skins).
- **AI-tutor (#100) — GEWENST (auteur):** A1-tutor-chat als **online** component bovenop een LLM (bv. Claude API), met strakke A1-guardrails (alleen A1-lexis/structuren, vriendelijk corrigeren, korte beurten). Enige spelvorm die internet vereist; API-sleutel/hosting apart te regelen.
- **Reservoir voor oefeningen:** oudere door de auteur gemaakte cursussen (in Drive) mogen als bron dienen bij het maken van oefeningen/spellen.

## 17 · Toetsen & leerplandoelen (BINDEND)

- **Leerplandoel-verwijzingen (LPD):** doorheen álle cursussen verwijzingen naar de leerplandoelen (III-Spa-d). **Claude zet de codes zelf** in de cursus, afgeleid uit het leerplan (`00-brondocumenten/leerplan/…`, reeds in repo).
- **Toetsen/evaluaties per unit:** **toetsen genereren die de leerstof effectief testen**, **leerplan-gebaseerd** (dekking van de LPD-doelen), met de vier vaardigheden en communicatieve eindtaken. Zelfde huisstijl/formaten (Word/PDF).

## 18 · Productie (WERKWIJZE — gestart 2026-07-25)

- **LEERLINGENEDITIE = NUL META (BINDEND, auteur 2026-07-27):** de finale leerling-editie bevat **geen enkele meta/placeholder-opmerking** — geen `[BEELD:…]`/`[AUDIO:…]`-hooks, geen «link volgt», «leerkracht vult aan», «nog te …», «volgt later», TODO's e.d. **Ontbrekende content wordt gegenereerd** (beeld/oefening/tekst); externe-bron-placeholders (profedeele/arche-ele) worden ingevuld met de door de auteur geleverde links óf verwijderd. **Scan elke unit hierop vóór finale levering.** (NB: «todo» = Spaans woord *alles*, geen placeholder; `placeholder="…"` = zoekveld-hint, geen meta.)
- **FINALE «hosting + links + audio»-SWEEP (auteur 2026-07-27) — UITGEVOERD.** De sweep is
  af: de nep-`qr()` is vervangen door **echte QR-codes** (eigen encoder `qr_codigo.py`, want
  `segno` bestaat hier niet), elke code wijst naar de **gehoste hub-URL + het juiste anker**,
  de ankers bestaan (nagerekend: 100 codes, 98 naar een specifieke oefening), en de audio is
  ingesproken en in de pagina's gebakken in plaats van «browser-TTS».
- **HOST = `espanol-en-la-practica.wim-wuyts1979.chatgpt.site` (auteur 2026-08-09).** Eerder
  stond hier **Netlify**; dat is achterhaald — de unidades komen op een door ChatGPT
  gegenereerde site. Het adres staat op één plaats in de code: **`BASE` in
  `03-build/web/enlaces.py`**, en alle QR-codes en kruisverwijzingen worden daaruit
  afgeleid. Verhuist de site, dan is dat één regel + de units herbouwen.
  (`sjbespanol.netlify.app` in §10 is iets anders: dat is de óude cursus, als bronmateriaal.)
  **Gevolg voor de AI-laag:** op zo'n gehoste pagina is er geen plek om een geheime sleutel
  te bewaren, dus een AI-partner die een externe dienst aanroept is daar sowieso niet veilig
  te bouwen. De keuze voor een **offline** oefenpartner (auteur 2026-08-09) is dus niet
  alleen een privacykeuze maar ook de enige route die op deze host werkt.
- **Volgorde:** **eerst U0 volledig** (bron → Word · PDF · PowerPoint · HTML), goedkeuren, **dan hetzelfde proces** voor alle units van jaar 5 (C5) en 6 (C6/C6+).
- **Één bron eerst:** per unit een **single-source contentbestand** (`01-cursussen/<cursus>/<unit>/<unit>_bron.md`) → daaruit de formaten.
- **Kernstandpunt (BINDEND):** álles wat in de vier md-specs (grammatica · woordenschat · vaardigheden · PowerPoint) + de 100 spelvormen staat, moet **ergens terugkomen** → **VARIATIE is key** (>200 suggesties; geen herhaling van dezelfde werkvorm). Geldt ook voor de generator-oefeningen.
- **Team van specialist-subagents** voert dit tot in detail uit, binnen de vastgelegde specs.
- **PRINT = PDF (BESLIST 2026-07-25):** Word mag, maar als het moeilijk gaat leveren we in **PDF** (visueel sterker, aldus auteur). Pijplijn: **HTML = bron → PDF via Chromium/Playwright** (werkt in déze sandbox; vervangt de defecte Word→PDF-route). AI-foto's komen van de auteur (`[BEELD:…]`-hooks tot dan).
- **Bladspiegelspecialist verplicht** in het build-team (zie §13 bladspiegel-regel: geen kaders, volle witruimte efficiënt benutten).
- **Print-build-sjabloon (VASTGELEGD, golden sample U0 · 2026-07-26):** `02-huisstijl/templates/cursus-print.css` — de **bindende layout/componentenkit** (hero · parada-kop met achtergrondcijfer · LPD-chips · activiteit met nummerbadge + vaardigheid/tijd/moeilijkheidsbadges + APOYO-ladder · regla-onthoudkaart · klankkaart · QR-audiokaart · mochila-gids · sectiescheider · semáforo). **Print-hygiëne zit erin:** veilige `@page`-marges boven/onder met **hero-bleed op p1** (`@page:first{margin:0 0 12mm 0}`), doorvloeiende tabellen (`thead` herhaalt), weesregel, `print-color-adjust:exact`. **Elke unit-HTML hergebruikt dit — niet opnieuw uitvinden.** Render: HTML → Chromium `--print-to-pdf`. Per cursus enkel de `--g/--gd/--gt`-tokens wisselen (C4 rood · C5 groen · C6 blauw · C6+ paars).
