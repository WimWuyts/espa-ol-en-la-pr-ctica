# PLAN — 100 spelvormen op de spaans-motor

> Ontwerpdocument. Vertaalt de 100 gebrainstormde spelideeën naar een **minimale,
> herbruikbare motor-architectuur**, met een bouwroadmap die **Unidad 0** als eerste
> doel neemt. Bindend kader: `README.md`, `SKILL.md`, `schema.md` (deze map) +
> CLAUDE.md §14 (didactiek) en §16 (motor).

---

## 0 · Grondinzicht: de motor is al judge-agnostisch

De bestaande `engine.js` doet **alles behalve het speelveld**: score, streak, adaptieve
toevoer (`makeFeeder`), foutenlog, resultaten-overlay, geluid, toegankelijkheid. Een
sjabloon rendert enkel het veld en meldt per beurt `api.judge(ok, meta)`.

> **Gevolg:** een spel = **een judge (rekenkern «goed/fout») + een skin (hoe het eruitziet)**.
> `tetris` bewijst dit al: het is geen aparte oefenlogica, maar een *arcade-skin over
> exact dezelfde `classify`-config en generator*. Dezelfde `api.judge`, ander veld.

Daarom clusteren we de 100 ideeën **niet** per thema maar per **judge**. Skins (tetris,
snake, mijnenveger, pinball, mollenmeppen…) zijn presentatie, geen nieuwe motorlogica.
Dit houdt de te bouwen kern klein en respecteert de gouden regel *variatie* (CLAUDE.md §13):
één judge, veel gezichten.

---

## 1 · Template-taxonomie (de minimale herbruikbare set)

Drie lagen boven op de motorkern, plus één uitzondering.

```
                 ┌───────────────────────────────────────────────┐
   LAAG 4        │  ai-tutor   (#100 — enige die internet vereist) │
                 └───────────────────────────────────────────────┘
   LAAG 3        meta-wrappers  (leitner · confidence · foutenmuseum · heatmap · streak · can-do)
                 └── consumeren tagStats + foutenlog van de engine; wrappen élke judge
   LAAG 2        skins / presentatie  (arcade-skins · point-scenes · text-skins · sim-mockups)
                 └── renderen het veld; delen de judge eronder
   LAAG 1        JUDGES  (de rekenkern: bepaalt goed/fout, voedt api.judge)
   LAAG 0        engine.js  (score · streak · adaptief · foutenlog · resultaten · geluid)
```

### 1.1 · De judges (rekenkernels)

| # | Judge | Bestaat? | Wat hij doet | Interactie |
|---|-------|:--:|---|---|
| J1 | **`classify`** (select) | ✅ | Kies 1 uit N categorieën voor één stimulus | tik knop / 1–9 |
| J2 | **`match`** (link) | ✅ | Verbind paren over twee kolommen | koppelen |
| J3 | **`text`** (cloze + type) | 🆕 | Typ een antwoord in een gat of bare prompt; **gecheckt tegen generator/dataset** (nooit vrije spelling accepteren) | toetsenbord |
| J4 | **`order`** (sequence) | 🆕 | Zet tegels/stappen in de juiste volgorde | slepen / tikken |
| J5 | **`point`** (locate) | 🆕 | Klik het juiste doel in een beeld, tekst, kaart of woord | klik/tik op doel |
| J6 | **`speak`** (speech) | 🆕 | Web Speech API vergelijkt je uitspraak met het doel | microfoon |
| J7 | **`sim`** (open) | 🆕 | Open productie (chat/schrijven) met **zachte** check (keyword / lengte / verplichte bouwstenen), geen strikt goed/fout | typen/kiezen |

**2 bestaan, 5 nieuw.** Alle vijf nieuwe judges gebruiken dezelfde motor-API
(`api.judge`, `api.next`, `api.setTarget`, `api.finish`, `api.bonus`). Ze pluggen in
zoals `README.md` beschrijft: `src/templates/<judge>.{js,css}` + één regel in `build.mjs`.

### 1.2 · De skins (presentatie boven een judge)

Skins zijn **puur veld-rendering**; ze bouwen geen nieuwe correctheidslogica.

