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

## Matrix C — functie × unit (● intro · ▲ uptrade/nivel+ · · recycle)
| ID | U1 | U2 | U3 | U4 | U5 | … | Exponentes die groeien |
|----|----|----|----|----|----|----|------------------------|
| F01 Saludar/despedirse | ● | ▲ | · | · | · | | hola/adiós → buenos días/tardes/noches · ¡buenas! · hasta mañana |
| F02 Presentarse | ● | · | ▲ | · | | | me llamo/soy → **soy de + país · soy [nacionalidad]** |
| F03 Info personal | ● | · | ▲ | · | | | ¿cómo te llamas? → **¿de dónde eres? ¿qué idiomas hablas?** |
| F04 Cortesía | | ● | · | · | · | | por favor · gracias · de nada · perdona |
| F05 Cómo estoy | | ● | · | | | | ¿cómo estás? · estoy bien/cansado-a · regular |
| F06 Pedir algo | | | ● | | ▲(bar) | | …, por favor · ¿me da…? → ¿me pones…? (U10) |
| F07 Contar 0–20 | | | ● | | · | | uno…veinte → precios (U11) · horas (U8) |
| F08 Gestionar comprensión | ● | ▲ | ▲ | · | · | | ¿cómo?/otra vez → ¿puedes repetir? → más despacio · no entiendo |

**Groei tot nu toe:** U1 = 4 functies · U2 = 6 (+cortesía, +cómo estoy) · U3 = 8 (+pedir algo, +contar).

## Noticing per unit («¿Qué hacen con el idioma?» — cita → función)
- **U1:** «¡Hola! ¿Qué tal?»→F01 · «Me llamo…»→F02 · «¿Cómo te llamas?»→F03 · «¿Cómo? Otra vez.»→F08
- **U2:** «Buenos días/tardes»→F01 · «¿Cómo estás?»→F05 · «Estoy ocupada/cansada»→F05 · «Adiós. Hasta luego.»→F01
- **U3:** «Buenas noches»→F01 · «¿De dónde eres? ¿De qué país?»→F03 · «Soy de Argelia. Eres argelina.»→F02 · «¿Habla usted francés?»→F03 · «Dinero, por favor.»→F06 · «Uno, dos, tres… veinte.»→F07

## Eindtaak-tags (recycling zichtbaar)
- **U1 «Mi presentación»** = F01 + F02 + F03
- **U2 «Un día de saludos»** = F01 + F05 + F04
- **U3 «Mi mapa»** = F02 + F03 + F08

## Zeven ontwerpregels
1. **Video-afgeleid:** elke functie begint bij een citaat uit de scène (noticing), nooit abstract.
2. **Cumulatief zichtbaar:** het banco groeit; de leerling ziet «8/8 functies» aangroeien (zoals de kaart).
3. **Uptrade i.p.v. herhaling:** een gekende functie keert terug met **rijkere** exponentes (nivel +).
4. **Spreiding & recycling:** meta-functies (F08 comprensión, F04 cortesía) keren in **elke** interactie-unit terug.
5. **Eindtaak = combinatie:** elke tarea tagt ≥2 oude + de nieuwe functie (afzender·ontvanger·doel).
6. **Zelf-evaluatie per functie:** semáforo (🟢🟡🔴) op functieniveau, receptief/productief apart mogelijk.
7. **CEFR + doelcode op de docentenpagina:** de leerlingpagina toont enkel función + exponentes + CEFR-chip; de codes staan hier (docentdossier).

## Uitbreiden naar U4+
Voeg in `funciones_data.py` bij bestaande functies een nieuwe `exp[<unit>]` (= uptrade) of een nieuwe
functie met `exp[<intro-unit>]`, vul `NOTICING[<unit>]` en `TAREA_FUN[<unit>]`. Herbouw
`gen_c4_funciones.py` per unit + de hub. Werk deze matrix bij.
