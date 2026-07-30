#!/usr/bin/env python3
"""Genereert PRODUCTIEVE typ-oefeningen (template `type`) uit de bestaande
woordenschat-data van een unit — de ontbrekende bovenkant van de leerladder.

Waarom: de units hadden 82 woordenschat-spellen, allemaal receptief
(koppelen/memory/aanwijzen). De fasen «ophalen» en «gestuurd produceren» uit
CLAUDE.md §14 ontbraken. Alle data die daarvoor nodig is stond al klaar in
`u<N>_vocab.json`: es · nl · soort · ej (voorbeeldzin) · grp (cluster).

Maakt per unit tot 5 oefeningen, elk met 3 rondes:
  1. escribe-palabra   NL → typ het Spaanse woord (letterhint)
  2. completa-frase    voorbeeldzin met gat → typ het woord (betekenis uit context)
  3. que-palabra       cluster-cue + omschrijving → typ het woord
  4. dictado           TTS spreekt → typ wat je hoort
  5. escribe-frase     open productie: typ een zin met dit woord (+ modeloplossing)

Gebruik:
    python3 make_vocab_type_games.py C5 3          # C5 unit 3
    python3 make_vocab_type_games.py C6+ 2
    python3 make_vocab_type_games.py C5 3 --dry    # alleen tonen, niets schrijven
"""
import argparse, json, os, re, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, "content")

COURSES = {
    "C5":  dict(vocab="01-cursussen/05-a1/U{n}/u{n}_vocab.json",     pref="es-u{n}-",        color="#2E8E68"),
    "C6+": dict(vocab="01-cursussen/06-vervolg/U{n}/u{n}_vocab.json", pref="es-c6plus-u{n}-", color="#8B5E9E"),
}
ALIAS = {"c5":"C5","c6+":"C6+","c6plus":"C6+"}

PER_ROUND = 12      # items per ronde (gesloten typen)
PER_ROUND_OPEN = 8  # open productie is trager
SERIES = 3          # drie rondes, afgesproken met de auteur

def nfc(s): return unicodedata.normalize("NFC", str(s))
def strip_art(s): return re.sub(r"^(el|la|los|las|un|una)\s+", "", nfc(s).strip(), flags=re.I).strip()

def letterhint(word):
    """e_ p____  — eerste letter per woord zichtbaar, rest streepjes."""
    out = []
    for w in nfc(word).split():
        out.append(w[0] + "_" * (len(w) - 1) if len(w) > 1 else w)
    return " ".join(out)

PAREN = re.compile(r"\s*\(([^)]*)\)")

def clean_es(es):
    """Splitst het bronveld in (typbare vorm, annotatie, optionele staart).

    De woordenschat gebruikt haakjes voor twee heel verschillende dingen:
      · didactische annotatie   despertarse (e→ie) · querer (+ infinitivo)
        → NIET intypen; wordt een hint.
      · optioneel taalonderdeel jugar (a) · tocar (la guitarra) · quedar (con)
        → beide varianten aanvaarden.
    """
    es = nfc(es).strip()
    ann, opt = [], []
    def take(m):
        inner = m.group(1).strip()
        # pijl, plus of losse afkorting = metataal, geen Spaans om te typen
        if re.search(r"[→+]|infinitiv|inf\.|pl\.|sing\.", inner, flags=re.I):
            ann.append(inner)
        else:
            opt.append(inner)
        return ""
    base = PAREN.sub(take, es).strip()
    base = re.sub(r"\s{2,}", " ", base)
    return base, " · ".join(ann), opt


def typable(w):
    """False voor bronvormen die je onmogelijk kan intypen (paradigma-lijsten)."""
    es = nfc(w["es"])
    return "/" not in es and len(clean_es(es)[0]) > 0


def accepted(w):
    """Aanvaarde antwoorden: met/zonder lidwoord, met/zonder optionele staart."""
    base, _ann, opt = clean_es(w["es"])
    forms = [base]
    for o in opt:                      # jugar (a) → «jugar a» én «jugar»
        forms.insert(0, (base + " " + o).strip())
    out = []
    for f in list(forms):
        if f and f not in out:
            out.append(f)
        bare = strip_art(f)
        if bare and bare not in out:
            out.append(bare)
    return out


def base_form(w):
    return clean_es(w["es"])[0]


def annotation(w):
    return clean_es(w["es"])[1]

