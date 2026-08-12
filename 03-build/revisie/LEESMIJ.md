# Reviewdocumenten (.docx) — om na te lezen, niet om te drukken

De cursus wordt in **PDF** geleverd. Deze map bevat iets anders: per unit één
Word-bestand waarin dezelfde inhoud staat, maar **zonder de opmaak**. Bedoeld
om na te lezen en te becommentariëren; daarna verwerk ik de opmerkingen in de
bron en volgt er een nieuwe PDF.

## Waarom niet gewoon de PDF omzetten

Dat is geprobeerd en het werkt hier niet, om twee redenen:

1. **Technisch.** LibreOffice kan in deze omgeving geen enkel bestand openen
   (getest: PDF→docx, HTML→docx, met en zonder eigen profiel — telkens *source
   file could not be loaded*), en `python-docx` staat er niet en is niet te
   installeren (PyPI is dicht).
2. **Inhoudelijk, en dat weegt zwaarder.** Een omgezette PDF geeft een
   nagebootste layout: kaders die net niet kloppen, kolommen die verschuiven,
   schrijflijnen die op de verkeerde plek belanden. U leest dan de opmaak na in
   plaats van de inhoud, en uw opmerkingen gaan over een layout die in de échte
   PDF niet bestaat.

Dit document gooit de opmaak daarom bewust weg: doorlopende tekst, koppen,
genummerde oefeningen, brede rechtermarge, regelnummers in de linkermarge.
Het lijkt níet op de cursus — dat is de bedoeling.

## Wat er met het niet-tekstuele gebeurt

| in het boek | hier |
|---|---|
| schrijflijn | `______` — even lang als in het boek (kort · midden · lang · vol) |
| geruit schrijfvlak | `[schrijfvlak]` |
| schrijfkolommen (sorteeroefening) | `Schrijfkolommen: kop → [schrijfruimte] │ …` |
| tabel | echte Word-tabel |
| tekening, kaart, QR-code | weggelaten — die kijkt u in de PDF na |
| icoontje | weggelaten (interface, geen inhoud) |
| kleuremoji op een woordkaart | blijft staan (die dráágt betekenis) |

**Wat u hier dus niet kunt nakijken:** de bladspiegel, de paginaovergangen, de
beeldkeuze en de kleuren. Opmerkingen daarover zet u in de PDF.

## Werkwijze

1. Open het `.docx` in Word.
2. Becommentarieer zoals u gewoon bent — *Controleren ▸ Nieuwe opmerking*, of
   gewoon in het rood typen. De rechtermarge is 6 cm breed zodat de
   opmerkingen naast de tekst passen; de regelnummers (om de vijf regels)
   maken verwijzen makkelijk.
3. Stuur het bestand terug.
4. Ik verwerk de opmerkingen in de **bron** (de generator, niet dit document)
   en lever de unit opnieuw in PDF + digitale pagina.

## Bouwen

```bash
python3 03-build/gen_word_revision.py C5 1      # één unit
python3 03-build/gen_word_revision.py --todos   # alle 31
python3 03-build/revisar_docx.py --todos        # nakijken vóór levering
```

`revisar_docx.py` bestaat omdat er hier geen programma is dat een .docx opent
vóór u dat doet: het controleert de zip, de volgorde van de XML-elementen
tegen het officiële schema (Word weigert een verkeerde volgorde), de tabellen,
en of élk woord van de unit ook echt in het reviewdocument staat.
