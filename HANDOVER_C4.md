# HANDOVER C4 «Bienvenidos al español» — productiehandboek (U1 gelockt)

> **Lees dit vóór je een C4-unit bouwt.** U1 «Presentaciones» is de **goedgekeurde golden sample**.
> Bouw U2–U14 met **exact dezelfde parameters/pijplijn**. Dit document is zelfstandig: alles wat je
> nodig hebt staat hier of in de verwezen bestanden. Projectgeheugen = `CLAUDE.md` (automatisch ingeladen).

---

## 0 · De cursus in één alinea

C4 (4 Moderne talen, 2de graad, 1 u/week) = een **voorafgaande, praktische** cursus «Survival in
Spanish», **buiten leerplan**, videogedreven (Hablamétodo-sitcom). **14 thema's × 2 lesuren.** Doel:
leerlingen **praktisch Spaans laten gebruiken** en een **voorsprong in de mechaniek** geven (uitspraak,
chunks, luisteren) **zónder de leerplaninhoud van C5 op te gebruiken**. Kleur = **rood**. Rode draad =
La Ruta, etappe **«El despegue»**; U1 = parada 1.

**Kernspanning (bindend):** grammatica **enkel functioneel** (herkennen/vaste vormen), **géén** systeem
(vervoeging als paradigma, verleden/futuro/condicional/subjuntivo → dat is C5/C6). Zie
`01-cursussen/04-welcome/C4_LEERDOELEN_EVALUATIE.md`.

---

## 1 · Repo-locaties (alles voor C4)

```
CLAUDE.md                                             ← projectgeheugen (§3 C4, §10 lock, §13/§14 bladspiegel)
HANDOVER_C4.md                                        ← dit document
01-cursussen/04-welcome/
    C4_LEERDOELEN_EVALUATIE.md                        ← can-do's + doelcodes + toetsmatrix + rubrics + 14-thema-tabel
    reservoir/
        C4_coverage.md                                ← dekkings-grootboek + UITSPRAAK-MATRIX A + CHUNK-RECYCLING B
        C4_reservoir_index.md                         ← de plukvijver (C4-filter) + 7 spreidingsregels
        C4_cocktail_TEMPLATE.md                       ← per-unit receptuur (kopie → U<N>_cocktail.md)
        U1_cocktail.md                                ← gewerkt voorbeeld (welke reservoir-IDs U1 gebruikt)
02-huisstijl/
    fonts/*.woff2                                     ← Bricolage Grotesque (700/800) · Inter (400/600) · Caveat (700)
    tokens/tokens.json · tokens.css                   ← huisstijl-tokens
    templates/cursus-print.css                        ← BINDENDE print-kit (C4 = --g/--gd/--gt overrulen)
03-build/web/
    gen_c4u1_escucha.py   → componentes/C4_U1_escucha.html   (video + meelees-transcript)
    gen_c4u1_kgt.py       → componentes/C4_U1_kgt.html       (Suena bien + Kit + Gramática + Tarea)
    gen_c4u1_practica.py  → componentes/C4_U1_practica.html  (zelfcorrigerende oefeningen)
    gen_c4_musica.py      → componentes/C4_musica.html       (banda sonora, herbruikbaar; TEMA-var per unit)
    gen_c4u1_hub.py       → componentes/C4_U1_hub.html       (HTML-hub met tabbladen, srcdoc-iframes)
    gen_c4u1_pdf.py       → print/C4_U1.html (+ editbar) → print/C4_U1.pdf
    gen_c4_leerdoelen_pdf.py → print/C4_Leerdoelen_Evaluatie.pdf
03-build/pptx/
    gen_c4u1_ppt.py       → C4_U1_docente.pptx + C4_U1_alumno.ppsx   (2 decks, geanimeerd)
    gen_u0_docente.py     ← BRON-machinerie (helpers/timing/chrome) waaruit gen_c4u1_ppt is samengesteld
    render_avatars.py · assets/*.png                 ← cast-avatars (mochila/tu…)
03-build/word/
    gen_c4u1_docx.js      → C4_U1.docx                (docx-js; zie §7 kanttekening)
```

