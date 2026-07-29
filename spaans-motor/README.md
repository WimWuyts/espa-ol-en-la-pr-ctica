# spaans-motor

Motor voor zelfbouwende oefenspellen (Spaans / NT2). Elk spel is één
zelfstandig, offline HTML-bestand — geen dependencies, geen server.

## Waar komen de spellen? — de keten in één blik

Elk spel bestaat op **drie plaatsen**, elk met een andere taak. Dat is bewust:
het recept is *bewerkbaar*, het losse spel is *portabel*, de hub is *leverbaar
aan de leerling*.

```
1 · RECEPT      spaans-motor/content/es-u3-hay-esta.json
                de items, de categorieën, en één regel `template` die de jas kiest
                (classify · type · mole …). Hier zit al het denkwerk.
                        │
                        │  node build.mjs      (lijmt engine + template + recept)
                        ▼
2 · LOS SPEL    spaans-motor/games/es-u3-hay-esta.html
                één standalone offline bestand: geen internet, geen bijbestanden.
                Los te openen, door te sturen, of ergens in te sluiten.
                        │
                        │  03-build/web/gen_u3_web.py   (bakt ze base64 in de hub)
                        ▼
3 · IN DE HUB   03-build/web/U3_web.html
                de unit-hub met de spellen fysiek erín (~1,3 MB), die ze in een
                modal-iframe opent. Dít is wat de leerling gebruikt.
                        ▲
                        │  QR-code in de print-PDF verwijst hierheen
                        │  (cosmetisch tot de hosting-sweep, CLAUDE.md §18)
```

**Twee menu's — niet verwarren:**

| Bestand | Wat het is | Voor wie |
|---|---|---|
| `spaans-motor/index.html` | menu met **álle** spellen door elkaar + «Mi progreso»-dashboard | de leerkracht, om te testen |
| `03-build/web/U<N>_web.html` | de unit-hub, met **enkel de spellen van die unit** | de leerling |

De leerling ziet die grote lijst dus nooit; die krijgt per unit zijn eigen set.

**Gevolg voor onderhoud:** wijzig je een spel, dan raakt dat **drie plaatsen** —
het recept (of het `make_<unit>_games.py`-script dat het genereert) → `node
build.mjs` → de hub-generator opnieuw draaien. Vandaar dat een skin-wissel of
een nieuw spel altijd die hele keten doorloopt. Zie ook `catalogos/` (inventaris
van wat er nu bestaat) en `PLAN_MOTOR_C4_C6_C6plus.md` (wat er nog moet komen).

## Wat zit erin

```
src/
  tokens.css, shell.css        gedeelde stijl (azulejo)
  engine.js                    motorkern: score, streak, adaptief,
                               foutenlog, resultaten, geluid, confidence-betting
  features.js/.css             meta-laag: Leitner, streak-kalender, heatmap,
                               can-do-zelfscan (voortgang in localStorage)
  generators.js                nagerekende vormen (vervoeging, geslacht)
  data.es.js                   geverifieerde Spaanse dataset
  templates/                   13 sjablonen — zie schema.md:
    classify · cloze · match · memory · order · point · tap    receptief → half
    type                       PRODUCTIEF typen (normalisatie, open/closed)
    speak                      PRODUCTIEF spreken (opname, shadowing, carrousel)
    sim                        open productie / mini-simulatie
    tetris · belt · mole · bubble · snake · platform · tower · pinball
                               8 arcade-skins op dezelfde classify-judge
content/                       de "recepten": één .json per spel
build.mjs                      lijmt motor + sjabloon + content → games/
games/                         gegenereerde spellen (build-uitvoer)
index.html                     menu naar alle spellen + voortgangsdashboard
catalogos/                     inventaris ES + voorstel-lijsten NT2/Engels
SKILL.md                       Claude Code-skill: leerstof → spel
schema.md                      contentformaat (alle sjablonen + features)
PLAN_MOTOR_C4_C6_C6plus.md     bouwplan: 16-slot-grid, arcade-rotatie, retrofit
```

## Bouwen

```bash
node build.mjs
```

Leest elk pakket in `content/`, schrijft `games/<id>.html` en werkt
`index.html` bij. Enkel Node nodig; geen npm-install, geen netwerk. Draait
dus ook in Claude Code web zonder internettoegang.

## Een spel maken

Twee manieren:

- **Handmatig:** zet een `.json` in `content/` (zie `schema.md`) → `node build.mjs`.
- **Via Claude Code:** upload je lesbestand en vraag *"maak hier het adequate
  oefenspel van"*. De skill (`SKILL.md`) kiest het sjabloon, stelt de content
  samen, controleert ze, en bouwt.

## Afleveren

- **Smartboard / delen:** open `games/<id>.html` rechtstreeks, of stuur het bestand door.
- **GitHub Pages:** zet Pages aan op deze repo. Elk spel is dan een URL:
  `https://<gebruiker>.github.io/<repo>/games/<id>.html`, en het menu staat op
  `.../index.html`. Voor leerlingen: die menu-link in Smartschool of een QR.

## Uitbreiden

De motor is taal-onafhankelijk: hetzelfde `classify`-sjabloon draait
`vervoeging→persoon` (ES) en `de/het` (NT2). Nieuwe sjablonen (`cloze`,
`order`, `point`) pluggen in via `src/templates/` + een regel in `build.mjs`;
ze gebruiken dezelfde motor-API (`api.judge`, `api.next`, `api.finish`).

## Status

**Motor-infrastructuur: compleet.** 13 sjablonen (incl. de productieve `type`- en
`speak`-laag en 8 arcade-skins), confidence-betting, en de meta-laag (Leitner ·
streak · heatmap · can-do). Generatoren `conjugation` + `gender` + `verbo`
(324 werkwoorden, presente nagerekend en getest).

**Content:** 309 gebouwde spellen — C5 (U0–U8) en C6+ (U0–U7), plus generieke
tools en 10 demo's die elke mechaniek tonen (`content/es-demo-*`).

**Nog te doen** (zie `PLAN_MOTOR_C4_C6_C6plus.md`): de arcade-rotatie voor C5/C6+
(§6bis — daar is `tetris` nu nog de enige arcade-vorm), de klassikale set, en de
per-unit 16-slot-content voor C4 en C6.
