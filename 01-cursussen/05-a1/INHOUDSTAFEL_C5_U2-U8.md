# C5 · Inhoudstafel unidades 2 → 8

Werkdocument om (a) de **bronnenlijsten** per unit samen te stellen en (b) de **escape rooms**
te ontwerpen. Alles hieronder is uit de gebouwde cursus zelf gehaald, niet uit het geheugen:
de sectiekoppen komen uit de print-HTML, de woordenschatgroepen uit `u<n>_vocab.json`, de
drills uit `hub_type_gram.py` en de teksten uit `lectura_data.py` / `escucha_data.py`.

## Hoe je dit gebruikt

**Voor de links.** De koppen onder «Onderwerpen voor de bronnenlijst» zijn al geschreven in
de vorm die `extra_bronnen.py` verwacht. Eén regel per bron:

```python
BRONNEN[("C5", 2)] = [
    ("§1 · La familia y el verbo tener", [
        ("ProfeDeELE", "La familia — vocabulario y árbol genealógico", "https://…"),
        ("Arche-ELE",  "El verbo tener — presente",                     "https://…"),
    ]),
    ("§2 · Los posesivos", [ … ]),
]
```

Herkende bronnen: `ProfeDeELE` · `Arche-ELE` · `My Daily Spanish`. Een YouTube-URL wordt
automatisch als video gemarkeerd. Een bron mag in meerdere groepen staan.

**Voor de escape rooms.** Onder elke unit staat «Wat de escape room moet testen»: de
leerstof die de leerling nodig heeft om eruit te raken, plus de *parada* als decor. Invullen
in `DESTACADO[("C5", n)]` met de velden `kicker · titel · soort · url · es · nl · tip` —
kijk naar U0 («El museo de las palabras perdidas») en U1 («Línea Cero · Madrid») als model.

---

## U2 «Mi gente» — parada **Sevilla** 🇪🇸

**Tarea final:** Álbum de familia · **Vocabulario:** 69 woorden · **Print:** 42 blz. · **Spellen:** 24

| § | Inhoud |
|---|---|
| §0 | ¡Ponte al día! (repaso) |
| §1 | La familia — los miembros + **tener** |
| §2 | Los posesivos — mi, tu, su, nuestro |
| §3 | Los adjetivos — describir a las personas |
| §4 | Ser o estar — la gran trampa del «zijn» |
| §5 | Los demostrativos — este y ese |
| §6 | Lectura «La familia de Lucía» |
| T | Taller de lengua — conectores + ortografía |
| §7 | **Lectura** «Mi familia en una foto» — correo electrónico |
| §8 | **Escucha** «¿Quién es quién?» — concurso de clase |
| C | Cultura — La familia hispana (apodos · quinceañera · Frida Kahlo) |
| R · V | Repaso · Vocabulario |

**Getypte drills:** el verbo tener · los posesivos · concordancia van het adjectief

**Onderwerpen voor de bronnenlijst**
- `§1 · La familia y el verbo tener`
- `§2 · Los posesivos — mi, tu, su, nuestro`
- `§3 · Los adjetivos — el físico y el carácter`
- `§4 · Ser o estar`
- `§5 · Los demostrativos — este y ese`
- `Taller — los conectores y la ortografía`
- `El cuerpo` · `Los colores` · `Cultura — la familia hispana`

**Wat de escape room moet testen** — decor: Sevilla, een familiealbum of een oud huis in de
Barrio de Santa Cruz. Leerstof: de familiebanden (primo ≠ sobrino), *tener* vervoegen, het
juiste bezittelijk voornaamwoord kiezen, een persoon beschrijven met kloppende concordancia,
en ser tegenover estar.

---

## U3 «El tiempo vuela» — parada **Barcelona** 🇪🇸

**Tarea final:** Un día en mi vida · **Vocabulario:** 71 woorden · **Print:** 43 blz. · **Spellen:** 29

| § | Inhoud |
|---|---|
| §0 | ¡Ponte al día! |
| §1 | La hora — ¿Qué hora es? |
| §2 | Mi rutina — los verbos reflexivos |
| §3 | Presente irregular — cambio de raíz (o→ue · e→ie · e→i · u→ue) |
| §4 | Frecuencia + días, meses y estaciones |
| §5 | Lectura «El día de Pau» |
| §6 | **Lectura** «¿Quedamos esta semana?» — chat de móvil |
| §7 | **Escucha** «Mi sábado en Barcelona» — mensajes de voz |
| ★ | Cultura · El horario español |
| ✓ · V | Repaso · Vocabulario |

**Getypte drills:** verbos reflexivos · cambio de raíz · hacer, ir, salir

**Onderwerpen voor de bronnenlijst**
- `§1 · La hora — es la una / son las…`
- `§2 · Los verbos reflexivos y la rutina diaria`
- `§3 · El presente irregular — cambio de raíz`
- `§3b · hacer · ir · salir`
- `§4 · La frecuencia — siempre, a veces, nunca`
- `Los días, los meses y las estaciones`
- `Taller — la ortografía del tiempo` · `Cultura — el horario español`

