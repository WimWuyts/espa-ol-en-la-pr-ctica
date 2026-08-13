#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""«Cien formas» op de digitale pagina — de honderd invulvormen uit C5 U1 §3.3.

De auteur leverde honderd invuloefeningen op het presente regular aan. Ze staan
in de gedrukte bundel als §3.3, en hier — met zelfcorrectie, want de bundel mag
geen oplossingen dragen (CLAUDE.md §14) en die honderd vormen zelf nakijken is
niet te doen.

Vorm: tien blokken van tien, op de bestaande `buildType`-motor uit `hub_drills`.
Accenten staan op **strict**: bij vosotros (habláis, coméis, vivís) ís de tilde
de leerstof, dus die mag niet wegvallen. Elk item krijgt een `hint` (eerste
letter + een streepje per ontbrekende letter) en een `why` met de persoon, zodat
een fout antwoord uitlegt wáár het misging in plaats van alleen «fout».

De tekstjes 61–100 komen als aparte drill: daar staat het onderwerp soms een zin
eerder, en dat is een ander soort denkwerk dan bij een losse zin.

    import hub_presente
    HTML = HTML.replace("__PRESENTESLOT__", hub_presente.slot())
    JS  += hub_presente.js()
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import presente_data as PD          # noqa: E402

PERSONA = {
    "o": "yo", "as": "tú", "a": "él/ella/usted", "amos": "nosotros",
    "áis": "vosotros", "an": "ellos/ustedes",
    "es": "tú", "e": "él/ella/usted", "emos": "nosotros", "éis": "vosotros",
    "en": "ellos/ustedes", "imos": "nosotros", "ís": "vosotros",
}


def _persona(inf, ans):
    """De persoon achter een vorm — voor de uitleg bij een fout antwoord."""
    fin = ans[len(inf) - 2:] if ans.lower().startswith(inf[:-2].lower()) else ""
    return PERSONA.get(fin, "")


def _hint(ans):
    """Eerste letter, daarna een streepje per ontbrekende letter."""
    return ans[0] + "_" * (len(ans) - 1)


def _item(pregunta, inf, ans):
    por = _persona(inf, ans)
    return {"q": pregunta.replace("{}", "___"), "ans": ans, "hint": _hint(ans),
            "why": ("%s · %s" % (inf, por)) if por else inf}


def items_sueltas():
    return [_item(q, inf, a)
            for _tit, _nl, its in PD.SUELTAS
            for _n, q, inf, a in its]


def items_textos():
    """Elk gat krijgt zijn tekstje mee als context; anders is het niet te maken.

    De ándere gaten van hetzelfde tekstje blijven staan als infinitief tussen
    haakjes. Ze invullen zou de vier volgende vragen weggeven; ze wegdenken zou
    de zin onleesbaar maken. De titel gaat als platte tekst mee: `buildType`
    escapet zijn vraagtekst, dus opmaak zou als tekens op het scherm belanden.
    """
    out = []
    for tit, _nl, cuerpo, huecos in PD.TEXTOS:
        partes = cuerpo.split("{}")
        for k, (_n, inf, a) in enumerate(huecos):
            texto = ""
            for i, p in enumerate(partes):
                texto += p
                if i < len(huecos):
                    texto += "___" if i == k else "(%s)" % huecos[i][1]
            out.append({"q": "«%s» — %s" % (tit, texto), "ans": a,
                        "hint": _hint(a), "why": "%s · %s" % (inf, _persona(inf, a) or "")})
    return out


SLOT = """    <h3 class="subh">💯 Cien formas — el presente sin pensar</h3>
    <p class="lead">De honderd invulvormen uit §3.3 van je boek, hier met zelfcorrectie.
    <span class="gloss">Accenten tellen mee: bij vosotros is de tilde de leerstof
    (habláis, coméis, vivís).</span></p>
    <div class="card ex escribe" id="pr_sueltas"></div>
    <div class="card ex escribe" id="pr_textos"></div>
"""


def slot():
    return SLOT


def js():
    sueltas = items_sueltas()
    textos = items_textos()
    out = ["function buildPresente(){"]
    out.append(" buildType('pr_sueltas',{title:%s,desc:%s,accents:'strict',perBlock:10,expect:%d,items:%s});"
               % (json.dumps("Frases sueltas · 1–60", ensure_ascii=False),
                  json.dumps("Escribe la forma correcta. El sujeto te dice la terminación. "
                             "· Vul de juiste vorm in; het onderwerp bepaalt de uitgang.",
                             ensure_ascii=False),
                  len(sueltas), json.dumps(sueltas, ensure_ascii=False)))
    out.append(" buildType('pr_textos',{title:%s,desc:%s,accents:'strict',perBlock:5,expect:%d,items:%s});"
               % (json.dumps("Textos cortos · 61–100", ensure_ascii=False),
                  json.dumps("Aquí el sujeto puede estar una frase más arriba. Lee todo el texto "
                             "antes de escribir. · Het onderwerp staat soms een zin eerder.",
                             ensure_ascii=False),
                  len(textos), json.dumps(textos, ensure_ascii=False)))
    out.append("}")
    out.append("buildPresente();")
    return "\n".join(out) + "\n"


def controla():
    """De pista moet even lang zijn als het antwoord — anders telt de leerling
    streepjes die er niet zijn en raakt hij het antwoord juist kwijt."""
    todo = items_sueltas() + items_textos()
    assert len(todo) == 100, "verwacht 100 vormen, kreeg %d" % len(todo)
    for it in todo:
        assert len(it["hint"]) == len(it["ans"]), (it["ans"], it["hint"])
        assert "___" in it["q"], it["q"]
    sin = [it["ans"] for it in todo if it["why"].endswith("· ")]
    assert not sin, "geen persoon herkend bij: %s" % sin[:5]


controla()


if __name__ == "__main__":
    print("%d losse zinnen + %d tekstgaten = %d vormen"
          % (len(items_sueltas()), len(items_textos()),
             len(items_sueltas()) + len(items_textos())))