| Skin-familie | Zit boven judge | Voorbeeld-skins (elk = look, geen nieuwe motor) |
|---|---|---|
| **arcade-skins** | `classify` (J1) | tetris ✅ · snake · mijnenveger · pinball/flipper · platformer · mollenmeppen · vier-op-een-rij · sorteerband · tower-defense¹ · slot-machine² · duel (2-speler) · pubquiz-buzzer · raket |
| **point-scenes** | `point` (J5) | isometrische kamer · plattegrond · SVG-inkleuren · kaart (Spanje/LatAm) · klok · tilde-schutter · diftong-splitser · foutenjacht · pretérito/imperfecto-tagger · acento-hero (ritme) |
| **text-skins** | `text` (J3) | cloze (gat in zin) · type-race (bare speed) · dictado · mad-libs · postal/dagboek-generator · woordgolf · emoji-vertaler · definitie-raden |
| **order-skins** | `order` (J4) | zinsmachine · pronomen-stapelaar · recept-stappen · detective-tijdlijn · zinsstretcher · lettergreep-bubbelschieter |
| **speak-skins** | `speak` (J6) | shadowing · herkenningsscore · karaoke · belscherm-simulator · alfabet-race |
| **sim-mockups** | `sim` (J7) | WhatsApp · Instagram · Wallapop · tweet · menú del día · tapas · airbnb · codenames · werewolf · cadáver exquisito · estafette · stamboom |

¹ tower-defense = `match`-judge (juiste vertaling bouwt de toren). ² slot-machine = `text`-judge (vervoeg binnen 5 s).

> **Regel (CLAUDE.md §13):** dezelfde judge mag **nooit twee keer met dezelfde skin**
> binnen één unit verschijnen. De SKILL kiest de skin voor *variatie*, niet de leerstof.

### 1.3 · De meta-wrappers (laag 3)

Geen judges — ze **wrappen** een bestaand spel en lezen de engine-data (`S.tagStats`, `S.log`).
Eén keer bouwen, werkt over álle judges.

| Wrapper | Idee(ën) | Leest | Doet |
|---|---|---|---|
| **leitner** | 48 | tagStats | spaced-repetition-doosjes; recyclet zwakke tags |
| **confidence** | 49 | judge-hook | inzet vóór antwoord; hoge inzet + fout = extra verlies |
| **foutenmuseum** | 50 | foutenlog | stelt jóuw fouten opnieuw voor, met bordje |
| **heatmap** | 97 | tagStats | dashboard groen→rood per categorie |
| **streak-kalender** | 98 | localStorage | dagelijkse mini-oefening, gewoontevorming |
| **can-do zelfscan** | 99 | routing | ERK-can-do → stuurt volgende oefening bij |
| *(escape-room container* | 20 | — | *bundelt sub-oefeningen; sim/meta-hybride)* |

### 1.4 · Samenvatting taxonomie

**Minimale herbruikbare set = 10 blokken:** 7 judges (2 bestaand + 5 nieuw) + arcade-skin-framework
+ meta-wrapper-laag + ai-tutor. Daarbinnen zijn alle 100 ideeën **skins of configs**, geen nieuwe motorlogica.

**Verdeling van de 100 ideeën:**

| | Aantal | Ideeën |
|---|--:|---|
| **Draaien VANDAAG op bestaande templates** (classify/match/tetris) | **27** | zie §1.5 |
| **Vereisen nieuwe template-code** | **73** | zie §1.5 |
| ↳ waarvan **buiten leerplan-scope** (schrappen/aanpassen) | 1 | #53 subjuntivo |

### 1.5 · Volledige mapping (alle 100 → judge · skin · bouwstatus)

**Op `classify` (✅ bestaand, 21):** 34 blind-luisteren · 36 minimale paren · 51 por/para ·
53 subjuntivo *(BUITEN scope)* · 56 reflexief · 57 ser/estar-weegschaal · 58 hay/está ·
60 ir-a-inf · 61 muy/mucho · 62 este/ese/aquel · 63 possessief · 65 b/v · 66 g/j ·
67 h muda · 68 ll/y · 76 sorteerband *(skin)* · 83 abierto/cerrado · 84 woordfamilie ·
85 collocatie · 88 valse vrienden · 96 wie-zei-wat.

**Op `match` (✅ bestaand, 5):** 71 woord-memory · 81 fiesta-kalender · 86 voorvoegsel ·
87 antoniemen · 89 register-schuif.