def build(course, n, dry=False):
    spec = COURSES[course]
    vpath = os.path.join(ROOT, spec["vocab"].format(n=n))
    if not os.path.exists(vpath):
        sys.exit("Geen woordenschat gevonden: %s" % vpath)
    vocab = json.load(open(vpath, encoding="utf-8"))
    pref = spec["pref"].format(n=n)
    unit = "%s · U%d" % (course, n)
    games, report = [], []

    def emit(slug, title, subtitle, mode, items, per_round, extra=None):
        if len(items) < per_round:
            report.append(("✗", slug, "te weinig items (%d < %d) — overgeslagen" % (len(items), per_round)))
            return
        cfg = {
            "id": pref + slug, "title": title, "subtitle": subtitle,
            "lang": "es", "template": "type",
            "options": {"rounds": per_round, "series": SERIES, "audio": False},
            "type": {"prompt": subtitle.split(" · ")[0], "mode": mode, "items": items},
        }
        if extra: cfg["type"].update(extra)
        games.append(cfg)
        rounds_fresh = "vers" if len(items) >= per_round * SERIES else "met herhaling"
        report.append(("✓", slug, "pool %d · %d×%d items (%s)" % (len(items), SERIES, per_round, rounds_fresh)))

    # ---- 1 · escribe la palabra (NL → ES), losse woorden ----
    items = []
    for w in vocab:
        if not typable(w):
            continue
        base = base_form(w)
        if len(base.split()) > 3 or base.endswith("?"):
            continue
        sub = " · ".join(x for x in (w.get("soort", ""), annotation(w)) if x)
        items.append({"stimulus": w["nl"], "answers": accepted(w),
                      "hint": letterhint(strip_art(base)), "tag": w.get("grp", "vocab"),
                      "sub": sub})
    emit("escribe-palabra", "Escribe la palabra",
         unit + " · schrijf het Spaanse woord (letterhint als steun)", "closed", items, PER_ROUND)

    # ---- 2 · completa la frase (voorbeeldzin met gat) ----
    items = []
    for w in vocab:
        if not typable(w):
            continue
        ej = nfc(w.get("ej", ""))
        kern = strip_art(base_form(w))
        if not ej or not kern:
            continue
        m = re.search(re.escape(kern), ej, flags=re.I)
        if not m:
            continue                      # woord staat vervoegd/verbogen in de zin → niet bruikbaar
        gap = ej[:m.start()] + "___" + ej[m.end():]
        items.append({"stimulus": gap, "answers": accepted(w) + [kern],
                      "tag": w.get("grp", "vocab"), "sub": w["nl"]})
    emit("completa-frase", "Completa la frase",
         unit + " · vul het ontbrekende woord in (betekenis uit de context)", "closed", items, PER_ROUND)

    # ---- 3 · ¿qué palabra? (cluster + soort als cue) ----
    items = []
    for w in vocab:
        grp = w.get("grp")
        if not grp or not typable(w):
            continue
        base = base_form(w)
        if len(base.split()) > 3:
            continue
        items.append({"stimulus": "%s → «%s»" % (grp, w["nl"]), "answers": accepted(w),
                      "hint": letterhint(strip_art(base)), "tag": grp,
                      "sub": " · ".join(x for x in (w.get("soort", ""), annotation(w)) if x)})
    emit("que-palabra", "¿Qué palabra?",
         unit + " · van thema naar woord (ophalen zonder zin)", "closed", items, PER_ROUND)

    # ---- 4 · dictado (TTS → typen) ----
    items = [{"stimulus": "🔊 " + base_form(w), "answers": accepted(w),
              "tag": w.get("grp", "vocab"), "sub": w["nl"]}
             for w in vocab if typable(w)]
    emit("dictado", "Dictado",
         unit + " · luister en typ · lees eerst, dan afdekken", "closed", items, PER_ROUND)

    # ---- 5 · escribe una frase (open productie) ----
    items = []
    for w in vocab:
        if not typable(w):
            continue
        ej, base = nfc(w.get("ej", "")), base_form(w)
        if not ej or len(ej.split()) < 3:
            continue
        items.append({"stimulus": "Escribe una frase con «%s»" % base,
                      "must": [strip_art(base)], "model": ej,
                      "tag": w.get("grp", "vocab"), "sub": w["nl"]})
    emit("escribe-frase", "Escribe una frase",
         unit + " · vrije productie · structuurcheck + modeloplossing", "open", items, PER_ROUND_OPEN)

    print("\n%s — %d woorden in de bron" % (unit, len(vocab)))
    for mark, slug, info in report:
        print("  %s %-18s %s" % (mark, slug, info))
    if dry:
        print("\n(dry run — niets geschreven)")
        return games
    for g in games:
        p = os.path.join(OUT, g["id"] + ".json")
        open(p, "w", encoding="utf-8").write(json.dumps(g, ensure_ascii=False, indent=2))
    print("\n%d oefeningen geschreven naar content/" % len(games))
    return games


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("course"); ap.add_argument("unit", type=int)
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    course = ALIAS.get(a.course.lower(), a.course)
    if course not in COURSES:
        sys.exit("Kies C5 of C6+")
    build(course, a.unit, a.dry)
