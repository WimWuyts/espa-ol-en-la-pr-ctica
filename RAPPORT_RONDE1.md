# Implementatierapport — fase 1 + ronde 1

> Werkbranch `claude/spanish-course-development-jx25ay`. Regressiecheck schoon na elke stap.

---

## Fase 1 · Gereedschap

### 1. Bouwers samengetrokken → `03-build/web/hub_drills.py`

**Meting eerst.** De aanname «zes bouwers staan 17× gekopieerd» klopte maar half:

| Bouwer | Kopieën | Wat het is |
|---|---|---|
| `buildChoice` · `buildOrder` · `buildOdd` | 16 identiek | echte duplicatie |
| `buildMatch` | 16 identiek **+ 1 afwijkende in C5 U0** | duplicatie + lokale variant |
| `speak` · `makeRecorder` · `exSample/exEsc/exFmt` | 17 identiek | echte duplicatie (stond niet in de opdracht) |
| `buildInlineExercises` · `buildRecorders` | **17× verschillend** | géén duplicatie — dit is de *inhoud* van de unit |

`buildInlineExercises` en `buildRecorders` zijn dus **niet** samengetrokken: die bevatten de
oefeningen en opnameopdrachten van die ene unit. Ze samentrekken zou inhoud tot code maken.
Wél samengetrokken zijn `speak`, `makeRecorder` en de drie helpers, die er niet bij stonden.

C5 U0 bleek een oudere generatie: het kent dezelfde motoren onder de namen
`exChoice/exMatch/exOrder/exOdd` plus een eigen `buildMatch(el,title,pairs)` met positionele
argumenten. Beide varianten zijn **expliciet** in de module opgenomen (`engines(prefix="ex")`
en `MATCH_LEGACY_JS`) in plaats van stilzwijgend gelijkgetrokken.

**Bewijs dat het een no-op was:** alle 17 hubs zijn na de refactor **byte-identiek** aan de
regeneratie ervoor — strenger dan de gevraagde «identiek op whitespace na». De splice gebeurt
per functie, zodat ook de tussenliggende commentaarregels blijven staan.

### 2. `buildType` — getypte drill

`Comprobar` · `Reintentar` · `Ver solución` · score over de volledige set · doorlopende
nummering over visuele blokken van 10–12 · Enter springt naar het volgende veld · zichtbare
focus (3 px outline) · `aria-label` + `aria-invalid` + `aria-live` · fout draagt een symbool
én tekst (niet enkel kleur) · geen horizontale overflow op 360 px. Alles getest in Chromium.

`accents:'strict'` bij werkwoordsvormen, `'soft'` bij woordenschat (beslissing C); de ñ blijft
in beide standen betekenisdragend — getest: `el ano` wordt afgekeurd voor `el año`, `el jardin`
wordt aanvaard voor `el jardín` met het accent expliciet in de correctie.

**Afwijking van het contract, bewust:** `Ver solución` verschijnt pas ná een tweede poging.
Mijn eerste versie gaf de oplossing meteen na één `Reintentar`; dat botst met «ophalen vóór
opnieuw tonen» (§14).

### 3. Luistercomponent `buildEscucha`

Zes treden, verwisselbare audiobron. Zonder mp3 leest browser-TTS het guion voor met een eigen
stemprofiel per spreker; zodra `audio/<cursus>_U<n>.mp3` bestaat wordt die automatisch gebruikt,
zonder de oefeningen te herbouwen. De mp3 wordt **pas bij de eerste klik** geladen — anders logt
de browser een netwerkfout bij het openen van elke hub en is «geen consolefouten» geen bruikbare
rooktest meer.

Ook nieuw: **`buildLectura`**, de leesroute van §14bis (voorspellen → globaal → scannen →
juist/fout met bewijs → betekenis uit context → productie). Scannen is getypt, niet aangeklikt.

---

## Ronde 1 · C5 U0 en C6+ U0

### Getelde itemaantallen

