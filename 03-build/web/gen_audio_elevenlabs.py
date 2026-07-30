#!/usr/bin/env python3
"""Genereert luisterfragmenten (mp3) via ElevenLabs — natuurlijke stem per spreker.

Tweede audioroute naast `gen_audio.py` (Google Cloud TTS). Zelfde uitvoer, zodat de
luistercomponenten niets hoeven te weten van de bron: ze zoeken gewoon het mp3-bestand
en vallen terug op browser-TTS zolang dat er niet is.

    ELEVENLABS_API_KEY=<sleutel>  python3 03-build/web/gen_audio_elevenlabs.py C5 0
    ELEVENLABS_API_KEY=<sleutel>  python3 03-build/web/gen_audio_elevenlabs.py C6+ 0 1 2
    python3 03-build/web/gen_audio_elevenlabs.py C5 0 --dry     # toon wat er gemaakt zou worden
    python3 03-build/web/gen_audio_elevenlabs.py --voices       # beschikbare stemmen ophalen

Uitvoer: `03-build/web/audio/<cursus>_U<n>.mp3` (+ `_<i>.mp3` per regel bij --split).

De dialoogteksten komen uit `escucha_data.py` (zie DATACONTRACT onderaan). Elke spreker
krijgt een vaste stem, zodat dezelfde cast door de hele cursus dezelfde stem houdt —
Lucía klinkt in U0 als in U8.

VEILIGHEID: de sleutel staat in een omgevingsvariabele, nooit in de repo of in een chat.
"""
import argparse, json, os, ssl, sys, urllib.error, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
AUDIO_DIR = os.path.join(ROOT, "03-build", "web", "audio")
API = "https://api.elevenlabs.io/v1"
KEY = os.environ.get("ELEVENLABS_API_KEY")

# Vaste stem per castlid — dezelfde stem door de hele cursus.
# Vul de ID's in met `--voices` (of laat leeg: dan wordt er in volgorde toegewezen).
CAST_VOICES = {
    "Lucía": "", "Diego": "", "Valen": "", "Nina": "", "Mateo": "",
    "Profesora": "", "Profesor": "", "Narrador": "", "Tú": "",
}
MODEL = "eleven_multilingual_v2"          # ondersteunt Spaans
SETTINGS = {"stability": 0.45, "similarity_boost": 0.75, "style": 0.15, "speed": 0.92}

CA = "/root/.ccr/ca-bundle.crt"


def _opener():
    ctx = ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()
    handlers = [urllib.request.HTTPSHandler(context=ctx)]
    px = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    if px:
        handlers.append(urllib.request.ProxyHandler({"https": px, "http": px}))
    return urllib.request.build_opener(*handlers)


OPENER = _opener()


def _get(path):
    req = urllib.request.Request(API + path, headers={"xi-api-key": KEY})
    with OPENER.open(req, timeout=45) as r:
        return json.load(r)


def list_voices():
    """Toont de beschikbare stemmen zodat je CAST_VOICES kan invullen."""
    data = _get("/voices")
    print("%-26s %-24s %s" % ("naam", "voice_id", "labels"))
    for v in data.get("voices", []):
        lab = v.get("labels", {})
        print("%-26s %-24s %s" % (v.get("name", "")[:25], v.get("voice_id", ""),
                                  ", ".join("%s=%s" % kv for kv in list(lab.items())[:3])))
    print("\nVul de gewenste voice_id's in bij CAST_VOICES bovenaan dit script.")


def synth(text, voice_id):
    body = {"text": text, "model_id": MODEL, "voice_settings": SETTINGS}
    req = urllib.request.Request(
        "%s/text-to-speech/%s?output_format=mp3_44100_128" % (API, voice_id),
        data=json.dumps(body).encode(),
        headers={"xi-api-key": KEY, "Content-Type": "application/json", "Accept": "audio/mpeg"})
    with OPENER.open(req, timeout=90) as r:
        return r.read()


def voice_for(speaker, toegewezen, pool):
    """Vaste stem per spreker; valt terug op de pool wanneer CAST_VOICES leeg is."""
    vid = CAST_VOICES.get(speaker) or toegewezen.get(speaker)
    if not vid:
        if not pool:
            sys.exit("Geen stemmen beschikbaar. Draai eerst --voices en vul CAST_VOICES in.")
        vid = pool[len(toegewezen) % len(pool)]
        toegewezen[speaker] = vid
    return vid


