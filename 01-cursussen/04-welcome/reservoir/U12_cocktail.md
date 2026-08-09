# C4 · U12 — cocktail-receta

> **Thema:** El tiempo y estaciones
> **Gebouwd:** 2026-08-08 · met de gedeelde generatoren (`gen_c4_escena/kit/practica/hub/pdf.py`).

## Waarom deze unit anders gebouwd is

U1–U10 hangen aan een sitcom-aflevering: de video is de leidraad en het
transcript staat exact in de unit. Voor aflevering 11 tot 14 is er geen video en
geen transcript in de repo (`00-brondocumenten/videos-jaar4/` is leeg).
`HANDOVER_C4.md` voorziet die situatie — *«Zonder transcript: bouw native op de
kernwoordenschat»* — en dat is hier gebeurd: een eigen scène in
`escena_data.py`, ingesproken met de acht Castiliaanse stemmen.

Komt de aflevering er later alsnog, dan is dat één wijziging in `escena_data.py`;
de oefeningen, de print en de hub volgen vanzelf.

## Matrix A · uitspraak

| Klankfocus (nieuw) | Acentuación-laag | Werkvorm |
|---|---|---|
| **entonación (¡qué frío!)** | ¡! ¿? en de melodie | luister-en-herhaal + klap de klemtoon + dictee + hardop lezen met ✓/✗ van je buur |

## Matrix B · chunk-recycling

De chunks van deze unit staan in `escena_data.ESCENAS[12]["chunks"]` en komen
terug in vier oefeningen van de Práctica-tab (kaartjes → luisteren → matchen →
gaten) én in de caza-de-chunks op papier.

## Matrix C · funciones comunicativas

Nieuw in deze unit: **F24 · F25**. Zie `funciones_data.py` en
`C4_funciones_matrix.md`.

## Gramática

**hace · está · llueve** — visueel aangeboden (voorbeelden → patroon → valstrik), daarna een
klassieke cloze én een substitutieketen. Zie `kit_data.GRAMATICA[12]`.

## Quota

| Eis | Gehaald |
|---|---|
| ≥1 luisterfragment met script | ✓ scène (3 escenas) + het eigen fragment bij de leestekst |
| ≥1 rijke leestekst | ✓ `comprension_data.LECTURA[12]` |
| ≥2 opname-oefeningen | ✓ Grábate (Práctica) + de eindtaak |
| ≥1 traditionele cloze | ✓ `CLOZE[12]` in `gen_c4_pdf.py` |
| zelfcorrigerende oefeningen | ✓ 7 op de hub, van herkennen tot vrij produceren |
| foutenzoeker | ✓ `CORRIGE[12]` — fouten die een Nederlandstalige écht maakt |
| bladspiegel | ✓ 11 bladzijden, gemeten 89–91 % vulling |
