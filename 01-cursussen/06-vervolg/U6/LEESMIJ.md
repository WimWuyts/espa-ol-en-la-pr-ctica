# C6+ · Unidad 6 «Cuando era pequeño» — LEESMIJ (levering)

Paarse vervolgcursus (C6+), Unidad 6. Sluit de verleden-tijdenboog (U4–U6) af met de tweede grote verledentijd.
**Thema:** de jeugd, hoe het vroeger was, herinneringen en nostalgie.
**Kerngrammatica:** ① pretérito imperfecto (era, tenía, jugaba, iba; 3 onregelmatige: era/iba/veía) — voor achtergrond, gewoontes en beschrijving · ② contraste indefinido ↔ imperfecto (afgerond feit vs. achtergrond) · ③ comparativos + que (más/menos… que, tan… como, mejor/peor/mayor/menor) + betrekkelijke que. **P3-strand:** mini-mening (*creo que antes era mejor porque…*).
**Buiten scope (leerplan):** géén futuro simple / condicional / subjuntivo.
**Parada op La Ruta:** Cusco 🇵🇪 (Peru), gastvrouw **Nina** — de digitale kaart toont Peru met ★ ¡Estás aquí! (thema «👪 En familia: muchos apellidos tienen raíces quechuas»).

## De vier formaten (in deze zip)

| Bestand | Wat | Hoe gebruiken |
|---|---|---|
| **C6plus_U6.pdf** | Print-cursus (29 genummerde + tarea/★ + 5 V oefeningen) | Afdrukken/projecteren. Niet bewerkbaar. |
| **C6plus_U6_BEWERKBAAR.html** | Bewerkbare laag van de PDF | Chrome/Edge → **«Bewerken»** · **«Opslaan als PDF»** · **«Bewaar»**. |
| **C6plus_U6_web.html** | Digitale hub (standalone, offline) | 7 tabbladen: Vocabulario (flip cards) · Gramática (imperfecto · contraste · comparativos, interactief) · Lectura · Juegos (12 spellen) · Hablar (opname) · Cultura (klikbare kaart, Perú ★ familia) · Extra. 100+ inline-oefeningen + 12 games met «↻ otra serie». |
| **C6plus_U6_docente.pptx** | PowerPoint docent (21 dia's) | Vrije navigatie, oplossingen + didactiek in notities. Klik-onthul. |
| **C6plus_U6_alumno.pptx** | PowerPoint leerling (20 dia's) | **F5**; elke klik onthult het volgende antwoord. |

> **Let op (PowerPoint):** PowerPoint kan bij het openen «Repareren» vragen — dat is normaal (de klik-onthul-animaties). Bevestigen; de animaties werken dan.

## Inhoud & didactiek
- **§0 ¡Ponte al día!** (indefinido → imperfecto) → **§1 la infancia** (woordenschat + antes↔ahora) → **§2 el imperfecto** (§2.1 machine/regla · §2.2 irregulares era/iba/veía · §2.3 practicar) → **§3 contraste indef. ↔ imperf.** (achtergrond of feit?) → **§4 comparativos + que** (más/menos/tan + betrekkelijke que) → **§5 Lectura** («El pueblo de mi abuela» — recuerdo) → **Taller** (acentos in het imperfecto -ía + y/ll + conectoren van vergelijking) → **Cultura** (la infancia en el mundo hispano · Cusco/Perú) → **Tarea «Cuando era pequeño/a»** → **Repaso** (semáforo) → **§V Vocabulario** (54 woorden, groepen infancia/escuela/familia/imperfecto/antes-ahora/comparar/relativo/opinar).
- **Elke § en subsectie start op een nieuwe bladzijde.** Steun bouwt af (MODELO → BANCO → MARCO → PISTA → SIN AYUDA). Vier vaardigheden geïntegreerd.
- **Traditioneel × modern:** visueel-eerste grammatica (imperfecto-machine · contrastkaart achtergrond/feit · vergelijkingsbalk más/menos/tan) **náást** een klassieke oefenbatterij (gap-fill · substitutie · matching · dictee · ordenen · foutenkliniek · transformeren).
- **Werkwoordsvormen nagerekend:** regelmatige imperfecto (-aba/-ábamos; -ía/-íamos); de 3 onregelmatige (era/eras/era…; iba/ibas/iba…; veía/veías…); comparativos onregelmatig (mejor/peor/mayor/menor).
- Échte LPD-codes (III-Spa-d): imperfecto/contrast/comparativos **8**, woordenschat **7**, beschrijven/vertellen **3**, interactie **4**, lezen/cultuur **1·2·5**.

## Kwaliteitscontrole (uitgevoerd)
- Print: **div-balans == 0**, geen doorgesneden tabellen, geen bare slotblokken; bladspiegel gemeten (geen dunne pagina's) + visueel gecontroleerd.
- Hub: elk tabblad aangeklikt (geen lege panelen), **0 JS-fouten**, zelfcorrigerende widgets + 12 spellen; kaart-klik op **Perú → ★ + «👪 En familia» + Cusco (Nina)** geverifieerd.
- PowerPoint: beide `.pptx` openen via python-pptx, zip-integriteit OK, 0 XML-fouten, **paars (0 groen-lek)**, 21/20 dia's, 102 klik-onthullingen, 32 hyperlinks, 4 vaardigheden.

## Regenereren
```
python3 01-cursussen/06-vervolg/U6/gen_c6plus_u6_print.py            # → C6plus_U6.html → PDF (Chromium)
python3 spaans-motor/make_c6plus_u6_games.py && node spaans-motor/build.mjs
python3 03-build/web/patch_maps_c6plus.py                            # bakt de kaart-fiche in (idempotent, U0–U6)
python3 03-build/web/gen_c6plus_u6_web.py                            # → 03-build/web/C6plus_U6_web.html
python3 03-build/pptx/gen_c6plus_u6_docente.py                      # → C6plus_U6_docente/alumno.pptx
```
