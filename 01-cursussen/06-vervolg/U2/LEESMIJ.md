# C6+ · Unidad 2 «Aquí vivo» — LEESMIJ (levering)

Paarse vervolgcursus (C6+), Unidad 2. Bouwt de A2-ruimte-motor: waar staat wat, wat gebeurt er nú, en woordgroepen korter maken.
**Thema:** wonen, de buurt, de weg.
**Kerngrammatica:** ① hay vs estar + preposiciones de lugar · ② estar + gerundio (aan het …) · ③ OD-pronomina lo/la/los/las. **P3-strand:** *me gusta mi barrio porque…*.
**Buiten scope (leerplan):** géén futuro simple / condicional / subjuntivo.
**Parada op La Ruta:** Cartagena 🇨🇴 (Colombia), gastvrouw Valen — de digitale kaart toont Colombia met ★ ¡Estás aquí! (thema «🏙️ Un lugar»).

## De vier formaten (in deze zip)

| Bestand | Wat | Hoe gebruiken |
|---|---|---|
| **C6plus_U2.pdf** | Print-cursus (45 p, 48 oefeningen) | Afdrukken/projecteren. Niet bewerkbaar. |
| **C6plus_U2_BEWERKBAAR.html** | Bewerkbare laag van de PDF | Chrome/Edge → **«Bewerken»** · **«Opslaan als PDF»** · **«Bewaar»**. |
| **C6plus_U2_web.html** | Digitale hub (standalone, offline) | 8 tabbladen: Vocabulario (flip cards) · Gramática (hay/estar · gerundio · lo/la, interactief) · Lectura · **Escuchar 🎧** · Juegos (12 spellen) · Hablar (opname) · Cultura (klikbare kaart, Colombia ★) · Extra. 100+ zelfcorrigerende oefeningen met «↻ otra serie». |
| **C6plus_U2_docente.pptx** | PowerPoint docent (21 dia's) | Vrije navigatie, oplossingen + didactiek in notities. Klik-onthul. |
| **C6plus_U2_alumno.pptx** | PowerPoint leerling (20 dia's) | **F5**; elke klik onthult het volgende antwoord. |

> **PowerPoint:** opent gewoon, zonder reparatievraag. Kwam die vroeger wél, dan had je een versie van vóór 2026-08-05: toen zat er een schemafout in elke vorm met een slagschaduw (twee `<a:effectLst>` in één `<p:spPr>`). Opgelost in de generatoren én in alle bestaande decks.

## Inhoud & didactiek
- **§0 ¡Ponte al día!** (repaso ser/estar + gustar) → **§1 la casa** (habitaciones · muebles) → **§2 hay vs estar + preposiciones** (§2.1/2.2/2.3) → **§3 estar + gerundio** (§3.1/3.2/3.3, incl. onregelmatige leyendo/durmiendo/pidiendo) → **§4 OD-pronomina lo/la/los/las** (§4.1/4.2/4.3, concordancia + plaats) → **§5 el barrio y cómo llegar** (de weg vragen/wijzen) → **§6 Lectura** → **Taller** (b/v + aquí/ahí/allí) → **§7 Lectura «Casa Azul»** → **§8 Escucha «Estoy perdido en Cartagena»** → **Cultura** (la vivienda hispana: patios, balcones, plazas) → **Tarea «Mapa de mi barrio»** → **Repaso** (semáforo) → **§V Vocabulario** (73 woorden, 8 groepen).
- **Elke § en subsectie start op een nieuwe bladzijde.** Steun bouwt af (MODELO → BANCO → MARCO → PISTA → SIN AYUDA). Vier vaardigheden geïntegreerd in print én PowerPoint.
- **Traditioneel × modern:** visueel-eerste grammatica (plattegrond-scène · richting-pijlen · vervangingskaart lo/la · werkwoordmachine gerundio) **náást** een klassieke oefenbatterij (gap-fill · substitutie · matching · dictee · ordenen · foutenkliniek · transformeren).
- **Bron oude cursus:** EELP U2 (estar + lugar, gerundio-hint, ser/estar-contrast) met de échte LPD-codes (III-Spa-d): casa/barrio **7**, hay/estar+preposiciones **8·4**, gerundio & lo/la **8**, de weg **4·9**, lezen **1·2·5**.

## Nieuw in deze ronde (1 augustus)

- **70 typvelden** waar de leerling zelf schrijft, geen keuzelijst: 34 in *Vocabulario*, 36 in *Gramática*. De drie grammatica-drills zijn **¿hay o está(n)?** (mét de tilde als deel van het antwoord), **estar + gerundio** (allebei de woorden, incl. leyendo/durmiendo/pidiendo/viendo) en **lo/la/los/las** (overeenkomst én plaats vóór het werkwoord).
- **§7 Lectura — «Casa Azul»: dos reseñas.** Twee beoordelingen van dezelfde woning, één enthousiast en één kritisch: de leerling vergelijkt standpunten, niet alleen feiten. Nieuw tekstgenre naast het prikbord (U0) en de blog (U1).
- **§8 Escucha — «Estoy perdido en Cartagena».** Sam belt Valen op voor de weg. Zes treden, transcript pas ná de taken. Ander genre en andere inhoud dan de leestekst: hier moet je een route volgen, niet een mening wegen.
- **Extra** — 14 bronnen in 6 groepen (ProfeDeELE · Más ProfeDeELE · Arche-ELE), geordend zoals de unit zelf.

## Wat nog niet af is

- De **QR-codes** in de print wijzen nog niet naar een echte pagina; dat gebeurt in één sweep zodra de site online staat.
- Het **luisteren** gebruikt de stem van je browser (TTS). Zodra er echte opnames zijn, pikt de hub die automatisch op.
- De **PowerPoints** in deze zip zijn nog de vorige versie (21/20 dia's). De dia's §5 Lectura en §6 Escucha staan in `gen_c6plus_u2_docente.py` klaar, maar konden in deze bouwsessie niet gerenderd worden: python-pptx is niet installeerbaar omdat de omgeving PyPI blokkeert (zie `03-build/SETUP_OMGEVING.md`). Eén keer het script draaien in een omgeving mét python-pptx volstaat.

## Kwaliteitscontrole (uitgevoerd)
- Print: **div-balans == 0**, geen doorgesneden tabellen, geen sectiekop onderaan, geen bare slotblokken; bladspiegel gemeten + visueel gecontroleerd.
- Hub: elk tabblad aangeklikt (geen lege panelen), **0 JS-fouten** (node --check), 17 grammatica-widgets, spellen openen; kaart-klik op **Colombia → ★ + «Un lugar» + Cartagena** geverifieerd.
- Hercontrole 1 augustus in Chromium: **8 tabbladen**, 70 zichtbare typvelden, zes luistertreden, transcript dicht tot ná de taken, geen consolefouten, kaart-fiche nog intact.
- PowerPoint: beide `.pptx` openen via python-pptx, zip-integriteit OK, 0 XML-fouten, **paars (0 groen-lek)**, 21/20 dia's, 96 klik-onthullingen, 32 hyperlinks, 4 vaardigheden.

## Regenereren
```
python3 01-cursussen/06-vervolg/U2/gen_c6plus_u2_print.py            # → C6plus_U2.html → PDF (Chromium)
python3 spaans-motor/make_c6plus_u2_games.py && node spaans-motor/build.mjs
python3 03-build/web/patch_maps_c6plus.py                            # bakt de kaart-fiche in (idempotent, U0–U2)
python3 03-build/web/gen_c6plus_u2_web.py                            # → 03-build/web/C6plus_U2_web.html
python3 03-build/pptx/gen_c6plus_u2_docente.py                      # → C6plus_U2_docente/alumno.pptx
```
Single source: `u2_vocab.json` + `U2_cocktail.md` + `mapa_c6plus.py` (route/thema's).
