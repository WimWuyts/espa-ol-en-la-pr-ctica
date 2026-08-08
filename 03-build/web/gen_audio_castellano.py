#!/usr/bin/env python3
"""Spreekt alle luisterfragmenten in, met de acht Castiliaanse stemmen.

DE MOTOR
sherpa-onnx, met de modellen uit zijn eigen release `tts-models` op GitHub. Dat
is een omweg met een reden: PyPI en HuggingFace zijn in deze bouwomgeving
geblokkeerd, GitHub-releasebijlagen niet. Zes van de acht stemmen zijn gewoon
Piper-modellen, opnieuw verpakt; de zevende komt uit Kokoro; de laatste twee
zijn toonhoogte-varianten van bestaande stemmen (zie `voces.py`).

    python3 gen_audio_castellano.py --muestra   # één dialoog
    python3 gen_audio_castellano.py C5 5        # één unit
    python3 gen_audio_castellano.py             # alle 59
    python3 gen_audio_castellano.py --dry       # tonen, niets maken

Uitvoer: het pad dat het fragment zelf opgeeft in zijn `audio`-veld, relatief
aan deze map. Datzelfde veld staat in de hub, dus generator en speler kunnen
niet uit elkaar lopen. Zolang er geen bestand is, leest de browserstem voor.

DE MAP MET STEMMEN
Standaard `03-build/web/voces-tts/`, te overrulen met de omgevingsvariabele
`TTS_VOCES`. `--donde` zegt waar hij kijkt en wat hij vindt.
"""
import argparse
import array
import os
import shutil
import subprocess
import sys
import wave

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import escucha_corta_data as EC          # noqa: E402
import escucha_data as ED                # noqa: E402
import voces as V                        # noqa: E402

VOCES_DIR = os.environ.get("TTS_VOCES", os.path.join(AQUI, "voces-tts"))
TTS_BIN = os.environ.get("TTS_BIN", "sherpa-onnx-offline-tts")

PAUSA_MISMO, PAUSA_OTRO, PAUSA_NARRADOR = 0.35, 0.65, 0.9
MUESTRA = "C5-U5-ESC-01"


# ─────────────────────────────────────────────────────────────────────────────
def fragmentos():
    out = []
    for (curso, u), lista in sorted(EC.CORTOS.items()):
        for f in lista:
            if f.get("tipo") == "cancion" or not f.get("guion"):
                continue          # een bestaand nummer valt niet op te nemen
            out.append((curso, u, f))
    for n in dir(ED):
        if n.startswith(("C5_U", "C6P_U")):
            v = getattr(ED, n)
            if isinstance(v, dict) and "guion" in v:
                out.append(("C5" if n.startswith("C5") else "C6+",
                            int(n.split("_U")[1]), v))
    return out


def hablantes_de(guion):
    vistos = []
    for g in guion:
        if g["who"] not in vistos:
            vistos.append(g["who"])
    return vistos


# ─────────────────────────────────────────────────────────────────────────────
def _args_voz(voz):
    """De vlaggen voor deze stem. Drie soorten model, drie vormen."""
    genero, tipo, carpeta, _ = V.VOCES[voz]
    d = os.path.join(VOCES_DIR, carpeta)
    sid = V.SID.get(voz)
    if tipo == "kokoro":
        args = ["--kokoro-model=%s/model.onnx" % d,
                "--kokoro-voices=%s/voices.bin" % d,
                "--kokoro-tokens=%s/tokens.txt" % d,
                "--kokoro-data-dir=%s/espeak-ng-data" % d,
                "--kokoro-dict-dir=%s/dict" % d,
                "--kokoro-lexicon=%s/lexicon-us-en.txt,%s/lexicon-zh.txt" % (d, d)]
    elif tipo == "coqui":
        args = ["--vits-model=%s/model.onnx" % d,
                "--vits-tokens=%s/tokens.txt" % d]
    else:                                     # piper
        modelo = carpeta.replace("vits-piper-", "")
        args = ["--vits-model=%s/%s.onnx" % (d, modelo),
                "--vits-tokens=%s/tokens.txt" % d,
                "--vits-data-dir=%s/espeak-ng-data" % d]
    if sid is not None:
        args.append("--sid=%d" % sid)
    return args


def _tono(ruta, factor):
    """Verschuift de toonhoogte door te herbemonsteren.

    Zoals een plaat trager of sneller laten draaien: de klank zakt of stijgt én
    de duur verandert een beetje mee. Bij 6 à 7 % blijft dat natuurlijk, en het
    levert een stem op die als een ánder persoon leest — precies wat er nodig is
    waar vier vrouwelijke personages naast elkaar staan.
    """
    with wave.open(ruta, "rb") as w:
        params = w.getparams()
        datos = array.array("h", w.readframes(w.getnframes()))
    n = int(len(datos) / factor)
    salida = array.array("h", [0] * n)
    for i in range(n):
        p = i * factor
        j = int(p)
        if j + 1 >= len(datos):
            salida[i] = datos[-1]
        else:
            f = p - j
            salida[i] = int(datos[j] * (1 - f) + datos[j + 1] * f)
    with wave.open(ruta, "wb") as w:
        w.setparams(params)
        w.writeframes(salida.tobytes())


