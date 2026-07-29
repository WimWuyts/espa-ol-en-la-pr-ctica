# C6+ · Unidad 5 «Érase una vez» — LEESMIJ (levering)

Paarse vervolgcursus (C6+), Unidad 5. Bouwt de kern-verleden tijd (indefinido) en de dubbele voornaamwoorden.
**Thema:** biografieën, verhalen en figuren uit het verleden.
**Kerngrammatica:** ① pretérito indefinido (regelmatig + de sterke vormen fue/hizo/tuvo/estuvo/dijo…) · ② OD+OI gecombineerd (se lo / se la). **P3-strand:** mini-mening over een figuur (*creo que fue un genio porque…*).
**Buiten scope (leerplan):** géén imperfecto (dat is U6), géén futuro simple / condicional / subjuntivo.
**Parada op La Ruta:** Buenos Aires 🇦🇷 (Argentinië), gastheer **Mateo** (voseo) — de digitale kaart toont Argentinië met ★ ¡Estás aquí! (thema «⭐ Alguien de aquí»). **Nieuw personage in de cast: Mateo.**

## De vier formaten (in deze zip)

| Bestand | Wat | Hoe gebruiken |
|---|---|---|
| **C6plus_U5.pdf** | Print-cursus (29 genummerde + 4 ★/tarea + 5 V oefeningen) | Afdrukken/projecteren. Niet bewerkbaar. |
| **C6plus_U5_BEWERKBAAR.html** | Bewerkbare laag van de PDF | Chrome/Edge → **«Bewerken»** · **«Opslaan als PDF»** · **«Bewaar»**. |
| **C6plus_U5_web.html** | Digitale hub (standalone, offline) | 7 tabbladen: Vocabulario (flip cards) · Gramática (indefinido · fuertes · se lo, interactief) · Lectura · Juegos (12 spellen) · Hablar (opname) · Cultura (klikbare kaart, Argentina ★ persona) · Extra. 100+ inline-oefeningen + 12 games met «↻ otra serie». |
| **C6plus_U5_docente.pptx** | PowerPoint docent (21 dia's) | Vrije navigatie, oplossingen + didactiek in notities. Klik-onthul. |
| **C6plus_U5_alumno.pptx** | PowerPoint leerling (20 dia's) | **F5**; elke klik onthult het volgende antwoord. |

> **Let op (PowerPoint):** PowerPoint kan bij het openen «Repareren» vragen — dat is normaal (de klik-onthul-animaties). Bevestigen; de animaties werken dan.

## Inhoud & didactiek
- **§0 ¡Ponte al día!** (perfecto → indefinido) → **§1 biografía y logros** → **§2 el indefinido** (§2.1 regular · §2.2 fuertes · §2.3 practicar) → **§3 se lo / se la** (§3.1 sistema · §3.2 practicar) → **§4 contar una historia** (conectoren) → **§5 Lectura** («Una vida de película» — Frida Kahlo / Messi) → **Taller** (ortografía c→qu/g→gu/z→c bij yo + conectoren) → **Cultura** (figuras hispanas + het voseo van Mateo) → **Tarea «Una biografía»** → **Repaso** (semáforo) → **§V Vocabulario** (66 woorden, 8 groepen).
- **Elke § en subsectie start op een nieuwe bladzijde.** Steun bouwt af (MODELO → BANCO → MARCO → PISTA → SIN AYUDA). Vier vaardigheden geïntegreerd; literatuur-component (LPD 6) via biografía/leyenda.
- **Traditioneel × modern:** visueel-eerste grammatica (indefinido-machine · fuertes-paren · se lo-vervangingskaart) **náást** een klassieke oefenbatterij (gap-fill · substitutie · matching · dictee · ordenen · foutenkliniek · transformeren).
- **Werkwoordsvormen nagerekend:** regelmatige indefinido (-é/-ó, -í/-ió); sterke vormen (fue/hizo/tuvo/estuvo/dijo/vino/dio/vio); se lo/se la-combinaties; yo-spelling (busqué/llegué/empecé).
- Échte LPD-codes (III-Spa-d): biografía **7·6**, indefinido/se lo **8**, vertellen **3**, interactie **4**, literatuur **6**, lezen **1·2·5**, cultuur **5**.

## Kwaliteitscontrole (uitgevoerd)
- Print: **div-balans == 0**, geen doorgesneden tabellen, geen bare slotblokken; bladspiegel gemeten (geen dunne pagina's) + visueel gecontroleerd.
- Hub: elk tabblad aangeklikt (geen lege panelen), **0 JS-fouten**, 19 zelfcorrigerende widgets + 12 spellen; kaart-klik op **Argentina → ★ + «⭐ Alguien de aquí» + Buenos Aires (Mateo)** geverifieerd.
- PowerPoint: beide `.pptx` openen via python-pptx, zip-integriteit OK, 0 XML-fouten, **paars (0 groen-lek, 398/395 hits)**, 21/20 dia's, 104 klik-onthullingen, 32 hyperlinks, 4 vaardigheden.

## Regenereren
```
python3 01-cursussen/06-vervolg/U5/gen_c6plus_u5_print.py            # → C6plus_U5.html → PDF (Chromium)
python3 spaans-motor/make_c6plus_u5_games.py && node spaans-motor/build.mjs
python3 03-build/web/patch_maps_c6plus.py                            # bakt de kaart-fiche in (idempotent, U0–U5)
python3 03-build/web/gen_c6plus_u5_web.py                            # → 03-build/web/C6plus_U5_web.html
python3 03-build/pptx/gen_c6plus_u5_docente.py                      # → C6plus_U5_docente/alumno.pptx
```
Single source: `u5_vocab.json` + `U5_cocktail.md` + `mapa_c6plus.py` (route/thema's). Cast: `cast_gen.py` (Mateo).
