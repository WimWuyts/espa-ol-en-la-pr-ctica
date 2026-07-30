#!/usr/bin/env python3
"""Getypte woordenschat-drills voor de panelen «Vocabulario» van elke hub.

Het gat dat dit dicht: `hub_drills.buildType` bestond wel, maar werd in geen
enkele generator aangeroepen. De panelen Vocabulario en Gramática bevatten
daardoor uitsluitend klik- en koppelwerk — de leerling herkende, maar schreef
nooit iets. Fase 4 en 5 uit CLAUDE.md §14 (ophalen · gestuurd produceren)
ontbraken op de digitale pagina.

Eén bron: `u<N>_vocab.json` (es · nl · soort · ej · grp · tier). Daaruit komen
drie drills, allemaal in het paneel zelf (dus zichtbaar zonder tabwissel):

  1. escribe la palabra  NL → typ het Spaanse woord            (letterhint)
  2. completa la frase   de voorbeeldzin met een gat           (betekenis uit context)
  3. dictado             TTS spreekt → typ wat je hoort        (klank → schrift)

De curatielogica (haakjes, lidwoorden, paradigma-vormen) is dezelfde als in
`spaans-motor/make_vocab_type_games.py`, zodat een woord in het spel en in het
paneel op precies dezelfde manier wordt afgerekend.

Gebruik in een generator:

    import hub_type_sets
    ...
    <div class="card ex" id="vt_palabra"></div>   # in het paneel vocab
    ...
    JS += hub_type_sets.vocab_type_js(vocab)      # naast buildInlineExercises()
"""
import json
import re
import unicodedata

PER = 12          # items per drill (gesloten typen) — afgesproken met de auteur
PER_DICT = 10     # dictado is trager

PAREN = re.compile(r"\s*\(([^)]*)\)")
ART = re.compile(r"^(el|la|los|las|un|una)\s+", re.I)


def nfc(s):
    return unicodedata.normalize("NFC", str(s))


def strip_art(s):
    return ART.sub("", nfc(s).strip()).strip()


def clean_es(es):
    """(typbare vorm, annotatie, optionele staarten) — zie make_vocab_type_games.py.

    Haakjes betekenen twee dingen: didactische annotatie «querer (+ infinitivo)»
    die je níét intypt, en een optioneel taaldeel «jugar (a)» dat je wél mag
    intypen. Ze uit elkaar houden voorkomt dat de leerling «(e→ie)» moet typen.
    """
    es = nfc(es).strip()
    ann, opt = [], []

    def take(m):
        inner = m.group(1).strip()
        if re.search(r"[→+]|infinitiv|inf\.|pl\.|sing\.", inner, flags=re.I):
            ann.append(inner)
        else:
            opt.append(inner)
        return ""

    base = re.sub(r"\s{2,}", " ", PAREN.sub(take, es).strip())
    return base, " · ".join(ann), opt


def letterhint(word):
    """e_ p____ — eerste letter per woord zichtbaar, de rest streepjes."""
    out = []
    for w in nfc(word).split():
        out.append(w[0] + "_" * (len(w) - 1) if len(w) > 1 else w)
    return " ".join(out)


def typable(w):
    es = nfc(w.get("es", ""))
    return "/" not in es and len(clean_es(es)[0]) > 0


def accepted(w):
    """Aanvaarde antwoorden: met/zonder lidwoord, met/zonder optionele staart."""
    base, _ann, opt = clean_es(w["es"])
    forms = [base]
    for o in opt:
        forms.insert(0, (base + " " + o).strip())
    out = []
    for f in forms:
        for cand in (f, strip_art(f)):
            if cand and cand not in out:
                out.append(cand)
    return out


def _short(w, maxwords=3):
    base = clean_es(w["es"])[0]
    return base and len(base.split()) <= maxwords and not base.endswith("?")


def _rank(w):
    """Productieve woorden eerst: die moet de leerling actief kunnen schrijven."""
    return (0 if w.get("tier") == "prod" else 1, len(clean_es(w["es"])[0]))


# --------------------------------------------------------------------------- #
#  1 · escribe la palabra — NL → ES
# --------------------------------------------------------------------------- #
def _items_palabra(vocab, n):
    items = []
    for w in sorted([v for v in vocab if typable(v) and _short(v)], key=_rank):
        base = clean_es(w["es"])[0]
        ann = clean_es(w["es"])[1]
        why = " · ".join(x for x in (w.get("soort", ""), ann) if x)
        items.append({"q": w["nl"], "ans": base, "alt": accepted(w)[1:],
                      "hint": letterhint(strip_art(base)),
                      "why": why or w.get("grp", "")})
        if len(items) >= n:
            break
    return items


