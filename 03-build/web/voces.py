#!/usr/bin/env python3
"""Wie klinkt hoe — de rolverdeling van de stemmen, los van de motor.

WAAROM APART
De keuze «Diego klinkt Mexicaans» is een cursusbeslissing, geen technische. Ze
moet dus hetzelfde blijven of je de audio nu met Piper maakt, met ElevenLabs of
met iets van later. Daarom staat ze hier, en niet in de generator.

DE TWEE REGELS
1. **Accent volgt het personage.** De cast reist van Spanje naar Mexico,
   Colombia, Peru en Argentinië, en de cursus wil laten horen dát Spaans niet
   overal hetzelfde klinkt. Diego uit Mexico-Stad krijgt dus een Mexicaanse
   stem, Mateo uit Buenos Aires een Argentijnse. Dat is didactiek, geen luxe.
2. **Binnen één fragment nooit twee keer dezelfde stem.** Anders is een gesprek
   niet te volgen. `controla()` rekent dat na op álle 59 fragmenten — dat is het
   deel dat hier wél te testen valt, ook zonder Piper te kunnen draaien.

Piper heeft acht Spaanse stemmen, wij hebben veertig sprekers. Dat hoeft geen
probleem te zijn: de vaste cast krijgt elk een eigen stem en houdt die de hele
cursus, de bijrollen (ober, klant, dokter) delen wat overblijft — zolang ze maar
niet in hetzelfde fragment staan.
"""
import sys

# ── de stemmen die we écht hebben ────────────────────────────────────────────
# Allemaal Castiliaans: de cursus is Castiliaans met Mexico als decor (auteur,
# 2026-08-08). De grondtoon is gemeten, niet gegokt — autocorrelatie op een
# proefzin, mannen rond 120-140 Hz, vrouwen rond 215 Hz.
#
# naam → (geslacht, herkomst, hoe je hem aanroept, omschrijving)
VOCES = {
    "davefx":    ("m", "piper",  "vits-piper-es_ES-davefx-medium",   "121 Hz · warm, duidelijk"),
    "sharvard-m":("m", "piper",  "vits-piper-es_ES-sharvard-medium", "130 Hz · neutraal (sid 0)"),
    "sharvard-v":("v", "piper",  "vits-piper-es_ES-sharvard-medium", "218 Hz · neutraal (sid 1)"),
    "carlfm":    ("m", "piper",  "vits-piper-es_ES-carlfm-x_low",    "128 Hz · lichter, jonger"),
    "coqui":     ("m", "coqui",  "vits-coqui-es-css10",              "139 Hz · iets formeler"),
    "dora":      ("v", "kokoro", "kokoro-multi-lang-v1_0",           "216 Hz · Kokoro, 24 kHz"),
    # Een derde vrouwenstem, want er waren er maar twee en de cast heeft vier
    # vrouwelijke personages. Dit is `sharvard-v` met de toonhoogte 7 % omlaag:
    # herbemonstering, zoals een plaat trager laten draaien. Klein genoeg om
    # natuurlijk te blijven, groot genoeg om als een andere vrouw te horen — en
    # het lagere timbre past bij de oma- en mevrouw-rollen.
    "sharvard-v2":("v","piper",  "vits-piper-es_ES-sharvard-medium", "warmer, lager (sid 1, −7 %)"),
    # En een vierde, om dezelfde reden: «Cuatro personas cuentan su verano» zet
    # vier vrouwelijke personages naast elkaar. Dora, 6 % hoger — jonger van klank.
    "dora-alta": ("v", "kokoro", "kokoro-multi-lang-v1_0",           "jonger, hoger (sid 28, +6 %)"),
}

# de vlaggen die de speler nodig heeft, per stem
SID = {"sharvard-m": 0, "sharvard-v": 1, "sharvard-v2": 1,
       "dora": 28, "dora-alta": 28}

# toonhoogte-verschuiving na het inspreken (1.0 = ongewijzigd)
TONO = {"sharvard-v2": 0.93, "dora-alta": 1.06}