def build(course, unit, dry=False, split=False):
    sys.path.insert(0, os.path.join(ROOT, "03-build", "web"))
    try:
        import escucha_data as ED
    except ImportError:
        sys.exit("escucha_data.py ontbreekt — zie het DATACONTRACT onderaan dit bestand.")

    frag = ED.FRAGMENTOS.get((course, unit))
    if not frag:
        sys.exit("Geen luisterfragment voor %s U%d in escucha_data.py" % (course, unit))

    guion = frag["guion"]
    tekens = sum(len(line) for _s, line in guion)
    print("%s U%d · «%s» — %d regels, %d tekens" % (course, unit, frag.get("titulo", ""), len(guion), tekens))
    for s, line in guion[:3]:
        print("    %-10s %s" % (s + ":", line[:70] + ("…" if len(line) > 70 else "")))
    if len(guion) > 3:
        print("    … en %d regels meer" % (len(guion) - 3))
    if dry:
        print("  (dry run — niets opgehaald)")
        return

    if not KEY:
        sys.exit("ELEVENLABS_API_KEY ontbreekt. Zet hem als omgevingsvariabele, niet in de repo.")

    pool = [v["voice_id"] for v in _get("/voices").get("voices", [])]
    toegewezen, mp3, delen = {}, b"", []
    for i, (spk, line) in enumerate(guion):
        vid = voice_for(spk, toegewezen, pool)
        try:
            audio = synth(line, vid)
        except urllib.error.HTTPError as e:
            sys.exit("ElevenLabs gaf %s: %s" % (e.code, e.read().decode("utf8", "ignore")[:200]))
        mp3 += audio                      # naïeve mp3-concat speelt in alle browsers
        delen.append(audio)
        print("    ✓ %2d/%d  %s" % (i + 1, len(guion), spk))

    os.makedirs(AUDIO_DIR, exist_ok=True)
    slug = course.replace("+", "plus")
    out = os.path.join(AUDIO_DIR, "%s_U%d.mp3" % (slug, unit))
    open(out, "wb").write(mp3)
    print("  → %s (%.0f KB)" % (os.path.relpath(out, ROOT), len(mp3) / 1024))
    if split:                             # losse regels: klik-om-te-horen in het transcript
        for i, d in enumerate(delen):
            p = os.path.join(AUDIO_DIR, "%s_U%d_%02d.mp3" % (slug, unit, i))
            open(p, "wb").write(d)
        print("  → %d losse regels voor het meelees-transcript" % len(delen))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("course", nargs="?", help="C5 | C6+ | C4")
    ap.add_argument("units", nargs="*", type=int)
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--split", action="store_true", help="ook elke regel apart opslaan")
    ap.add_argument("--voices", action="store_true", help="toon beschikbare stemmen")
    a = ap.parse_args()
    if a.voices:
        if not KEY:
            sys.exit("ELEVENLABS_API_KEY ontbreekt.")
        list_voices(); sys.exit(0)
    if not a.course or not a.units:
        sys.exit("Gebruik: gen_audio_elevenlabs.py C5 0 [1 2 …]  |  --voices  |  --dry")
    for u in a.units:
        build(a.course, u, dry=a.dry, split=a.split)

# ---------------------------------------------------------------------------
# DATACONTRACT — 03-build/web/escucha_data.py
#
# FRAGMENTOS = {
#   ("C5", 0): {
#     "titulo":  "En la puerta del instituto",
#     "tipo":    "dialogo",            # dialogo | informativo | entrevista | anuncio
#     "situacion": "Primer día de clase. Dos alumnos se conocen.",
#     "guion": [                       # (spreker, zin) — spreker bepaalt de stem
#        ("Lucía", "¡Hola! ¿Cómo te llamas?"),
#        ("Diego", "Me llamo Diego. ¿Y tú?"),
#     ],
#     "antes":   ["¿Dónde están?", "¿Cuántas personas hablan?"],   # vóór het luisteren
#     "global":  {"q": "¿De qué hablan?", "opts": [...], "ans": "…"},
#     "detalle": [ {"q":"¿Cómo se llama la chica?", "ans":"Lucía"}, … ],   # 5 items
#     "vf":      [ {"q":"Diego es de México.", "ans":True, "bewijs":"Soy de México."}, … ],
#     "produccion": "Preséntate tú: nombre, ciudad, edad.",
#   },
# }
#
# Dezelfde `guion` voedt zowel het mp3 (dit script) als het meelees-transcript en de
# browser-TTS-fallback in het luistercomponent. Eén bron, drie gebruiken.
# ---------------------------------------------------------------------------
