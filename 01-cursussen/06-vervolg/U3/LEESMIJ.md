# C6+ · Unidad 3 «Conectados» — LEESMIJ (levering)

Paarse vervolgcursus (C6+), Unidad 3. Bouwt de A2-toekomst-motor: plannen maken, aan wie je iets doet, en je eerste echte mening.
**Thema:** media, technologie, sociale media en weekendplannen.
**Kerngrammatica:** ① ir a + infinitivo (futuro próximo) + acabar de · ② OI-pronomina le/les (¿a quién?) · ③ creo que + INDICATIVO (mening). **P3-strand:** *creo que las redes son útiles porque…*.
**Buiten scope (leerplan):** géén futuro simple / condicional / subjuntivo — «creo que» gaat mét indicativo.
**Parada op La Ruta:** Ciudad de México 🇲🇽 (México), gastheer Diego — de digitale kaart toont México met ★ ¡Estás aquí! (thema «🎵 Música»).

## De vier formaten (in deze zip)

| Bestand | Wat | Hoe gebruiken |
|---|---|---|
| **C6plus_U3.pdf** | Print-cursus (36 p, 35 genummerde + 5 ★/tarea + 5 V = 45 oefeningen) | Afdrukken/projecteren. Niet bewerkbaar. |
| **C6plus_U3_BEWERKBAAR.html** | Bewerkbare laag van de PDF | Chrome/Edge → **«Bewerken»** · **«Opslaan als PDF»** · **«Bewaar»**. |
| **C6plus_U3_web.html** | Digitale hub (standalone, offline) | 7 tabbladen: Vocabulario (flip cards) · Gramática (ir a · le/les · creo que, interactief) · Lectura · Juegos (13 spellen) · Hablar (opname) · Cultura (klikbare kaart, México ★ música) · Extra. 164 inline-oefeningen + 13 games met «↻ otra serie». |
| **C6plus_U3_docente.pptx** | PowerPoint docent (21 dia's) | Vrije navigatie, oplossingen + didactiek in notities. Klik-onthul. |
| **C6plus_U3_alumno.pptx** | PowerPoint leerling (20 dia's) | **F5**; elke klik onthult het volgende antwoord. |

> **Let op (PowerPoint):** PowerPoint kan bij het openen «Repareren» vragen — dat is normaal (de klik-onthul-animaties). Bevestigen; de animaties werken dan.

## Inhoud & didactiek
- **§0 ¡Ponte al día!** (repaso presente + gustar→le/les) → **§1 el móvil y las redes** (aparatos · redes · acciones) → **§2 ir a + infinitivo** (§2.1 sistema/máquina · §2.2 expresiones de tiempo · §2.3 practicar) → **§3 le/les** (§3.1 ¿qué es? · §3.2 verbos de comunicación · §3.3 posición) → **§4 acabar de + creo que + indicativo** (§4.1 acabar de · §4.2 creo que · vrije mening) → **§5 comunicar y hacer planes** (chat + info-gap) → **§6 Lectura** («¿Adicto al móvil?» — Diego/Lucía) → **Taller** (c/z/qu + conectores de tiempo) → **Cultura** (el mundo digital hispano: reguetón, WhatsApp, el español online) → **Tarea «Mi plan de fin de semana»** → **Repaso** (semáforo) → **§V Vocabulario** (74 woorden, 7 groepen).
- **Elke § en subsectie start op een nieuwe bladzijde.** Steun bouwt af (MODELO → BANCO → MARCO → PISTA → SIN AYUDA). Vier vaardigheden geïntegreerd in print én PowerPoint.
- **Traditioneel × modern:** visueel-eerste grammatica (ir a-machine · tijdlijn nú→straks · le/les-vervangingskaart · creo que-observatiekader) **náást** een klassieke oefenbatterij (gap-fill · substitutie · matching · dictee · ordenen · foutenkliniek · vertalen).
- **Bron oude cursus:** media/tech/ir a/OI zijn ✗ in EELP (gap) → zelf gebouwd; de comunicación- en cognición-werkwoorden komen uit de master-pool. Échte LPD-codes (III-Spa-d): media/redes **7**, ir a + infinitivo **8·3**, le/les **8·7·4**, acabar de/creo que **8·3**, interactie **4**, lezen **1·2·5**, cultuur **5**.

## Kwaliteitscontrole (uitgevoerd)
- Print: **div-balans == 0**, geen doorgesneden tabellen, geen sectiekop onderaan, geen bare slotblokken; bladspiegel gemeten (geen dunne/lege pagina's, 36 p) + visueel gecontroleerd (hero + grammatica-spread).
- Hub: elk tabblad aangeklikt (geen lege panelen), **0 JS-fouten**, 19 zelfcorrigerende widgets (164 inline-items) + 13 spellen; kaart-klik op **México → ★ + «🎵 Música» + CDMX (Diego)** geverifieerd.
- PowerPoint: beide `.pptx` openen via python-pptx, zip-integriteit OK, 0 XML-fouten, **paars (0 groen-lek, 392/389 hits)**, 21/20 dia's, 96 klik-onthullingen, 32 hyperlinks, 4 vaardigheden.

## Regenereren
```
python3 01-cursussen/06-vervolg/U3/gen_c6plus_u3_print.py            # → C6plus_U3.html → PDF (Chromium)
python3 spaans-motor/make_c6plus_u3_games.py && node spaans-motor/build.mjs
python3 03-build/web/patch_maps_c6plus.py                            # bakt de kaart-fiche in (idempotent, U0–U3)
python3 03-build/web/gen_c6plus_u3_web.py                            # → 03-build/web/C6plus_U3_web.html
python3 03-build/pptx/gen_c6plus_u3_docente.py                      # → C6plus_U3_docente/alumno.pptx
```
Single source: `u3_vocab.json` + `U3_cocktail.md` + `mapa_c6plus.py` (route/thema's).