# ── de vaste cast: één stem, de hele cursus lang ─────────────────────────────
CAST = {
    "Narradora":    "sharvard-v",    # de verteller van de oefeningen
    "Lucía":        "dora",          # Sevilla
    "Diego":        "davefx",        # Mexico-Stad — Castiliaans, Mexicaans decor
    "Valen":        "sharvard-v",    # Cartagena (zie NOTA)
    "Nina":         "dora",          # Cusco (zie NOTA)
    "Mateo":        "sharvard-m",    # Buenos Aires
    "Pau":          "carlfm",        # Barcelona
    "Sam":          "coqui",         # de Vlaamse leerling
    "Tú":           "carlfm",        # de leerling zelf
}

# ── bijrollen ────────────────────────────────────────────────────────────────
# Ze komen zelden samen voor, dus ze mogen stemmen delen. De volgorde hieronder
# is wat `controla()` mag verschuiven als er tóch een botsing ontstaat.
ROLES = {
    "Camarero":     "carlfm",
    "Cliente":      "davefx",
    "Dependienta":  "sharvard-v",
    "Recepcionista": "dora",
    "Doctora":      "sharvard-v2",
    "Guía":         "coqui",
    "Turista":      "carlfm",
    "Profesora":    "dora",
    "Presentador":  "davefx",
    "Periodista":   "sharvard-m",
    "Agente":       "coqui",
    "Abuela":       "sharvard-v2",
    "Madre":        "dora",
    "Señora":       "sharvard-v2",
    "Chico":        "carlfm",
    "Chica":        "dora",
    "Alumno":       "sharvard-m",
    "Alumna":       "sharvard-v",
    "Voz":          "davefx",
    "Sofía":        "dora",
    "Bea":          "sharvard-v",
    "Rosa":         "dora",
    "Marta":        "sharvard-v2",
    "Hugo":         "coqui",
    "Álex":         "carlfm",
    "Aarón":        "davefx",
    "Andrés":       "sharvard-m",
    "Yuki":         "dora",
    "Tom":          "davefx",
    "Voz_España":   "davefx",
    "Voz_América":  "coqui",
}

# Nina is uit Cusco en zou een Andes-stem verdienen; die zit niet bij de acht.
# De neutrale Spaanse stem is dan eerlijker dan een Mexicaanse of Argentijnse,
# die een ánder accent zou suggereren dan het personage heeft.
NOTA = """Wat er niet perfect kan, en waarom.

1. **Zeven stemmen, veertig sprekers.** Dat hoeft geen probleem te zijn: de vaste
   cast houdt zijn eigen stem de hele cursus door, en de bijrollen delen wat
   overblijft — zolang ze niet in hetzelfde fragment staan. `controla()` rekent
   dat na op alle 59 fragmenten.

2. **Vier vrouwelijke personages, drie vrouwenstemmen.** Narradora, Lucía, Valen
   en Nina komen alle zes mogelijke paren tegen elkaar in beeld, dus twee van
   hen moeten delen. Waar het botst, leent er een; het script zegt waar.

3. **Alles Castiliaans.** Er zijn wél Mexicaanse en Argentijnse Piper-stemmen,
   maar de auteur koos (2026-08-08) voor één accent: de cursus is Castiliaans,
   met Mexico als decor. Dat is ook eerlijker dan een half-Mexicaans klankbeeld
   dat toch niet klopt met Colombia of Peru."""

TODAS = dict(CAST)
TODAS.update({k: v for k, v in ROLES.items() if k not in TODAS})

# reservestemmen, in volgorde, voor als er in één fragment tóch een botsing is
RESERVA = ["davefx", "sharvard-m", "carlfm", "coqui", "sharvard-v", "dora",
           "sharvard-v2", "dora-alta"]


# Wie er als eerste zijn eigen stem mag houden als twee castleden botsen.
# De verteller staat vooraan: die spreekt in élk fragment, dus als zij verschuift
# valt het over de hele cursus op.
PRIORIDAD = ["Narradora", "Diego", "Lucía", "Valen", "Nina", "Mateo", "Pau", "Sam", "Tú"]


def _genero(voz):
    return VOCES[voz][0]


