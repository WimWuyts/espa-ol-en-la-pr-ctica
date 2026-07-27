# C6+ — pas deze werkprincipes toe (IN DEZE CHAT)

> **Lees dit als werkinstructie voor de C6+-cursus waar je nu aan brainstormt en bouwt.** Het zijn de principes uit de C5-ontwikkeling (dezelfde monorepo). **Pas ze rechtstreeks hier toe.**
>
> ⛔ **BELANGRIJK — doe dit NIET:** géén nieuwe chats, sessies, triggers of achtergrond-operaties aanmaken. Niets "opzetten" of "delegeren". **Alles gebeurt in deze chat, stap voor stap, door jou zelf.** Dit is geen opdracht om iets te orkestreren — het zijn richtlijnen om zélf te volgen wanneer je een C6+-onderdeel maakt.

---

## 0 · Meld telkens welk model je nodig hebt
Vóór je een cursusonderdeel bouwt, zeg je kort welk model je daarvoor nodig hebt (de auteur zet het dan goed; hij werkt op **Opus**): sterk redeneermodel (Opus) voor het bouwen + Spaanse correctheid; een snel model volstaat voor puur mechanisch nakijken (tellingen, dekking). Eén regeltje volstaat: *«Voor dit onderdeel heb ik [model] nodig.»*

## 1 · Wat C6+ is
Paarse **vervolgcursus** op *Español en la práctica* (6de, huidige cohorte). Eindpunt = A2 → aanzet B1 (zoals C6), maar via een ander vertrekpunt: je **vult de hiaten** in t.o.v. leerplan + outlines 5 & 6. **Het wát — de gap-analyse en welke hiaten/units — beslis je in deze chat.** Deze principes zeggen enkel *hoe* je het bouwt.
- **Leerplan-scope (hard):** géén futuro simple, géén condicional, géén subjuntivo. «Aanzet B1» = A2 consolideren.
- **Kleur = paars:** `--g:#7C56A9 · --gd:#5B3E83 · --gt:#EEE8F5` (uit `02-huisstijl/tokens/tokens.json`, sleutel `c6plus`). Enige kleurwissel; verder niets aan layout/CSS wijzigen.
- Bronnen: `00-brondocumenten/espanol-en-la-practica/` (oude cursus) + `00-brondocumenten/gap-analyse/` + `00-brondocumenten/outlines/`.

## 2 · Neem C5·U5 als voorbeeld en hergebruik de bestaande bouwstenen
Kopieer de U5-generatoren en wissel enkel content + paars-kleur (niets aan de opbouw wijzigen):
`01-cursussen/05-a1/U5/gen_u5_print.py` (print + editlaag) · `03-build/web/gen_u5_web.py` (hub) · `03-build/pptx/gen_u5_docente.py` (2 decks) · `spaans-motor/make_u5_games.py` (games) · `01-cursussen/05-a1/U5/U5_cocktail.md` (voorbeeld-receta).
Gedeeld en klaar voor gebruik: `02-huisstijl/reservoir/` · `02-huisstijl/beeld/generators/vocab_emoji.py` · `cast_gen.py` · `02-huisstijl/templates/cursus-print.css` · `02-huisstijl/fonts/` · `spaans-motor/`. C6+-units leven in `01-cursussen/06-vervolg/`.

## 3 · De cocktail-aanpak — lees deze drie documenten vóór élk onderdeel
1. `02-huisstijl/reservoir/reservoir_index.md` — de plukvijver (453 werkvormen/patronen/tools).
2. `02-huisstijl/reservoir/coverage.md` — het dekkings-grootboek (voeg C6+-kolommen toe).
3. je eigen `01-cursussen/06-vervolg/U<N>/U<N>_cocktail.md` — de receta per unit.

Werkwijze per unit: schrijf een cocktail-receta die per onderdeel **bewust onder-gebruikte reservoir-IDs** kiest (variatie), cureer de woordenschat uit de master-pool (`materiales-vorig-project/…Master_v8.xlsx`, kandidatenpool — niet forceren), weef passende parels in (`PARELS_materiales.md`), en werk na de build het grootboek bij.

## 4 · Kwaliteitsregels (het U5-niveau)
- **4 formaten** per unit: PDF **altijd mét** bewerkbare `U<N>.html`-laag · HTML-hub · PowerPoint (docente + alumno, **beide `.pptx`, nooit `.ppsx`**) · motor-games (10–20).
- **Emoji-flashcards** (via `vocab_emoji.py`), **ruta-kaart discreet** (groot enkel U0), **Cultura unit-eigen** (2–3 kaarten, geen 4× dezelfde kaart).
- **Visueel-eerst grammatica + een traditionele oefenbatterij ernaast** (gap-fill · substitutie · matching · dictee · ordenen) — de klassieke cursus-feeling náást het moderne.
- **Quota per unit:** ≥1 luisterdialoog · ≥1 rijke Lectura · ≥2 opname-oefeningen · ≥1 traditionele cloze-werkwoord · **HTML-hub ≥100 interactieve oefeningen met meerdere reeksen per oefening**.
- **Volle antwoordruimte**; nooit oplossingen op de leerlingpagina; sectienummering zonder gat; **4 vaardigheden** in de PowerPoint; kruisverwijzingen print↔hub↔pptx; tellingen kloppen.

## 5 · GEEN lege pagina's — controleer echt
Vertrouw niet op één inkt-drempel. HTML: simuleer een **echte klik** op elk tabblad en **bekijk** de screenshot (JS-panelen renderen pas op klik). Print: meet de vulling per pagina én **kijk** naar de dunste pagina('s). Los halflege pagina's op; nooit een los slotkader dat alleen op een pagina spilt.

## 6 · Levering & git (jij doet dit hier)
Bouw stap voor stap zelf. `03-build/*` is gitignored → outputs met `git add -f`. Commit in het Nederlands, push naar de C6+-branch (vraag de auteur de naam). Lever per unit een zip met de 4 formaten + LEESMIJ. Het zijn klasversies → controleer dat beide pptx openen en de PDF volledig rendert.

---

> **In één zin:** bouw de C6+-inhoud die je in deze chat beslist, **hier en zelf**, met C5·U5 als voorbeeld, de cocktail-aanpak (lees de drie documenten), de U5-kwaliteitsregels, in het paars — en **maak géén nieuwe chats of operaties aan**.
