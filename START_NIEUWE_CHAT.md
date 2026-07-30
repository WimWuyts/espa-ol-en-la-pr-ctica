# Startprompt voor de nieuwe bouwchat

> Kopieer het blok hieronder als eerste bericht in de nieuwe chat.

---

Werk op branch **`claude/spanish-course-development-jx25ay`** (de verzamelbranch met C4, C5, C6+ en de motor).

**Lees eerst, in deze volgorde:** `CLAUDE.md` · `HANDOVER_VOLGENDE_CHAT.md` · `BOUWPLAN_SWEEP.md` · `FEEDBACK_BLUEPRINTS.md`. De canonieke oefeninhoud staat in `00-brondocumenten/gap-analyse/` (twee blueprints).

## Wat je bouwt

**Fase 1 — gereedschap (eerst, blokkeert de rest):**
1. Trek de zes hub-bouwers (`buildChoice`, `buildMatch`, `buildOrder`, `buildOdd`, `buildInlineExercises`, `buildRecorders`) samen in `03-build/web/hub_drills.py`. Ze staan nu **17× gekopieerd**. Dit is een **no-op refactor**: na afloop moeten alle 17 hubs identiek zijn op whitespace na, en `python3 03-build/check_regressie.py` moet schoon zijn.
2. Voeg `buildType` toe: getypte drill in het paneel, met `Comprobar` · `Reintentar` · score over de volledige set · doorlopende nummering · toetsenbord · zichtbare focus · ARIA · fout niet alleen met kleur.
3. Luistercomponent met **verwisselbare audiobron**: browser-TTS nu, mp3 automatisch zodra die bestaat.

**Daarna ronde 1 — C5 U0 én C6+ U0**, elk compleet: hub + printlaag + PDF + 2 PowerPoints. Dan pas U1, U2, enzovoort.

## Per unit toevoegen

- de blueprint-oefeningen voor die unit (ID's exact overnemen, `console.assert` op het itemaantal);
- de getypte woordenschatladder: `python3 spaans-motor/make_vocab_type_games.py C5 <n>` → 5 oefeningen, 12 items × 3 rondes (8 bij open productie);
- **één leestekst én één luisteroefening**, elk op twee plaatsen: print (met antwoordruimte + QR) én interactief in de hub. Tekstsoort kies je bij het thema (dialoog · informatieve tekst · interview). Luisterladder: situatie vooraf → globaal → 5 detailvragen → juist/fout **met bewijs** → transcript pas ná de taken → productieve reactie;
- het **QR-balkje** naast elke corresponderende oefening: `python3 03-build/web/gen_qr_extra.py --oefening <ID>`.

## Bindende regels

- **Cursuslaag: alleen toevoegen, nooit weglaten.** Bestaande oefeningen, secties en nummering blijven staan; nieuwe krijgen een eigen subsectienummer erachter.
- **Lange sets:** visuele blokken van 10–12, maar **doorlopende nummering en één totaalscore** over de volledige canonieke set.
- **Accenten:** verplicht bij werkwoordsvormen (*hablo ≠ habló*), tolerant bij woordenschat met het accent zichtbaar in de correctie.
- **Overlap:** nieuwe sets komen **náást** de bestaande spellen, als andere trede. Niets verwijderen.
- **Game-ID's nooit hernoemen** — de hub-generators linken erop.
- **Draai `python3 03-build/check_regressie.py` na elke stap.** Er mag bij komen, er mag niets weg.
- Corrigeer de zes fouten in de canonieke inhoud (`BOUWPLAN_SWEEP.md` fase 2) en vermeld elke correctie in het implementatierapport.

## Netwerk

**WebSearch werkt** — daarmee vind je URL's op paginadelespanol.com voor `03-build/web/qr_links.json` (196 onderwerpen, 0 ingevuld). **WebFetch is geblokkeerd** (403). Vraag de auteur of hij `paginadelespanol.com` aan de allowlist heeft toegevoegd; zonder ophalen kan je de **scope niet controleren** — die site bevat ook subjuntivo-oefeningen, en subjuntivo/condicional/futuro simple vallen buiten III-Spa-d.

## Vraag dit meteen aan de auteur

«Op twee plaatsen» heb ik gelezen als **print + digitaal** (dezelfde tekst en oefening in beide dragers). Bedoelde je **twee leesteksten en twee luisteroefeningen per unit**? Bevestig vóór je U0 bouwt.

## Sleutels (optioneel, blokkeren niets)

`ELEVENLABS_API_KEY` of `GOOGLE_TTS_API_KEY` als omgevingsvariabele → dan draai je
`python3 03-build/web/gen_audio_elevenlabs.py C5 0 --split` voor echte dialoogaudio. Zonder sleutel werkt browser-TTS.

## Lever op na ronde 1

De twee bijgewerkte hubs, de twee PDF's, vier PowerPoints, een schone regressiecheck, en een kort implementatierapport (gewijzigde bestanden · itemaantallen geteld · afwijkingen).
