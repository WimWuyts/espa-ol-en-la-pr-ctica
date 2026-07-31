# Startprompt — de overige unidades bouwen

> Kopieer het blok onder de streep als eerste bericht in de nieuwe chat.
> Alles erboven is context voor de auteur.

**Stand op 2026-07-31:** U0 en U1 zijn af voor C5 en C6+ — vier formaten, getypte
oefeningen, leestekst, luisterfragment, bronnenlijst en escape room. Te gaan:
**C5 U2–U8** (zeven units) en **C6+ U2–U7** (zes units). U1 is de norm.

---

Werk op branch **`claude/spanish-course-development-jx25ay`**.

**Lees eerst:** `CLAUDE.md` — vooral §13, §14, §14bis, §14ter en §18.

## Wat je bouwt

Breng **U2 tot en met U8 (C5)** en **U2 tot en met U7 (C6+)** op exact het niveau van
**U1**. Eén unit tegelijk, en per unit eerst C5, dan C6+. Lever pas op als een unit
volledig af is; begin niet aan de volgende.

U0 en U1 zijn af — daar niets aan wijzigen tenzij de auteur erom vraagt.

## De zeven stappen per unit

Neem `U1` als voorbeeld: elk van deze stappen is daar precies één keer gezet, en de
bestanden staan er nog. Kijk hoe het daar gebeurde vóór je iets nieuws bedenkt.

**1 · Getypte grammatica** — `03-build/web/hub_type_gram.py`
Voeg `SETS[("C5", n)]` toe: **drie drills van elk twaalf items**. Kies ze uit de
grammatica van díé unit (kijk in het paneel Gramática van de hub welke onderwerpen er
zijn). `accents:"strict"` bij werkwoordsvormen en overal waar het accent zélf de
leerstof is; `"soft"` bij woordenschat. Elk item krijgt `why`, en `hint` waar het helpt.
**Reken elke vorm na** — dit is de plaats waar een fout jarenlang blijft staan.

**2 · Leestekst en luisterfragment** — `lectura_data.py` en `escucha_data.py`
Eén van elk per unit. **Drie regels die de validatoren afdwingen:**
* het bewijs bij elke juist/fout-stelling staat **letterlijk** in de tekst;
* precies **vijf** detailvragen per luisterfragment, ≥4 scan- en V/F-vragen per leestekst;
* bij elke meerkeuzevraag zit het antwoord in de opties.
`python3 -c "import lectura_data, escucha_data"` moet schoon draaien — de controle zit
onderaan beide bestanden en gaat af bij import.
**Kies de tekstsoort bewust anders** dan die van het luisterfragment van dezelfde unit,
én anders dan wat er in eerdere units al stond (tot nu gebruikt: anuncio · tablón ·
perfil · blog · diálogo · entrevista).

**3 · De hub** — `03-build/web/gen_u<n>_web.py` / `gen_c6plus_u<n>_web.py`
* paneel **`escuchar`** toevoegen vlak vóór `juegos`, en `['escuchar','Escuchar 🎧']`
  in de `PANELS`-array;
* het **lectura-blok** onderaan het bestaande lectura-paneel;
* imports: `hub_bloques`, `escucha_data`, `lectura_data`;
* CSS: `hub_drills.ESCUCHA_CSS + hub_drills.LECTURA_CSS`;
* JS: `hub_drills.ESCUCHA_JS + hub_drills.LECTURA_JS`, en
  `JS += hub_bloques.escucha_js(...) + hub_bloques.lectura_js(...)`.

**4 · De printlaag** — `01-cursussen/…/U<n>/gen_*_print.py`
`§5 Lectura` en `§6 Escucha`, elk op een eigen bladzijde, vlak vóór `CULTURA`, via
`PB.lectura_print(...)` en `PB.escucha_print(...)`. Vergeet `+ PB.CSS` niet in de
`<style>` als die er nog niet staat. **Alleen toevoegen, nooit weglaten** — bestaande
secties, oefeningen en nummering blijven ongemoeid.