| ID | Items | Eis | `console.assert` |
|---|---:|---:|---|
| `C5-U0-NAT-01` | 11 | 11 | ✓ |
| `C5-U0-NAT-02` | 11 | 11 | ✓ (met TTS-knop, zoals de blueprint vraagt) |
| `c6p-u0-nationalities-20` | 20 paren | 20 | ✓ |
| `c6p-u0-nationalities-20-type` | 20 | 20 | ✓ (getypte tweeling) |
| `C5-U0-ESC-01` | 12 regels · 5 detail · 3 V/F | 5 detail | ✓ |
| `C6P-U0-ESC-01` | 11 regels · 5 detail · 3 V/F | 5 detail | ✓ |
| `C5-U0-LEC-01` | 4 scan · 4 V/F · 3 context | — | import-controle |
| `C6P-U0-LEC-01` | 4 scan · 4 V/F · 3 context | — | import-controle |

Woordenschatladder: **5 getypte oefeningen per unit**, 12 items × 3 rondes (8 bij open
productie). Motor: 314 → **324** spellen.

De import-controles in `escucha_data.py` en `lectura_data.py` verifiëren dat elk *bewijs* bij
een juist/fout-stelling **letterlijk in het fragment of de tekst staat**. Zonder die controle is
«met bewijs» een lege eis.

### Wat er per unit bij kwam

**Hub** — blueprint-oefeningen · nieuw tabblad «Escuchar 🎧» · volledige Lectura naast de
bestaande leesoefening · motorgroep «Escribir» met de vijf typ-spellen. C5 U0: 17 → 22 spellen;
C6+ U0: 13 → 18. Rooktest: geen consolefouten, geen mislukte assert, geen horizontale overflow
op 360 px.

**Print** — drie nieuwe bladzijden per unit (§3.4/§4.3 reeksen, §5 Lectura, §6 Escucha), elk op
een eigen blad, met antwoordruimte volgens §14 en zonder oplossingen. C5 U0 had **helemaal geen
Lectura en geen luisterblok in print**; C6+ U0 evenmin.

**PDF** — C5 U0 54 → 62 bladzijden; C6+ U0 32 → 41.

### Afwijkingen en bevindingen

1. **Twee U0-hubs waren verouderd.** Regenereren voegde ~230 kB toe zonder dat er inhoud
   bijkwam: dezelfde spellen, maar met de oude, kleinere payload — de motor was herbouwd, de
   twee U0-hubs nooit opnieuw ingebed. Puur additief, regressiecheck bleef schoon.
2. **`buildMatch` toonde maar 10 van de 20 paren.** De standaardsteekproef botst met
   beslissing A («de set blijft compleet, alleen de presentatie wordt opgedeeld»). Op `per=20`
   gezet, score nu `/20`.
3. **C5 U0-woordenschat miste clusterlabels** (`grp`), waardoor de typ-oefening *que-palabra*
   niet gegenereerd kon worden en de unit op 4 in plaats van 5 oefeningen bleef. Labels
   toegevoegd — alleen toegevoegd, niets gewijzigd.
4. **`.gitignore` sloot nieuwe bronbestanden uit.** `03-build/*` verbergt de hele map; de
   bestaande generatoren staan alleen in git omdat ze ouder zijn dan die regel. `hub_drills.py`
   viel er stil buiten. `03-build/web/*.py` is nu expliciet bron.
5. **`gen_audio_elevenlabs.py` en `escucha_data.py` bestonden niet.** De overdracht beschrijft
   ze als gebouwd; in de repo staat alleen een markdown-prompt voor C4. `escucha_data.py` is nu
   alsnog gemaakt.
6. **Afleiders waren gameable.** De eerste opzet gaf item 1, 2 en 3 exact dezelfde vier opties,
   en bij NAT-02 was het juiste antwoord altijd het laagste getal. Nu 11/11 unieke optiesets.

### De zes correcties uit `BOUWPLAN_SWEEP.md` fase 2

Alle zes raken units die **in ronde 2 en later** gebouwd worden. Ze zijn nu al canoniek
vastgelegd in `nat_data.py`, bij het item zelf, zodat die ronden ze niet opnieuw hoeven te
ontdekken. Nog niet zichtbaar in gebouwde output — die units bestaan nog niet.

