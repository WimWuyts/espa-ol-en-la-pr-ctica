# Inhoudstafel · C5 U2–U8 en C6+ U2–U7

Werkdocument om (a) de **bronnenlijsten** per unit samen te stellen en (b) de **escape rooms**
te ontwerpen. Alles hieronder komt uit de gebouwde cursus zelf, niet uit het geheugen: de
sectiekoppen uit de print-HTML, de aantallen uit `u<n>_vocab.json` en de PDF's, de drills uit
`hub_type_gram.py` en de teksten uit `lectura_data.py` / `escucha_data.py`. Alle cijfers zijn
daarna teruggecontroleerd tegen diezelfde bestanden.

**Dertien units:** C5 unidad 2 tot 8 (zeven) en C6+ unidad 2 tot 7 (zes).

## Hoe je dit gebruikt

**Voor de links.** De koppen onder «Onderwerpen voor de bronnenlijst» staan al in de vorm die
`03-build/web/extra_bronnen.py` verwacht, in de volgorde van de unit zelf. Eén regel per bron:

```python
BRONNEN[("C5", 2)] = [
    ("§1 · La familia y el verbo tener", [
        ("ProfeDeELE", "La familia — vocabulario y árbol genealógico", "https://…"),
        ("Arche-ELE",  "El verbo tener — presente",                     "https://…"),
    ]),
    ("§2 · Los posesivos — mi, tu, su, nuestro", [ … ]),
]
```

Herkende bronnen: `ProfeDeELE` · `Arche-ELE` · `My Daily Spanish`. Een YouTube-URL wordt
automatisch als video gemarkeerd. Eén bron mag in meerdere groepen staan — dat is geen fout
maar een gevolg van hoe die sites hun oefeningen bundelen. Zolang er voor een unit geen lijst
is, toont het Extra-tabblad de leerlingklare terugvalinhoud; er komt nooit «link volgt» op de
leerlingpagina.

**Voor de escape rooms.** Onder elke unit staat «Wat de escape room moet testen»: de leerstof
die de leerling nodig heeft om eruit te raken, plus de *parada* als decor. Dat vult
`DESTACADO[("C5", n)]` met de velden `kicker · titel · soort · url · es · nl · tip`. Model:
U0 «El museo de las palabras perdidas» en U1 «Línea Cero · Madrid» voor C5, «El vuelo 69» en
«El martes desaparecido» voor C6+.

**Overlappende thema's.** Drie keer behandelen C5 en C6+ hetzelfde onderwerp in een ander
jaar; dat staat telkens als «Let op» bij de betrokken unit, zodat je bewust kan kiezen of je
één escape room hergebruikt of er twee maakt.

---

# Deel 1 · C5 (groen) — het vijfde jaar

## C5 U2 «Mi gente» — parada **Sevilla** 🇪🇸

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

## C5 U3 «El tiempo vuela» — parada **Barcelona** 🇪🇸

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

## C5 U4 «Me gusta» — parada **València / la costa** 🇪🇸

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

## C5 U5 «¡Ñam!» — parada **México · CDMX** 🇲🇽

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

## C5 U6 «De tiendas» — parada **México · los mercados** 🇲🇽

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

## C5 U7 «Mi casa y mi barrio» — parada **Colombia · Cartagena** 🇨🇴

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

## C5 U8 «¿Qué has hecho?» — parada **Perú · Cusco / Machu Picchu** 🇵🇪

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

---

# Deel 2 · C6+ (paars) — het zesde jaar, huidige cohorte

## C6+ U2 «Aquí vivo» — parada **Cartagena** 🇨🇴

**Tarea final:** Mapa de mi barrio · **Vocabulario:** 73 woorden · **Print:** 45 blz. · **Spellen:** 12

| § | Inhoud |
|---|---|
| §0 | ¡Ponte al día! |
| §1 | La casa — habitaciones y muebles |
| §2 · 2.2 · 2.3 | Hay vs estar · las preposiciones de lugar · practicar |
| §3 · 3.2 · 3.3 | Estar + gerundio · gerundios irregulares · ¿qué están haciendo? |
| §4 · 4.2 · 4.3 | Los pronombres lo/la/los/las · concordancia · la posición |
| §5 | El barrio y cómo llegar |
| §6 | Lectura «Mi barrio en Cartagena» |
| T | Taller de lengua (b/v · aquí, ahí, allí) |
| §7 | **Lectura** «Casa Azul»: dos reseñas |
| §8 | **Escucha** «Estoy perdido en Cartagena» — llamada con indicaciones |
| C · ★ · ✓ · V | Cultura (la vivienda hispana) · Tarea · Repaso · Vocabulario |

