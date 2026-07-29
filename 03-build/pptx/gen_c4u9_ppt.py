#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_c4u9_ppt.py — Interactieve PowerPoint C4 · Unidad 9 «Planes y obligaciones»
================================================================================
Gedeelde builder (één bron) → TWEE decks:
  · C4_U9_docente.pptx  — docentversie: vrije navigatie; antwoorden verschijnen bij
    klik (fade) + volledige oplossing & didactiek in de spreker-notities.
  · C4_U9_alumno.ppsx   — leerlingversie: GEEN docentnotities, GEEN kiosk; gewone
    diavoorstelling waarin de antwoorden/oplossingen bij klik verschijnen.

ECHTE interactiviteit: op elke oefendia wordt <p:timing>-XML geïnjecteerd met
standaard SEQUENTIËLE on-click entrance-animaties (fade-in) in de hoofdsequentie
(mainSeq): elke klik onthult de volgende reveal-shape. + hyperlink-navigatie
(menutegels, ⌂ Menú). Cast-avatars = de ECHTE flat-vector SVG's.

Thema U9: Planes y obligaciones · los planes met ir a + infinitivo (voy a / vas a /
vamos a + het hele werkwoord) · las obligaciones met tener que + infinitivo (tengo
que / tienes que) · tener + sustantivo (tengo hambre · tengo sueño = «ik ben
slaperig» · tengo sed · tengo prisa) · rechazar con educación (no puedo + la razón ·
¡qué pena! · otro día, ¿vale?). Eindtaak «Mi finde».
Huisstijl: unitkleur rood #D64550 (C4). Spaans-eerst + NL-steun. Twee kleurlagen:
cursusrood (navigatie) + functionele taalsemantiek (persoon = blauw · WERKWOORD =
oranje #EA7317 — de dominante laag in deze unit · tijd = paars #7C3AED · rood =
valstrik/ontkenning). Nieuw visueel element: «La máquina de frases» — een zinbouwer
in 3 blokken naast elkaar ([Voy a / Tengo que] + [+ infinitivo] + [estudiar…]) op
twee rijen, met de resulterende zin als on-click reveal.

TWEE VALSTRIKKEN, elk in een eigen opvallend kader (§4-gramática + repaso):
  (1) «ik ben slaperig» = tengo sueño (letterlijk «ik héb slaap») — nooit
      «estoy sueño»/«soy sueño»;
  (2) de «que» is verplicht vóór een werkwoord (tengo que trabajar, niet
      «tengo trabajar») maar valt weg vóór een naamwoord (tengo hambre).

VIDEO: voor aflevering 9 bestaat GEEN YouTube-link. De bron is een Google-Drive-
bestand (file-id 1YlBRdAs4L4fOvmXylmQLlRSJMoRto7Kb, deelrechten reader/anyone).
De online-video-embed gebruikt daarom de Drive-/preview-URL; daarnaast staat er een
gewone hyperlink-knop «▶ Abrir en Drive» als gegarandeerde noodroute (browser).
Internet vereist.

C4-scope: «voy a / vas a / vamos a» en «tengo que / tienes que» zijn VASTE CHUNKS,
géén vervoegingsparadigma van «ir» of «tener» (dat systeem hoort in het 5de jaar,
C5). «ir a + infinitivo» is de A1-manier om over de toekomst te praten — géén
futuro simple.

Bron: 03-build/web/gen_c4u9_kgt.py · gen_c4u9_pdf.py · gen_c4u9_practica.py
"""
import os, zipfile, shutil, math
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.oxml.ns import qn, nsdecls
from pptx.oxml import parse_xml

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
OUT_DOCENTE = os.path.join(HERE, "C4_U9_docente.pptx")
OUT_ALUMNO_PPTX = os.path.join(HERE, "C4_U9_alumno.pptx")
OUT_ALUMNO = os.path.join(HERE, "C4_U9_alumno.ppsx")

# --- build-modus (wordt door build() gezet) ---
MODE = "docente"          # "docente" | "alumno"
def is_alumno():
    return MODE == "alumno"

# ---------------------------------------------------------------- kleuren (kit.json)
G      = RGBColor(0xD6, 0x45, 0x50)  # unitrood C4 (hoofdkleur)
GD     = RGBColor(0xA8, 0x32, 0x3B)  # donkerrood C4
GT     = RGBColor(0xFB, 0xEA, 0xEC)  # rood-tint C4 (vlak)
INK    = RGBColor(0x20, 0x24, 0x2E)  # tekst
MUT    = RGBColor(0x6A, 0x6E, 0x78)  # gedempt
PAPER  = RGBColor(0xFC, 0xFB, 0xF8)  # papier
CREMA  = RGBColor(0xF3, 0xEE, 0xE4)  # warme neutraal
LINE   = RGBColor(0xE4, 0xE3, 0xDE)
RED    = RGBColor(0xDC, 0x26, 0x26)
AMBER  = RGBColor(0xB7, 0x86, 0x0B)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
# functionele taalsemantiek (§13)
F_SUBJ = RGBColor(0x25, 0x63, 0xEB)  # onderwerp/persoon  (blauw)
F_VERB = RGBColor(0xEA, 0x73, 0x17)  # WERKWOORD          (oranje · U9: ir a / tener que — dominante laag)
F_OBJ  = RGBColor(0x1E, 0x9E, 0x74)  # voorwerp           (groen)
F_TIME = RGBColor(0x7C, 0x3A, 0xED)  # tijd               (paars · esta noche · el domingo)
F_PLAC = RGBColor(0x0E, 0x9E, 0x97)  # plaats             (turquoise · en mi casa · en el centro)
F_NEG  = RGBColor(0xDC, 0x26, 0x26)  # ontkenning/waarschuwing (rood)
F_STRA = RGBColor(0xEA, 0xB3, 0x08)  # strategie          (geel)
# cast-accentkleuren
ACC = {
    "lucia": RGBColor(0xE0, 0x7A, 0x5F), "diego": RGBColor(0x5B, 0x8D, 0xEF),
    "valen": RGBColor(0x2F, 0xA8, 0xA0), "nina": RGBColor(0xD6, 0x9A, 0x2E),
    "tu": RGBColor(0x8A, 0x7B, 0xE0), "mochila": G,
}

DISPLAY = "Bricolage Grotesque"  # koppen (fallback: systeem-sans)
BODY    = "Inter"                # tekst  (fallback: systeem-sans)
HAND    = "Caveat"              # notities

EMU_W, EMU_H = Inches(13.333), Inches(7.5)

# --- presentatie-globals (per build opnieuw gezet) ---
prs = None
BLANK = None
SLIDE_LIST = []      # alle slide-objecten in volgorde
REVEALS = []         # (slide, reveal_spid) — verschijnt bij klik (volgorde = klikvolgorde)
MENU_LINKS = []      # (shape, target_index) — hyperlink-navigatie
SOL_NOTES = {}       # id(slide) -> [platte oplossingstekst] (docent-notities)

def new_presentation():
    global prs, BLANK, PAGE, SLIDE_LIST, REVEALS, MENU_LINKS, SOL_NOTES
    prs = Presentation()
    prs.slide_width = EMU_W
    prs.slide_height = EMU_H
    BLANK = prs.slide_layouts[6]
    PAGE = 0
    SLIDE_LIST = []
    REVEALS = []
    MENU_LINKS = []
    SOL_NOTES = {}

# ============================================================ low-level helpers
def slide():
    s = prs.slides.add_slide(BLANK)
    SLIDE_LIST.append(s)
    return s

# ---------------------------------------------------------- interactiviteit
def register_reveal(s, reveal_shape):
    """Registreer een reveal-shape: die start verborgen en verschijnt (entrance-fade)
    bij de VOLGENDE klik in de gewone diavoorstelling. De registratievolgorde bepaalt
    de klikvolgorde binnen één dia (sequentiële on-click entrance in de hoofdsequentie)."""
    REVEALS.append((s, reveal_shape.shape_id))

def link_to(shape, target_index):
    """Klik-actie op shape → spring naar slide met index target_index (hyperlink-navigatie)."""
    MENU_LINKS.append((shape, target_index))

def _click_group(cid, rev):
    """Eén on-click click-groep in de hoofdsequentie: bij de volgende klik verschijnt
    <rev> met een fade-in (entrance). Gebruikt 5 opeenvolgende cTn-id's vanaf cid.
    De buitenste <p:cond delay="indefinite"/> = «bij klik». Dit is exact de canonieke
    structuur die PowerPoint schrijft voor «Fade, Start: On Click» — presetClass=entr
    → PowerPoint houdt <rev> automatisch verborgen tot zijn klik."""
    a, b, c, d, e = cid, cid + 1, cid + 2, cid + 3, cid + 4
    return (
      f'<p:par><p:cTn id="{a}" fill="hold"><p:stCondLst><p:cond delay="indefinite"/></p:stCondLst><p:childTnLst>'
        f'<p:par><p:cTn id="{b}" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>'
          f'<p:par><p:cTn id="{c}" presetID="10" presetClass="entr" presetSubtype="0" fill="hold" grpId="0" nodeType="clickEffect">'
          f'<p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>'
            f'<p:set><p:cBhvr><p:cTn id="{d}" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn>'
            f'<p:tgtEl><p:spTgt spid="{rev}"/></p:tgtEl><p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr>'
            f'<p:to><p:strVal val="visible"/></p:to></p:set>'
            f'<p:animEffect transition="in" filter="fade"><p:cBhvr><p:cTn id="{e}" dur="500"/>'
            f'<p:tgtEl><p:spTgt spid="{rev}"/></p:tgtEl></p:cBhvr></p:animEffect>'
          f'</p:childTnLst></p:cTn></p:par>'
        f'</p:childTnLst></p:cTn></p:par>'
      f'</p:childTnLst></p:cTn></p:par>')

def apply_all_timing():
    """Bouwt per slide met reveals één <p:timing>-boom: tmRoot → mainSeq met per
    reveal-shape één on-click click-groep (sequentieel «verschijnen bij klik»).
    Alle id's zijn uniek binnen de dia (3/4/5/6/7, 8/9/10/11/12, …)."""
    groups = {}      # id(slide) -> list[rev_spid]
    slide_of = {}    # id(slide) -> slide
    order = []
    for s, r in REVEALS:
        k = id(s)
        if k not in groups:
            groups[k] = []; slide_of[k] = s; order.append(k)
        groups[k].append(r)
    n = 0
    total = 0
    for k in order:
        s = slide_of[k]
        cgs = ""; cid = 3
        for r in groups[k]:
            cgs += _click_group(cid, r); cid += 5; total += 1
        xml = (
          f'<p:timing {nsdecls("p", "a")}><p:tnLst><p:par>'
          f'<p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot"><p:childTnLst>'
          f'<p:seq concurrent="1" nextAc="seek"><p:cTn id="2" dur="indefinite" nodeType="mainSeq"><p:childTnLst>'
          f'{cgs}'
          f'</p:childTnLst></p:cTn>'
          f'<p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst>'
          f'<p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst>'
          f'</p:seq></p:childTnLst></p:cTn></p:par></p:tnLst></p:timing>')
        s._element.append(parse_xml(xml))
        n += 1
    return n, total

def apply_hyperlinks():
    for shape, idx in MENU_LINKS:
        if 0 <= idx < len(SLIDE_LIST):
            try:
                shape.click_action.target_slide = SLIDE_LIST[idx]
            except Exception:
                pass

def _set_fill(shape, color):
    if color is None:
        shape.fill.background()
    else:
        shape.fill.solid(); shape.fill.fore_color.rgb = color

def _set_line(shape, color, w=None):
    if color is None:
        shape.line.fill.background()
    else:
        shape.line.color.rgb = color
        if w is not None:
            shape.line.width = Pt(w)

def rect(s, x, y, w, h, fill=None, line=None, lw=1.0, shadow=False, round=False, radius=0.08):
    shp = s.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE if round else MSO_SHAPE.RECTANGLE,
        x, y, w, h)
    _set_fill(shp, fill)
    _set_line(shp, line, lw)
    shp.shadow.inherit = False
    if round:
        try:
            shp.adjustments[0] = radius
        except Exception:
            pass
    if shadow:
        _soft_shadow(shp)
    return shp

