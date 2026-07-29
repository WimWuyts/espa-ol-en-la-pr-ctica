# PLAN — Spellenmotor over de drie cursussen (C4 · C6 · C6+)

> **Status:** plan (goedgekeurd te bouwen ná akkoord). Referentie = C5 (klaar).
>
> **✅ MOTOR-INFRASTRUCTUUR VOLLEDIG GEBOUWD (2026-07-29)** — de herbruikbare
> engine-laag uit §8/§9 stap 1-2 staat er compleet (vóór de per-unit-content, die
> volgt als de cursussen v1 af zijn):
> - **`type`** (§2/§4-A) — getypte-productie-judge: normalisatie (accent-tolerant,
>   ñ behouden), meerdere aanvaarde antwoorden, «closed» + «open» (structuurcheck
>   `must` + «Ver modelo»), accentbalk. → deblokkeert V3·V4·G4·G5·G6.
> - **8 arcade-skins** (§3/§4-C): bestaand `tetris` + nieuw `belt` (sorteerband) ·
>   `mole` (mollenmeppen) · `bubble` (bubbelschieter) · `snake` (sturen) ·
>   `platform` (loop-naar-deur) · `tower` (torenverdediging, levens) · `pinball`
>   (flipper-fysica). Allemaal dunne skins op de classify-judge → volledige M1-rotatie.
> - **`speak`** dekt §2/§4-B al (repeat · shadowing · substitutie-carrousel ·
>   spraakbericht + zelfscan-rubric) — geen extra werk nodig.
> - **Motor-features** (§4-D, `src/features.js`): **Leitner**-doosjes · **streak**-
>   kalender · beheersings-**heatmap** · **confidence**-betting (engine-optie 🎲 ×2) ·
>   **can-do**-zelfscan. Voortgang persisteert (localStorage) en staat op de
>   menu-`index.html`. Direct getest → games/tags/dagen + Leitner promotie/degradatie OK.
> - 10 **demo-pakketten** (`content/es-demo-*`) tonen elke mechaniek; headless
>   Chromium-gerookttest → geen JS-fouten, offline werkend, bestaande games intact.
>
> **Nog te bouwen (volgende ronde):** klassikale set (§8-5: pubquiz · codenames ·
> werewolf · estafette), en de **per-unit 16-slot-content** (§6) per cursus — pas als
> de cursussen v1 af zijn.
> **Aanpak (auteur, 2026-07-27/29):** leerstof-eerst → kies uit de pool van 100 (uitgebreid) →
> bouw de motor als die er nog niet is → lever het spel op. **Minimum 15 games/thema** (mix
> grammatica + woordenschat). **Elke webpagina** bevat oefeningen waar de leerling het antwoord
> **schrijft of zegt** (productief), niet enkel «kies/klik/sleep». **Variatie is de wet:** geen
> mechaniek die zich binnen één cursus blijft herhalen (bv. niet 5× tetris).
> **Bestaande spellen blijven staan.**

---

## 0 · Wat dit plan oplost (de drie bedenkingen van de auteur)

1. **«Veel types voelen hetzelfde.»** — Klopt: van de 100 brainstormvormen zijn er **66 een
   *reskin*** van 10 bestaande templates (classify/match/memory/order/point/sim/speak/tap/tetris/cloze).
   Dat is niet erg *als de jas echt anders is*, maar het wordt lui als dezelfde mechaniek 5× dezelfde
   skin krijgt. → **Oplossing:** een **arcade-rotatieslot** (§3) + een **mechaniek-grootboek** (§5)
   dat per cursus bewaakt dat elke mechaniek maar beperkt terugkeert.
2. **«Te veel kies-het-juiste (klik/sleep).»** — Klopt: 7 van de 10 templates zijn receptief
   (aanwijzen/sorteren/koppelen). → **Oplossing:** een **productieve laag** (§4) — getypte en
   gesproken antwoorden — met een **harde grid-quota van ≥8 productieve slots per pagina** (§3).
3. **«Elk van de 100 moet érgens terugkomen.»** — → **Oplossing:** de **100-dekkingskaart** (§7)
   verdeelt alle 100 (+ de uitbreidingen) over C4·C5·C6·C6+ zodat elke vorm minstens één keer
   ergens leeft, telkens op de leerstof waar hij hoort.

---

## 1 · Eén grid voor de drie cursussen (de kern)

