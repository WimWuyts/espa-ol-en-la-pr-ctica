# De luisterfragmenten opnemen

59 fragmenten, 818 regels, 40 sprekers. Er zijn drie manieren om ze te maken;
ze schrijven alle drie naar dezelfde bestandsnamen, dus de cursus merkt geen
verschil.

## 1 · Piper — gratis, op je eigen computer

Acht Spaanse stemmen in drie accenten (Spanje, Mexico, Argentinië). **58 van de
59 fragmenten** kunnen hiermee volledig.

```bash
pip install piper-tts

cd 03-build/web
python3 gen_audio_piper.py --muestra      # één dialoog, om te beluisteren
```

Dat maakt `audio/C5_U5.mp3` — «Una mesa para tres», dertien regels, de ober en
Diego, allebei met een Mexicaanse stem. **Luister daar eerst naar.** Vind je het
goed genoeg, dan:

```bash
python3 gen_audio_piper.py                # alle 58
python3 gen_audio_piper.py C5 5           # of één unit
python3 gen_audio_piper.py --dry          # tonen wat er zou gebeuren
```

De eerste keer haalt Piper de stemmodellen zelf op (samen ongeveer 200 MB); die
komen in `03-build/web/voces-piper/` en blijven daar.

**ffmpeg** is nodig om er mp3 van te maken. Ontbreekt het, dan blijft er een
`.wav` staan en zegt het script dat erbij — de bestanden zijn dan groter maar
werken wel.

## 2 · ElevenLabs — betaald, voor wat Piper niet kan

```bash
ELEVENLABS_API_KEY=<sleutel> python3 gen_audio_elevenlabs.py C5 8
```

Nodig voor **één fragment**: `C5-U8-AUD-01` («Cuatro personas cuentan su
verano») heeft vier vrouwenrollen naast elkaar, en Piper heeft er drie. Verder
handig als een gesprek te vlak klinkt — dan maak je alleen dát fragment opnieuw.

## 3 · Zelf inspreken

De opnamescripts staan klaar in `print/GUIONES_AUDIO.md` en
`print/GUIONES_AUDIO.html`: per fragment de tekst regel voor regel, wie het
zegt, en de bestandsnaam die de opname moet krijgen.

---

## Wie klinkt hoe

Staat in **`voces.py`**, los van de motor — het is een cursuskeuze, geen
technische. Twee regels: het accent volgt het personage (Diego klinkt
Mexicaans), en binnen één fragment klinkt niemand hetzelfde.

```bash
python3 voces.py       # rekent de rolverdeling na op alle 59 fragmenten
```

Drie dingen die niet perfect kunnen, en waarom, staan onderaan die uitvoer.

## De bestandsnaam ligt vast

De digitale pagina zoekt elk fragment op een exact pad (`audio/C5_U3_02.mp3`) en
speelt de browserstem zolang het er niet is. Eén letter verschil en de opname
wordt nooit gevonden — dat merk je pas in de klas. Alle drie de scripts halen
dat pad uit dezelfde bron als de hub, dus ze kunnen niet uit elkaar lopen.

## Nog niet uitgeprobeerd

`gen_audio_piper.py` is geschreven maar nooit gedraaid: in de omgeving waar de
cursus gebouwd wordt zijn PyPI en HuggingFace geblokkeerd, dus Piper en de
stemmen zijn daar niet te installeren. De rolverdeling, de bestandsnamen en de
volgorde zijn wél nagerekend (`voces.py` en `--dry`). De eerste echte proef is
op jouw computer — vandaar dat `--muestra` er is.