**Op `tetris` (✅ bestaand arcade-skin, 1):** 1 conjugatie-tetris.

**Nieuw — `text`/J3 (18):** 8 reactietijd-ladder · 13 pinautomaat · 22 verbo-slotmachine ·
23 mad libs · 25 omgekeerde quiz · 27 woordgolf · 29 emoji-vertaler · 30 definitie ·
33 dicteerace · 47 estafette · 52 gustar-machine · 59 comparativo · 70 alfabet-race ·
77 woordketting · 90 postal · 93 dagboek · 94 podcast-gaten · 95 getallen-dictee.

**Nieuw — `point`/J5 (15):** 4 acento hero · 12 kassa · 16 consulta médica · 17 weerkaart ·
24 foutenjacht · 37 isometrische kamer · 38 plattegrond · 39 SVG-inkleuren · 43 kaart Spanje ·
54 pretérito/imperfecto · 64 tilde-schutter · 69 diftong-splitser · 73 mollenmeppen ·
80 kaart LatAm · 82 telenovela-stamboom.

**Nieuw — `order`/J4 (7):** 14 metro imperativo · 19 detective · 21 zinsmachine ·
26 zinsstretcher · 55 pronomen-stapelaar · 72 lettergreep-bubbel · 92 recept.

**Nieuw — `speak`/J6 (4):** 11 belscherm · 31 shadowing · 32 herkenningsscore · 35 karaoke.

**Nieuw — `sim`/J7 (16):** 9 WhatsApp · 10 Instagram · 15 Wallapop · 18 airbnb ·
20 escape room · 28 cadáver · 40 stamboom-audio · 41 aankleedpop · 42 klok · 45 codenames ·
46 werewolf · 78 menú · 79 tapas · 91 tweet.

**Nieuw — arcade-skins over `classify` (7):** 2 mijnenveger · 3 snake · 5 ser/estar-duel ·
6 tower-defense *(over match)* · 7 pinball · 44 pubquiz-buzzer · 74 vier-op-een-rij · 75 platformer.

**Nieuw — `meta`-wrappers (6):** 48 leitner · 49 confidence · 50 foutenmuseum ·
97 heatmap · 98 streak-kalender · 99 can-do.

**Nieuw — `ai-tutor` (1):** 100 AI-gesprekspartner.

---

## 2 · Bouwroadmap — Unidad 0 eerst

**U0-leerstof:** alfabet · klanken/uitspraak · klemtoon/accent · getallen (0–1000) ·
begroeten & chunks · klastaal. Doel van deze fase: **12–15 gevarieerde U0-spellen**
met een minimale hoeveelheid nieuwe code.

### Prioriteitsvolgorde

| Wave | Bouwen | Kost | Ontgrendelt voor U0 |
|---|---|---|---|
| **0** | *niets* — **audio-flag toevoegen aan `classify`** (kleine ingreep: TTS/clip afspelen bij stimulus) | XS | 6 fonetiek/luister-spellen **vandaag** |
| **1** | judge **`point`** + `tilde`-generator (aguda/llana/esdrújula, lettergrepen) | M | klemtoon & diftongen — kern van U0 |
| **2** | judge **`text`** + `numeros`-generator + audio-in | M | getallen, dictee, spellen |
| **3** | laag **`meta`** (leitner + foutenmuseum) | S | spreiding & retrieval over de U0-set |
| **4** | arcade-skins (mollen, vier-op-een-rij) + judge **`speak`** *(met caveat)* | M | variatie + uitspraak |

> `match` bestaat al → begroetingen/register/getal-cijfer zijn ook **nul bouw**.
> Waves 0–1–2 leveren samen ruim 15 U0-spellen; 3–4 voegen spreiding en variatie toe.

### De concrete U0-set (15 spellen)

