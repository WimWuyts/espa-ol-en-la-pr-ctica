#!/usr/bin/env python3
"""Zet de inhoudsbronnen om in hub-JS.

De data staat in `nat_data.py`, `escucha_data.py` en `lectura_data.py`; dit
bestand maakt er de `build…(...)`-aanroepen van die in de hub terechtkomen.
Zo blijft de inhoud op één plaats en kan de printgenerator dezelfde bron lezen
zonder de JS te moeten napluizen.
"""
import json

_J = lambda o: json.dumps(o, ensure_ascii=False)


def choice_js(host_id, bloque, per=None, extra_desc="", prefix="build"):
    """Blueprint-oefening als vierkeuze. `per` = None -> alle items in één reeks,
    want de blueprints eisen «presenteer alle N items».

    `prefix` bestaat omdat C5 U0 de motoren onder hun oudere naam kent
    (`exChoice` in plaats van `buildChoice`); zie hub_drills.engines()."""
    n = len(bloque["items"])
    desc = bloque.get("instruccion_nl", "")
    if extra_desc:
        desc += " " + extra_desc
    cfg = {
        "title": "%s <span class=\"natid\">%s</span>" % (bloque["titulo"], bloque["id"]),
        "desc": desc,
        "per": per or n,
        "pool": bloque["items"],
    }
    # console.assert: de blueprint eist een exact aantal, dus laat het zichzelf
    # controleren in de browser in plaats van erop te vertrouwen.
    return ("console.assert(%d===%d,'%s: itemaantal wijkt af');\n"
            "%sChoice(%s,%s);\n" % (n, bloque["aantal"], bloque["id"],
                                    prefix, _J(host_id), _J(cfg)))


def match_js(host_id, bloque, per=None, prefix="build"):
    pares = [{"a": a, "b": b} for a, b in bloque["pares"]]
    n = len(pares)
    cfg = {
        "title": "%s <span class=\"natid\">%s</span>" % (bloque["titulo"], bloque["id"]),
        "desc": bloque.get("instruccion_nl", "") +
                (" Modelo: %s" % bloque["modelo"] if bloque.get("modelo") else ""),
        "per": per or min(10, n),
        "pool": pares,
    }
    return ("console.assert(%d===%d,'%s: itemaantal wijkt af');\n"
            "%sMatch(%s,%s);\n" % (n, bloque["aantal"], bloque["id"], prefix, _J(host_id), _J(cfg)))


def type_js(host_id, bloque, per_block=10):
    cfg = {
        "title": "%s <span class=\"natid\">%s</span>" % (bloque["titulo"], bloque["id"]),
        "desc": bloque.get("instruccion_nl", ""),
        "perBlock": per_block,
        "accents": bloque.get("accents", "soft"),
        "expect": bloque["aantal"],
        "items": bloque["items"],
    }
    return "buildType(%s,%s);\n" % (_J(host_id), _J(cfg))


def _unidad_de(frag_id):
    """«C5-U5-ESC-01» -> ("C5", 5) · «C6P-U3-ESC-01» -> ("C6+", 3)."""
    curso, unidad = frag_id.split("-")[:2]
    return ("C6+" if curso == "C6P" else curso), int(unidad[1:])


def escucha_js(host_id, frag):
    """Het luisterpaneel van een unit: het lange fragment plus de korte audiotaken.

    De korte taken (`escucha_corta_data.py`) hangen bewust aan dezelfde aanroep.
    Ze horen didactisch in hetzelfde paneel, en zo hoeft geen enkele
    unit-generator een extra container of extra regel te krijgen: het component
    zet zijn eigen kaart net ná `host_id` in de DOM. Welke unit het is, staat al
    in de id van het fragment.
    """
    cfg = {
        "title": frag["titulo"],
        "audio": frag["audio"],
        "expectDetalle": 5,
        "situacion": frag["situacion"],
        "guion": frag["guion"],
        "global": frag["global"],
        "detalle": frag["detalle"],
        "vf": frag["vf"],
        "produccion": frag["produccion"],
    }
    js = "buildEscucha(%s,%s);\n" % (_J(host_id), _J(cfg))

    import escucha_corta_data
    cortos = escucha_corta_data.CORTOS.get(_unidad_de(frag["id"]), [])
    # De `clave` gaat NIET mee naar de hub: antwoordsleutels horen in het
    # docentendossier (CLAUDE.md §14), niet op de leerlingpagina.
    frags = [{"etiqueta": f["etiqueta"], "seccion": f["seccion"], "titulo": f["titulo"],
              "tarea": f["tarea"], "audio": f["audio"], "guion": f["guion"]}
             for f in cortos if f["guion"]]
    if frags:
        js += "buildAudioCortos(%s,%s);\n" % (_J(host_id), _J({"fragmentos": frags}))
    return js


