#!/usr/bin/env python3
"""Genereert luisterfragmenten (mp3) via ElevenLabs — natuurlijke stem per spreker.

Tweede audioroute naast `gen_audio.py` (Google Cloud TTS). Zelfde uitvoer, zodat de
luistercomponenten niets hoeven te weten van de bron: ze zoeken gewoon het mp3-bestand
en vallen terug op browser-TTS zolang dat er niet is.

    ELEVENLABS_API_KEY=<sleutel>  python3 03-build/web/gen_audio_elevenlabs.py C5 0
    ELEVENLABS_API_KEY=<sleutel>  python3 03-build/web/gen_audio_elevenlabs.py C6+ 0 1 2
    python3 03-build/web/gen_audio_elevenlabs.py C5 0 --dry     # toon wat er gemaakt zou worden
    python3 03-build/web/gen_audio_elevenlabs.py C5 0 --solo cortos   # enkel de korte taken
    python3 03-build/web/gen_audio_elevenlabs.py --voices       # beschikbare stemmen ophalen

Uitvoer: het pad dat het fragment zelf opgeeft in zijn `audio`-veld, relatief aan
`03-build/web/` — dus `audio/C5_U0.mp3` voor de begripsladder en `audio/C5_U0_03.mp3`
voor een korte audiotaak (+ `_<i>.mp3` per regel bij --split). Datzelfde veld staat in
de hub, zodat generator en speler nooit uit elkaar kunnen lopen.

Twee bronnen, één guion-formaat (zie DATACONTRACT onderaan):
  * `escucha_data.py`        — het lange luisterfragment per unit (begripsladder);
  * `escucha_corta_data.py`  — de korte audiotaken per unit (microdictado, klankreeks,
                               mini-dialoog, weerbericht, wegbeschrijving…).
Elke spreker krijgt een vaste stem, zodat dezelfde cast door de hele cursus dezelfde
stem houdt — Lucía klinkt in U0 als in U8.

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
    # de vaste cast (§15 CLAUDE.md)
    "Lucía": "", "Diego": "", "Valen": "", "Nina": "", "Mateo": "",
    "Profesora": "", "Profesor": "", "Narrador": "", "Narradora": "", "Tú": "",
    # terugkerende rolstemmen uit de korte audiotaken
    "Camarero": "", "Cliente": "", "Dependienta": "", "Turista": "",
    "Presentador": "", "Sofía": "", "Bea": "", "Voz": "",
    # het seseo-fragment vraagt expliciet twee accenten (C5-U0-AUD-07)
    "Voz_España": "", "Voz_América": "",
    # eenmalige sprekers uit C5-U1-AUD-01
    "Marta": "", "Andrés": "", "Yuki": "", "Tom": "",
    # sprekers uit de lange luisterfragmenten (escucha_data.py)
    "Aarón": "", "Abuela": "", "Agente": "", "Alumna": "", "Alumno": "",
    "Chica": "", "Chico": "", "Doctora": "", "Guía": "", "Hugo": "",
    "Madre": "", "Pau": "", "Periodista": "", "Recepcionista": "",
    "Rosa": "", "Sam": "", "Señora": "", "Álex": "",
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


def fragmentos(course, unit, cuales="todos"):
    """Alle fragmenten van één unit: het lange luisterfragment + de korte audiotaken.

    Twee bronnen, één contract: `escucha_data.py` levert de zesdelige
    begripsladder (één per unit), `escucha_corta_data.py` de kortere audiotaken
    (microdictado, klankreeks, mini-dialoog…). Beide gebruiken hetzelfde
    guion-formaat, dus hieronder hoeft niets te weten waar een fragment vandaan
    komt.
    """
    sys.path.insert(0, os.path.join(ROOT, "03-build", "web"))
    lista = []
    if cuales in ("todos", "largo"):
        import escucha_data as ED
        frag = ED.TODOS.get((course, unit))
        if frag:
            lista.append(frag)
    if cuales in ("todos", "cortos"):
        import escucha_corta_data as EC
        lista.extend(EC.CORTOS.get((course, unit), []))
    return lista


def build_fragmento(frag, pool, dry=False, split=False):
    guion = frag["guion"]
    nombre = frag.get("id") or frag.get("titulo", "?")
    if not frag.get("audio") or not guion:
        print("%-14s «%s» — overgeslagen: geen eigen script (extern af te spelen)"
              % (nombre, frag.get("titulo", "")))
        return
    tekens = sum(len(l["es"]) for l in guion)
    print("%-14s «%s» — %d regels, %d tekens → %s"
          % (nombre, frag.get("titulo", ""), len(guion), tekens, frag["audio"]))
    for l in guion[:3]:
        print("    %-12s %s" % (l["who"] + ":", l["es"][:66] + ("…" if len(l["es"]) > 66 else "")))
    if len(guion) > 3:
        print("    … en %d regels meer" % (len(guion) - 3))
    if dry:
        return

    toegewezen, mp3, delen = {}, b"", []
    for i, l in enumerate(guion):
        vid = voice_for(l["who"], toegewezen, pool)
        try:
            audio = synth(l["es"], vid)
        except urllib.error.HTTPError as e:
            sys.exit("ElevenLabs gaf %s: %s" % (e.code, e.read().decode("utf8", "ignore")[:200]))
        mp3 += audio                      # naïeve mp3-concat speelt in alle browsers
        delen.append(audio)
        print("    ✓ %2d/%d  %s" % (i + 1, len(guion), l["who"]))

    out = os.path.join(ROOT, "03-build", "web", frag["audio"])
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "wb").write(mp3)
    print("  → %s (%.0f KB)" % (os.path.relpath(out, ROOT), len(mp3) / 1024))
    if split:                             # losse regels: klik-om-te-horen in het transcript
        base = out[:-4]
        for i, d in enumerate(delen):
            open("%s_%02d.mp3" % (base, i), "wb").write(d)
        print("  → %d losse regels voor het meelees-transcript" % len(delen))


def build(course, unit, dry=False, split=False, cuales="todos"):
    lista = fragmentos(course, unit, cuales)
    if not lista:
        sys.exit("Geen fragmenten voor %s U%d." % (course, unit))
    print("=== %s U%d — %d fragment(en) ===" % (course, unit, len(lista)))
    if dry:
        for frag in lista:
            build_fragmento(frag, [], dry=True)
        print("  (dry run — niets opgehaald)")
        return
    if not KEY:
        sys.exit("ELEVENLABS_API_KEY ontbreekt. Zet hem als omgevingsvariabele, niet in de repo.")
    pool = [v["voice_id"] for v in _get("/voices").get("voices", [])]
    for frag in lista:
        build_fragmento(frag, pool, split=split)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("course", nargs="?", help="C5 | C6+ | C4")
    ap.add_argument("units", nargs="*", type=int)
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--split", action="store_true", help="ook elke regel apart opslaan")
    ap.add_argument("--voices", action="store_true", help="toon beschikbare stemmen")
    ap.add_argument("--solo", choices=["todos", "largo", "cortos"], default="todos",
                    help="largo = enkel de begripsladder · cortos = enkel de korte audiotaken")
    a = ap.parse_args()
    if a.voices:
        if not KEY:
            sys.exit("ELEVENLABS_API_KEY ontbreekt.")
        list_voices(); sys.exit(0)
    if not a.course or not a.units:
        sys.exit("Gebruik: gen_audio_elevenlabs.py C5 0 [1 2 …]  |  --voices  |  --dry "
                 "|  --solo cortos")
    for u in a.units:
        build(a.course, u, dry=a.dry, split=a.split, cuales=a.solo)

# ---------------------------------------------------------------------------
# DATACONTRACT — twee bronnen, één guion-formaat
#
# 1) 03-build/web/escucha_data.py — het lange luisterfragment per unit
#
#    TODOS = {("C5", 0): {
#      "id": "C5-U0-ESC-01", "ancla": "c5-u0-esc-01",
#      "titulo": "En la puerta de embarque",
#      "audio":  "audio/C5_U0.mp3",          # pad relatief aan 03-build/web/
#      "situacion": {"lugar": …, "quien": …, "que": …, "claves": [3 chunks]},
#      "guion":  [{"who": "Lucía", "es": "¡Hola!…", "nl": "Hallo!…"}, …],
#      "global": {"q": …, "opts": [...], "ans": …, "why": …},
#      "detalle": [ … 5 items … ],
#      "vf": [{"q": …, "ans": True, "prueba": "letterlijk uit het guion"}, …],
#      "produccion": {"prompt": …, "modo": "escribir" | "grabar"},
#    }}
#
# 2) 03-build/web/escucha_corta_data.py — de korte audiotaken per unit
#
#    CORTOS = {("C5", 0): [{
#      "id": "C5-U0-AUD-02", "ancla": "c5-u0-aud-02",
#      "curso": "C5", "unidad": 0,
#      "seccion":  "§1.3 · Microdictado",
#      "etiqueta": "Audio 1.3 · Microdictado · 0:50",   # letterlijk zoals in print
#      "titulo": …, "tipo": "dictado", "tarea": …,
#      "audio":  "audio/C5_U0_02.mp3",       # None = extern af te spelen, geen mp3
#      "guion":  [{"who": …, "es": …, "nl": …}, …],
#      "clave":  [ … antwoordsleutel, enkel voor het docentendossier … ],
#      "nota":   "optioneel: afwijking/waarschuwing",
#    }, …]}
#
# Dit script raakt enkel `guion` en `audio` aan; alles daarbuiten is voor de hub en
# het docentendossier. Dezelfde `guion` voedt dus het mp3, het meelees-transcript en
# de browser-TTS-terugval. Eén bron, drie gebruiken.
# ---------------------------------------------------------------------------
