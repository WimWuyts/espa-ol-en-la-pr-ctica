# Español en la práctica — C5

## Native Exercise Integration Blueprint voor Claude Code Web

**Versie:** 1.0  
**Scope:** U0–U8 · `C5_deel1_U0U4.zip` + `C5_deel2_U5U8.zip`  
**Doel:** inhoudsaudit, bronmapping en exacte implementatie van dertien nieuwe native oefeningen  
**Totaal nieuwe oefeningen:** 13  
**Totaal nieuwe items:** 215  

---

# 0. Opdracht aan Claude Code Web

Lees vóór elke wijziging alle bestaande bestanden van de betrokken unit:

1. `1-PDF_bewerkbare-laag_U<N>.html`;
2. `2-HTML-hub_U<N>.html`;
3. indien aanwezig de buildbron waaruit PDF en PowerPoints worden gegenereerd;
4. `LEESMIJ.md`.

Voer daarna uitsluitend de aanvullingen uit die in hoofdstuk 4 en 5 van dit dossier staan.

## Niet-onderhandelbare bouwregels

- Behoud de bestaande groene huisstijl, typografie, navigatie, cast, route, componentnamen en offline werking.
- Verwijder of herschrijf geen bestaande oefening.
- Voeg geen futuro simple, condicional of subjuntivo toe.
- Gebruik de nieuwe oefening-ID’s exact zoals opgegeven.
- De hier opgenomen Spaanse zinnen, prompts, opties en antwoorden zijn de canonieke nieuwe inhoud.
- Iedere digitale oefening is volledig native HTML/CSS/JavaScript: geen iframe, externe widget, LearningApps-embed of afhankelijkheid van de bronsite.
- Iedere digitale oefening werkt offline.
- Zelfcorrigerende oefeningen hebben:
  - één antwoord per item;
  - directe maar niet storende feedback;
  - knop `Comprobar`;
  - knop `Reintentar`;
  - score als `x / n`;
  - toetsenbordbediening;
  - zichtbare focus;
  - ARIA-labels;
  - diakritiekvriendelijke vergelijking;
  - behoud van correcte antwoorden bij `Reintentar`;
  - geen straf voor hoofdlettergebruik tenzij orthografie het leerdoel is.
- Gebruik `↻ Otra serie` alleen waar in dit dossier meerdere reeksen of randomisering worden gevraagd. De set blijft altijd exact even groot als het opgegeven itemaantal.
- Printoefeningen worden toegevoegd aan de bewerkbare cursuslaag en moeten bij hergeneratie ook in de PDF verschijnen.
- Voeg printoefeningen niet als verkleinde schermafbeelding toe, maar als echte HTML met selecteerbare tekst.
- Zet oplossingen niet in de leerlingweergave. Voeg ze toe aan de docent-PowerPoint en aan de bestaande digitale oplossingslogica.
- Actualiseer interne oefeningentellers, navigatie, eventuele voortgangsbalken, ankerlinks en metadata.
- Wijzig bestaande QR-doelen niet. Nieuwe printoefeningen die naar de hub verwijzen, gebruiken het bestaande QR-component en een nieuw stabiel anker.
- Gebruik bronvermelding alleen in ontwikkelaarsdocumentatie. Toon de naam of vormgeving van de externe website niet aan leerlingen.

## Auteursrechtelijke regel

De externe pagina’s zijn uitsluitend gebruikt om oefentype en omvang te analyseren. Deze blueprint bevat nieuwe, zelfstandig geschreven items. Kopieer geen afbeeldingen, werkbladen, zinnen, antwoordformuleringen, CSS, JavaScript of huisstijl van de bronsite.

---

# 1. Uitgebreide inhoudstafel van de bestaande cursus

## Overkoepelende leerlijn

| Unit | Titel en route | Communicatieve kern | Grammatica | Woordenschat en cultuur | Bestaande eindtaak |
|---|---|---|---|---|---|
| U0 | **¡Empezamos!** · Spanje en de Spaanstalige wereld | begroeten, afscheid nemen, spellen, klascommunicatie, leeftijd en telefoonnummer geven | alfabet, klank-tekenkoppeling, klemtoon, tilde, getallen 0–100 | metataal, begroetingen, beleefdheid, klastaal, landen en variatie | `Tu tarjeta de embarque` |
| U1 | **¿Quién eres?** · Madrid | persoonlijke informatie vragen en geven, formulieren invullen, iemand voorstellen | `ser`, regelmatig presente, vraagwoorden, lidwoorden, genus/getal, hoofdletters, `y/e`, `o/u`, `porque` | persoonsgegevens, formulieren, landen, nationaliteiten, begroetingen | `Mi pasaporte` |
| U2 | **Mi gente** · Andalusië/Sevilla | familie voorstellen, uiterlijk en karakter beschrijven, toestand benoemen | `tener`, possessiva, adjectiefcongruentie, `ser/estar`, `este/ese` | familie, uiterlijk, lichaam, kleuren, karakter | `Álbum de familia` |
| U3 | **El tiempo vuela** · Barcelona | tijd zeggen, routine en weekplanning beschrijven, frequentie uitdrukken | reflexieve werkwoorden, presente met stamwisseling, `hacer/ir/salir`, tijdsconnectors | kloktijd, dagelijkse routine, dagen, maanden, seizoenen, frequentie | `Un día en mi vida` |
| U4 | **Me gusta** · València en de kust | voorkeuren, reacties en meningen geven; voorstellen doen en afspreken | `gustar/encantar`, indirecte voornaamwoorden, `querer/poder`, `porque`, verbindingswoorden | sport, vrije tijd, muziek, film, gevoelens, frequentie | `Mi playlist` |
| U5 | **¡Ñam!** · Mexico-Stad | hoeveelheden uitdrukken, plannen maken, bestellen, boodschappen en recepten bespreken | `mucho/a/os/as`, `ir a + infinitivo`, lijdend-voorwerpspronomen, sequentieconnectors | eten, fruit, groenten, dranken, tafel, restaurant, verpakkingen, smaken | `La carta` |
| U6 | **De tiendas** · Mexicaanse markten | kleding beschrijven, winkelen, verwijzen zonder herhaling, recente handeling benoemen | `lo/la/los/las`, `acabar de`, demonstrativa, adjectiefcongruentie, klemtoonfamilies | kleding, schoenen, accessoires, kleuren, patronen, materialen, winkels, kopen | `Abre tu tienda` |
| U7 | **Mi casa y mi barrio** · Cartagena | huis en buurt beschrijven, plaats bepalen, zeggen wat iemand doet, de weg wijzen | `hay/estar`, plaatsvoorzetsels, `estar + gerundio`, affirmatieve tú-imperatief, ordinalen | woning, kamers, meubels, stad, richtingen, vervoer | `Mapa de mi barrio` |
| U8 | **¿Qué has hecho?** · Cusco en Machu Picchu | ervaringen en recente gebeurtenissen vertellen, reisdagboek schrijven, weer bespreken | pretérito perfecto compuesto, participia, `ya/todavía no`, weerconstructies, diakritische tilde | reizen, vakantie, weer, vervoer, ervaringen, Peru | `Diario de viaje` |

