#!/usr/bin/env python3
# C4 — genereer echte dialoog-audio (mp3) voor de «Lee y escucha»-luisterfragmenten via
# Google Cloud Text-to-Speech (de enige TTS-host die door de sandbox-proxy bereikbaar is).
# Elke SPREKER krijgt een eigen natuurlijke stem → klinkt als een echt gesprek. De mp3's komen in
# 03-build/web/componentes/audio/C4_U<n>_audio.mp3 en worden automatisch ingebed door gen_c4_comprension.py.
#
# GEBRUIK:  GOOGLE_TTS_API_KEY=<jouw-sleutel>  python3 gen_audio.py
#           (optioneel:  C4_ONLY=2,4  om enkel bepaalde units te doen)
# Vrije laag van Google Cloud TTS dekt dit ruim (Neural2/WaveNet: 1M tekens/maand gratis).
import os, sys, json, base64, ssl, urllib.request
ROOT="/home/user/espa-ol-en-la-pr-ctica"
sys.path.insert(0, f"{ROOT}/03-build/web")
import comprension_data as CD

KEY=os.environ.get("GOOGLE_TTS_API_KEY")
AUDIO_DIR=f"{ROOT}/03-build/web/componentes/audio"
ENDPOINT="https://texttospeech.googleapis.com/v1/text:synthesize"
# afwisselend ♀/♂ en ES/US zodat opeenvolgende sprekers duidelijk verschillen
VOICES=["es-ES-Neural2-A","es-ES-Neural2-B","es-US-Neural2-A","es-US-Neural2-B","es-ES-Neural2-F","es-ES-Neural2-C"]

CA="/root/.ccr/ca-bundle.crt"
def _opener():
    ctx=ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()
    handlers=[urllib.request.HTTPSHandler(context=ctx)]
    px=os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    if px: handlers.append(urllib.request.ProxyHandler({"https":px,"http":px}))
    return urllib.request.build_opener(*handlers)
OPENER=_opener()

def synth(text, voice):
    body={"input":{"text":text},
          "voice":{"languageCode":voice[:5],"name":voice},
          "audioConfig":{"audioEncoding":"MP3","speakingRate":0.92,"pitch":0.0}}
    req=urllib.request.Request(ENDPOINT+"?key="+KEY, data=json.dumps(body).encode(),
                               headers={"Content-Type":"application/json"})
    with OPENER.open(req, timeout=45) as r:
        return base64.b64decode(json.load(r)["audioContent"])

def build_unit(unit, A):
    spk_voice={}
    mp3=b""
    for s,line in A["guion"]:
        if s not in spk_voice:
            spk_voice[s]=VOICES[len(spk_voice)%len(VOICES)]
        mp3+=synth(line, spk_voice[s])   # naïeve mp3-concat speelt in alle browsers
    os.makedirs(AUDIO_DIR, exist_ok=True)
    out=f"{AUDIO_DIR}/C4_U{unit}_audio.mp3"
    open(out,"wb").write(mp3)
    print(f"  U{unit}: {out} · {len(mp3)} bytes · {len(spk_voice)} stemmen ({', '.join(spk_voice.values())})")

if __name__=="__main__":
    if not KEY:
        sys.exit("⛔ Zet GOOGLE_TTS_API_KEY (env). Voorbeeld: GOOGLE_TTS_API_KEY=xxx python3 gen_audio.py")
    only=os.environ.get("C4_ONLY")
    units=[int(x) for x in only.split(",")] if only else [u for u,A in CD.AUDIO.items() if A]
    print("Genereer audio voor units:", units)
    for u in units:
        A=CD.AUDIO.get(u)
        if not A: print(f"  U{u}: geen audio-data — overslaan"); continue
        build_unit(u, A)
    print("Klaar. Herbouw nu de componenten:  for u in", " ".join(map(str,units)),
          "; do C4_UNIT=$u C4_COMPR_OUT=C4_U${u}_comprension.html python3 gen_c4_comprension.py; python3 gen_c4u${u}_hub.py; done")
