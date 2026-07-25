# 50 interactieve PowerPoint-ideeën voor een cursus Spaans

**Doel:** een didactisch bruikbare ideeën- en bouwbibliotheek voor interactieve PowerPoints bij een doorlopende cursus Spaans.

**Technische referentie:** PowerPoint voor Microsoft 365 en recente desktopversies, gecontroleerd op 25 juli 2026.

---

## Compatibiliteitslabels

| Label | Betekenis |
|---|---|
| 🟢 **Native** | Kan met gewone PowerPoint-functies worden gebouwd. |
| 🟡 **Microsoft 365** | Vereist of werkt het best met Microsoft 365, internet of een moderne PowerPointversie. |
| 🟠 **Templatewerk** | Goed uitvoerbaar, maar vraagt vooraf gebouwde triggers, verborgen dia’s of zorgvuldig templatewerk. |
| 🔴 **VBA/add-in** | Volledige functionaliteit vraagt een macrobestand, add-in of externe webtool. Gebruik dit niet als kernfunctionaliteit. |

> **Belangrijk:** ontwerp de cursus eerst voor PowerPoint Desktop op Windows. Test daarna afzonderlijk in PowerPoint voor Mac, PowerPoint voor het web en Teams. Niet alle triggers, add-ins, macro’s en mediabesturing gedragen zich overal identiek.

---

# I. Navigatie en spelarchitectuur

| Nr. | Idee | Toepassing in de cursus Spaans | Technische bouwstenen | Niveau |
|---:|---|---|---|---|
| 1 | **Interactieve startpagina** | Bouw een beginscherm met tegels voor woordenschat, grammatica, lezen, luisteren, spreken, schrijven, cultuur en evaluatie. De leraar kiest tijdens de les rechtstreeks de gewenste route. | Summary Zoom, secties, hyperlinks, actieknoppen | 🟢 |
| 2 | **Klikbare cursuskaart** | Gebruik bijvoorbeeld een kaart van Antwerpen, Madrid of Valencia. Iedere locatie opent een les, dialoog, opdracht of cultuurkader. | Afbeelding, transparante hotspots, Slide Zoom, Morph | 🟢 |
| 3 | **Niet-lineaire leskeuze** | Laat de leraar de volgorde aanpassen aan de klas: eerst grammatica, eerst verhaal, eerst woordenschat of meteen een probleemtaak. | Section Zoom, aangepaste diavoorstellingen, terugkeerknoppen | 🟢 |
| 4 | **Drie moeilijkheidsroutes** | Voorzie op een keuzedia drie routes: **con apoyo**, **ruta básica** en **desafío**. Alle routes oefenen hetzelfde doel met verschillende steun. | Hyperlinks, verborgen dia’s, kleur- of pictogramcodes | 🟠 |
| 5 | **Vertakkend verhaal** | Laat de klas beslissen wat een personage doet: “¿Va en metro o en bicicleta?” Iedere keuze leidt naar een andere scène, maar uiteindelijk naar hetzelfde leerdoel. | Actieknoppen, hyperlinks, duplicaatdia’s, verborgen vertakkingen | 🟠 |
| 6 | **Vaste thuis-, terug- en hulpknoppen** | Plaats op iedere interactieve dia dezelfde knoppen voor startmenu, vorige stap, woordenhulp en oplossing. Zo voelt de PowerPoint als een echte applicatie. | Diamodel, actieknoppen, hyperlinks | 🟢 |
| 7 | **Verborgen hintlagen** | Een leerling klikt eerst op **pista 1**, daarna eventueel op **pista 2** en pas ten slotte op **solución**. De ondersteuning wordt dus zichtbaar afgebouwd. | Animatietriggers, verschijnen/vervagen, objectnamen | 🟠 |
| 8 | **Visuele voortgangsmeter** | Toon bovenaan hoeveel fasen van de opdracht zijn voltooid: oriënteren, begrijpen, oefenen, produceren en reflecteren. | Vormen, Morph, verschillende dia-statussen | 🟢 |
| 9 | **Zelfstandig leerstation in kioskmodus** | Leerlingen doorlopen individueel of per duo een les zonder met de muis willekeurig naar de volgende dia te kunnen gaan. Alleen de ingebouwde knoppen werken. | Kioskmodus, actieknoppen, vaste navigatie, `.ppsx` | 🟢 |
| 10 | **Digitale escape room** | Combineer woordenschat, grammatica, luisteren en lezen in een missie. Correcte antwoorden leveren letters, cijfers of locaties op voor een eindcode. | Verborgen dia’s, hotspots, hyperlinks, feedbacklagen, optioneel Forms | 🟠 |

