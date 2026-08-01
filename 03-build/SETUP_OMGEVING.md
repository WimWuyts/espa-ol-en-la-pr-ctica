# Setup-script voor de cloud-omgeving (PowerPoint-bouw én -controle)

## Het probleem, precies gediagnosticeerd (2026-07-30)

Een bouwchat meldde dat de PowerPoints niet gebouwd konden worden. De diagnose was maar
half juist. Gemeten in de omgeving:

| Onderdeel | Status | Gevolg |
|---|---|---|
| **python-pptx** | ✅ aanwezig (1.0.2) | **decks bouwen werkt** — bewezen met een testdeck én door de 54 bestaande decks in de repo |
| **libreoffice-core** | ✅ aanwezig | — |
| **libreoffice-impress** | ❌ **ontbrak** | `soffice --convert-to pdf` faalde met *«source file could not be loaded»* → geen visuele controle |

Dus: **bouwen kon wel, controleren niet.** De PowerPoints hoeven niet te wachten.

## De oplossing

Zet dit als **Setup script** in de omgeving (claude.ai/code → wolk-icoontje boven het
berichtvak → tandwiel bij de omgeving → veld **Setup script**):

```bash
#!/bin/bash
# PowerPoint bouwen (python-pptx) én visueel controleren (LibreOffice Impress)
apt-get update -qq || true
apt-get install -y -qq libreoffice-impress || true
pip install --quiet python-pptx || true
exit 0
```

**`apt-get update` is niet optioneel.** Zonder die regel geeft de installatie `404 Not Found`
op de pakketten — de index in het basisimage is verouderd. Dat is precies de fout die
optrad bij de eerste poging.

`|| true` en `exit 0` staan er omdat een setup-script dat niet-nul afsluit de sessie laat
falen (documentatie: *Script requirements*).

## Verificatie na installatie

```bash
python3 -c "import pptx; print(pptx.__version__)"
soffice --headless --convert-to pdf 03-build/pptx/C5_U3_docente.pptx --outdir /tmp
```

Getest in deze omgeving na installatie: `C5_U3_docente.pptx` → PDF van 1,4 MB, met de
melding `using filter : impress_pdf_Export`.

## Waarom dit blijvend moet

Een handmatige `apt-get install` in een sessie verdwijnt zodra de VM wordt opgeruimd. Het
setup-script wordt éénmalig uitgevoerd en daarna **gecachet** (filesystem-snapshot), dus
elke volgende sessie start mét Impress op schijf — zonder wachttijd.

Let op: wijzig je het setup-script of de toegestane domeinen, dan wordt de cache opnieuw
opgebouwd. Dat is eenmalig trager.

## Nagekomen (2026-08-01): pip bereikt PyPI niet meer

In de bouwsessie van 1 augustus was **python-pptx afwezig** én niet te installeren:

```
$ pip install python-pptx
ERROR: Could not find a version that satisfies the requirement python-pptx (from versions: none)
$ curl -o /dev/null -w '%{http_code}' https://pypi.org/simple/python-pptx/
403
```

Ook `apt-get update` gaf 403 op `archive.ubuntu.com`. Dat is geen certificaat- of
cachekwestie maar een **egress-policy van de omgeving**: de proxy-status meldt
`connect_rejected · gateway answered 403 to CONNECT`. Er valt niets omheen te werken —
het setup-script hierboven kan de pakketten alleen ophalen als PyPI en het Ubuntu-archief
in de toegestane domeinen van de omgeving staan.

**Gevolg voor de bouw:** de dia's §5 Lectura en §6 Escucha zijn wél in de generatoren
gezet (twee regels in elke `_run_all`), maar de `.pptx`-bestanden in de repo zijn nog de
vorige versie. Eén keer per unit `python3 03-build/pptx/gen_u<n>_docente.py` draaien in een
omgeving mét python-pptx volstaat; er hoeft niets herschreven te worden.
