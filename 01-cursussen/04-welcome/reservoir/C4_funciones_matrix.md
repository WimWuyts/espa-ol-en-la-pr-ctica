# C4 · Matrix C — Funciones comunicativas (doorlopende, groeiende ruggengraat)

> **Wat dit is (PROTOTYPE, ter validatie 2026-07-27):** naast **matrix A** (klanken, spreiding) en
> **matrix B** (chunk-recycling) is dit de **derde spreidingsmatrix**: de *funciones comunicativas*
> die de leerling **gradueel opbouwt** over de units heen — steeds **vertrekkend vanuit de
> sitcom-fragmenten**. Bron van waarheid = `03-build/web/funciones_data.py`; leerlaag =
> `gen_c4_funciones.py` → tab «🗣️ Funciones» in elke hub.

## Principe
Een video toont geen losse woorden maar **taal in actie**: de personages *dóen* iets (groeten, naar
herkomst vragen, corrigeren, iets vragen, tellen…). Elke unit:
1. **extraheert** die functies uit de scène — «¿Qué hacen con el idioma?» (noticing);
2. voegt **nieuwe** functies toe én **uptrade't** bestaande (rijkere *exponentes*);
3. toont het **cumulatieve repertoire** (banco) met een **semáforo per functie**;
4. **tagt de eindtaak** met de functies die ze combineert (recycling zichtbaar).

## De catalogus (A1-kern, uit de fragmenten)
| ID | Función | NL | CEFR (A1) | Doelcode |
|----|---------|----|-----------|----------|
| F01 | Saludar y despedirse | groeten & afscheid | establecer contacto social | C4-GE-1 |
| F02 | Presentarse (decir quién soy) | jezelf voorstellen | presentarse | C4-SP-1 |
| F03 | Pedir y dar información personal | persoonlijke info vragen/geven | dar y pedir datos personales | C4-GE-1 |
| F04 | Reaccionar con cortesía | beleefd reageren | fórmulas de cortesía | C4-GE-2 |
| F05 | Preguntar y decir cómo estoy | vragen/zeggen hoe het gaat | preguntar/expresar el estado | C4-GE-1 |
| F06 | Pedir algo | iets vragen/bestellen | peticiones básicas | C4-GE-3 |
| F07 | Contar (números 0–20) | tellen | números | C4-WS-1 |
| F08 | Gestionar la comprensión | om verduidelijking vragen | estrategias de comprensión | C4-STR-1 |
| F09 | Hablar de la familia | over je familie praten | la familia y la posesión | C4-WS-1 |
| F10 | Describir a alguien | iemand beschrijven (fysiek/karakter) | descripción de personas | C4-SP-2 |
| F11 | Identificar objetos | voorwerpen benoemen (¿qué es esto?) | identificar cosas | C4-WS-1 |
| F12 | Decir qué hay y para qué sirve | zeggen wat er is / waarvoor iets dient | existencia y función | C4-WS-1 |
| F13 | Ubicar cosas · decir dónde está | situeren (¿dónde está? · preposiciones) | localización en el espacio | C4-TS-3 |
| F14 | Pedir y dar permiso | om toestemming vragen/geven (¿puedo…?) | pedir/dar permiso | C4-GE-2 |
| F15 | Hablar del trabajo | over je werk/beroep praten | profesión y lugar de trabajo | C4-SP-1 |
| F16 | Especular y adivinar | gissen & vermoedens uiten (puede ser…) | expresar hipótesis sencillas | C4-STR-1 |
| F17 | Decir y preguntar la hora | de tijd vragen & zeggen | la hora y los días | C4-WS-1 |
| F18 | Quedar con alguien | een afspraak maken | concertar una cita | C4-GE-3 |
| F19 | Hablar de planes | over plannen praten (ir a + inf.) | expresar planes e intenciones | C4-TS-4 |
| F20 | Expresar obligación | zeggen wat je moet doen (tener que + inf.) | expresar obligación | C4-TS-3 |
| F21 | Ofrecer y pedir ayuda | hulp aanbieden & vragen | ofrecer/pedir ayuda | C4-GE-3 |
| F22 | Decir lo que sé hacer | zeggen wat je kunt/weet te doen (saber + inf.) | expresar habilidad | C4-SP-2 |
| F23 | Comprar: precio, talla y cantidad | kopen: prijs, maat en hoeveelheid | transacción de compra | C4-SP-1 |
| F24 | Hablar del tiempo que hace | over het weer praten | describir el entorno | C4-WS-1 |
| F25 | Reaccionar con una exclamación | reageren met een uitroep | expresar una reacción | C4-GE-2 |
| F27 | Decir lo que te gusta y con qué frecuencia | zeggen wat je graag doet | expresar gustos y preferencias | C4-SP-2 |
| F28 | Hablar de cómo te sientes | zeggen hoe jij je voelt | sensaciones físicas | C4-GE-2 |
| F29 | Hablar de la rutina diaria | over je dagelijkse routine praten | acciones habituales (reflexivos) | C4-TS-4 |
| F30 | Preguntar y dar la razón | naar de reden vragen en ze geven | causa y consecuencia | C4-TS-3 |
| F31 | Desenvolverse en un restaurante | je redden in een restaurant | transacción de restaurante | C4-SP-1 |
| F32 | Mostrar acuerdo y desacuerdo | het eens of oneens zijn | expresar (des)acuerdo | C4-GE-2 |
| F33 | Valorar la comida y las personas | eten en mensen beoordelen | valorar con el superlativo | C4-SP-2 |