def lectura_js(host_id, texto):
    cfg = {
        "titulo": texto["titulo"], "tipo": texto["tipo"],
        "emisor": texto["emisor"], "receptor": texto["receptor"],
        "objetivo": texto["objetivo"],
        "prediccion": texto["prediccion"], "texto": texto["texto"],
        "traduccion": texto.get("traduccion", ""),
        "global": texto["global"], "escanear": texto["escanear"],
        "vf": texto["vf"], "contexto": texto["contexto"],
        "produccion": texto["produccion"],
    }
    return "buildLectura(%s,%s);\n" % (_J(host_id), _J(cfg))


# De typ-oefeningen uit make_vocab_type_games.py verschijnen als motor-spellen;
# dit is de groep waaronder ze in de hub komen te staan.
GRUPO_ESCRIBIR = ["escribe-palabra", "completa-frase", "que-palabra", "dictado", "escribe-frase"]
GRUPO_ESCRIBIR_TITULOS = {
    "escribe-palabra": ("NL → typ het Spaanse woord", "type"),
    "completa-frase": ("vul het woord in de zin in", "type"),
    "que-palabra": ("omschrijving → typ het woord", "type"),
    "dictado": ("dictee: typ wat je hoort", "type"),
    "escribe-frase": ("schrijf zelf een zin", "type"),
}


def grupo_escribir(prefix_bestaat):
    """Bouwt de MOTOR-groep «Escribir» uit de vijf getypte woordenschat-spellen.
    `prefix_bestaat(slug)` zegt of het spelbestand er is, zodat een ontbrekend
    spel niet als dode tegel in de hub belandt."""
    juegos = [[s, GRUPO_ESCRIBIR_TITULOS[s][0], GRUPO_ESCRIBIR_TITULOS[s][1]]
              for s in GRUPO_ESCRIBIR if prefix_bestaat(s)]
    return ["Escribir · typen ✍️", juegos] if juegos else None


CSS_EXTRA = """
.natid{font-size:10px;font-weight:700;color:var(--mut);background:var(--crema,#eee);border-radius:6px;padding:2px 6px;letter-spacing:.04em;vertical-align:middle}
.exsay{border:none;background:var(--gt);color:var(--gd);border-radius:7px;padding:2px 7px;cursor:pointer;font-size:14px}
"""


