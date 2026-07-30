# Overdracht → volgende chat

> Geschreven 2026-07-29 aan het einde van de brainstorm-/ontwikkelchat.
> **Lees dit samen met `CLAUDE.md`.** Alles hieronder is gecontroleerd, niet gegokt.
> Werkbranch: `claude/spanish-course-development-jx25ay` (de verzamelbranch).

---

## 1 · Waar het project staat

| Cursus | Units | Formaten | Opmerking |
|---|---|---|---|
| **C4** 🔴 | U1–U10 (van 14) | hub · print-PDF · 2 PPTX · componenten | eigen chat/branch `claude/c4-spanish-handover-yaa2a8` |
| **C5** 🟢 | U0–U8 **compleet** | idem (hub = `03-build/web/U<N>_web.html`) | versie 1 |
| **C6+** 🟣 | U0–U7 **compleet** | idem (`C6plus_U<N>_web.html`) | eigen chat/branch `claude/spanish-c6plus-u1-386jov` |
| **C6** 🔵 | — | — | nog niet begonnen (bewuste keuze auteur) |
| **Motor** | 314 spellen | 13 templates | zie `spaans-motor/README.md` |

**Branches:** ontwikkel op de verzamelbranch; de twee cursus-chats werken door op hun
eigen branch. Periodiek mergen naar de verzamelbranch (dat is deze chat steeds geweest).

**Zips:** `python3 03-build/make_zip.py C5|C6+|C4` bouwt ze uit de *huidige* bestanden.
Nooit een oude zip hergebruiken — dat ging één keer mis (bevatte nog tetris i.p.v. pinball).

---

## 2 · Het openstaande probleem (belangrijkste punt van deze overdracht)

De auteur stelde vast: **de digitale pagina's bestaan bijna volledig uit klik-oefeningen.**
Gemeten over de 17 hubs van C5 + C6+:

| Waar | Wat er staat | Typwerk |
|---|---|---|
| Panelen «Vocabulario» / «Gramática» | `buildChoice` 185 · `buildMatch` 60 · `buildOrder` 49 · `buildOdd` 32 | **0** |
| Motor-spellen | 291 spellen | **0** (behalve de U3-pilot) |

Dat botst met bindende instructies: **§14** (vijf fasen: herkennen → onderscheiden →
ophalen → gestuurd produceren → vrij produceren; steun bouwt af), **§14bis** (élke unit
een klassieke cloze waarin de leerling werkwoordsvormen *invult*) en **§14ter**
(gap-fill-drills mét feedback in de vocab-/grammaticapanelen). De woordenschat blijft
overal steken bij *herkennen*: flashcards omdraaien + koppelen/aanwijzen.

Extra: de auteur liet de site door ChatGPT vergelijken met een commerciële methode en
kwam op **meer hiaten**. Die lijst is nog niet in de repo → **vraag ernaar en zet ze in
`00-brondocumenten/gap-analyse/` als checklist** vóór je aan de sweep begint.

### Wat al gebouwd is als antwoord (klaar, getest)

- **`type`-template** in de motor: getypte productie, normalisatie (accent-tolerant,
  ñ blijft betekenisdragend), meerdere geldige antwoorden, letterhint, open-modus met
  structuurcheck + «Ver modelo», en **series** (`options.series`) met tussenscherm.
- **`make_vocab_type_games.py`**: genereert 5 typ-oefeningen per unit uit de bestaande
  `u<N>_vocab.json`. **Pilot staat op C5 U3** (hub-groep «⑥ Escribir»): pools
  62/40/64/71/69 → 3 verse rondes, 84 getypte antwoorden per doorloop.
- Afspraak auteur: **12 items per ronde** (8 bij open productie), **3 rondes**.

### Wat nog moet (in volgorde)

1. **`buildType` in de panelen.** De 185 `buildChoice`-pools bevatten `ans` én `why` al —
   een getypte variant is bijna gratis (opties weglaten). ⚠️ **Die JS staat 17× gekopieerd**
   (één keer per `gen_*_web.py`). Advies: eerst de bouwers naar één gedeelde module
   (`03-build/web/hub_drills.py`) trekken, dán `buildType` toevoegen — anders raak je bij
   elke latere verbetering opnieuw 17 bestanden aan.
