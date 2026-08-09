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

## MP3 — hoe de fragmenten kleiner werden (2026-08-09)

De spraakmotor levert WAV: onbewerkt en groot (114 MB voor alle 77 fragmenten).
Normaal zet je dat om met `ffmpeg`, maar dat staat niet in deze bouwomgeving, en
PyPI en npm zijn er geblokkeerd. Wat wél werkt is `git clone`.

**lamejs** is de LAME-encoder, volledig herschreven in JavaScript. Die is
opgehaald en met Node gedraaid:

```bash
git clone --depth 1 https://github.com/zhuker/lamejs.git
node 03-build/web/wav_a_mp3.js <map-met-lamejs> 03-build/web/audio 64
```

Resultaat: **114 MB → 21 MB**, 5,4× kleiner. 64 kbps mono is voor spraak ruim
voldoende — beter dan een telefoongesprek, en de acht stemmen blijven volledig
herkenbaar.

**Nagerekend, niet gegokt:** van alle 77 bestanden is elk MP3-frame uitgelezen
en de totale duur vergeleken met het origineel. Alle 77 kloppen op een tiende
seconde na.

**Licentie:** lamejs staat onder LGPL-3.0 en zit daarom *niet* in deze repo — het
is gereedschap, geen cursusmateriaal. De MP3's die eruit komen zijn van ons; een
encoder legt geen voorwaarden op aan wat je ermee maakt.

**De WAV's blijven staan** als origineel. Ze zijn niet zomaar opnieuw te maken:
daarvoor is de spraakmotor met zijn acht stemmodellen nodig, en die staat ook
niet in de repo.