> **F26 (hotel) bestaat niet.** Ze was voorzien voor U13, maar geen van de
> veertien afleveringen speelt in een hotel: U13 gaat over de markt. Een functie
> in het repertoire zetten waar geen les bij hoort, zou de leerling laten zien
> dat hij iets «kan» dat hij nooit geleerd heeft. Reserveren komt in C5 terug.
> Het nummer blijft leeg om de andere niet te laten opschuiven.

## Matrix C — functie × unit (● intro · ▲ uptrade/nivel+ · · recycle)
| ID | U1 | U2 | U3 | U4 | U5 | … | Exponentes die groeien |
|----|----|----|----|----|----|----|------------------------|
| F01 Saludar/despedirse | ● | ▲ | · | · | · | | hola/adiós → buenos días/tardes/noches · ¡buenas! · hasta mañana |
| F02 Presentarse | ● | · | ▲ | ▲ | · | | me llamo/soy → **soy de + país** → **presentar a alguien (esta es mi madre)** |
| F03 Info personal | ● | · | ▲ | · | · | | ¿cómo te llamas? → **¿de dónde eres? ¿qué idiomas hablas?** |
| F04 Cortesía | | ● | · | · | · | | por favor · gracias · de nada · perdona |
| F05 Cómo estoy | | ● | · | | | | ¿cómo estás? · estoy bien/cansado-a · regular |
| F06 Pedir algo | | | ● | | ▲(bar) | | …, por favor · ¿me da…? → ¿me pones…? (U10) |
| F07 Contar 0–20 | | | ● | | · | | uno…veinte → precios (U11) · horas (U8) |
| F08 Gestionar comprensión | ● | ▲ | ▲ | · | · | | ¿cómo?/otra vez → ¿puedes repetir? → más despacio · no entiendo |
| F09 Hablar de la familia | | | | ● | · | | mi madre/padre · hermano-a · abuelo-a · tío-a · la hermana de María (de + nombre) |
| F10 Describir a alguien | | | | ● | · | | es alto-a/guapo-a · simpático-a/divertido-a · muy… · un poco… |
| F11 Identificar objetos | | | | | ● | · | ¿qué es esto? · esto es un/una… · esto son… · un/el · una/la |
| F12 Qué hay / para qué sirve | | | | | ● | · | ¿hay…? · (no) hay… → hay ↔ está (U6) · que sirve para + infinitivo |
| F13 Ubicar · dónde está | | | | | | ● | ¿dónde está? · encima/debajo/dentro/al lado de · del (de+el) |
| F14 Pedir y dar permiso | | | | | | ● | ¿puedo…? · ¿puedes…? · sí, puedes… · aquí no · puedes ir fuera |
| F15 Hablar del trabajo | | | | | | | ● (U7) — ¿a qué te dedicas? · soy profesor/a · trabajo en… (ser sin un/una) |
| F16 Especular y adivinar | | | | | | | ● (U7) — puede ser… · ¿trabaja en…? · creo que es… · ¡ya lo sé! |
| F17 Decir/preguntar la hora | | | | | | | ● (U8) — ¿qué hora es? · es la una ↔ son las… · y media/menos cuarto · ¿a qué hora? · el/los lunes |
| F18 Quedar con alguien | | | | | | | ● (U8) — ¿quieres quedar? · quedamos a las… ▲ (U9) quedar para + inf. · afwijzen |
| F19 Hablar de planes | | | | | | | ● (U9) — voy a / vas a / vamos a + infinitivo · ¿qué vas a hacer? |
| F20 Expresar obligación | | | | | | | ● (U9) — tengo que + infinitivo · tengo cosas que hacer · tengo hambre/sueño ▲ (U10) hay que + infinitivo (onpersoonlijk) · no tienes que molestarte |
| F21 Ofrecer y pedir ayuda | | | | | | | ● (U10) — yo te ayudo · ¿te ayudo? · ¿qué tengo que hacer? · no es molestia · déjame, lo hago yo |
| F22 Decir lo que sé hacer | | | | | | | ● (U10) — sé + infinitivo · ¿sabes…? · ¿sabes cómo funciona? · sabemos… · claro que sé |
| F23 Comprar (precio/talla) | | | | | | | ● (U12) — ¿cuánto cuesta? · ¿qué talla lleva? · me queda ancho/bien ▲ (U13) ¿cuánto cuestan? · un kilo · es una oferta · ¿dónde venden…? |
| F24 El tiempo que hace | | | | | | | ● (U11) — hace sol/frío/calor · está nublado · llueve · nieva · ¿qué tiempo hace? |
| F25 Exclamación | | | | | | | ● (U11) — ¡qué frío! · ¡qué calor! ▲ (U14) ¡qué rico! · ¡qué tensión! |
| F27 Gustos y frecuencia | | | | | | | ● (U11) — me/te/le gusta · me encanta · no soporto · prefiero · siempre…nunca |
| F28 Cómo te sientes | | | | | | | ● (U11) — tengo frío/calor/hambre/sueño ▲ (U13) estoy enfermo · no tienes buen aspecto · tienes que cuidarte |
| F29 La rutina diaria | | | | | | | ● (U12) — me levanto · me ducho · me peino · se afeita · os ducháis · me pongo la chaqueta |
| F30 Preguntar la razón | | | | | | | ● (U13) — ¿por qué…? · porque… · por eso… · no lo sé |
| F31 En el restaurante | | | | | | | ● (U14) — mesa para cuatro · ¿quiere algo de beber? · de primero/segundo/postre · les recomiendo · la cuenta |
| F32 Acuerdo y desacuerdo | | | | | | | ● (U14) — yo también · yo tampoco · yo sí · yo no · exacto |
| F33 Valorar (-ísimo) | | | | | | | ● (U14) — está buenísimo · es guapísimo · son simpatiquísimos · ¡qué rico! |