Elke unit-webpagina levert een **vaste receptuur van 16 slots** (minimum 15 gehaald, met marge).
De receptuur is **identiek van vorm** over C4·C6·C6+ (consistentie), maar wordt **per unit met
andere mechanieken/skins ingevuld** (variatie). De verdeling grammatica ↔ woordenschat ↔ transfer
en receptief ↔ productief ligt vast:

| # | Slot | Domein | Modus | Bron-mechaniek (voorbeeld) |
|---|------|--------|-------|-----------------------------|
| 1 | **V1** herkennen | woordenschat | receptief | match / memory / point |
| 2 | **V2** onderscheiden | woordenschat | receptief | classify / tap (sorteerband) |
| 3 | **V3** schrijf het woord | woordenschat | **productief · typen** | cloze-typed / «escribe la palabra» |
| 4 | **V4** beschrijf/vul aan | woordenschat | **productief · typen** | open-kort (definitie → woord) |
| 5 | **V5** zeg het | woordenschat | **productief · spreken** | speak (shadowing / mensaje de voz) |
| 6 | **G1** ontdekken (noticing) | grammatica | receptief | classify (kleur-sorteren) / tap |
| 7 | **G2** onderscheiden | grammatica | receptief | classify (weegschaal/radar) |
| 8 | **G3** bouwen | grammatica | half-productief | order / tetris-variant |
| 9 | **G4** vervoeg (cloze) | grammatica | **productief · typen** | cloze-verbo (klassiek, nagerekend) |
| 10 | **G5** herschrijf/transformeer | grammatica | **productief · typen** | transform-typed |
| 11 | **G6** bouw de zin | grammatica | **productief · typen** | build-a-sentence typed |
| 12 | **G7** vervoeg hardop | grammatica | **productief · spreken** | speak (di la forma / describe) |
| 13 | **M1** arcade-verrassing | gemengd | receptief/reflex | **rotatieslot** (§3) |
| 14 | **M2** mini-simulatie | gemengd | **productief · typen** | sim (chat/kassa/wallapop) |
| 15 | **R1** repaso adaptief | gemengd | gemengd | foutenjacht / quiz adaptief |
| 16 | **(reserve)** unit-parel | vrij | vrij | unit-eigen (bv. stamboom, mapa) |

**Harde quota per pagina (bewaakt door de build):**
- **≥15 games**, mix grammatica + woordenschat (hier 7 G + 5 V + 3 gemengd + 1 reserve).
- **≥8 productieve slots** (V3·V4·V5·G4·G5·G6·G7·M2) = **>50 % productie**, waarvan **≥2 spreken**
  (V5·G7) en **≥6 getypt**. → lost «te veel klik/sleep» structureel op.
- **≥1 klassieke werkwoord-cloze** (G4) met **nagerekende** vormen (motor-generator).
- **M1 mechaniek ≠** de arcade-mechaniek van de vorige unit (rotatie, §3).
- **HTML-hub totaal ≥100 oefeningen** (CLAUDE.md §14ter): elke game trekt uit een pool ≥12 →
  «↻ otra serie» geeft nieuwe reeksen; de 16 games × meerdere rondes + de zelfcorrigerende
  grammaticatools/drills in de panelen halen samen ≥100.

**Waarom een vaste grid?** De auteur vroeg «het afgesproken aantal per pagina, maximaal consistent
met de grid». De grid **gárandeert** het aantal én de mix én de productie-balans, terwijl de
*invulling* (welke van de 100, welke skin) per unit varieert. Consistentie uit het systeem,
variatie uit de inhoud — exact de gouden regel van §13/§14.

---

## 2 · Productieve laag = de belangrijkste uitbreiding (auto-correctie eerlijk)

Vrije tekst offline nakijken kan niet perfect. Daarom **drie productieniveaus**, elk met een
haalbare correctie — zo krijgt elke pagina écht schrijf/zeg-werk zonder valse beloftes:

- **P-gesloten (goud):** de leerling **typt** een antwoord met **één (of enkele) correcte
  oplossing** → auto-check via **normalisatie** (spaties/hoofdletters/accenten-tolerant, `á≈a`
  optioneel, meerdere aanvaarde varianten). Voorbeelden: werkwoord-cloze, «escribe el gentilicio»,
  concordancia typen, getallen in cijfers→letters. **Dit is de motor van V3·G4·G5·G6.**