| # | Waar | Correctie |
|---|---|---|
| 1 | C5-U3-NAT-01 item 12 | `ponerse de pie` is pronominaal → vervangen door `desayunar` |
| 2 | C6+ §5.9 item 15 | antwoord stond in de zin → tweede helft herschreven |
| 3 | C6+ §5.10 item 25 | cue `compartirlo` bevatte het pronomen → wordt `compartir` |
| 4 | C5-U5/U6-NAT-01 | woordgroepen blijven klikoefening, niet getypt |
| 5 | C5-U1-NAT-01 | 20 nationaliteiten → `accents:'soft'` |
| 6 | C5-U4-NAT-01 | twee dropdowns → `buildType` met invulvelden |

---

## Wat NIET geleverd is

**De vier PowerPoints zijn niet gebouwd.** `python-pptx` en `lxml` ontbreken in deze omgeving
en PyPI is onbereikbaar via de proxy (`pip install` → *no matching distribution*). De
generatoren zijn wél klaar: beide U0-decks hebben er een dia Lectura en een dia Escucha bij, met
de oplossing in `exercise_solucion` (zichtbaar bij de docent, bij klik bij de leerling) en
docentnotities met de didactische route. Syntaxis compileert en de nieuwe dia's verwijzen naar
geen enkele onbekende naam. Na `bash scripts/setup-build.sh` leveren

    python3 03-build/pptx/gen_u0_docente.py
    python3 03-build/pptx/gen_c6plus_u0_docente.py

de vier bijgewerkte decks. De bestanden in `03-build/pptx/` zijn nu nog de vorige versie.

**QR bij Lectura en Escucha.** De blueprint-oefeningen krijgen het al gegenereerde balkje met
een **echte** QR-code. Voor de nieuwe lees- en luisterblokken is er geen: `segno` is niet
installeerbaar, en de hub-URL bestaat sowieso pas na de hosting-sweep (§18). In plaats van een
nagemaakte QR staat er een gewone verwijzing naar het juiste tabblad — leerlingtekst, geen meta.

**`qr_links.json`: 14 van de 196 onderwerpen ingevuld** (de units van ronde 1, 33 links).

---

## Netwerk — de diagnose is veranderd

De vorige chat noteerde `403 to CONNECT` van de proxy. Dat klopt niet meer: het domein is
doorgelaten en de proxy geeft **HTTP 200**. Wat nu tegenhoudt is de site zelf — SiteGround zet
een bot-controle (`/.well-known/sgcaptcha/`) voor bezoekers uit een datacenter. De inhoud blijft
dus onbereikbaar, om een andere reden dan gedacht; een allowlist-wijziging lost dit niet op.

Daarom draagt elke link `status: "titel-gecontroleerd"`. De **scope** wordt wel afgedwongen: een
filter weigert subjuntivo, condicional, futuro simple, pluscuamperfecto en «avanzado», en is
getest. Dat is geen theoretisch risico — bij het zoeken naar de presente kwam
*«¿Presente de indicativo o de subjuntivo?»* naar boven.

---

## Gewijzigde bestanden

**Nieuw:** `03-build/web/hub_drills.py` · `hub_bloques.py` · `print_bloques.py` · `nat_data.py` ·
`escucha_data.py` · `lectura_data.py` · `vul_qr_links.py` · `01-cursussen/05-a1/U0/add_bloques_u0.py`

**Gewijzigd:** alle 17 `gen_*_web.py` (refactor) · `gen_u0_web.py` en `gen_c6plus_u0_web.py`
(inhoud) · `03-build/pptx/gen_u0_docente.py` en `gen_c6plus_u0_docente.py` ·
`01-cursussen/06-vervolg/U0/gen_u0_print.py` · `01-cursussen/05-a1/U0/U0.html` en `u0_vocab.json` ·
`qr_links.json` · `.gitignore`

**Gegenereerd:** 17 hubs · 2 PDF's · 10 nieuwe motor-spellen
