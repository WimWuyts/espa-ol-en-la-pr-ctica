# Lucide — herkomst en licentie

- **Bron:** <https://github.com/lucide-icons/lucide>
- **Commit:** `113a3b1a3bda9a31d30f4b056cd434ce9462828e`
- **Licentie:** ISC (zie `LICENSE`). Let op: CLAUDE.md §15 noemde MIT; dat klopt
  alleen voor de deelverzameling die van Feather is afgeleid. ISC en MIT zijn
  praktisch gelijk — vrij gebruik, met behoud van de copyrightvermelding. Die
  staat daarom hier, verbatim, naast de iconen.
- **Wat er is overgenomen:** enkel de tekenpaden van de 1766 iconen, samengevoegd
  tot één bestand `lucide.json` (`{naam: paden}`). Niet de 1766 losse
  SVG-bestanden en niet de metadata: dat zou de repo met duizenden bestanden
  vullen zonder dat we er iets mee doen.
- **Waarom niet de hele SVG:** de omhullende `<svg>` bepaalt maat, lijndikte en
  kleur. Die maken we zelf in `iconos.py`, uit onze eigen tokens, zodat een
  icoon meekleurt met de cursuskleur en in print dezelfde lijndikte houdt als de
  rest van de bladzijde.
- **Bijwerken:** repo opnieuw klonen en dit script overdoen. De iconen zijn
  stabiel; een update is zelden nodig.