**`classify` + audio — ✅ bestaand (Wave 0):**
- **¿B o V?** — dictado, enkel dit onderscheid telt (`baca`/`vaca`). *(idee 65)*
- **¿G o J?** — `gente`/`jefe`, met de ge/gi-valstrik. *(66)*
- **Minimale paren** — audio → `pero`/`perro`, `caro`/`carro`. *(36)*
- **Blind luisteren** — audio → kies uit 3 iconen, geen tekst. *(34)*
  *(reserve: ¿LL o Y? #68, ¿H o nada? #67)*

**`match` — ✅ bestaand (Wave 0):**
- **Memory: saludos** — `hola`/`buenos días`/`hasta luego` ↔ NL, tegen de klok. *(71)*
- **Register-schuif** — `¿qué tal?` ↔ `¿cómo está?`, tú/usted. *(89)*
- **Getal ↔ cijfer** — `uno`↔1, klastaal-uitdrukking ↔ functie.

**`point` — 🆕 (Wave 1):**
- **Tilde-schutter** — klik de beklemtoonde lettergreep; motor checkt aguda/llana/esdrújula. *(64)*
- **Diftong-splitser** — splits `ai`/`ei`/`au` en tel de lettergrepen. *(69)*
- **Acento Hero** — tik de klemtoon-lettergreep op de beat (ritme-skin). *(4)*

**`text` — 🆕 (Wave 2):**
- **Pinautomaat** — typ het getal dat je hoort (0–1000). *(13)*
- **Getallen-dictee** — telefoonnummers, prijzen, huisnummers door elkaar. *(95)*
- **Alfabet-race** — spel je naam / mailadres / straat. *(70)*

**`meta` — 🆕 (Wave 3, wrapt bovenstaande):**
- **Leitner-doosjes** over de saludos- en fonetiek-sets (spreiding).
- **Foutenmuseum** over je eigen fonetiek-missers (retrieval).

Deze 15 dekken elk U0-domein en bewegen van **receptief** (classify/match/point-herkennen)
→ **gestuurd productief** (text: typ het getal, spel je naam), met meta-wrappers voor spreiding.

---

## 3 · De AI-laag (#100) — apart, want breekt de offline-belofte

Alle 99 andere spellen zijn dependency-vrije offline HTML (`README.md`). **#100 is de
enige uitzondering:** een A1-tutor-chat die een LLM-API en dus **internet** vereist.
Daarom staat ze los, in de **Extra-tab**, en mag geen enkel ander spel ervan afhangen.

### Aanpak

- **Rol/systeemprompt (strak A1):** «Je bent een warme reisgezel op *La Ruta*. Praat op
  **A1-niveau**. **Korte beurten** (1–2 zinnen). **Spaans eerst**, minimale NL-steun enkel
  op vraag. Eindig elke beurt met **één vraag** zodat het gesprek doorloopt.»
- **Didactische guardrails (hard):**
  - **Alleen A1-lexis en -structuren.** Modelleer **geen** futuro simple, condicional of
    subjuntivo — dit spiegelt de harde scope-grens uit CLAUDE.md §2. De tutor mag die
    vormen dus zélf niet gebruiken, ook niet als de leerling ze uitlokt.
  - **Vriendelijk corrigeren via *recast*, niet becijferen:** «Ah, ¿quieres decir…?» +
    de correcte vorm, daarna meteen door. Max één correctie per beurt.
  - **Geen monologen**, geen lange uitleg, geen vertaalmachine spelen.
  - **Content-filter** voor tieners; off-topic → vriendelijk terugsturen naar het thema/parada.
- **Difficulty-knop:** «más fácil / más difícil» past zinslengte en woordfrequentie aan.

### Praktische noden (knopen voor de leerkracht)

- **API-sleutel mag NIET in de HTML** (lekt onmiddellijk). → er is een **kleine proxy**
  nodig (Cloudflare Worker / Netlify-function) die de sleutel bewaart, rate-limit oplegt
  en doorstuurt. Dit is de enige serverkant in het hele project.
- **Provider/model:** de natuurlijke keuze is de **Claude API met een Haiku-klasse model**
  (goedkoop, snel, volstaat voor A1-chat). *(Bij het effectief bouwen: eerst de
  `claude-api`-skill lezen voor actuele model-ID's, prijzen en streaming.)*
- **Kosten:** korte beurten + klein model ≈ verwaarloosbaar per gesprek; Worker-hosting
  valt binnen gratis tiers. Toch **een limiet** per leerling/dag instellen tegen misbruik.
- **Privacy (AVG / minderjarigen / Katholiek Onderwijs):** leerlingtekst gaat naar een
  **derde partij**. → **geen PII** (naam/mail/foto), **niets loggen** wat identificeert,
  **opt-in**, en bij voorkeur een **door de school gehoste sleutel** zodat de school
  spend én data controleert. Dit is een beleidsbeslissing, geen technische.

---

## 4 · Asset-noden (wat de auteur aanlevert vs. puur data)

De motor blijft tekst/data-gedreven; assets komen van de auteur (Drive «Estilo
Exploración», CLAUDE.md §15) of als in-huis SVG. Kaarten hergebruiken de **La Ruta**-SVG
uit de huisstijl (§12, bindend: verzorgde kaartstijl).

| Judge / familie | AUDIO | ILLUSTRATIE / SVG | FOTO | Puur tekst/data |
|---|:--:|:--:|:--:|:--:|
| `classify` grammatica (51,56–63,84,85,88…) | – | soms icoon | – | ✅ |
| `classify` fonetiek/luister (34,36,65–68,96) | **✅** (clip of TTS) | 3-iconen-set (34) | – | data |
| `match` (71,81,86,87,89) | opt. (saludos) | – | – | ✅ |
| `text` getallen/dictee (13,33,94,95) | **✅** | – | – | generator |
| `text` schrijven (23,27,29,30,47,52,59,90,93) | – | mockup (postal 90) | – | ✅ |
| `point` scènes (12,16,37,38,39) | **✅** (klik-wat-je-hoort) | **✅ scène-SVG** | – | – |
| `point` kaarten (17,43,80) | opt. | **✅ La Ruta-kaart** | – | data |
| `point` klemtoon (4,64,69) | opt. (4) | – | – | generator |
| `order` (14,19,21,26,55,72,92) | – | opt. (recept 92) | – | ✅ |
| `speak` (11,31,32,35) | **✅ referentie-audio** | golfvorm (in-huis) | – | Web Speech |
| `sim`-mockups (9,10,15,18,78,79,91) | ober-audio (78) | **✅ UI-mockups** (chat/menu/tweet) | realia-foto (menú/mercado) | tekst |
| `sim` visueel (40,41,42,82) | audio (40,42) | **✅** (stamboom/pop/klok) | – | – |
| `meta` (48,49,50,97,98,99) | – | – | – | ✅ (engine-data) |
| `ai-tutor` (100) | opt. TTS | avatar (cast) | – | LLM |

**Vuistregel:** grammatica-, woordenschat- en meta-judges zijn **puur data** (nul assets,
bouw eerst). Fonetiek/luister/getallen hebben **audio** nodig. `point`-scènes en
`sim`-mockups hebben **SVG/beeld** nodig. **Kaarten = de La Ruta-SVG hergebruiken.**

> **Audio-bron is een keuze (zie knopen §6):** Web Speech **TTS** (offline-ish, robotachtig,
> nul werk) versus **door de auteur ingesproken clips** (mooier, ~30 games aan opnames).

---

## 5 · Integratie — SKILL-routing + unit-HTML + spreiding

### 5.1 · Uitgebreide routeringstabel (aanvulling op `SKILL.md`)

De SKILL kiest in **twee stappen**: eerst de **judge** op basis van het leerstof-signaal,
dan een **skin** voor variatie.

| Leerstof-signaal | Judge | Bron | Voorbeeld-skin |
|---|---|---|---|
| welke persoon/tijd? · ser/estar · por/para · geslacht · b/v · tilde-keuze · sorteren | `classify` | generator/`items` | classify / tetris / mollen / vier-op-een-rij |
| woordenschat · vertaling · land↔nat. · antoniemen · register | `match` | `pairs` | match / memory / tower-defense |
| **getallen · dictee · vervoeging typen · gestuurd schrijven** | `text` 🆕 | `numeros`/`conjugation` | cloze / type-race / slot-machine |
| **klemtoon · lettergreep · fout aanklikken · plaats op kaart/scène** | `point` 🆕 | `tilde`/data | tilde-schutter / kaart / seek-find |
| **juiste volgorde · zinsbouw · stappenplan** | `order` 🆕 | generator-check | zinsmachine / bubbelschieter |
| **uitspraak · shadowing · hardop** | `speak` 🆕 | Web Speech | shadowing / karaoke |
| **vrij schrijven · dialoog · interactie** | `sim` 🆕 | keyword/structuur-check | WhatsApp / menú / tweet |
| **herhaling · spreiding · zelfevaluatie** | `meta` 🆕 | engine-data | leitner / foutenmuseum / heatmap |

**Blokkerende controles blijven gelden** (`SKILL.md`): elke grammaticale vorm uit een
generator (nooit zelf vervoegen/geslacht verzinnen); uniciteit; geen valse afleider;
volledigheid. Voor `text` komt er één bij: **de check gebeurt tegen een geverifieerde
vorm** (generator of dataset), nooit tegen vrije spelling.

### 5.2 · Plaatsing in de unit-HTML (CLAUDE.md §16)

- Elk spel blijft **één standalone offline HTML** in `games/`. In de unit-pagina embedden
  via `<iframe>` in een **«Juega / Oefenen»**-zone of onder de betreffende skill-tab.
- **Kruisverwijzing verplicht (§16, bindend):** cursus (Word/PDF) ↔ HTML: «oefen online: …»
  met consistente iconen/kleuren; en HTML ↔ PowerPoint («zie dia …»).
- **#100 (ai-tutor)** uitsluitend in de **Extra-tab**, gelabeld «vereist internet»; nooit
  in de kern-flow.

### 5.3 · Spreiding & receptief→productief (CLAUDE.md §14, bindend)

De SKILL genereert per thema geen losse spellen maar een **ladder** die de vijf fasen volgt
(herkennen → onderscheiden → ophalen → gestuurd produceren → vrij produceren):

```
receptief ───────────────────────────────────────────► productief
classify/match/point   →   text/order (cloze,volgorde)   →   sim/speak (vrij)
(herkennen/onderscheiden)   (gestuurd produceren)             (vrij produceren)
        └────────── meta-wrappers (leitner/foutenmuseum) recyclen zwakke tags ──────────┘
```

- **Gedeelde tag-woordenschat:** laat elk spel dezelfde `tag`-namen gebruiken als de
  cursus-semáforo/«Lo esencial». De engine logt al per tag (`S.tagStats`), dus beheersing
  **reist mee** tussen spellen, judges én meta-wrappers — en de leitner/foutenmuseum weten
  automatisch welke tags zwak zijn.
- **Recycling zonder waarschuwing (§14):** een woord uit U0 keert in een latere unit terug
  in een **andere skin, ander personage, andere vaardigheid** — de generator/dataset
  trekt hetzelfde item, de skin verschilt. Dat is gratis in dit model.
- **Steun afbouwen:** binnen `text`/`sim` de steun trapsgewijs weghalen (model → woordbank
  → beginletters/zinsframe → cue → niets), zoals §14 vereist; een `text`-spel is pas
  productief als het antwoord niet volledig te kopiëren valt.

---

## 6 · Knopen die de leerkracht moet doorhakken

1. **AI-tutor (#100) — privacy & sleutel.** Mag leerlingtekst (minderjarigen) naar een
   LLM-API (AVG / Katholiek Onderwijs)? Wie **host en betaalt** de sleutel (school-gehost
   aanbevolen)? Zonder deze knoop kan #100 niet gebouwd worden — maar het blokkeert de
   andere 99 niet.
2. **Uitspraak-games (`speak`, #11/31/32/35).** Web Speech **herkenning** vereist in de
   meeste browsers **internet** (audio gaat naar de cloud) → breekt de offline-belofte.
   Aanvaarden we die caveat voor de speak-familie, of houden we het bij shadowing zónder
   scoring (offline)?
3. **#53 Subjuntivo-radar valt BUITEN scope** (subjuntivo/futuro/condicional uitgesloten,
   §2). Schrappen, of ombouwen tot een indicativo-only variant?
4. **Audio-bron voor ~30 games.** TTS (offline, robotachtig, nul werk) versus door de
   auteur **ingesproken clips** (mooier, veel opnamewerk)? Deze keuze bepaalt de
   asset-pijplijn voor alle fonetiek/luister/getallen-spellen.
5. **Akkoord met de volgorde?** U0-eerst, en de vijf nieuwe kern-judges in de volgorde
   **`point` → `text` → `meta` → arcade-skins → `speak`/`sim`** (grammatica/woordenschat
   draaien intussen al op classify/match).
```