**Getypte drills:** hay of está(n) · estar + gerundio · lo/la/los/las

**Onderwerpen voor de bronnenlijst**
- `§2 · Hay o está(n) + las preposiciones de lugar`
- `§3 · Estar + gerundio — y los gerundios irregulares`
- `§4 · Los pronombres lo / la / los / las`
- `§5 · Cómo llegar — dar y seguir indicaciones`
- `La casa y los muebles` · `El barrio y la ciudad` · `Los verbos de movimiento`
- `Taller — b/v y aquí, ahí, allí` · `Cultura — la vivienda hispana`

**Wat de escape room moet testen** — decor: de ommuurde stad van Cartagena, een huis met
kamers die niet kloppen, of een adres dat je moet reconstrueren. Leerstof: hay tegenover
está(n), een voorwerp lokaliseren met de juiste preposición, zeggen wat er op dit moment
gebeurt, en met lo/la korter praten.

> **Let op:** dit thema overlapt met **C5 U7**. Als je één escape room voor allebei wil
> gebruiken, kan dat — maar C6+ heeft er *estar + gerundio* bij en C5 de *ordinales* en de
> *imperativo*. Twee aparte kamers is didactisch zuiverder.

---

## C6+ U3 «Conectados» — parada **Ciudad de México** 🇲🇽

**Tarea final:** Mi plan de fin de semana · **Vocabulario:** 63 woorden · **Print:** 44 blz. · **Spellen:** 13

| § | Inhoud |
|---|---|
| §0 | ¡Ponte al día! |
| §1 | El móvil y las redes |
| §2 · 2.2 · 2.3 | Ir a + infinitivo · las expresiones de tiempo · practicar |
| §3 · 3.2 · 3.3 | Los pronombres le/les · los verbos de comunicación · la posición |
| §4 · 4.2 | Acabar de + creo que · creo que + indicativo |
| §5 | Comunicar y hacer planes |
| §6 | Lectura «¿Adicto al móvil?» |
| T | Taller de lengua (c/z/qu · conectores de tiempo) |
| §7 | **Lectura** «¿Cuántas horas de pantalla?» — artículo met enquête |
| §8 | **Escucha** «Cómo hacer una videollamada con la abuela» — tutorial |
| C · ★ · ✓ · V | Cultura (el mundo digital hispano) · Tarea · Repaso · Vocabulario |

**Getypte drills:** ir a + infinitivo · le/les · creo que & acabar de

**Onderwerpen voor de bronnenlijst**
- `§2 · Ir a + infinitivo — el futuro próximo`
- `§3 · Los pronombres le / les — el objeto indirecto`
- `§4 · Creo que + indicativo — dar tu opinión`
- `§4b · Acabar de + infinitivo`
- `Los dispositivos y las redes sociales` · `Los verbos de comunicación`
- `Hacer planes y quedar` · `Cultura — el español en internet`

**Wat de escape room moet testen** — decor: een vergrendelde telefoon, een gesloten account,
of een groepschat die je moet ontcijferen. Leerstof: over morgen praten met *ir a*, aan wíe
je iets doet (le/les), *acabar de* voor wat net gebeurde, en een mening formuleren met
*creo que* + de gewone tijd — nooit subjuntivo.

---

## C6+ U4 «De viaje» — parada **Chile** 🇨🇱

**Tarea final:** Mi mejor viaje · **Vocabulario:** 66 woorden · **Print:** 38 blz. · **Spellen:** 12