---

## 2 · De 4 formaten & pijplijn (één bron → 4 outputs)

| Formaat | Generator | Render | Opmerking |
|---|---|---|---|
| **HTML-hub** | `gen_c4u1_hub.py` (bundelt de 4 componenten in `srcdoc`-iframes, tabbladen) | — (standalone, offline) | fonts base64-embed; `allow`-permissies op `.frame` voor de video |
| **PDF (print)** | `gen_c4u1_pdf.py` (HTML-bron met print-CSS + editbar) | Chromium `--headless --print-to-pdf` | **primeair print-formaat**; bevat bewerkbare `U<N>.html`-laag |
| **PowerPoint** | `gen_c4u1_ppt.py` (python-pptx + `<p:timing>`) | — | docente `.pptx` + alumno `.ppsx`; «Repareren»-dialoog aanvaard |
| **Word (optioneel)** | `gen_c4u1_docx.js` (docx-js) | LibreOffice **werkt niet in sandbox** | bouwbaar + XSD-valide, maar niet te renderen → PDF primeert |

**Render-commando's (werken in deze sandbox):**
```bash
# HTML-componenten + hub
python3 03-build/web/gen_c4u2_escucha.py && python3 03-build/web/gen_c4u2_kgt.py \
 && python3 03-build/web/gen_c4u2_practica.py && python3 03-build/web/gen_c4_musica.py \
 && python3 03-build/web/gen_c4u2_hub.py
# PDF
python3 03-build/web/gen_c4u2_pdf.py
/opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless --no-sandbox --disable-gpu \
  --no-pdf-header-footer --print-to-pdf=03-build/web/print/C4_U2.pdf 03-build/web/print/C4_U2.html
# PowerPoint (2 decks)
cd 03-build/pptx && python3 gen_c4u2_ppt.py
```
Deps die je (eenmalig) installeert: `pip install segno markdown` · `npm install docx` (in `03-build/word/`).
Fonts: base64-inbedden via de `face()`-helper (staat in elke generator).

---

## 3 · Bindende C4-regels (elke unit)

1. **Vaste sectiestructuur** (zoals U1): §1 **Escucha** (video + meelees-transcript) → **Suena bien**
   (uitspraak) → §2 **Kit de supervivencia** (woordenschat visueel, per taalhandeling) → §4 **Gramática
   en la práctica** (functioneel, géén kader) → §3 **Práctica** (receptief→productief, zelfcorrigerend)
   → §5 **Tarea final** (communicatief) → **Cultura · Banda sonora** → **Repaso** (spiekkaart + semáforo).
2. **Kleur = C4-rood:** `--g:#D64550 · --gd:#A8323B · --gt:#FBEAEC`. Functionele taalsemantiek (blauw=persoon,
   oranje=werkwoord…) blijft zoals §13. Print: overschrijf enkel `--g/--gd/--gt` in `cursus-print.css`.
3. **Español-eerst + NL-steun** overal (ook verteltekst, ¡Ojo!, grammatica).
4. **BLADSPIEGEL (BINDEND):** elke hoofdsectie op nieuwe pagina **én** verrijkt tot **volle pagina**
   (85–99 % vulling; nooit 30–50 %). **Meet elke print-unit** met het meet-script (§6) vóór levering.
   Verrijken = échte inhoud (extra oefening met antwoordruimte, model-dialoog, noticing, cognaten-warm-up,
   luistertaak, mini-auto-test…), nooit opvulling.
5. **Antwoordruimte** (§14): elke oefening krijgt type-correcte schrijfruimte; **nooit oplossingen op de
   leerlingpagina** (die horen in de HTML-zelfcorrectie + docent-notities).
6. **Uitspraak = matrix A** (`C4_coverage.md`): één klankfocus + acentuación-laag per unit, telkens een
   **andere** werkvorm. **U2 = j/g (jota) + h muda.** Put uit SK-080/086/087/088 · PPT-037/038 · DS-009.
