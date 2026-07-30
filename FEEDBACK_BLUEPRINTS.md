# Feedback op de twee native-oefening-blueprints

> Betreft: `C5_NATIVE_EXERCISE_INTEGRATION_CLAUDE_CODE_WEB_v1.0.md` en
> `C6PLUS_NATIVE_EXERCISE_INTEGRATION_CLAUDE_CODE_WEB_v1.01.md` (auteur, 2026-07-29).
> Geschreven na inhoudelijke controle tegen de bestaande repo. **Bewaar de blueprints
> zelf in `00-brondocumenten/gap-analyse/`** — dit document is enkel het commentaar erop.

## Oordeel

Bruikbaar zoals ze zijn: vaste ID's, exacte itemaantallen, canonieke inhoud, plaatsing,
QA-checklist én validatiecode. De auteursrechtelijke lijn is correct (alleen oefenvorm en
aantal ontleend; items zelf geschreven) en de scope-grens (geen futuro simple, condicional,
subjuntivo) klopt met III-Spa-d. Hieronder wat er vóór de bouw moet worden bijgesteld.

---

## 1 · De drie lagen — wat waar hoort

De auteur onderscheidt drie lagen; dit dossier volgt die indeling.

| Laag | Status | Wat de blueprints hier toevoegen |
|---|---|---|
| **Spellen** (motor) | **afgesproken, niet wijzigen** | niets — de arcade-rotatie en de getypte woordenschatladder (U3-pilot) blijven de afspraak |
| **Oefeningenpagina** (panelen «Vocabulario»/«Gramática» in de hub) | **hier zit het gat** | het grootste deel van beide blueprints landt hier |
| **Cursus zelf** (print + PDF + PPTX) | **ook hiaten**, door de blueprints benoemd | C5: 3 oefeningen · C6+: 4 oefeningen |

Belangrijke observatie: de blueprints plaatsen bijna alles in *«tab Woordenschat»* en
*«tab Gramática»* — dus precies in de panelen, niet in de spellensectie. Dat is exact waar
de meting het tekort aantoonde (326 klik-oefeningen, 0 typwerk).

---

## 2 · Ze sluiten het gat maar half

Geteld per platform, **op de digitale hub**:

| | Typen | Klikken/kiezen |
|---|---|---|
| **C5** | 65 (U1 · U7 · U8) | **132** — 6 vierkeuze-oefeningen + U4's twee dropdowns |
| **C6+** | 70 (U1 · U3 · U6) | 65 — 3 match-oefeningen |

C6+ is in balans; **C5 blijft 2:1 klikken**. Aandachtspunt: C5-U4 «Gustos en ruta» werkt met
twee dropdowns — dat is *selecteren*, geen productie. Juist bij `gustar` moet de leerling
`me gustan` zelf schrijven.

**De woordenschatladder blijft open.** Alle vocabulaire-toevoegingen zijn *definitie → kies
het woord* (herkennen). Er zit geen NL→ES-ophalen, geen dictee, geen «schrijf het woord» in.
De vijf gegenereerde oefeningen uit de U3-pilot vullen precies dat aan en conflicteren niet.

---

## 3 · Inhoudelijke fouten in de canonieke inhoud

Deze zouden 1-op-1 doorrollen naar de leerling en moeten dus eerst gecorrigeerd worden.

1. **C5-U3-NAT-01, item 12** — `ponerse de pie` wordt als controle-item ingezet waarbij de
   leerling «no reflexivo» moet kiezen, maar *ponerse* **is** pronominaal. Item 17
   (`regresar a casa`) klopt wél als niet-reflexief. → vervang item 12 door een echt
   niet-reflexief werkwoord (`desayunar`, `salir de casa`).
2. **C6+ §5.9, item 15** — *«Todos **cantábamos** aunque no cantábamos bien.»* Het antwoord
   staat letterlijk verderop in dezelfde zin. → herschrijf de tweede helft
   (bv. *aunque no teníamos buena voz*).
3. **C6+ §5.10, item 25** — de infinitiefcue is `compartirlo`, met het pronomen er al in;
   moet `compartir` zijn — het aanhechten van *-lo* is juist het leerdoel.
4. **Granulariteit** — in sets die «20 verbos» heten staan woordgroepen:
   `calentar en el microondas` (C5-U5-NAT-01) en `subir la cremallera` (C5-U6-NAT-01).
   Als klikoefening prima, als typoefening foutgevoelig.
5. **Afweging, geen fout** — C5-U1-NAT-01 laat 20 nationaliteiten typen mét verplichte
   accenten (*puertorriqueño*, *panameño*, *nicaragüense*) in het eerste jaar. Advies:
   eerste poging accent-tolerant, accent expliciet tonen in de correctie.

---

## 4 · Overlap met wat er al is

Gecontroleerd tegen `spaans-motor/content/`: **élk onderwerp uit beide blueprints bestaat al
als spel** — `es-u1-pais-nacionalidad`, `es-c6plus-u0-pais-nacionalidad`,
`es-u0-numeros-match`, `es-c6plus-u4-participio-tipo`, `es-c6plus-u6-imperfecto`,
`es-c6plus-u5-indefinido`, `es-u7-imperativo-cloze`, `es-c6plus-u1-reflexivos`, …

