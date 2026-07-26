#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Regenereert de twee U0-motorspellen waarvan de pool < 12 was, zodat ELK
# U0-spel een pool >= 12 items heeft (U5-model: herspelen geeft nieuwe reeksen).
# De overige es-u0-*.json bestanden hebben al pools >= 12 en blijven ongemoeid.
# Run:  python3 make_u0_games.py   →   daarna:  node build.mjs
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(HERE, "content")

# ---- 1) País ↔ gentilicio (was 6 → nu 14 paren) ----
gentilicios = {
    "id": "es-u0-gentilicios",
    "title": "País ↔ gentilicio",
    "subtitle": "U0 · el mundo hispano — land en nationaliteit",
    "lang": "es",
    "template": "match",
    "options": {"chunk": 6, "audio": False},
    "match": {
        "prompt": "Verbind elk land met de nationaliteit (gentilicio)",
        "pairs": [
            {"a": "Bélgica", "b": "belga"},
            {"a": "España", "b": "español"},
            {"a": "México", "b": "mexicano"},
            {"a": "Colombia", "b": "colombiano"},
            {"a": "Perú", "b": "peruano"},
            {"a": "Argentina", "b": "argentino"},
            {"a": "Chile", "b": "chileno"},
            {"a": "Cuba", "b": "cubano"},
            {"a": "Venezuela", "b": "venezolano"},
            {"a": "Ecuador", "b": "ecuatoriano"},
            {"a": "Bolivia", "b": "boliviano"},
            {"a": "Guatemala", "b": "guatemalteco"},
            {"a": "Costa Rica", "b": "costarricense"},
            {"a": "Puerto Rico", "b": "puertorriqueño"},
        ],
    },
}

# ---- 2) Lenguaje de clase (was 10 → nu 14 items) ----
lenguaje = {
    "id": "es-u0-lenguaje-de-clase",
    "title": "Lenguaje de clase",
    "subtitle": "U0 · vul de juiste klaszin aan",
    "lang": "es",
    "template": "cloze",
    "options": {"rounds": 14, "audio": False},
    "cloze": {
        "prompt": "Kies het juiste woord (lenguaje de clase)",
        "items": [
            {"stimulus": "¿Cómo se ___ «mochila» en español?", "options": ["dice", "llama", "escribe"], "answer": "dice", "tag": "clase", "sub": "Hoe zeg je …?"},
            {"stimulus": "¿Qué ___ «parada»?", "options": ["significa", "dice", "tiene"], "answer": "significa", "tag": "clase", "sub": "Wat betekent …?"},
            {"stimulus": "Más ___, por favor.", "options": ["despacio", "rápido", "alto"], "answer": "despacio", "tag": "clase", "sub": "Trager, a.u.b."},
            {"stimulus": "¿Puedes ___, por favor?", "options": ["repetir", "hablar", "comer"], "answer": "repetir", "tag": "clase", "sub": "Kun je herhalen?"},
            {"stimulus": "No ___ , profe.", "options": ["entiendo", "tengo", "voy"], "answer": "entiendo", "tag": "clase", "sub": "Ik begrijp het niet"},
            {"stimulus": "No ___ la respuesta.", "options": ["sé", "es", "hay"], "answer": "sé", "tag": "clase", "sub": "Ik weet het niet"},
            {"stimulus": "¿Cómo se ___ tu nombre?", "options": ["escribe", "dice", "abre"], "answer": "escribe", "tag": "clase", "sub": "Hoe schrijf je …?"},
            {"stimulus": "Tengo una ___.", "options": ["pregunta", "palabra", "letra"], "answer": "pregunta", "tag": "clase", "sub": "Ik heb een vraag"},
            {"stimulus": "¿Puedes ___ tu nombre, letra por letra?", "options": ["deletrear", "repetir", "cerrar"], "answer": "deletrear", "tag": "clase", "sub": "Kun je spellen?"},
            {"stimulus": "Muchas gracias. — Por ___.", "options": ["favor", "nada", "fin"], "answer": "favor", "tag": "clase", "sub": "por favor = alsjeblieft"},
            {"stimulus": "Abre el ___ en la página diez.", "options": ["libro", "mapa", "lápiz"], "answer": "libro", "tag": "clase", "sub": "Doe je boek open"},
            {"stimulus": "Levanta la ___ para hablar.", "options": ["mano", "voz", "letra"], "answer": "mano", "tag": "clase", "sub": "Steek je hand op"},
            {"stimulus": "¿Está ___ o mal?", "options": ["bien", "aquí", "hoy"], "answer": "bien", "tag": "clase", "sub": "Is het goed of fout?"},
            {"stimulus": "¿Cómo se ___ esta palabra?", "options": ["pronuncia", "abre", "cierra"], "answer": "pronuncia", "tag": "clase", "sub": "Hoe spreek je dit uit?"},
        ],
    },
}

for pack in (gentilicios, lenguaje):
    path = os.path.join(CONTENT, pack["id"] + ".json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(pack, fh, ensure_ascii=False, indent=2)
    n = len(pack.get("match", pack.get("cloze", {})).get("pairs", pack.get("cloze", {}).get("items", [])))
    print(f"geschreven: {pack['id']}.json  (pool = {n})")
