# Opdracht: bouw de website «Español en la práctica»

> **Voor de auteur:** dit hele document is de prompt. Plak het integraal in ChatGPT
> (of geef het als bestand mee). Alles wat hieronder in **VAST** staat is bindend:
> die dingen liggen al vast in de gedrukte cursussen en de QR-codes en mogen niet
> "verbeterd" worden. De rest is ontwerpvrijheid.

---

## 0 · De opdracht in één zin

Bouw een **statische website** die als schil dient rond ~27 al bestaande,
volledig zelfstandige HTML-pagina's en ~27 PDF's: vier cursusportalen, per unit
een landingspagina, en een navigatie die zowel een leerling met een QR-code als
een leerkracht met een muis in twee klikken op de juiste plek brengt.

**Je bouwt géén leerinhoud. Je bouwt de doos eromheen.**

---

## 1 · Context — wat dit is

«Español en la práctica» is een volledige Spaanse cursus voor het Vlaamse
secundair onderwijs (doorstroomfinaliteit, Katholiek Onderwijs Vlaanderen,
leerplan III-Spa-d). Eén leraar, vier cursussen, ongeveer 400 leerlingen per
jaar. Doelgroep van de site: **tieners van 14 tot 18** op hun telefoon of een
schoollaptop, en **de leerkracht** op een klasbord.

De vier cursussen, elk met een eigen vaste kleur — die kleur is de belangrijkste
navigatiedrager van de hele site:

| Code | Naam | Jaar | Kleur | Hex (primary / dark / tint) |
|---|---|---|---|---|
| **C4** | Welcome to Spanish | 4 Moderne talen | **Rood** | `#D64550` / `#A8323B` / `#FBEAEC` |
| **C5** | Español en la práctica | 5de jaar | **Groen** | `#1E9E74` / `#157355` / `#E4F4EE` |
| **C6** | Historias y mundos | 6de jaar (nieuw) | **Blauw** | `#2E77C2` / `#1E5691` / `#E5EFF9` |
| **C6+** | Vervolgcursus | 6de jaar (huidige groep) | **Paars** | `#7C56A9` / `#5B3E83` / `#EEE8F5` |

De rode draad door alle cursussen heet **«La Ruta»**: één doorlopende reis over
de kaart van de Spaanstalige wereld. Elke unit is een *parada* (halte). C5 gaat
van Spanje (U0–U4) via Mexico (U5–U6) naar Colombia (U7) en Peru (U8). **Die
reis is het thema van de site** — zie §7.

---

## 2 · Wat er precies geüpload wordt — VAST

Dit is de volledige inventaris. Bouw de site rond exact deze bestanden en deze
aantallen. Waar een cursus nog niet compleet is, moet de site dat netjes tonen
(zie §6.4), niet verbergen.

### 2.1 Interactieve hubs (de kern) — 27 bestanden

Standalone HTML, werkt volledig **offline**, geen externe requests, alles
ingebed (CSS, JS, lettertypes, afbeeldingen als data-URI). **Groot: 0,5 tot
2,1 MB per stuk.**

| Cursus | Aantal | Bestandsnamen zoals aangeleverd |
|---|---|---|
| C4 | 10 (van 14 gepland) | `C4_U1_hub.html` … `C4_U10_hub.html` |
| C5 | 9 (compleet) | `U0_web.html` … `U8_web.html` |
| C6 | 0 (nog niet gebouwd) | — |
| C6+ | 8 (van 9 gepland) | `C6plus_U0_web.html` … `C6plus_U7_web.html` |

Elke hub heeft intern **acht tabbladen**, altijd in deze volgorde en met deze
sleutels (het `data-p`-attribuut op de panelen):

| # | Sleutel | Label in de hub |
|---|---|---|
| 1 | `vocab` | Vocabulario |
| 2 | `gram` | Gramática |
| 3 | `lectura` | Lectura |
| 4 | `escuchar` | Escuchar 🎧 |
| 5 | `juegos` | Juegos |
| 6 | `hablar` | Hablar 🎙️ |
| 7 | `cultura` | Cultura |
| 8 | `extra` | Extra |