De blueprints zeggen «vermijd duplicatie» maar toetsen dat niet tegen de inventaris.
Dat maakt beslispunt D hieronder noodzakelijk.

---

## 5 · Technische landing

| Blueprint-type | Landt op |
|---|---|
| `fill-gap` (typen) | nieuwe **`buildType`** in het paneel |
| `match` / `lexicon-grid` | bestaande motor-templates (`match`, `memory`, `point`) of native in het paneel |
| woordzoeker (C5-U7-NAT-01) | **nieuw component** — bestaat nog niet |
| cursusoefeningen | bewerkbare HTML-laag → PDF → PPTX (docent mét sleutel) |

⚠️ `buildChoice` c.s. staan **17× gekopieerd**, één keer per `gen_*_web.py`. Trek ze eerst
samen in `03-build/web/hub_drills.py`, anders kost elke latere correctie zeventien bestanden.

---

## 6 · De vier beslispunten — BESLIST door de auteur (2026-07-29)

| # | Kwestie | **Beslissing** |
|---|---|---|
| **A** | C5 eist «splits niets»; wij spraken 12×3 rondes af. | **C6+-regel overal.** Visuele blokken van 10–12 met tussenscherm, **doorlopende nummering en één totaalscore** over de volledige canonieke set. De set blijft dus compleet; alleen de presentatie wordt opgedeeld. |
| **B** | «Geen iframe» vs. onze bestaande spelmodal. | **Geldt enkel voor de nieuwe oefeningen** — die worden native in het paneel. De bestaande iframe-spelmodal (base64, offline) blijft ongemoeid; geen herbouw van de 309 spellen. |
| **C** | Accentbeleid. | **Gedifferentieerd.** Werkwoordsvormen: accent **verplicht** (*hablo ≠ habló*, *habéis*, *leído*). Woordenschat: eerste poging **accent-tolerant**, correctie toont het juiste accent expliciet. |
| **D** | Overlap met bestaande spellen. | **Náást elkaar, verschillende treden.** De nieuwe sets = de grote canonieke reeks (20–30 items) in het paneel; de bestaande korte spellen blijven als lagere trede in de spellensectie. Niets verwijderen. |

Deze vier gelden als **bindend** voor de implementatie van beide blueprints.

---

## 7 · Voorgestelde volgorde

1. `hub_drills.py` (gedeelde bouwers) + **`buildType`** — het gereedschap eerst.
2. **C6+** (11 oefeningen, beter uitgebalanceerd, kleiner).
3. **C5** (13 oefeningen) mét de correcties uit §3.
4. **Cursuslaag**: de 3 (C5) + 4 (C6+) printoefeningen → bewerkbare HTML → PDF → PPTX.
5. Woordzoeker-component (C5-U7) — apart, want nieuw.
6. Conformiteitscheck (`check_unit.py`) als poortwachter, zie `HANDOVER_VOLGENDE_CHAT.md` §3.

**Omvang:** C5 raakt 8 hubs + 3× print/PDF/PPTX; C6+ 6 hubs + 4× print/PDF/PPTX; samen ~470
nieuwe items. Het zwaartepunt zit in de PowerPoint/PDF-synchronisatie, niet in de oefeningen.

---

## 8 · Laag 3 — de cursus zelf (print)

De auteur bevestigt dat ook de **cursusoefeningen** hiaten hebben. De blueprints benoemen
er zeven, die via de bewerkbare HTML-laag → PDF → PPTX moeten lopen:

| Oefening | Unit | Items | Inhoud |
|---|---|---:|---|
| `C5-U2-NAT-01` | C5 U2 | 8 | herschrijven met possessivum (§2.3 nieuw) |
| `C5-U5-NAT-02` | C5 U5 | 20 | smaak-/textuuradjectieven uit woordbank, mét congruentie |
| `C5-U7-NAT-02` | C5 U7 | 25 | bevestigende tú-imperatief, vijf themablokken |
| `c6p-u1-ser-estar-30` | C6+ U1 | 30 | ser/estar-contrast in presente |
| `c6p-u4-perfecto-20` | C6+ U4 | 20 | pretérito perfecto in reiscontext |
| `c6p-u5-indefinido-30` | C6+ U5 | 30 | indefinido als biografische tijdlijn |
| `c6p-u7-imperative-25` | C6+ U7 | 25 | gezondheids-/milieuadvies in tú-imperatief |

**Regels die hier gelden** (uit CLAUDE.md §14 + de blueprints):
- élke oefening krijgt **type-correcte antwoordruimte** (`wl` schrijflijn, `wcols`, `wtab`,
  `wbox`) — de leerling schrijft écht op papier;
- **geen oplossingen in de leerlingweergave**; sleutel enkel in het docentmateriaal;
- geen pagina-einde midden in een item; lange sets in betekenisvolle blokken met
  **doorlopende nummering** (beslissing A);
- PDF, bewerkbare laag en beide PPTX blijven inhoudelijk gesynchroniseerd.

Dit is het zwaarste blok qua uitvoering (regeneratie van PDF én twee PowerPoints per unit),
maar didactisch het minst risicovol: de inhoud ligt canoniek vast.
