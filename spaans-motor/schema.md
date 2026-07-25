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

## Een spel toevoegen

1. Zet een `.json` in `content/`.
2. `node build.mjs`.
3. `games/<id>.html` is klaar; `index.html` linkt het automatisch.
