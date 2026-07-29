#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_c4u7_ppt.py — Interactieve PowerPoint C4 · Unidad 7 «Las profesiones»
================================================================================
Gedeelde builder (één bron) → TWEE decks:
  · C4_U7_docente.pptx  — docentversie: vrije navigatie; antwoorden verschijnen bij
    klik (fade) + volledige oplossing & didactiek in de spreker-notities.
  · C4_U7_alumno.ppsx   — leerlingversie: GEEN docentnotities, GEEN kiosk; gewone
    diavoorstelling waarin de antwoorden/oplossingen bij klik verschijnen.

ECHTE interactiviteit: op elke oefendia wordt <p:timing>-XML geïnjecteerd met
standaard SEQUENTIËLE on-click entrance-animaties (fade-in) in de hoofdsequentie
(mainSeq): elke klik onthult de volgende reveal-shape. + hyperlink-navigatie
(menutegels, ⌂ Menú). Cast-avatars = de ECHTE flat-vector SVG's.

Thema U7: Las profesiones · ¿a qué te dedicas? · ser + profesión (zonder un/una:
soy profesor/a · es actriz) · trabajo/trabajas/trabaja als chunks + en · ser ↔ estar
(es profesora ↔ está tranquila · estamos todos bien). Huisstijl: unitkleur rood
#D64550 (C4). Spaans-eerst + NL-steun. Twee kleurlagen: cursusrood (navigatie) +
functionele taalsemantiek (persoon = blauw · werkwoord = oranje · plaats =
turquoise). Bron: 03-build/web/gen_c4u7_kgt.py · gen_c4u7_pdf.py ·
gen_c4u7_practica.py · gen_c4u7_escucha.py
"""
import os, zipfile, shutil
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn, nsdecls
from pptx.oxml import parse_xml

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
OUT_DOCENTE = os.path.join(HERE, "C4_U7_docente.pptx")
OUT_ALUMNO_PPTX = os.path.join(HERE, "C4_U7_alumno.pptx")
OUT_ALUMNO = os.path.join(HERE, "C4_U7_alumno.ppsx")

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
F_VERB = RGBColor(0xEA, 0x73, 0x17)  # werkwoord          (oranje · U7: ser/estar/trabajar)
F_OBJ  = RGBColor(0x1E, 0x9E, 0x74)  # voorwerp           (groen)
F_TIME = RGBColor(0x7C, 0x3A, 0xED)  # tijd               (paars)
F_PLAC = RGBColor(0x0E, 0x9E, 0x97)  # plaats             (turquoise · en una tienda)
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

def footer(s, tab="U7 · LAS PROFESIONES", page=None):
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
# C4 · UNIDAD 7 «Las profesiones» — slides (survival). Herbruikt de machinerie.
# ============================================================================
FTAB = "U7 · LAS PROFESIONES"

def s01_title():
    s = slide(); bg(s)
    rect(s, 0, 0, EMU_W, Inches(4.7), fill=G)
    rect(s, 0, Inches(4.62), EMU_W, Inches(0.08), fill=GD)
    chip(s, Inches(0.6), Inches(0.5), "C4 · LA RUTA · EL DESPEGUE · PARADA 7", fill=WHITE, tcolor=G, size=12)
    text(s, Inches(0.55), Inches(1.15), Inches(12.3), Inches(1.1),
         [[("Las profesiones", {"size": 46, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(0.6), Inches(2.25), Inches(11.8), Inches(0.7),
         [[("¿A qué te dedicas? ", {"size": 26, "bold": True, "color": WHITE, "font": DISPLAY}),
           ("— Soy profesora.", {"size": 17, "italic": True, "color": GT})]])
    text(s, Inches(0.6), Inches(3.2), Inches(11.5), Inches(1.1),
         [[("Naar ", {"size": 16, "color": WHITE}), ("werk vragen", {"size": 16, "bold": True, "color": WHITE}),
           (" en je ", {"size": 16, "color": WHITE}), ("beroep zeggen", {"size": 16, "bold": True, "color": WHITE}),
           (" (ser + profesión · trabajo en… · ser ↔ estar).", {"size": 16, "color": WHITE})],
          [("Survival in Spanish — hablar del trabajo y adivinar como Josefina.", {"size": 13, "italic": True, "color": GT})]])
    # mochila-gids
    avatar(s, "mochila", Inches(10.7), Inches(4.95), d=Inches(1.7))
    text(s, Inches(0.6), Inches(5.25), Inches(9), Inches(1.4),
         [[("En esta unidad vas a…", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})],
          [("• Preguntar por el trabajo  ", {"size": 13, "color": INK}), ("¿a qué te dedicas? · ¿en qué trabajas? · ¿dónde trabajas?", {"size": 11, "italic": True, "color": MUT})],
          [("• Decir tu profesión + trabajo-chunks  ", {"size": 13, "color": INK}), ("soy profesor/a (zonder un/una) · trabajo en una tienda", {"size": 11, "italic": True, "color": MUT})],
          [("• Usar ser ↔ estar  ", {"size": 13, "color": INK}), ("es profesora (wie/wat) · está tranquila (toestand)", {"size": 11, "italic": True, "color": MUT})]])
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
             ("2", "Suena bien", "c/qu = /k/ · esdrújula", 3),
             ("3", "Kit", "profesiones · lugares", 4),
             ("4", "Gramática", "ser + profesión · ser/estar", 6),
             ("5", "Práctica", "oefenen samen", 8),
             ("6", "Hablar", "¿quién soy? · adivina", 9),
             ("7", "Música", "el trabajo en el mundo hispano", 10),
             ("8", "Tarea", "¿Quién soy? · adivina la profesión", 11),
             ("9", "Repaso", "wat kun je nu?", 12)]
    x0, y0 = Inches(0.55), Inches(1.7)
    w = Inches(3.0); gx = Inches(0.18); gy = Inches(0.2)
    for i, t in enumerate(tiles):
        col = i % 4; row = i // 4
        _tile(s, x0 + col * (w + gx), y0 + row * (Inches(1.15) + gy), w, *t)
    text(s, Inches(0.6), Inches(5.95), Inches(12), Inches(0.9),
         [[("Consejo · Tip. ", {"size": 12, "bold": True, "color": GD, "font": DISPLAY}),
           ("Gis zoals waarzegster Josefina: «¿puede ser…?». Durf raden — fouten maken hoort erbij.", {"size": 12, "italic": True, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

# ── Online-video (YouTube) inbedden zodat hij ÍN PowerPoint afspeelt ───────────
# Bron = YouTube (geen lokale mp4), dus een ONLINE-video: PowerPoint desktop (2016+/365)
# speelt hem in-app af via de ingebedde speler (internet vereist). Poster = PIL-render.
from PIL import Image as _Img, ImageDraw as _Dw, ImageFont as _Ft
_VIDEO_REL="http://schemas.openxmlformats.org/officeDocument/2006/relationships/video"
_MEDIA_REL="http://schemas.microsoft.com/office/2007/relationships/media"
_P14="http://schemas.microsoft.com/office/powerpoint/2010/main"
VIDEO_ID="_636fQfHIa4"; VIDEO_TOP="Sitcom · Episodio 7"; VIDEO_MAIN="Las profesiones"
VIDEO_POSTER=os.path.join(HERE,"assets","video_poster_U7.png")
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
    dr.text((70,156),main,font=_load_font(66),fill=(255,255,255))
    dr.text((70,626),"▶ Klik om af te spelen · Spanish Sitcom (YouTube)",font=_load_font(28,False),fill=(255,255,255))
    im.save(png)
make_video_poster(VIDEO_POSTER,VIDEO_TOP,VIDEO_MAIN)
def add_online_video(s,video_id,x,y,w,h,poster_png):
    url="https://www.youtube.com/embed/%s"%video_id
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
    sectionbar(s, "§1 · ¡ESCUCHA!", "Bekijk la escena y escucha", "Kijk & luister — Josefina «leest» de kaarten en gist María's beroep", num=1)
    card(s, Inches(0.55), Inches(1.55), Inches(7.4), Inches(4.9), fill=WHITE, line=LINE)
    dia = [("Fernando", "Yo trabajo aquí, tú trabajas aquí y él trabaja aquí.", F_VERB),
           ("María", "Está todo bien. Yo estoy bien. Él está bien. Estamos todos bien.", F_VERB),
           ("Fernando", "Yo os veo… No estáis bien.", F_SUBJ),
           ("Josefina", "Silencio. Hay una mujer. Puede ser escritora.", F_SUBJ),
           ("Julio", "No, no es escritora.", F_VERB),
           ("Josefina", "¿Dependienta? ¿Trabaja en una tienda? ¡Ya lo sé! Es una actriz.", F_PLAC),
           ("Julio", "Si es la que creo, es profesora.", F_VERB),
           ("Josefina", "Es María, la nueva. Tú no estás bien, estás muy mal.", F_SUBJ),
           ("Fernando", "Si tú estás tranquila, yo estoy tranquilo. ¡Qué tranquilidad!", F_VERB)]
    y = Inches(1.8)
    for sp, tx, col in dia:
        chip(s, Inches(0.75), y, sp, fill=col, tcolor=WHITE, size=10)
        text(s, Inches(2.35), y - Inches(0.02), Inches(5.4), Inches(0.5),
             [[(tx, {"size": 11.5, "color": INK})]])
        y = y + Inches(0.51)
    # chunks-kaart rechts (ingekort om plaats te maken voor de video)
    card(s, Inches(8.2), Inches(1.55), Inches(4.6), Inches(2.45), fill=GT, line=G)
    text(s, Inches(8.45), Inches(1.72), Inches(4.1), Inches(2.2),
         [[("Chunks para llevar 🎒", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})],
          [("¿a qué te dedicas? · ¿en qué trabajas?", {"size": 11.5, "color": INK})],
          [("soy profesor/a · es profesora · puede ser…", {"size": 11.5, "color": INK})],
          [("trabajo en una tienda · la academia", {"size": 11.5, "color": INK})],
          [("estamos todos bien · ¿estáis bien?", {"size": 11.5, "color": INK})]])
    # echte, afspeelbare video (online YouTube-embed) — speelt in PowerPoint
    text(s, Inches(8.2), Inches(4.12), Inches(4.6), Inches(0.3),
         [[("🎬 Sitcom · Episodio 7 — klik om af te spelen", {"size": 11, "bold": True, "color": GD, "font": DISPLAY})]])
    add_online_video(s, VIDEO_ID, Inches(8.2), Inches(4.45), Inches(4.6), Inches(2.55), VIDEO_POSTER)
    footer(s, tab=FTAB, page=pg())

def s04_kit():
    s = slide(); bg(s)
    sectionbar(s, "§2 · KIT", "Las profesiones · los lugares de trabajo", "De beroepen (♂/♀), de werkplekken & naar werk vragen", num=2)
    cols = [("Las profesiones", [("el profesor · la profesora", "leraar/lerares"), ("el escritor · la escritora", "schrijver/-ster"),
              ("el actor · la actriz", "acteur · actrice"), ("el dependiente · la dependienta", "winkelbediende"),
              ("el/la estudiante", "student(e)"), ("el médico · la médica", "de dokter")]),
            ("Los lugares de trabajo", [("la academia · la escuela", "de (taal)school"), ("la tienda", "de winkel"),
              ("la oficina", "het kantoor"), ("el hospital", "het ziekenhuis"), ("el teatro", "het theater")]),
            ("Preguntar por el trabajo", [("¿A qué te dedicas?", "wat doe je (voor werk)?"), ("¿En qué trabajas?", "waarin werk je?"),
              ("¿Dónde trabajas?", "waar werk je?"), ("¿Trabaja en una tienda?", "werkt hij/zij in een winkel?")])]
    x = Inches(0.55); w = Inches(4.0)
    for title, items in cols:
        card(s, x, Inches(1.6), w, Inches(4.9), fill=WHITE, line=LINE)
        text(s, x + Inches(0.25), Inches(1.78), w - Inches(0.4), Inches(0.5),
             [[(title, {"size": 13.5, "bold": True, "color": GD, "font": DISPLAY})]])
        y = Inches(2.45)
        for es, nl in items:
            text(s, x + Inches(0.25), y, w - Inches(0.5), Inches(0.6),
                 [[(es, {"size": 13.5, "bold": True, "color": INK}), ("   " + nl, {"size": 10.5, "italic": True, "color": MUT})]])
            y = y + Inches(0.65)
        x = x + w + Inches(0.2)
    footer(s, tab=FTAB, page=pg())

def s05_presentarse():
    s = slide(); bg(s)
    sectionbar(s, "§2 · KIT", "Decir el trabajo & ¿cómo estamos?", "Je beroep zeggen & zeggen hoe het met iedereen gaat", num=2)
    left = [("Soy profesor/a", "ik ben leraar/lerares"), ("Soy estudiante", "ik ben student(e)"), ("Trabajo en una oficina", "ik werk op een kantoor"),
            ("yo trabajo · tú trabajas · él trabaja", "ik · jij · hij werk(t)"), ("¿A qué te dedicas?", "wat doe je (voor werk)?")]
    right = [("Estoy bien · tranquilo/a", "ik ben oké · rustig"), ("Estamos todos bien", "we zijn allemaal oké"), ("¿Estáis bien?", "zijn jullie oké?"),
             ("Estás muy mal", "jij bent er erg aan toe"), ("¡Qué tranquilidad!", "wat een rust!")]
    card(s, Inches(0.55), Inches(1.6), Inches(6.0), Inches(4.9), fill=GT, line=G)
    text(s, Inches(0.8), Inches(1.78), Inches(5.5), Inches(0.5),
         [[("Decir el trabajo", {"size": 13.5, "bold": True, "color": GD, "font": DISPLAY})]])
    y = Inches(2.5)
    for es, nl in left:
        text(s, Inches(0.8), y, Inches(5.4), Inches(0.6), [[(es, {"size": 15, "bold": True, "color": INK}), ("   " + nl, {"size": 11, "italic": True, "color": MUT})]])
        y = y + Inches(0.72)
    card(s, Inches(6.8), Inches(1.6), Inches(6.0), Inches(4.9), fill=WHITE, line=LINE)
    text(s, Inches(7.05), Inches(1.78), Inches(5.5), Inches(0.5),
         [[("¿Cómo estamos? · estar", {"size": 13.5, "bold": True, "color": GD, "font": DISPLAY})]])
    y = Inches(2.5)
    for es, nl in right:
        text(s, Inches(7.05), y, Inches(5.4), Inches(0.6), [[(es, {"size": 15, "bold": True, "color": INK}), ("   " + nl, {"size": 11, "italic": True, "color": MUT})]])
        y = y + Inches(0.72)
    text(s, Inches(7.05), Inches(5.7), Inches(5.5), Inches(0.7),
         [[("¡Ojo! ", {"size": 12, "bold": True, "color": RED}),
           ("soy profesora — zónder un/una · actor → actriz · el/la estudiante blijft gelijk.", {"size": 12, "italic": True, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

def s06_gram_ser():
    s = slide(); bg(s)
    sectionbar(s, "§4 · GRAMÁTICA", "ser + profesión · trabajo en…", "Je beroep zeggen zonder un/una + de trabajo-chunks uit de scène", num=4)
    legend_func(s, Inches(0.55), Inches(1.42))
    # ser + profesión-kaart (links, breed)
    card(s, Inches(0.55), Inches(1.9), Inches(7.6), Inches(4.1), fill=WHITE, line=LINE)
    text(s, Inches(0.8), Inches(2.05), Inches(7.1), Inches(0.4), [[("ser + profesión — zónder un/una", {"size": 15, "bold": True, "color": GD, "font": DISPLAY})]])
    filas = [("Soy profesora.", "ik ben lerares", "niet: soy una profesora"),
             ("Es escritor.", "hij is schrijver", "¿Es actriz? — No, es profesora."),
             ("Soy estudiante.", "ik ben student(e)", "el/la estudiante (blijft gelijk)")]
    y = Inches(2.55)
    for es, nl, ex in filas:
        text(s, Inches(0.8), y, Inches(7.2), Inches(0.4),
             [[(es + "  ", {"size": 14, "bold": True, "color": F_VERB}), (nl, {"size": 12, "color": INK}), ("   " + ex, {"size": 10.5, "italic": True, "color": MUT})]])
        y = y + Inches(0.5)
    text(s, Inches(0.8), Inches(4.15), Inches(7.1), Inches(0.4),
         [[("♂ / ♀  ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("profesor/profesora · escritor/escritora · dependiente/dependienta", {"size": 12.5, "color": INK})],
          [("actor → ", {"size": 12.5, "color": INK}), ("actriz", {"size": 12.5, "bold": True, "color": F_SUBJ}), ("  ·  el/la estudiante blijft gelijk", {"size": 12.5, "color": INK})]])
    text(s, Inches(0.8), Inches(5.25), Inches(7.1), Inches(0.6),
         [[("¡Ojo! ", {"size": 11.5, "bold": True, "color": RED}), ("nooit «soy una profesora» — beroep = zonder lidwoord.", {"size": 11.5, "italic": True, "color": INK})]])
    # trabajo-chunks-kaart (rechts)
    card(s, Inches(8.4), Inches(1.9), Inches(4.4), Inches(4.1), fill=GT, line=G)
    text(s, Inches(8.65), Inches(2.05), Inches(3.9), Inches(0.4), [[("trabajo · trabajas · trabaja", {"size": 15, "bold": True, "color": GD, "font": DISPLAY})]])
    text(s, Inches(8.65), Inches(2.6), Inches(3.9), Inches(2.4),
         [[("(yo) ", {"size": 13, "color": F_SUBJ}), ("trabajo", {"size": 14, "bold": True, "color": F_VERB}), ("  ik werk", {"size": 11, "italic": True, "color": MUT})],
          [("(tú) ", {"size": 13, "color": F_SUBJ}), ("trabajas", {"size": 14, "bold": True, "color": F_VERB}), ("  jij werkt", {"size": 11, "italic": True, "color": MUT})],
          [("(él/ella) ", {"size": 13, "color": F_SUBJ}), ("trabaja", {"size": 14, "bold": True, "color": F_VERB}), ("  hij/zij werkt", {"size": 11, "italic": True, "color": MUT})],
          [("", {"size": 6})],
          [("Trabajo ", {"size": 14, "bold": True, "color": F_VERB}), ("en una tienda", {"size": 14, "bold": True, "color": F_PLAC}), (".", {"size": 14, "color": INK})],
          [("chunks uit de scène — leer ze als vaste vormen", {"size": 10.5, "italic": True, "color": MUT})]])
    text(s, Inches(8.65), Inches(5.15), Inches(3.9), Inches(0.7),
         [[("¡Ojo! ", {"size": 11.5, "bold": True, "color": RED}), ("werkplek altijd met en: trabajo en una academia · en casa.", {"size": 11.5, "italic": True, "color": INK})]])
    notes(s, "Functioneel: je beroep zeggen met ser + profesión ZONDER un/una (soy profesora, nooit «soy una profesora»). ♂/♀-vormen: profesor/profesora · escritor/escritora · dependiente/dependienta · actor/actriz; el/la estudiante blijft gelijk. trabajo/trabajas/trabaja zijn CHUNKS uit de scène («yo trabajo aquí, tú trabajas aquí…») — géén vervoegingsparadigma aanleren; het volledige werkwoordsysteem komt in het 5de jaar (C5). Werkplek altijd met en (trabajo en una tienda — plaats = turquoise). Doelcodes: C4-SP-1 · C4-WS-1.")
    footer(s, tab=FTAB, page=pg())

def s07_gram_mv():
    s = slide(); bg(s)
    sectionbar(s, "§4 · GRAMÁTICA", "ser ↔ estar", "Wie/wat je bent → ser · hoe je je voelt (toestand) → estar", num=4)
    # ser-kaart
    card(s, Inches(0.55), Inches(1.65), Inches(7.6), Inches(2.5), fill=WHITE, line=LINE)
    text(s, Inches(0.8), Inches(1.8), Inches(7.1), Inches(0.4), [[("SER — wie/wat je bent", {"size": 15, "bold": True, "color": GD, "font": DISPLAY})]])
    filas = [("es profesora", "beroep (wie/wat)", "Si es la que creo, es profesora."),
             ("soy belga", "afkomst (U3)", "Soy de Bélgica."),
             ("es María, la nueva", "identiteit", "¿Es actriz? — No, es profesora.")]
    y = Inches(2.35)
    for p, nl, ex in filas:
        text(s, Inches(0.8), y, Inches(7.2), Inches(0.4),
             [[(p + "  ", {"size": 13, "bold": True, "color": F_VERB}), (nl, {"size": 12.5, "color": INK}), ("   " + ex, {"size": 11, "italic": True, "color": MUT})]])
        y = y + Inches(0.52)
    # estar-kaart
    card(s, Inches(8.4), Inches(1.65), Inches(4.4), Inches(2.5), fill=GT, line=G)
    text(s, Inches(8.65), Inches(1.8), Inches(3.9), Inches(0.4), [[("ESTAR — toestand", {"size": 15, "bold": True, "color": GD, "font": DISPLAY})]])
    text(s, Inches(8.65), Inches(2.35), Inches(3.9), Inches(1.7),
         [[("Estoy ", {"size": 14, "bold": True, "color": F_VERB}), ("bien · tranquilo/a", {"size": 14, "color": INK})],
          [("Estamos ", {"size": 14, "bold": True, "color": F_VERB}), ("todos bien ", {"size": 14, "color": INK}), ("wij", {"size": 11, "italic": True, "color": MUT})],
          [("¿", {"size": 14, "color": INK}), ("Estáis", {"size": 14, "bold": True, "color": F_VERB}), (" bien? ", {"size": 14, "color": INK}), ("jullie", {"size": 11, "italic": True, "color": MUT})],
          [("Tú no estás bien, estás muy mal.", {"size": 12.5, "italic": True, "color": MUT})]])
    # mini-quiz met reveal
    card(s, Inches(0.55), Inches(4.35), Inches(12.25), Inches(1.7), fill=GT, line=G)
    text(s, Inches(0.8), Inches(4.5), Inches(11.7), Inches(0.5),
         [[("Completa · vul aan (klik voor de oplossing): ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("María ___ profesora.  Julio no ___ bien.  Nosotros ___ tranquilos.", {"size": 13, "color": INK})]])
    exercise_solucion(s, Inches(0.8), Inches(5.15), Inches(11.7), Inches(0.7),
        [[("es · está · estamos", {"bold": True, "color": GD, "size": 13})]])
    noodroute(s)
    notes(s, "Functioneel: ser = wie/wat je bent (es profesora · soy belga · es María) ↔ estar = toestand/hoe je je voelt (estoy bien · está tranquila · estamos todos bien · ¿estáis bien?). Nieuw uit de scène: estamos/estáis — als chunks, geen paradigma (het volledige werkwoordsysteem is C5). estar kennen ze al van U2 (estoy cansado) en U6 (¿dónde está?). Oplossing: es · está · estamos.")
    footer(s, tab=FTAB, page=pg())

def s08_practica():
    s = slide(); bg(s)
    sectionbar(s, "§3 · PRÁCTICA", "Completa el diálogo", "Vul samen aan — klik voor de oplossing", num=3)
    card(s, Inches(0.55), Inches(1.7), Inches(7.6), Inches(4.5), fill=WHITE, line=LINE)
    lines = [("— ¿A qué te ___?", "dedicas"),
             ("— ___ profesora.", "Soy"),
             ("— ¿Y dónde ___?", "trabajas"),
             ("— ___ en una academia.", "Trabajo"),
             ("— ¿Y ___ contenta? — Sí, muy contenta.", "estás")]
    y = Inches(1.95)
    for q, _a in lines:
        text(s, Inches(0.8), y, Inches(7.1), Inches(0.6), [[(q, {"size": 16, "color": INK})]])
        y = y + Inches(0.8)
    exercise_solucion(s, Inches(8.4), Inches(1.9), Inches(4.4), Inches(4.0),
        [[("1. dedicas", {"color": GD, "size": 14})], [("2. Soy", {"color": GD, "size": 14})],
         [("3. trabajas", {"color": GD, "size": 14})], [("4. Trabajo", {"color": GD, "size": 14})],
         [("5. estás", {"color": GD, "size": 14})]],
        title_doc="SOLUCIÓN · docent")
    noodroute(s)
    notes(s, "Laat leerlingen eerst zelf proberen (in duo). Klik daarna de oplossing open. Let op: ¿a qué te dedicas? = de vaste kennismakingsvraag; Soy profesora (zonder un/una); trabajas/trabajo als chunks + en (trabajo en una academia); ¿estás contenta? = toestand → estar. Oplossing: dedicas · Soy · trabajas · Trabajo · estás.")
    footer(s, tab=FTAB, page=pg())

def s09_speaking():
    s = slide(); bg(s)
    sectionbar(s, "§3 · HABLAR", "¿Quién soy? · adivina", "Geef pistas over een beroep en laat je buur gissen — sin leer", num=3)
    card(s, Inches(0.55), Inches(1.7), Inches(7.6), Inches(3.4), fill=GT, line=G)
    text(s, Inches(0.85), Inches(1.95), Inches(7.1), Inches(3.0),
         [[("Modelo · zeg dit hardop:", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})],
          [("«— Trabajo en un hospital.", {"size": 18, "color": INK})],
          [("Estoy con muchas personas.", {"size": 18, "color": INK})],
          [("— ¿Puede ser… médica?", {"size": 18, "color": INK})],
          [("— ¡Sí! Soy médica.»", {"size": 18, "color": INK})]])
    card(s, Inches(8.4), Inches(1.7), Inches(4.4), Inches(3.4), fill=WHITE, line=LINE)
    text(s, Inches(8.65), Inches(1.95), Inches(3.9), Inches(3.0),
         [[("¿Cómo? · Werkvorm", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})],
          [("1. Kies (geheim!) een beroep.", {"size": 13, "color": INK})],
          [("2. Geef pistas: «trabajo en… · estoy…».", {"size": 13, "color": INK})],
          [("3. Je buur gist: «¿puede ser…?».", {"size": 13, "color": INK})],
          [("4. Wissel van rol (3×).", {"size": 13, "color": INK})]])
    text(s, Inches(0.6), Inches(5.4), Inches(12), Inches(0.7),
         [[("Interactie ", {"size": 12, "bold": True, "color": GD, "font": DISPLAY}),
           ("= beurt nemen, gissen en reageren. Begrijp je iets niet? Zeg: «¿Cómo? / Otra vez, por favor.»", {"size": 12, "italic": True, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

def s10_musica():
    s = slide(); bg(s)
    sectionbar(s, "CULTURA", "El trabajo en el mundo hispano", "Hoe werk klinkt in de Spaanstalige wereld + muziek die jullie kennen", num=None)
    bandas = [("Rosalía", "La Perla", "🇪🇸 España"), ("Juanes", "A Dios le Pido", "🇨🇴 Colombia"),
              ("Álvaro Soler", "Sofía", "🇪🇸 España"), ("Marc Anthony", "Vivir Mi Vida", "🇵🇷 P. Rico"),
              ("Manu Chao", "Me Gustas Tú", "🇪🇸/🇫🇷"), ("Shakira", "Antología", "🇨🇴 Colombia")]
    x0, y0 = Inches(0.55), Inches(1.75); w = Inches(4.0)
    for i, (ar, sg, ge) in enumerate(bandas):
        col = i % 3; row = i // 3
        x = x0 + col * (w + Inches(0.18)); y = y0 + row * (Inches(1.5) + Inches(0.18))
        card(s, x, y, w, Inches(1.5), fill=WHITE, line=LINE)
        text(s, x + Inches(0.25), y + Inches(0.2), w - Inches(0.4), Inches(1.2),
             [[(ar, {"size": 15, "bold": True, "color": INK, "font": DISPLAY})],
              [("🎵 " + sg, {"size": 12, "color": MUT})], [(ge, {"size": 11, "color": GD})]])
    card(s, Inches(0.55), Inches(5.5), Inches(12.25), Inches(1.05), fill=GT, line=G)
    text(s, Inches(0.85), Inches(5.65), Inches(11.7), Inches(0.8),
         [[("💼 El trabajo en el mundo hispano ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("soy profesor — zónder un/una · het horario partido (winkels dicht van 14 tot 17 u) · beroemde beroepen: Frida Kahlo pintora · García Márquez escritor · Messi futbolista · Rosalía cantante. Playlist + LyricsTraining op de digitale hub → tabblad Música.", {"size": 12, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

def s11_tarea():
    s = slide(); bg(s)
    sectionbar(s, "§5 · TAREA FINAL", "¿Quién soy? · adivina la profesión", "Kies geheim een beroep, geef 3 pistas — de klas gist zoals Josefina", num=5)
    card(s, Inches(0.55), Inches(1.7), Inches(6.0), Inches(3.5), fill=WHITE, line=G, lw=1.6)
    rect(s, Inches(0.55), Inches(1.7), Inches(6.0), Inches(0.55), fill=G)
    text(s, Inches(0.75), Inches(1.78), Inches(5.6), Inches(0.4), [[("FICHA · noteer je frames", {"size": 12, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(0.85), Inches(2.5), Inches(5.4), Inches(2.5),
         [[("💼 Mi profesión: ", {"size": 14, "bold": True, "color": INK}), ("____ (geheim!).", {"size": 14, "color": LINE})],
          [("🕵️ Pista: Trabajo en ", {"size": 14, "bold": True, "color": INK}), ("____ · Estoy ____ .", {"size": 14, "color": LINE})],
          [("🎯 Adivina: ¿Puede ser ", {"size": 14, "bold": True, "color": INK}), ("____ ? · ¡Ya lo sé!", {"size": 14, "color": LINE})]])
    card(s, Inches(6.8), Inches(1.7), Inches(6.0), Inches(3.5), fill=GT, line=G)
    text(s, Inches(7.05), Inches(1.9), Inches(5.5), Inches(3.1),
         [[("Los pasos · stappen", {"size": 14, "bold": True, "color": GD, "font": DISPLAY})],
          [("1. Elige (geheim!) una profesión + werkplek.", {"size": 13, "color": INK})],
          [("2. Da tres pistas: «trabajo en…» · «estoy…» · «trabajo con…».", {"size": 13, "color": INK})],
          [("3. La clase adivina: «¿puede ser…?» · «¿trabajas en…?» · «¡ya lo sé!».", {"size": 13, "color": INK})],
          [("4. Confirma: «Sí, soy…» / «No, no soy…» — wie raadt, is aan de beurt.", {"size": 13, "color": INK})]])
    text(s, Inches(0.6), Inches(5.5), Inches(12), Inches(0.9),
         [[("🏁 Klaar als… ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("je drie pistas geeft met «trabajo en…» + «estoy…», en gist/antwoordt met ser zónder un/una («¿puede ser médica?» — «sí, soy médica») — zónder af te lezen.", {"size": 12.5, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

def s12_repaso():
    s = slide(); bg(s)
    sectionbar(s, "REPASO", "Lo esencial de un vistazo", "Wat je nu kunt — semáforo", num=None)
    card(s, Inches(0.55), Inches(1.7), Inches(7.6), Inches(4.4), fill=WHITE, line=LINE)
    text(s, Inches(0.85), Inches(1.9), Inches(7.1), Inches(4.0),
         [[("Zo praat je over werk", {"size": 14, "bold": True, "color": GD, "font": DISPLAY})],
          [("¿A qué te dedicas? · ¿En qué trabajas? · ¿Dónde trabajas?", {"size": 13.5, "color": INK})],
          [("Soy profesor/a · soy estudiante — zónder un/una", {"size": 13, "color": INK})],
          [("trabajo · trabajas · trabaja + en (trabajo en una tienda)", {"size": 13, "color": INK})],
          [("", {"size": 6})],
          [("ser ↔ estar · ♂/♀", {"size": 14, "bold": True, "color": GD, "font": DISPLAY})],
          [("ser = wie/wat je bent (es profesora) · estar = toestand (estoy bien)", {"size": 13, "color": INK})],
          [("estamos todos bien · ¿estáis bien? · estás muy mal", {"size": 13, "color": INK})],
          [("profesor/profesora · actor/actriz · el/la estudiante", {"size": 13, "color": INK})]])
    card(s, Inches(8.4), Inches(1.7), Inches(4.4), Inches(4.4), fill=GT, line=G)
    text(s, Inches(8.65), Inches(1.9), Inches(3.9), Inches(0.5), [[("Puedo… · Ik kan…", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    items = ["naar werk vragen (¿a qué te dedicas?)", "mijn beroep zeggen zónder un/una", "trabajo/trabajas/trabaja + en gebruiken", "ser en estar juist kiezen", "gissen zoals Josefina (¿puede ser…?)"]
    y = Inches(2.5)
    for it in items:
        text(s, Inches(8.65), y, Inches(3.9), Inches(0.7), [[("🟢🟡🔴  ", {"size": 12}), (it, {"size": 11.5, "color": INK})]])
        y = y + Inches(0.62)
    text(s, Inches(8.65), Inches(5.6), Inches(3.9), Inches(0.7), [[("🎮 Repasa jugando", {"size": 12, "bold": True, "color": GD, "font": DISPLAY})], [("online op de hub · ¿quién soy?", {"size": 11, "italic": True, "color": MUT})]])
    footer(s, tab=FTAB, page=pg())

def s13_teacher():
    s = slide(); bg(s, color=RGBColor(0x24,0x1C,0x1B))
    text(s, Inches(0.6), Inches(0.5), Inches(12), Inches(0.7), [[("Docentendossier · Unidad 7 «Las profesiones»", {"size": 22, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(0.6), Inches(1.4), Inches(12.1), Inches(5.4),
         [[("Timing (2 lesuren van 50 min).", {"size": 14, "bold": True, "color": RGBColor(0xFB,0xEA,0xEC), "font": DISPLAY})],
          [("Les 1: Escucha (sitcom ep. 7 · id _636fQfHIa4, Fernando ondervraagt María «yo trabajo aquí, tú trabajas aquí…»; waarzegster Josefina leest de kaarten en gist beroepen) + Suena bien (c + a/o/u = /k/ · qu + e/i = /k/ met stille u · la esdrújula) + Kit (profesiones ♂/♀ · lugares de trabajo · preguntar por el trabajo). Les 2: gramática functioneel (ser + profesión zonder un/una · trabajo-chunks + en · ser ↔ estar), hablar «¿Quién soy? · adivina», tarea + cultura.", {"size": 12.5, "color": RGBColor(0xEC,0xEA,0xE3)})],
          [("", {"size": 6})],
          [("Aanpak C4 (survival).", {"size": 14, "bold": True, "color": RGBColor(0xFB,0xEA,0xEC), "font": DISPLAY})],
          [("Chunks komen auditief binnen (luisteren → naspreken). trabajo/trabajas/trabaja en estamos/estáis presenteren als CHUNKS uit de scène — géén vervoegingsparadigma; het volledige werkwoordsysteem komt in het 5de jaar (C5). Kernvalstrikken: soy profesora zónder un/una (nooit «soy una profesora»); ♂/♀: profesor/profesora · escritor/escritora · dependiente/dependienta · actor/actriz, el/la estudiante blijft gelijk; ser = wie/wat je bent ↔ estar = toestand; werkplek met en (trabajo en una tienda); qu = /k/ met stille u (que = «ke», niet «kwe»); esdrújula = altijd tilde (MÉ·di·co). Doelcodes: C4-SP-1 · C4-STR-1 · C4-GE-1 · C4-WS-1 · C4-MEC-1/2 · C4-CU-1.", {"size": 12.5, "color": RGBColor(0xEC,0xEA,0xE3)})],
          [("", {"size": 6})],
          [("Evaluatie.", {"size": 14, "bold": True, "color": RGBColor(0xFB,0xEA,0xEC), "font": DISPLAY})],
          [("Mondelinge mini-taak («¿Quién soy? · adivina la profesión»: geheim beroep kiezen, drie pistas geven met «trabajo en…» / «estoy…» / «trabajo con…», de klas gist met «¿puede ser…?»). Geen leerplan → focus op «kunnen gebruiken in de praktijk». Rubric: pistas correct (trabajo en · estoy) · adivinar + ser zonder un/una · uitspraak & durf.", {"size": 12.5, "color": RGBColor(0xEC,0xEA,0xE3)})],
          [("", {"size": 6})],
          [("Oplossingen staan bij elke oefendia in de presenter-notities; antwoorden verschijnen bij klik.", {"size": 11.5, "italic": True, "color": RGBColor(0xA6,0xA2,0x9A)})]])
    footer(s, tab=FTAB, page=pg())

def s_uitspraak():
    s = slide(); bg(s)
    sectionbar(s, "SUENA BIEN", "c + a/o/u = /k/ · qu + e/i = /k/ · la esdrújula", "De /k/-klank (met stille u!) & de klemtoon op de 3de lettergreep van achter", num=None)
    # c fuerte-kaart
    card(s,Inches(0.55),Inches(1.6),Inches(6.05),Inches(2.15),fill=WHITE,line=LINE)
    rect(s,Inches(0.55),Inches(1.6),Inches(6.05),Inches(0.14),fill=G)
    text(s,Inches(0.8),Inches(1.85),Inches(5.6),Inches(0.4),[[("c + a/o/u = /k/ · la c fuerte",{"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
    text(s,Inches(0.8),Inches(2.35),Inches(5.6),Inches(1.3),
         [[("casa · cocina · médico · actriz · carta · tranquilo",{"size":15,"bold":True,"color":INK})],
          [("vóór a, o, u klinkt de c als /k/ (vergelijk: cine /θ/ · U3).",{"size":11,"italic":True,"color":MUT})]])
    # qu-kaart
    card(s,Inches(6.75),Inches(1.6),Inches(6.05),Inches(2.15),fill=WHITE,line=LINE)
    rect(s,Inches(6.75),Inches(1.6),Inches(6.05),Inches(0.14),fill=G)
    text(s,Inches(7.0),Inches(1.85),Inches(5.6),Inches(0.4),[[("qu + e/i = /k/ · de stille u",{"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
    text(s,Inches(7.0),Inches(2.35),Inches(5.6),Inches(1.3),
         [[("queso = «ke-so» · ¿quién? = «kjen» · aquí · pequeño",{"size":14,"bold":True,"color":INK})],
          [("vóór e en i schrijf je qu — de u hoor je NIET.",{"size":11,"italic":True,"color":MUT})]])
    card(s,Inches(0.55),Inches(3.9),Inches(12.25),Inches(0.85),fill=GT,line=G)
    text(s,Inches(0.85),Inches(4.05),Inches(11.7),Inches(0.6),
         [[("¡Ojo! ",{"size":13,"bold":True,"color":RED,"font":DISPLAY}),("que",{"size":13,"bold":True,"color":GD}),(" = «ke» (niet «kwe»!) · ",{"size":13,"color":INK}),("qui",{"size":13,"bold":True,"color":GD}),(" = «ki». Vergelijk: ",{"size":13,"color":INK}),("c",{"size":13,"bold":True,"color":GD}),("asa /k/ maar ",{"size":13,"color":INK}),("c",{"size":13,"bold":True,"color":GD}),("ine /θ/ — dáárom bestaat qu!",{"size":13,"color":INK})]])
    text(s,Inches(0.6),Inches(5.0),Inches(12),Inches(0.4),[[("La esdrújula · klemtoon op de 3de lettergreep van achter — áltijd een accent",{"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
    text(s,Inches(0.6),Inches(5.55),Inches(12.2),Inches(0.7),
         [[("MÉ",{"color":G,"bold":True}),("·di·co      ",{}),("MÚ",{"color":G,"bold":True}),("·si·ca      ",{}),("SÁ",{"color":G,"bold":True}),("·ba·do      te·",{}),("LÉ",{"color":G,"bold":True}),("·fo·no",{})]],size=20,font=DISPLAY)
    text(s,Inches(0.6),Inches(6.35),Inches(12),Inches(0.4),[[("🔊 Oefen de klanken online op de hub (tabblad Kit · Suena bien).",{"size":11,"italic":True,"color":MUT})]])
    footer(s, tab=FTAB, page=pg())

# ── Funciones-comunicativas-dia (matrix C) — leest de gedeelde funciones_data ──
import sys as _sys
_sys.path.insert(0, os.path.join(os.path.dirname(HERE), "web"))
import funciones_data as FD
FUNC_UNIT = 7
def s_funciones():
    s = slide(); bg(s)
    sectionbar(s, "FUNCIONES", "Mis funciones comunicativas", "Lo que ya sé hacer — crece cada unidad", num=None)
    fs = FD.funciones_hasta(FUNC_UNIT); have=len(fs); total=len(FD.FUNCIONES)
    text(s, Inches(0.6), Inches(1.42), Inches(12.2), Inches(0.35),
         [[("Mi repertorio: %d / %d funciones — " % (have,total), {"size":13,"bold":True,"color":GD,"font":DISPLAY}),
           ("no solo palabras: lo que puedo HACER con el español.", {"size":12,"color":MUT})]])
    cols_x=[Inches(0.55), Inches(6.85)]; w=Inches(5.9)
    # adaptieve rijhoogte: bij 16 funciones (U7, incl. de nieuwe F15/F16) mag geen
    # rij van de dia vallen → pitch schaalt met het aantal rijen (blijft ≤ 1.32);
    # bij ≥15 funciones zakt ook de fontgrootte van de exponentes-regel mee.
    nrows = (len(fs) + 1) // 2
    top = 1.82; bottom = 7.0
    pitch = min(1.32, (bottom - top) / nrows)
    ch = pitch - 0.16
    exsz = 8.5 if have <= 14 else 7.0
    for i,f in enumerate(fs):
        col=i%2; row=i//2
        x=cols_x[col]; y=Inches(top+row*pitch)
        st=FD.status(f,FUNC_UNIT); hot = st in ("nueva","nivel")
        card(s,x,y,w,Inches(ch),fill=(GT if hot else WHITE),line=(G if hot else LINE))
        badge = "  ● NUEVA" if st=="nueva" else ("  ▲ nivel+" if st=="nivel" else "")
        text(s,x+Inches(0.22),y+Inches(0.05),w-Inches(0.44),Inches(0.28),
             [[(f["es"], {"size":11,"bold":True,"color":INK,"font":DISPLAY}),(badge,{"size":9,"bold":True,"color":GD})]])
        exps=" · ".join(e for u in sorted(k for k in f["exp"] if k<=FUNC_UNIT) for e in f["exp"][u])
        text(s,x+Inches(0.22),y+Inches(0.05)+Inches(ch*0.45),w-Inches(0.44),Inches(ch*0.5),[[(exps,{"size":exsz,"color":MUT})]])
    footer(s, tab=FTAB, page=pg())

def _run_all_slides(include_teacher=True):
    s01_title(); s02_menu(); s03_escucha(); s_uitspraak()
    s04_kit(); s05_presentarse(); s06_gram_ser()
    s07_gram_mv(); s08_practica(); s09_speaking()
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