def _soft_shadow(shp):
    spPr = shp._element.spPr
    el = spPr.makeelement(qn('a:effectLst'), {})
    sh = el.makeelement(qn('a:outerShdw'),
                        {'blurRad': '90000', 'dist': '38000', 'dir': '5400000', 'rotWithShape': '0'})
    clr = sh.makeelement(qn('a:srgbClr'), {'val': '20242E'})
    alp = clr.makeelement(qn('a:alpha'), {'val': '22000'})
    clr.append(alp); sh.append(clr); el.append(sh); spPr.append(el)

def _p_spacing(p, before=0, after=2, line=None):
    p.space_before = Pt(before); p.space_after = Pt(after)
    if line is not None:
        p.line_spacing = line

def text(s, x, y, w, h, runs, size=16, bold=False, color=INK, font=BODY,
         align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, line=1.06, wrap=True,
         shrink=False):
    """runs = str  OF  list van paragrafen; elke paragraaf = list van
    (tekst, {opts}) tuples. opts: size,bold,color,font,italic."""
    tb = s.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = wrap
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Pt(3)
    tf.margin_top = tf.margin_bottom = Pt(2)
    if shrink:
        from pptx.enum.text import MSO_AUTO_SIZE
        tf.auto_size = MSO_AUTO_SIZE.NONE
    if isinstance(runs, str):
        runs = [[(runs, {})]]
    first = True
    for para in runs:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.alignment = align
        _p_spacing(p, after=2, line=line)
        if isinstance(para, tuple):
            para = [para]
        for txt, o in para:
            r = p.add_run(); r.text = txt
            r.font.size = Pt(o.get("size", size))
            r.font.bold = o.get("bold", bold)
            r.font.italic = o.get("italic", False)
            r.font.name = o.get("font", font)
            r.font.color.rgb = o.get("color", color)
    return tb

def chip(s, x, y, text_str, fill=GT, tcolor=GD, size=11, bold=True, w=None, font=BODY):
    if w is None:
        w = Inches(0.13 + 0.092 * len(text_str))
    h = Inches(0.32)
    shp = rect(s, x, y, w, h, fill=fill, line=None, round=True, radius=0.5)
    tf = shp.text_frame; tf.word_wrap = False
    tf.margin_left = tf.margin_right = Pt(7); tf.margin_top = tf.margin_bottom = Pt(1)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = text_str
    r.font.size = Pt(size); r.font.bold = bold; r.font.name = font; r.font.color.rgb = tcolor
    return shp, w

def avatar(s, name, x, y, d=Inches(0.9)):
    p = os.path.join(ASSETS, f"{name}.png")
    if os.path.exists(p):
        return s.shapes.add_picture(p, x, y, d, d)
    return None

def _flatten_solucion_lines(lines):
    """Zet de solución-regels (str of list van (txt, opts)-tuples) om naar platte tekst."""
    out = []
    for ln in lines:
        if isinstance(ln, str):
            out.append(ln)
        else:
            if isinstance(ln, tuple):
                ln = [ln]
            out.append("".join(t for t, _o in ln))
    return "\n".join(out)

def notes(s, txt):
    # Docentnotities enkel in de docentversie; leerlingversie krijgt geen docentnotities.
    if is_alumno():
        return
    extra = SOL_NOTES.get(id(s))
    if extra:
        # Antwoorden staan nu (ook in de docentversie) verborgen tot klik → daarom
        # de VOLLEDIGE oplossing hier in de spreker-notities (presenter view).
        txt = txt + "\n\n— SOLUCIÓN (docent · presenter view) —\n" + "\n\n".join(extra)
    s.notes_slide.notes_text_frame.text = txt

# ------------------------------------------------------------- vaste chrome
def bg(s, color=PAPER):
    rect(s, 0, 0, EMU_W, EMU_H, fill=color)

def sectionbar(s, label, title_es, title_nl, accent=G, num=None):
    """Kopbalk met sectielabel-vaantje + Spaanse titel + NL-steun. Idee 6: vaste kop."""
    rect(s, 0, 0, EMU_W, Inches(1.18), fill=accent)
    rect(s, 0, Inches(1.18), EMU_W, Inches(0.06), fill=GD)
    # sectielabel-vaantje
    chip(s, Inches(0.55), Inches(0.2), label, fill=WHITE, tcolor=accent, size=11)
    if num is not None:
        # groot achtergrondcijfer rechts
        text(s, Inches(11.4), Inches(-0.15), Inches(1.9), Inches(1.5),
             [[(str(num), {"size": 88, "bold": True, "color": RGBColor(0xFF,0xFF,0xFF), "font": DISPLAY})]],
             align=PP_ALIGN.RIGHT)
        # halftransparant effect simuleren via lichtere tint niet mogelijk simpel; laat wit
    text(s, Inches(0.5), Inches(0.5), Inches(10.6), Inches(0.55),
         [[(title_es, {"size": 27, "bold": True, "color": WHITE, "font": DISPLAY})]],
         anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.55), Inches(1.02), Inches(10.6), Inches(0.3),
         [[(title_nl, {"size": 12.5, "italic": True, "color": GT, "font": BODY})]])