**Die acht sleutels zijn VAST.** De QR-codes in de gedrukte boeken gaan ze
gebruiken als URL-fragment (`…/hub/#escuchar`). Verander ze niet, hernoem ze
niet, en herschik de volgorde niet.

### 2.2 Print-PDF's — 27 bestanden

`C4_U1.pdf` … `C4_U10.pdf` · `C5_U0.pdf` … `C5_U8.pdf` ·
`C6plus_U0.pdf` … `C6plus_U7.pdf`. Tussen 38 en 57 bladzijden, 2 tot 8 MB.

### 2.3 Bewerkbare HTML-laag — 27 bestanden

Van elke PDF bestaat een HTML-versie met `contenteditable` en een knop
«Opslaan als PDF». Bedoeld voor de leerkracht die iets wil aanpassen.
Bestandsnaam: `C5_U2_BEWERKBAAR.html` enzovoort. **Ook standalone en ook groot.**

### 2.4 PowerPoints — 2 per unit

`C5_U2_docente.pptx` (leerkracht: vrije navigatie, oplossingen in de notities)
en `C5_U2_alumno.pptx` (leerling: F5 indrukken, elke klik onthult een antwoord).
Enkel downloaden, niet in de browser tonen.

### 2.5 Losse componenten — C4 alleen

Per C4-unit staan er nog losse deelpagina's naast de hub:
`C4_U1_comprension.html`, `_escucha.html`, `_funciones.html`, `_kgt.html`,
`_mapa.html`, `_practica.html`. Die worden vanuit de C4-hub in een `<iframe>`
met `srcdoc` geladen, maar moeten **ook rechtstreeks bereikbaar** zijn op een
eigen URL.

### 2.6 Cursusbrede werktuigen

- **`Conjugador.html`** (520 kB) — werkwoordengenerator, presente, ~1000
  werkwoorden. Twee lagen: opzoeken en zelf vervoegen. Geldt voor **alle**
  cursussen, dus die hoort niet ónder een cursus maar ernaast.
- **`LEESMIJ.md`** per unit — een korte handleiding voor de leerkracht.
  Die tekst is bronmateriaal voor de unit-pagina (§6.3), geen download.

---

## 3 · De gouden regel — lees dit twee keer

> **Je mag geen enkel van de aangeleverde HTML-bestanden openen, herschrijven,
> herformatteren, opsplitsen, minificeren, "moderniseren", door een bundler
> halen, in een framework-component gieten, of van nieuwe CSS voorzien.**

Elke hub is één zelfstandig bestand met een eigen, volledig gesloten CSS- en
JS-omgeving: honderden generieke klassenamen (`.panel`, `.sec`, `.controls`,
`.card`), globale JavaScript-functies (`renderFC()`, `buildType()`, …) en
inline `onclick`-handlers. Zodra er sitebrede CSS of JS bij komt, botst dat en
gaat er stil iets kapot dat een leerling pas in de klas ontdekt.

De bestanden worden bovendien **automatisch opnieuw gegenereerd** uit
Python-scripts. Alles wat jij met de hand in zo'n bestand verandert, is bij de
volgende build weg. De site moet dus zo gebouwd zijn dat een hub **vervangen**
kan worden door een nieuwe versie zonder dat er ook maar iets aan de site
verandert: bestand overschrijven, klaar.

**Gevolg voor de architectuur:** elke hub wordt onaangeraakt uitgeserveerd op
een eigen URL, als eigen document. Niet in een iframe binnen jouw layout, niet
als React-route, niet met een sitebrede header eromheen. De navigatie terug naar
de site wordt later ín de generator toegevoegd — dat is niet jouw werk.

Hetzelfde geldt voor de bewerkbare HTML-lagen, de C4-componenten en de
Conjugador.

---

## 4 · URL-structuur — VAST en onveranderlijk

Dit is het belangrijkste technische deel van de opdracht. In de gedrukte boeken
komen **QR-codes op papier**. Papier is voor altijd. Een URL die volgend jaar
verandert, breekt een boek dat al bij honderd leerlingen in de boekentas zit.

Neem daarom exact deze structuur over:

```
/                                  startpagina — de kaart, vier portalen
/c4/                               portaal C4  (rood)
/c5/                               portaal C5  (groen)
/c6/                               portaal C6  (blauw, nog leeg)
/c6plus/                           portaal C6+ (paars)

/c5/u2/                            unit-pagina: overzicht + downloads
/c5/u2/hub/                        DE HUB ZELF, onaangeraakt
/c5/u2/hub/#escuchar               deep link naar een tabblad
/c5/u2/editar/                     de bewerkbare HTML-laag
/c5/u2/print.pdf                   de print-PDF
/c5/u2/docente.pptx                PowerPoint leerkracht
/c5/u2/alumno.pptx                 PowerPoint leerling

/c4/u1/practica/                   losse C4-componenten (alleen C4)
/c4/u1/mapa/    /c4/u1/kgt/    /c4/u1/escucha/
/c4/u1/comprension/                /c4/u1/funciones/

/herramientas/conjugador/          de werkwoordengenerator
/herramientas/                     overzicht van alle werktuigen
/docente/                          zone voor de leerkracht (§10)
/q/<code>                          korte QR-doorverwijzing (§4.2)
```

### 4.1 Regels

- **Alles in kleine letters.** `c6plus`, niet `C6+` of `c6-plus`.
- **Altijd een slash op het einde** van een mappad. `/c5/u2/` en niet `/c5/u2`.
  Zet een permanente omleiding klaar van de vorm zónder slash naar die mét.
- **Nooit een unitnummer met voorloopnul.** `u0`, `u1`, `u10` — geen `u01`.
- **Geen taalprefix** (`/nl/`, `/es/`). De site is eentalig, zie §8.
- **Het URL-fragment (`#escuchar`) moet ongeschonden aankomen.** Geen
  omleiding, geen service worker, geen router die het opeet. Test dit expliciet.
- **Bestandsnamen op de eindpunten zijn `index.html`.** `/c5/u2/hub/index.html`
  is dus het hub-bestand, letterlijk gekopieerd, alleen hernoemd.

### 4.2 Het `/q/`-systeem — verplicht

Naast de gewone URL's komt er een tabel met **korte codes**, uitsluitend voor
QR-gebruik op papier. Een QR-code met minder tekens is een QR-code met grovere
blokjes, en die scant een telefoon in een klaslokaal met slecht licht veel
sneller. Even belangrijk: als de sitestructuur ooit wijzigt, past de auteur één
tabel aan en blijven alle gedrukte boeken werken.

Formaat van de code: `<cursus><unit><letter>`, bijvoorbeeld:

| Korte URL | Verwijst naar |
|---|---|
| `/q/c5-2` | `/c5/u2/hub/` |
| `/q/c5-2e` | `/c5/u2/hub/#escuchar` |
| `/q/c5-2l` | `/c5/u2/hub/#lectura` |
| `/q/c5-2j` | `/c5/u2/hub/#juegos` |
| `/q/c5-2v` | `/c5/u2/hub/#vocab` |

Lever dit als **één tekstbestand met omleidingsregels** (bij Netlify:
`_redirects`) dat de auteur kan bijwerken zonder de site opnieuw te bouwen.
Elke regel is een permanente omleiding (301) **inclusief het fragment**. Zet er
zelf al de regels in voor alle bestaande units en alle acht tabbladen — dat zijn
27 × 9 = 243 regels, machinaal te genereren.

---

## 5 · Techniek

### 5.1 Wat het moet zijn

Een **statische site**. Geen database, geen server-side code, geen inlogsysteem.
De site wordt op Netlify gehost. Een leerling moet hem kunnen gebruiken op een
telefoon met een trage 4G-verbinding en op een schoollaptop met een oude browser.

Kies **geen** zwaar framework. Next.js, Nuxt of Gatsby voegen hier niets toe en
maken het onderhoud voor een leraar zonder programmeerachtergrond onmogelijk.
Twee goede opties:

1. **Handgeschreven HTML + CSS + een klein beetje JavaScript**, met een
   Python- of Node-scriptje dat de unit-pagina's genereert uit één JSON-bestand.
   Aanbevolen: sluit aan bij hoe de rest van het project al werkt.