---

# II. Quizzen, antwoorden en feedback

| Nr. | Idee | Toepassing in de cursus Spaans | Technische bouwstenen | Niveau |
|---:|---|---|---|---|
| 11 | **Klik om het antwoord te onthullen** | Toon eerst alleen de vraag. De klas formuleert een antwoord en klikt daarna om modelantwoord, uitleg of vertaling zichtbaar te maken. | Triggeranimatie, verschijnen, vervagen | 🟢 |
| 12 | **Meerkeuze met onmiddellijke feedback** | Iedere antwoordknop toont een eigen feedbacklaag: **¡Correcto!**, **Casi**, of een gerichte grammaticahint. | Objecttriggers, meerdere feedbackvakken, geluid optioneel | 🟠 |
| 13 | **Hotspotvraag op een afbeelding** | Leerlingen klikken in een kamer, stad, menukaart of strip op het juiste object, personage, vervoermiddel of informatie-element. | Transparante vormen, actie-instellingen, feedbacktriggers | 🟠 |
| 14 | **Zoek de fout** | Verberg klikzones over woorden of zinsdelen. De leerling moet precies aanduiden waar de fout staat en daarna de zin verbeteren. | Transparante hotspots, kleurverandering, uitleglaag | 🟠 |
| 15 | **Memoryspel met woord en beeld** | Achter kaartjes zitten Spaanse woorden, afbeeldingen, audio of definities. De klas zoekt passende paren. | Triggers, afdekvlakken, meerdere kaartstatussen | 🟠 |
| 16 | **Volgordepuzzel** | Zet een dialoog, route, dagplanning of verhaal in de juiste volgorde. Een volledig native versie gebruikt klikbare antwoordreeksen; echt vrij slepen vraagt extra techniek. | Hyperlinks, nummerknoppen, verborgen feedback; VBA voor echt drag-and-drop | 🟠/🔴 |
| 17 | **Jeopardy-bord** | Categorieën kunnen zijn: vocabulario, gramática, cultura, escucha en expresión. Gekozen vakjes verdwijnen of veranderen van kleur. | Hyperlinks, terugkeerknoppen, aangepaste shows | 🟠 |
| 18 | **Wie wordt miljonair?** | Bouw een oplopende reeks taalvragen met hulplijnen zoals 50/50, woordenboekhint, publieksstem en extra voorbeeldzin. | Triggers, vertakkingen, geluid, verborgen hulplagen | 🟠 |
| 19 | **Visuele aftelklok** | Geef 10, 20, 30 of 60 seconden voor woordoproep, overleg, spreken of schrijven. De tijdsbalk loopt zichtbaar leeg. | Wipe-animatie, timing, geluidssignaal | 🟢 |
| 20 | **Live quiz of exit ticket** | Plaats een Microsoft Forms-quiz, poll of exit ticket rechtstreeks in een dia. Antwoorden kunnen klassikaal worden verzameld en later geanalyseerd. | Microsoft Forms-integratie, internet, schoolaccount | 🟡 |

---

# III. Woordenschat en grammatica