## U0 · ¡Empezamos!

1. Instap en herkenning van de Spaanstalige wereld.
2. Alfabet:
   - de 27 letters;
   - spellen van naam en e-mailadres;
   - letter-klankrelaties.
3. Uitspraak:
   - klinkers;
   - `b/v`;
   - stille `h`;
   - `g/j`;
   - `c/z/s`;
   - `r/rr`;
   - minimale paren en microdictee.
4. Klemtoon en tilde:
   - lettergrepen;
   - agudas, llanas en esdrújulas als voorbereidende logica;
   - hoorbare en geschreven klemtoon.
5. Getallen:
   - 0–15;
   - 16–29;
   - tientallen en `y`;
   - 30–100;
   - leeftijd en telefoonnummer.
6. Functies:
   - begroeten en afscheid nemen;
   - naam vragen en geven;
   - vragen hoe iets gespeld wordt;
   - elementaire klastaal;
   - beleefd reageren.
7. Cultuur:
   - waar Spaans gesproken wordt;
   - Spanje tegenover Hispano-Amerika;
   - beperkte regionale woordvariatie.
8. Eindtaak: boardingcard voorbereiden en mondeling presenteren.

## U1 · ¿Quién eres?

1. Herhaling U0: groeten, spellen, getallen en klastaal.
2. Persoonsfiche van Lucía en patroon van een zelfpresentatie.
3. `ser`: vormen, persoonsherkenning en toepassing.
4. Regelmatige werkwoorden op `-ar`, `-er`, `-ir`.
5. Vraagvorming en vraagwoorden.
6. Bepaalde en onbepaalde lidwoorden.
7. Genus en getal.
8. Hoofdletters bij landen en nationaliteiten.
9. Connectors: `y/e`, `o/u`, `porque`.
10. Lezen van profielen en grafieken.
11. Woordenschat:
    - 19 woorden persoonsgegevens;
    - 7 formulierwoorden;
    - 7 vraagwoorden;
    - 6 begroetingen;
    - 22 woorden bij Spaanstalige landen en nationaliteiten;
    - 25 landen van de wereld.
12. Eindtaak: persoonlijk paspoort.

## U2 · Mi gente

1. Herhaling presente, `ser/tener`, getallen en klastaal.
2. Familieleden en familieboom.
3. `tener`: vormen en bezit/familierelaties.
4. Possessiva:
   - `mi/tu/su/nuestro`;
   - enkelvoud en meervoud;
   - congruentie met het bezetene.
5. Uiterlijke beschrijving:
   - haar;
   - ogen;
   - basislichaam;
   - kleuren.
6. Adjectiefcongruentie op `-o/-a/-os/-as`.
7. Adjectieven op `-e` en medeklinker.
8. Karaktereigenschappen.
9. Contrast `ser/estar`.
10. Demonstrativa `este/ese`.
11. Lezen, beschrijven en raden wie bedoeld wordt.
12. Woordenschat: 22 familie, 17 uiterlijk, 6 kleuren, 10 karakter, 5 lichaam en 9 functiewoorden.
13. Eindtaak: familiealbum.

## U3 · El tiempo vuela

1. Herhaling getallen, regelmatig presente, `ser/tener` en weekdagen.
2. Kloktijd:
   - `es la/son las`;
   - `y cuarto/y media/menos cuarto`;
   - dagdelen.
3. Dagelijkse handelingen en ordening van een routine.
4. Reflexieve voornaamwoorden `me/te/se`.
5. Reflexieve werkwoorden in presente.
6. Stamwisselingen:
   - `o → ue`;
   - `e → ie`;
   - `e → i`.
7. Onregelmatige ik-vormen van `hacer`, `ir`, `salir`.
8. Frequentieadverbia.
9. Dagen, maanden en seizoenen.
10. Tijdsconnectors: `primero`, `después`, `luego`, `por fin`.
11. Lees- en spreekketen over Pau en de eigen routine.
12. Woordenschat: 18 klok, 17 routine, 11 onregelmatige werkwoorden, 9 frequentie, 16 kalender/seizoenen.
13. Eindtaak: een dag uit het eigen leven.

## U4 · Me gusta

1. Herhaling vrije tijd, presente en frequentie.
2. Omgekeerde constructie met `gustar`.
3. `gusta/gustan` en `encanta/encantan`.
4. Indirecte voornaamwoorden in voorkeurzinnen.
5. Reageren: instemmen, tegenspreken en nuanceren.
6. `querer` en `poder`.
7. Voorstellen, accepteren, weigeren en afspreken.
8. Reden en mening met `por qué/porque`.
9. Connectors: `y`, `también`, `pero`, `además`, `sobre todo`.
10. Liedrecensie en klassikale playlist.
11. Woordenschat: 12 voorkeur/mening, 11 sport/vrije tijd, 12 muziek/film, 8 gevoelens, 7 frequentie, 8 afspreken, 6 València/kust.
12. Eindtaak: eigen playlist.

## U5 · ¡Ñam!

1. Herhaling eten in presente en prijzen.
2. Hoeveelheid en congruentie met `mucho/a/os/as`.
3. Telbaar tegenover niet-telbaar.
4. Verpakkingen en hoeveelheden koppelen aan producten.
5. Nabije toekomst met `ir a + infinitivo`.
6. Restaurantfuncties:
   - ober tegenover klant;
   - bestellen;
   - beleefd vragen;
   - dialoogvolgorde.
7. Lijdend-voorwerpspronomen `lo/la/los/las`.
8. Recepten en volgordeconnectors.
9. Orthografie van `n/ñ`.
10. Woordenschat: 11 basiseten, 7 fruit, 7 groenten, 6 dranken, 7 tafel, 9 restaurant, 6 hoeveelheden/verpakkingen, 7 beleefd bestellen, 8 Mexicaanse/Latijns-Amerikaanse smaken.
11. Eindtaak: menukaart.

## U6 · De tiendas

1. Herhaling kleding, prijzen, lidwoorden en presente.
2. Lijdend-voorwerpspronomen:
   - referent herkennen;
   - plaats in de zin;
   - herhaling vermijden.
3. Recente handeling met `acabar de + infinitivo`.
4. Demonstrativa volgens afstand:
   - `este`;
   - `ese`;
   - `aquel`;
   - genus en getal.
