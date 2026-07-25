---
name: oefenspel-bouwer
description: >
  Zet leerstof (een geüpload lesbestand, een woordenlijst, of een korte
  omschrijving) om in een speelbaar, offline oefenspel via de spaans-motor.
  Gebruik deze skill wanneer de gebruiker vraagt om "een oefenspel", "een
  spel van deze les", "iets om dit in te oefenen", of een contentpakket voor
  de motor. Werkt voor Spaans en NT2.
---

# Oefenspel-bouwer

Deze skill routeert leerstof naar het juiste sjabloon van de motor, stelt een
contentpakket samen, controleert het, en bouwt een zelfstandig spel.

## Werkwijze (stille modus)

Minimale narratie, directe uitvoering. Toon één keer je keuze van sjabloon en
laat de gebruiker met één woord bijsturen. Geen lange uitleg.

## Pijplijn

1. **Lezen.** Verwerk het lesbestand / de lijst / de omschrijving. Haal de
   leerstof en de doelwoorden of doelvormen eruit.
2. **Type herkennen** → kies sjabloon via de routeringstabel hieronder. Bij
   twijfel tussen twee: kies er één, meld ze, en vraag niet verder.
3. **Content samenstellen.**
   - **Grammatica met een generator** (vervoeging, geslacht): gebruik
     `"generator": { ... }`. De vormen komen dan uit de nagerekende motor —
     NOOIT zelf vervoegen of geslachten verzinnen.
   - **Vaste items / woordenschat**: schrijf `items` of `pairs` uit.
4. **Blokkerende controle** (zie onder). Faalt er één → niet bouwen, meld wat.
5. **Schrijven** naar `content/<id>.json` en **`node build.mjs`** draaien.
   Resultaat: `games/<id>.html` + bijgewerkte `index.html`.

## Routeringstabel (leerstof-signaal → sjabloon)

| Leerstof | Sjabloon | Bron |
|---|---|---|
| werkwoord vervoegen (welke persoon/tijd) | `classify` | generator `conjugation` |
| geslacht / el-la | `classify` / `tetris` | generator `gender` |
| werkwoord: welke presente-klasse (regular / cambio vocálico / onregelmatig) | `classify` / `tetris` | generator `verbo` (mode `clase`) |
| werkwoord: cambio vocálico & onregelmatig inoefenen | `tetris` | generator `verbo` (mode `person`, `classes`) |
| keuze tussen 2–3 opties (ser/estar, por/para, pretérito/imperfecto, b/v, tilde…) | `classify` | vaste `items` |
| woordenschat, vertalingen, land↔nationaliteit, synoniemen | `match` | vaste `pairs` |

Sjablonen die nog niet bestaan (`cloze`, `order`, `point`): nog niet
aanbieden; kies het dichtstbijzijnde bestaande of meld dat het sjabloon
ontbreekt.

## Blokkerende controles (spel wordt NIET gebouwd als één faalt)

1. **Geverifieerde vormen.** Elke grammaticale vorm komt uit een generator.
   Staat er een handgeschreven vervoeging of geslacht in `items`, controleer
   die tegen de generator of weiger.
2. **Uniciteit.** Geen dubbele doelwoorden of dubbele `pairs`-linkerzijden
   binnen één pakket. (Dubbele stimulus = dubbelzinnige oefening.)
3. **Geen valse afleider.** Bij `classify` met vaste `items`: het opgegeven
   `answer` moet de enige juiste categorie zijn, tenzij bewust meerdere juist
   zijn (dan `answer` als array). Nooit een afleider die óók klopt.
4. **Volledigheid.** Elk item heeft `stimulus` + `answer` (+ `tag`); elk paar
   heeft `a` + `b`. Elke `answer`/`tag` verwijst naar een bestaande categorie.

## Naamgeving

`<taal>-<onderwerp>[-<niveau>].json`, kleine letters, koppeltekens.
Voorbeelden: `es-presente-regular.json`, `es-ser-estar.json`,
`nt2-de-het-a1.json`.

## Contentschema

Zie `schema.md` voor het volledige formaat en meer voorbeelden.