*(NB: F05 kreeg in U7 een ▲-uptrade: estamos todos bien · ¿estáis bien? · ser↔estar-contrast.
F07 en F08 kregen in U8 een ▲-uptrade: F07 números → **las horas** (y media · en veinte minutos) ·
F08 comprensión → **telefoonregister** (¿sí? · no te oigo nada · ¿puedes hablar más despacio?).)*

**Groei tot nu toe:** U1 = 4 functies · U2 = 6 (+cortesía, +cómo estoy) · U3 = 8 (+pedir algo, +contar) ·
U4 = 10 (+hablar de la familia, +describir a alguien; F02 uptrade → presentar a alguien) ·
U5 = 12 (+identificar objetos, +decir qué hay/para qué sirve) ·
U6 = 14 (+ubicar cosas/dónde está, +pedir y dar permiso) ·
U7 = 16 (+hablar del trabajo, +especular y adivinar; F05 uptrade → estamos/estáis) ·
U8 = 18 (+decir/preguntar la hora, +quedar; F07 uptrade → horas, F08 uptrade → teléfono) ·
U9 = 20 (+hablar de planes, +expresar obligación; F18 uptrade → quedar para + inf. / afwijzen) ·
U10 = **22** (+ofrecer y pedir ayuda, +decir lo que sé hacer; F20 uptrade → **hay que + infinitivo**
= onpersoonlijke verplichting náást het persoonlijke *tengo que*, en *no tienes que molestarte*).