7. **Chunk-recycling = matrix B:** breng ≥2 eerdere functies terug, in een **andere** werkvorm dan de intro.
   (Vanaf U2 actief; U1 was de intro-laag.)
8. **Reservoir/variatie:** kies **nog niet-gebruikte** IDs (zie `C4_coverage.md`), geen werkvorm 2× «met
   dezelfde jas», ≥6 verschillende motor-speltypes. Grammatica enkel **✓/~**-items (functioneel).
9. **Video:** YouTube-embed (`youtube-nocookie.com/embed/<id>?rel=0&playsinline=1`) met
   `allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; fullscreen; web-share"`
   + `allowfullscreen`; dezelfde `allow` op de hub-`.frame`-iframe; **zichtbare fallback-link** «Op YouTube».
   **In de PowerPoint (BINDEND, auteur 2026-07-27):** de video zit als **echte, afspeelbare
   online-video** op de Escucha-dia (speelt ín PowerPoint desktop 2016+/365, internet vereist).
   Techniek: helper `add_online_video()` in `gen_c4u<N>_ppt.py` — poster (PIL-render, C4-rood +
   play-knop) via `add_picture`, dan `<a:videoFile r:link>` (extern, `.../relationships/video`) +
   `<p14:media r:embed>` (extern, `.../2007/relationships/media`), beide naar
   `youtube.com/embed/<id>`, + `<a:hlinkClick action="ppaction://media">`. Zet per unit
   `VIDEO_ID/VIDEO_TOP/VIDEO_MAIN`. **Bij het klonen van de generator gaat dit automatisch mee** —
   niet verwijderen. (LibreOffice kan pptx-video niet renderen in de sandbox; verifieer via
   round-trip + rels: `videoFile`/`p14:media` aanwezig, embed-URL klopt, thema blijft rood.)
10. **Geen bouw-jargon/metaberichten** op de leerlingpagina (Engelse componentnamen, «native/component/rood»,
    build-notities → enkel in broncode/docentdossier).
11. **Doelcodes** uit `C4_LEERDOELEN_EVALUATIE.md` op de **docentenpagina** van elke unit (niet leerling).
12. **QR's op print → naar de HTML-hub** (juist ankerpunt), niet rechtstreeks YouTube/PPTX.
13. **Funciones-comunicativas-laag (BINDEND, auteur 2026-07-27 — matrix C):** elke unit bouwt de
    **doorlopende functie-ruggengraat** verder uit, vertrekkend uit het fragment. Werkwijze: in
    `03-build/web/funciones_data.py` een nieuwe `exp[<unit>]` bij een bestaande functie zetten
    (= *uptrade/nivel+*) of een nieuwe functie toevoegen (`exp[<intro-unit>]`), plus
    `NOTICING[<unit>]` (cita→función uit de scène) en `TAREA_FUN[<unit>]`. De laag komt **automatisch**
    in de 3 formaten: hub-tab «🗣️ Funciones» (`gen_c4_funciones.py`), print-sectie tussen Música en
    Repaso (`funciones_print.py`, bladspiegel 85–99 %), en de PPT-dia `s_funciones()`. Werk daarna
    `01-cursussen/04-welcome/reservoir/C4_funciones_matrix.md` bij. Leerlingpagina toont función +
    exponentes + CEFR-chip; **doelcodes enkel in matrix C (docentdossier)**.
14. **Lees- & luisterlaag «Lee y escucha» (BINDEND, auteur 2026-07-28):** elke unit krijgt een
    korte **leestekst** (begripsladder globaal→detalle→transfer) + een **2e luisterfragment**
    (script, TTS-play) die de functies recyclen. Genereer met de NotebookLM-prompts in
    `00-brondocumenten/prompts/C4_comprension_prompts.md` (vast format) en plak de output in
    `03-build/web/comprension_data.py` onder `LECTURA[<unit>]`/`AUDIO[<unit>]`. De laag verschijnt
    dan automatisch: hub-tab «📖 Lee y escucha» (`gen_c4_comprension.py`) + print-sectie na Escucha
    (`comprension_print.py`, alleen als er data is; bladspiegel 85–99 %). Kies per unit een **andere
    tekstsoort** (variatie). U1 = ingevulde demo; U2/U3 wachten op je NotebookLM-output.