| § | Inhoud |
|---|---|
| §0 | ¡Ponte al día! |
| §1 | Transporte y alojamiento |
| §2 · 2.2 · 2.3 | El pretérito perfecto · los participios irregulares · practicar |
| §3 · 3.2 | Por y para · practicar |
| §4 | Experiencias y lugares |
| §5 | Lectura «Un viaje inolvidable» |
| T | Taller de lengua |
| §6 | **Lectura** «Una postal desde Valparaíso» — postal + diario |
| §7 | **Escucha** «En la recepción del hostal» — reservering die niet klopt |
| C · ★ · ✓ · V | Cultura (el gran viaje hispano) · Tarea · Repaso · Vocabulario |

**Getypte drills:** haber + participio · los participios irregulares · por of para

**Onderwerpen voor de bronnenlijst**
- `§2 · El pretérito perfecto compuesto`
- `§2b · Los participios irregulares`
- `§3 · Por y para`
- `Los marcadores — ya, todavía no, alguna vez, nunca`
- `El transporte y el alojamiento` · `El viaje — reservar, perder el tren, sacar fotos`
- `Los paisajes y los lugares` · `Cultura — Atacama, Rapa Nui, el Camino de Santiago`

**Wat de escape room moet testen** — decor: een hostel in Valparaíso, een gemiste vlucht, of
een koffer die niet van jou is. Leerstof: haber + participio inclusief de onregelmatige, het
verschil ya ↔ todavía no, en por tegenover para (reden ↔ doel, doorheen ↔ bestemming).

> **Let op:** het perfecto en de participios komen ook in **C5 U8** voor. De C6+-versie heeft
> er *por/para* bij; de C5-versie het *clima*.

---

## C6+ U5 «Érase una vez» — parada **Buenos Aires** 🇦🇷

**Tarea final:** Una biografía · **Vocabulario:** 61 woorden · **Print:** 36 blz. · **Spellen:** 12

| § | Inhoud |
|---|---|
| §0 | ¡Ponte al día! |
| §1 | Biografía y logros |
| §2 · 2.2 · 2.3 | El pretérito indefinido · los pretéritos fuertes · practicar |
| §3 · 3.2 | Los pronombres juntos — se lo / se la · practicar |
| §4 | Contar una historia (érase una vez · primero… después… al final) |
| §5 | Lectura «Una vida de película» |
| T | Taller de lengua |
| §6 | **Lectura** «La leyenda de la yerba mate» — leyenda guaraní |
| §7 | **Escucha** «Los que llegaron en barco» — visita guiada |
| C · ★ · ✓ · V | Cultura (figuras del mundo hispano) · Tarea · Repaso · Vocabulario |

**Getypte drills:** el indefinido regular · los pretéritos fuertes · se lo / se la

**Onderwerpen voor de bronnenlijst**
- `§2 · El pretérito indefinido — verbos regulares`
- `§2b · Los pretéritos fuertes — ser, ir, tener, hacer, estar, decir, venir, poder, dar`
- `§3 · Se lo, se la — dos pronombres juntos`
- `§4 · Contar una historia — los conectores del relato`
- `La biografía — nacer, crecer, casarse, mudarse` · `Los logros y los premios`
- `Cultura — figuras del mundo hispano` · `Las leyendas`

**Wat de escape room moet testen** — decor: een archief in Buenos Aires, een verdwenen
biografie, of een koffer van een immigrant. Leerstof: het indefinido mét zijn tildes op de
yo- en él-vorm, de negen sterke verledens die juist géén tilde dragen, se lo / se la, en de
volgorde van een verhaal reconstrueren.

---

## C6+ U6 «Cuando era pequeño» — parada **Cusco** 🇵🇪

**Tarea final:** Cuando era pequeño/a · **Vocabulario:** 54 woorden · **Print:** 36 blz. · **Spellen:** 12

| § | Inhoud |
|---|---|
| §0 | ¡Ponte al día! |
| §1 | La infancia |
| §2 · 2.2 · 2.3 | El pretérito imperfecto · más práctica · ¿cómo era tu vida? |
| §3 · 3.2 | Contraste indefinido ↔ imperfecto · practicar |
| §4 · 4.2 | Comparativos + que · la frase con «que» + antes/ahora |
| §5 | Lectura «El pueblo de mi abuela» |
| T | Taller de lengua |
| §6 | **Lectura** «Carta de la abuela Rosario» — carta manuscrita |
| §7 | **Escucha** Pódcast «Antes y ahora» — twee kindertijden vergeleken |
| C · ★ · ✓ · V | Cultura (la infancia en el mundo hispano) · Tarea · Repaso · Vocabulario |