def retos_js(host_id, curso, unidad):
    """De hub-retos van één unit.

    Alleen de retos met soporte="hub" komen hier; de andere leven in print of in
    de PowerPoint en zouden half overgezet niets toevoegen. De `clave` gaat niet
    mee: antwoordsleutels horen in het docentendossier (CLAUDE.md §14).
    """
    import retos_data
    salida = []
    for r in retos_data.RETOS:
        if r["curso"] != curso or r["unidad"] != unidad or r["soporte"] != "hub":
            continue
        base = {k: r[k] for k in ("num", "nombre", "lente", "gancho_es", "gancho_nl",
                                  "consigna_es", "consigna_nl", "regla")}
        d = r["datos"]
        if r["id"] == "C5-U0-RETO-01":
            base["tipo"] = "grabar"
            base["situaciones"] = [{"es": es, "nl": nl, "pista": p}
                                   for es, nl, p in d["situaciones"]]
            base["items"] = [{"text": "¡Hola! Buenos días", "cue": nl}
                             for _es, nl, _p in d["situaciones"]]
        elif r["id"] == "C5-U0-RETO-09":
            base["tipo"] = "grabar"
            base["situaciones"] = [{"es": "Modelo — %s" % m, "nl": n, "pista": ""}
                                   for n, m in d["modelos"]]
            base["items"] = [{"text": "Mi firma sonora", "cue": "vijf seconden · één klank uitgerekt"}]
        elif r["id"] == "C5-U0-RETO-04":
            base["tipo"] = "detector"
            reglas = sorted({p for _w, ok, p in d["items"] if not ok})
            base["reglas"] = reglas
            base["items"] = [{"palabra": w, "posible": ok, "porque": p,
                              "regla": (reglas.index(p) if not ok else -1)}
                             for w, ok, p in d["items"]]
        elif r["id"] == "C5-U0-RETO-07":
            base["tipo"] = "mapa"
            base["paises"] = [{"iso": i, "nombre": n, "silabas": s} for i, n, s in d["paises"]]
        elif r["id"] == "C5-U1-RETO-05":
            base["tipo"] = "articulo"
            reglas = {k: t for k, t in d["reglas"]}
            base["reglas"] = [{"clave": k, "texto": t} for k, t in d["reglas"]]
            base["objetos"] = [{"palabra": w, "articulo": art, "regla": k,
                                "porque": reglas[k]} for w, art, k in d["objetos"]]
        elif r["id"] == "C5-U1-RETO-07":
            base["tipo"] = "escena"
            base["escena"] = [{"x": x, "y": y, "w": w, "h": h, "forma": f, "color": c,
                               "es": es, "nl": nl, "cuando": cu}
                              for x, y, w, h, f, c, es, nl, cu in d["escena"]]
            base["marco"] = d["marco"]
        elif r["id"] == "C5-U1-RETO-10":
            base["tipo"] = "grabar"
            base["situaciones"] = [{"es": m, "nl": "", "pista": ""} for m in d["marco"]]
            base["items"] = [{"text": "Te presento a mi compañero/a",
                              "cue": "één minuut, derde persoon, voor iemand die geen "
                                     "Nederlands kent"}]
        elif r["id"] == "C5-U2-RETO-04":
            base["tipo"] = "retrato"
            base["retratos"] = [{"n": n, "pelo": pelo, "gafas": "lleva" in gaf,
                                 "sonrie": son == "sonríe"}
                                for n, pelo, gaf, son, _adj in d["retratos"]]
            base["descripciones"] = [{"correcto": n, "texto": t} for n, t in d["descripciones"]]
        elif r["id"] == "C5-U2-RETO-07":
            base["tipo"] = "grabar"
            base["situaciones"] = [{"es": t, "nl": "", "pista": ""} for _q, t in d["guion"]]
            base["items"] = [{"text": "Mi respuesta a Curro",
                              "cue": "dertig seconden · beantwoord zijn drie vragen"}]
        elif r["id"] == "C5-U2-RETO-09":
            base["tipo"] = "voces"
            base["voces"] = [{"quien": q, "texto": t} for q, t in d["voces"]]
        elif r["id"] == "C5-U3-RETO-05":
            base["tipo"] = "opciones"
            base["items"] = [{"enunciado": e, "correcta": c, "opciones": o, "audio": True,
                              "porque": "let op het uur"} for e, c, o in d["items"]]
        elif r["id"] == "C5-U3-RETO-04":
            base["tipo"] = "grabar"
            base["situaciones"] = [{"es": m, "nl": "", "pista": ""} for m in d["marco"]]
            base["items"] = [{"text": "Mi día en 60 segundos",
                              "cue": "exact een minuut · pas de inhoud aan, niet je tempo"}]
        elif r["id"] == "C5-U3-RETO-09":
            base["tipo"] = "voces"
            base["voces"] = [{"quien": "Frase %d" % k, "texto": f}
                             for k, (f, _sub) in enumerate(d["frases"], 1)]
        elif r["id"] == "C5-U4-RETO-02":
            base["tipo"] = "voces"
            base["voces"] = [{"quien": t, "texto": g} for t, g in d["playlist"]]
        elif r["id"] == "C5-U4-RETO-06":
            base["tipo"] = "grabar"
            base["situaciones"] = [{"es": m, "nl": "", "pista": ""} for m in d["marco"]]
            base["items"] = [{"text": "Antes y ahora",
                              "cue": "vier contrasten · alles in het presente"}]
        elif r["id"] == "C5-U4-RETO-09":
            base["tipo"] = "opciones"
            base["items"] = [{"enunciado": nl, "correcta": c, "opciones": o, "porque": p}
                             for nl, c, o, p in d["items"]]
        elif r["id"] == "C5-U5-RETO-01":
            # de stap wordt voorgelezen, niet getoond: daarom audio
            base["tipo"] = "opciones"
            base["items"] = [{"enunciado": paso, "correcta": c, "opciones": o, "audio": True,
                              "porque": "let op de hoeveelheid, niet op het product"}
                             for paso, c, o in d["pasos_receta"]]
        elif r["id"] == "C5-U5-RETO-06":
            base["tipo"] = "opciones"
            base["items"] = [{"enunciado": "«%s» — ¿cuánto es eso?" % expr,
                              "correcta": c, "opciones": o, "porque": p}
                             for expr, c, o, p in d["items"]]
        elif r["id"] == "C5-U5-RETO-09":
            base["tipo"] = "grabar"
            base["situaciones"] = [{"es": m, "nl": "", "pista": ""} for m in d["marco"]]
            base["items"] = [{"text": "Mi receta en directo",
                              "cue": "één minuut · minstens vijf van de zeven kookwerkwoorden: "
                                     + " · ".join(d["verbos"])}]
        elif r["id"] == "C5-U6-RETO-06":
            base["tipo"] = "opciones"
            base["items"] = [{"enunciado": e, "correcta": c, "opciones": o, "porque": p}
                             for e, c, o, p in d["items"]]
        elif r["id"] == "C5-U6-RETO-09":
            base["tipo"] = "grabar"
            base["situaciones"] = [{"es": m, "nl": "", "pista": ""} for m in d["marco"]]
            base["items"] = [{"text": "Mi anuncio de radio",
                              "cue": "exact 20 seconden · één kledingstuk uit: "
                                     + " · ".join(d["prendas"])}]
        elif r["id"] == "C5-U6-RETO-10":
            base["tipo"] = "opciones"
            base["items"] = [{"enunciado": e, "correcta": c, "opciones": o, "porque": p}
                             for e, c, o, p in d["items"]]
        else:
            continue
        salida.append(base)
    if not salida:
        return ""
    return "buildRetos(%s,%s);\n" % (_J(host_id), _J({"retos": salida}))