- **P-halfopen:** de leerling typt een **vrijere** productie (mini-zin) → **structuurcheck**
  (bevat het werkwoord in de juiste persoon? bevat het verplichte element?) + **modeloplossing
  onthullen** ter zelfcorrectie. Voorbeelden: build-a-sentence, tweet in 280, postal-bouwstenen.
- **P-spreken:** **MediaRecorder** (opnemen → terugluisteren → heropnemen) + **zelfevaluatie/
  can-do**; optioneel Web Speech-herkenning **als hint, nooit als enige oordeel** (vereist
  internet). Criteria = begrijpelijkheid/boodschap/interactie. Voorbeelden: shadowing, mensaje
  de voz, «di la forma».

Deze laag wordt gebouwd als **twee nieuwe/uitgebreide templates** bovenop de bestaande:
- **`type`** (nieuw, of uitbreiding van `cloze`): vrij invulveld met normalisatie-judge +
  meerdere aanvaarde antwoorden + «onthul modelo». Dekt V3·V4·G4·G5·G6 en alle P-gesloten/halfopen.
- **`speak`** (bestaat al): uitbreiden met **substitutie-carrousel** en **zelfscan-rubric** voor
  V5·G7.

---

## 3 · Arcade-rotatieslot (M1) — het einde van «5× tetris»

M1 is één slot per unit, maar de **mechaniek roteert** zodat geen enkele arcade-vorm zich binnen
een cursus opdringt. Vaste rotatievolgorde (put uit de bestaande + nieuw te bouwen mechanieken):

`tetris → bubbelschieter → mollenmeppen → platformer → snake → sorteerband → torenverdediging → pinball/flipper`

Per cursus doorloopt M1 deze cyclus; een mechaniek keert **pas terug na de hele cyclus**. Zo staat
tetris in **hooguit één unit** als arcade-slot (i.p.v. 4–5×). Waar tetris didactisch écht past
(vervoeging in kolommen), blijft hij; elders neemt een **andere** mechaniek met dezelfde judge de
plaats in (bv. «woord-in-juiste-veld» → sorteerband i.p.v. tetris).

**Te bouwen arcade-mechanieken** (nieuw, elk = dunne skin op bestaande judge-logica):
bubbelschieter, mollenmeppen, platformer, snake, sorteerband, torenverdediging, pinball. → **7
nieuwe skins**, samen de arcade-variatie voor álle cursussen.

---

## 4 · Uitbreiding van de 100 (het «absolute minimum»)

De 100 blijven de ideeënvijver; we breiden uit met de laag die ontbreekt (**productie + variant-skins**).
Nieuwe items krijgen doorlopende ID's (`WV-101…` in `reservoir.json`), gegroepeerd:

**A · Productieve varianten (typen) — 12 nieuw** (spiegelen bestaande receptieve vormen naar productie):
101 escribe-la-palabra · 102 gentilicio-typen · 103 concordancia-typen · 104 verbo-cloze-libre
(zonder opties) · 105 transforma (sing↔plur, m↔f, afirm↔neg) · 106 completa-la-frase-typen ·
107 número-en-letras · 108 la-hora-en-palabras · 109 pregunta-inversa-typen · 110 dictado-typen
(luister→typ) · 111 reconstruye-la-frase (woorden→zin typen) · 112 define-tú (leerling typt definitie).

**B · Productieve varianten (spreken) — 6 nieuw:** 113 di-la-forma (vervoeg hardop) · 114
describe-la-imagen · 115 substitutie-carrousel-hardop · 116 mensaje-de-voz-taak · 117
lee-en-voz-alta (uitspraak-shadow) · 118 role-play-hardop (halve dialoog inspreken).

**C · Arcade-skins — 7 nieuw:** 119 bubbelschieter · 120 mollenmeppen · 121 platformer · 122
snake · 123 sorteerband · 124 torenverdediging · 125 pinball.

**D · Motor-features (geen spel, wél gevraagd) — 5:** 126 Leitner-doosjes · 127 streak-kalender ·
128 foutenprofiel-heatmap · 129 confidence-betting · 130 zelfscan-can-do. (Adaptief/meta-laag;
één keer bouwen, overal inzetbaar.)

Totaal pool na uitbreiding: **130 vormen**, teruggebracht tot **~12 herbruikbare templates**
(10 bestaand + `type` + de 7 arcade-skins delen grotendeels dezelfde engine).

---

