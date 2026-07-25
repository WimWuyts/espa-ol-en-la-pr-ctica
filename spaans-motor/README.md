# spaans-motor

Motor voor zelfbouwende oefenspellen (Spaans / NT2). Elk spel is één
zelfstandig, offline HTML-bestand — geen dependencies, geen server.

## Wat zit erin

```
src/
  tokens.css, shell.css        gedeelde stijl (azulejo)
  engine.js                    motorkern: score, streak, adaptief,
                               foutenlog, resultaten, geluid
  generators.js                nagerekende vormen (vervoeging, geslacht)
  data.es.js                   geverifieerde Spaanse dataset
  templates/
    classify.{js,css}          classificeren (persoon, ser/estar, geslacht…)
    match.{js,css}             koppelen (woordenschat, land↔nationaliteit…)
content/                       de "laagjes": één .json per spel
build.mjs                      lijmt motor + sjabloon + content → games/
games/                         gegenereerde spellen (build-uitvoer)
index.html                     menu naar alle spellen
SKILL.md                       Claude Code-skill: leerstof → spel
schema.md                      contentformaat
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

## Status (v1)

Werkend: motor, build, skill, sjablonen `classify` + `match` + `tetris`,
generatoren `conjugation` + `gender` + `verbo` (324 werkwoorden, presente
nagerekend en getest), acht voorbeeldspellen. Volgende sjablonen en generatoren
bouwen hierop voort.
