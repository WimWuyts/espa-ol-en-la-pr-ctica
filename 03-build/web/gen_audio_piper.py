#!/usr/bin/env python3
"""Maakt de luisterfragmenten met Piper — lokaal, gratis, acht Spaanse stemmen.

WAAROM PIPER
De cursus heeft 59 fragmenten met veertig sprekers, en de reis gaat van Spanje
naar Mexico, Colombia, Peru en Argentinië. Piper heeft acht Spaanse stemmen in
drie accenten, dus Diego uit Mexico-Stad kán Mexicaans klinken. Dat is het
didactische punt: leerlingen horen dat Spaans niet overal hetzelfde klinkt.

Wie welke stem krijgt staat in `voces.py`, niet hier — dat is een cursuskeuze,
geen technische, en ze moet gelijk blijven welke motor je ook gebruikt.

    pip install piper-tts                       # eenmalig
    python3 gen_audio_piper.py --muestra        # één dialoog, om te beluisteren
    python3 gen_audio_piper.py C5 5             # alle fragmenten van C5 U5
    python3 gen_audio_piper.py                  # alles
    python3 gen_audio_piper.py C5 5 --dry       # tonen wat er zou gebeuren

De uitvoer gaat naar het pad dat het fragment zélf opgeeft in zijn `audio`-veld
(`audio/C5_U5.mp3`), relatief aan deze map. Datzelfde veld staat in de hub, dus
generator en speler kunnen niet uit elkaar lopen.

NIET GETEST IN DE BOUWOMGEVING
Deze code is geschreven maar nooit uitgevoerd: in de omgeving waar de cursus
gebouwd wordt, zijn PyPI en HuggingFace geblokkeerd, dus Piper en de
stemmodellen zijn daar niet te krijgen. De eerste echte proef is op jouw
computer. Alles wat wél te controleren viel — de rolverdeling, de bestandsnamen,
de volgorde — is nagerekend door `voces.py` en `--dry`.
"""
import argparse
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

VOCES_DIR = os.path.join(AQUI, "voces-piper")     # hier komen de modellen
SALIDA = AQUI

# stiltes tussen de regels, in seconden
PAUSA_MISMO = 0.35        # dezelfde spreker praat door
PAUSA_OTRO = 0.65         # de beurt gaat over
PAUSA_NARRADOR = 0.9      # na «Número uno» mag de leerling nadenken

MUESTRA = "C5-U5-ESC-01"  # «Una mesa para tres» — twee Mexicaanse stemmen


# ─────────────────────────────────────────────────────────────────────────────
def fragmentos():
    """[(curso, unidad, fragment)] — de korte taken en de lange fragmenten."""
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
def piper_disponible():
    return shutil.which("piper") is not None


def modelo(voz):
    """Het pad naar het stemmodel; haalt het op als het er nog niet is."""
    ruta = os.path.join(VOCES_DIR, voz + ".onnx")
    if os.path.exists(ruta):
        return ruta
    os.makedirs(VOCES_DIR, exist_ok=True)
    # piper haalt een onbekende stem zelf op van HuggingFace
    r = subprocess.run(["piper", "--model", voz, "--download-dir", VOCES_DIR,
                        "--data-dir", VOCES_DIR, "--output-file", os.devnull],
                       input=".", capture_output=True, text=True)
    if not os.path.exists(ruta):
        sys.exit("de stem «%s» kon niet opgehaald worden.\n"
                 "Probeer met de hand:\n"
                 "  piper --model %s --download-dir %s --output-file test.wav\n"
                 "Foutmelding van piper:\n%s"
                 % (voz, voz, VOCES_DIR, (r.stderr or r.stdout)[-500:]))
    return ruta


def di(texto, voz, destino):
    """Eén regel inspreken."""
    r = subprocess.run(["piper", "--model", modelo(voz),
                        "--data-dir", VOCES_DIR, "--output-file", destino],
                       input=texto, capture_output=True, text=True)
    if r.returncode != 0 or not os.path.exists(destino):
        sys.exit("piper struikelde over deze regel:\n  %s\n%s"
                 % (texto[:90], (r.stderr or r.stdout)[-400:]))