2. **Eleventy (11ty)** als je een generator wil. Licht, snel, geen JavaScript in
   de uitvoer, één configuratiebestand.

In beide gevallen: **de uitgeserveerde site bevat geen build-artefacten in de
paden** en werkt ook als je hem gewoon vanaf schijf opent.

### 5.2 Prestaties — dit is het echte probleem

De hubs zijn 0,5 tot 2,1 MB. Dat is per stuk zo groot als een hele gewone
website. Regel daarom:

- **Zet caching-headers op de hubs en PDF's**: lang cachen, maar met een
  mechanisme om een nieuwe versie meteen door te duwen (bijvoorbeeld
  `Cache-Control: public, max-age=0, must-revalidate` voor de HTML en een lange
  cache voor de PDF's).
- **Zorg dat brotli/gzip-compressie aan staat.** Een hub van 2 MB comprimeert
  naar ongeveer 300 kB; zonder compressie is dat op 4G het verschil tussen twee
  en vijftien seconden.
- **De portaal- en unit-pagina's die jij bouwt, moeten licht zijn.** Streef naar
  onder de 150 kB voor een unit-pagina, inclusief lettertypes.
- **Toon een laadindicatie bij het openen van een hub.** Een leerling die op
  «Oefenen» klikt en drie seconden een wit scherm ziet, klikt nog eens.
  Een eenvoudige aanpak: de knop toont na de klik een spinner en de tekst
  *«Un momento… se está cargando la unidad»*.
- **Geen enkele externe request.** Geen Google Fonts, geen CDN, geen analytics,
  geen embeds. Alles zelf hosten. Dat is hier zowel een prestatie-eis als een
  privacy-eis (§11).

### 5.3 Lettertypes

Drie, alle drie onder SIL OFL 1.1, en ze worden als `.woff2`-bestand
meegeleverd — **zelf hosten, niet van Google Fonts halen**:

- **Bricolage Grotesque** (600, 700, 800) — koppen, unittitels.
- **Inter** (400, 500, 600, 700) — alle lopende tekst, knoppen, labels.
- **Caveat** (400, 700) — uitsluitend voor handgeschreven accenten: een
  post-itnotitie, een citaat van een personage. Zuinig gebruiken.

Laad ze met `font-display: swap` en een systeemfont als terugval
(`'Inter', 'Segoe UI', system-ui, sans-serif`).

---

## 6 · De pagina's

### 6.1 De startpagina — «La Ruta»

Dit is de plek waar je het Spaanse thema laat werken (§7). De opbouw:

1. **Een kaart van de Spaanstalige wereld** als hoofdbeeld — echte geografie,
   geen gestileerde wereldbol. Op die kaart staan de *paradas* van de route:
   Madrid, Sevilla, Barcelona, València, Mexico-Stad, Cartagena, Cusco, Buenos
   Aires. Elke parada is klikbaar en brengt je naar de bijbehorende unit.
   Onder de kaart staat, voor wie de kaart niet kan of wil gebruiken, dezelfde
   informatie als gewone lijst — de kaart mag nooit de énige ingang zijn.
2. **De vier portaalkaarten**, groot, elk in zijn eigen kleur, met naam, jaar,
   aantal units en een korte zin over waar die cursus over gaat. Dit is het
   drukste element van de pagina; alles eromheen mag rustig zijn.
3. **«Ga meteen verder»** — als de bezoeker eerder een unit opende, staat die
   hier bovenaan terug (uit `localStorage`, zie §9.3).
4. **Een strook met de werktuigen**: de Conjugador en de zoekfunctie.

Geen schuifcarrousel, geen video-achtergrond, geen animatie die vanzelf begint.

### 6.2 Een cursusportaal (`/c5/`)

De kop draagt de cursuskleur. Daaronder:

- **Eén zin over de cursus** en het niveau (bijvoorbeeld voor C5: «A1 met de
  eerste A2-structuren — het dagelijkse leven, van Spanje naar Peru»).
- **Het traject als route**, niet als tabel: de units in volgorde, elk met zijn
  nummer, titel, *parada* en een miniatuur van waar op de kaart je bent. Een
  leerling moet in één oogopslag zien: dit zijn negen haltes en ik ben bij de
  derde.
- **Per unit een kaart** met: nummer, Spaanse titel, de eindtaak
  (*tarea final*), en drie knoppen — **Oefenen** (hub) · **Boek** (PDF) ·
  **Meer** (unit-pagina).
- **Een strook «Voor de leerkracht»** onderaan met de PowerPoints en de
  bewerkbare lagen van die cursus gebundeld.

De vier portalen zijn qua structuur identiek en verschillen alleen in kleur en
inhoud. Dat is bewust: een leerling die van C5 naar C6 gaat, moet niets
opnieuw leren.

### 6.3 Een unit-pagina (`/c5/u2/`)

De belangrijkste pagina van de site na de hub zelf. Vaste opbouw:

1. **Kop**: `Unidad 2 · Mi gente`, de parada (`Sevilla, Andalucía`), de kleur
   van de cursus, en een broodkruimel `Inicio › C5 › Unidad 2`.
2. **De vier formaten als vier duidelijke keuzes**, elk met een woord uitleg
   over wanneer je het gebruikt:
   - **Oefenen online** → de hub. *«Flashcards, spellen, luisteren, +100
     oefeningen met verbetering.»* Vermeld de grootte, bijvoorbeeld «1,8 MB».
   - **Het boek (PDF)** → *«42 bladzijden om af te drukken.»*
   - **Bewerkbaar (leerkracht)** → *«Pas de cursus aan en sla op als PDF.»*
   - **PowerPoint** → twee knoppen, docente en alumno.
3. **De acht tabbladen van de hub als acht rechtstreekse ingangen.** Dit is
   essentieel: een leerkracht die alleen het luisterfragment wil, klikt hier op
   *Escuchar* en landt op `/c5/u2/hub/#escuchar`. Toon ze met hun eigen icoon
   en een halve zin uitleg.
4. **Wat je leert** — de scope van de unit, in gewone taal. Deze tekst staat al
   in het `LEESMIJ.md`-bestand van elke unit; die tekst is de bron.
5. **De eindtaak** (*tarea final*), uitgelicht: dat is waar de hele unit naartoe
   werkt.
6. **Vorige / volgende unit** onderaan, met naam. Nooit een doodlopende pagina.

### 6.4 Wat er nog niet is

C6 is nog niet gebouwd, C4 heeft 10 van de 14 units, C6+ heeft er 8 van 9.
De site moet dat **eerlijk en rustig** tonen: het portaal C6 bestaat, draagt zijn
blauwe kleur, en zegt in één zin *«Deze cursus wordt in de loop van het jaar
opgebouwd.»* Een ontbrekende unit is een grijze kaart met het nummer en het
woord *Binnenkort*, niet een gat in de rij en niet een foutmelding.

Bouw dit zo dat het vanzelf omslaat: als het bestand er is, is de kaart actief.
De auteur mag nooit op twee plekken iets moeten aanpassen om een unit
vrij te geven.

### 6.5 Zoeken

Eén zoekveld, bereikbaar vanaf elke pagina (ook met de toets `/`). Het doorzoekt
**de titels van de units, de paradas, de eindtaken en de grammatica-onderwerpen**
— niet de volledige inhoud van de hubs, dat is niet haalbaar en niet nodig.
Bouw de index als één klein JSON-bestand dat bij de build gemaakt wordt.

Iemand die «perfecto» typt moet bij C5 U8 uitkomen. Iemand die «Sevilla» typt
bij C5 U2. Iemand die «ser estar» typt bij C5 U2.

---

## 7 · Vormgeving — een Spaans thema zonder cliché

De auteur vroeg om een Spaans thema. Doe dat, maar begrijp waar de cursus
over gaat: **de helft van de route ligt in Latijns-Amerika.** Een site vol
flamencowaaiers, stierenvechters, sangría en sombrero's is niet alleen een
cliché, hij is voor deze cursus ook feitelijk verkeerd — en de leerplancomponent
heet uitgerekend *«Identiteit in diversiteit»*.

### 7.1 Waar het thema wél vandaan komt

- **De kaart en de route.** Het sterkste Spaanse element van deze site is de
  reis zelf. Laat die het werk doen.
- **Azulejo-geometrie.** Het patroon van de Spaanse en Portugese tegels: strak,
  geometrisch, herhalend. Uitstekend als subtiele achtergrondtextuur in een
  koptekst of als scheidingslijn. In het project bestaat al een «azulejo-stijl»
  voor de spellen; sluit daarbij aan.
- **Warme neutralen.** De achtergrond van de site is niet wit maar `#FCFBF8`
  (papier) met `#F3EEE4` (crema) voor rustige vlakken. Dat leest als kalk en
  zon zonder dat er één cliché aan te pas komt.
- **Ruime, heldere typografie** met veel lucht — een gebouw met een patio, niet
  een volle etalage.
- **De personages.** De cursus heeft een vaste cast: Lucía (Sevilla), Diego
  (Mexico-Stad), Valen (Cartagena), Nina (Cusco), Mateo (Buenos Aires) en een
  rugzak-mascotte. Zij horen bij hun parada. Als je ze gebruikt, gebruik ze dan
  consequent en op de juiste plek.

### 7.2 Wat je niet doet

Geen stierengevecht, geen flamencodanseres, geen sombrero, geen taco als icoon
voor Mexico, geen felrood-geel als sitekleur (dat is de Spaanse vlag, niet de
Spaanstalige wereld), geen «¡Olé!» in de knoppen, geen omgekeerd uitroepteken
als decoratie waar het geen zin heeft, en geen letters met accenten waar geen
accent hoort (`Éspañól`).

Een omgekeerd vraagteken staat in echt Spaans altijd aan het begin van een
échte vraag. Als je Spaanse tekst gebruikt, moet ze correct zijn — dit is een
talenwebsite en de leerlingen leren er juist die regel.

### 7.3 De kleurenlogica — VAST

Er zijn **twee kleurlagen** en ze mogen elkaar nooit in de weg zitten:

1. **De cursuskleur** (rood, groen, blauw, paars) — voor navigatie en huisstijl.
   Eén kleur per cursus, overal consequent. Zodra iemand op een groene pagina
   is, weet hij dat hij in het vijfde jaar zit.
2. **De functionele taalkleuren** — die horen bij de grammatica ín de hubs
   (blauw = onderwerp, oranje = werkwoord, groen = voorwerp, paars = tijd,
   turkoois = plaats, rood = ontkenning, geel = strategie). **Gebruik die
   kleuren nergens in de site-navigatie**, want dan gaan ze betekenen wat ze
   niet betekenen.

Regel die overal geldt: **kleur is nooit de enige informatiedrager.** Naast
kleur altijd ook een label, een vorm of een icoon. Een leerling met
kleurenblindheid moet de site even goed kunnen gebruiken, en een pagina in
grijswaarden afdrukken moet blijven werken.

### 7.4 Donkere modus

Ondersteun `prefers-color-scheme: dark` voor de pagina's die jij bouwt. De
kleuren staan klaar: inkt `#ECEBE6`, papier `#15161A`, paneel `#1C1E24`,
lijn `#2C2E36`. **De hubs zelf hebben geen donkere modus** — probeer die er
niet in te forceren met een filter, dat maakt de tekeningen onleesbaar.

### 7.5 Vormtaal

Hoekradius: 14 px voor kaarten, 6 px voor chips, volledig rond voor pillen.
Afgeronde vormen voor hulp, chat en digitale bronnen; rechte vormen voor
grammatica, evaluatie en formele tabellen. Regelbreedte maximaal 65 tekens.

---

## 8 · Taal van de interface

De **inhoud** is Spaans met Nederlandse steun. De **navigatie van de site** is
Nederlands, met de Spaanse vaktermen die de leerlingen sowieso leren:
*unidad, parada, vocabulario, gramática, lectura, escuchar, juegos, hablar,
cultura, tarea final*. Dus: knop «Oefenen online», tabblad heet *Escuchar*.

Nooit Engels in de interface. Geen «Home», «Download», «Search» of «Loading».
Gebruik «Start», «Downloaden», «Zoeken», «Even geduld».

---

## 9 · Gedrag en interactie

### 9.1 Mobiel eerst

De meeste leerlingen komen via een QR-code, dus via een telefoon, dus
rechtstreeks op een hub. Test **staand op een scherm van 360 px breed** vóór je
naar de desktopweergave kijkt. Aanraakvlakken minstens 44 × 44 px.

### 9.2 Toetsenbord en schermlezer

Volledige bediening met het toetsenbord, zichtbare focusrand (die van de browser
mag je vervangen maar nooit verwijderen), correcte koppenhiërarchie (één `h1`
per pagina), alt-tekst bij elk beeld, `lang="nl"` op het document en
`lang="es"` op elk stukje Spaanse tekst — dat laatste zorgt ervoor dat een
schermlezer het Spaans ook echt als Spaans uitspreekt. Contrast minstens 4,5:1.

### 9.3 Onthouden waar je was

In `localStorage` (niet in een cookie): de laatst geopende unit, zodat de
startpagina «Ga verder waar je gebleven was» kan tonen. Meer niet. Geen
gebruikersprofielen, geen voortgangsregistratie — de hubs bewaren hun eigen
oefenresultaten al lokaal en dat moet zo blijven.

### 9.4 Delen en afdrukken

Elke unit-pagina krijgt fatsoenlijke metagegevens (`og:title`, `og:description`,
`og:image` in de cursuskleur), zodat een link die de leerkracht in Smartschool
of WhatsApp plakt er goed uitziet. En een afdrukstijl: wie een unit-pagina
afdrukt, krijgt de titel, de inhoud en de **volledige URL's uitgeschreven** —
geen navigatie, geen knoppen.

### 9.5 Foutpagina's

Een 404 in de cursuskleur van het pad waar iemand op zat, met de zin *«Deze
parada bestaat niet»*, een zoekveld en de vier portalen. Nooit een kale
servermelding.

---

## 10 · De zone voor de leerkracht

De PowerPoints van de leerkracht bevatten **oplossingen**. De bewerkbare
HTML-lagen ook. Die mogen niet zomaar op een pagina staan waar een leerling
langswandelt.

Dit is een statische site, dus echte beveiliging bestaat hier niet — en dat moet
je ook eerlijk zeggen in plaats van te doen alsof. Wat wel kan en volstaat:

- Alles voor de leerkracht staat onder `/docente/`.
- Die tak staat **niet in de navigatie** en wordt met `robots.txt` en een
  `noindex`-metatag uit de zoekmachines gehouden.
- Er staat een eenvoudige toegangspoort voor (een wachtwoord in JavaScript of
  Netlify's ingebouwde wachtwoordbeveiliging als die beschikbaar is).
- **Zeg in de oplevering met zoveel woorden dat dit een drempel is en geen
  slot**, zodat de auteur zelf kan beslissen of dat volstaat.

De leerling-PowerPoint (`alumno`) mag wél gewoon op de unit-pagina staan; daar
staan geen oplossingen in.

---

## 11 · Privacy en recht

Dit is een site voor minderjarigen in een schoolcontext. Dat maakt het simpel:

- **Geen enkele tracker.** Geen Google Analytics, geen Meta-pixel, geen
  Hotjar, geen ingebedde YouTube-speler op de pagina's die jij bouwt
  (de hubs regelen hun eigen video's met `youtube-nocookie`).
- **Geen cookies.** `localStorage` voor één ding (§9.3) is geen cookie en
  vereist geen banner. Bouw dus ook geen cookiebanner.
- **Alles zelf gehost**, inclusief de lettertypes. Een Google Font laden stuurt
  het IP-adres van elke leerling naar een derde partij.
- Een korte, leesbare **privacyverklaring** op `/privacy/`: wat er bewaard
  wordt (bijna niets), waar en door wie. Twintig regels, geen juridisch proza.
- **Een colofon** op `/info/` met de auteur, het leerplan (III-Spa-d,
  D/2024/13.758/220) en de licenties van de lettertypes (SIL OFL 1.1) en van
  de gebruikte iconenset (Lucide, MIT). Dat is een verplichting van die
  licenties, geen beleefdheid.

---

## 12 · Wat je moet opleveren

1. **De volledige site als bronbestanden**, met een `README.md` die uitlegt hoe
   je hem lokaal draait en hoe je hem publiceert.
2. **Eén configuratiebestand** (JSON) waarin alle units staan: cursus, nummer,
   titel, parada, eindtaak, scope, en welke bestanden bestaan. **Alle
   pagina's worden hieruit gegenereerd.** Een unit toevoegen = één blok in dat
   bestand. Dit is de belangrijkste eis van deze paragraaf: de auteur is
   leraar, geen webontwikkelaar, en moet dit in vijf jaar nog kunnen bijwerken.
3. **Het `_redirects`-bestand** met alle `/q/`-codes (§4.2), machinaal
   gegenereerd uit hetzelfde configuratiebestand.
4. **Een lijst van alle definitieve URL's** als tekstbestand. Die heeft de
   auteur nodig om de QR-codes in de boeken te laten aanmaken.
5. **Een pagina met de bouwstenen** (`/docente/estilo/`, niet in de navigatie):
   alle knoppen, kaarten, kleuren en tekststijlen op één pagina, zodat er later
   consequent bijgebouwd kan worden.

---

## 13 · Opleverchecklist

Loop dit letterlijk af voor je zegt dat de site af is:

- [ ] Alle 27 hubs openen en werken **precies zoals ze in het bestand stonden**
      — vergelijk er drie zij aan zij met het origineel.
- [ ] `…/hub/#escuchar` opent het juiste tabblad, ook als je de URL rechtstreeks
      plakt en ook na een `/q/`-omleiding.
- [ ] Alle 243 `/q/`-codes komen op de juiste plek uit.
- [ ] Geen enkele externe request op geen enkele pagina (controleer in het
      netwerkpaneel van de browser).
- [ ] Een unit-pagina laadt onder 150 kB.
- [ ] De site werkt op een scherm van 360 px breed.
- [ ] Volledig bedienbaar met alleen het toetsenbord.
- [ ] Elke pagina heeft precies één `h1`.
- [ ] Een pagina in grijswaarden afdrukken blijft leesbaar en begrijpelijk.
- [ ] De vier cursuskleuren zijn exact de hex-waarden uit §1.
- [ ] Nergens Engels in de interface.
- [ ] De Spaanse tekst in de interface is grammaticaal correct.
- [ ] C6 en de ontbrekende units tonen «Binnenkort» en geen fout.
- [ ] 404 werkt en is bruikbaar.
- [ ] `/docente/` staat niet in de navigatie en niet in `robots.txt` als
      toegankelijk pad.
- [ ] Een nieuwe versie van een hub erin zetten = één bestand overschrijven,
      niets anders.

---

## 14 · Wat je zeker niet doet

- De aangeleverde HTML-bestanden aanpassen, opsplitsen of herformatteren.
- Ze in een iframe of een framework-component stoppen.
- Sitebrede CSS of JavaScript op de hub-pagina's laden.
- Een inlogsysteem, een gebruikersaccount of een voortgangsdatabase bouwen.
- De acht tabbladsleutels hernoemen of herordenen.
- De URL-structuur uit §4 «verbeteren».
- Een cookiebanner toevoegen.
- Een chatbot, een AI-assistent of een nieuwsbrief toevoegen.
- De cursuskleuren aanpassen omdat ze «mooier» kunnen.
- Placeholder-inhoud achterlaten (`lorem ipsum`, «hier komt tekst»,
  «TODO»). Als iets ontbreekt, zeg dat in de oplevering.

---

## 15 · Als er iets onduidelijk is

Vraag het, en verzin het niet. Concreet: de titels, paradas en eindtaken van
alle units staan in het bestand `INHOUDSTAFEL_C5_C6plus.md` en in de
`LEESMIJ.md`-bestanden die bij de units geleverd worden. De cursuskleuren en
lettertypes staan in `tokens.json`. Als je iets nodig hebt dat daar niet in
staat — vraag het op, en zet er in geen geval iets bedachts voor in de plaats.
Het gaat om lesmateriaal dat volgende maand voor een klas ligt.
