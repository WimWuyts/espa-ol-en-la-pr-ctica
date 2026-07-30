# Bouwplan — oefeningen-sweep C5 & C6+

> Concreet plan voor de uitvoering van de twee blueprints (`00-brondocumenten/gap-analyse/`)
> plus de getypte woordenschatladder. Beslissingen A–D staan in `FEEDBACK_BLUEPRINTS.md` §6
> en zijn bindend. Stand van het project: `HANDOVER_VOLGENDE_CHAT.md`.

## Het uitgangspunt: herbouwen is goedkoop, regressie is duur

Alles is **gegenereerd**. Een hub opnieuw bouwen is één commando van enkele seconden:

```
python3 03-build/web/gen_u3_web.py      # één hub
node spaans-motor/build.mjs             # alle spellen
python3 03-build/make_zip.py C5         # levering
```

Er hoeft dus niets «met de hand herbouwd» te worden — de **inhoud blijft staan**, alleen de
generatoren wijzigen. Het echte risico is **stille regressie**: iets verdwijnt zonder dat
iemand het merkt. Dat is in dit project al gebeurd (17 gebouwde spellen stonden in géén hub).

**Daarom is er nu een vangnet:**

```
python3 03-build/check_regressie.py     # na ELKE stap draaien
```

Het vergelijkt alle 17 hubs met de baseline in `03-build/.baseline/`: spellen, oefenblokken,
bouwer-aanroepen en bestandsgrootte. **Regel: er mag van alles bij komen, er mag niets weg.**
Faalt met exitcode 1 en een lijst. Bewuste wijziging? Pas ná goedkeuring `--herijk` draaien.

Baseline bij aanvang: **17 hubs · 296 spellen · 394 bouwer-aanroepen · 238 oefenblokken**.

---

## Fase 1 · Gereedschap (eenmalig, blokkeert al de rest)

### 1a. Bouwers samentrekken → `03-build/web/hub_drills.py`

`buildChoice`, `buildMatch`, `buildOrder`, `buildOdd`, `buildInlineExercises` en
`buildRecorders` staan **17× gekopieerd**, één keer per `gen_*_web.py`. Trek ze samen in één
module die de JS als string levert.

**Aanpak met vangnet — dit is een no-op refactor:**
1. module maken uit de canonieke kopie;
2. alle 17 generators laten importeren i.p.v. hun eigen kopie;
3. alle 17 hubs opnieuw genereren;
4. `check_regressie.py` → moet **schoon** zijn;
5. extra: byte-diff met de vorige hub-output. Verschillen mogen alleen whitespace zijn.

Wijkt een hub inhoudelijk af, dan had die generator een lokale variant van een bouwer.
Die variant expliciet als optie in de module opnemen — niet stilzwijgend gelijktrekken.

### 1b. `buildType` toevoegen (in de nieuwe module)

Getypte drill in het paneel. Contract, afgeleid van de blueprints + beslissingen A/C:

```js
buildType('gx_perfecto', {
  title: 'Experiencias', desc: '…',
  perBlock: 10,                 // beslissing A: visuele blokken…
  items: [ {q:'Hoy Lucía ___ (visitar) el Prado.', ans:'ha visitado',
            alt:['ha visitado'], why:'haber + participio', hint:'h_ v_______'} ]
});
```

Eisen (uit beide blueprints): `Comprobar` · `Reintentar` · score `x / n` **over de volledige
set** · doorlopende nummering over de blokken · correcte antwoorden blijven staan bij
`Reintentar` · toetsenbordbediening · zichtbare focus · ARIA-labels · fout niet alleen met
kleur · geen horizontale overflow op 360 px.

**Accentregel (beslissing C)** — implementeer als vlag per oefening:
`accents:'strict'` bij werkwoordsvormen, `accents:'soft'` bij woordenschat (eerste poging
tolerant, correctie toont het accent). `ñ` blijft altijd betekenisdragend.

### 1c. Woordzoeker-component (`C5-U7-NAT-01`)

Nieuw; bestaat nog niet. 15×15 raster, horizontaal/verticaal/diagonaal, voor- en achterwaarts.
Intern genormaliseerd (`SALON`, `BANO`, `JARDIN`, `SOFA`), in de woordlijst mét accenten.
Bedienbaar met muis, touch **en** toetsenbord; lijstweergave als toegankelijk alternatief.
Oplossing pas na `Rendirse`. `Otra serie` verplaatst woorden, voegt er nooit toe of af.

---

## Fase 2 · Unit per unit — VOLGORDE BESLIST (auteur, 2026-07-29)

**Niet meer per cursus, maar per unitnummer, beide cursussen samen.** De auteur heeft U0
het snelste nodig.

| Ronde | Bouw | Bevat |
|---|---|---|
| **1** | **C5 U0 + C6+ U0** | blueprint-oefeningen · typ-woordenschatladder · luisterblok · QR-pagina |
| 2 | C5 U1 + C6+ U1 | idem |
| 3 | C5 U2 + C6+ U2 | idem |
| … | … tot C5 U8 (C6+ eindigt bij U7) | |