def di(texto, voz, destino):
    r = subprocess.run([TTS_BIN] + _args_voz(voz) +
                       ["--output-filename=" + destino, texto],
                       capture_output=True, text=True)
    if not os.path.exists(destino):
        sys.exit("mislukt op «%s» met stem %s:\n%s"
                 % (texto[:70], voz, (r.stderr or r.stdout)[-400:]))
    if voz in V.TONO:
        _tono(destino, V.TONO[voz])


def pegar(trozos, pausas, destino):
    """Plakt de regels aan elkaar met stiltes ertussen.

    De stemmen komen uit drie modellen met drie bemonsteringsfrequenties (16,
    22 en 24 kHz). Het geheel volgt de eerste; de rest wordt herbemonsterd,
    anders klinkt de helft van het gesprek te snel of te traag.
    """
    with wave.open(trozos[0], "rb") as w:
        params = w.getparams()
    with wave.open(destino, "wb") as out:
        out.setparams(params)
        silencio = b"\x00" * (params.sampwidth * params.nchannels)
        for i, t in enumerate(trozos):
            with wave.open(t, "rb") as w:
                datos = array.array("h", w.readframes(w.getnframes()))
                if w.getframerate() != params.framerate:
                    f = w.getframerate() / params.framerate
                    n = int(len(datos) / f)
                    datos = array.array(
                        "h", [datos[min(int(i2 * f), len(datos) - 1)] for i2 in range(n)])
            out.writeframes(datos.tobytes())
            if i < len(pausas):
                out.writeframes(silencio * int(params.framerate * pausas[i]))
    with wave.open(destino) as w:
        return w.getnframes() / w.getframerate()


# ─────────────────────────────────────────────────────────────────────────────
def hacer(f, dry=False):
    guion = f["guion"]
    quienes = hablantes_de(guion)
    reparto, prestados, imposibles = V.reparto(quienes)
    rel = f.get("audio") or ""
    if not rel:
        return None, "geen bestandsnaam in de gegevens"
    if imposibles:
        return None, ("te veel sprekers van hetzelfde geslacht (%s)"
                      % ", ".join(q for q, _ in imposibles))
    if dry:
        return rel, "%d regels · %s" % (
            len(guion), " · ".join("%s→%s" % (q, reparto[q]) for q in quienes))

    destino = os.path.join(AQUI, rel)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    tmp = os.path.join(AQUI, ".tts-tmp")
    os.makedirs(tmp, exist_ok=True)
    trozos, pausas = [], []
    for i, g in enumerate(guion):
        pieza = os.path.join(tmp, "%03d.wav" % i)
        di(g["es"], reparto[g["who"]], pieza)
        trozos.append(pieza)
        if i + 1 < len(guion):
            sig = guion[i + 1]["who"]
            pausas.append(PAUSA_MISMO if g["who"] == sig
                          else (PAUSA_NARRADOR if g["who"].startswith("Narrad")
                                else PAUSA_OTRO))
    wav = destino[:-4] + ".wav" if destino.endswith(".mp3") else destino
    dur = pegar(trozos, pausas, wav)
    shutil.rmtree(tmp, ignore_errors=True)
    nota = "%.0f s" % dur
    if prestados:
        nota += " · " + "; ".join("%s leent %s" % (q, o) for q, _, o in prestados)
    return os.path.basename(wav), nota


def donde():
    print("stemmen in: %s" % VOCES_DIR)
    for voz, (gen, tipo, carpeta, desc) in sorted(V.VOCES.items()):
        p = os.path.join(VOCES_DIR, carpeta)
        print("   %-12s %-3s %-8s %-34s %s"
              % (voz, gen, tipo, desc, "ok" if os.path.isdir(p) else "ONTBREEKT"))
    print("\nspeler: %s  %s"
          % (TTS_BIN, "ok" if shutil.which(TTS_BIN) else "NIET GEVONDEN"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("curso", nargs="?", choices=["C5", "C6+"])
    ap.add_argument("unidad", nargs="?", type=int)
    ap.add_argument("--muestra", action="store_true")
    ap.add_argument("--solo")
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--donde", action="store_true", help="waar staan de stemmen?")
    a = ap.parse_args()

    if a.donde:
        return donde()

    trabajo = fragmentos()
    if a.muestra:
        trabajo = [x for x in trabajo if x[2].get("id") == MUESTRA]
    if a.solo:
        trabajo = [x for x in trabajo if x[2].get("id") == a.solo]
    if a.curso:
        trabajo = [x for x in trabajo if x[0] == a.curso]
    if a.unidad is not None:
        trabajo = [x for x in trabajo if x[1] == a.unidad]
    if not trabajo:
        sys.exit("niets te doen")

    print("%d fragment(en)%s\n" % (len(trabajo), "  (dry run)" if a.dry else ""))
    fallos = 0
    for curso, u, f in trabajo:
        hecho, nota = hacer(f, dry=a.dry)
        if hecho is None:
            fallos += 1
            print("  !  %-4s U%-2d %-30s %s" % (curso, u, f.get("titulo", "")[:30], nota))
        else:
            print("     %-4s U%-2d %-30s → %-22s %s"
                  % (curso, u, f.get("titulo", "")[:30], hecho, nota))
    if fallos:
        print("\n%d fragment(en) niet gelukt" % fallos)


if __name__ == "__main__":
    main()