def footer(s, tab="U9 · PLANES", page=None):
    rect(s, 0, Inches(7.16), EMU_W, Inches(0.34), fill=CREMA)
    text(s, Inches(0.45), Inches(7.18), Inches(6), Inches(0.3),
         [[("● ", {"color": G, "size": 11, "bold": True}),
           (tab + "   ·   C4 · La Ruta", {"color": MUT, "size": 9.5})]],
         anchor=MSO_ANCHOR.MIDDLE)
    vlabel = "Leerlingenversie — klik onthult" if is_alumno() else "Docentenversie — met oplossingen"
    text(s, Inches(9.5), Inches(7.18), Inches(3.35), Inches(0.3),
         [[(vlabel, {"color": MUT, "size": 9, "italic": True})]],
         align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
    if page is not None:
        text(s, Inches(12.55), Inches(7.18), Inches(0.5), Inches(0.3),
             [[(str(page), {"color": GD, "size": 9.5, "bold": True})]],
             align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)

def noodroute(s, y=Inches(6.62)):
    """Idee 6 + §5-noodroute: vaste knoppen toon oplossing / sla over / terug naar menu.
    Geeft de «Mostrar solución»-knop terug (visuele noodroute; elke klik in de gewone
    diavoorstelling onthult toch de volgende reveal). «⌂ Menú» krijgt een echte
    hyperlink naar de menudia."""
    labels = [("▶  Mostrar solución", G, WHITE),
              ("⏭  Saltar", WHITE, GD),
              ("⌂  Menú (dia 2)", WHITE, GD)]
    x = Inches(0.5)
    btn_sol = None; btn_menu = None
    for txt, fill, tc in labels:
        w = Inches(0.2 + 0.11 * len(txt))
        shp = rect(s, x, y, w, Inches(0.4), fill=fill, line=LINE, lw=1.0, round=True, radius=0.5)
        tf = shp.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf.margin_top = tf.margin_bottom = Pt(1)
        p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        r = p.add_run(); r.text = txt; r.font.size = Pt(10.5); r.font.bold = True
        r.font.name = BODY; r.font.color.rgb = tc
        if txt.startswith("▶"):
            btn_sol = shp
        if txt.startswith("⌂"):
            btn_menu = shp
        x = x + w + Inches(0.16)
    if btn_menu is not None:
        link_to(btn_menu, 1)  # dia 2 = LESSON_MENU (index 1)
    hint = ("Klik ▶ om de solución te tonen · ⌂ terug naar het menu"
            if is_alumno() else "Noodroute (§5): werkt zonder audio/internet")
    text(s, Inches(9.1), y, Inches(3.7), Inches(0.4),
         [[(hint, {"size": 8.5, "italic": True, "color": MUT})]],
         align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
    return btn_sol

def solucion(s, x, y, w, h, lines, title="SOLUCIÓN · docent"):
    """Zichtbaar oplossingskader (alleen docentversie). Rood-getint met label."""
    box = rect(s, x, y, w, h, fill=GT, line=G, lw=1.5, round=True, radius=0.06)
    chipshp, _ = chip(s, x + Inches(0.15), y - Inches(0.14), title, fill=G, tcolor=WHITE, size=9.5)
    tf = box.text_frame; tf.word_wrap = True
    tf.margin_left = tf.margin_right = Pt(10); tf.margin_top = Pt(11); tf.margin_bottom = Pt(6)
    first = True
    for ln in lines:
        p = tf.paragraphs[0] if first else tf.add_paragraph(); first = False
        _p_spacing(p, after=3, line=1.02)
        if isinstance(ln, str):
            ln = [(ln, {})]
        for txt, o in ln:
            r = p.add_run(); r.text = txt
            r.font.size = Pt(o.get("size", 12)); r.font.bold = o.get("bold", False)
            r.font.italic = o.get("italic", False); r.font.name = BODY
            r.font.color.rgb = o.get("color", GD)
    return box, chipshp

# ------------------------------------------------------- oefen-interactiviteit
def exercise_solucion(s, x, y, w, h, lines, trigger=None, title_doc="SOLUCIÓN · docent"):
    """Solución-kader op een oefendia — in BEIDE decks verborgen tot klik.
      · Het kader én het label verschijnen sequentieel bij klik (fade-in).
      · docentversie → géén oplossing blijft zichtbaar staan die de onthulling
        verklapt; de VOLLEDIGE oplossing gaat naar de spreker-notities (zie notes()).
    De <trigger>-parameter wordt niet meer gebruikt (geen triggers meer) maar blijft
    voor call-compatibiliteit."""
    title = "SOLUCIÓN" if is_alumno() else title_doc
    box, chipshp = solucion(s, x, y, w, h, lines, title=title)
    register_reveal(s, box)
    register_reveal(s, chipshp)
    if not is_alumno():
        SOL_NOTES.setdefault(id(s), []).append(_flatten_solucion_lines(lines))
    return box

def check_badge(s, x, y, trigger_shape=None, label="✓ correcto", w=None):
    """Klein groen «✓ correcto»-vlak dat verborgen start en bij de volgende klik
    verschijnt (entrance-fade) — het antwoord «springt in». Werkt in béíde versies.
    <trigger_shape> wordt niet meer gebruikt (geen triggers) maar blijft voor
    call-compatibiliteit."""
    if w is None:
        w = Inches(0.2 + 0.088 * len(label))
    h = Inches(0.34)
    b = rect(s, x, y, w, h, fill=F_OBJ, line=GD, lw=1.0, round=True, radius=0.5, shadow=True)
    tf = b.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE; tf.word_wrap = False
    tf.margin_left = tf.margin_right = Pt(7); tf.margin_top = tf.margin_bottom = Pt(1)
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = label; r.font.size = Pt(11); r.font.bold = True
    r.font.name = BODY; r.font.color.rgb = WHITE
    register_reveal(s, b)
    return b

def card(s, x, y, w, h, fill=WHITE, line=LINE, lw=1.2, shadow=True, radius=0.055):
    return rect(s, x, y, w, h, fill=fill, line=line, lw=lw, shadow=shadow, round=True, radius=radius)

def legend_func(s, x, y):
    """Mini-legenda functionele taalkleuren (grijswaarden-veilig: ook labels)."""
    items = [("persoon", F_SUBJ), ("werkw.", F_VERB), ("tijd", F_TIME), ("plaats", F_PLAC), ("valstrik", F_NEG)]
    cx = x
    text(s, x, y - Inches(0.02), Inches(1.3), Inches(0.3),
         [[("Kleurcode:", {"size": 9, "bold": True, "color": MUT})]])
    cx = x + Inches(1.15)
    for lab, col in items:
        dot = rect(s, cx, y + Inches(0.02), Inches(0.14), Inches(0.14), fill=col, round=True, radius=0.5)
        text(s, cx + Inches(0.18), y - Inches(0.03), Inches(1.0), Inches(0.3),
             [[(lab, {"size": 9, "color": INK})]])
        cx = cx + Inches(0.18) + Inches(0.1 + 0.062 * len(lab))

PAGE = 0
def pg():
    global PAGE; PAGE += 1; return PAGE

# ============================================================================
# C4 · UNIDAD 9 «Planes y obligaciones» — slides (survival). Herbruikt de machinerie.
# ============================================================================
FTAB = "U9 · PLANES"

def s01_title():
    s = slide(); bg(s)
    rect(s, 0, 0, EMU_W, Inches(4.7), fill=G)
    rect(s, 0, Inches(4.62), EMU_W, Inches(0.08), fill=GD)
    chip(s, Inches(0.6), Inches(0.5), "C4 · LA RUTA · EL DESPEGUE · PARADA 9", fill=WHITE, tcolor=G, size=12)
    text(s, Inches(0.55), Inches(1.15), Inches(12.3), Inches(1.1),
         [[("Planes y obligaciones", {"size": 46, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(0.6), Inches(2.25), Inches(11.8), Inches(0.7),
         [[("Voy a preparar café. ", {"size": 26, "bold": True, "color": WHITE, "font": DISPLAY}),
           ("— Eh… tengo cosas que hacer.", {"size": 17, "italic": True, "color": GT})]])
    text(s, Inches(0.6), Inches(3.2), Inches(11.5), Inches(1.1),
         [[("Zeggen wat je ", {"size": 16, "color": WHITE}), ("gaat doen", {"size": 16, "bold": True, "color": WHITE}),
           (" en wat je ", {"size": 16, "color": WHITE}), ("moet doen", {"size": 16, "bold": True, "color": WHITE}),
           (" — en beleefd «nee» zeggen (voy a · tengo que · no puedo).", {"size": 16, "color": WHITE})],
          [("Survival in Spanish — Julio stelt de hele week plannen voor… en María heeft élke keer «cosas que hacer».", {"size": 13, "italic": True, "color": GT})]])
    # mochila-gids
    avatar(s, "mochila", Inches(10.7), Inches(4.95), d=Inches(1.7))
    text(s, Inches(0.6), Inches(5.25), Inches(9), Inches(1.5),
         [[("En esta unidad vas a…", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})],
          [("• Hablar de planes  ", {"size": 13, "color": INK}), ("ir a + infinitivo: voy a estudiar · vamos a dormir · ¿qué vas a hacer?", {"size": 11, "italic": True, "color": MUT})],
          [("• Expresar obligación  ", {"size": 13, "color": INK}), ("tener que + infinitivo: tengo que trabajar · ¿tienes que hacer algo?", {"size": 11, "italic": True, "color": MUT})],
          [("• Usar tener + sustantivo  ", {"size": 13, "color": INK}), ("tengo hambre · tengo sueño · tengo sed · tengo prisa", {"size": 11, "italic": True, "color": MUT})],
          [("• Rechazar con educación  ", {"size": 13, "color": INK}), ("no puedo, tengo que… · ¡qué pena! · otro día, ¿vale?", {"size": 11, "italic": True, "color": MUT})]])
    footer(s, tab=FTAB, page=pg())

def _tile(s, x, y, w, num, es, nl, target):
    c = card(s, x, y, w, Inches(1.15), fill=WHITE, line=LINE)
    text(s, x + Inches(0.2), y + Inches(0.12), Inches(0.7), Inches(0.6),
         [[(num, {"size": 24, "bold": True, "color": G, "font": DISPLAY})]])
    text(s, x + Inches(0.2), y + Inches(0.62), w - Inches(0.35), Inches(0.5),
         [[(es, {"size": 14, "bold": True, "color": INK, "font": DISPLAY})],
          [(nl, {"size": 10.5, "italic": True, "color": MUT})]])
    if target is not None:
        link_to(c, target)

def s02_menu():
    s = slide(); bg(s)
    sectionbar(s, "MENÚ", "¿Qué vamos a hacer?", "Wat gaan we doen? — klik op een tegel", num=None)
    tiles = [("1", "¡Escucha!", "la escena + chunks", 2),
             ("2", "Suena bien", "los diptongos ie & ue", 3),
             ("3", "La máquina de frases", "voy a / tengo que + infinitivo", 4),
             ("4", "Kit", "planes · obligaciones", 5),
             ("5", "Gramática", "ir a · tener que", 7),
             ("6", "Práctica", "oefenen samen", 9),
             ("7", "Hablar", "invita y rechaza", 10),
             ("8", "Cultura", "el finde en el mundo hispano", 11),
             ("9", "Tarea", "Mi finde", 12),
             ("10", "Repaso", "wat kun je nu?", 14)]
    x0, y0 = Inches(0.55), Inches(1.7)
    w = Inches(3.0); gx = Inches(0.18); gy = Inches(0.2)
    for i, t in enumerate(tiles):
        col = i % 4; row = i // 4
        _tile(s, x0 + col * (w + gx), y0 + row * (Inches(1.15) + gy), w, *t)
    text(s, Inches(0.6), Inches(5.95), Inches(12), Inches(0.9),
         [[("Consejo · Tip. ", {"size": 12, "bold": True, "color": GD, "font": DISPLAY}),
           ("Ná «voy a» en «tengo que» komt áltijd het hele werkwoord: voy a estudiar · tengo que trabajar. En «ik ben slaperig» = tengo sueño!", {"size": 12, "italic": True, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

# ── Online-video inbedden zodat hij ÍN PowerPoint afspeelt ────────────────────
# Bron U9 = GOOGLE DRIVE (net als U8 bestaat er voor deze aflevering géén
# YouTube-link): file-id 1YlBRdAs4L4fOvmXylmQLlRSJMoRto7Kb, deelrechten
# reader/anyone → de /preview-embed is openbaar bereikbaar.
# Dus een ONLINE-video: PowerPoint desktop (2016+/365) probeert hem in-app af te
# spelen via de ingebedde speler (internet vereist). De helper aanvaardt een
# VOLLEDIGE URL i.p.v. enkel een YouTube-id; álle OOXML-markup blijft identiek
# (poster-picture + a:hlinkClick action="ppaction://media" + a:videoFile r:link
# + p14:media r:embed). Poster = PIL-render.
from PIL import Image as _Img, ImageDraw as _Dw, ImageFont as _Ft
_VIDEO_REL="http://schemas.openxmlformats.org/officeDocument/2006/relationships/video"
_MEDIA_REL="http://schemas.microsoft.com/office/2007/relationships/media"
_P14="http://schemas.microsoft.com/office/powerpoint/2010/main"
DRIVE_ID="1YlBRdAs4L4fOvmXylmQLlRSJMoRto7Kb"
VIDEO_URL="https://drive.google.com/file/d/%s/preview"%DRIVE_ID   # embed-URL (in-app speler)
VIDEO_WATCH="https://drive.google.com/file/d/%s/view"%DRIVE_ID    # browser-URL (noodroute)
VIDEO_TOP="Sitcom · Episodio 9"; VIDEO_MAIN="Planes y obligaciones"
VIDEO_POSTER=os.path.join(HERE,"assets","video_poster_U9.png")
def _load_font(sz,bold=True):
    for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
        try: return _Ft.truetype(p,sz)
        except Exception: pass
    return _Ft.load_default()
def make_video_poster(png,top,main):
    os.makedirs(os.path.dirname(png),exist_ok=True)
    W,H=1280,720; im=_Img.new("RGB",(W,H)); dr=_Dw.Draw(im)
    c0=(0xD6,0x45,0x50); c1=(0xA8,0x32,0x3B)
    for yy in range(H):
        t=yy/H; dr.line([(0,yy),(W,yy)],fill=tuple(int(c0[i]+(c1[i]-c0[i])*t) for i in range(3)))
    dr.ellipse([560,320,720,480],fill=(255,255,255))
    dr.polygon([(618,362),(618,438),(688,400)],fill=c1)
    dr.text((70,96),top,font=_load_font(38),fill=(255,255,255))
    dr.text((70,156),main,font=_load_font(60),fill=(255,255,255))
    dr.text((70,626),"▶ Klik om af te spelen · Spanish Sitcom (Google Drive)",font=_load_font(28,False),fill=(255,255,255))
    im.save(png)
make_video_poster(VIDEO_POSTER,VIDEO_TOP,VIDEO_MAIN)
def add_online_video(s,url,x,y,w,h,poster_png):
    """<url> = de VOLLEDIGE embed-URL (U1–U7: youtube.com/embed/<id> · U8–U9: de
    Drive-/preview-URL). De markup eronder is ongewijzigd t.o.v. U1–U8."""
    pic=s.shapes.add_picture(poster_png,x,y,w,h)
    part=s.part
    rIdv=part.relate_to(url,_VIDEO_REL,is_external=True)
    rIdm=part.relate_to(url,_MEDIA_REL,is_external=True)
    el=pic._element; nvPicPr=el.find(qn('p:nvPicPr'))
    cNvPr=nvPicPr.find(qn('p:cNvPr'))
    cNvPr.insert(0,parse_xml('<a:hlinkClick xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" r:id="" action="ppaction://media"/>'))
    nvPr=nvPicPr.find(qn('p:nvPr'))
    nvPr.append(parse_xml('<a:videoFile xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" r:link="%s"/>'%rIdv))
    nvPr.append(parse_xml('<p:extLst xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><p:ext uri="{DAA4B4D4-6D71-4841-9C94-3DE7FCFB9230}"><p14:media xmlns:p14="%s" r:embed="%s"/></p:ext></p:extLst>'%(_P14,rIdm)))
    return pic

def s03_escucha():
    s = slide(); bg(s)
    sectionbar(s, "§1 · ¡ESCUCHA!", "Bekijk la escena y escucha", "Kijk & luister — Julio stelt de hele week plannen voor; María heeft élke keer iets te doen", num=1)
    card(s, Inches(0.55), Inches(1.55), Inches(7.4), Inches(4.9), fill=WHITE, line=LINE)
    dia = [("Julio", "Buenos días. Voy a preparar café. ¿Quieres desayunar?", F_VERB),
           ("María", "Ah… no tengo mucha hambre.", F_SUBJ),
           ("Julio", "Pero es sábado. Tengo sueño. ¿No tienes sueño?", F_SUBJ),
           ("Julio", "Vamos a dormir un poquito más.", F_VERB),
           ("María", "Tengo cosas que hacer.", F_NEG),
           ("Julio", "Y esta noche, ¿quedamos para ir al cine?", F_TIME),
           ("María", "Eh… no puedo. Tengo que pasear al perro de mi madre.", F_NEG),
           ("Julio", "¿Y esta tarde? ¿Vamos a pasear, a comprar cosas?", F_TIME),
           ("María", "Mmm…, tengo que lavarme el pelo.", F_NEG),
           ("Julio", "¿Y mañana? ¿Tienes que hacer algo?", F_TIME),
           ("María", "El domingo voy a quedar con unas amigas.", F_VERB),
           ("Julio", "¿El lunes, el martes, el miércoles?", F_TIME),
           ("María", "Tengo que trabajar.", F_NEG),
           ("Julio", "¿Por las noches?", F_TIME),
           ("María", "Por las noches tengo que dormir.", F_NEG),
           ("Julio", "El jueves voy a dar unas clases de baile flamenco.", F_VERB),
           ("Julio", "El próximo fin de semana. ¿Tienes que ir a la India en globo?", F_TIME),
           ("María", "No, estoy aquí, pero tengo cosas que hacer. Cosas. Adiós.", F_NEG)]
    y = Inches(1.72)
    for sp, tx, col in dia:
        chip(s, Inches(0.72), y, sp, fill=col, tcolor=WHITE, size=9.5)
        text(s, Inches(1.5), y - Inches(0.02), Inches(6.35), Inches(0.42),
             [[(tx, {"size": 9.5, "color": INK})]])
        y = y + Inches(0.259)
    # chunks-kaart rechts (ingekort om plaats te maken voor de video)
    card(s, Inches(8.2), Inches(1.55), Inches(4.6), Inches(2.45), fill=GT, line=G)
    text(s, Inches(8.45), Inches(1.72), Inches(4.1), Inches(2.2),
         [[("Chunks para llevar 🎒", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})],
          [("Voy a preparar café · vamos a dormir", {"size": 11.5, "color": INK})],
          [("Tengo que trabajar · ¿tienes que…?", {"size": 11.5, "color": INK})],
          [("Tengo sueño · no tengo mucha hambre", {"size": 11.5, "color": INK})],
          [("No puedo · tengo cosas que hacer", {"size": 11.5, "color": INK})],
          [("esta noche · esta tarde · el próximo finde", {"size": 11.5, "color": INK})]])
    # echte, afspeelbare video (online-embed met de Drive-/preview-URL) + hyperlink-noodroute
    text(s, Inches(8.2), Inches(4.12), Inches(2.95), Inches(0.3),
         [[("🎬 Episodio 9 — klik om af te spelen", {"size": 11, "bold": True, "color": GD, "font": DISPLAY})]])
    btn, _bw = chip(s, Inches(11.2), Inches(4.09), "▶ Abrir en Drive", fill=G, tcolor=WHITE, size=9.5)
    try:
        btn.click_action.hyperlink.address = VIDEO_WATCH
    except Exception:
        pass
    add_online_video(s, VIDEO_URL, Inches(8.2), Inches(4.45), Inches(4.6), Inches(2.55), VIDEO_POSTER)
    notes(s, "De video van aflevering 9 komt uit GOOGLE DRIVE (er is voor deze aflevering géén YouTube-link): file-id 1YlBRdAs4L4fOvmXylmQLlRSJMoRto7Kb, deelrechten reader/anyone → INTERNET VEREIST. Klik op de poster om in PowerPoint af te spelen; lukt dat niet, klik dan de knop «▶ Abrir en Drive» (of open de Drive-link zelf in een browser: " + VIDEO_WATCH + ") — dan speelt de video in het browsertabblad. Aanpak: eerst één keer kijken zónder transcript (globaal begrijpen: Julio blijft de hele week voorstellen doen, María heeft élke keer een excuus), daarna met het transcript. Laat de leerlingen twee kolommen maken: PLANES (voy a…) ↔ OBLIGACIONES (tengo que…). Focus op de contrasterende chunks: «voy a preparar café» / «vamos a dormir» / «voy a quedar con unas amigas» tegenover «tengo que pasear al perro» / «tengo que lavarme el pelo» / «tengo que trabajar» / «tengo cosas que hacer». Let ook op «tengo sueño» (= slaperig zijn) en het beleefde «no puedo». Doelcodes: C4-LU-1 · C4-STR-1 · C4-WS-1.")
    footer(s, tab=FTAB, page=pg())

def s04_kit():
    s = slide(); bg(s)
    sectionbar(s, "§2 · KIT", "Los planes · las obligaciones · el finde", "Plannen maken, zeggen wat je moet doen & wat je in het weekend doet", num=2)
    cols = [("Los planes · voy a… 🗓️", [("Voy a + infinitivo", "ik ga + werkwoord"), ("Voy a preparar café", "ik ga koffie zetten"),
              ("Vamos a dormir", "we gaan / laten we slapen"), ("¿Vamos a pasear?", "gaan we wandelen?"),
              ("¿Qué vas a hacer?", "wat ga je doen?"), ("El domingo voy a quedar", "zondag ga ik afspreken")]),
            ("Las obligaciones · tengo que… ✅", [("Tengo que + infinitivo", "ik moet + werkwoord"), ("Tengo que trabajar", "ik moet werken"),
              ("Tengo que estudiar", "ik moet studeren"), ("¿Tienes que hacer algo?", "moet je iets doen?"),
              ("Tengo cosas que hacer", "ik heb dingen te doen"), ("Tengo que dormir", "ik moet slapen")]),
            ("Actividades del finde 🎉", [("ir al cine", "naar de cinema gaan"), ("pasear al perro", "de hond uitlaten"),
              ("quedar con amigos/as", "afspreken met vrienden"), ("ver una película", "een film kijken"),
              ("jugar al fútbol", "voetballen"), ("tomar algo", "iets gaan drinken")])]
    x = Inches(0.55); w = Inches(4.0)
    for title, items in cols:
        card(s, x, Inches(1.6), w, Inches(4.9), fill=WHITE, line=LINE)
        text(s, x + Inches(0.25), Inches(1.78), w - Inches(0.4), Inches(0.5),
             [[(title, {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
        y = Inches(2.45)
        for es, nl in items:
            text(s, x + Inches(0.25), y, w - Inches(0.5), Inches(0.6),
                 [[(es, {"size": 12.5, "bold": True, "color": INK}), ("   " + nl, {"size": 10, "italic": True, "color": MUT})]])
            y = y + Inches(0.65)
        x = x + w + Inches(0.2)
    footer(s, tab=FTAB, page=pg())

def s05_kit2():
    s = slide(); bg(s)
    sectionbar(s, "§2 · KIT", "Con tener · aceptar o rechazar", "«Tener» waar wij «zijn/hebben» zeggen & ja of nee zeggen op een uitnodiging", num=2)
    left = [("Tengo hambre", "ik heb honger"), ("Tengo sueño", "ik ben slaperig"), ("Tengo sed", "ik heb dorst"),
            ("Tengo prisa", "ik heb haast"), ("Tengo cosas que hacer", "ik heb dingen te doen")]
    right = [("¡Vale! · ¡Perfecto!", "oké! · perfect!"), ("Estoy libre", "ik ben vrij"), ("No puedo", "ik kan niet"),
             ("¡Qué pena!", "wat jammer!"), ("Otro día, ¿vale?", "een andere dag, oké?")]
    card(s, Inches(0.55), Inches(1.6), Inches(6.0), Inches(4.9), fill=GT, line=G)
    text(s, Inches(0.8), Inches(1.78), Inches(5.5), Inches(0.5),
         [[("Con tener · «geen ser/estar»! 🙋", {"size": 13.5, "bold": True, "color": GD, "font": DISPLAY})]])
    y = Inches(2.5)
    for es, nl in left:
        text(s, Inches(0.8), y, Inches(5.4), Inches(0.6), [[(es, {"size": 15, "bold": True, "color": INK}), ("   " + nl, {"size": 11, "italic": True, "color": MUT})]])
        y = y + Inches(0.72)
    card(s, Inches(6.8), Inches(1.6), Inches(6.0), Inches(4.9), fill=WHITE, line=LINE)
    text(s, Inches(7.05), Inches(1.78), Inches(5.5), Inches(0.5),
         [[("Aceptar o rechazar 🤷", {"size": 13.5, "bold": True, "color": GD, "font": DISPLAY})]])
    y = Inches(2.5)
    for es, nl in right:
        text(s, Inches(7.05), y, Inches(5.4), Inches(0.6), [[(es, {"size": 15, "bold": True, "color": INK}), ("   " + nl, {"size": 11, "italic": True, "color": MUT})]])
        y = y + Inches(0.72)
    text(s, Inches(0.8), Inches(5.7), Inches(11.9), Inches(0.7),
         [[("¡Ojo! ", {"size": 12, "bold": True, "color": RED}),
           ("Tengo sueño = «ik ben slaperig» (letterlijk «ik héb slaap») · rechazar = nee + reden: «No puedo. Tengo que…» + ¡Qué pena!", {"size": 12, "italic": True, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

def s06_gram_ira():
    s = slide(); bg(s)
    sectionbar(s, "§4 · GRAMÁTICA", "ir a + infinitivo — hablar de planes", "Zeggen wat je gaat doen: voy a / vas a / vamos a + het hele werkwoord", num=4)
    legend_func(s, Inches(0.55), Inches(1.42))
    # ir a-kaart (links, breed)
    card(s, Inches(0.55), Inches(1.9), Inches(7.6), Inches(4.1), fill=WHITE, line=LINE)
    text(s, Inches(0.8), Inches(2.05), Inches(7.1), Inches(0.4), [[("voy a  ·  vas a  ·  vamos a  +  infinitivo", {"size": 15, "bold": True, "color": GD, "font": DISPLAY})]])
    filas = [("voy a", "ik ga", "Voy a preparar café."),
             ("vas a", "jij gaat", "¿Qué vas a hacer?"),
             ("vamos a", "we gaan / laten we", "Vamos a dormir un poquito más.")]
    y = Inches(2.6)
    for chunk, nl, ex in filas:
        rect(s, Inches(0.8), y, Inches(1.75), Inches(0.42), fill=RGBColor(0xFE,0xF1,0xE7), line=None, round=True, radius=0.2)
        text(s, Inches(0.8), y + Inches(0.02), Inches(1.75), Inches(0.38),
             [[(chunk, {"size": 14, "bold": True, "color": F_VERB, "font": DISPLAY})]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text(s, Inches(2.68), y + Inches(0.02), Inches(1.5), Inches(0.38),
             [[(nl, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, Inches(4.22), y + Inches(0.02), Inches(3.8), Inches(0.38),
             [[(ex, {"size": 12, "italic": True, "color": MUT})]], anchor=MSO_ANCHOR.MIDDLE)
        y = y + Inches(0.52)
    # de «a» mag nooit weg
    rect(s, Inches(0.8), Inches(4.3), Inches(7.1), Inches(0.62), fill=GT, line=G, lw=1.4, round=True, radius=0.1)
    text(s, Inches(0.95), Inches(4.38), Inches(6.8), Inches(0.5),
         [[("Siempre con «a»: ", {"size": 12.5, "bold": True, "color": GD}), ("voy ", {"size": 13, "color": INK}),
           ("a", {"size": 15, "bold": True, "color": F_VERB}), (" estudiar  ·  vamos ", {"size": 13, "color": INK}),
           ("a", {"size": 15, "bold": True, "color": F_VERB}), (" pasear  —  ", {"size": 13, "color": INK}),
           ("de «a» mag nooit weg.", {"size": 12, "italic": True, "color": MUT})]])
    text(s, Inches(0.8), Inches(5.05), Inches(7.1), Inches(0.85),
         [[("💡 ", {"size": 12}), ("Net als in het Nederlands: «ik ", {"size": 12, "color": INK}),
           ("ga", {"size": 12, "bold": True, "color": F_VERB}), (" koffie zetten». Dit is dé A1-manier om over de ", {"size": 12, "color": INK}),
           ("toekomst", {"size": 12, "bold": True, "color": F_TIME}), (" te praten.", {"size": 12, "color": INK})],
          [("Y para preguntar: ", {"size": 12, "color": INK}), ("¿Qué vas a hacer esta tarde? · ¿Vamos a tomar algo?", {"size": 12, "bold": True, "color": F_VERB})]])
    # Fíjate-kaart rechts
    card(s, Inches(8.4), Inches(1.9), Inches(4.4), Inches(4.1), fill=GT, line=G)
    chip(s, Inches(8.6), Inches(1.76), "🔎 FÍJATE · EN LA ESCENA", fill=G, tcolor=WHITE, size=9.5)
    text(s, Inches(8.65), Inches(2.3), Inches(3.9), Inches(2.4),
         [[("Je hoorde het al:", {"size": 12, "bold": True, "color": GD, "font": DISPLAY})],
          [("«", {"size": 13, "color": INK}), ("Voy a", {"size": 13, "bold": True, "color": F_VERB}), (" preparar café.»", {"size": 13, "color": INK})],
          [("«", {"size": 13, "color": INK}), ("Vamos a", {"size": 13, "bold": True, "color": F_VERB}), (" dormir un poquito más.»", {"size": 13, "color": INK})],
          [("«El domingo ", {"size": 13, "color": INK}), ("voy a", {"size": 13, "bold": True, "color": F_VERB}), (" quedar con unas amigas.»", {"size": 13, "color": INK})],
          [("«El jueves ", {"size": 13, "color": INK}), ("voy a", {"size": 13, "bold": True, "color": F_VERB}), (" dar unas clases de baile.»", {"size": 13, "color": INK})]])
    text(s, Inches(8.65), Inches(4.75), Inches(3.9), Inches(1.2),
         [[("¿Y tú? · En jij?", {"size": 12, "bold": True, "color": GD, "font": DISPLAY})],
          [("¿Qué vas a hacer el finde?", {"size": 13, "bold": True, "color": INK})],
          [("Antwoord met «Voy a…» + het hele werkwoord.", {"size": 11, "italic": True, "color": MUT})]])
    notes(s, "Functioneel: «ir a + infinitivo» is de A1-manier om over de toekomst te praten — géén futuro simple (dat blijft buiten C4 én C6). Presenteer «voy a / vas a / vamos a» als VASTE CHUNKS, niet als vervoegingsparadigma van «ir»: het werkwoordsysteem (en dus het volledige paradigma voy/vas/va/vamos/vais/van) hoort in het 5de jaar (C5). Kernpunt: de «a» mag nooit weg (voy A estudiar) en ná «voy a» komt áltijd het hele werkwoord. Sterke steun voor Nederlandstaligen: het parallel loopt met «ik ga + infinitief». Kleurcode: werkwoord = oranje (§13). Doelcodes: C4-WS-1 · C4-TS-3 · C4-SP-1 · C4-GE-3.")
    footer(s, tab=FTAB, page=pg())

def s07_gram_tener():
    s = slide(); bg(s)
    sectionbar(s, "§4 · GRAMÁTICA", "tener que + infinitivo ↔ tener + sustantivo", "«Moeten» met que + het hele werkwoord — maar géén «que» vóór een naamwoord", num=4)
    # tener que-kaart
    card(s, Inches(0.55), Inches(1.42), Inches(6.05), Inches(1.62), fill=WHITE, line=LINE)
    text(s, Inches(0.8), Inches(1.54), Inches(5.6), Inches(0.35), [[("tener que + infinitivo · moeten", {"size": 13.5, "bold": True, "color": GD, "font": DISPLAY})]])
    filas = [("tengo que", "ik moet", "Tengo que trabajar."),
             ("tienes que", "jij moet", "¿Tienes que hacer algo?")]
    y = Inches(1.98)
    for chunk, nl, ex in filas:
        text(s, Inches(0.8), y, Inches(5.6), Inches(0.4),
             [[(chunk + "  ", {"size": 14, "bold": True, "color": F_VERB, "font": DISPLAY}),
               (nl + "   ", {"size": 11.5, "color": INK}), (ex, {"size": 11, "italic": True, "color": MUT})]])
        y = y + Inches(0.42)
    text(s, Inches(0.8), Inches(2.78), Inches(5.6), Inches(0.3),
         [[("Letterlijk: «ik ", {"size": 11, "italic": True, "color": MUT}), ("héb te", {"size": 11, "bold": True, "color": GD}), (" werken» → tengo que trabajar.", {"size": 11, "italic": True, "color": MUT})]])
    # tener + sustantivo-kaart
    card(s, Inches(6.75), Inches(1.42), Inches(6.05), Inches(1.62), fill=CREMA, line=LINE)
    text(s, Inches(7.0), Inches(1.54), Inches(5.6), Inches(0.35), [[("tener + sustantivo · zonder «que»", {"size": 13.5, "bold": True, "color": GD, "font": DISPLAY})]])
    mv1 = rect(s, Inches(7.0), Inches(1.96), Inches(2.85), Inches(0.92), fill=RGBColor(0xFE,0xF1,0xE7), line=None, round=True, radius=0.1)
    text(s, Inches(7.12), Inches(2.02), Inches(2.65), Inches(0.85),
         [[("✅ así lo dice el español", {"size": 9.5, "bold": True, "color": RGBColor(0xB4,0x53,0x0E)})],
          [("Tengo hambre · sed", {"size": 12, "bold": True, "color": INK})],
          [("Tengo sueño · prisa", {"size": 12, "bold": True, "color": INK})]])
    mv2 = rect(s, Inches(9.95), Inches(1.96), Inches(2.85), Inches(0.92), fill=RGBColor(0xE8,0xF0,0xFE), line=None, round=True, radius=0.1)
    text(s, Inches(10.07), Inches(2.02), Inches(2.65), Inches(0.85),
         [[("🇳🇱 wat wij zeggen", {"size": 9.5, "bold": True, "color": RGBColor(0x1E,0x40,0xAF)})],
          [("ik heb honger · dorst", {"size": 12, "color": INK})],
          [("ik ben slaperig · heb haast", {"size": 12, "color": INK})]])
    # ── VALSTRIK 1 · tengo sueño
    card(s, Inches(0.55), Inches(3.16), Inches(6.05), Inches(1.28), fill=RGBColor(0xFD,0xE8,0xE8), line=RED, lw=2.4)
    chip(s, Inches(0.75), Inches(3.02), "¡OJO! · LA TRAMPA 1", fill=RED, tcolor=WHITE, size=9.5)
    text(s, Inches(0.8), Inches(3.42), Inches(5.6), Inches(1.0),
         [[("«ik ben slaperig» = ", {"size": 13, "color": INK}), ("tengo sueño", {"size": 17, "bold": True, "color": F_VERB, "font": DISPLAY})],
          [("nooit ", {"size": 12, "color": INK}), ("estoy sueño", {"size": 12.5, "bold": True, "color": RED}),
           (" of ", {"size": 12, "color": INK}), ("soy sueño", {"size": 12.5, "bold": True, "color": RED}),
           (" — letterlijk: «ik héb slaap».", {"size": 12, "color": INK})]])
    # ── VALSTRIK 2 · la «que» obligatoria
    card(s, Inches(6.75), Inches(3.16), Inches(6.05), Inches(1.28), fill=RGBColor(0xFD,0xE8,0xE8), line=RED, lw=2.4)
    chip(s, Inches(6.95), Inches(3.02), "¡OJO! · LA TRAMPA 2", fill=RED, tcolor=WHITE, size=9.5)
    text(s, Inches(7.0), Inches(3.42), Inches(5.6), Inches(1.0),
         [[("vóór een werkwoord → ", {"size": 12, "color": INK}), ("tengo ", {"size": 13, "bold": True, "color": INK}),
           ("que", {"size": 15, "bold": True, "color": RED}), (" trabajar", {"size": 13, "bold": True, "color": INK}),
           ("  (niet ", {"size": 11.5, "color": INK}), ("tengo trabajar", {"size": 11.5, "bold": True, "color": RED}), (")", {"size": 11.5, "color": INK})],
          [("vóór een naamwoord → ", {"size": 12, "color": INK}), ("tengo hambre", {"size": 13, "bold": True, "color": INK}),
           ("  (géén «que»!)", {"size": 11.5, "italic": True, "color": MUT})]])
    # rechazar con educación
    card(s, Inches(0.55), Inches(4.56), Inches(12.25), Inches(0.78), fill=GT, line=G)
    text(s, Inches(0.8), Inches(4.64), Inches(11.8), Inches(0.65),
         [[("Rechazar con educación · ", {"size": 12.5, "bold": True, "color": GD, "font": DISPLAY}),
           ("«— ¿Quedamos para ir al cine? — ", {"size": 12, "color": INK}),
           ("No puedo", {"size": 12.5, "bold": True, "color": F_NEG}), (". ", {"size": 12, "color": INK}),
           ("Tengo que", {"size": 12.5, "bold": True, "color": F_VERB}), (" pasear al perro. ", {"size": 12, "color": INK}),
           ("¡Qué pena!", {"size": 12.5, "bold": True, "color": GD}), ("»", {"size": 12, "color": INK})],
          [("Dos pasos: ", {"size": 11.5, "color": INK}), ("no puedo", {"size": 11.5, "bold": True, "color": F_NEG}),
           (" + ", {"size": 11.5, "color": INK}), ("la razón (tengo que…)", {"size": 11.5, "bold": True, "color": F_VERB}),
           (" · verzachters: ¡Qué pena! · Otro día, ¿vale?", {"size": 11.5, "italic": True, "color": MUT})]])
    # mini-quiz met reveal
    text(s, Inches(0.6), Inches(5.45), Inches(12.2), Inches(0.4),
         [[("Completa · vul aan (klik voor de oplossing): ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("Yo ___ estudiar (plan).   Tengo ___ trabajar.   Tengo ___ (honger).", {"size": 13, "color": INK})]])
    exercise_solucion(s, Inches(0.8), Inches(5.88), Inches(11.7), Inches(0.5),
        [[("voy a · que · hambre", {"bold": True, "color": GD, "size": 13})]])
    noodroute(s)
    notes(s, "Twee contrasten op één dia. (1) «tener que + infinitivo» = moeten: tengo que / tienes que + het HELE werkwoord. De «que» is verplicht: tengo QUE trabajar, nooit «tengo trabajar». (2) «tener + sustantivo» = precies zónder que: tengo hambre / sed / sueño / prisa. DE KERNVALSTRIK voor Nederlandstaligen: «ik ben slaperig» = tengo sueño (letterlijk «ik héb slaap») — nooit «estoy sueño» of «soy sueño»; hetzelfde patroon geldt voor honger, dorst en haast. Rechazar = twee stappen: «no puedo» + de reden («tengo que…»), eventueel verzacht met «¡qué pena!» of «otro día, ¿vale?». C4-scope: «tengo que / tienes que» zijn VASTE CHUNKS — géén vervoegingsparadigma van «tener» (tengo/tienes/tiene/tenemos/tenéis/tienen); dat systeem komt in het 5de jaar (C5). Oplossing: voy a · que · hambre.")
    footer(s, tab=FTAB, page=pg())

def s08_practica():
    s = slide(); bg(s)
    sectionbar(s, "§3 · PRÁCTICA", "Completa el diálogo", "Vul samen aan — klik voor de oplossing", num=3)
    card(s, Inches(0.55), Inches(1.7), Inches(7.6), Inches(4.5), fill=WHITE, line=LINE)
    lines = ["— ¿Qué haces esta tarde?",
             "— ___ a estudiar.",
             "— ¿Y esta noche?",
             "— ___ ___ pasear al perro.",
             "— ¿Y el domingo? ¿___ a tomar algo?",
             "— El domingo no ___. ¡Qué pena!"]
    y = Inches(1.95)
    for q in lines:
        text(s, Inches(0.8), y, Inches(7.1), Inches(0.6), [[(q, {"size": 16, "color": INK})]])
        y = y + Inches(0.7)
    exercise_solucion(s, Inches(8.4), Inches(1.9), Inches(4.4), Inches(4.0),
        [[("1. Voy", {"color": GD, "size": 14})], [("2. Tengo", {"color": GD, "size": 14})],
         [("3. que", {"color": GD, "size": 14})], [("4. vamos", {"color": GD, "size": 14})],
         [("5. puedo", {"color": GD, "size": 14})]],
        title_doc="SOLUCIÓN · docent")
    noodroute(s)
    notes(s, "Laat leerlingen eerst zelf proberen (in duo, hardop). Klik daarna de oplossing open. Let op: «Voy a estudiar» — de «a» staat er al, dus enkel «Voy» invullen; «Tengo que pasear» — hier zijn twee gaten (Tengo + que) omdat de «que» vóór een werkwoord verplicht is; «¿Vamos a tomar algo?» = een uitnodiging (wij); «no puedo» = de beleefde afwijzing, versterkt door «¡qué pena!». Oplossing: Voy · Tengo · que · vamos · puedo.")
    footer(s, tab=FTAB, page=pg())

def s09_speaking():
    s = slide(); bg(s)
    sectionbar(s, "§3 · HABLAR", "Invita y rechaza", "Nodig uit, wijs beleefd af en zoek samen een moment dat past — sin leer", num=3)
    card(s, Inches(0.55), Inches(1.7), Inches(7.6), Inches(3.4), fill=GT, line=G)
    text(s, Inches(0.85), Inches(1.95), Inches(7.1), Inches(3.0),
         [[("Modelo · zeg dit hardop:", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})],
          [("«— ¿Vamos al cine el sábado?", {"size": 16, "color": INK})],
          [("— No puedo. Tengo que cuidar a mi hermano. ¡Qué pena!", {"size": 16, "color": INK})],
          [("— ¿Y el domingo por la tarde?", {"size": 16, "color": INK})],
          [("— Vale, el domingo estoy libre.»", {"size": 16, "color": INK})]])
    card(s, Inches(8.4), Inches(1.7), Inches(4.4), Inches(3.4), fill=WHITE, line=LINE)
    text(s, Inches(8.65), Inches(1.95), Inches(3.9), Inches(3.0),
         [[("¿Cómo? · Werkvorm", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})],
          [("1. Invita: «¿Vamos a…?» · «¿Quedamos para…?».", {"size": 12.5, "color": INK})],
          [("2. Rechaza: «No puedo. Tengo que…».", {"size": 12.5, "color": INK})],
          [("3. Suaviza: «¡Qué pena! Otro día, ¿vale?».", {"size": 12.5, "color": INK})],
          [("4. Propón otro momento: «¿Y el domingo?».", {"size": 12.5, "color": INK})],
          [("5. Acepta: «Vale, estoy libre».", {"size": 12.5, "color": INK})]])
    text(s, Inches(0.6), Inches(5.4), Inches(12), Inches(0.7),
         [[("Interactie ", {"size": 12, "bold": True, "color": GD, "font": DISPLAY}),
           ("= uitnodigen, afwijzen mét een echte reden, en tóch een moment vinden. Wijs 2× af en zeg 1× ja. Verstaan? Zeg: «¿Cómo? / ¿Puedes repetir?»", {"size": 12, "italic": True, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

def s10_musica():
    s = slide(); bg(s)
    sectionbar(s, "CULTURA", "El finde en el mundo hispano", "Het weekend begint er later — en muziek die jullie kennen", num=None)
    bandas = [("Quevedo", "Bzrp #52", "🇪🇸 España"), ("Karol G", "Provenza", "🇨🇴 Colombia"),
              ("Aitana", "Las Babys", "🇪🇸 España"), ("Manu Chao", "Me Gustas Tú", "🇪🇸/🇫🇷"),
              ("Álvaro Soler", "El Mismo Sol", "🇪🇸 España"), ("Camilo", "Vida de Rico", "🇨🇴 Colombia")]
    x0, y0 = Inches(0.55), Inches(1.75); w = Inches(4.0)
    for i, (ar, sg, ge) in enumerate(bandas):
        col = i % 3; row = i // 3
        x = x0 + col * (w + Inches(0.18)); y = y0 + row * (Inches(1.5) + Inches(0.18))
        card(s, x, y, w, Inches(1.5), fill=WHITE, line=LINE)
        text(s, x + Inches(0.25), y + Inches(0.2), w - Inches(0.4), Inches(1.2),
             [[(ar, {"size": 15, "bold": True, "color": INK, "font": DISPLAY})],
              [("🎵 " + sg, {"size": 12, "color": MUT})], [(ge, {"size": 11, "color": GD})]])
    card(s, Inches(0.55), Inches(5.5), Inches(12.25), Inches(1.05), fill=GT, line=G)
    text(s, Inches(0.85), Inches(5.62), Inches(11.7), Inches(0.9),
         [[("🎉 El «finde» en el mundo hispano ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("In España spreekt men om uit te gaan vaak pas om ", {"size": 12, "color": INK}),
           ("las diez o las once (22–23 u)", {"size": 12, "bold": True, "color": F_TIME}),
           (" af. Valt een feestdag op donderdag, dan «maakt men een brug» — ", {"size": 12, "color": INK}),
           ("hacer puente", {"size": 12, "bold": True, "color": GD}), (": ook de vrijdag vrij.", {"size": 12, "color": INK})],
          [("Jongeren zeggen ", {"size": 12, "color": INK}), ("el finde", {"size": 12, "bold": True, "color": GD}),
           (" (spreektaal voor ", {"size": 12, "color": INK}), ("el fin de semana", {"size": 12, "italic": True, "color": INK}),
           ("), en ", {"size": 12, "color": INK}), ("el domingo", {"size": 12, "bold": True, "color": F_TIME}),
           (" is bij veel families de dag van de familiemaaltijd. Playlist + LyricsTraining op de hub → tabblad Música.", {"size": 12, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

def s11_tarea():
    s = slide(); bg(s)
    sectionbar(s, "§5 · TAREA FINAL", "Mi finde", "Vul je weekend-agenda in: 3 planes + 2 obligaciones — en maak samen een afspraak", num=5)
    # FICHA · weekend-agenda met invulvakken
    card(s, Inches(0.55), Inches(1.7), Inches(6.6), Inches(3.6), fill=WHITE, line=G, lw=1.6)
    rect(s, Inches(0.55), Inches(1.7), Inches(6.6), Inches(0.5), fill=G)
    text(s, Inches(0.75), Inches(1.76), Inches(6.2), Inches(0.4), [[("MI FINDE · Academia «Welcome to Spanish»", {"size": 12, "bold": True, "color": WHITE, "font": DISPLAY})]])
    heads = [("¿Cuándo?", Inches(2.0)), ("Voy a… (plan)", Inches(2.2)), ("Tengo que… (obligación)", Inches(2.2))]
    hx = Inches(0.68)
    for h, hw in heads:
        rect(s, hx, Inches(2.32), hw, Inches(0.32), fill=GT, line=LINE, lw=1.0, round=True, radius=0.16)
        text(s, hx, Inches(2.34), hw, Inches(0.28),
             [[(h, {"size": 9.5, "bold": True, "color": GD, "font": DISPLAY})]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        hx = hx + hw + Inches(0.06)
    momentos = ["El sábado por la mañana", "El sábado por la tarde", "El sábado por la noche", "El domingo"]
    ry = Inches(2.7)
    for mo in momentos:
        rect(s, Inches(0.68), ry, Inches(2.0), Inches(0.48), fill=CREMA, line=LINE, lw=1.0, round=True, radius=0.08)
        text(s, Inches(0.76), ry + Inches(0.03), Inches(1.9), Inches(0.42),
             [[(mo, {"size": 9.5, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        rect(s, Inches(2.74), ry, Inches(2.2), Inches(0.48), fill=PAPER, line=LINE, lw=1.0, round=True, radius=0.08)
        rect(s, Inches(5.0), ry, Inches(2.2), Inches(0.48), fill=PAPER, line=LINE, lw=1.0, round=True, radius=0.08)
        ry = ry + Inches(0.52)
    text(s, Inches(0.75), Inches(4.85), Inches(6.2), Inches(0.45),
         [[("🤝 Nuestro plan: Quedamos el ", {"size": 11.5, "bold": True, "color": INK}), ("______ ", {"size": 11.5, "color": LINE}),
           ("a las ", {"size": 11.5, "bold": True, "color": INK}), ("______ ", {"size": 11.5, "color": LINE}),
           ("en ", {"size": 11.5, "bold": True, "color": INK}), ("__________ .", {"size": 11.5, "color": LINE})]])
    # pasos
    card(s, Inches(7.4), Inches(1.7), Inches(5.4), Inches(3.6), fill=GT, line=G)
    text(s, Inches(7.65), Inches(1.88), Inches(4.9), Inches(3.3),
         [[("Los pasos · stappen", {"size": 14, "bold": True, "color": GD, "font": DISPLAY})],
          [("1. Rellena tu finde: 3 planes met «voy a + infinitivo» + 2 obligaciones met «tengo que + infinitivo».", {"size": 12, "color": INK})],
          [("2. Invita a un compañero: «¿Vamos a…?» · «¿Quedamos para… el…?».", {"size": 12, "color": INK})],
          [("3. Rechaza una vez con educación: «No puedo. Tengo que… ¡Qué pena!».", {"size": 12, "color": INK})],
          [("4. Cerrad un plan: zoek tóch één moment dat past en spreek af (dag + uur).", {"size": 12, "color": INK})],
          [("5. Presenta: vertel je finde + jullie afspraak aan de klas — sin leer.", {"size": 12, "color": INK})]])
    text(s, Inches(0.6), Inches(5.45), Inches(7.6), Inches(1.0),
         [[("🏁 Klaar als… ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("je 3 plannen zegt met «voy a + infinitivo», 2 verplichtingen met «tengo que + infinitivo», één uitnodiging beleefd afwijst («no puedo, tengo que…») en samen één afspraak vastlegt — zónder af te lezen.", {"size": 12, "color": INK})]])
    card(s, Inches(8.4), Inches(5.42), Inches(4.4), Inches(1.05), fill=WHITE, line=LINE)
    text(s, Inches(8.6), Inches(5.5), Inches(4.0), Inches(0.9),
         [[("Evaluatie · 🟢🟡🔴", {"size": 11.5, "bold": True, "color": GD, "font": DISPLAY})],
          [("· ir a + infinitivo correct (planes)", {"size": 10.5, "color": INK})],
          [("· tener que + infinitivo correct", {"size": 10.5, "color": INK})],
          [("· rechazar met excuus & durf", {"size": 10.5, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

def s12_repaso():
    s = slide(); bg(s)
    sectionbar(s, "REPASO", "Lo esencial de un vistazo", "Wat je nu kunt — semáforo", num=None)
    card(s, Inches(0.55), Inches(1.7), Inches(7.6), Inches(3.3), fill=WHITE, line=LINE)
    text(s, Inches(0.85), Inches(1.85), Inches(7.1), Inches(3.1),
         [[("Zo maak je een plan", {"size": 14, "bold": True, "color": GD, "font": DISPLAY})],
          [("Voy a estudiar · Vamos a dormir · ¿Qué vas a hacer?", {"size": 13.5, "color": INK})],
          [("altijd «a» + het hele werkwoord — dé A1-manier voor de toekomst", {"size": 12, "italic": True, "color": MUT})],
          [("", {"size": 6})],
          [("Zo zeg je wat je moet doen", {"size": 14, "bold": True, "color": GD, "font": DISPLAY})],
          [("Tengo que trabajar · ¿Tienes que hacer algo? · Tengo cosas que hacer", {"size": 13, "color": INK})],
          [("Tengo hambre · sueño · sed · prisa (zónder «que»)", {"size": 13, "color": INK})],
          [("", {"size": 6})],
          [("Zo wijs je beleefd af", {"size": 14, "bold": True, "color": GD, "font": DISPLAY})],
          [("No puedo. Tengo que… · ¡Qué pena! · Otro día, ¿vale? · Vale, estoy libre.", {"size": 13, "color": INK})]])
    # de valstrikken keren terug (§13: spreiding & recycling)
    card(s, Inches(0.55), Inches(5.15), Inches(7.6), Inches(1.0), fill=RGBColor(0xFD,0xE8,0xE8), line=RED, lw=2.0)
    text(s, Inches(0.85), Inches(5.23), Inches(7.1), Inches(0.9),
         [[("¡Ojo! · las dos trampas ", {"size": 12.5, "bold": True, "color": RED, "font": DISPLAY}),
           ("«ik ben slaperig» = ", {"size": 12, "color": INK}), ("tengo sueño", {"size": 12.5, "bold": True, "color": F_VERB}),
           (" (nooit «estoy sueño»).", {"size": 12, "color": INK})],
          [("En de «que»: tengo ", {"size": 12, "color": INK}), ("que", {"size": 12.5, "bold": True, "color": RED}),
           (" trabajar (werkwoord) ↔ tengo hambre (naamwoord, géén «que»).", {"size": 12, "color": INK})]])
    card(s, Inches(8.4), Inches(1.7), Inches(4.4), Inches(4.45), fill=GT, line=G)
    text(s, Inches(8.65), Inches(1.9), Inches(3.9), Inches(0.5), [[("Puedo… · Ik kan…", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    items = ["plannen zeggen (voy a · vamos a + inf.)", "vragen «¿qué vas a hacer?»",
             "verplichtingen zeggen (tengo que + inf.)", "tener + naamwoord (hambre · sueño)",
             "een uitnodiging aannemen (¡vale!)", "beleefd afwijzen (no puedo, tengo que…)"]
    y = Inches(2.5)
    for it in items:
        text(s, Inches(8.65), y, Inches(3.9), Inches(0.7), [[("🟢🟡🔴  ", {"size": 12}), (it, {"size": 11, "color": INK})]])
        y = y + Inches(0.55)
    text(s, Inches(8.65), Inches(5.65), Inches(3.9), Inches(0.7), [[("🎮 Repasa jugando", {"size": 12, "bold": True, "color": GD, "font": DISPLAY})], [("online op de hub · la máquina de frases · invita y rechaza", {"size": 11, "italic": True, "color": MUT})]])
    footer(s, tab=FTAB, page=pg())

def s13_teacher():
    s = slide(); bg(s, color=RGBColor(0x24,0x1C,0x1B))
    text(s, Inches(0.6), Inches(0.5), Inches(12), Inches(0.7), [[("Docentendossier · Unidad 9 «Planes y obligaciones»", {"size": 22, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(0.6), Inches(1.3), Inches(12.1), Inches(5.6),
         [[("Timing (2 lesuren van 50 min).", {"size": 14, "bold": True, "color": RGBColor(0xFB,0xEA,0xEC), "font": DISPLAY})],
          [("Les 1: Escucha (sitcom ep. 9 — op een zaterdagmorgen stelt Julio de hele week plannen voor: café, samen slapen, cine, pasear… en María heeft élke keer «cosas que hacer»: tengo que pasear al perro, tengo que lavarme el pelo, tengo que trabajar) + Suena bien (los diptongos ie & ue + la tilde en el diptongo) + La máquina de frases + Kit (planes · obligaciones · actividades del finde · con tener · aceptar o rechazar). Les 2: gramática functioneel (ir a + infinitivo · tener que + infinitivo ↔ tener + sustantivo · rechazar con educación), práctica, hablar «Invita y rechaza», tarea «Mi finde» + cultura.", {"size": 12, "color": RGBColor(0xEC,0xEA,0xE3)})],
          [("", {"size": 5})],
          [("VIDEO = GOOGLE DRIVE (geen YouTube voor deze aflevering).", {"size": 14, "bold": True, "color": RGBColor(0xFB,0xEA,0xEC), "font": DISPLAY})],
          [("File-id 1YlBRdAs4L4fOvmXylmQLlRSJMoRto7Kb (deelrechten reader/anyone). INTERNET VEREIST. In de escucha-dia klik je op de poster om in PowerPoint af te spelen; lukt dat niet, gebruik de knop «▶ Abrir en Drive» of open " + VIDEO_WATCH + " zelf in een browser. Test de verbinding vóór de les.", {"size": 12, "color": RGBColor(0xEC,0xEA,0xE3)})],
          [("", {"size": 5})],
          [("Aanpak C4 (survival).", {"size": 14, "bold": True, "color": RGBColor(0xFB,0xEA,0xEC), "font": DISPLAY})],
          [("Chunks komen auditief binnen (luisteren → naspreken). «voy a / vas a / vamos a» en «tengo que / tienes que» presenteren als VASTE CHUNKS uit de scène — géén vervoegingsparadigma van «ir» of «tener»; het volledige werkwoordsysteem komt in het 5de jaar (C5). «ir a + infinitivo» is bovendien de A1-manier om over de toekomst te praten: géén futuro simple introduceren (dat blijft ook in het 6de buiten scope). TWEE KERNVALSTRIKKEN: (1) «ik ben slaperig» = tengo sueño (letterlijk «ik héb slaap») — nooit «estoy sueño»/«soy sueño»; idem tengo hambre/sed/prisa; (2) de «que» is verplicht vóór een werkwoord (tengo QUE trabajar, niet «tengo trabajar») maar valt weg vóór een naamwoord (tengo hambre). Verder: de «a» in «voy a estudiar» mag nooit weg; ná voy a / tengo que komt áltijd het hele werkwoord. Rechazar = twee stappen (no puedo + de reden), verzacht met «¡qué pena!» of «otro día, ¿vale?». Uitspraak: los diptongos ie & ue = twee klinkers in ÉÉN lettergreep (qu-ie-ro in 2 stukken, pue-do niet «pu-e-do»); in que/qui is de u stil (recycling U7), dus daar géén diptongo; la tilde valt op de tweede klinker (adiós · después · también · canción). Doelcodes: C4-WS-1 · C4-TS-3 · C4-SP-1 · C4-LU-1 · C4-GE-3 · C4-STR-1 · C4-MEC-1/2 · C4-CU-1.", {"size": 12, "color": RGBColor(0xEC,0xEA,0xE3)})],
          [("", {"size": 5})],
          [("Evaluatie.", {"size": 14, "bold": True, "color": RGBColor(0xFB,0xEA,0xEC), "font": DISPLAY})],
          [("Mondelinge mini-taak «Mi finde»: weekend-agenda met 3 planes (voy a…) + 2 obligaciones (tengo que…) presenteren, een klasgenoot uitnodigen, één keer beleefd afwijzen en samen één afspraak vastleggen. Geen leerplan → focus op «kunnen gebruiken in de praktijk». Rubric: ir a + infinitivo correct (planes) · tener que + infinitivo correct · rechazar met excuus & durf.", {"size": 12, "color": RGBColor(0xEC,0xEA,0xE3)})],
          [("", {"size": 5})],
          [("Oplossingen staan bij elke oefendia in de presenter-notities; antwoorden verschijnen bij klik.", {"size": 11, "italic": True, "color": RGBColor(0xA6,0xA2,0x9A)})]])
    footer(s, tab=FTAB, page=pg())

def s_uitspraak():
    s = slide(); bg(s)
    sectionbar(s, "SUENA BIEN", "Los diptongos ie & ue · la tilde en el diptongo", "Twee klinkers samen = één lettergreep — en waar het accent dan komt", num=None)
    # diptongo ie-kaart
    card(s,Inches(0.55),Inches(1.6),Inches(6.05),Inches(2.15),fill=WHITE,line=LINE)
    rect(s,Inches(0.55),Inches(1.6),Inches(6.05),Inches(0.14),fill=G)
    text(s,Inches(0.8),Inches(1.85),Inches(5.6),Inches(0.4),[[("① El diptongo ie · una sola sílaba",{"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
    text(s,Inches(0.8),Inches(2.35),Inches(5.6),Inches(1.3),
         [[("qu",{"size":14.5,"color":INK}),("ie",{"size":14.5,"bold":True,"color":G}),("·ro · t",{"size":14.5,"color":INK}),("ie",{"size":14.5,"bold":True,"color":G}),("·nes · b",{"size":14.5,"color":INK}),("ie",{"size":14.5,"bold":True,"color":G}),("n · s",{"size":14.5,"color":INK}),("ie",{"size":14.5,"bold":True,"color":G}),("·te · f",{"size":14.5,"color":INK}),("ie",{"size":14.5,"bold":True,"color":G}),("s·ta · v",{"size":14.5,"color":INK}),("ie",{"size":14.5,"bold":True,"color":G}),("r·nes",{"size":14.5,"color":INK})],
          [("«quiero» = 2 stukken (qu",{"size":11,"italic":True,"color":MUT}),("ie",{"size":11,"bold":True,"color":G}),("-ro), niet 3 (qui-e-ro).",{"size":11,"italic":True,"color":MUT})]])
    # diptongo ue-kaart
    card(s,Inches(6.75),Inches(1.6),Inches(6.05),Inches(2.15),fill=WHITE,line=LINE)
    rect(s,Inches(6.75),Inches(1.6),Inches(6.05),Inches(0.14),fill=G)
    text(s,Inches(7.0),Inches(1.85),Inches(5.6),Inches(0.4),[[("② El diptongo ue · una sola sílaba",{"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
    text(s,Inches(7.0),Inches(2.35),Inches(5.6),Inches(1.3),
         [[("p",{"size":14.5,"color":INK}),("ue",{"size":14.5,"bold":True,"color":G}),("·do · b",{"size":14.5,"color":INK}),("ue",{"size":14.5,"bold":True,"color":G}),("·no · l",{"size":14.5,"color":INK}),("ue",{"size":14.5,"bold":True,"color":G}),("·go · f",{"size":14.5,"color":INK}),("ue",{"size":14.5,"bold":True,"color":G}),("·ra · j",{"size":14.5,"color":INK}),("ue",{"size":14.5,"bold":True,"color":G}),("·go · c",{"size":14.5,"color":INK}),("ue",{"size":14.5,"bold":True,"color":G}),("n·ta",{"size":14.5,"color":INK})],
          [("Glijd vloeiend van de u naar de e — in één beweging.",{"size":11,"italic":True,"color":MUT})]])
    card(s,Inches(0.55),Inches(3.9),Inches(12.25),Inches(0.85),fill=GT,line=G)
    text(s,Inches(0.85),Inches(4.05),Inches(11.7),Inches(0.6),
         [[("¡Ojo! ",{"size":13,"bold":True,"color":RED,"font":DISPLAY}),("Splits ze niet: «pu-e-do» klinkt fout — zeg «",{"size":13,"color":INK}),("pue",{"size":13,"bold":True,"color":GD}),("-do» in één beweging. En in ",{"size":13,"color":INK}),("que / qui",{"size":13,"bold":True,"color":GD}),(" is de u ",{"size":13,"color":INK}),("stil",{"size":13,"bold":True,"color":RED}),(" (zoals in U7): daar is het géén diptongo.",{"size":13,"color":INK})]])
    text(s,Inches(0.6),Inches(5.0),Inches(12),Inches(0.4),[[("③ La tilde en el diptongo · het accent komt op de tweede klinker",{"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
    text(s,Inches(0.6),Inches(5.55),Inches(12.2),Inches(0.7),
         [[("a·di",{}),("ÓS",{"color":G,"bold":True}),("      des·p",{}),("UÉS",{"color":G,"bold":True}),("      tam·b",{}),("IÉN",{"color":G,"bold":True}),("      can·c",{}),("IÓN",{"color":G,"bold":True})]],size=20,font=DISPLAY)
    text(s,Inches(0.6),Inches(6.28),Inches(12.2),Inches(0.5),
         [[("Valt de klemtoon op een diptongo aan het eind van het woord, dan staat de tilde op de TWEEDE klinker: adiós · después · también · canción.",{"size":11,"color":INK})],
          [("🔊 Oefen de klanken online op de hub (tabblad Kit · Suena bien).",{"size":11,"italic":True,"color":MUT})]])
    footer(s, tab=FTAB, page=pg())

# ── NIEUW in U9: «La máquina de frases» — zinbouwer in 3 blokken (2 rijen) ──
def _maq_row(s, y, chunk, chunk_nl, opts, result, result_nl):
    """Eén rij van de zinbouwer: [chunk] + [+ infinitivo] + [opties]  →  resultaat.
    Blok 1 = oranje-tint (werkwoord-semantiek), blok 2 = de rode huistint, blok 3 = wit.
    Het resultaat verschijnt bij klik (on-click reveal)."""
    h = Inches(1.0)
    b1 = rect(s, Inches(0.6), y, Inches(3.1), h, fill=RGBColor(0xFE,0xF1,0xE7), line=LINE, lw=1.5, round=True, radius=0.09)
    text(s, Inches(0.75), y + Inches(0.16), Inches(2.8), Inches(0.7),
         [[(chunk, {"size": 20, "bold": True, "color": RGBColor(0xB4,0x53,0x0E), "font": DISPLAY})],
          [(chunk_nl, {"size": 10, "color": MUT})]], align=PP_ALIGN.CENTER)
    b2 = rect(s, Inches(3.7), y, Inches(3.1), h, fill=GT, line=LINE, lw=1.5)
    text(s, Inches(3.85), y + Inches(0.16), Inches(2.8), Inches(0.7),
         [[("+ infinitivo", {"size": 20, "bold": True, "color": GD, "font": DISPLAY})],
          [("het hele werkwoord", {"size": 10, "color": MUT})]], align=PP_ALIGN.CENTER)
    b3 = rect(s, Inches(6.8), y, Inches(3.1), h, fill=WHITE, line=LINE, lw=1.5, round=True, radius=0.09)
    text(s, Inches(6.9), y + Inches(0.16), Inches(2.9), Inches(0.7),
         [[(opts, {"size": 15, "bold": True, "color": INK, "font": DISPLAY})],
          [("kies een werkwoord", {"size": 10, "color": MUT})]], align=PP_ALIGN.CENTER)
    text(s, Inches(9.95), y + Inches(0.28), Inches(0.45), Inches(0.45),
         [[("→", {"size": 22, "bold": True, "color": G, "font": DISPLAY})]], align=PP_ALIGN.CENTER)
    # resultaat = on-click reveal
    res = rect(s, Inches(10.4), y, Inches(2.4), h, fill=G, line=GD, lw=1.4, round=True, radius=0.09, shadow=True)
    tf = res.text_frame; tf.word_wrap = True
    tf.margin_left = tf.margin_right = Pt(7); tf.margin_top = Pt(6); tf.margin_bottom = Pt(4)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    _p_spacing(p, after=2, line=1.02)
    r = p.add_run(); r.text = result
    r.font.size = Pt(16); r.font.bold = True; r.font.name = DISPLAY; r.font.color.rgb = WHITE
    p2 = tf.add_paragraph(); p2.alignment = PP_ALIGN.CENTER
    _p_spacing(p2, after=0, line=1.02)
    r2 = p2.add_run(); r2.text = result_nl
    r2.font.size = Pt(10); r2.font.italic = True; r2.font.name = BODY; r2.font.color.rgb = GT
    register_reveal(s, res)
    return res

def s_maquina():
    s = slide(); bg(s)
    sectionbar(s, "§4 · LA MÁQUINA DE FRASES", "Voy a / Tengo que + infinitivo", "Twee bouwstenen, altijd in dezelfde volgorde — klik en de zin verschijnt", num=4)
    legend_func(s, Inches(0.55), Inches(1.42))
    _maq_row(s, Inches(1.85), "Voy a", "un plan · ik ga", "estudiar · ir al cine",
             "Voy a estudiar.", "Ik ga studeren.")
    _maq_row(s, Inches(3.0), "Tengo que", "obligación · ik moet", "trabajar · dormir",
             "Tengo que trabajar.", "Ik moet werken.")
    # regel-strip
    card(s, Inches(0.55), Inches(4.2), Inches(12.25), Inches(0.8), fill=GT, line=G)
    text(s, Inches(0.85), Inches(4.3), Inches(11.7), Inches(0.65),
         [[("Cómo funciona · ", {"size": 12.5, "bold": True, "color": GD, "font": DISPLAY}),
           ("blok 1 (", {"size": 12.5, "color": INK}), ("voy a", {"size": 13, "bold": True, "color": F_VERB}),
           (" of ", {"size": 12.5, "color": INK}), ("tengo que", {"size": 13, "bold": True, "color": F_VERB}),
           (") + blok 2 = altijd het ", {"size": 12.5, "color": INK}), ("hele werkwoord", {"size": 13, "bold": True, "color": GD}),
           (" (el infinitivo: -ar · -er · -ir). Nooit een vervoegde vorm!", {"size": 12.5, "color": INK})],
          [("Ook zo: ", {"size": 11.5, "color": INK}), ("vamos a pasear · ¿qué vas a hacer? · ¿tienes que trabajar?", {"size": 12, "bold": True, "color": F_VERB}),
           ("   —   en de ", {"size": 11.5, "color": INK}), ("a", {"size": 12.5, "bold": True, "color": RED}),
           (" en de ", {"size": 11.5, "color": INK}), ("que", {"size": 12.5, "bold": True, "color": RED}),
           (" mogen nooit weg.", {"size": 11.5, "color": INK})]])
    # mini-oefening met reveal
    text(s, Inches(0.6), Inches(5.2), Inches(12.2), Inches(0.4),
         [[("Construye · bouw zelf (klik voor de oplossing): ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("plan + ir al cine  ·  obligación + estudiar  ·  nosotros + plan + tomar algo", {"size": 13, "color": INK})]])
    exercise_solucion(s, Inches(0.8), Inches(5.68), Inches(11.7), Inches(0.55),
        [[("Voy a ir al cine. · Tengo que estudiar. · Vamos a tomar algo.", {"bold": True, "color": GD, "size": 13})]])
    noodroute(s)
    notes(s, "Werkvorm: bouw hardop in koor. Wijs blok 1 aan (voy a / tengo que), dan blok 3 (het infinitivo) en de klas zegt de volledige zin; klik daarna de zin open ter controle. Daarna variëren: laat leerlingen zelf een infinitivo roepen. Kernidee van de máquina: de eerste blok is een VASTE CHUNK (voy a · vamos a · tengo que · tienes que) en blok 2 dwingt het HELE werkwoord af — zo hoeven leerlingen niets te vervoegen (het paradigma van «ir» en «tener» komt in C5). Kleurcode: werkwoord = oranje (§13); de rode middenblok = de huisstijlkleur van C4. Oplossing: Voy a ir al cine. · Tengo que estudiar. · Vamos a tomar algo. Doelcodes: C4-WS-1 · C4-TS-3 · C4-SP-1 · C4-MEC-2.")
    footer(s, tab=FTAB, page=pg())

# ── Funciones-comunicativas-dia (matrix C) — leest de gedeelde funciones_data ──
import sys as _sys
_sys.path.insert(0, os.path.join(os.path.dirname(HERE), "web"))
import funciones_data as FD
FUNC_UNIT = 9

def _cap_exps(t, n):
    """Kort de exponentes-regel in op een «·»-grens zodat ze binnen twee regels blijft."""
    if len(t) <= n:
        return t
    cut = t.rfind(" · ", 0, n)
    return (t[:cut] if cut > 0 else t[:n]) + " …"

def s_funciones():
    s = slide(); bg(s)
    sectionbar(s, "FUNCIONES", "Mis funciones comunicativas", "Lo que ya sé hacer — crece cada unidad", num=None)
    fs = FD.funciones_hasta(FUNC_UNIT); have=len(fs); total=len(FD.FUNCIONES)
    text(s, Inches(0.6), Inches(1.42), Inches(12.2), Inches(0.35),
         [[("Mi repertorio: %d / %d funciones — " % (have,total), {"size":13,"bold":True,"color":GD,"font":DISPLAY}),
           ("no solo palabras: lo que puedo HACER con el español.", {"size":12,"color":MUT})]])
    cols_x=[Inches(0.55), Inches(6.85)]; w=Inches(5.9)
    # adaptieve rijhoogte: bij 20 funciones (U9, incl. de nieuwe F19/F20) mag geen
    # rij van de dia vallen → pitch schaalt met het aantal rijen (blijft ≤ 1.32);
    # bij veel funciones zakken ook de binnenmarge én de fontgrootte van de
    # exponentes-regel mee (en wordt die regel op een «·»-grens ingekort).
    nrows = (len(fs) + 1) // 2
    top = 1.82; bottom = 7.0
    pitch = min(1.32, (bottom - top) / nrows)
    ch = pitch - (0.16 if pitch > 0.80 else 0.10)
    off = 0.05 if pitch > 0.80 else 0.03
    tsz = 11 if have <= 16 else (10.5 if have <= 18 else 10)
    exsz = 8.5 if have <= 14 else (7.0 if have <= 16 else (6.3 if have <= 18 else 6.0))
    excap = 300 if have <= 16 else (235 if have <= 18 else 205)
    for i,f in enumerate(fs):
        col=i%2; row=i//2
        x=cols_x[col]; y=Inches(top+row*pitch)
        st=FD.status(f,FUNC_UNIT); hot = st in ("nueva","nivel")
        card(s,x,y,w,Inches(ch),fill=(GT if hot else WHITE),line=(G if hot else LINE))
        badge = "  ● NUEVA" if st=="nueva" else ("  ▲ nivel+" if st=="nivel" else "")
        text(s,x+Inches(0.22),y+Inches(off),w-Inches(0.44),Inches(min(0.28, ch*0.5)),
             [[(f["es"], {"size":tsz,"bold":True,"color":INK,"font":DISPLAY}),(badge,{"size":9,"bold":True,"color":GD})]])
        exps=" · ".join(e for u in sorted(k for k in f["exp"] if k<=FUNC_UNIT) for e in f["exp"][u])
        text(s,x+Inches(0.22),y+Inches(off)+Inches(ch*0.42),w-Inches(0.44),Inches(ch*0.54),
             [[(_cap_exps(exps, excap),{"size":exsz,"color":MUT})]])
    footer(s, tab=FTAB, page=pg())

def _run_all_slides(include_teacher=True):
    # dia-indexen (0-based) = de hyperlink-targets van de menutegels in s02_menu:
    # 0 título · 1 menú · 2 escucha · 3 suena bien · 4 la máquina de frases ·
    # 5 kit · 6 kit (con tener / rechazar) · 7 gram ir a · 8 gram tener que ·
    # 9 práctica · 10 hablar · 11 cultura · 12 tarea · 13 funciones · 14 repaso ·
    # (15 docentendossier)
    s01_title(); s02_menu(); s03_escucha(); s_uitspraak(); s_maquina()
    s04_kit(); s05_kit2(); s06_gram_ira()
    s07_gram_tener(); s08_practica(); s09_speaking()
    s10_musica(); s11_tarea(); s_funciones(); s12_repaso()
    if include_teacher:
        s13_teacher()


# Themapalet → C4-rode familie. python-pptx start van het Office-standaardthema
# (accent1 blauw, accent3 groen, blauwe hyperlinks). Elk overgeërfd element
# (stijl-fills/-lijnen, schaduwen via effectRef, hyperlinks, tx2) trok daardoor naar
# Office-blauw/groen. Hier herschrijven we het klerenschema naar rood + warme neutralen,
# zónder de expliciete functionele taalkleuren (§13) te raken.
THEME_MAP = {
    "dk2": "20242E", "lt2": "F3EEE4",       # tekst2 = ink · achtergrond2 = crema
    "accent1": "D64550", "accent2": "A8323B",  # C4-rood + donkerrood
    "accent3": "C25A63", "accent4": "E08A90",  # rood-tinten
    "accent5": "9D2A33", "accent6": "FBEAEC",  # diep rood · rood-vlak
    "hlink": "A8323B", "folHlink": "D64550",   # hyperlinks in C4-rood
}
def patch_theme(pptx_path):
    """Herschrijf alle theme*.xml-klerenschema's naar de C4-rode familie."""
    import re
    with zipfile.ZipFile(pptx_path, "r") as zin:
        items = [(n, zin.read(n)) for n in zin.namelist()]
    changed = 0
    out = []
    for n, data in items:
        if n.startswith("ppt/theme/") and n.endswith(".xml"):
            txt = data.decode("utf-8")
            m = re.search(r"<a:clrScheme\b.*?</a:clrScheme>", txt, re.S)
            if m:
                block = m.group(0)
                for tag, hexv in THEME_MAP.items():
                    block = re.sub(
                        r'(<a:%s>\s*<a:srgbClr val=")[0-9A-Fa-f]{6}' % tag,
                        lambda mo, h=hexv: mo.group(1) + h, block)
                txt = txt[:m.start()] + block + txt[m.end():]
                data = txt.encode("utf-8")
                changed += 1
        out.append((n, data))
    with zipfile.ZipFile(pptx_path, "w", zipfile.ZIP_DEFLATED) as zout:
        for n, data in out:
            zout.writestr(n, data)
    return changed


def build(mode, out, include_teacher=True):
    global MODE
    MODE = mode
    new_presentation()
    _run_all_slides(include_teacher=include_teacher)
    ndia_timing, nreveals = apply_all_timing()
    apply_hyperlinks()
    prs.save(out)
    nthemes = patch_theme(out)
    print(f"themapalet → C4-rood gepatcht in {nthemes} theme-XML('s): {out}")
    ndias = len(prs.slides._sldIdLst)
    print(f"opgeslagen: {out} · {ndias} dia's · {ndia_timing} dia's met on-click animaties · "
          f"{nreveals} on-click onthullingen · {len(MENU_LINKS)} hyperlinks")
    return out, ndias, ndia_timing, nreveals


def to_ppsx(pptx_path, ppsx_path):
    """Converteer .pptx → .ppsx door in [Content_Types].xml de override voor
    /ppt/presentation.xml naar het slideshow-contenttype te zetten."""
    OLD = "application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"
    NEW = "application/vnd.openxmlformats-officedocument.presentationml.slideshow.main+xml"
    if os.path.exists(ppsx_path):
        os.remove(ppsx_path)
    with zipfile.ZipFile(pptx_path, "r") as zin:
        names = zin.namelist()
        with zipfile.ZipFile(ppsx_path, "w", zipfile.ZIP_DEFLATED) as zout:
            for n in names:
                data = zin.read(n)
                if n == "[Content_Types].xml":
                    txt = data.decode("utf-8")
                    assert OLD in txt, "presentation override niet gevonden in [Content_Types].xml"
                    txt = txt.replace(OLD, NEW)
                    data = txt.encode("utf-8")
                zout.writestr(n, data)
    return ppsx_path


def build_alumno():
    # 1) bouw de leerling-.pptx (GEEN kiosk, geen docentnotities, geen teacher-dia)
    build("alumno", OUT_ALUMNO_PPTX, include_teacher=False)
    # 2) verifieer dat de .pptx een geldige OOXML is (round-trip)
    _ = Presentation(OUT_ALUMNO_PPTX)
    print("round-trip OK (alumno-.pptx opent):", OUT_ALUMNO_PPTX)
    # 3) converteer naar .ppsx (slideshow-contenttype)
    to_ppsx(OUT_ALUMNO_PPTX, OUT_ALUMNO)
    # 4) verifieer dat de .ppsx nog een geldige zip/OOXML is
    with zipfile.ZipFile(OUT_ALUMNO) as z:
        bad = z.testzip()
        assert bad is None, f"corrupte .ppsx entry: {bad}"
        ct = z.read("[Content_Types].xml").decode("utf-8")
        assert "slideshow.main+xml" in ct, ".ppsx mist slideshow-contenttype"
    _ = Presentation(OUT_ALUMNO_PPTX)  # pptx blijft leesbaar
    print("opgeslagen (.ppsx, slideshow-contenttype geverifieerd):", OUT_ALUMNO)


if __name__ == "__main__":
    # Docentenversie: vrije navigatie; antwoorden verschijnen bij klik + volledige
    # oplossing in de spreker-notities.
    build("docente", OUT_DOCENTE, include_teacher=True)
    # Leerlingenversie: gewone diavoorstelling (geen kiosk), antwoorden bij klik → .ppsx.
    build_alumno()
