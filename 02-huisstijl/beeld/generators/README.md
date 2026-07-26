# Beeld-generatoren (flat-vector, huisstijl)

Alle beeld in de cursus wordt **in code getekend** (geen externe AI-tool nodig).

- `cast_gen.py` — cast (Lucía·Diego·Valen·Nina·Tú) + mochila-mascotte (busten, avatars, poses).
- `build_svgs.py` — schematische grammatica-diagrammen (SílabaStrip, TresFamilias, DosMontones, beslisboom, drie-lagen, SummaryQuadrant, routemap, La-Ruta-stickers).
- `assets2.py` — composite illustraties (quote-strip, café-sombrero, poster, chat, bingo, profielen, telkaarten, vocab-opener).
- `build_map.py` — **echte wereldkaart** uit Natural Earth (public domain, `ne_110m_admin_0_countries.geojson`), equirectangular, Spaanstalige landen opgelicht + paradas met cast.

Render: functies geven SVG-strings terug → in HTML (web) of via Chromium → 300 dpi PNG (print).