**Getypte drills:** el imperfecto · indefinido of imperfecto · comparar

**Onderwerpen voor de bronnenlijst**
- `§2 · El pretérito imperfecto`
- `§3 · Contraste — indefinido o imperfecto`
- `§4 · Los comparativos — más/menos… que, tan… como, mejor, peor`
- `§4b · La frase de relativo con «que»`
- `La infancia y los juguetes` · `La escuela de antes` · `Antes y ahora`
- `Cultura — la infancia en el mundo hispano`

**Wat de escape room moet testen** — decor: het dorp van de grootmoeder bij Cusco, een
fotoalbum zonder bijschriften, of een dag die verdween toen de weg kwam. Leerstof: het
imperfecto met zijn tildes, kiezen tussen indefinido en imperfecto op basis van de
signaalwoorden, en twee tijden vergelijken met más/menos… que.

---

## C6+ U7 «¡Opina y cuídate!» — parada **Costa Rica** 🇨🇷 · *einde van de ruta*

**Tarea final:** Mi cartel de opinión · **Vocabulario:** 54 woorden · **Print:** 34 blz. · **Spellen:** 12

| § | Inhoud |
|---|---|
| §0 | ¡Ponte al día! |
| §1 | La salud y el medio ambiente |
| §2 · 2.2 · 2.3 | El imperativo (tú) · el imperativo + enclíticos · un cartel de consejos |
| §3 · 3.2 | Opinar y argumentar · practicar la opinión |
| §4 · 4.2 | Conectores — argumentar · a favor y en contra |
| §5 | Lectura «Diez consejos para el planeta» |
| T | Taller de lengua |
| §6 | **Lectura** «Carta al director» — ingezonden brief |
| §7 | **Escucha** «En la consulta» — vier adviezen, één geweigerd |
| C · ★ · ✓ · V | Cultura (Costa Rica y la «pura vida») · Tarea · Repaso · Vocabulario |

**Getypte drills:** el imperativo · el imperativo + pronombre (mét de tilde) · los conectores

**Onderwerpen voor de bronnenlijst**
- `§2 · El imperativo afirmativo (tú)`
- `§2b · El imperativo + pronombres — cuídate, recíclalo`
- `§3 · Dar tu opinión — creo que, me parece que, (no) estoy de acuerdo`
- `§4 · Los conectores — porque, además, por eso, sin embargo`
- `La salud y los consejos` · `El medio ambiente y el reciclaje`
- `Cultura — Costa Rica y la «pura vida»`

**Wat de escape room moet testen** — decor: een gezondheidscentrum, een bos dat gekapt dreigt
te worden, of een schoolkrant met een deadline. Leerstof: adviezen geven met de imperativo,
het pronombre eraan plakken mét de juiste tilde, een mening onderbouwen, en de vier
conectores op hun plaats zetten. Sluitstuk van de ruta — mag terugblikken op Cartagena,
CDMX, Chile, Buenos Aires en Cusco.

> **Let op:** de vocabulariolijst van deze unit bevat **`deberías`**. Dat is een condicional
> en valt daarmee buiten de leerplanscope (CLAUDE.md §2). In de nieuwe drills en teksten heb
> ik het vermeden; zeg of je het uit de lijst wil halen.

---

## Openstaand

1. **Tarea final van C5 U7 en U8.** De print zegt «Mi barrio» en «Mis vacaciones»;
   CLAUDE.md §12 zegt «Mapa de mi barrio» en «Diario de viaje». Zeg welke klopt, dan trek ik
   het gelijk in de print, de LEESMIJ en CLAUDE.md.
2. **`deberías` in de vocabulariolijst van C6+ U7** is een condicional en valt buiten de
   leerplanscope. In de nieuwe drills en teksten vermeden; laat weten of het uit de lijst mag.
3. **De PowerPoints** missen nog de twee dia's §Lectura en §Escucha. De aanroep staat in alle
   dertien generatoren klaar; er is alleen `python-pptx` voor nodig, en dat kan pas
   geïnstalleerd worden als `pypi.org` in de toegestane domeinen van de omgeving staat.
