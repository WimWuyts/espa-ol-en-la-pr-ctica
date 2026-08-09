# C4 · U11 — cocktail-receta

> **Thema:** El tiempo · las vacaciones · lo que me gusta
> **Aflevering:** «Aquí hace demasiado calor» (2 escenas, 33 regels)
> **Gebouwd:** 2026-08-08 · **op het echte transcript gezet:** 2026-08-09
> Gedeelde generatoren: `gen_c4_escena/kit/practica/hub/pdf.py`.

## Waarom deze unit anders gebouwd is

U1–U10 hebben elk hun eigen generator, gebouwd op hun sitcom-aflevering. U11–U14
zijn in één keer gemaakt en delen er daarom één: de inhoud staat in
`escena_data.py` en `kit_data.py`, de vorm in de generatoren. Vier bijna
identieke kopieën zouden vier plaatsen opleveren waar een verbetering apart moet.

Deze vier hebben een tijdlang op eigen materiaal gedraaid, omdat de transcripten
er nog niet waren (`HANDOVER_C4.md`: *«zonder transcript: bouw native op de
kernwoordenschat»*). Op 2026-08-09 leverde de auteur ze alle vier en is de unit
op de échte aflevering gezet. Dat veranderde bij alle vier ook het thema: de
oorspronkelijke themalijst voorzag hier iets anders dan er in beeld gezegd wordt,
en in C4 is de vídeo de leidraad (CLAUDE.md §3).

De video zelf is de opname — met echte acteurs. Er wordt daarom géén eigen
scène meer ingesproken; het enige gesynthetiseerde fragment van deze unit is dat
bij de leestekst.

## Matrix A · uitspraak

| Klankfocus | Acentuación-laag | Werkvorm |
|---|---|---|
| **s (siempre sorda)** | klemtoon in de seizoenen | luister-en-herhaal + klap de klemtoon + dictee + hardop lezen met ✓/✗ van je buur |

De klankfocus ligt vast in matrix A en is niet mee veranderd met het thema —
alleen de voorbeeldwoorden komen nu uit de nieuwe scène. Zo blijft elke klank
precies één keer aan de beurt over de veertien units.

## Matrix B · chunk-recycling

16 chunks in `escena_data.ESCENAS[11]["chunks"]`, 42 woorden in zes
clusters in `kit_data.CLUSTERS[11]`. Ze keren terug in vier oefeningen van de
Práctica-tab (kaartjes → luisteren → matchen → gaten), in de caza-de-chunks op
papier en in de eindtaak.

## Matrix C · funciones comunicativas

Nieuw in deze unit: **F24 · F25 · F27 · F28**. Kreeg er een niveau bij: **—**.
Zie `funciones_data.py` en `C4_funciones_matrix.md`.

## Gramática

**me gusta · te gusta · le gusta** — wie iets graag doet, en hoe vaak. Visueel aangeboden (voorbeelden → patroon → valstrik),
daarna een klassieke cloze én een substitutieketen. Zie `kit_data.GRAMATICA[11]`.

## Quota

| Eis | Gehaald |
|---|---|
| ≥1 luisterfragment met script | ✓ de aflevering (33 regels, meelees-laag) + het ingesproken fragment bij de leestekst |
| ≥1 rijke leestekst | ✓ `comprension_data.LECTURA[11]` |
| ≥2 opname-oefeningen | ✓ Grábate (Práctica) + de eindtaak |
| ≥1 traditionele cloze | ✓ `CLOZE[11]` in `gen_c4_pdf.py` |
| zelfcorrigerende oefeningen | ✓ 7 op de hub, van herkennen tot vrij produceren |
| foutenzoeker | ✓ `CORRIGE[11]` — fouten die een Nederlandstalige écht maakt |
| bladspiegel | ✓ 12 bladzijden, gemeten 92 % vulling, geen halflege bladzijde |