5. Adjectiefcongruentie bij kleding, kleur en materiaal.
6. Winkeldialogen, wijzen, vragen en reageren.
7. Klemtoon: agudas, llanas en esdrújulas.
8. Connectors: `y/e`, `o/u`, `pero/sino`, `así que/por eso`.
9. Woordenschat: 13 kleding, 11 schoeisel/accessoires, 12 kleuren, 12 vorm/materiaal/patroon, 9 winkels, 11 winkeltaal, 12 koopwerkwoorden, 6 Mexico/duurzame mode.
10. Eindtaak: eigen winkel openen.

## U7 · Mi casa y mi barrio

1. Herhaling wonen, ordinalen, presente, `ser/estar` en eten/winkels.
2. Contrast `hay` tegenover `está/están`.
3. Kamers, meubels en plaatsvoorzetsels.
4. `estar + gerundio`.
5. Richtingen en affirmatieve tú-imperatief.
6. Luisteren en route volgen.
7. Ordinalen en apocope `primero → primer`.
8. Plaatsconnectors.
9. Diftongen, hiatus en tilde.
10. Woordenschat: 12 huis, 7 kamers, 11 meubels, 13 buurt/stad, 10 richtingen, 5 vervoer, 8 voorzetsels.
11. Eindtaak: buurtkaart.

## U8 · ¿Qué has hecho?

1. Herhaling presente, `haber`, locaties en ervaringen.
2. Pretérito perfecto compuesto:
   - vormen van `haber`;
   - regelmatige participia;
   - frequente onregelmatige participia;
   - omzetting van presente naar perfecto.
3. `ya`, `todavía no` en ervaringsvragen.
4. Weer:
   - `hace`;
   - `está`;
   - weerwerkwoorden.
5. Reisvolgorde en dagboekconnectors.
6. Diakritische tilde.
7. Woordenschat: 16 reis/vakantie, 16 weer, 10 vervoer, 10 ervaringen/markeerders, 8 participia, 4 Peru-route.
8. Eindtaak: reisdagboek.

---

# 2. Audit van de bestaande oefeningen

De printcursus bevat ongeveer 48–56 benoemde activiteiten per unit. De digitale hubs bevatten daarnaast flashcards, zelfcorrectie, visuele grammatica en 17–20 spelmodules per unit.

## Sterktes

- Duidelijke opbouw van herkennen naar produceren en communiceren.
- Veel herhaling tussen units.
- Goede spreiding over lezen, luisteren, schrijven, spreken en interactie.
- Sterke combinatie van print en digitale zelfcorrectie.
- Consequente cast en reisroute.
- Voldoende variatie: cloze, classificeren, ordenen, koppelen, dictee, simulatie, info-gap en spraakopname.

## Gerichte aanvulling

De nieuwe set vermijdt simpele duplicatie en versterkt vooral:

- retrieval met grotere gesloten itemsets;
- systematische contrasttraining;
- langere reeksen binnen één grammaticaal doel;
- woordenschat in concrete functies;
- automatische foutdiagnose;
- overdracht naar de vaste personages en route.

---

# 3. Geselecteerde externe oefenmodellen

| ID | Unit | Geanalyseerd oefenmodel | Vastgesteld aantal | Nieuwe native omzetting | Platform |
|---|---:|---|---:|---|---|
| C5-U0-NAT-01 | U0 | Los números del 0 al 10 | 11 | getal ↔ woord, één item per getal | digitale hub |
| C5-U0-NAT-02 | U0 | Los números del 10 al 20 | 11 | luister/lees en kies het cijfer | digitale hub |
| C5-U1-NAT-01 | U1 | Nacionalidades de los países hispanohablantes | 20 | clue-quiz met 20 landen/nationaliteiten | digitale hub |
| C5-U2-NAT-01 | U2 | Adjetivos posesivos | 8 | herschrijf met possessivum | printcursus |
| C5-U3-NAT-01 | U3 | 20 verbos reflexivos | 20 | routinewerkwoord ↔ context | digitale hub |
| C5-U4-NAT-01 | U4 | 25 frases para practicar `gustar` y similares | 25 | completeer met pronomen + `gusta(n)/encanta(n)` | digitale hub |
| C5-U5-NAT-01 | U5 | 20 verbos para cocinar | 20 | kookhandeling ↔ betekenis/context | digitale hub |
| C5-U5-NAT-02 | U5 | Completa con 20 adjetivos sobre la comida | 20 | kies passend smaak-/textuuradjectief | printcursus |
| C5-U6-NAT-01 | U6 | 20 verbos para hablar sobre la ropa | 20 | kledinghandeling ↔ situatie | digitale hub |
| C5-U6-NAT-02 | U6 | 25 palabras relacionadas con la moda | 25 | modewoord ↔ definitie/categorie | digitale hub |
| C5-U7-NAT-01 | U7 | Sopa de letras: 15 palabras relacionadas con la casa | 15 | native woordzoeker met exact 15 woorden | digitale hub |
| C5-U7-NAT-02 | U7 | 25 frases para practicar el imperativo | 25 | route- en huisinstructies in tú-imperatief | printcursus + hubcontrole |
| C5-U8-NAT-01 | U8 | 20 frases para practicar el pretérito perfecto | 20 | perfecto binnen de eigen reisroute | digitale hub |

**Rekensom:** 11 + 11 + 20 + 8 + 20 + 25 + 20 + 20 + 20 + 25 + 15 + 25 + 20 = **215 items**.

## Geverifieerde bronpagina’s

