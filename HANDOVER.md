# HANDOVER — stand van zaken & volgende stappen

> Vluchtige status (verandert vaak). De **duurzame** afspraken staan in `CLAUDE.md`.
> **Nieuwe sessie? Doe dit:** (1) `bash scripts/setup-build.sh` · (2) lees `CLAUDE.md` · (3) lees dit bestand · (4) ga verder.

## Waar we staan (2026-07-26)
- **Golden sample = C5 · Unidad 0 «¡Empezamos!»**. Layout/toon **goedgekeurd** door de auteur.
- **Bron (single source):** `01-cursussen/05-a1/U0/U0_bron.md` (±2100 regels, compleet).
- **Print-sjabloon (VAST):** `02-huisstijl/templates/cursus-print.css` — herbruikbare componentenkit + print-hygiëne (veilige `@page`-marges, hero-bleed p1, doorvloeiende tabellen, weesregel). Zie `CLAUDE.md` §18.
- **Gebouwd & gerenderd (PDF):** `01-cursussen/05-a1/U0/U0.html` bevat **opener + §1.1 + §1.2** in de huisstijl (Chromium → PDF werkt; fonts renderen).
- **In uitvoering:** een background-workflow bouwde de resterende secties als HTML-fragmenten in `01-cursussen/05-a1/U0/_html/` (§1.3 · §2 · §3 · §4 · Cultura · Tarea · Repaso · §V). *Check of die er staan; zo niet, herbouw ze — de inputs (U0_bron.md, U0.html, cursus-print.css) staan in de repo.*

## Volgende stappen (in volgorde)
1. **U0-PDF afmaken:** de fragmenten uit `_html/` integreren in `U0.html` (invoegen vóór `</body>`, ná §1.2), renderen met Chromium → **volledige U0-PDF**, visueel controleren (bladspiegel: geen halflege pagina's, weesregel, veilige marges).
2. **PowerPoint** U0: docent `.pptx` + leerling `.ppsx` via `python-pptx`, uit dezelfde bron, huisstijl + avatars (spec: `02-huisstijl/richtlijnen/INTERACTIEVE_POWERPOINT_50_IDEEEN.md`).
3. **HTML-versie** U0: 4 tabbladen, flip cards (ES↔NL) voor álle woorden, spellen met de **motor** (`spaans-motor/` — eerst templates uitbreiden, zie `spaans-motor/PLAN_100_SPELVORMEN.md`), tab «Extra» (profedeele-YouTube + arche-ele-genially; auteur levert links).
4. **AI-assets inwisselen:** auteur zet personages (Estilo Exploración) + 2 scènes in de Drive-map (<https://drive.google.com/drive/folders/1RCPLRj6xukL7f7FYugV6KkAxWtkeBMoE>); placeholders vervangen. Audio: TTS → later eigen opnames.
5. **Opschalen:** zelfde proces voor alle units van C5 (jaar 5) en C6/C6+ (jaar 6).

## Render-omgeving (verse container telkens opnieuw)
- `bash scripts/setup-build.sh` installeert python-libs (python-docx, python-pptx, pymupdf, fonttools, brotli) + de huisstijl-fonts in `~/.fonts`.
- Chromium staat in `/opt/pw-browsers/chromium-*/chrome-linux/chrome`.
- **LibreOffice conversie is stuk in de sandbox** → PDF komt via Chromium (`--print-to-pdf`), niet via Word.

## Werkbranch
`claude/spanish-course-development-jx25ay` — commit klein & beschrijvend (NL), push regelmatig.