**Wat de escape room moet testen** — decor: Barcelona, een klok die stilstaat, een gemiste
trein of een dag die zich herhaalt. Leerstof: het uur lezen én zeggen, de dagindeling in de
juiste volgorde met reflexieve werkwoorden, de klinkerwissel in het presente, en
frequentiewoorden koppelen aan een weekschema.

---

## U4 «Me gusta» — parada **València / la costa** 🇪🇸

**Tarea final:** Mi playlist · **Vocabulario:** 64 woorden · **Print:** 43 blz. · **Spellen:** 24

| § | Inhoud |
|---|---|
| §0 | ¡Ponte al día! |
| §1 | Me gusta(n) · gustar & encantar |
| §2 | Estar de acuerdo · también / tampoco · a mí sí / a mí no |
| §3 | Proponer un plan · querer / poder + quedar |
| §4 | Lectura «Perfiles de gustos» |
| §5 | **Lectura** «Fiesta de la Música · València» — programa de festival |
| §6 | **Escucha** «¿Qué haces en tu tiempo libre?» — encuesta callejera |
| ★ ♫ | Cultura · El ocio joven y Rosalía · Banda sonora |
| ✓ · V | Repaso · Vocabulario |

**Getypte drills:** gustar al revés · también/tampoco/a mí sí/a mí no · querer & poder

**Onderwerpen voor de bronnenlijst**
- `§1 · El verbo gustar — y encantar, interesar`
- `§2 · Reaccionar — también, tampoco, a mí sí, a mí no`
- `§3 · Querer y poder + infinitivo — quedar con alguien`
- `Los pronombres OI — me, te, le, nos, os, les`
- `El ocio y el tiempo libre` · `La música y el cine`
- `Cultura — Rosalía y la música en español`

**Wat de escape room moet testen** — decor: het festivalterrein aan de Malvarrosa, een
verloren playlist of een concert waar je binnen moet raken. Leerstof: gusta ↔ gustan met het
juiste pronombre, akkoord of niet akkoord reageren, en een afspraak maken met querer/poder.

---

## U5 «¡Ñam!» — parada **México · CDMX** 🇲🇽

**Tarea final:** La carta · **Vocabulario:** 68 woorden · **Print:** 39 blz. · **Spellen:** 21
· *referentie-unit (CLAUDE.md §10)*

| § | Inhoud |
|---|---|
| §0 | ¡Ponte al día! |
| §1 | Cantidades · mucho / poco / un poco de |
| §2 | Voy a comer · ir a + infinitivo |
| §3 | Pedir en el restaurante · la cortesía |
| §4 | La cuenta → la traigo · lo / la / los / las |
| §5 | Lectura «Dos cartas / una receta» |
| §6 | **Lectura** «El mercado de La Merced en cinco datos» — infografía |
| §7 | **Escucha** «Una mesa para tres» — en el restaurante |
| ★ | Cultura · Tacos, mercados y horarios |
| ✓ · V | Repaso · Vocabulario |

**Getypte drills:** ir a + infinitivo · cantidades · lo/la/los/las

**Onderwerpen voor de bronnenlijst**
- `§1 · Las cantidades — mucho, poco, un poco de`
- `§2 · Ir a + infinitivo — hablar del futuro próximo`
- `§3 · Pedir en el restaurante — la cortesía`
- `§4 · Los pronombres lo / la / los / las`
- `La comida, la fruta y la verdura` · `Las bebidas` · `La mesa`
- `Cultura — la comida mexicana y los horarios`

**Wat de escape room moet testen** — decor: het mercado de La Merced of een restaurant waar
de rekening niet klopt. Leerstof: hoeveelheden met de juiste concordancia, een bestelling
plaatsen met de beleefdheidsformules, over straks praten met *ir a*, en een gerecht vervangen
door lo/la/los/las.

---

## U6 «De tiendas» — parada **México · los mercados** 🇲🇽

**Tarea final:** Abre tu tienda · **Vocabulario:** 86 woorden · **Print:** 41 blz. · **Spellen:** 20

| § | Inhoud |
|---|---|
| §0 | ¡Ponte al día! |
| §1 | lo / la / los / las · ¿la falda? → la compro |
| §2 | Acabar de + infinitivo |
| §3 | este / ese / aquel · cerca ↔ lejos |
| §4 | Concordancia · una camiseta roja de rayas |
| §5 | Lectura «¡Rebajas! + una reseña» |
| §6 | **Lectura** «Cinco trucos para ir de rebajas» — artículo de consejos |
| §7 | **Escucha** «En el probador» — meningen en maten |
| ★ | Cultura · Rebajas, regateo y tianguis |
| ✓ · V | Repaso · Vocabulario |

**Getypte drills:** acabar de + infinitivo · este/ese/aquel · kleur + kledingstuk

