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

# ── de acht Piper-stemmen ────────────────────────────────────────────────────
# naam → (bestandsnaam op HuggingFace, geslacht, accent, korte omschrijving)
PIPER = {
    "es_ES-davefx-medium":    ("m", "España",     "warme mannenstem, duidelijk"),
    "es_ES-sharvard-medium":  ("v", "España",     "neutrale vrouwenstem"),
    "es_ES-carlfm-x_low":     ("m", "España",     "lichter, jonger"),
    "es_ES-mls_9972-low":     ("v", "España",     "uit een sprekersarchief"),
    "es_ES-mls_10246-low":    ("m", "España",     "uit een sprekersarchief"),
    "es_MX-claude-high":      ("m", "México",     "Mexicaans, hoogste kwaliteit"),
    "es_MX-ald-medium":       ("m", "México",     "Mexicaans, tweede stem"),
    "es_AR-daniela-high":     ("v", "Argentina",  "Argentijns, voseo-klank"),
}

# ── de vaste cast: één stem, de hele cursus lang ─────────────────────────────
CAST = {
    "Narradora":    "es_ES-sharvard-medium",   # de verteller van de oefeningen
    "Lucía":        "es_ES-mls_9972-low",      # Sevilla
    "Diego":        "es_MX-claude-high",       # Mexico-Stad
    "Valen":        "es_AR-daniela-high",      # Cartagena — geen Colombiaanse
                                               # stem beschikbaar; de Argentijnse
                                               # ligt er van de acht het dichtst bij
    "Nina":         "es_ES-mls_9972-low",      # Cusco (zie NOTA hieronder)
    "Mateo":        "es_ES-mls_10246-low",     # Buenos Aires (zie NOTA)
    "Pau":          "es_ES-carlfm-x_low",      # Barcelona
    "Sam":          "es_ES-davefx-medium",     # de Vlaamse leerling
    "Tú":           "es_ES-carlfm-x_low",      # de leerling zelf
}

# ── bijrollen ────────────────────────────────────────────────────────────────
# Ze komen zelden samen voor, dus ze mogen stemmen delen. De volgorde hieronder
# is wat `controla()` mag verschuiven als er tóch een botsing ontstaat.
ROLES = {
    "Camarero":     "es_MX-ald-medium",
    "Cliente":      "es_ES-davefx-medium",
    "Dependienta":  "es_ES-mls_9972-low",
    "Recepcionista": "es_ES-sharvard-medium",
    "Doctora":      "es_ES-mls_9972-low",
    "Guía":         "es_MX-ald-medium",
    "Turista":      "es_ES-carlfm-x_low",
    "Profesora":    "es_ES-sharvard-medium",
    "Presentador":  "es_ES-davefx-medium",
    "Periodista":   "es_ES-mls_10246-low",
    "Agente":       "es_ES-mls_10246-low",
    "Abuela":       "es_ES-mls_9972-low",
    "Madre":        "es_ES-sharvard-medium",
    "Señora":       "es_ES-mls_9972-low",
    "Chico":        "es_ES-carlfm-x_low",
    "Chica":        "es_ES-sharvard-medium",
    "Alumno":       "es_ES-carlfm-x_low",
    "Alumna":       "es_ES-mls_9972-low",
    "Voz":          "es_ES-davefx-medium",
    "Sofía":        "es_ES-sharvard-medium",
    "Bea":          "es_ES-mls_9972-low",
    "Rosa":         "es_ES-sharvard-medium",
    "Marta":        "es_ES-mls_9972-low",
    "Hugo":         "es_ES-mls_10246-low",
    "Álex":         "es_ES-carlfm-x_low",
    "Aarón":        "es_ES-davefx-medium",
    "Andrés":       "es_ES-mls_10246-low",
    "Yuki":         "es_ES-sharvard-medium",
    "Tom":          "es_ES-davefx-medium",
    # het seseo-fragment vraagt uitdrukkelijk twee accenten naast elkaar
    "Voz_España":   "es_ES-davefx-medium",
    "Voz_América":  "es_MX-claude-high",
}

# Nina is uit Cusco en zou een Andes-stem verdienen; die zit niet bij de acht.
# De neutrale Spaanse stem is dan eerlijker dan een Mexicaanse of Argentijnse,
# die een ánder accent zou suggereren dan het personage heeft.
NOTA = """Drie dingen die niet perfect kunnen, en waarom.

1. Piper heeft acht Spaanse stemmen, waarvan er drie vrouwelijk zijn. De cast
   heeft vier vrouwen — Narradora, Lucía, Valen en Nina — en ze komen alle zes
   mogelijke paren tegen elkaar in beeld. Twee van hen móéten dus een stem
   delen. Gekozen is het paar dat het mínst samen voorkomt: Lucía en Nina staan
   in één enkel fragment samen. Daar leent Nina een andere stem; overal elders
   klinkt ze zichzelf. `controla()` zegt precies waar dat gebeurt.

2. Voor Colombia en Peru bestaat er geen Piper-stem. Valen en Nina krijgen
   daarom de dichtstbijzijnde, respectievelijk een neutrale — geen accent is
   eerlijker dan het verkeerde accent.

3. De enige Argentijnse stem is vrouwelijk, en Mateo is een jongen. Hij krijgt
   dus een mannelijke Spaanse stem: het accent gaat verloren, maar een jongen
   met een vrouwenstem is een grotere fout."""

TODAS = dict(CAST)
TODAS.update({k: v for k, v in ROLES.items() if k not in TODAS})

# reservestemmen, in volgorde, voor als er in één fragment tóch een botsing is
RESERVA = ["es_ES-davefx-medium", "es_ES-sharvard-medium", "es_ES-carlfm-x_low",
           "es_ES-mls_9972-low", "es_ES-mls_10246-low", "es_MX-ald-medium",
           "es_MX-claude-high", "es_AR-daniela-high"]


# Wie er als eerste zijn eigen stem mag houden als twee castleden botsen.
# De verteller staat vooraan: die spreekt in élk fragment, dus als zij verschuift
# valt het over de hele cursus op.
PRIORIDAD = ["Narradora", "Diego", "Lucía", "Valen", "Nina", "Mateo", "Pau", "Sam", "Tú"]


def _genero(voz):
    return PIPER[voz][0]


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
    print("%d fragmenten · %d sprekers · %d Piper-stemmen"
          % (n, len(TODAS), len(PIPER)))
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
