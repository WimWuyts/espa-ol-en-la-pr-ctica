# C6+ · Unidad 4 «De viaje» — LEESMIJ (levering)

Paarse vervolgcursus (C6+), Unidad 4. Bouwt de eerste échte verleden tijd: de voltooide tijd, plus por/para.
**Thema:** reizen, vervoer, verblijf en recente ervaringen.
**Kerngrammatica:** ① pretérito perfecto compuesto (haber + participio, incl. onregelmatige) · ② por / para (intro). **P3-strand:** mini-mening over de reis (*lo mejor ha sido… porque…*).
**Buiten scope (leerplan):** géén indefinido/imperfecto (dat is U5–U6), géén futuro simple / condicional / subjuntivo.
**Parada op La Ruta:** Chile 🇨🇱 · el gran viaje — de digitale kaart toont Chile met ★ ¡Estás aquí! (thema «✈️ Para visitar»).

## De vier formaten (in deze zip)

| Bestand | Wat | Hoe gebruiken |
|---|---|---|
| **C6plus_U4.pdf** | Print-cursus (15 bladspiegels, 31 genummerde + 4 ★/tarea + 5 V oefeningen) | Afdrukken/projecteren. Niet bewerkbaar. |
| **C6plus_U4_BEWERKBAAR.html** | Bewerkbare laag van de PDF | Chrome/Edge → **«Bewerken»** · **«Opslaan als PDF»** · **«Bewaar»**. |
| **C6plus_U4_web.html** | Digitale hub (standalone, offline) | 7 tabbladen: Vocabulario (flip cards) · Gramática (perfecto · participios · por/para, interactief) · Lectura · Juegos (12 spellen) · Hablar (opname) · Cultura (klikbare kaart, Chile ★ viaje) · Extra. 100+ inline-oefeningen + 12 games met «↻ otra serie». |
| **C6plus_U4_docente.pptx** | PowerPoint docent (21 dia's) | Vrije navigatie, oplossingen + didactiek in notities. Klik-onthul. |
| **C6plus_U4_alumno.pptx** | PowerPoint leerling (20 dia's) | **F5**; elke klik onthult het volgende antwoord. |

> **Let op (PowerPoint):** PowerPoint kan bij het openen «Repareren» vragen — dat is normaal (de klik-onthul-animaties). Bevestigen; de animaties werken dan.

## Inhoud & didactiek
- **§0 ¡Ponte al día!** (repaso presente + ir a) → **§1 transporte y alojamiento** → **§2 el perfecto compuesto** (§2.1 sistema/máquina · §2.2 participios irregulares · §2.3 practicar) → **§3 por / para** (§3.1 contraste · §3.2 practicar) → **§4 experiencias y lugares** (ya/todavía no/nunca/alguna vez) → **§5 Lectura** («Un viaje inolvidable» — Nina/Diego) → **Taller** (h muda + conectores de secuencia) → **Cultura** (el gran viaje hispano: Atacama, Camino de Santiago, Rapa Nui) → **Tarea «Mi mejor viaje»** → **Repaso** (semáforo) → **§V Vocabulario** (72 woorden, 8 groepen).
- **Elke § en subsectie start op een nieuwe bladzijde.** Steun bouwt af (MODELO → BANCO → MARCO → PISTA → SIN AYUDA). Vier vaardigheden geïntegreerd in print én PowerPoint.
- **Traditioneel × modern:** visueel-eerste grammatica (haber-machine · participio-paren · por/para-beslisboom) **náást** een klassieke oefenbatterij (gap-fill · substitutie · matching · dictee · ordenen · foutenkliniek · transformeren · vertalen).
- **Bron:** de perfecto is de eerste A2-verleden tijd (leerplan). Échte LPD-codes (III-Spa-d): viaje **7**, perfecto **8·3**, participios/por-para **8**, interactie **4**, lezen **1·2·5**, cultuur **5**.

## Kwaliteitscontrole (uitgevoerd)
- Print: **div-balans == 0**, geen doorgesneden tabellen, geen bare slotblokken; bladspiegel gemeten (geen dunne pagina's) + visueel gecontroleerd.
- Hub: elk tabblad aangeklikt (geen lege panelen), **0 JS-fouten**, 19 zelfcorrigerende widgets + 12 spellen; kaart-klik op **Chile → ★ + «✈️ Para visitar» + el gran viaje** geverifieerd.
- PowerPoint: beide `.pptx` openen via python-pptx, zip-integriteit OK, 0 XML-fouten, **paars (0 groen-lek, 398/395 hits)**, 21/20 dia's, 104 klik-onthullingen, 32 hyperlinks, 4 vaardigheden.
- **Werkwoordsvormen nagerekend:** haber (he/has/ha/hemos/habéis/han) + participio; onregelmatige participios (hecho/visto/dicho/vuelto/puesto/escrito/abierto/roto); por/para-gevallen.

## Regenereren
```
python3 01-cursussen/06-vervolg/U4/gen_c6plus_u4_print.py            # → C6plus_U4.html → PDF (Chromium)
python3 spaans-motor/make_c6plus_u4_games.py && node spaans-motor/build.mjs
python3 03-build/web/patch_maps_c6plus.py                            # bakt de kaart-fiche in (idempotent, U0–U4)
python3 03-build/web/gen_c6plus_u4_web.py                            # → 03-build/web/C6plus_U4_web.html
python3 03-build/pptx/gen_c6plus_u4_docente.py                      # → C6plus_U4_docente/alumno.pptx
```
Single source: `u4_vocab.json` + `U4_cocktail.md` + `mapa_c6plus.py` (route/thema's).