**5 · De PowerPoints** — `03-build/pptx/gen_*_docente.py`
Twee regels in de `_run_all`-lijst, vlak vóór `s18_tarea()`:
```python
import lectura_data as _LD, escucha_data as _ED     # bovenaan
E.s_lectura(_LD.C5_U<n>); E.s_escucha(_ED.C5_U<n>)  # in _run_all
```
De twee dia-bouwers in de engine (`gen_u0_docente.py`) nemen hun data als argument, dus
je hoeft niets te kopiëren. Elk deck komt zo op 23 dia's (docente) en 22 (alumno).

**6 · Bronnen en escape room** — `03-build/web/extra_bronnen.py`
De auteur levert per unit een linkenlijst en een escape-room-URL. Zolang die er niet
zijn: **niets verzinnen** en het Extra-tabblad de terugvalinhoud laten tonen (die staat
er al en is leerlingklaar). Komen ze wel: `BRONNEN[(cursus, n)]` in groepen die de
volgorde van de unit volgen, en `DESTACADO[(cursus, n)]` voor de escape room.
**Controleer altijd** dat elke aangeleverde unieke URL er precies één keer in staat —
niets verloren, niets bijgekomen — en meld welke rijen je hebt samengevoegd.

**7 · PDF's en zips**
```
/opt/pw-browsers/chromium --headless --no-sandbox --disable-gpu \
  --print-to-pdf=03-build/pdf/<naam>.pdf --no-pdf-header-footer "file://<abs pad>/<unit>.html"
python3 03-build/make_zip.py C5 --units <n> --out <pad>.zip
```

## Controleren vóór je oplevert

```
python3 03-build/check_regressie.py      # moet schoon zijn: erbij mag, eraf niet
```

Daarnaast, in een echte browser (er zijn geen playwright-bindings; injecteer een klein
proefscript in een kopie van de hub en lees het uit met `--dump-dom`):
* 8 tabbladen, waaronder **Escuchar 🎧**;
* ± **70 zichtbare typvelden** (34 vocabulaire + 36 grammatica);
* het luisterblok telt **zes treden** en het transcript staat dicht;
* **geen consolefouten**, geen horizontale overloop op 380 px.

En een meta-scan op de leerlingpagina's (§18): geen `link volgt`, `leerkracht vult`,
`nog te …`, `[BEELD:`, `[AUDIO:`, `TODO`. Let op: **«todo» is het Spaanse woord voor
«alles»** en dus geen placeholder — kijk naar de context vóór je iets weghaalt.

## Voetangels die tijd kosten

* **`03-build/` staat in `.gitignore`.** PowerPoints, PDF's en zips moeten met
  `git add -f`. De `.py`-bronbestanden zijn wél uitgezonderd.
* **`gen_c6plus_u<n>_print.py` importeert `gen_u0_print`** als engine, en dat schrijft
  bij import ook `U0.html` opnieuw. Dat is normaal en onschadelijk.
* **Zoek-en-vervang op korte namen ontspoort.** `"s18_tarea()"` vervangen raakt óók
  `def s18_tarea():`. Vervang op de regel uit `_run_all`, niet op de losse naam.
* **De spelaantallen niet met de hand schrijven.** Ze klopten in vier units al niet.
  Gebruik de plaatshouder `__NGAMES__` met `str(len(GAMES))`, of tel in JS.
* **Chromium staat op `/opt/pw-browsers/chromium`** (een symlink; niet het pad
  eronder gebruiken).

## Wat je NIET doet

Geen futuro simple, geen condicional, geen subjuntivo — ook niet als afleider in een
meerkeuzevraag. Geen bouw-jargon of metatekst op een leerlingpagina. Geen oplossingen
op de leerlingpagina: die horen in het docentendossier en in de zelfcorrectie.

## Opleveren

Per unit: de bijgewerkte hub, de PDF met zijn bewerkbare HTML-laag, twee PowerPoints,
een schone regressiecheck, en drie regels over wat er is bijgekomen en wat je
onderweg hebt rechtgezet. Committen in het Nederlands, pushen naar
`claude/spanish-course-development-jx25ay`.

## Nog open

De **QR-codes** en de **echte audio** worden in één sweep afgewerkt zodra alle units
klaar zijn en de Netlify-pagina bestaat (`CLAUDE.md` §18). Tot dan blijven de QR's
cosmetisch en leest browser-TTS de fragmenten voor — meld dat eerlijk, maak er geen
belofte van.