Elke ronde levert **twee complete units** op: hub + print + PDF + 2 PowerPoints, mét
regressiecheck. Zo heeft de auteur na ronde 1 meteen bruikbaar lesmateriaal in plaats van
een half afgewerkte cursus.

**Cursuslaag — BINDEND (auteur):** in de printcursus wordt **alleen toegevoegd, nooit
weggelaten**. Bestaande oefeningen, secties en nummering blijven staan; nieuwe oefeningen
krijgen een eigen subsectienummer erachter.

**Per unit dezelfde vijf stappen:**
1. oefeningdata toevoegen in de generator (canonieke inhoud uit de blueprint, ID exact);
2. `console.assert` op het itemaantal (blueprint eist dit expliciet);
3. hub genereren;
4. `check_regressie.py`;
5. headless smoke-test: paneel rendert, `Comprobar`/`Reintentar` werken, geen consolefouten.

### Correcties op de canonieke inhoud (goedgekeurd door de auteur)

| Waar | Wat | Correctie |
|---|---|---|
| C5-U3-NAT-01 item 12 | `ponerse de pie` als «no reflexivo» — maar *ponerse* ís pronominaal | vervang door een echt niet-reflexief item (`desayunar` / `salir de casa`) |
| C6+ §5.9 item 15 | *«Todos **cantábamos** aunque no cantábamos bien»* — antwoord staat in de zin | tweede helft herschrijven: *aunque no teníamos buena voz* |
| C6+ §5.10 item 25 | cue `compartirlo` bevat het pronomen al | cue wordt `compartir`; het aanhechten van *-lo* is het leerdoel |
| C5-U5-NAT-01 / U6-NAT-01 | woordgroepen in «20 verbos»-sets | behouden als klikoefening; niet gebruiken als typ-item |
| C5-U1-NAT-01 | 20 nationaliteiten typen met verplichte accenten | `accents:'soft'` (beslissing C) |
| C5-U4-NAT-01 | twee dropdowns = selecteren, geen productie | omzetten naar `buildType` met twee invulvelden |

Elke correctie wordt in het implementatierapport vermeld — de blueprints eisen dat
afwijkingen niet stilzwijgend worden opgelost.

---

## Fase 3 · Woordenschatladder (motor, uitrol pilot)

De U3-pilot uitrollen over de overige 16 units:

```
python3 spaans-motor/make_vocab_type_games.py C5 <n>
python3 spaans-motor/make_vocab_type_games.py C6+ <n>
node spaans-motor/build.mjs
```

Per unit 5 getypte oefeningen (12 items × 3 rondes; open productie 8). Daarna de groep
«⑥ Escribir» in de hub-generator toevoegen en de hub opnieuw bouwen. Grotendeels
generatorwerk; enkel de pool-rapportage per unit nakijken (zie de dry-run-uitvoer).

---

## Fase 4 · Cursuslaag (print → PDF → PPTX)

Het zwaarste blok. Zeven oefeningen, elk door de volledige keten:

| Oefening | Unit | Items |
|---|---|---:|
| `C5-U2-NAT-01` possessivos | C5 U2 | 8 |
| `C5-U5-NAT-02` adjetivos de comida | C5 U5 | 20 |
| `C5-U7-NAT-02` imperativo | C5 U7 | 25 |
| `c6p-u1-ser-estar-30` | C6+ U1 | 30 |
| `c6p-u4-perfecto-20` | C6+ U4 | 20 |
| `c6p-u5-indefinido-30` | C6+ U5 | 30 |
| `c6p-u7-imperative-25` | C6+ U7 | 25 |

Per oefening: bewerkbare HTML-laag → PDF opnieuw renderen → docent-PPTX (mét sleutel) →
leerling-PPTX (zonder). Antwoordruimte volgens §14 (`wl`, `wcols`, `wtab`, `wbox`),
doorlopende nummering, geen pagina-einde midden in een item, geen oplossingen in de
leerlingweergave.

---

## Fase 5 · Poortwachter

`03-build/check_unit.py <cursus> <unit>` — meet per unit de bindende quota uit CLAUDE.md
§14/§14bis/§14ter en faalt met een lijst: aandeel productief vs. receptief, ≥6 getypt,
≥2 spreken, ≥1 getypte werkwoord-cloze, ≥1 luisterdialoog, ≥1 Lectura, ≥8 speltypes,
pool ≥12 per spel, ≥100 interacties op de hub, geen meta/placeholders (§18).

Daarna: alle hubs opnieuw genereren, `check_regressie.py --herijk`, verse zips.

---

## Wat je per fase terugkrijgt

| Fase | Oplevering | Kan zonder jouw tussenkomst? |
|---|---|---|
| 1 | module + `buildType` + woordzoeker, regressiecheck schoon | ja |
| 2 | 14 bijgewerkte hubs, implementatierapport met afwijkingen | ja, na goedkeuring van de eerste unit |
| 3 | 16 units × 5 getypte oefeningen | ja |
| 4 | 7 units × (PDF + 2 PPTX) | ja, maar visuele controle door jou is aan te raden |
| 5 | conformiteitscheck + verse zips | ja |