---

## 4 · De per-unit workflow (stap voor stap)

1. **Auteur levert aan:** (a) de **video** (YouTube-link of Drive-id), (b) het **transcript** (scènes),
   (c) de **centrale taalhandelingen** van de video. *(Zonder transcript: bouw native op de kernwoordenschat.)*
2. **Cocktail invullen:** kopieer `C4_cocktail_TEMPLATE.md` → `U<N>_cocktail.md`. Kies reservoir-IDs
   (nieuwe t.o.v. `C4_coverage.md`), vul **matrix A** (klankfocus van deze unit) en **matrix B**
   (welke chunks terugkeren) in. Vink de quota-check.
3. **Generatoren maken:** kopieer de `gen_c4u1_*`-scripts → `gen_c4u2_*`, vervang **inhoud + unitnummer +
   parada + banda sonora (`TEMA`)**; pijplijn/CSS/helpers **ongewijzigd**.
4. **Bouwen** (zie commando's §2): componenten → hub → PDF → PPTX.
5. **Bladspiegel meten** (§6) → verrijk dunne secties tot 85–99 %. **Herhaal tot alle secties vol.**
6. **QA:** screenshot de hub-tabs + PDF-secties (Chromium `--screenshot`), dump PPTX-titels (python-pptx).
7. **Meta-jargon check** (grep op leerlingpagina's). **Doelcodes** op docentenpagina.
8. **Coverage bijwerken** (`C4_coverage.md`: U-kolom + samenvatting) na de build.
9. **Committen** (branch `claude/spanish-course-development-jx25ay`, Nederlandse boodschap) + **leveren**.

---

## 5 · Toolchain-kanttekeningen (belangrijk)

- **Chromium** (render/QA/screenshot): `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`
  (`--headless --no-sandbox --disable-gpu`). Gebruik **absolute paden** (cwd kan verspringen).
- **LibreOffice/soffice = defect in de sandbox**: kan géén `.docx`/`.pptx` laden → PPTX enkel via
  **python-pptx round-trip + XML-structuur** verifiëren; Word niet renderbaar → **PDF is het print-formaat**.
- **QR** = `segno` (SVG inline, `dark="#A8323B"`), placeholder-URL `HUB_URL` → auteur vervangt door de
  gehoste hub-URL.
- **Audio** = browser-TTS (`SpeechSynthesis`, `es-ES`).
- **Fonts** = base64-inbedden (woff2) in HTML; python-pptx/docx-js embedden niet → font-namen zetten.

---

## 6 · Bladspiegel-meet-script (verplicht vóór levering)

Meet de vulling van elke sectiepagina (streef 85–99 %, geen 30–50 %):
```bash
python3 - <<'PY'
h=open("03-build/web/print/C4_U2.html",encoding="utf-8").read()
js='''<div id="R"></div><script>window.addEventListener("load",function(){var P=(297-24)/25.4*96,F=(297-12)/25.4*96,o=[],i=0;
document.querySelectorAll(".hero,.sec").forEach(function(e){var h=e.getBoundingClientRect().height,p=(i==0?F:P),pg=h/p,l=pg<=1?h/p:(pg-Math.floor(pg));var t=(e.querySelector("h1,h2")||{}).textContent||"hero";o.push((i+1)+". "+t.slice(0,22)+" "+Math.round(h/96*25.4)+"mm "+pg.toFixed(2)+"p last "+Math.round(l*100)+"%");i++;});
document.getElementById("R").textContent=o.join("\\n");});</script>'''
open("/tmp/measure.html","w",encoding="utf-8").write(h.replace("</body>",js+"</body>"))
PY
/opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless --no-sandbox --disable-gpu \
  --virtual-time-budget=4000 --window-size=794,1123 --dump-dom /tmp/measure.html \
  | python3 -c "import sys,re;m=re.search(r'id=.R.>(.*?)</div>',sys.stdin.read(),re.S);print(m.group(1) if m else '?')"
```
Regel: `p` (aantal pagina's) net boven 1.0 met lage `last %` = **halflege 2de pagina → trimmen of tot
volle 2 pagina's verrijken.** Elke sectie op 1.0 (85–99 %) of nette 2.0.

---

## 7 · U2 concreet — «Saludos y cortesía» (parada 2)

- **Parada/cultuur:** begroetingen door de dag (buenos días/tardes/noches), beleefdheid, afscheid; kies een
  cultuurhoek (bv. saludos & besos in de Spaanstalige wereld) + banda sonora (`TEMA="saludos"` → Rosalía «La Perla» / Luis Fonsi / Manu Chao).
- **Matrix A (uitspraak):** klankfocus **j / g+e,i = /x/ (jota)** + **h muda**; acentuación = klemtoon in
  groetformules (bue·nos **DÍ**·as). Werkvorm ≠ die van U1 (bv. minimale paren + teken-wat-je-hoort).
- **Matrix B (recycling):** breng U1-chunks terug — saludos/despedidas, presentarse, cortesía — in een
  **andere** werkvorm (bv. via een §0 «Ponte al día»-opstapje + rollenspel).
- **Doelcodes:** o.a. `C4-GE-1/2`, `C4-WS-2`, `C4-MEC-1/3`, `C4-CU-2` (zie leerdoelendoc §3, thema 2).
- **Auteur levert:** transcript + centrale taalhandelingen van sitcomvideo 2 + de YouTube-link (of Drive-id).

De volledige 14-thema-tabel (met dominante doelcodes en eindtaken) staat in
`C4_LEERDOELEN_EVALUATIE.md` §3.

---

## 8 · PLAK-DIT in de nieuwe chat (U2-bouwchat, zelfde project)

```
Nieuwe chat, zelfde project (Spaanse cursus, repo espa-ol-en-la-pr-ctica).
We bouwen UNIDAD 2 van C4 «Bienvenidos al español» (thema: Saludos y cortesía).

Lees eerst:
- CLAUDE.md                                   → projectgeheugen (§3 C4, §10 U1-lock, §13/§14 bladspiegel)
- HANDOVER_C4.md                              → productiehandboek (VOLG DIT)
- 01-cursussen/04-welcome/C4_LEERDOELEN_EVALUATIE.md   → doelcodes + 14-thema-tabel (thema 2)
- 01-cursussen/04-welcome/reservoir/C4_coverage.md     → matrix A (klankfocus U2 = jota + h muda) + matrix B + nog-beschikbare IDs
- U1 als golden sample: 03-build/web/gen_c4u1_*.py · 03-build/pptx/gen_c4u1_ppt.py

Werkwijze (uit HANDOVER_C4.md §4): (1) ik lever transcript + centrale taalhandelingen + videolink van
video 2; (2) vul U2_cocktail.md in (nieuwe reservoir-IDs + matrix A jota/h-muda + matrix B chunk-terugkeer);
(3) kopieer de gen_c4u1_*-scripts → gen_c4u2_*, vervang inhoud/nummer/parada/TEMA, pijplijn ongewijzigd;
(4) bouw de 4 formaten (hub · PDF · PPTX), (5) MEET de bladspiegel en verrijk elke sectie tot volle pagina
(85–99 %), (6) verwijder meta-jargon, zet doelcodes op de docentenpagina, (7) update coverage, commit op
branch claude/spanish-course-development-jx25ay en lever.

Begin met vragen wat ik aanlever voor video 2, en met het invullen van U2_cocktail.md.
```

---

*C4 · U1 gelockt 2026-07-26. Zelfde parameters/pijplijn voor U2–U14. Print = PDF; Word optioneel/onverifieerbaar in sandbox.*