def pegar(trozos, pausas, destino):
    """Plakt de losse regels aan elkaar, met stiltes ertussen.

    Met de `wave`-module uit Python zelf: geen ffmpeg nodig om te monteren, en
    dus één afhankelijkheid minder tussen jou en het eerste geluid.
    """
    with wave.open(trozos[0], "rb") as w:
        params = w.getparams()
    with wave.open(destino, "wb") as out:
        out.setparams(params)
        silencio = b"\x00" * (params.sampwidth * params.nchannels)
        for i, t in enumerate(trozos):
            with wave.open(t, "rb") as w:
                out.writeframes(w.readframes(w.getnframes()))
            if i < len(pausas):
                out.writeframes(silencio * int(params.framerate * pausas[i]))


def a_mp3(wav, mp3):
    """Zet om naar mp3 als ffmpeg er is; anders blijft de wav staan."""
    if not shutil.which("ffmpeg"):
        return False
    r = subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav,
                        "-codec:a", "libmp3lame", "-q:a", "4", mp3],
                       capture_output=True)
    return r.returncode == 0 and os.path.exists(mp3)


# ─────────────────────────────────────────────────────────────────────────────
def hacer(f, dry=False):
    """Eén fragment: regel voor regel inspreken, monteren, wegschrijven."""
    guion = f["guion"]
    quienes = hablantes_de(guion)
    reparto, prestados, imposibles = V.reparto(quienes)
    destino_rel = f.get("audio") or ""
    if not destino_rel:
        return None, "geen bestandsnaam in de gegevens"
    destino = os.path.join(SALIDA, destino_rel)

    if imposibles:
        return None, ("meer sprekers van hetzelfde geslacht dan Piper stemmen heeft "
                      "(%s) — dit fragment vraagt een andere motor"
                      % ", ".join(q for q, _ in imposibles))

    if dry:
        return destino_rel, "%d regels · %s" % (
            len(guion), " · ".join("%s→%s" % (q, reparto[q].replace("es_", ""))
                                   for q in quienes))

    if not piper_disponible():
        sys.exit("piper staat niet in het pad. Installeer het met:\n"
                 "    pip install piper-tts")

    os.makedirs(os.path.dirname(destino), exist_ok=True)
    tmp = os.path.join(SALIDA, ".piper-tmp")
    os.makedirs(tmp, exist_ok=True)
    trozos, pausas = [], []
    for i, g in enumerate(guion):
        pieza = os.path.join(tmp, "%03d.wav" % i)
        di(g["es"], reparto[g["who"]], pieza)
        trozos.append(pieza)
        if i + 1 < len(guion):
            siguiente = guion[i + 1]["who"]
            if g["who"] == siguiente:
                pausas.append(PAUSA_MISMO)
            elif g["who"] in ("Narradora", "Narrador"):
                pausas.append(PAUSA_NARRADOR)
            else:
                pausas.append(PAUSA_OTRO)

    wav = destino[:-4] + ".wav" if destino.endswith(".mp3") else destino
    pegar(trozos, pausas, wav)
    hecho = destino_rel
    if destino.endswith(".mp3"):
        if a_mp3(wav, destino):
            os.remove(wav)
        else:
            hecho = os.path.basename(wav) + "  (wav — ffmpeg ontbreekt voor mp3)"
    shutil.rmtree(tmp, ignore_errors=True)
    nota = ""
    if prestados:
        nota = "; ".join("%s leent %s" % (q, o) for q, _, o in prestados)
    return hecho, nota


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("curso", nargs="?", choices=["C5", "C6+"])
    ap.add_argument("unidad", nargs="?", type=int)
    ap.add_argument("--muestra", action="store_true",
                    help="alleen de voorbeelddialoog, om te beluisteren")
    ap.add_argument("--solo", help="één fragment op zijn id, bv. C5-U5-AUD-02")
    ap.add_argument("--dry", action="store_true", help="tonen, niet maken")
    a = ap.parse_args()

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
        sys.exit("niets te doen — controleer curso/unidad/--solo")

    print("%d fragment(en)%s\n" % (len(trabajo), "  (dry run)" if a.dry else ""))
    saltados = 0
    for curso, u, f in trabajo:
        hecho, nota = hacer(f, dry=a.dry)
        if hecho is None:
            saltados += 1
            print("  !  %-4s U%-2d %-30s %s" % (curso, u, f.get("titulo", "")[:30], nota))
        else:
            print("     %-4s U%-2d %-30s → %s%s"
                  % (curso, u, f.get("titulo", "")[:30], hecho,
                     ("  · " + nota) if nota else ""))
    if saltados:
        print("\n%d fragment(en) overgeslagen — zie hierboven" % saltados)
    if a.muestra and not a.dry:
        print("\nBeluister het resultaat en laat weten of dit goed genoeg is.")


if __name__ == "__main__":
    main()