2. **Woordenschatpaneel**: typ-oefeningen uit `u<N>_vocab.json` + **typmodus op de
   flashcards** (typen i.p.v. omdraaien).
3. **Grammatica**: verbo-cloze *libre* (typen i.p.v. kiezen — dit maakt §14bis pas echt
   waar), transformación, construye la frase.
4. **Uitrol** van de U3-pilot over de overige 16 units (grotendeels generatorwerk).
5. **Openstaande vragen aan de auteur** (nog niet beantwoord): voelen 12×3 goed?
   accenten tolerant of streng? letterhint standaard aan of soms uit?

### Openstaande vraag van de auteur (onbeantwoord gebleven)

*Blijven de bestaande klik-versies staan naast de getypte?* Mijn advies was: **ja, behouden** —
ze zijn fase 1–3 van de ladder; het probleem is dat de ladder daar stopt, niet dat ze bestaan.
Alleen de werkwoord-clozes verdienen een getypte tweelingversie (fase 4).

---

## 3 · Aanbeveling: maak de spec meetbaar

De reden dat dit hiaat kon ontstaan is dat `CLAUDE.md` proza is: «≥8 productieve slots»
staat er wel, maar niets *toetst* het. Bouw daarom vroeg in de volgende chat een
**conformiteitscheck** (`03-build/check_unit.py <cursus> <unit>`) die per unit meet:

- aantal productieve slots (typen/spreken) vs. receptief — norm >50 %, ≥6 getypt, ≥2 spreken
- ≥1 getypte werkwoord-cloze · ≥1 luisterdialoog · ≥1 Lectura · ≥2 opname-oefeningen
- ≥8 verschillende motor-speltypes · pool ≥12 per spel (nu haalt lang niet elk spel dat)
- ≥100 interactieve oefeningen op de hub
- geen meta/placeholders in de leerlingeditie (§18)

Laat hem **falen met een duidelijke lijst**. Dan is «voldoet aan het didactieksysteem»
een testuitslag in plaats van een interpretatie — en zie je bij elke unit meteen wat ontbreekt.

---

## 4 · Werkafspraken die in deze chat zijn vastgelegd

- **Arcade-rotatie uitgevoerd** (C5 + C6+): elk van de 8 skins 1× per cursus, tetris van
  16× naar 2×. Skins toegewezen op het aantal categorieën (bubbels/mollen/snake bij 6;
  torens/deuren/pinball bij 3–5). Zie `spaans-motor/PLAN_MOTOR_C4_C6_C6plus.md` §6bis.
- **17 spellen die in géén hub stonden** zijn toegevoegd (C5 U1–U5). Dekking nu 291/291
  — *meet dit opnieuw na elke wijziging*, het was stil misgegaan.
- **Game-ID's nooit hernoemen**: de hub-generators linken op ID.
- **Ketenregel**: elke wijziging aan een spel raakt drie plaatsen —
  `make_<unit>_games.py` → `node build.mjs` → `gen_<unit>_web.py`. Zie het schema in
  `spaans-motor/README.md`.
- **Catalogus**: `spaans-motor/catalogos/` (inventaris ES + voorstel-lijsten NT2/Engels,
  met generator). De motor is taal-onafhankelijk; alleen de TTS-taalcode en een handvol
  Spaanse chrome-woordjes zitten nog vast — zie de i18n-notitie hieronder.

### Nog niet gedaan, wel besproken
- **i18n-laagje** voor NT2/Engels (TTS-taalcode + ~10 UI-woordjes in `speak`/`type`).
- **Motor als losse `motor.bundle.js`** afleveren voor gebruik in een andere cursus.
- **Klassikale set** (pubquiz · codenames · werewolf · estafette) uit het motorplan §8-5.
- **Hosting-sweep** (§18): echte QR-codes → Netlify-URL + ankers, Extra-links invullen.

---

## 5 · Hoe je de volgende chat begint

1. Nieuwe chat in dezelfde groep, op branch `claude/spanish-course-development-jx25ay`.
2. Eerste opdracht: **de hiatenlijst van de auteur inlezen** (ChatGPT-vergelijking) en
   samen met §2 hierboven tot één werklijst maken.
3. Daarna: gedeelde `hub_drills.py` + `buildType` + de conformiteitscheck (§3).
4. Pas dan uitrollen over de units — met de check als poortwachter.