- U0: [Los números del 0 al 10](https://paginadelespanol.com/los-numeros-del-0-al-10/) en [Los números del 10 al 20](https://paginadelespanol.com/los-numeros-del-10-al-20/).
- U1: [Nacionalidades de los países hispanohablantes](https://paginadelespanol.com/nacionalidades-de-los-paises-hispanohablantes/).
- U2: [Adjetivos posesivos](https://paginadelespanol.com/adjetivos-posesivos/).
- U3: [20 verbos reflexivos](https://paginadelespanol.com/utiliza-estos-verbos-reflexivos/).
- U4: [25 frases para practicar el verbo “gustar” y similares](https://paginadelespanol.com/25-frases-para-practicar-el-verbo-gustar-y-similares/).
- U5: [20 verbos para cocinar](https://paginadelespanol.com/20-verbos-cocinar-espanol/) en [20 adjetivos sobre la comida](https://paginadelespanol.com/completa-frases-con-adjetivos-comida/).
- U6: [20 verbos para hablar sobre la ropa](https://paginadelespanol.com/20-verbos-para-hablar-sobre-la-ropa/) en [25 palabras relacionadas con la moda](https://paginadelespanol.com/25-palabras-relacionadas-con-la-moda/).
- U7: [Sopa de letras: 15 palabras relacionadas con la casa](https://paginadelespanol.com/sopa-de-letras-15-palabras-relacionadas-con-la-casa/) en [25 frases para practicar el imperativo](https://paginadelespanol.com/25-frases-para-practicar-el-imperativo/).
- U8: [20 frases para practicar el pretérito perfecto](https://paginadelespanol.com/20-frases-para-practicar-el-preterito-perfecto/).

---

# 4. Plaatsingsplan

| ID | Exacte invoeglocatie | Presentatie |
|---|---|---|
| C5-U0-NAT-01 | U0-hub, paneel `Vocabulario`, na bestaande getallenflashcards en vóór bredere getallenspellen | 11 tegelitems; cijfer als prompt, vier woordopties |
| C5-U0-NAT-02 | U0-hub, paneel `Juegos`, direct na C5-U0-NAT-01 | 11 luister-/leesitems; TTS-knop + vier cijfers |
| C5-U1-NAT-01 | U1-hub, paneel `Cultura` of `Extra`, na landen/nationaliteiten | kaart- of clue-quiz met 20 items |
| C5-U2-NAT-01 | U2-bewerkbare cursuslaag, na §2.2 en vóór de eerste vrije familieproductie | compacte tabel met acht herschrijvingen |
| C5-U3-NAT-01 | U3-hub, paneel `Vocabulario`, na routineflashcards | match/keuze, twintig contexten |
| C5-U4-NAT-01 | U4-hub, paneel `Gramática`, na de eerste bestaande `gusta/gustan`-oefening en vóór vrije productie | 25-item adaptieve cloze |
| C5-U5-NAT-01 | U5-hub, paneel `Vocabulario`, na eten/ingrediënten en vóór receptvolgorde | twintig kookhandelingen, icoon optioneel |
| C5-U5-NAT-02 | U5-bewerkbare cursuslaag, na de smaakwoordenschat en vóór `Escribe tu mini-receta` | woordbank + twintig zinnen |
| C5-U6-NAT-01 | U6-hub, paneel `Vocabulario`, na kledingflashcards | twintig korte situaties |
| C5-U6-NAT-02 | U6-hub, paneel `Extra`, na `describe tu ropa` | 25-item begrippensprint |
| C5-U7-NAT-01 | U7-hub, paneel `Juegos`, na meubels en kamers | gegenereerde woordzoeker met exact vijftien doelwoorden |
| C5-U7-NAT-02 | U7-bewerkbare cursuslaag, na §4.1 en vóór `Ordena las instrucciones` | 25 cloze-items; vijf themablokken |
| C5-U8-NAT-01 | U8-hub, paneel `Gramática`, na participia en vóór de communicatieve ervaringsketen | twintig cloze-items |

---

# 5. Canonieke oefeninhoud

## C5-U0-NAT-01 · Los números del 0 al 10

**Platform:** digitale hub  
**Aantal:** exact 11  
**Instructie leerling:** `Elige la palabra correcta para cada número.`  
**Mechaniek:** vierkeuze; presenteer alle elf items in willekeurige volgorde. Gebruik per afleider een ander woord uit dezelfde set.

| # | Prompt | Correct antwoord |
|---:|---:|---|
| 1 | 0 | cero |
| 2 | 1 | uno |
| 3 | 2 | dos |
| 4 | 3 | tres |
| 5 | 4 | cuatro |
| 6 | 5 | cinco |
| 7 | 6 | seis |
| 8 | 7 | siete |
| 9 | 8 | ocho |
| 10 | 9 | nueve |
| 11 | 10 | diez |

**Feedbackregel:** bij fout antwoord: `Mira otra vez la forma escrita del número.`  
**Anker:** `#c5-u0-nat-01`

## C5-U0-NAT-02 · Los números del 10 al 20

**Platform:** digitale hub  
**Aantal:** exact 11  
**Instructie leerling:** `Escucha o lee el número y elige la cifra correcta.`  
**Mechaniek:** toon het getalwoord, voorzie een TTS-knop, en bied vier cijfers aan. Afleiders komen uit dezelfde set.

| # | Prompt/TTS | Correct antwoord |
|---:|---|---:|
| 1 | diez | 10 |
| 2 | once | 11 |
| 3 | doce | 12 |
| 4 | trece | 13 |
| 5 | catorce | 14 |
| 6 | quince | 15 |
| 7 | dieciséis | 16 |
| 8 | diecisiete | 17 |
| 9 | dieciocho | 18 |
| 10 | diecinueve | 19 |
| 11 | veinte | 20 |

**Feedbackregel:** markeer de accentvorm in `dieciséis` pas na controle.  
**Anker:** `#c5-u0-nat-02`

## C5-U1-NAT-01 · Pasaporte hispano: país y nacionalidad

**Platform:** digitale hub  
**Aantal:** exact 20  
**Instructie leerling:** `Lee la pista y escribe la nacionalidad en masculino singular.`  
**Mechaniek:** tekstinvoer; accepteer hoofdlettervarianten, maar geen verkeerd accent. Toon na correctie ook de vrouwelijke vorm.

| # | Pista | Antwoord m. | Toon ook |
|---:|---|---|---|
| 1 | Lucía vive en Madrid. Es de España. | español | española |
| 2 | Diego vive en Ciudad de México. Es de México. | mexicano | mexicana |
| 3 | Valen vive en Cartagena. Es de Colombia. | colombiano | colombiana |
| 4 | Nina vive en Cusco. Es de Perú. | peruano | peruana |
| 5 | Mateo vive en Buenos Aires. Es de Argentina. | argentino | argentina |
| 6 | Una persona de Chile es… | chileno | chilena |
| 7 | Una persona de Uruguay es… | uruguayo | uruguaya |
| 8 | Una persona de Paraguay es… | paraguayo | paraguaya |
| 9 | Una persona de Bolivia es… | boliviano | boliviana |
| 10 | Una persona de Ecuador es… | ecuatoriano | ecuatoriana |
| 11 | Una persona de Venezuela es… | venezolano | venezolana |
| 12 | Una persona de Panamá es… | panameño | panameña |
| 13 | Una persona de Costa Rica es… | costarricense | costarricense |
| 14 | Una persona de Nicaragua es… | nicaragüense | nicaragüense |
| 15 | Una persona de Honduras es… | hondureño | hondureña |
| 16 | Una persona de El Salvador es… | salvadoreño | salvadoreña |
| 17 | Una persona de Guatemala es… | guatemalteco | guatemalteca |
| 18 | Una persona de Cuba es… | cubano | cubana |
| 19 | Una persona de la República Dominicana es… | dominicano | dominicana |
| 20 | Una persona de Puerto Rico es… | puertorriqueño | puertorriqueña |

**Feedbackregel:** geef na een fout eerst alleen de beginletter; geef na een tweede fout de laatste drie letters.  
**Anker:** `#c5-u1-nat-01`

## C5-U2-NAT-01 · Cambia la frase con un posesivo

**Platform:** printcursus  
**Aantal:** exact 8  
**Instructie leerling:** `Sustituye la parte en negrita por el adjetivo posesivo correcto. Escribe la frase completa.`  
**Layout:** drie kolommen: nummer, zin, schrijflijn. Zet geen antwoordbank in de leerlingversie.

1. La madre **de Lucía** trabaja en Sevilla.  
2. Los primos **de nosotros** viven en Granada.  
3. La mascota **de ti** es muy curiosa.  
4. Las fotos **de mí** están en el álbum.  
5. El hermano **de Mateo** tiene diecisiete años.  
6. Los abuelos **de vosotros** son muy simpáticos.  
7. La casa **de Valen y su familia** está en Cartagena.  
8. Las amigas **de Nina** son peruanas.

**Oplossingen docent:**

1. Su madre trabaja en Sevilla.
2. Nuestros primos viven en Granada.
3. Tu mascota es muy curiosa.
4. Mis fotos están en el álbum.
5. Su hermano tiene diecisiete años.
6. Vuestros abuelos son muy simpáticos.
7. Su casa está en Cartagena.
8. Sus amigas son peruanas.

**Printplaatsing:** nieuwe subsectie `§2.3 · Del nombre al posesivo`, direct na §2.2.  
**Hubverwijzing:** geen nieuw QR-blok nodig.

## C5-U3-NAT-01 · Veinte verbos reflexivos en contexto

**Platform:** digitale hub  
**Aantal:** exact 20  
**Instructie leerling:** `Lee la situación y elige el verbo reflexivo que corresponde.`  
**Mechaniek:** vierkeuze. Infinitieven worden eenmaal gebruikt; randomiseer de itemvolgorde en de opties.

| # | Situación | Antwoord |
|---:|---|---|
| 1 | Suena el despertador y abres los ojos. | despertarse |
| 2 | Sales de la cama. | levantarse |
| 3 | Entras bajo el agua por la mañana. | ducharse |
| 4 | Usas agua y jabón para la cara. | lavarse |
| 5 | Usas un cepillo para el pelo. | peinarse |
| 6 | Usas un cepillo y pasta para los dientes. | cepillarse |
| 7 | Te pones la ropa. | vestirse |
| 8 | Te pones los zapatos antes de salir. | calzarse |
| 9 | Miras tu imagen antes de salir. | mirarse |
| 10 | Dices tu nombre a una persona nueva. | presentarse |
| 11 | Tomas una silla en clase. | sentarse |
| 12 | Dejas de estar sentado. | ponerse de pie |
| 13 | Te vas de casa hacia el instituto. | marcharse |
| 14 | Ves a tus amigos en la plaza. | encontrarse |
| 15 | Lo pasas bien durante una actividad. | divertirse |
| 16 | No recuerdas dónde están las llaves. | olvidarse |
| 17 | Vuelves a casa después de clase. | regresar a casa |
| 18 | Te quitas la ropa antes de dormir. | desvestirse |
| 19 | Entras en la cama. | acostarse |
| 20 | Cierras los ojos y empiezas a dormir. | dormirse |

**Implementatienoot:** `ponerse de pie` en `regresar a casa` zijn controle-items. Toon na correctie: `No todos los verbos de una rutina son reflexivos.` Laat de leerling bij deze twee `no reflexivo` selecteren en daarna het juiste chunk kiezen. Het totaal blijft twintig.

**Anker:** `#c5-u3-nat-01`

## C5-U4-NAT-01 · Gustos en ruta

**Platform:** digitale hub  
**Aantal:** exact 25  
**Instructie leerling:** `Completa con el pronombre y la forma correcta: gusta, gustan, encanta o encantan.`  
**Mechaniek:** per item twee dropdowns: pronomen + werkwoordsvorm. Het antwoord telt pas als beide correct zijn.

| # | Zin met gaten | Pronomen | Werkwoord |
|---:|---|---|---|
| 1 | A Lucía ___ ___ bailar flamenco. | le | encanta |
| 2 | A Diego ___ ___ los mercados de su ciudad. | le | gustan |
| 3 | A Valen ___ ___ la música del Caribe. | le | encanta |
| 4 | A Nina ___ ___ las excursiones por la montaña. | le | encantan |
| 5 | A Mateo ___ ___ jugar al fútbol. | le | gusta |
| 6 | A mí ___ ___ las películas de aventuras. | me | gustan |
| 7 | A ti ___ ___ escuchar pódcast. | te | gusta |
| 8 | A nosotros ___ ___ las tardes en la playa. | nos | encantan |
| 9 | A vosotros ___ ___ quedar con amigos. | os | gusta |
| 10 | A ellas ___ ___ los conciertos pequeños. | les | gustan |
| 11 | A Lucía y a Nina ___ ___ cantar juntas. | les | gusta |
| 12 | A Diego no ___ ___ levantarse temprano. | le | gusta |
| 13 | A Valen ___ ___ las novelas gráficas. | le | encantan |
| 14 | A Mateo no ___ ___ la música electrónica. | le | gusta |
| 15 | A mí ___ ___ aprender palabras nuevas. | me | encanta |
| 16 | A ti no ___ ___ los deportes de riesgo. | te | gustan |
| 17 | A nuestra clase ___ ___ esta canción. | le | encanta |
| 18 | A mis amigos ___ ___ ir al cine. | les | gusta |
| 19 | A mi hermana ___ ___ los videojuegos. | le | encantan |
| 20 | A mis padres no ___ ___ conducir de noche. | les | gusta |
| 21 | A nosotros ___ ___ preparar una playlist. | nos | gusta |
| 22 | A vosotros ___ ___ las actividades culturales. | os | encantan |
| 23 | A usted ___ ___ el jazz. | le | gusta |
| 24 | A ustedes ___ ___ las fiestas populares. | les | gustan |
| 25 | A la profesora ___ ___ nuestras recomendaciones. | le | encantan |

**Foutdiagnose:**

- correct pronomen, fout werkwoord: `Mira lo que gusta: ¿singular, plural o infinitivo?`
- fout pronomen, correct werkwoord: `Mira a quién le gusta.`
- beide fout: toon beide hints, zonder oplossing.

**Anker:** `#c5-u4-nat-01`

## C5-U5-NAT-01 · Veinte acciones en la cocina

**Platform:** digitale hub  
**Aantal:** exact 20  
**Instructie leerling:** `Relaciona cada instrucción con el verbo de cocina.`  
**Mechaniek:** vierkeuze of drag-and-drop met toetsenbordalternatief. Toon een eenvoudige eigen lijnicoonset indien al beschikbaar; geen externe beelden.

| # | Instrucción/contexto | Antwoord |
|---:|---|---|
| 1 | Hacer trozos pequeños con un cuchillo. | cortar |
| 2 | Quitar la piel de una patata o fruta. | pelar |
| 3 | Hacer trozos muy pequeños de cebolla. | picar |
| 4 | Pasar queso o zanahoria por un rallador. | rallar |
| 5 | Unir ingredientes con una cuchara. | mezclar |
| 6 | Mover con fuerza huevos o nata. | batir |
| 7 | Poner un líquido dentro de un recipiente. | verter |
| 8 | Poner sal, pimienta o especias. | sazonar |
| 9 | Cocinar un alimento dentro de agua muy caliente. | hervir |
| 10 | Cocinar en aceite muy caliente. | freír |
| 11 | Cocinar en una sartén con poco aceite. | saltear |
| 12 | Cocinar con calor seco dentro del horno. | hornear |
| 13 | Cocinar sobre una parrilla. | asar |
| 14 | Calentar comida con ondas en un aparato. | calentar en el microondas |
| 15 | Dejar que un alimento pierda calor. | enfriar |
| 16 | Poner un líquido fuera con ayuda de un colador. | escurrir |
| 17 | Probar una pequeña cantidad para controlar el sabor. | probar |
| 18 | Colocar la comida en platos antes de llevarla a la mesa. | servir |
| 19 | Poner una capa de salsa, aceite o huevo con un pincel. | untar |
| 20 | Poner una bebida o preparación en el frigorífico para que esté fría. | refrigerar |

**Feedbackregel:** toon na elk correct antwoord een korte modelzin in imperatief, bijvoorbeeld `Corta el tomate.` Gebruik alleen affirmatieve tú-vormen die in U7 later expliciet worden geanalyseerd; label ze hier als vaste receptchunks, niet als nieuwe grammatica.

**Anker:** `#c5-u5-nat-01`

## C5-U5-NAT-02 · ¿Cómo sabe y cómo está?

**Platform:** printcursus  
**Aantal:** exact 20  
**Instructie leerling:** `Completa cada frase con un adjetivo del banco. Usa cada palabra una sola vez.`  
**Woordbank:** `dulce · salado · ácido · amargo · picante · suave · fuerte · fresco · crujiente · cremoso · jugoso · seco · tierno · duro · frío · caliente · maduro · crudo · cocido · delicioso`

1. Este chocolate tiene mucho azúcar: es __________.
2. Las patatas llevan demasiada sal: están __________.
3. El limón es muy __________.
4. El café sin azúcar puede ser __________.
5. Esta salsa mexicana lleva mucho chile: es __________.
6. Este queso joven no tiene un sabor intenso: es __________.
7. Este queso curado tiene un sabor muy __________.
8. La ensalada se ha preparado hoy: está __________.
9. La tostada hace ruido al morderla: está __________.
10. La sopa tiene una textura lisa y espesa: está __________.
11. La naranja tiene mucho zumo: está __________.
12. Este bizcocho necesita más leche: está demasiado __________.
13. La carne se corta fácilmente: está __________.
14. No puedo cortar este pan viejo: está muy __________.
15. El gazpacho se sirve __________.
16. La sopa acaba de salir de la cocina: está __________.
17. El aguacate ya se puede comer: está __________.
18. La zanahoria no ha pasado por el fuego: está __________.
19. El arroz ya ha pasado por el agua caliente: está __________.
20. Todo el grupo quiere repetir el plato: está __________.

**Oplossingen:** 1 dulce; 2 saladas; 3 ácido; 4 amargo; 5 picante; 6 suave; 7 fuerte; 8 fresca; 9 crujiente; 10 cremosa; 11 jugosa; 12 seco; 13 tierna; 14 duro; 15 frío; 16 caliente; 17 maduro; 18 cruda; 19 cocido; 20 delicioso.

**Didactische noot:** de woordbank geeft de lemma’s. De leerling moet waar nodig congruentie toepassen.  
**Printplaatsing:** na `Sabores de México y América` en vóór de receptproductie.

## C5-U6-NAT-01 · Veinte acciones con la ropa

**Platform:** digitale hub  
**Aantal:** exact 20  
**Instructie leerling:** `Lee la situación y elige la acción correcta.`  
**Mechaniek:** vierkeuze; na correctie verschijnt één voorbeeld met lijdend-voorwerpspronomen.

| # | Situación | Antwoord | Model na correctie |
|---:|---|---|---|
| 1 | Poner una prenda en el cuerpo. | ponerse | Me la pongo. |
| 2 | Sacar una prenda del cuerpo. | quitarse | Me la quito. |
| 3 | Comprobar si una prenda te queda bien. | probarse | Me la pruebo. |
| 4 | Tener ropa en el cuerpo. | llevar | La llevo. |
| 5 | Cubrir el cuerpo con ropa. | vestirse | Me visto. |
| 6 | Dejar de llevar la ropa. | desvestirse | Me desvisto. |
| 7 | Limpiar una prenda con agua. | lavar | La lavo. |
| 8 | Quitar el agua de la ropa después de lavarla. | escurrir | La escurro. |
| 9 | Colocar ropa húmeda para que se seque. | tender | La tiendo. |
| 10 | Perder la humedad al aire. | secarse | Se seca. |
| 11 | Quitar las arrugas con calor. | planchar | La plancho. |
| 12 | Poner una prenda doblada en el armario. | guardar | La guardo. |
| 13 | Hacer una prenda más pequeña con pliegues. | doblar | La doblo. |
| 14 | Unir dos partes con botones. | abrochar | La abrocho. |
| 15 | Separar los botones de una prenda. | desabrochar | La desabrocho. |
| 16 | Cerrar una chaqueta con una cremallera. | subir la cremallera | La subo. |
| 17 | Reparar tela con hilo y aguja. | coser | La coso. |
| 18 | Hacer una prenda más corta. | acortar | La acorto. |
| 19 | Hacer una prenda más grande o larga. | alargar | La alargo. |
| 20 | Devolver una compra y recibir otra talla. | cambiar | La cambio. |

**Anker:** `#c5-u6-nat-01`

## C5-U6-NAT-02 · Veinticinco palabras de moda y compras

**Platform:** digitale hub  
**Aantal:** exact 25  
**Instructie leerling:** `Lee la definición y elige la palabra correcta.`  
**Mechaniek:** vierkeuze; verdeel visueel in vijf reeksen van vijf, maar scoreer als één oefening op 25.

| # | Definitie/context | Antwoord |
|---:|---|---|
| 1 | Conjunto de prendas que llevas. | el conjunto |
| 2 | Forma de vestir popular en un momento. | la moda |
| 3 | Persona que crea ropa. | el diseñador / la diseñadora |
| 4 | Lugar donde se muestran prendas a compradores. | el escaparate |
| 5 | Espacio privado para probarse ropa. | el probador |
| 6 | Número o letra que indica el tamaño. | la talla |
| 7 | Precio más bajo durante una promoción. | la rebaja |
| 8 | Papel que demuestra una compra. | el tique |
| 9 | Dinero que te devuelven. | el cambio |
| 10 | Acción de pedir un precio más bajo. | regatear |
| 11 | Ropa que otra persona ya ha usado. | de segunda mano |
| 12 | Ropa producida con menor impacto ambiental. | sostenible |
| 13 | Material que viene de la oveja. | la lana |
| 14 | Material común de camisetas y vaqueros. | el algodón |
| 15 | Material animal usado en zapatos o cinturones. | el cuero |
| 16 | Diseño con líneas paralelas. | de rayas |
| 17 | Diseño formado por cuadrados. | de cuadros |
| 18 | Diseño con muchas flores. | de flores |
| 19 | Prenda que cubre la parte superior del cuerpo y tiene mangas. | la camisa |
| 20 | Prenda larga que cubre las piernas por separado. | el pantalón |
| 21 | Calzado deportivo. | las zapatillas |
| 22 | Objeto que llevas alrededor del cuello. | la bufanda |
| 23 | Objeto para llevar cosas, normalmente con asas. | el bolso |
| 24 | Pieza que protege la cabeza del sol. | la gorra |
| 25 | Decisión de llevarte una prenda en la tienda. | Me lo/la llevo. |

**Acceptatie:** accepteer zonder lidwoord waar semantisch ondubbelzinnig.  
**Anker:** `#c5-u6-nat-02`

## C5-U7-NAT-01 · La casa escondida

**Platform:** digitale hub  
**Aantal:** exact 15 doelwoorden  
**Instructie leerling:** `Encuentra las quince palabras relacionadas con la casa.`  
**Mechaniek:** genereer bij buildtijd een stabiel 15×15-raster. Woorden mogen horizontaal, verticaal en diagonaal, voorwaarts en achterwaarts staan. Selectie moet met muis, touch en toetsenbord werken.

**Exacte woordlijst:**

1. casa
2. piso
3. salón
4. cocina
5. baño
6. dormitorio
7. pasillo
8. terraza
9. jardín
10. sofá
11. mesa
12. silla
13. armario
14. cama
15. ventana

**Technische regels:**

- normaliseer alleen intern voor het raster: `SALON`, `BANO`, `JARDIN`, `SOFA`;
- toon in de woordlijst altijd de correcte accenten;
- de leerling moet exact vijftien woorden vinden;
- markeer gevonden woorden ook in de lijst;
- toon de oplossing pas na `Rendirse`;
- `Otra serie` mag posities veranderen, maar nooit woorden toevoegen of verwijderen.

**Anker:** `#c5-u7-nat-01`

## C5-U7-NAT-02 · Veinticinco instrucciones para llegar y actuar

**Platform:** printcursus + compacte hubcontrole  
**Aantal:** exact 25  
**Instructie leerling:** `Completa con el imperativo afirmativo de tú.`  
**Printlayout:** vijf blokken van vijf items met voldoende invulruimte.  
**Digitale controle:** dezelfde 25 items, één tekstveld per vorm.

### A. En casa

1. __________ (abrir) la ventana del salón.
2. __________ (cerrar) la puerta de la cocina.
3. __________ (subir) al primer piso.
4. __________ (bajar) al garaje.
5. __________ (poner) las llaves sobre la mesa.

### B. En la calle

6. __________ (salir) de la plaza por la calle Mayor.
7. __________ (seguir) todo recto.
8. __________ (girar) a la derecha en la farmacia.
9. __________ (cruzar) el puente.
10. __________ (parar) delante del museo.

### C. En el transporte

11. __________ (tomar) el autobús número doce.
12. __________ (comprar) el billete en la máquina.
13. __________ (esperar) en la parada.
14. __________ (bajar) en la tercera parada.
15. __________ (mirar) el mapa antes de continuar.

### D. Para ayudar a un visitante

16. __________ (decir) el nombre de la calle.
17. __________ (venir) conmigo hasta la esquina.
18. __________ (tener) cuidado con las bicicletas.
19. __________ (ir) por el camino corto.
20. __________ (hacer) una foto del plano.

### E. Al llegar

21. __________ (buscar) el número veinte.
22. __________ (llamar) al timbre.
23. __________ (entrar) en el edificio.
24. __________ (sentarse) en el sofá.
25. __________ (dar) el mensaje a Valen.

**Oplossingen:** 1 abre; 2 cierra; 3 sube; 4 baja; 5 pon; 6 sal; 7 sigue; 8 gira; 9 cruza; 10 para; 11 toma; 12 compra; 13 espera; 14 baja; 15 mira; 16 di; 17 ven; 18 ten; 19 ve; 20 haz; 21 busca; 22 llama; 23 entra; 24 siéntate; 25 da.

**Foutdiagnose digitale versie:**

- items 1–4, 6–15 en 21–23: `Forma regular o cambio ya conocido.`
- items 5 en 16–20, 25: `Imperativo irregular corto.`
- item 24: `No olvides el pronombre reflexivo y la tilde.`

**Printplaatsing:** na §4.1, vóór de bestaande ordeningsoefening.  
**Anker hub:** `#c5-u7-nat-02`

## C5-U8-NAT-01 · Veinte experiencias de La Ruta

**Platform:** digitale hub  
**Aantal:** exact 20  
**Instructie leerling:** `Completa con el pretérito perfecto compuesto.`  
**Mechaniek:** de leerling vult de volledige werkwoordgroep in. Accepteer normale spaties en hoofdlettervarianten; accenten zijn verplicht.

| # | Zin | Antwoord |
|---:|---|---|
| 1 | Hoy Lucía __________ (visitar) el Museo del Prado. | ha visitado |
| 2 | Esta semana Diego __________ (comer) tacos con el grupo. | ha comido |
| 3 | Valen ya __________ (escribir) una postal desde Cartagena. | ha escrito |
| 4 | Nina todavía no __________ (subir) a Machu Picchu. | ha subido |
| 5 | Mateo __________ (hacer) muchas fotos en Buenos Aires. | ha hecho |
| 6 | Yo __________ (preparar) mi mochila esta mañana. | he preparado |
| 7 | Tú __________ (ver) alguna vez el mar Mediterráneo. | has visto |
| 8 | Nosotros __________ (viajar) en tren hoy. | hemos viajado |
| 9 | Vosotros __________ (volver) tarde al hotel. | habéis vuelto |
| 10 | Los estudiantes __________ (abrir) el mapa digital. | han abierto |
| 11 | Lucía y Nina __________ (poner) las entradas en la mochila. | han puesto |
| 12 | Diego no __________ (probar) todavía este plato peruano. | ha probado |
| 13 | Valen __________ (decir) la dirección correcta. | ha dicho |
| 14 | Mateo y yo __________ (resolver) el problema. | hemos resuelto |
| 15 | ¿Tú __________ (romper) alguna vez una maleta? | has roto |
| 16 | La profesora __________ (leer) nuestros diarios de viaje. | ha leído |
| 17 | Esta tarde __________ (llover) en Cusco. | ha llovido |
| 18 | Mis amigos __________ (llegar) ya al aeropuerto. | han llegado |
| 19 | Yo todavía no __________ (escribir) la última página. | he escrito |
| 20 | ¿Ustedes __________ (estar) alguna vez en Perú? | han estado |

**Foutdiagnose:**

- hulpwerkwoord fout: `Mira la persona del sujeto.`
- participium fout: `¿Participio regular o irregular?`
- ontbrekend accent bij `habéis` of `leído`: `La tilde también cuenta.`

**Anker:** `#c5-u8-nat-01`

---

# 6. Data- en componentcontract voor implementatie

Sla de nieuwe inhoud niet verspreid als losse hardcoded DOM-fragmenten op. Voeg per unit een gegevensarray toe volgens het bestaande projectpatroon. Als er geen bestaand patroon is, gebruik:

```js
const NATIVE_EXERCISES = [
  {
    id: "c5-u4-nat-01",
    unit: "U4",
    title: "Gustos en ruta",
    placement: "hub",
    type: "dual-cloze",
    itemCount: 25,
    items: []
  }
];
```

## Verplichte validatie per oefening

Voeg een ontwikkelaarsassertie toe:

```js
console.assert(
  exercise.items.length === exercise.itemCount,
  `${exercise.id}: expected ${exercise.itemCount} items, got ${exercise.items.length}`
);
```

Voor de woordzoeker geldt `targets.length === 15`.

## Voortgang en opslag

- Gebruik de bestaande opslagmethode indien de hub al `localStorage` gebruikt.
- Anders: sleutel `c5-native-progress-v1`.
- Sla alleen oefening-ID, hoogste score en voltooiingsstatus op.
- Geen persoonsgegevens of vrije leerlingtekst bewaren.

## TTS

- Gebruik bestaande browser-TTS.
- Taal: `es-ES`, tenzij de unit al een andere vaste stemvariant gebruikt.
- Voor U0 wordt elk getalwoord afzonderlijk uitgesproken.
- TTS is ondersteuning, geen externe audio-afhankelijkheid.

---

# 7. PowerPoint- en PDF-synchronisatie

## Nieuwe printoefeningen

De volgende oefeningen moeten in cursuslaag, PDF en docent-PowerPoint terechtkomen:

- C5-U2-NAT-01;
- C5-U5-NAT-02;
- C5-U7-NAT-02.

## Docent-PowerPoint

Voeg per printoefening twee dia’s toe:

1. leerlingweergave zonder oplossingen;
2. dezelfde oefening met antwoorden in de bestaande oplossingskleur.

Voor C5-U7-NAT-02 mag de reeks over twee leerlingdia’s en twee oplossingsdia’s worden verdeeld om leesbaarheid te behouden. Het itemaantal verandert niet.

## Leerling-PowerPoint

Voeg alleen de leerlingweergave toe. Geen antwoorden in notities, alt-tekst of verborgen objecten.

## Nieuwe digitale verwijzingen vanuit print

Voeg in de relevante herhalings- of spelroute van iedere unit een korte regel toe:

`Practica también en la página digital: «[titel]».`

Gebruik het bestaande QR-component en het opgegeven anker. Maak geen nieuwe externe URL.

---

# 8. QA-checklist

Claude Code Web rondt de build pas af wanneer alle onderstaande controles slagen.

## Inhoud

- [ ] Alle 13 oefening-ID’s bestaan exact eenmaal.
- [ ] Het totale aantal nieuwe items is 215.
- [ ] De aantallen per oefening zijn respectievelijk 11, 11, 20, 8, 20, 25, 20, 20, 20, 25, 15, 25 en 20.
- [ ] Alle antwoorden uit hoofdstuk 5 zijn exact geïmplementeerd.
- [ ] Geen item introduceert futuro simple, condicional of subjuntivo.
- [ ] De castnamen en locaties zijn consistent met de unitroute.

## Techniek

- [ ] Alle hubs openen zonder netwerkverbinding.
- [ ] Geen iframe of externe oefenwidget.
- [ ] Geen consolefouten.
- [ ] Alle `console.assert`-controles slagen.
- [ ] Score, reset en opnieuw proberen werken.
- [ ] Toetsenbord en zichtbare focus werken.
- [ ] TTS faalt stil en bruikbaar wanneer geen Spaanse stem beschikbaar is.
- [ ] De woordzoeker bevat precies vijftien doelwoorden en is oplosbaar.

## Layout

- [ ] Geen horizontale overflow op 360 px.
- [ ] Geen afgekapt tekstveld of knop.
- [ ] Printpagina’s blijven binnen het bestaande formaat.
- [ ] Nieuwe PowerPoint-dia’s gebruiken dezelfde master en marges.
- [ ] Accenten, ñ, ü en omgekeerde vraagtekens renderen correct.

## Regressie

- [ ] Alle bestaande oefeningen blijven aanwezig.
- [ ] Bestaande score- en navigatielogica blijft werken.
- [ ] Bestaande QR-links en ankers blijven geldig.
- [ ] De unitvolgorde U0–U8 blijft ongewijzigd.
- [ ] PDF, bewerkbare laag, hub en PowerPoints blijven inhoudelijk gesynchroniseerd waar van toepassing.

---

# 9. Vereiste oplevering door Claude Code Web

Lever na de build:

1. de gewijzigde bronbestanden;
2. opnieuw gegenereerde PDF’s voor U2, U5 en U7;
3. bijgewerkte hubs voor U0, U1, U3, U4, U5, U6, U7 en U8;
4. bijgewerkte docent- en leerling-PowerPoints voor U2, U5 en U7;
5. een compact `C5_NATIVE_EXERCISE_IMPLEMENTATION_REPORT.md` met:
   - gewijzigde bestanden;
   - plaatsing per oefening-ID;
   - werkelijk geteld itemaantal;
   - testresultaten;
   - eventuele afwijkingen;
6. screenshots op desktop en mobiel van minstens één nieuwe oefening per betrokken hub;
7. rendercontrole van elke nieuwe printpagina en PowerPoint-dia.

Een afwijking van inhoud, aantal of plaatsing wordt niet stilzwijgend opgelost. Rapporteer die als blocker voordat je de canonieke oefeninhoud wijzigt.