def reparto(hablantes):
    """({spreker: stem}, [wie moest lenen]) voor één fragment.

    Niemand klinkt twee keer hetzelfde in één gesprek, anders is het niet te
    volgen. De vaste cast houdt zijn eigen stem — dat is wat een personage
    herkenbaar maakt — behalve als twee castleden dezelfde stem hebben en samen
    in beeld komen. Dan wijkt degene die het laagst in PRIORIDAD staat uit naar
    een vrije stem van hetzelfde geslacht, en zegt het script dat erbij.
    """
    salida, usadas, prestados, imposibles = {}, set(), [], []

    orden = sorted([h for h in hablantes if h in CAST],
                   key=lambda h: PRIORIDAD.index(h) if h in PRIORIDAD else 99)
    for quien in orden:
        voz = CAST[quien]
        if voz in usadas:
            # Uitwijken mag, van geslacht veranderen niet. Nina een mannenstem
            # geven omdat er toevallig geen vrouwenstem vrij is, klinkt niet als
            # een compromis maar als een fout. Kan het niet, dan zegt het script
            # dat dit fragment een andere motor nodig heeft — dat is één
            # fragment betalen in plaats van de hele cursus.
            libres = [v for v in RESERVA
                      if v not in usadas and _genero(v) == _genero(voz)]
            if libres:
                prestados.append((quien, voz, libres[0]))
                voz = libres[0]
            else:
                imposibles.append((quien, voz))
        salida[quien] = voz
        usadas.add(voz)

    for quien in [h for h in hablantes if h not in CAST]:
        preferida = TODAS.get(quien, RESERVA[0])
        if preferida in usadas:
            libres = [v for v in RESERVA
                      if v not in usadas and _genero(v) == _genero(preferida)]
            if not libres:
                libres = [v for v in RESERVA if v not in usadas]
            if libres:
                preferida = libres[0]
        salida[quien] = preferida
        usadas.add(preferida)
    return salida, prestados, imposibles


def controla():
    """Rekent de rolverdeling na op alle fragmenten. Geeft de problemen terug."""
    import escucha_corta_data as EC
    import escucha_data as ED

    frag = []
    for (curso, u), lista in sorted(EC.CORTOS.items()):
        for f in lista:
            if f.get("tipo") == "cancion" or not f.get("guion"):
                continue
            frag.append((f["id"], f.get("titulo", ""), f["guion"]))
    for n in dir(ED):
        if n.startswith(("C5_U", "C6P_U")):
            v = getattr(ED, n)
            if isinstance(v, dict) and "guion" in v:
                frag.append((v.get("id", n), v.get("titulo", ""), v["guion"]))

    problemas, avisos = [], []
    for fid, titulo, guion in frag:
        hablantes = []
        for g in guion:
            if g["who"] not in hablantes:
                hablantes.append(g["who"])
        rep, prestados, imposibles = reparto(hablantes)
        for quien, suya, otra in prestados:
            avisos.append((fid, titulo, quien, suya, otra))
        if imposibles:
            problemas.append((fid, titulo, [q for q, _ in imposibles]))
        vueltas = {}
        for quien, voz in rep.items():
            vueltas.setdefault(voz, []).append(quien)
        for voz, quienes in vueltas.items():
            if len(quienes) > 1 and not imposibles:
                problemas.append((fid, titulo, quienes))
    return len(frag), problemas, avisos


if __name__ == "__main__":
    n, problemas, avisos = controla()
    print("%d fragmenten · %d sprekers · %d Castiliaanse stemmen"
          % (n, len(TODAS), len(VOCES)))
    if problemas:
        print("\n%d fragment(en) passen niet in acht stemmen — die vragen een andere "
              "motor (bv. ElevenLabs):" % len(problemas))
        for fid, titulo, quienes in problemas:
            print("   %-16s %-32s te veel stemmen van hetzelfde geslacht (%s)"
                  % (fid, titulo[:32], ", ".join(quienes)))
    print("%d van de %d fragmenten kunnen volledig met Piper" % (n - len(problemas), n))
    if avisos:
        print("\n%d keer moet een castlid een andere stem lenen:" % len(avisos))
        for fid, titulo, quien, suya, otra in avisos:
            print("   %-16s %-28s %s: %s → %s" % (fid, titulo[:28], quien, suya, otra))
        print("   (overal elders klinkt dat personage wél zichzelf)")
    print("\n%s" % NOTA)