## Noticing per unit («¿Qué hacen con el idioma?» — cita → función)
- **U1:** «¡Hola! ¿Qué tal?»→F01 · «Me llamo…»→F02 · «¿Cómo te llamas?»→F03 · «¿Cómo? Otra vez.»→F08
- **U2:** «Buenos días/tardes»→F01 · «¿Cómo estás?»→F05 · «Estoy ocupada/cansada»→F05 · «Adiós. Hasta luego.»→F01
- **U3:** «Buenas noches»→F01 · «¿De dónde eres? ¿De qué país?»→F03 · «Soy de Argelia. Eres argelina.»→F02 · «¿Habla usted francés?»→F03 · «Dinero, por favor.»→F06 · «Uno, dos, tres… veinte.»→F07
- **U4:** «Esta es mi madre.»→F02 · «Es muy elegante, pero un poco gorda.»→F10 · «Paula es la hermana de María.»→F09 · «El tío Fermín, el guapo de la familia.»→F09 · «Es muy alto y muy fuerte.»→F10
- **U5:** «¿Qué es esto?»→F11 · «Esto es un sofá.»→F11 · «Sirve para descansar.»→F12 · «¿Hay un ordenador?»→F12 · «Esto son mis llaves.»→F11
- **U6:** «Hay cosas encima de las sillas.»→F13 · «Debajo de la cama.»→F13 · «Dentro del frigorífico…»→F13 · «¿Puedo fumar?»→F14 · «Aquí no, pero puedes ir fuera.»→F14
- **U7:** «Puede ser escritora.»→F16 · «¿Trabaja en una tienda?»→F16 · «Es profesora.»→F15 · «Yo trabajo aquí, tú trabajas aquí.»→F15 · «Estamos todos bien.»→F05
- **U8:** «¿Qué hora es? ¿Las ocho y media?»→F17 · «¿A qué hora? Mejor a las doce.»→F17 · «¿Quieres quedar esta noche?»→F18 · «Quedamos en mi casa.»→F18 · «No te oigo nada. ¿Puedes hablar más despacio?»→F08 · «Te veo en veinte minutos.»→F07
- **U10:** «Yo te ayudo.»→F21 · «¿Qué tengo que hacer?»→F21 · «No es molestia.»→F21 · «Hay que limpiar esto.»→F20 · «¿Sabes pasar la aspiradora?»→F22 · «Los hombres también sabemos pasar la aspiradora.»→F22
- **U9:** «Voy a preparar café.»→F19 · «Vamos a dormir un poquito más.»→F19 · «Tengo que pasear al perro.»→F20 · «Tengo cosas que hacer.»→F20 · «¿Quedamos para ir al cine?»→F18 · «Tengo sueño. ¿No tienes sueño?»→F20

## Eindtaak-tags (recycling zichtbaar)
- **U1 «Mi presentación»** = F01 + F02 + F03
- **U2 «Un día de saludos»** = F01 + F05 + F04
- **U3 «Mi mapa»** = F02 + F03 + F08
- **U4 «Mi árbol de familia»** = F09 + F10 + F02
- **U5 «Diccionario de la clase»** = F11 + F12 + F10
- **U6 «Plano de mi casa»** = F13 + F12 + F14
- **U7 «¿Quién soy? · adivina»** = F15 + F16 + F03
- **U8 «Mi horario»** = F17 + F18 + F07
- **U9 «Mi finde»** = F19 + F20 + F18
- **U10 «¿Quién hace qué?»** = F21 + F22 + F20
- **U11 «El tiempo y mis vacaciones»** = F24 + F27 + F28
- **U12 «El desfile de la clase»** = F10 + F29 + F23
- **U13 «Mi lista de la compra»** = F23 + F07 + F30
- **U14 «La cena del año»** = F31 + F06 + F32 + F33

## Zeven ontwerpregels
1. **Video-afgeleid:** elke functie begint bij een citaat uit de scène (noticing), nooit abstract.
2. **Cumulatief zichtbaar:** het banco groeit; de leerling ziet «8/8 functies» aangroeien (zoals de kaart).
3. **Uptrade i.p.v. herhaling:** een gekende functie keert terug met **rijkere** exponentes (nivel +).
4. **Spreiding & recycling:** meta-functies (F08 comprensión, F04 cortesía) keren in **elke** interactie-unit terug.
5. **Eindtaak = combinatie:** elke tarea tagt ≥2 oude + de nieuwe functie (afzender·ontvanger·doel).
6. **Zelf-evaluatie per functie:** semáforo (🟢🟡🔴) op functieniveau, receptief/productief apart mogelijk.
7. **CEFR + doelcode op de docentenpagina:** de leerlingpagina toont enkel función + exponentes + CEFR-chip; de codes staan hier (docentdossier).

## Uitbreiden of bijstellen
Voeg in `funciones_data.py` bij bestaande functies een nieuwe `exp[<unit>]` (= uptrade) of een nieuwe
functie met `exp[<intro-unit>]`, vul `NOTICING[<unit>]` en `TAREA_FUN[<unit>]`. Herbouw
`gen_c4_funciones.py` per unit + de hub. Werk deze matrix bij.
