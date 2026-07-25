# 02-huisstijl — gedeeld designsysteem

Het **gedeelde** designsysteem voor alle vier de cursussen (C4·C5·C6·C6+) en alle vier de
formaten (Word · PDF · PPTX · HTML). Gouden regel: **variatie**.

## Inhoud

- **`tokens/tokens.json`** — de *single source of truth*: kleuren, fonts, type-schaal, vormen.
- **`tokens/tokens.css`** — dezelfde tokens als CSS-variabelen + `@font-face` (voor HTML-builds), incl. licht/donker.
- **`fonts/`** — de lettertypes (woff2, SIL OFL 1.1) + licentie. Lokaal opgeslagen → builds zijn reproduceerbaar en offline.
- **`richtlijnen/`** — de twee bindende ontwerpspecs (uitgeefsysteem + visuele woordenschat/grammatica).

## Beslist (2026-07-25)

- **Fonts — Richting 1 · modern & karaktervol:** koppen **Bricolage Grotesque**, tekst **Inter**, fictieve notities **Caveat**. Alle drie SIL OFL 1.1 → vrij in te bedden in Word/PPTX/PDF en zelf te hosten in HTML.
- **Kleurenpalet** goedgekeurd (zie stalenkaart): vier cursuskleuren als één familie + gedeelde warme neutralen.

## Twee kleurlagen (belangrijk)

1. **Cursuskleur** (`--accent`) = navigatie & huisstijl (unittab, kop/voet, labels, badges, voortgang). Zet per cursus met `.course-c5` enz. op een container.
2. **Functionele taalkleuren** (`--f-subject` … `--f-strategy`) = enkel binnen grammatica-/woordenschatmarkering. Vast over alle cursussen.

De twee lagen raken nooit hetzelfde element. Kleur is **nooit** de enige drager — altijd ook label, vorm of icoon.

## Gebruik (HTML)

```html
<link rel="stylesheet" href="/02-huisstijl/tokens/tokens.css">
<div class="course-c5"> … pagina met var(--accent) voor chrome … </div>
```

Nog te bouwen (bij de golden sample): de componentenbibliotheek en paginatemplates uit `richtlijnen/`.