| Nr. | Idee | Toepassing in de cursus Spaans | Technische bouwstenen | Niveau |
|---:|---|---|---|---|
| 21 | **Klikbare woordmuur** | Woorden verschijnen per thema. Een klik toont afbeelding, uitspraak, vertaling, voorbeeldzin, collocatie of grammaticale informatie. | Triggers, audio, pictogrammen, lagen | 🟠 |
| 22 | **Beeld-woord-audiokaarten** | Een afbeelding kan achtereenvolgens het Spaanse woord, het lidwoord, de uitspraak en een modelzin onthullen. | Audio-icoon, animatietriggers, kaarttemplate | 🟢 |
| 23 | **Ophaalflashcards met afbouw** | Ronde 1 toont beeld en woord; ronde 2 alleen beeld; ronde 3 een context; ronde 4 vraagt een eigen zin. | Duplicaatdia’s, Morph, hyperlinks | 🟢 |
| 24 | **Semantisch sorteerspel** | Leerlingen plaatsen woorden conceptueel bij eten, vervoer, personen, handelingen of emoties. De native versie laat categorieën aanklikken; vrij slepen is optioneel. | Klikkeuzes, triggers, feedbacklagen; VBA alleen voor vrij slepen | 🟠 |
| 25 | **Interactieve zinsbouwer** | Laat leerlingen onderwerp, werkwoord, tijd, plaats en aanvulling combineren. Daarna verdwijnt de steun en produceren ze de zin mondeling. | Klikbare bouwblokken, Morph, duplicaatdia’s | 🟠 |
| 26 | **Woordvolgordepuzzel** | Toon losse zinsdelen. De klas kiest de correcte volgorde en ziet vervolgens hoe de delen animerend in de zin schuiven. | Motion paths, Morph, triggers | 🟠 |
| 27 | **Grammaticatransformatie met Morph** | Laat **hablo → hablamos**, **es → está**, enkelvoud → meervoud of heden → toekomst vloeiend veranderen. De vormverandering wordt visueel zichtbaar. | Morph, identieke objectnamen, kleurcodes | 🟢 |
| 28 | **Vervoegingswiel** | Een wiel kiest persoon, werkwoord of tijd. De leerling produceert de vorm en gebruikt ze in een zin. Echte willekeur vraagt een macro; een vooraf bepaalde draaireeks kan native. | Draai-animatie, triggers; VBA voor willekeur | 🟠/🔴 |
| 29 | **Beslisboom voor ser, estar en hay** | Leerlingen beantwoorden opeenvolgende betekenisvragen en komen zo bij de juiste vorm. Foute routes geven een gerichte tegenvoorbeeldzin. | Vertakkingen, actieknoppen, kleurcodes | 🟠 |
| 30 | **Grammaticakliniek** | Een “patiëntzin” heeft een probleem. Leerlingen diagnosticeren de fout, kiezen een ingreep en zien daarna de herstelde zin in een nieuwe context. | Hotspots, feedbacklagen, Morph, geluid optioneel | 🟠 |

---

# IV. Lezen, luisteren, spreken en schrijven

