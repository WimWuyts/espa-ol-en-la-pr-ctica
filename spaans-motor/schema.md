# Contentschema

E�n pakket = één `.json` in `content/`. De build maakt er een zelfstandig
spel van in `games/`.

## Gemeenschappelijke velden

| Veld | Verplicht | Uitleg |
|---|---|---|
| `id` | ja | bestandsnaam van het spel (zonder `.html`) |
| `title` | ja | titel bovenaan (mag `<span>…</span>` voor accentkleur) |
| `subtitle` | nee | ondertitel |
| `lang` | ja bij generator | `"es"` (bepaalt welke dataset ingelijmd wordt) |
| `template` | ja | `"classify"` of `"match"` |
| `options` | nee | `{ "rounds": 20, "audio": false, "hint": true }` |

## Sjabloon `classify`

Stimulus verschijnt; speler kiest een categorie/persoon.

```json
{
  "template": "classify",
  "classify": {
    "prompt": "ser of estar?",
    "categories": [
      { "id": "ser",   "label": "ser",   "glaze": "#C4402C" },
      { "id": "estar", "label": "estar", "glaze": "#3D74D6" }
    ],
    "items": [
      { "stimulus": "Yo ___ profesor.", "answer": "ser", "tag": "ser", "sub": "beroep" }
    ]
  }
}
```

- `answer` mag een **array** zijn als meerdere categorieën juist zijn
  (bv. bij imperfecto is `yo` = `él`). De generator vult dit automatisch.
- `tag` bepaalt de adaptieve keuze en de balk per categorie in de resultaten.
- **Generatorvariant** (i.p.v. `items`):

```json
"generator": { "kind": "conjugation", "tense": "pres", "pool": "reg",
               "persons": ["yo","tu","el","nos","vos","ellos"] }
```
```json
"generator": { "kind": "gender", "trapsOnly": false }
```

`tense`: `pres | indef | imperf | perf | fut | cond | mix`.
`pool`: `reg | irr | all`.

## Sjabloon `match`

Twee kolommen; verbind elk paar.

```json
{
  "template": "match",
  "options": { "chunk": 6 },
  "match": {
    "prompt": "Verbind woord met vertaling",
    "pairs": [ { "a": "el padre", "b": "de vader" } ]
  }
}
```

`chunk` = aantal paren per scherm (default 6).

## Sjabloon `cloze`

Invulgat / meerkeuze. Elk item heeft ZIJN EIGEN opties (anders dan `classify`,
waar de categorieën vast zijn). `answer` = de juiste optiestring (of array).

```json
{
  "template": "cloze",
  "cloze": {
    "prompt": "¿Con tilde o sin tilde?",
    "items": [
      { "stimulus": "«Peru» (het land)", "options": ["Perú","Peru"], "answer": "Perú", "tag": "con-tilde", "sub": "aguda op vocaal" }
    ]
  }
}
```

- In `stimulus`: `___` wordt een gat-streep, `**x**` markeert een letter.
- `options` worden per beurt geschud; `tag` stuurt de balk per categorie.

## Sjabloon `tap`

Woord in tikbare stukken; tik het juiste stuk (sílaba tónica, letter met tilde).

```json
{
  "template": "tap",
  "tap": {
    "prompt": "Tik de sílaba tónica",
    "joiner": "·",
    "items": [ { "parts": ["ca","fé"], "answer": 1, "tag": "aguda", "sub": "café" } ]
  }
}
```

`answer` = 0-based index (of array van indices). `joiner` = scheidingsteken (default `·`).

## Sjabloon `order`

Zet tegels op volgorde (oplopend volgens `key`). Eén ronde = één setje.

```json
{
  "template": "order",
  "order": {
    "prompt": "Van klein naar groot",
    "rounds": [
      { "tag": "orden", "sub": "3 · 7 · 12", "items": [ {"label":"tres","key":3}, {"label":"siete","key":7}, {"label":"doce","key":12} ] }
    ]
  }
}
```

Juist = de hele ronde zonder misklik gelegd (één `judge` per ronde).

## Sjabloon `memory`

Geheugenspel (concentration): draai twee kaartjes om en zoek de paren.

```json
{
  "template": "memory",
  "options": { "pairs": 6 },
  "memory": { "prompt": "Zoek de paren", "pairs": [ { "a": "el país", "b": "het land" } ] }
}
```

`options.pairs` = aantal paren per bord (default 6 → 12 kaartjes).

## Sjabloon `type` (productief typen)

De leerling **typt** het antwoord (i.p.v. kiezen). Normalisatie is
accent-tolerant (á≈a, é≈e, …) mét behoud van **ñ** (año ≠ ano), en tolerant
voor hoofdletters/spaties/leestekens. Twee modi:

```json
{
  "template": "type",
  "options": { "rounds": 8 },
  "type": {
    "prompt": "Escribe en español",
    "mode": "closed",
    "accentSensitive": false,
    "items": [
      { "stimulus": "de vader", "answers": ["el padre","padre"], "tag": "familia", "hint": "e_ p____" }
    ]
  }
}
```

- **`mode":"closed"`** (goud): `answer` (string) of `answers` (array) = aanvaarde
  oplossingen → auto-check. Bij fout wordt het modelantwoord getoond.
- **`mode":"open"`** (halfopen): vrije mini-zin → **structuurcheck** via `must`
  (array verplichte tokens) + knop **«Ver modelo»** (`model`) ter zelfcorrectie.
- `stimulus`: `___` = gat-streep, `**x**` = markering. `hint` = optionele letterhint.
- Een accentbalk (á é í ó ú ñ ü ¿ ¡) staat onder het invoerveld (mobiel/AZERTY).

## Arcade-skins `tetris` · `belt` · `mole` · `bubble` · `snake`

**Zelfde judge-logica als `classify`, andere «jas».** Ze consumeren een
**identiek `classify`-blok** (`categories` + `items`, of een generator) — je kan
elk classify-pakket omzetten door enkel `template` te wisselen.

| skin | mechaniek | interactie |
|---|---|---|
| `tetris` | vallende tegel → juiste kolom | tik kolom / ← → + spatie / 1-9 |
| `belt` | sorteerband → juiste bak vóór hij afvalt | tik bak / ← → + spatie / 1-9 |
| `mole` | mollenmeppen → mep het juiste hol (tijdbalk) | tik hol / 1-9 |
| `bubble` | bubbelschieter → schiet naar juiste bubbel | tik bubbel / 1-9 |
| `snake` | stuur de slang naar de juiste voedseltegel | pijltjes · WASD · vegen |

```json
{
  "template": "belt",
  "options": { "rounds": 12 },
  "classify": {
    "prompt": "¿el o la?",
    "categories": [ { "id":"el","label":"el","glaze":"#3D74D6" }, { "id":"la","label":"la","glaze":"#C4402C" } ],
    "items": [ { "stimulus":"casa", "answer":"la", "tag":"la", "sub":"-a" } ]
  }
}
```

**Rotatie (plan §3):** laat het arcade-slot (M1) per unit roteren over deze skins
zodat geen enkele mechaniek zich binnen één cursus opdringt.

## Een spel toevoegen

1. Zet een `.json` in `content/`.
2. `node build.mjs`.
3. `games/<id>.html` is klaar; `index.html` linkt het automatisch.