**Onderwerpen voor de bronnenlijst**
- `§1 · Los pronombres lo / la / los / las`
- `§2 · Acabar de + infinitivo`
- `§3 · Los demostrativos — este, ese, aquel`
- `§4 · La concordancia — el color y la prenda`
- `La ropa y el calzado` · `Los colores y los materiales`
- `En la tienda — tallas, probador, caja` · `Cultura — rebajas, regateo y tianguis`

**Wat de escape room moet testen** — decor: een tianguis of een winkel die op slot gaat bij
de laatste klant. Leerstof: het juiste demonstrativo bij de afstand, kleur en kledingstuk
laten overeenkomen, *acabar de* om te zeggen wat net gebeurd is, en lo/la om niet in
herhaling te vallen.

---

## U7 «Mi casa y mi barrio» — parada **Colombia · Cartagena** 🇨🇴

**Tarea final:** Mi barrio · **Vocabulario:** 66 woorden · **Print:** 42 blz. · **Spellen:** 20

| § | Inhoud |
|---|---|
| §0 | ¡Ponte al día! |
| §1 | Hay / estar · er is ↔ waar het staat |
| §2 | ¿Dónde está? · las preposiciones de lugar |
| §3 | Estoy cocinando · estar + gerundio |
| §4 | ¿Cómo se va? · el imperativo (el camino) |
| §5 | Los ordinales · primero → el primer piso |
| §6 | Lectura «Un paseo por Cartagena» |
| §7 | **Lectura** «Se alquila apartamento en el centro» — anuncio de alquiler |
| §8 | **Escucha** «La visita al piso» — wat er ontbreekt |
| ★ | Cultura · La plaza y el barrio |
| ✓ · V | Repaso · Vocabulario |

**Getypte drills:** hay of está(n) · el imperativo · los ordinales met apócope

**Onderwerpen voor de bronnenlijst**
- `§1 · Hay o está(n)`
- `§2 · Las preposiciones de lugar`
- `§3 · Estar + gerundio`
- `§4 · El imperativo — dar direcciones`
- `§5 · Los números ordinales`
- `La casa y los muebles` · `El barrio y los servicios` · `El transporte`
- `Cultura — la plaza y la vida de barrio`

**Wat de escape room moet testen** — decor: de ommuurde stad van Cartagena, een huis waarin
je de weg kwijtraakt, of een adres dat je moet vinden. Leerstof: hay tegenover está, een
voorwerp lokaliseren met de juiste preposición, een route volgen én geven met de imperativo,
en de verdieping benoemen met een ordinal.

---

## U8 «¿Qué has hecho?» — parada **Perú · Cusco / Machu Picchu** 🇵🇪

**Tarea final:** Mis vacaciones · **Vocabulario:** 64 woorden · **Print:** 38 blz. · **Spellen:** 18

| § | Inhoud |
|---|---|
| §0 | ¡Ponte al día! |
| §1 | ¿Qué has hecho? · el pretérito perfecto compuesto |
| §2 | Los participios · -ado / -ido + los ocho irregulares |
| §3 | Marcadores · ya · todavía no · hoy · alguna vez · nunca |
| §4 | ¿Qué tiempo hace? · el clima |
| §5 | Lectura «El diario de viaje de Nina» |
| §6 | **Lectura** «¿Qué tipo de viajero eres?» — test de revista |
| §7 | **Escucha** «El tiempo en los Andes» — parte del tiempo |
| ★ | Cultura · Machu Picchu y el clima andino |
| ✓ · V | Repaso · Vocabulario |

**Getypte drills:** haber + participio · los participios irregulares · los marcadores

**Onderwerpen voor de bronnenlijst**
- `§1 · El pretérito perfecto compuesto`
- `§2 · Los participios — regulares e irregulares`
- `§3 · Los marcadores — ya, todavía no, alguna vez, nunca`
- `§4 · El tiempo y el clima`
- `Los viajes y el transporte` · `Las vacaciones`
- `Cultura — Machu Picchu y los Andes`

**Wat de escape room moet testen** — decor: het treinstation naar Aguas Calientes, een
reisdagboek met ontbrekende bladzijden, of Machu Picchu in de mist. Leerstof: haber +
participio, de acht onregelmatige participios, ya tegenover todavía no, en het weer
beschrijven om te weten welke dag het is. Sluitstuk van de hele ruta — mag terugblikken op
Spanje, Mexico, Colombia en Peru.

---

## Twee dingen om te bevestigen

1. **Tarea final van U7 en U8.** De print zegt «Mi barrio» en «Mis vacaciones»; CLAUDE.md §12
   zegt «Mapa de mi barrio» en «Diario de viaje». Zeg welke van de twee klopt, dan trek ik
   het gelijk.
2. **De paradas van U6.** Die staat nu als «México / los mercados», een tweede halte in
   Mexico na U5. In CLAUDE.md §12 heet ze «México — mercados». Dat komt overeen; alleen de
   nummering op de kaart loopt door tot parada 8, terwijl de ruta negen unidades telt.
