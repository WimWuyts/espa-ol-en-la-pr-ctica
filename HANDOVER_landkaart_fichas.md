# Handover — de «landkaart-fiches» (meelopende feitenlaag) hergebruiken in C4 & C6+

> **Wat dit is:** de interactieve *mundo hispano*-kaart in de HTML-hub toont, als je op
> een land klikt, een **informatiefiche**. Die fiche heeft twee lagen:
> 1. een **vaste set data** (altijd gelijk, elk land): vlag · capital · población ·
>    moneda · gentilicio · idioma(s) + **«¿Sabías que…?»** (coole weetjes: personen,
>    architectuur, geschiedenis Maya's/Inca's/Azteken);
> 2. één **themafeit dat meebeweegt met de unidad** (U5 = eten, U2 = familia,
>    U7 = wonen, …) + een **★ ¡Estás aquí!**-markering voor La Ruta.
>
> Deze laag is al gebouwd voor **C5 (U0–U8)**. Dit document legt uit hoe je ze in
> **C4 (rood)** en **C6+ (paars)** integreert — **zonder van branch te wisselen**.
>
> ⛔ **Doe NIET:** geen nieuwe chats/branches/triggers aanmaken. Alles gebeurt in de
> chat waarin je die cursus bouwt, stap voor stap, door jou zelf.

---

## 0 · Waarom dit makkelijk hergebruikbaar is

De **data is cursus-onafhankelijk**: alle vier de cursussen spelen zich af in dezelfde
**Spaanstalige wereld**. Daarom staat álle inhoud in **één gedeelde bron**:

```
03-build/web/paises_data.py     ← 22 landen × vaste fiche + 9 thema's × 22 = 198 themafeiten
03-build/web/patch_maps.py      ← bakt de fiche in de gen_u*_web.py van een cursus
```

Een cursus hergebruikt die bron en levert enkel **twee kleine mappings** aan:
- **`UNIT_TEMA`** — welke themalaag hoort bij welke unit (bv. `U3 → comida`);
- **`PARADAS`** — de route (welk land is «parada» vanaf welke unit, voor de ★-markering).

De **kleur klopt vanzelf**: de render gebruikt de cursus-kleurtokens (`--g/--gd/--gt`),
dus de fiche wordt rood in C4, blauw in C6, paars in C6+ — niets aan te passen.

---

## 1 · De twee bestanden op je branch krijgen (GEEN branch-switch)

De bron leeft op branch **`claude/spanish-course-c5-c6-cadm4g`**. Haal enkel die twee
bestanden binnen op jóuw branch met één commando (dit wisselt **niet** van branch, het
kopieert alleen die paden naar je working tree):

```bash
git checkout claude/spanish-course-c5-c6-cadm4g -- 03-build/web/paises_data.py 03-build/web/patch_maps.py
```

> Bestaan de bestanden al op je branch (bv. na een merge met de default-branch)? Dan
> hoef je niets te doen. Zit je op een branch waar `03-build/web/` nog niet bestaat?
> Maak de map aan; de bestanden zijn verder zelfstandig (enkel `json` uit de stdlib).

---

## 2 · Integratie in 3 stappen (per cursus)

De C4/C6+-hubs worden gebouwd vanuit hetzelfde C5-sjabloon (zie de C4/C6+-handovers),
dus ze hebben al: een `#mapwrap` met de ingebedde `mundo_map_real.svg`
(`path.spa/path.usa` met `data-c="XXX"`), een `#mapinfo`-kader en de klik-IIFE met
`const INFO={…}` + de render-regel `box.innerHTML=…`. Je vervangt enkel díe twee.

### Stap A — definieer je cursus-mappings
Zet bovenaan een klein bestandje, bv. `03-build/web/mapa_<cursus>.py`:

```python
# mapa_c6plus.py — route + themalagen voor C6+ (paars)
import paises_data as PD

# welke themalaag per unit  (thema_key MOET in PD.TEMAS bestaan; zie §3)
UNIT_TEMA = {
 0: ("simbolo", "🌎 Símbolo"),
 1: ("persona", "⭐ Alguien de aquí"),
 2: ("familia", "👪 En familia"),
 3: ("rutina",  "🕐 El ritmo del día"),
 4: ("comida",  "🍽️ En la mesa"),
 5: ("compras", "🛍️ De compras"),
 6: ("lugar",   "🏙️ Un lugar"),
 7: ("viaje",   "✈️ Para visitar"),
 # … pas aan aan het EXACTE aantal en de thema's van je C6+-units
}

# de route: {landcode: (start-unit, "rango", "NL-beschrijving")}
PARADAS = {
 "ESP": (0, "U0–U2", "España — het vertrekpunt"),
 "MEX": (3, "U3–U4", "México"),
 "COL": (5, "U5",    "Colombia"),
 "ARG": (6, "U6",    "Argentina (Mateo · voseo)"),
 "PER": (7, "U7",    "Perú"),
 # … de landen/units van jóuw route
}
```

### Stap B — bak de fiche in je gen_u*_web.py
De meegeleverde `patch_maps.py` is voor C5 (gebruikt `PD.info_block_js(u)` zonder
mappings). Maak een cursus-variant die jóuw mappings meegeeft:

```python
# patch_maps_c6plus.py
import re, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paises_data as PD
import mapa_c6plus as M          # jouw UNIT_TEMA + PARADAS

WEB   = os.path.dirname(os.path.abspath(__file__))
INFO  = re.compile(r"const INFO=\{.*?\n \};", re.S)   # of: r"const INFO=\{.*?\};" na 1e patch
REND  = re.compile(r"box\.innerHTML='<h3>'\+d\.fl\+[^\n]*;")

for u in M.UNIT_TEMA:                                  # enkel jouw units
    f = os.path.join(WEB, f"gen_u{u}_web.py")          # of jouw naamgeving/pad
    if not os.path.exists(f): continue
    src = open(f, encoding="utf-8").read()
    info_js = PD.info_block_js(u, unit_tema=M.UNIT_TEMA, paradas=M.PARADAS)
    src, n1 = INFO.subn(lambda m: " " + info_js, src, count=1)
    src, n2 = REND.subn(lambda m: PD.RENDER_JS, src, count=1)
    open(f, "w", encoding="utf-8").write(src)
    print(f"U{u}: info={n1} render={n2}")
```

> **Belangrijke les uit C5 (niet in de val trappen):** `info_block_js()` levert al een
> **compleet** blok `const INFO={…};` (met sluit-`}` én `;`). Voeg er **geen** extra
> `};` achter toe — dat gaf een JS-syntaxfout die de héle inline-`<script>` (en dus de
> subnav, de spellen, alles) stillegde. Regexen matchen zowel het originele blok
> (`…\n };`) als de reeds-gepatchte vorm, dus herdraaien is veilig (idempotent).

### Stap C — herbouw de hubs en **verifieer echt**
```bash
python3 patch_maps_c6plus.py
for u in 0 1 2 …; do python3 gen_u${u}_web.py; done
```
Controleer daarna hard (niet «het ziet er goed uit»):
1. **JS-syntax:** trek de `<script>` uit elke `U*_web.html` en draai `node --check`.
   Eén foutje legt de hele pagina plat.
2. **Echte klik:** open de hub met Playwright, klik de **Cultura**-subnav-knop, klik
   een land-`path` en lees `#mapinfo`. Je moet de vaste velden **plus** het juiste
   themafeit voor die unit zien (én de ★ bij een parada). Voorbeeld-script:
   `03-build/web/…` → hergebruik het patroon uit deze sessie (klik subnav → dispatch
   click op `path[data-c="ARG"]` → `document.getElementById('mapinfo').innerText`).

---

## 3 · Thema's & landen uitbreiden (indien nodig)

- **Bestaande thema's** (herbruikbaar zoals ze zijn): `simbolo · persona · familia ·
  rutina · musica · comida · compras · lugar · viaje`. Map je units gewoon op deze
  sleutels.
- **Nieuw thema nodig** (bv. C4 «sonidos», of C6+ «historia»)? Voeg één dict toe aan
  `PD.TEMAS`, met per landcode een kort feit, en gebruik die sleutel in je `UNIT_TEMA`.
  Ontbreekt een land in een thema-dict, dan valt dat land netjes terug op enkel de
  vaste fiche (geen crash).
- **Landgegevens** (población, weetjes…) staan één keer in `PD.PAISES`; een verbetering
  daar werkt **meteen in álle cursussen** door. Landcodes = ISO-3
  (`MEX, ESP, COL, PER, ARG, VEN, CHL, ECU, GTM, CUB, BOL, DOM, HND, PRY, NIC, SLV,
  CRI, PAN, URY, PRI, GNQ, USA`) — dezelfde als de `data-c` in de kaart-SVG.

---

## 4 · Voorgestelde mappings

### C6+ (paars) — dezelfde route als C5/C6, ander vertrekpunt
Neem de **9 bestaande thema's** en map ze op je C6+-units (pas aan aan wat je in de
C6+-chat beslist hebt). De route mag de C5-boog volgen (España → México → Colombia →
Argentina (Mateo) → Perú), met de starts op jóuw unit-nummers.

### C4 (rood) — «El despegue», pre-A1, videogedreven
C4 draait rond **klank, accent en chunks**; het is lichter. Twee opties:
- **Heb je de kaart in de C4-hub?** Gebruik dan vroege, herkenbare thema's:
  `simbolo` (símbolos/saludos) · `persona` (bekende namen) · `musica` · `comida`.
  Zo krijgen de 4de-jaars dezelfde «meelopende weetjes» zonder leerplaninhoud van het
  5de op te souperen (enkel cultureel-motiverend, geen A2-doelen).
- **Nog geen kaart in C4?** Voeg `#mapwrap`+`#mapinfo`+de klik-IIFE toe zoals in het
  C5-sjabloon (kopieer uit een `gen_u*_web.py` van C5), en volg dan §2.

> Houd de **overlap met C5 bewust klein** (CLAUDE.md §3): de kaart-fiches in C4 zijn
> een *motiverende* laag, geen leerstof die je in C5 zou willen afvinken.

---

## 5 · In één zin
De feitenlaag is **al gebouwd en cursus-onafhankelijk** (`paises_data.py`). Haal de twee
bestanden branch-loos binnen (`git checkout … -- …`), schrijf je **`UNIT_TEMA` + `PARADAS`**
voor die cursus, bak ze met een cursus-variant van `patch_maps.py` in de `gen_u*_web.py`,
herbouw de hubs en **verifieer met een echte klik** — de kleur en de rest volgen vanzelf.