# --------------------------------------------------------------------------- #
#  2 · completa la frase — voorbeeldzin met gat
# --------------------------------------------------------------------------- #
def _gap(ej, base):
    """Zoekt de (eventueel verbogen) vorm in de voorbeeldzin en maakt er een gat van.

    De voorbeeldzinnen staan in lopende tekst: «la letra» verschijnt er als
    «letras». Daarom matchen we de kale stam met een optionele meervoudsuitgang;
    het weggehaalde woord zelf wordt het verwachte antwoord.
    """
    kern = strip_art(base)
    if not kern or len(kern.split()) > 3:
        return None
    stam = re.escape(kern)
    pat = re.compile(r"(?<![\wáéíóúñü])(%s(?:es|s)?)(?![\wáéíóúñü])" % stam, re.I)
    m = pat.search(nfc(ej))
    if not m:
        return None
    weg = m.group(1)
    return nfc(ej)[:m.start()] + "___" + nfc(ej)[m.end():], weg


def _items_frase(vocab, n, skip):
    items = []
    for w in sorted([v for v in vocab if typable(v) and v.get("ej")], key=_rank):
        base = clean_es(w["es"])[0]
        if base in skip:
            continue
        g = _gap(w["ej"], base)
        if not g:
            continue
        zin, weg = g
        alt = [a for a in {strip_art(base), base, weg.lower()} if a and a != weg]
        items.append({"q": zin, "ans": weg, "alt": alt,
                      "hint": letterhint(weg), "why": w["nl"]})
        if len(items) >= n:
            break
    return items


# --------------------------------------------------------------------------- #
#  3 · dictado — luister en schrijf
# --------------------------------------------------------------------------- #
def _items_dictado(vocab, n, skip):
    items = []
    for w in sorted([v for v in vocab if typable(v) and _short(v, 2)], key=_rank):
        base = clean_es(w["es"])[0]
        if base in skip:
            continue
        items.append({"q": "···", "say": base, "ans": base,
                      "alt": accepted(w)[1:], "why": w["nl"]})
        if len(items) >= n:
            break
    return items


# --------------------------------------------------------------------------- #
#  publieke API
# --------------------------------------------------------------------------- #
SLOTS_HTML = """    <h3 class="subh">✍️ Escribe tú — van herkennen naar schrijven</h3>
    <p class="lead">Hier klik je niet: je <b>typt</b> het antwoord zelf. Fout? Je krijgt een
    <b>pista</b> en mag opnieuw. <span class="gloss">ophalen → gestuurd produceren · accenten worden
    getoond in de correctie.</span></p>
    <div class="card ex escribe" id="vt_palabra"></div>
    <div class="card ex escribe" id="vt_frase"></div>
    <div class="card ex escribe" id="vt_dictado"></div>
"""


def vocab_type_js(vocab, per=PER, per_dict=PER_DICT, func="buildVocabType"):
    """JS-blok met de drie getypte woordenschat-drills + de aanroep ervan."""
    pal = _items_palabra(vocab, per)
    skip = {i["ans"] for i in pal}
    fra = _items_frase(vocab, per, skip)
    skip |= {i["ans"] for i in fra}
    dic = _items_dictado(vocab, per_dict, skip)
    if len(dic) < 4:                       # kleine unit: dan liever niets dan een stompje
        dic = []

    def j(x):
        return json.dumps(x, ensure_ascii=False)

    blocks = [
        ("vt_palabra", "Escribe la palabra", "Lees het Nederlands en <b>typ</b> het Spaanse woord. "
         "Klik op <b>pista</b> voor de beginletters.", "soft", pal),
        ("vt_frase", "Completa la frase", "Vul het ontbrekende woord in. De zin geeft je de betekenis; "
         "let op enkelvoud of meervoud.", "soft", fra),
    ]
    out = ["function %s(){" % func]
    for slot, title, desc, mode, items in blocks:
        if len(items) < 4:
            continue
        out.append(" buildType('%s',{title:%s,desc:%s,accents:'%s',perBlock:%d,expect:%d,items:%s});"
                   % (slot, j(title), j(desc), mode, per, len(items), j(items)))
    if dic:
        out.append(" buildType('vt_dictado',{title:%s,desc:%s,accents:'soft',speak:true,"
                   "perBlock:%d,expect:%d,items:%s});"
                   % (j("Dictado — escucha y escribe"),
                      j("Klik op 🔊, luister en <b>schrijf</b> het woord. Zo koppel je klank aan schriftbeeld."),
                      per_dict, len(dic), j(dic)))
    out.append("}")
    out.append("%s();" % func)
    return "\n".join(out) + "\n"


if __name__ == "__main__":                 # snelle controle: hoeveel items per unit?
    import os
    import sys
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    paden = [("C5", n, f"{root}/01-cursussen/05-a1/U{n}/u{n}_vocab.json") for n in range(9)]
    paden += [("C6+", n, f"{root}/01-cursussen/06-vervolg/U{n}/u{n}_vocab.json") for n in range(9)]
    for cur, n, p in paden:
        if not os.path.exists(p):
            continue
        v = json.load(open(p, encoding="utf-8"))
        pal = _items_palabra(v, PER)
        skip = {i["ans"] for i in pal}
        fra = _items_frase(v, PER, skip)
        skip |= {i["ans"] for i in fra}
        dic = _items_dictado(v, PER_DICT, skip)
        print("%-4s U%d  woorden %3d → palabra %2d · frase %2d · dictado %2d  = %2d typvelden"
              % (cur, n, len(v), len(pal), len(fra), len(dic), len(pal) + len(fra) + len(dic)))
