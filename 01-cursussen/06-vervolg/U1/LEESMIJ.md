# C6+ · Unidad 1 «El día a día» — LEESMIJ (levering)

Paarse vervolgcursus (C6+), Unidad 1. Start van de A2-motor, bouwt op U0 (presente/género/países).
**Thema:** dagelijks leven, routine, de klok, gevoelens en smaken.
**Kerngrammatica:** ① reflexieve werkwoorden (me levanto…) · ② ser vs estar — het contrast · ③ gustar + OI (me/te/le gusta(n)). **P3-seed:** *me gusta… porque*.
**Buiten scope (leerplan):** géén futuro simple / condicional / subjuntivo.
**Parada op La Ruta:** España (el horario español), gastvrouw Lucía + Diego.

## De vier formaten (in deze zip)

| Bestand | Wat | Hoe gebruiken |
|---|---|---|
| **C6plus_U1.pdf** | Print-cursus (40 p, 44 oefeningen) | Afdrukken/projecteren. Niet bewerkbaar. |
| **C6plus_U1_BEWERKBAAR.html** | Bewerkbare laag van de PDF | Open in Chrome/Edge → knop **«Bewerken»** (pas tekst aan) · **«Opslaan als PDF»** · **«Bewaar»** (eigen versie downloaden). |
| **C6plus_U1_web.html** | Digitale hub (standalone, offline) | Open in de browser. 7 tabbladen: Vocabulario (flip cards) · Gramática (interactief) · Lectura · Juegos (13 spellen) · Hablar (opname) · Cultura (klikbare kaart) · Extra. 100+ zelfcorrigerende oefeningen met «↻ otra serie». |
| **C6plus_U1_docente.pptx** | PowerPoint docent (21 dia's) | Vrije navigatie, presenter view, oplossingen + didactiek in de notities. Klik-onthul-animaties. |
| **C6plus_U1_alumno.pptx** | PowerPoint leerling (20 dia's) | Druk **F5** voor de diavoorstelling; elke klik onthult het volgende antwoord. |

> **Let op (PowerPoint):** PowerPoint vraagt bij het openen soms «Repareren» — dat is normaal (de klik-onthul-animaties). Bevestig; de animaties werken dan.

## Inhoud & didactiek
- **§0 ¡Ponte al día!** (repaso presente + ser/estar) → **§1 la hora** → **§2 mi rutina** (acciones · conectores · frecuencia) → **§3 reflexivos** (§3.1/§3.2/§3.3, zware drillbatterij) → **§4 ser vs estar** (§4.1/§4.2/§4.3, contrast + sentimientos) → **§5 gustar + OI** (§5.1/§5.2/§5.3, escala + «me gusta… porque») → **§6 Lectura** → **Taller** (sílaba tónica + conectores) → **Cultura** (el horario español) → **Tarea «Mi día a día»** → **Repaso** (semáforo) → **§V Vocabulario** (78 woorden, 8 groepen).
- **Elke § en subsectie start op een nieuwe bladzijde.** Steun bouwt af: MODELO → BANCO → MARCO → PISTA → SIN AYUDA.
- **Vier vaardigheden geïntegreerd** (lezen·luisteren·spreken·schrijven) in print én PowerPoint.
- **Traditioneel × modern:** visueel-eerste grammatica (werkwoordmachine · beslisboom · minimale contrastparen · escala-schuifregelaar) **náást** een klassieke oefenbatterij (gap-fill · substitutie · matching · dictee · ordenen · foutenkliniek · vertalen al revés).
- **Bron oude cursus:** overgenomen oefeningen uit *Español en la práctica* U3 «El tiempo vuela» (rutina/reflexivos) en U4 «Me gusta» (gustar), met de **échte LPD-codes** (III-Spa-d): reflexivos/rutina **8·3 / 7·8·3**, gustar **8·7**, lezen **1·2·5**.
- **Parels:** «La Perla» (Rosalía) als luister-cloze; LatAm-gustos in de Lectura.

## Kwaliteitscontrole (uitgevoerd)
- Print: **div-balans == 0**, geen doorgesneden tabellen, geen sectiekop onderaan, geen bare slotblokken; bladspiegel gemeten + visueel gecontroleerd (contactblad).
- Hub: elk tabblad aangeklikt + gescreenshot (geen lege panelen), **0 JS-fouten**, 18 grammatica-widgets, spellen openen in het venster.
- PowerPoint: beide `.pptx` openen via python-pptx, zip-integriteit OK, **paars toegepast (0 groen-lek)**, 21/20 dia's, 98 klik-onthullingen, 32 hyperlinks, 4 vaardigheden.

## Regenereren (bron → formaten)
```
# print (PDF + bewerkbare laag)
python3 01-cursussen/06-vervolg/U1/gen_c6plus_u1_print.py       # → C6plus_U1.html
chromium --headless --print-to-pdf=C6plus_U1.pdf file://…/C6plus_U1.html
# motor-spellen
python3 spaans-motor/make_c6plus_u1_games.py && node spaans-motor/build.mjs
# digitale hub
python3 03-build/web/gen_c6plus_u1_web.py                        # → 03-build/web/C6plus_U1_web.html
# PowerPoint (2 decks)
python3 03-build/pptx/gen_c6plus_u1_docente.py                   # → C6plus_U1_docente/alumno.pptx
```
Enige single source: `u1_vocab.json` (woordenschat) + `U1_cocktail.md` (receta/reservoir-IDs).