## 5 · Mechaniek-grootboek (bewaakt variatie per cursus)

Per cursus een tabel **mechaniek × unit** met een teller; een build faalt de variatie-check als één
mechaniek te vaak als **hoofdvorm** verschijnt. Streefband per cursus (8–9 units):

| Mechaniek | max. als hoofdvorm/cursus | opmerking |
|-----------|---------------------------|-----------|
| classify | 3 | noticing/sorteren — mag vaker, altijd andere skin |
| match/memory | 3 | vocab-herkennen |
| cloze/**type** | elke unit (G4 verplicht) | maar telkens andere inhoud |
| order | 2 | zinsbouw |
| point | 2 | scène/plattegrond |
| sim | 2 | M2 mini-simulatie |
| speak | elke unit (V5/G7 verplicht) | opname |
| tap | 2 | reflex/onderscheiden |
| **arcade (M1)** | 1 per mechaniek (rotatie §3) | tetris incl. |

Dit is precies de «denk na over varianten»-vraag, meetbaar gemaakt.

---

## 6 · Per cursus — leerstof-eerst inventaris

Werkwijze identiek voor de drie: **(a)** neem de kern-leerstofeenheden van de unit uit de outline →
**(b)** kies per grid-slot de best passende vorm uit de 130-pool (voorrang aan nog-niet-gebruikte,
raadpleeg `coverage.md`) → **(c)** noteer mechaniek + receptief/productief → **(d)** bouw wat
ontbreekt → **(e)** update `coverage.md`. Hieronder de **kern-leerstof per unit** die de inventaris
stuurt (de volledige 16-slot-invulling komt per unit in het `U<N>_cocktail.md`).

### C4 «El despegue» 🔴 — pre-A1 mechaniek (videogedreven)
> **Voorbehoud:** de *taalinhoud* volgt de 14 video's (nog niet in repo). De **grid** en de
> **mechaniekkeuze** liggen wél nu vast; per video-unit vullen we de inhoud in.
> **Focus:** klank↔schriftbeeld, accent/klemtoon, hoogfrequente chunks, basiswoordenschat,
> uitspraak. Grammatica louter functioneel. **Minimale overlap met C5** (mechaniek delen mag,
> leerplandoel-afvinken blijft in C5).

| Unit-type | Kern-leerstof | Grid-accent (afwijking) | Signatuur-vormen uit de 100 |
|-----------|---------------|--------------------------|------------------------------|
| Klank & alfabet | alfabet, klanken, spelling | V-slots → **fonetiek**; G-slots licht | 64 tilde-schutter · 65 b/v · 66 g/j · 67 h muda · 68 ll/y · 70 alfabet-race · 36 minimale paren |
| Accent/klemtoon | aguda/llana/esdrújula | G1–G3 = accent i.p.v. syntax | 4 acento-hero · 69 diftong-splitser · 31 shadowing |
| Chunks & begroeten | saludos, cortesía, klaslokaal-taal | M2 = fake-whatsapp chunks | 9 fake-whatsapp · 116 mensaje-de-voz · 30 definitie/taboe (licht) |
| Getallen & datum | números, fechas | V-productie = **cijfers→letters typen** | 13 pinautomaat · 95 getallen-dictee · 107/108 (nieuw, typen) |
| Basiswoordenschat | kleuren, dagen, klas | standaard grid | 71 memory · 73 mollenmeppen · 76 sorteerband · 39 pinta (SVG) |

C4 zet de **spreek- en typ-productie vroeg** neer (uitspraak = kern), dus V5·G7 wegen hier zwaar.

### C6 «Historias y mundos» 🔵 — A2 → aanzet B1 (9 units, U0–U8)
> Volgt `Outline_Jaar6`. C6 is **nog leeg** → hier komt het meeste bouwwerk. Elke unit de volle
> 16-slot-grid.

| U | Kern-leerstof | Signatuur-grammaticaspellen | Productie-accent |
|---|---------------|------------------------------|-------------------|
| 0 | repaso presente + **perfecto compuesto** | 54-achtig kleur-tijdlijn (classify) · verbo-cloze | G5 «he/has…» typen |
| 1 | **pretérito indefinido** (reg.+onreg.) | verbo-cloze indefinido · tetris-kolommen (arcade-slot) | G4 cloze + G7 «di la forma» hardop |
| 2 | **imperfecto** + **contrast indef./imperf.** | 54 pret/imperf-tijdlijn kleuren · radar | G5 herschrijf verhaal · M2 anekdote-chat |
| 3 | verleden gecombineerd + **por/para** | 51 por/para-poort · order-verhaal | G6 bouw reisverhaal-zin |
| 4 | **OD/OI compleet** (*se lo*, redup.) | 55 pronomen-stapelaar · 52-achtig | G6 «se lo doy» typen · sim-cadeaus |
| 5 | **comparativos + superlativos + que** | 59 comparativo-bouwer · 87 antoniemen-duel | G5 vergelijk-zin · M2 dos-ciudades |
| 6 | **mening met indicativo** + conectoren | 89 register-schuif · conectoren-order | 91 tweet-280 typen · debat-opname |
| 7 | **imperativo** (+ pronomina) | 20 escape/point · imperativo-cloze | 92 recept-imperativo · role-play-opname |
| 8 | **integratie alle tijden** + argumenteren | foutenjacht-mix · 19 detective-tijdlijn | opiniestuk typen + reportage-opname |

Arcade-rotatie C6: U1 tetris · U2 mollenmeppen · U3 platformer · U4 sorteerband · U5 bubbelschieter
· U6 snake · U7 torenverdediging · U8 pinball (U0 = sorteerband-repaso). → tetris **1×**.

### C6+ «El reencuentro» 🟣 — diagnose → A2-motor → verleden (8 units, U0–U7)
> Volgt `Outline_C6plus`. U0 (13 games) **bestaat al** → in dit plan alleen **aanvullen tot de
> 16-slot-grid** (mist vooral productieve typ/spreek-slots en de arcade-rotatie). U1–U7 volledig.
> **Lean:** 1 u/week → de grid blijft 16 slots, maar met **extra gewicht op de verleden tijden**
> (U4–U6) en de doorlopende **mini-opinión** (M2 wordt vanaf U1 een mini-mening).

| U | Kern-leerstof | Aandachtspunt t.o.v. C6 |
|---|---------------|--------------------------|
| 0 | **diagnose-repaso** (presente, género, nacionalidades, getallen) | **al gebouwd** → +V3/V4/G5/G6 typen, +V5/G7 spreken, +arcade-rotatie, +M2 |
| 1 | reflexief · **ser/estar** · **gustar+OI** | M2 = *me gusta… porque* (P3-seed) |
| 2 | **hay/estar** + voorzetsels · **OD-pron.** | point-plattegrond (38/58) · pronomen-cloze |
| 3 | **ir a + inf.** · acabar de · **OI-pron.** | 60 ir-a-raket · M2 = media + *creo que* (indicativo) |
| 4 | **perfecto compuesto** · por/para (intro) | brugtijd; G5 «he viajado» typen |
| 5 | **indefinido** · **OD+OI compleet (se lo)** | figuur uit cultuur; G6 pronomen-zin |
| 6 | **imperfecto** · contrast · comparativos+que | tijdlijn-kleuren · comparativo-bouwer |
| 7 | **imperativo** (+pron.) · **mening indicativo** | P3-capstone: opiniestuk typen + debat-opname |

Arcade-rotatie C6+: U0 tetris · U1 bubbelschieter · U2 mollenmeppen · U3 platformer · U4 snake ·
U5 sorteerband · U6 torenverdediging · U7 pinball.

---

## 6bis · Arcade-retrofit voor de GEBOUWDE cursussen (C5 · C6+) — te bouwen

**Situatie (eerlijk, 2026-07-29):** C5 en C6+ zijn gebouwd **vóór** de 7 nieuwe
arcade-skins bestonden. In de 299 bestaande spellen is `tetris` daarom de **enige**
arcade-vorm: precies **één** arcade-slot per unit, telkens tetris. De andere zeven
skins zijn wél gebouwd en klaar, maar nog niet ingezet in het Spaans.

**Wat er moet gebeuren (goedkoop):** de 8 skins zijn *onderling verwisselbare jassen op
dezelfde classify-judge* — dezelfde content-JSON werkt met elke skin. Het arcade-slot per
unit krijgt dus enkel een **andere skin** (veld `template`, plus titel/subtitel/hub-label
in dezelfde stijl). Géén nieuwe didactische content nodig; de items blijven identiek.

**Rotatie C5** (tetris blijft in U1, waar «vervoeging in kolommen» didactisch het best past):

| Unit | Bestaand arcade-slot | Wordt | Skin |
|---|---|---|---|
| U1 | `es-u1-presente-regular` | **blijft** | `tetris` |
| U2 | `es-u2-familia-tetris` (ser/estar/tener) | → | `belt` sorteerband |
| U3 | `es-u3-irregular-tetris` | → | `mole` mollenmeppen |
| U4 | `es-u4-presente-tetris` | → | `bubble` bubbelschieter |
| U5 | `es-u5-cantidad-tetris` (mucho) | → | `snake` |
| U6 | `es-u6-concordancia-tetris` | → | `platform` |
| U7 | `es-u7-preposicion-tetris` | → | `tower` torenverdediging |
| U8 | `es-u8-haber-tetris` | → | `pinball` |

**Rotatie C6+** (volgt de reeds vastgelegde volgorde hierboven):

| Unit | Bestaand arcade-slot | Wordt | Skin |
|---|---|---|---|
| U0 | `es-c6plus-u0-concordancia-tetris` | **blijft** | `tetris` |
| U1 | `es-c6plus-u1-pronombre-tetris` | → | `bubble` |
| U2 | `es-c6plus-u2-lo-la-tetris` | → | `mole` |
| U3 | `es-c6plus-u3-ir-a-tetris` | → | `platform` |
| U4 | `es-c6plus-u4-participio-tetris` | → | `snake` |
| U5 | `es-c6plus-u5-indef-tetris` | → | `belt` |
| U6 | `es-c6plus-u6-imperf-tetris` | → | `tower` |
| U7 | `es-c6plus-u7-imper-tetris` | → | `pinball` |

→ Resultaat: **alle 8 arcade-vormen** leven in het Spaans, elke skin **1×** per cursus,
tetris van 16× naar 2×. Dit is de invulling van §3 voor de bestaande cursussen.

**Uitvoeringsketen (3 plaatsen per slot, ID's blijven ongewijzigd):**
1. `spaans-motor/make_<unit>_games.py` — de **bron**: `template` + titel + subtitel
   (arcade-woord: Tetris · Cinta · Topos · Burbujas · Serpiente · Puertas · Torres · Pinball),
   en tetris-only opties (`rows`/`speed`) → `rounds` (+ `lives` bij `tower`).
2. `spaans-motor/content/es-…json` — hergenereren via het make-script.
3. `03-build/web/gen_<unit>_web.py` — het **zichtbare hub-label** + de badge-naam.

⚠️ **Niet de game-ID's hernoemen:** de hub-generators linken de spellen op ID
(`…-tetris`). Naam wijzigen breekt die links; de skin-wissel gebeurt in `template` +
labels. (Optioneel later: ID's mee hernoemen in één gecoördineerde pass, samen met de
hub-generators.)

**Inpassen:** neem dit mee in de **digitale sweep** van C5/C6+ (de motor-integratielaag),
niet als losse pass — dan hergenereer je elke unit één keer.

---

## 7 · 100-dekkingskaart (elk idee komt érgens terug)

Doel: **alle 100 (+ uitbreidingen)** minstens één keer, op de cursus/unit waar ze passen.
Toewijzing per blok (samenvatting; het detail komt in `coverage.md` per unit):

- **Arcade & mechaniek (1–8, 71–77):** verdeeld over de arcade-rotatieslots van **C4·C5·C6·C6+**
  (elk 8 units → samen ~32 arcade-slots, ruim genoeg voor alle arcade-vormen minstens 1×).
- **Simulatie & rollenspel (9–20):** M2-slot. WhatsApp/Insta/bel/kassa → C4–C5; wallapop/consulta/
  metro/detective/escape → C6·C6+ (passen bij imperativo, verleden, onderhandelen).
- **Generatief & taalspel (21–30):** G3/G5/M2. Zinsmachine/mad-libs/foutenjacht → elke cursus;
  omgekeerde quiz/definitiegenerator → C6·C6+.
- **Audio & uitspraak (31–36):** V5/G7 + fonetiek-slots. Zwaartepunt **C4** (uitspraak = kern),
  shadowing/minimale-paren ook in C5–C6.
- **Visueel & ruimtelijk (37–43):** point/classify. Kamer/plattegrond/klok/stamboom/kaart →
  C5·C6·C6+ waar het thema past (wonen, familie, tijd, geografie).
- **Klassikaal (44–47):** aparte **klassikale set** (pubquiz/codenames/werewolf/estafette) — één
  keer bouwen, inzetbaar in élke cursus als klasmoment (buiten de 16-slot-grid).
- **Meta & strategie (48–50, 97–99, 126–130):** motor-features, over álle cursussen (Leitner,
  streak, heatmap, confidence, can-do).
- **Grammatica-mechaniek (51–63):** G-slots, gekoppeld aan de exacte leerstof:
  por/para→C6-U3/C6+-U4 · gustar→C6+-U1 · pretérito/imperfecto→C6-U1-2/C6+-U5-6 · pronomen-stapelaar
  →C6-U4/C6+-U5 · ser/estar→C6+-U1 · hay/está→C6+-U2 · comparativo→C6-U5/C6+-U6 · ir-a→C6+-U3 ·
  este/ese, muy/mucho, posesivo→C5/C6+-vroeg. **Subjuntivo-radar (53) = buiten scope → niet bouwen.**
- **Fonetiek/spelling (64–70):** **C4** (kern) + repaso in C5-U0.
- **Realia (78–83):** M2/sim + cultuur. Menú/tapas→eten-units · kaart-LatAm→geografie · fiesta→cultuur.
- **Woordenschat diep (84–89):** V3/V4. Woordfamilie/collocatie/prefijos/antoniemen/valse-vrienden/
  register → elke cursus, oplopend in diepte naar C6.
- **Productie & schrijven (90–93):** V3/V4/M2 typen. Postal/tweet/recept/dagboek → C5–C6·C6+.
- **Luisteren (94–96):** een **luister-slot** in R1/M2 (podcast-gaten, getallen-dictee, wie-zei-wat)
  — koppelt aan de verplichte luisterdialoog per unit (CLAUDE.md §14ter).
- **AI-tutor (100):** online component, **apart** (API/hosting); optioneel bovenop élke hub.

Zo staat **elke** van de 100 minstens één keer op de juiste plek, met de mechaniek-rotatie die
herhaling-met-dezelfde-jas voorkomt.

---

## 8 · Wat er concreet nog gebouwd moet worden (samengevat)

**Nieuwe/uitgebreide templates (één keer, voor alle cursussen):**
1. `type` — getypte-productie-judge (normalisatie + meerdere antwoorden + onthul-modelo). *[grootste winst]*
2. `speak`-uitbreiding — substitutie-carrousel + zelfscan-rubric.
3. 7 arcade-skins — bubbelschieter · mollenmeppen · platformer · snake · sorteerband · torenverdediging · pinball.
4. Motor-features — Leitner · streak · heatmap · confidence · can-do (meta-laag).
5. Klassikale set — pubquiz · codenames · werewolf · estafette (buiten de grid).

**Content (per unit, volgens de 16-slot-grid):**
- **C6:** U0–U8 volledig (nu leeg) — grootste blok.
- **C6+:** U0 aanvullen tot 16 slots (+typen/spreken/arcade/M2); U1–U7 volledig.
- **C4:** grid + mechaniek vastgelegd; content per video-unit zodra de video's in de repo staan.
- **C5 (referentie/retrofit, optioneel):** U0 aanvullen (miste 4 mechanieken), U5 +tap,
  U6–U8 games nog bouwen — enkel als de auteur C5 ook naar de nieuwe grid wil optrekken.

**Reservoir-boekhouding:** `reservoir.json` uitbreiden met WV-101…130; `coverage.md` per unit
bijwerken met de exact gebruikte ID's; per unit een `U<N>_cocktail.md` met de 16-slot-invulling.

---

## 9 · Volgorde van uitvoering (voorstel — ná akkoord)

1. **Templates eerst:** `type` + `speak`-uitbreiding (deblokkeert de productie-quota overal).
2. **Arcade-skins + motor-features** (deblokkeert de rotatie en de meta-laag).
3. **Pilootunit** in elke cursus volgens de grid (bv. C6-U1 indefinido · C6+-U1 · C4-klank-unit) →
   auteur keurt de grid-invulling goed (zoals de golden sample U0/U5).
4. **Opschalen** unit per unit, met de mechaniek-grootboek- en dekkings-check na elke unit.

> Consistentie = dezelfde 16-slot-grid, dezelfde ≥8-productie-quota, dezelfde rotatie en dezelfde
> boekhouding over C4·C6·C6+. Variatie = per unit andere mechanieken/skins/inhoud uit de 130-pool.