| Nr. | Idee | Toepassing in de cursus Spaans | Technische bouwstenen | Niveau |
|---:|---|---|---|---|
| 31 | **Ingebedde video met observatieopdracht** | Speel een korte authentiek ogende scène af. Vooraf krijgen leerlingen één globale kijkvraag; daarna verschijnen detailvragen. | Ingebedde MP4 of onlinevideo, posterframe, animatietiming | 🟢/🟠 |
| 32 | **Pauzeer, voorspel en kijk verder** | Stop een dialoog net vóór een antwoord of beslissing. Leerlingen voorspellen wat iemand zegt en vergelijken daarna met de video. | Getrimde videofragmenten, duplicaatdia’s, actieknoppen | 🟠 |
| 33 | **Video met ondertitels en taalsteun** | Voeg Spaanse ondertitels toe en maak eventueel aparte versies met Engelse of Nederlandse ondersteuning. Gebruik ondertitels ook voor luisterstrategieën. | Ingebedde video, WebVTT/SRT, captionfunctie | 🟡 |
| 34 | **Audiopaneel met personages** | Klik op Noor, Adam, Lucía of Tomás om afzonderlijke uitspraken af te spelen. Daarna reconstrueert de klas de dialoog. | Audio per object, actie-instellingen, avatars | 🟢 |
| 35 | **Luisteren en ordenen** | Leerlingen luisteren naar routeaanwijzingen, afspraken of gebeurtenissen en kiezen daarna de juiste beeld- of zinsvolgorde. | Audio, antwoordknoppen, feedbacklagen | 🟠 |
| 36 | **Microdictee met gefaseerd transcript** | Eerst luisteren zonder tekst, dan kernwoorden noteren, daarna lege plaatsen invullen en ten slotte het volledige transcript vergelijken. | Audio, meerdere transcriptlagen, triggers | 🟢 |
| 37 | **Shadowingmodule** | Een korte zin wordt afgespeeld; leerlingen spreken bijna gelijktijdig mee. Daarna verdwijnen tekst en kernwoorden stapsgewijs. | Audiofragmenten, karaokeachtige markering, timings | 🟠 |
| 38 | **Uitspraakcontrast** | Laat bijvoorbeeld **pero/perro**, **caro/carro** of klinkercontrasten horen. Leerlingen kiezen wat ze hoorden en spreken daarna zelf. | Audioknoppen, A/B-keuzes, mondpositiebeelden | 🟢 |
| 39 | **Rollenkaart met spreektimer** | Laat PowerPoint een personage, situatie, doel en verplichte functie tonen: weigeren, voorstellen, verduidelijken of reageren. Daarna start de timer. | Triggers, kaartlagen, timer; VBA alleen voor echte willekeur | 🟠 |
| 40 | **Gesimuleerde chatbot** | Een digitaal personage zegt of vraagt iets. De leerling kiest of formuleert een reactie en komt in een ander gecontroleerd dialoogpad terecht. | Vertakkende dia’s, audio, tekstballonnen, actieknoppen | 🟠 |
| 41 | **Leesdetective met bewijsstukken** | Verdeel een chat, ticket, kaart, menu en agenda over klikbare bronnen. Leerlingen verzamelen bewijs om een probleem op te lossen. | Hotspots, pop-uplagen, verborgen bronnen, eindbeslissing | 🟠 |
| 42 | **Schrijfopdracht die zichzelf opbouwt** | Klik achtereenvolgens ontvanger, doel, verplichte informatie, tekststructuur en checklist open. Daarna verdwijnt de steun voor de echte schrijfversie. | Triggers, lagen, duplicaatdia’s | 🟢 |
| 43 | **Peerfeedbackpaneel** | Toon na een schrijf- of spreektaak één feedbackvraag per klik: boodschap, volledigheid, woordenschat, grammatica, uitspraak en volgende stap. | Triggerlagen, checklists, pictogrammen | 🟢 |
| 44 | **Opnemen, vergelijken en hernemen** | Gebruik een gelinkte webrecorder, Teams-opdracht of andere schooltool zodat leerlingen een eerste en verbeterde spreekversie bewaren. PowerPoint levert de prompt, timer en feedbackcriteria. | Hyperlink/QR-code, externe recorder, terugkeerdia | 🟡 |
| 45 | **Vier-vaardighedenmissie** | Start met een tekst, laat leerlingen een audio beluisteren, laat hen overleggen en eindig met een geschreven of gesproken product. Alles blijft binnen één visuele verhaallijn. | Secties, media, vertakkingen, geïntegreerde einddia | 🟠 |

---

# V. Visuele verhalen, cultuur en presentatiemodus

| Nr. | Idee | Toepassing in de cursus Spaans | Technische bouwstenen | Niveau |
|---:|---|---|---|---|
| 46 | **Geanimeerde routekaart** | Laat een personage door Antwerpen, Madrid, Bogotá of Valencia bewegen terwijl routewoorden en plaatsvoorzetsels verschijnen. | Motion paths, Morph, kaartafbeelding, geluid | 🟢 |
| 47 | **Culturele fotoverkenning met zoom** | Start met een volledig plein, gebouw of markt en zoom daarna vloeiend in op details waarover leerlingen vragen beantwoorden. | Morph, uitsnedes, beeldhotspots | 🟢 |
| 48 | **Interactief 3D-object** | Draai een 3D-model van bijvoorbeeld een gebouw, gerecht, vervoermiddel of kunstvoorwerp en verbind kijkhoeken aan woordenschat of cultuurvragen. | 3D-model, 360° rotatie, Morph/animatie | 🟡 |
| 49 | **Microfilms met GIF, schermopname en Ink Replay** | Gebruik een korte GIF voor emoties of handelingen, een schermopname voor digitale taken en Ink Replay om spelling, accenten of zinsopbouw stap voor stap te tonen. | GIF, Screen Recording, Draw, Ink Replay | 🟡 |
| 50 | **Live docentlaag en finale eindmissie** | Gebruik Cameo om de docentcamera in de dia te plaatsen, live ondertitels of vertaling tijdens instructie, en sluit af met een grote vertakkende missie waarin de leerlingen alle vaardigheden inzetten. | Cameo, live captions, Zoom, media, vertakkingen, Forms optioneel | 🟡/🟠 |

---

# Aanbevolen kernset voor de eerste versie

Bouw niet onmiddellijk alle vijftig functies. Een sterke eerste cursusversie gebruikt deze vijftien:

1. interactieve startpagina;
2. klikbare cursuskaart;
3. vaste navigatieknoppen;
4. verborgen hintlagen;
5. drie moeilijkheidsroutes;
6. klikbare antwoorden;
7. meerkeuze met feedback;
8. hotspotvragen;
9. visuele timer;
10. woordkaarten met audio;
11. zinsbouwer;
12. grammaticatransformaties met Morph;
13. ingebedde video;
14. audiopaneel met personages;
15. geïntegreerde eindmissie.

Voeg Forms, Cameo, 3D, echte willekeur en macro’s pas toe nadat de basispresentatie stabiel werkt.

---

# Bouwarchitectuur voor Claude

## 1. Werk met een vaste diamaster

Voorzie minimaal deze layouts:

- `TITLE`
- `LESSON_MENU`
- `STORY_SCENE`
- `VOCABULARY`
- `GRAMMAR`
- `READING`
- `LISTENING`
- `SPEAKING`
- `WRITING`
- `QUIZ`
- `FEEDBACK`
- `CULTURE`
- `FINAL_MISSION`
- `TEACHER_NOTES`

## 2. Gebruik vaste objectnamen

Voorbeelden:

```text
BTN_HOME
BTN_BACK
BTN_HELP
BTN_ANSWER
TRG_Q01_A
TRG_Q01_B
FB_Q01_CORRECT
FB_Q01_RETRY
AUDIO_U01_L02_01
VIDEO_U01_STORY_01
TXT_HINT_LEVEL_1
TXT_HINT_LEVEL_2
PROGRESS_STEP_03
```

## 3. Scheid drie lagen

```text
CONTENT
├── teksten
├── vragen
├── antwoorden
├── audio
└── video

INTERACTION
├── hyperlinks
├── triggers
├── animaties
├── vertakkingen
└── feedbacklagen

TEACHER
├── didactische instructies
├── timing
├── verwachte antwoorden
├── differentiatie
└── technische noodroute
```

## 4. Maak twee uitvoerversies

### Docentversie — `.pptx`

- vrije navigatie;
- Presenter View;
- sprekersnotities;
- oplossingen;
- extra uitleg;
- alternatieve routes.

### Zelfstandige leerlingversie — `.ppsx`

- kioskmodus;
- beperkte navigatie;
- ingebouwde feedback;
- vaste terugkeerknoppen;
- geen zichtbare docentnotities.

## 5. Voorzie altijd een noodroute

Iedere complexe interactieve dia krijgt ook:

- een knop **toon oplossing**;
- een knop **sla over**;
- een knop **terug naar lesmenu**;
- een statische fallback wanneer video, internet of audio niet werkt.

---

# Didactische ontwerpregels

1. **Interactie moet een taalhandeling uitlokken.** Een knop is geen leeractiviteit zolang de leerling alleen klikt.
2. **Laat leerlingen eerst antwoorden en onthul daarna pas het model.**
3. **Gebruik animaties om betekenis of structuur zichtbaar te maken, niet als decoratie.**
4. **Beperk iedere dia tot één duidelijke opdracht.**
5. **Bouw steun zichtbaar af:** model → woordenbank → kernwoorden → inhoudelijke cue → geen taalsteun.
6. **Laat feedback tot nieuwe productie leiden:** poging → feedback → herformulering → nieuwe context.
7. **Gebruik audio en video in korte, doelgerichte fragmenten.**
8. **Voorzie ondertitels, transcript of visuele steun zonder die onmiddellijk volledig te tonen.**
9. **Gebruik dezelfde navigatie, pictogrammen en kleuren in de hele cursus.**
10. **Test iedere PowerPoint op het echte schooltoestel, scherm, account en netwerk.**

---

# Technische waarschuwingen

## Onlinevideo

- vereist een betrouwbare internetverbinding;
- kan door schoolfilters worden geblokkeerd;
- kan wijzigen of verdwijnen;
- is minder veilig dan een lokaal ingebedde MP4;
- ondertiteling wordt bij onlinevideo doorgaans door het videoplatform beheerd.

## Ingebedde video en audio

- maakt het PowerPointbestand groter;
- gebruik bij voorkeur moderne, breed ondersteunde mediaformaten;
- bewaar ook de originele mediabestanden buiten de PowerPoint;
- comprimeer media pas nadat een kwaliteitskopie is bewaard.

## Microsoft Forms