**Aanbevolen ritme:** fase 1 in één sessie (met de refactor-diff als bewijs), dan per fase
één sessie. Elke sessie eindigt met `check_regressie.py` schoon en een push, zodat een
volgende chat koud kan verdergaan.

---

## Fase 2b · Luistervaardigheid — de grootste inhoudelijke leemte

**Meting (2026-07-29):** C5 heeft **9/9** units met een `Lectura`-paneel, maar **0/9** met een
luisterpaneel. Wat er is, zijn 14–21 losse TTS-knopjes die één woord uitspreken. Er is dus
geen luisterbegrip — dat schendt §14ter (≥1 luisterdialoog per unit mét begripstaak).
C6+ heeft hetzelfde beeld.

### Wat er al klaarstaat

- **C4 heeft de pijplijn al**: `03-build/web/gen_audio.py` (Google Cloud TTS, **eigen stem per
  spreker** → klinkt als een echt gesprek) en per unit een `escucha`- én `comprension`-component.
- ⚠️ **Er staat nog geen enkele mp3 in de repo** — het script is nooit gedraaid; het vraagt
  `GOOGLE_TTS_API_KEY`. C4's luisterblokken draaien nu op video + TTS-transcript.
- C5/C6+ hebben geen videobron, dus daar moet het van **audio** komen.

### Voorstel: één luisterblok per unit, dat met én zonder API-sleutel werkt

Bouw het component zo dat de audiobron verwisselbaar is:

1. **nu, zonder sleutel** — browser-TTS speelt de dialoog af, met een ander stemprofiel
   (toonhoogte/tempo) per spreker. Werkt offline, is robotisch maar bruikbaar.
2. **later, mét sleutel** — `gen_audio.py` produceert echte mp3's per unit; het component
   pakt die automatisch op zodra ze bestaan. Geen herbouw van de oefeningen nodig.

**De luisterladder per unit** (volgt `VIER_VAARDIGHEDEN_GEINTEGREERD.md`):

| Trede | Taak |
|---|---|
| vóór het luisteren | situatie + wie spreekt + 3 sleutelwoorden vooraf |
| globaal begrip | waar gaat het over? · 3 keuzes |
| gericht luisteren | 5 detailvragen (getallen, tijd, plaats, naam) |
| scannen | juist/fout **met bewijs** uit het fragment |
| meelezen | transcript verschijnt pas ná de taken (klik-om-te-horen per zin) |
| productie | schriftelijke of gesproken reactie op het fragment |

**In print:** de begripstaak met antwoordruimte + een QR naar het fragment op de hub.

### Leesvaardigheid

`Lectura` bestaat wél, maar is per unit één tekst. Uitbreiden volgens §14bis met de volledige
route: voorspellen → globaal → **scannen** → juist/fout **met bewijs** → betekenis uit context
→ productieve reactie. Dat is uitbreiding van een bestaand paneel, geen nieuw component.

---

## Fase 2c · QR naar externe oefenpagina's — LET OP: wijkt af van de blueprints

De auteur vraagt in de cursus te verwijzen naar de **exacte deelpagina** van *La página del
español* via een QR-pagina.

⚠️ **Dit spreekt de blueprints tegen.** C5 §0: *«Gebruik bronvermelding alleen in
ontwikkelaarsdocumentatie. Toon de naam of vormgeving van de externe website niet aan
leerlingen.»* C6+ §6.1 zegt hetzelfde («alleen in docentmetadata»). De auteur mag die keuze
herzien — dit is enkel de vastlegging dat het een bewuste wijziging is, geen vergissing.

**Juridisch is linken onproblematisch** (linken ≠ overnemen); de items in de cursus blijven
zelf geschreven. Aandachtspunten zijn praktisch:

- **link-rot** — externe pagina's verdwijnen of veranderen;
- **internet vereist** — botst met de offline-belofte van de hub;
- **geen controle** over wat er op die pagina staat (advertenties, niveau, taalvariant).

**Aanbevolen uitvoering — één QR-pagina per unit, niet verspreid:**

- één printpagina achteraan de unit: **«Práctica extra en línea»**, met per onderwerp een
  QR + de titel van de oefening (in het Spaans, zonder de huisstijl van de bronsite over te nemen);
- dezelfde lijst in de hub-tab **«Extra · bronnen»**, waar externe bronnen al thuishoren;
- expliciet gelabeld als **online** (≠ de offline hub);
- één plaats om te onderhouden bij link-rot, in plaats van dertien verspreide QR's.

**Technisch kan dit nu al:** `segno` is beschikbaar en de externe URL's zijn bekend, dus deze
QR-codes worden **echt** — in tegenstelling tot de hub-QR's, die op de Netlify-URL wachten (§18).