- is vooral geschikt voor Microsoft 365 Education of zakelijke schoolaccounts;
- kan door de Microsoft 365-beheerder worden uitgeschakeld;
- vereist voor live gegevensverzameling doorgaans internet.

## Macro’s en VBA

- vereisen meestal `.pptm` in plaats van `.pptx`;
- kunnen door schoolbeveiliging worden geblokkeerd;
- werken niet betrouwbaar in PowerPoint voor het web;
- mogen daarom alleen een optionele uitbreidingslaag vormen;
- bied altijd een versie zonder macro’s aan.

## Triggeranimaties

- test triggers steeds in echte diavoorstellingsmodus;
- geef ieder object een duidelijke naam in het selectiedeelvenster;
- gebruik niet te veel overlappende transparante objecten;
- documenteer per dia welke trigger welk object activeert.

## Toegankelijkheid

- gebruik ondertitels bij essentiële video en audio;
- voorzie voldoende contrast en grote klikzones;
- vermijd informatie die alleen door kleur wordt overgebracht;
- voeg alternatieve tekst toe aan betekenisvolle afbeeldingen;
- zorg dat animaties niet te snel, flitsend of afleidend zijn.

---

# Geschikte verdeling over een les van 50 minuten

| Lesfase | PowerPointfuncties | Richttijd |
|---|---|---:|
| Oriëntatie | startmenu, verhaalbeeld, kaart, videohaak | 5 min. |
| Begrijpen | luister- of leestekst, globale vraag, hotspots | 8 min. |
| Opmerken | kleurcodes, Morph, grammaticale ontdekking | 7 min. |
| Oefenen met steun | quiz, zinsbouwer, woordkaarten, hints | 12 min. |
| Productie | rollenkaart, timer, schrijf- of spreektaak | 10 min. |
| Feedback | modelantwoord, peerfeedback, herneming | 5 min. |
| Exit | Forms-vraag, code, reflectie of vervolgstap | 3 min. |

---

# Officiële technische referenties

- [Action buttons in PowerPoint](https://support.microsoft.com/en-us/powerpoint/add-commands-to-your-presentation-with-action-buttons)
- [Trigger an animation effect](https://support.microsoft.com/en-us/powerpoint/trigger-an-animation-effect)
- [Use Zoom for PowerPoint](https://support.microsoft.com/en-us/powerpoint/use-zoom-for-powerpoint-to-bring-your-presentation-to-life)
- [Use the Morph transition](https://support.microsoft.com/en-us/powerpoint/training/use-the-morph-transition-in-powerpoint)
- [Morph tips and tricks](https://support.microsoft.com/en-us/powerpoint/morph-transition-tips-and-tricks)
- [Insert a form or quiz into PowerPoint](https://support.microsoft.com/en-us/forms/insert-a-form-or-quiz-into-powerpoint)
- [Add, format and record video](https://support.microsoft.com/en-us/powerpoint/training/add-format-and-record-video-in-powerpoint)
- [Add closed captions or subtitles to media](https://support.microsoft.com/en-us/powerpoint/add-closed-captions-or-subtitles-to-media-in-powerpoint)
- [Present with live captions or subtitles](https://support.microsoft.com/en-us/powerpoint/present-with-real-time-automatic-captions-or-subtitles-in-powerpoint)
- [Presenting with Cameo](https://support.microsoft.com/en-us/powerpoint/presenting-with-cameo)
- [Get creative with 3D models](https://support.microsoft.com/en-us/office/graphics-visuals/get-creative-with-3d-models)
- [Replay ink strokes](https://support.microsoft.com/en-us/office/replay-your-ink-strokes-in-office)
- [Create a self-running presentation](https://support.microsoft.com/en-us/powerpoint/training/create-a-self-running-presentation)
- [Use Presenter View](https://support.microsoft.com/en-us/office/what-is-presenter-view-98f31265-9630-41a7-a3f1-9b4736928ee3)

---

# Eindadvies

De krachtigste interactieve PowerPoint is geen verzameling losse effecten, maar een consistente lesomgeving. Gebruik daarom:

```text
verhaal en context
→ begrijpen
→ taal opmerken
→ oefenen met afbouwende steun
→ zelfstandig produceren
→ feedback
→ hernemen in een nieuwe situatie
```

De PowerPoint ondersteunt die didactische beweging met navigatie, media, animaties, triggers en feedback, maar vervangt de taalhandeling van de leerling niet.
