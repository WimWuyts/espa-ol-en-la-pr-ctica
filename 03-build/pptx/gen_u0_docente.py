#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_u0_docente.py — Interactieve PowerPoint C5 · Unidad 0 «¡Empezamos!»
========================================================================
Gedeelde builder (één bron) → TWEE decks:
  · C5_U0_docente.pptx  — docentversie: vrije navigatie; antwoorden verschijnen bij
    klik (fade) + volledige oplossing & didactiek in de spreker-notities.
  · C5_U0_alumno.ppsx   — leerlingversie: GEEN docentnotities, GEEN kiosk; gewone
    diavoorstelling waarin de antwoorden/oplossingen bij klik verschijnen.

ECHTE interactiviteit: op elke oefendia (QUIZ/WRITING/SPEAKING + números/tilde)
wordt <p:timing>-XML geïnjecteerd met standaard SEQUENTIËLE on-click entrance-
animaties (fade-in) in de hoofdsequentie (mainSeq): elke klik onthult de volgende
reveal-shape. Dit is exact wat PowerPoint schrijft voor «Fade, Start: On Click».
+ hyperlink-navigatie (menutegels, ⌂ Menú). Cast-avatars = de ECHTE flat-vector
SVG's (zie render_avatars.py).

Volgt INTERACTIEVE_POWERPOINT_50_IDEEEN.md:
  - diamaster-layouts (TITLE · LESSON_MENU · VOCABULARY · GRAMMAR · READING ·
    LISTENING · SPEAKING · WRITING · QUIZ · FEEDBACK · CULTURE · FINAL_MISSION ·
    TEACHER_NOTES)
  - drie lagen CONTENT / INTERACTION / TEACHER
  - noodroute (toon oplossing / sla over / terug) op elke oefendia
Huisstijl (kit.json): unitkleur groen #1E9E74. Spaans-eerst + NL-steun.
Twee kleurlagen: cursusgroen (navigatie) + functionele taalsemantiek.
Bron: 01-cursussen/05-a1/U0/U0_bron.md  ·  01-cursussen/05-a1/U0/U0.html
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
OUT_DOCENTE = os.path.join(HERE, "C5_U0_docente.pptx")
OUT_ALUMNO_PPTX = os.path.join(HERE, "C5_U0_alumno.pptx")
OUT_ALUMNO = os.path.join(HERE, "C5_U0_alumno.ppsx")

# --- build-modus (wordt door build() gezet) ---
MODE = "docente"          # "docente" | "alumno"
import sys as _sys
_sys.path.insert(0, "/home/user/espa-ol-en-la-pr-ctica/03-build/web")
import lectura_data as _LD, escucha_data as _ED
_LEC = _LD.C5_U0
_ESC = _ED.C5_U0

def is_alumno():
    return MODE == "alumno"

# ---------------------------------------------------------------- kleuren (kit.json)
G      = RGBColor(0x1E, 0x9E, 0x74)  # unitgroen (hoofdkleur)
GD     = RGBColor(0x15, 0x73, 0x55)  # donkergroen
GT     = RGBColor(0xE4, 0xF4, 0xEE)  # groen-tint (vlak)
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
F_VERB = RGBColor(0xEA, 0x73, 0x17)  # werkwoord          (oranje)
F_OBJ  = RGBColor(0x1E, 0x9E, 0x74)  # voorwerp           (groen)
F_TIME = RGBColor(0x7C, 0x3A, 0xED)  # tijd               (paars)
F_PLAC = RGBColor(0x14, 0xB8, 0xA6)  # plaats             (turquoise)
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
    """Zachte slagschaduw — in de BESTAANDE effectLst, niet in een tweede.

    `shp.shadow.inherit = False` (in rect()) laat python-ppt al een lege
    <a:effectLst/> achter. Hingen we daar een tweede naast, dan had de vorm er
    twee, en dat laat het schema niet toe (CT_ShapeProperties: hoogstens één).
    PowerPoint vroeg daardoor bij elk deck om te «Repareren». Vandaar: hergebruik
    wat er staat, en maak alleen een nieuwe aan als er nog geen is.
    """
    spPr = shp._element.spPr
    el = spPr.find(qn('a:effectLst'))
    if el is None:
        el = spPr.makeelement(qn('a:effectLst'), {})
        spPr.append(el)
    else:
        for viejo in list(el):          # leeg maken: één schaduw per vorm
            el.remove(viejo)
    sh = el.makeelement(qn('a:outerShdw'),
                        {'blurRad': '90000', 'dist': '38000', 'dir': '5400000', 'rotWithShape': '0'})
    clr = sh.makeelement(qn('a:srgbClr'), {'val': '20242E'})
    alp = clr.makeelement(qn('a:alpha'), {'val': '22000'})
    clr.append(alp); sh.append(clr); el.append(sh)

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

def footer(s, tab="U0 · ¡EMPEZAMOS!", page=None):
    rect(s, 0, Inches(7.16), EMU_W, Inches(0.34), fill=CREMA)
    text(s, Inches(0.45), Inches(7.18), Inches(6), Inches(0.3),
         [[("● ", {"color": G, "size": 11, "bold": True}),
           (tab + "   ·   C5 · A1 · La Ruta", {"color": MUT, "size": 9.5})]],
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
    """Zichtbaar oplossingskader (alleen docentversie). Groen-getint met label."""
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
# DIA 1 · TITLE — ¡Empezamos!
# ============================================================================
def s01_title():
    s = slide(); bg(s, PAPER)
    # groene hero-band met bleed
    rect(s, 0, 0, EMU_W, Inches(4.7), fill=G)
    rect(s, 0, Inches(4.7), EMU_W, Inches(0.09), fill=GD)
    # groot unitnummer
    text(s, Inches(0.6), Inches(0.35), Inches(3.4), Inches(3.6),
         [[("0", {"size": 260, "bold": True, "color": RGBColor(0x2E,0xB0,0x85), "font": DISPLAY})]],
         anchor=MSO_ANCHOR.MIDDLE)
    # titelblok
    chip(s, Inches(4.35), Inches(0.85), "LA RUTA · PARADA 0 · EL MUNDO HISPANO", fill=WHITE, tcolor=GD, size=12)
    text(s, Inches(4.3), Inches(1.35), Inches(8.6), Inches(1.5),
         [[("¡Empezamos!", {"size": 72, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(4.35), Inches(2.7), Inches(8.4), Inches(0.6),
         [[("We beginnen! — jouw eerste stappen in het Spaans en op La Ruta.",
            {"size": 16, "italic": True, "color": GT})]])
    text(s, Inches(4.35), Inches(3.35), Inches(8.4), Inches(0.9),
         [[("¿Estás listo/a para el viaje?", {"size": 26, "bold": True, "color": WHITE, "font": DISPLAY})],
          [("Klaar voor de reis?", {"size": 13, "italic": True, "color": GT})]])
    # cast-strip onderaan
    text(s, Inches(0.6), Inches(4.95), Inches(6), Inches(0.4),
         [[("La gente de la ruta — je reisgezellen", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    x = Inches(0.6)
    for nm, city in [("lucia","Sevilla 🇪🇸"),("diego","CDMX 🇲🇽"),("valen","Cartagena 🇨🇴"),
                     ("nina","Cusco 🇵🇪"),("tu","Tú · Flandes 🇧🇪"),("mochila","La mochila")]:
        avatar(s, nm, x, Inches(5.4), Inches(1.0))
        text(s, x - Inches(0.15), Inches(6.42), Inches(1.3), Inches(0.5),
             [[(nm.capitalize() if nm!="tu" else "Tú", {"size": 10.5, "bold": True, "color": INK})],
              [(city.split("·")[-1].strip() if nm!="tu" else "de reiziger = jij", {"size": 8.5, "color": MUT})]],
             align=PP_ALIGN.CENTER)
        x = x + Inches(2.05)
    footer(s, page=pg())
    notes(s, "TEACHER · TITLE. Open de reis (La Ruta). Stel cast + mochila voor (30-40 s). "
             "Klasritueel: laat de klas straks (§4/opener) de NAAM van de mochila kiezen. "
             "Instructietaal: Spaans-eerst met NL-steun. Timing hele les: 50 min — zie dia TEACHER_NOTES. "
             "Docentversie = vrije navigatie + oplossing in notities; leerlingversie (.ppsx) = "
             "gewone diavoorstelling waarin elke klik het volgende antwoord onthult (geen kiosk).")

# ============================================================================
# DIA 2 · LESSON_MENU — interactieve startpagina (idee 1)
# ============================================================================
def s02_menu():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "MENÚ DE LA LECCIÓN", "El mapa de la Unidad 0",
               "Kies je route — klik een tegel (of volg de volgorde). Alles oefent naar de Tarea final toe.", num=0)
    # dia = werkelijk dianummer (1-based) = doel van de hyperlink (index = dia-1)
    tiles = [
        ("§1", "Sonar en español", "alfabet · uitspraak · klanktrampas", G, 4),
        ("§2", "La regla del sombrero", "klemtoon · aguda/llana/esdrújula · tilde", G, 7),
        ("§3", "Números 0–100", "tellen · leeftijd · telefoon", G, 10),
        ("§4", "Saludos y clase", "groeten · voorstellen · lengua de clase", G, 13),
        ("★", "Cultura", "¿Dónde se habla español? (+20 países)", GD, 16),
        ("✈", "Tarea final", "Tarjeta de embarque (eindmissie)", GD, 18),
        ("?", "Quiz «La mezcla»", "gemengde ophaal — mét oplossing", AMBER, 19),
        ("◎", "Repaso + semáforo", "lo esencial · zelfevaluatie", GD, 20),
    ]
    cols, x0, y0 = 4, Inches(0.5), Inches(1.55)
    tw, th, gx, gy = Inches(3.0), Inches(2.45), Inches(0.14), Inches(0.2)
    for i, (tag, es, nl, col, dia) in enumerate(tiles):
        r, c = divmod(i, cols)
        x = x0 + c * (tw + gx); y = y0 + r * (th + gy)
        cardshp = card(s, x, y, tw, th, fill=WHITE, line=col, lw=1.6)
        link_to(cardshp, dia - 1)  # hele tegel = klikbare hyperlink naar de sectie
        hdr = rect(s, x, y, tw, Inches(0.5), fill=col, round=False)
        link_to(hdr, dia - 1)  # kopbalk ligt bovenop → ook klikbaar
        # ronde badge
        b = rect(s, x + Inches(0.12), y + Inches(0.08), Inches(0.34), Inches(0.34),
                 fill=WHITE, round=True, radius=0.5)
        tf=b.text_frame; tf.vertical_anchor=MSO_ANCHOR.MIDDLE; p=tf.paragraphs[0]; p.alignment=PP_ALIGN.CENTER
        rr=p.add_run(); rr.text=tag; rr.font.size=Pt(12); rr.font.bold=True; rr.font.name=DISPLAY; rr.font.color.rgb=col
        text(s, x + Inches(0.58), y + Inches(0.06), tw - Inches(0.7), Inches(0.4),
             [[(es, {"size": 14.5, "bold": True, "color": WHITE, "font": DISPLAY})]],
             anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(0.18), y + Inches(0.68), tw - Inches(0.36), Inches(1.2),
             [[(nl, {"size": 11.5, "color": INK})]], line=1.12)
        chip(s, x + Inches(0.18), y + th - Inches(0.45), f"→ dia {dia}", fill=GT, tcolor=GD, size=9.5)
    footer(s, page=pg())
    notes(s, "TEACHER · LESSON_MENU (idee 1: interactieve startpagina · idee 3: niet-lineaire keuze). "
             "Vaste navigatie: elke tegel = hyperlink naar de betreffende dia; op elke oefendia staat ⌂ Menú terug hierheen. "
             "Kies je route naargelang de klas (zij-instromers): begin gerust bij §4 (saludos) om drempel te verlagen, "
             "of lineair §1→Repaso. Richttijd totaal 50 min (zie laatste dia).")

# ============================================================================
# DIA 3 · SPEAKING/STORY — la gente de la ruta (audiopaneel personages, idee 34)
# ============================================================================
def s03_cast():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "LA RUTA · PERSONAJES", "La gente de la ruta",
               "Je koppelt de reis aan mensen, niet aan een landenlijst. Tú = de reiziger (jij).")
    people = [
        ("lucia", "Lucía", "Sevilla 🇪🇸", "«¡Hola! Yo soy Lucía, de Sevilla.»", "gastvrouw España · familie (U2)"),
        ("diego", "Diego", "CDMX 🇲🇽", "«¡Qué onda! Soy Diego, de México.»", "eten & markt (U5–U6)"),
        ("valen", "Valen", "Cartagena 🇨🇴", "«¡Hey! Soy Valen, de Colombia.»", "wonen & barrio (U7)"),
        ("nina", "Nina", "Cusco 🇵🇪", "«¡Buenas! Soy Nina, de Perú.»", "reizen & natuur (U8)"),
        ("tu", "Tú", "Flandes 🇧🇪", "«Yo soy… — en jij?»", "de reiziger = JIJ"),
    ]
    x0, y0 = Inches(0.5), Inches(1.55); tw = Inches(2.42); th = Inches(4.3); gx = Inches(0.13)
    for i, (nm, naam, stad, quote, rol) in enumerate(people):
        x = x0 + i * (tw + gx)
        card(s, x, y0, tw, th, fill=WHITE, line=ACC[nm], lw=1.8)
        rect(s, x, y0, tw, Inches(0.14), fill=ACC[nm])
        avatar(s, nm, x + (tw - Inches(1.5)) / 2, y0 + Inches(0.35), Inches(1.5))
        text(s, x, y0 + Inches(1.95), tw, Inches(0.4),
             [[(naam, {"size": 18, "bold": True, "color": INK, "font": DISPLAY})]], align=PP_ALIGN.CENTER)
        text(s, x, y0 + Inches(2.35), tw, Inches(0.3),
             [[(stad, {"size": 11, "bold": True, "color": ACC[nm]})]], align=PP_ALIGN.CENTER)
        # quote-bubbel
        qb = rect(s, x + Inches(0.15), y0 + Inches(2.75), tw - Inches(0.3), Inches(0.9),
                  fill=GT, line=None, round=True, radius=0.1)
        tf=qb.text_frame; tf.word_wrap=True; tf.vertical_anchor=MSO_ANCHOR.MIDDLE
        tf.margin_left=tf.margin_right=Pt(6)
        p=tf.paragraphs[0]; p.alignment=PP_ALIGN.CENTER
        rr=p.add_run(); rr.text=quote; rr.font.size=Pt(11); rr.font.italic=True; rr.font.bold=True; rr.font.name=BODY; rr.font.color.rgb=GD
        text(s, x + Inches(0.12), y0 + Inches(3.75), tw - Inches(0.24), Inches(0.5),
             [[(rol, {"size": 9.5, "color": MUT})]], align=PP_ALIGN.CENTER, line=1.05)
    text(s, Inches(0.5), Inches(6.0), Inches(12.3), Inches(0.4),
         [[("🎒 ", {"size": 13}), ("La mochila viajera", {"size": 12.5, "bold": True, "color": GD, "font": DISPLAY}),
           ("  = reisgezel. Klasritueel: ", {"size": 12, "color": INK}),
           ("¿Cómo se llama nuestra mochila?", {"size": 12, "bold": True, "italic": True, "color": G}),
           ("  (de klas kiest de naam — meteen een mini-taak).", {"size": 12, "color": INK})]])
    text(s, Inches(0.5), Inches(6.5), Inches(12.3), Inches(0.4),
         [[("Teaser C6: ", {"size": 10.5, "italic": True, "color": MUT}),
           ("Mateo, de Buenos Aires 🇦🇷", {"size": 10.5, "bold": True, "italic": True, "color": MUT}),
           (" komt er pas in het 6de bij (voseo). Niet productief in C5.", {"size": 10.5, "italic": True, "color": MUT})]])
    footer(s, page=pg())
    notes(s, "TEACHER · Audiopaneel personages (idee 34). Klik-per-avatar speelt in HTML de chunk af; hier klassikaal voorlezen. "
             "Laat elke leerling één castlid 'nadoen' (soy … de …). Kies NU samen de naam van de mochila (schrijf op bord). "
             "Differentiatie: sterke leerlingen voegen '¿y tú?' toe. Cross-ref: HTML flip-cards cast · PDF opener A.1.3.")

# ============================================================================
# DIA 4 · §1 opener + VOCABULARY — el abecedario (27 letras)
# ============================================================================
def s04_alfabeto():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · SONAR EN ESPAÑOL", "El abecedario — las 27 letras",
               "Spaans lees je zoals je het schrijft. Eén keer de klankregels → daarna lees je bijna elk woord correct hardop.", num=1)
    # leerdoel-strip
    text(s, Inches(0.5), Inches(1.4), Inches(12.3), Inches(0.35),
         [[("Doel: ", {"size": 11, "bold": True, "color": GD}),
           ("de klanken & letters herkennen · je naam kunnen spellen (deletrear).  ", {"size": 11, "color": INK}),
           ("[LPD · Taalsysteem — klank–schriftbeeld A1]", {"size": 9.5, "italic": True, "color": MUT})]])
    # letterraster
    letters = [("A","a"),("B","be"),("C","ce"),("D","de"),("E","e"),("F","efe"),("G","ge"),
               ("H","hache"),("I","i"),("J","jota"),("K","ka"),("L","ele"),("M","eme"),("N","ene"),
               ("Ñ","eñe"),("O","o"),("P","pe"),("Q","cu"),("R","erre"),("S","ese"),("T","te"),
               ("U","u"),("V","uve"),("W","uve doble"),("X","equis"),("Y","ye"),("Z","zeta")]
    trampas = {"H","J","Ñ","R","V","Z","G"}  # klanktrampas
    cols = 9
    x0, y0 = Inches(0.5), Inches(1.85); cw = Inches(1.33); ch = Inches(0.82); gx=Inches(0.05); gy=Inches(0.08)
    for i,(L,naam) in enumerate(letters):
        r,c = divmod(i, cols)
        x = x0 + c*(cw+gx); y = y0 + r*(ch+gy)
        istr = L in trampas
        card(s, x, y, cw, ch, fill=(RGBColor(0xFD,0xEC,0xEC) if istr else WHITE),
             line=(RED if istr else LINE), lw=(1.5 if istr else 1.0), shadow=False)
        text(s, x, y + Inches(0.03), cw, Inches(0.45),
             [[(L, {"size": 21, "bold": True, "color": (RED if istr else GD), "font": DISPLAY})]],
             align=PP_ALIGN.CENTER)
        text(s, x, y + Inches(0.48), cw, Inches(0.3),
             [[(naam, {"size": 9.5, "color": MUT})]], align=PP_ALIGN.CENTER)
    # legenda + regel
    y = Inches(5.05)
    rect(s, Inches(0.5), y, Inches(0.32), Inches(0.32), fill=RGBColor(0xFD,0xEC,0xEC), line=RED, lw=1.4, round=True, radius=0.2)
    text(s, Inches(0.9), y - Inches(0.02), Inches(6), Inches(0.35),
         [[("= klanktrampa (klinkt anders dan in het NL) → dia 5", {"size": 11, "color": INK})]])
    solucion(s, Inches(0.5), Inches(5.55), Inches(12.33), Inches(0.95),
             [[("Regla · ", {"bold": True, "color": GD}), ("27 letras", {"bold": True, "color": G}),
               (" = 26 van het NL ", {"color": GD}), ("+ ñ", {"bold": True, "color": G}),
               (". ", {"color": GD}), ("ch / ll", {"bold": True, "color": G}),
               (" = dígrafos (klankcombinaties), géén aparte letters meer. ", {"color": GD}),
               ("De letternaam verraadt soms de klank: ", {"color": GD}),
               ("«jota», «ge», «zeta».", {"italic": True, "bold": True, "color": G})],
              [("¿Welke letter zie je niet in het NL? → ", {"color": GD}), ("ñ", {"bold": True, "color": G}),
               ("  ·  ¿Welke hoor je nooit? → ", {"color": GD}), ("h", {"bold": True, "color": G})]],
             title="OBSERVAR + REGLA · docent")
    footer(s, page=pg())
    notes(s, "TEACHER · VOCABULARY (idee 21 woordmuur · idee 22 beeld-woord-audio). Fase: context→observeren→regel. "
             "Speel eerst 'la canción del abecedario' (audio) — luister, nog niet schrijven. Rode vakjes = klanktrampas (dia 5). "
             "Observatievragen (en parejas, NL): welke letternaam verrast? welke letter zie je niet in NL (ñ)? welke hoor je nooit (h)? "
             "Actividad: 'Deletrea tu nombre' — modelo 'Me llamo Lucía: ele-u-ce-i-a, con tilde en la i'. "
             "Cross-ref: HTML flip-cards alfabet · PDF §1.1.")

# ============================================================================
# DIA 5 · §1 GRAMMAR/PRONUNCIATION — klanktrampas
# ============================================================================
def s05_trampas():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · TRAMPAS PARA NEERLANDESES", "Los sonidos que cambian",
               "Een handvol letters doet iets anders dan je gewend bent. Vorm + label + icoon dragen de info (geen kleur alleen).")
    fams = [
        ("La jota /x/", "j · ge · gi", "hard, achter in de keel — als «ch» in lachen, acht, Bach", "Juan · jamón · gente · Gijón", "🔴 niet de NL-j! Juan = «Choean»"),
        ("ll / y /ʝ/", "ll · y", "als «j» in ja, jong (yeísmo)", "calle · paella · yo · playa", "🔴 paella = «pa-e-JA», geen l-l"),
        ("ñ /ɲ/", "ñ", "als «nj» in oranje, Anja", "España · niño · año", "🔴 año ≠ ano — het streepje telt!"),
        ("b = v /b/", "b · v", "b én v klinken exact gelijk (/b/)", "Bélgica · vino · Sevilla · vivir", "🔴 vivir = «bi-bir»"),
        ("h muda", "h", "de h zwijgt altijd — doe alsof ze er niet staat", "hola · hora · ahora · hay", "🔴 hola = «ola» (ch = wél eigen klank)"),
        ("qu / z /k/ /θ/", "qu · z · ce · ci", "qu = «k» (u zwijgt) · z/ce/ci = «th» (España)", "queso · aquí · zapato · gracias", "🔴 aquí = «a-kie», gracias met «th»"),
    ]
    x0, y0 = Inches(0.4), Inches(1.4); tw=Inches(4.13); th=Inches(1.72); gx=Inches(0.09); gy=Inches(0.12)
    for i,(titel, letters, uitleg, ejem, val) in enumerate(fams):
        r,c = divmod(i, 3)
        x = x0 + c*(tw+gx); y = y0 + r*(th+gy)
        card(s, x, y, tw, th, fill=WHITE, line=G, lw=1.4)
        rect(s, x, y, Inches(0.12), th, fill=G)
        text(s, x + Inches(0.2), y + Inches(0.06), tw - Inches(0.3), Inches(0.35),
             [[(titel, {"size": 14, "bold": True, "color": GD, "font": DISPLAY}),
               ("   " + letters, {"size": 11.5, "bold": True, "color": G})]])
        text(s, x + Inches(0.2), y + Inches(0.45), tw - Inches(0.3), Inches(0.5),
             [[(uitleg, {"size": 10.5, "color": INK})]], line=1.04)
        text(s, x + Inches(0.2), y + Inches(0.95), tw - Inches(0.3), Inches(0.32),
             [[("Ej.: ", {"size": 10.5, "bold": True, "color": MUT}),
               (ejem, {"size": 10.5, "italic": True, "color": INK})]])
        text(s, x + Inches(0.2), y + Inches(1.27), tw - Inches(0.3), Inches(0.4),
             [[(val, {"size": 10, "bold": True, "color": RED})]], line=1.02)
    footer(s, page=pg())
    notes(s, "TEACHER · Uitspraak in 6 families (PronunciationCard). Route: 'Caza de sonidos' — beluister het intro-tekstje "
             "en onderstreep de jota (Jorge, Gijón, colegio, gente, jamón). Betekenis eerst (waar komt Jorge vandaan?). "
             "Escucha y repite met opname (ListenRepeatRecorder). Sombrero-brug: het golfje op ñ + puntjes op güe/güi horen bij §2. "
             "De klanktrampa-quiz staat op de volgende dia.")

# ============================================================================
# DIA 6 · §1 QUIZ — ¿B o V? / r-rr (meerkeuze + oplossing zichtbaar)
# ============================================================================
def s06_quiz1():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · QUIZ · ESCUCHA Y DECIDE", "¿Qué oyes? — klankdiscriminatie",
               "Je hoort één woord; kruis aan wat je hoort. Daarna spreek je beide vormen zelf in. (idee 38: uitspraakcontrast)")
    # kolom links: b/v & h
    text(s, Inches(0.5), Inches(1.45), Inches(6), Inches(0.35),
         [[("A · ¿B o V? ¿H o sin H?", {"size": 14, "bold": True, "color": GD, "font": DISPLAY})]])
    # correct = wat je hoort (bij vaca/baca en hola/ola klinken beide gelijk → b=v, h muda)
    itemsA = [("1", "vaca", "baca", 0), ("2", "gente", "tente", 0), ("3", "casa", "caza", 0), ("4", "hola", "ola", 0)]
    y = Inches(1.85)
    for n, a, b, corr in itemsA:
        card(s, Inches(0.5), y, Inches(6.0), Inches(0.62), fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, Inches(0.62), y, Inches(0.4), Inches(0.62), [[(n, {"size": 13, "bold": True, "color": G})]], anchor=MSO_ANCHOR.MIDDLE)
        opt_a = text(s, Inches(1.05), y, Inches(2.5), Inches(0.62), [[("☐  " + a, {"size": 13, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, Inches(3.7), y, Inches(2.5), Inches(0.62), [[("☐  " + b, {"size": 13, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        # klik op de correcte optie → «✓» springt in (antwoord verschijnt)
        check_badge(s, Inches(2.55), y + Inches(0.13), opt_a, label="✓", w=Inches(0.36))
        y = y + Inches(0.72)
    # kolom rechts: r/rr minimale paren
    text(s, Inches(6.9), Inches(1.45), Inches(6), Inches(0.35),
         [[("B · ¿", {"size": 14, "bold": True, "color": GD, "font": DISPLAY}),
           ("pero", {"size": 14, "bold": True, "color": GD, "font": DISPLAY}),
           (" o ", {"size": 14, "bold": True, "color": GD, "font": DISPLAY}),
           ("perro", {"size": 14, "bold": True, "color": GD, "font": DISPLAY}),
           ("? — één tik ↔ rol", {"size": 14, "bold": True, "color": GD, "font": DISPLAY})]])
    pairs = [("pero", "perro", "maar / hond 🐶"), ("caro", "carro", "duur / kar 🚗"),
             ("coro", "corro", "koor / ik ren 🏃"), ("pera", "perra", "peer / teef 🍐")]
    y = Inches(1.85)
    for a, b, gl in pairs:
        card(s, Inches(6.9), y, Inches(5.9), Inches(0.62), fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, Inches(7.02), y, Inches(2.0), Inches(0.62), [[(a, {"size": 13, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, Inches(8.7), y, Inches(2.0), Inches(0.62), [[(b, {"size": 13, "bold": True, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, Inches(10.5), y, Inches(2.2), Inches(0.62), [[(gl, {"size": 10.5, "italic": True, "color": MUT})]], anchor=MSO_ANCHOR.MIDDLE)
        y = y + Inches(0.72)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.85), Inches(12.3), Inches(1.05),
             [[("A · «geen fout, dat is Spaans!»  ", {"bold": True, "color": GD}),
               ("vaca=baca en hola=ola klinken IDENTIEK", {"color": GD}),
               (" (b=v, h muda). ", {"color": GD}),
               ("gente≠tente (jota-klank), casa≠caza (s ↔ th).", {"color": GD})],
              [("B · r/rr:  ", {"bold": True, "color": GD}),
               ("één tik", {"bold": True, "color": G}), (" tussen klinkers (pero) ↔ ", {"color": GD}),
               ("rol", {"bold": True, "color": G}), (" bij rr, woordbegin en na n/l/s (perro, Roma, Enrique). Betekenis verandert!", {"color": GD})]],
             trigger=btn, title_doc="SOLUCIÓN + uitleg · docent")
    footer(s, page=pg())
    notes(s, "TEACHER · QUIZ (idee 12 meerkeuze met feedback · idee 38 uitspraakcontrast). "
             "Onthul-flow: laat de klas eerst kiezen (klik audio), DAN de solución tonen. Belangrijk: b=v en h muda "
             "maken sommige paren identiek — dat is geen valstrik-fout maar Spaans. Na kiezen: elke leerling spreekt "
             "BEIDE vormen zelf in (van receptie → productie). Trabalenguas als extra: 'Rápido corre el carro del ferrocarril'.")

# ============================================================================
# DIA 7 · §2 opener/GRAMMAR — la sílaba tónica (noticing)
# ============================================================================
def s07_tonica():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · TALLER DE LENGUA", "El acento — «la regla del sombrero»",
               "Welke lettergreep zeg je harder (sílaba tónica)? En wanneer schrijf je een hoedje (´)?", num=2)
    text(s, Inches(0.5), Inches(1.4), Inches(12.3), Inches(0.35),
         [[("① Observeren — luister & klap 👏.  ", {"size": 12, "bold": True, "color": GD}),
           ("Elk woord heeft één 'sterke' lettergreep. Klap ze aan.", {"size": 12, "color": INK})]])
    # lettergreep-treintjes
    woorden = [("café", ["ca","FÉ"], "laatste"), ("casa", ["CA","sa"], "voorlaatste"),
               ("México", ["MÉ","xi","co"], "3e van achteren"), ("teléfono", ["te","LÉ","fo","no"], "3e van achteren"),
               ("Perú", ["pe","RÚ"], "laatste"), ("número", ["NÚ","me","ro"], "3e van achteren")]
    x0, y0 = Inches(0.5), Inches(1.9); rowh = Inches(0.72)
    for i,(w, sil, plek) in enumerate(woorden):
        r,c = divmod(i, 2)
        x = x0 + c*Inches(6.25); y = y0 + r*rowh
        text(s, x, y, Inches(1.5), rowh, [[(w, {"size": 15, "bold": True, "color": INK, "font": DISPLAY})]], anchor=MSO_ANCHOR.MIDDLE)
        wx = x + Inches(1.5)
        for syl in sil:
            strong = syl.isupper()
            bw = Inches(0.55 + 0.14*len(syl))
            b = rect(s, wx, y + (Inches(0.06) if strong else Inches(0.14)), bw,
                     (Inches(0.5) if strong else Inches(0.34)),
                     fill=(G if strong else GT), line=(GD if strong else None), lw=1.2, round=True, radius=0.25)
            tf=b.text_frame; tf.vertical_anchor=MSO_ANCHOR.MIDDLE; tf.margin_top=tf.margin_bottom=Pt(0)
            p=tf.paragraphs[0]; p.alignment=PP_ALIGN.CENTER
            rr=p.add_run(); rr.text=syl.lower() if not strong else syl
            rr.font.size=Pt(12 if strong else 10.5); rr.font.bold=strong; rr.font.name=BODY
            rr.font.color.rgb=(WHITE if strong else GD)
            if strong:
                text(s, wx, y - Inches(0.12), bw, Inches(0.25), [[("🎩", {"size": 11})]], align=PP_ALIGN.CENTER)
            wx = wx + bw + Inches(0.06)
        text(s, x + Inches(4.4), y, Inches(1.7), rowh, [[("(" + plek + ")", {"size": 10, "italic": True, "color": MUT})]], anchor=MSO_ANCHOR.MIDDLE)
    solucion(s, Inches(0.5), Inches(4.55), Inches(12.3), Inches(1.35),
             [[("Regla 1 · ", {"bold": True, "color": GD}),
               ("Elk woord heeft ", {"color": GD}), ("één sílaba tónica", {"bold": True, "color": G}),
               (" — die ", {"color": GD}), ("hoor", {"bold": True, "color": G}),
               (" je altijd; het streepje (´) ", {"color": GD}), ("schrijf", {"bold": True, "color": G}),
               (" je maar soms.", {"color": GD})],
              [("🔴 Kernvalstrik: ", {"bold": True, "color": RED}),
               ("klemtoon ≠ tilde", {"bold": True, "color": RED}),
               (".  Bij casa hoor je de klap op 'ca', maar er staat géén hoedje.", {"color": GD})],
              [("🔴 NL-valstrik: ", {"bold": True, "color": RED}),
               ("leg je Nederlandse klemtoon af — «pe-RÚ» (niet PE-ru), «es-pa-ÑOL» (niet ES-panjol).", {"color": GD})]],
             title="OBSERVAR → REGLA · docent")
    footer(s, page=pg())
    notes(s, "TEACHER · GRAMMAR-noticing (idee 27 Morph kan het hoedje visueel laten 'landen'). "
             "Fase: context→observeren→regel, NOG geen tilde-regel. Laat de klas hardop lezen en klappen (Escucha y da una palmada, 8 woorden). "
             "Truc: tel van achteren — última(1)·penúltima(2)·antepenúltima(3), heb je nodig op dia 8. "
             "Sombrero-familie: golfje ~ (ñ) en puntjes ¨ (güe) zijn ándere hoedjes dan de tilde ´.")

# ============================================================================
# DIA 8 · §2 GRAMMAR — tres familias + regla del sombrero + beslisboom
# ============================================================================
def s08_sombrero():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · LA REGLA DEL SOMBRERO", "Tres familias · ¿cuándo la tilde?",
               "Drie families naar de plaats van de klap — en dé regel voor het hoedje: de magische eindletters -n, -s, klinker.")
    fams = [("agudas", "laatste lettergreep", "ca-fé · Pe-rú · es-pa-ñol · Ma-drid · ja-món", ACC["lucia"]),
            ("llanas", "voorlaatste (de gewoonste!)", "ca-sa · lu-nes · a-mi-go · ár-bol", G),
            ("esdrújulas", "derde van achteren", "Mé-xi-co · te-lé-fo-no · mú-si-ca", ACC["tu"])]
    x0, y0 = Inches(0.5), Inches(1.4); tw=Inches(4.0); gx=Inches(0.16)
    for i,(nm, plek, ej, col) in enumerate(fams):
        x = x0 + i*(tw+gx)
        card(s, x, y0, tw, Inches(1.75), fill=WHITE, line=col, lw=1.6)
        rect(s, x, y0, tw, Inches(0.46), fill=col)
        text(s, x, y0 + Inches(0.02), tw, Inches(0.42), [[(nm, {"size": 16, "bold": True, "color": WHITE, "font": DISPLAY})]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(0.15), y0 + Inches(0.54), tw - Inches(0.3), Inches(0.35),
             [[("klap op de ", {"size": 11, "color": INK}), (plek, {"size": 11, "bold": True, "color": col})]], align=PP_ALIGN.CENTER)
        text(s, x + Inches(0.15), y0 + Inches(0.95), tw - Inches(0.3), Inches(0.7),
             [[(ej, {"size": 11, "italic": True, "color": INK})]], align=PP_ALIGN.CENTER, line=1.14)
    # de regel-tabel
    solucion(s, Inches(0.5), Inches(3.55), Inches(7.4), Inches(2.55),
             [[("REGLA DEL SOMBRERO 🎩", {"bold": True, "size": 14, "color": G})],
              [("• Esdrújula → ", {"bold": True, "color": GD}), ("SIEMPRE ´", {"bold": True, "color": G}),
               ("  (México, teléfono, música)", {"italic": True, "color": GD})],
              [("• Aguda → ´ als ze eindigt op ", {"bold": True, "color": GD}), ("-n, -s of klinker", {"bold": True, "color": G})],
              [("     wél: café, Perú, jamón, adiós  ·  niet: Madrid, español, reloj", {"italic": True, "color": GD, "size": 11})],
              [("• Llana → ´ als ze NÍET zo eindigt", {"bold": True, "color": GD})],
              [("     wél: árbol, lápiz, Cádiz  ·  niet: casa, lunes, examen", {"italic": True, "color": GD, "size": 11})],
              [("• Monosílabo (1 lettergreep) → géén ´ (sol, pan, tres)", {"bold": True, "color": GD})]],
             title="REGLA · de kern")
    # spiegel-truc + beslisboom
    card(s, Inches(8.1), Inches(3.55), Inches(4.72), Inches(2.55), fill=CREMA, line=AMBER, lw=1.4)
    text(s, Inches(8.3), Inches(3.65), Inches(4.4), Inches(0.6),
         [[("🟡 Spiegel-truc", {"size": 13, "bold": True, "color": AMBER, "font": DISPLAY})]])
    text(s, Inches(8.3), Inches(4.1), Inches(4.4), Inches(0.9),
         [[("Dezelfde 3 eindletters (-n · -s · klinker) doen bij ", {"size": 11, "color": INK}),
           ("agudas", {"size": 11, "bold": True, "color": ACC["lucia"]}),
           (" het hoedje verschijnen en bij ", {"size": 11, "color": INK}),
           ("llanas", {"size": 11, "bold": True, "color": G}),
           (" verdwijnen.", {"size": 11, "color": INK})]], line=1.12)
    text(s, Inches(8.3), Inches(5.1), Inches(4.4), Inches(0.95),
         [[("Beslisboom: ", {"size": 11, "bold": True, "color": GD}),
           ("¿Esdrújula? ", {"size": 11, "color": INK}), ("→ sí: ´", {"size": 11, "bold": True, "color": G})],
          [("¿No? → ¿termina en -n/-s/vocal?", {"size": 11, "color": INK})],
          [("aguda: sí→´  ·  llana: no→´", {"size": 11, "italic": True, "color": MUT})]], line=1.1)
    footer(s, page=pg())
    notes(s, "TEACHER · GRAMMAR (idee 29 beslisboom · idee 27 Morph). Laat de klas eerst sorteren (Ordena por familia) "
             "vóór je de regel-tabel toont. Ezelsbrug: a-GU-das is zelf een llana maar 'wijst naar het einde'; es-DRÚ-ju-las "
             "doet wat de naam zegt. Grootste A1-fout = TE VEEL tildes zetten. Recycling-teaser: joven→jóvenes / canción→canciones "
             "(hoedje verspringt) komt pas later. Cross-ref: HTML klikbare beslisboom (StressTapper).")

# ============================================================================
# DIA 9 · §2 QUIZ — ¿Lleva sombrero? (met oplossing)
# ============================================================================
def s09_quiz2():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · QUIZ · COLOCA LA TILDE", "¿Lleva sombrero o no?",
               "Zet de tilde ALLEEN waar het moet — en enkel op de tónica-klinker. Beslis eerst, onthul dan.")
    # (weergave, correcte vorm, krijgt-tilde?)
    palabras = [("Peru", "Perú", True), ("cafe", "café", True), ("casa", "casa", False),
                ("arbol", "árbol", True), ("Mexico", "México", True), ("numero", "número", True),
                ("lunes", "lunes", False), ("adios", "adiós", True)]
    x0, y0 = Inches(0.5), Inches(1.55); cw=Inches(2.9); ch=Inches(0.95); gx=Inches(0.18); gy=Inches(0.2)
    for i,(w, corr, tilde) in enumerate(palabras):
        r,c = divmod(i, 4)
        x = x0 + c*(cw+gx); y = y0 + r*(ch+gy)
        cardshp = card(s, x, y, cw, ch, fill=WHITE, line=LINE, lw=1.2)
        text(s, x, y + Inches(0.08), cw, Inches(0.45), [[(w, {"size": 20, "bold": True, "color": INK, "font": DISPLAY})]], align=PP_ALIGN.CENTER)
        text(s, x, y + Inches(0.55), cw, Inches(0.35),
             [[("☐ con ´    ☐ sin ´", {"size": 11.5, "color": MUT})]], align=PP_ALIGN.CENTER)
        # klik op de kaart → correcte vorm springt in (con of sin sombrero)
        lab = corr if tilde else corr + " · sin ´"
        check_badge(s, x + cw/2 - Inches(0.9), y + Inches(0.63), cardshp, label=lab, w=Inches(1.8))
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.35), Inches(12.3), Inches(1.55),
             [[("Perú", {"bold": True, "color": G}), (" (aguda -ú) · ", {"color": GD}),
               ("café", {"bold": True, "color": G}), (" (aguda -é) · ", {"color": GD}),
               ("casa", {"bold": True, "color": G}), (" → GEEN (llana -a) · ", {"color": GD}),
               ("árbol", {"bold": True, "color": G}), (" (llana -l → wél) · ", {"color": GD}),
               ("México", {"bold": True, "color": G}), (" (esdrújula → altijd)", {"color": GD})],
              [("número", {"bold": True, "color": G}), (" (esdrújula) · ", {"color": GD}),
               ("lunes", {"bold": True, "color": G}), (" → GEEN (llana -s) · ", {"color": GD}),
               ("adiós", {"bold": True, "color": G}), (" (aguda -s → wél)", {"color": GD})],
              [("🔴 Ojo — geen hoedjes strooien! ", {"bold": True, "color": RED}),
               ("lunes en profesor krijgen er GÉÉN. De grootste A1-fout is te veel tildes zetten.", {"color": GD})]],
             trigger=btn, title_doc="SOLUCIÓN + uitleg · docent")
    footer(s, page=pg())
    notes(s, "TEACHER · QUIZ (idee 11 klik-om-te-onthullen · idee 14 zoek de fout). Laat elke leerling eerst zelf beslissen + "
             "de regel benoemen ('waarom?'), dan solución. Vervolg: 'Clínica de tildes' (foutenkliniek): ✗cásada→casa, ✗Mexico→México, "
             "✗telefóno→teléfono, ✗árból→árbol. Het CORRECTE model komt altijd als laatste, nooit de fout alleen (§14). "
             "Communicatief slot: 'Sube el sombrero al mapa' met paradas (Perú, México, Bogotá, Panamá dragen ´).")

# ============================================================================
# DIA 10 · §3 opener/VOCABULARY — números 0-100 (drie lagen)
# ============================================================================
def s10_numeros():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · VOCABULARIO", "Números 0–100 — en tres capas",
               "Geen kale lijst: drie bouwlagen, elk met één truc. Voor je leeftijd (edad) en je telefoonnummer.", num=3)
    # laag 1
    def numrow(x, y, w, title, trick, cells, tint):
        card(s, x, y, w, Inches(1.55), fill=WHITE, line=G, lw=1.4)
        rect(s, x, y, w, Inches(0.42), fill=tint)
        text(s, x + Inches(0.15), y + Inches(0.02), w - Inches(0.3), Inches(0.4),
             [[(title, {"size": 12.5, "bold": True, "color": WHITE, "font": DISPLAY}),
               ("   " + trick, {"size": 10.5, "italic": True, "color": GT})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(0.18), y + Inches(0.52), w - Inches(0.36), Inches(0.95),
             [[(cells, {"size": 12, "color": INK})]], line=1.25)
    numrow(Inches(0.5), Inches(1.45), Inches(12.33), "Laag 1 · los cimientos (0–15)", "apart leren",
           "0 cero · 1 uno · 2 dos · 3 tres · 4 cuatro · 5 cinco · 6 seis · 7 siete · 8 ocho · 9 nueve · 10 diez · 11 once · 12 doce · 13 trece · 14 catorce · 15 quince", G)
    numrow(Inches(0.5), Inches(3.15), Inches(12.33), "Laag 2 · «todo junto» (16–29)", "één woord, geen «y» · let op 4 hoedjes",
           "16 dieciséis · 17 diecisiete · 18 dieciocho · 19 diecinueve · 20 veinte · 21 veintiuno · 22 veintidós · 23 veintitrés · 24 veinticuatro · 25 veinticinco · 26 veintiséis · 27 veintisiete · 28 veintiocho · 29 veintinueve", GD)
    # laag 3 + machine
    card(s, Inches(0.5), Inches(4.85), Inches(7.8), Inches(1.55), fill=WHITE, line=G, lw=1.4)
    rect(s, Inches(0.5), Inches(4.85), Inches(7.8), Inches(0.42), fill=G)
    text(s, Inches(0.65), Inches(4.87), Inches(7.5), Inches(0.4),
         [[("Laag 3 · las decenas + «y» (30–100)", {"size": 12.5, "bold": True, "color": WHITE, "font": DISPLAY}),
           ("   drie stukjes", {"size": 10.5, "italic": True, "color": GT})]], anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.68), Inches(5.35), Inches(7.5), Inches(1.0),
         [[("30 treinta · 40 cuarenta · 50 cincuenta · 60 sesenta · 70 setenta · 80 ochenta · 90 noventa · 100 cien", {"size": 12, "color": INK})]], line=1.25)
    # machine-box
    card(s, Inches(8.5), Inches(4.85), Inches(4.33), Inches(1.55), fill=CREMA, line=AMBER, lw=1.4)
    text(s, Inches(8.68), Inches(4.95), Inches(4.0), Inches(0.35),
         [[("⚙ La máquina «y»", {"size": 12, "bold": True, "color": AMBER, "font": DISPLAY})]])
    text(s, Inches(8.68), Inches(5.35), Inches(4.0), Inches(1.0),
         [[("[ decena ] + ", {"size": 12, "color": F_SUBJ, "bold": True}),
           ("y", {"size": 13, "bold": True, "color": F_VERB}),
           (" + [ unidad ]", {"size": 12, "bold": True, "color": F_OBJ})],
          [("treinta ", {"size": 12, "color": F_SUBJ}), ("y", {"size": 12, "bold": True, "color": F_VERB}),
           (" cinco → ", {"size": 12, "color": F_OBJ}), ("35", {"size": 12, "bold": True, "color": INK})],
          [("noventa ", {"size": 12, "color": F_SUBJ}), ("y", {"size": 12, "bold": True, "color": F_VERB}),
           (" nueve → ", {"size": 12, "color": F_OBJ}), ("99", {"size": 12, "bold": True, "color": INK})]], line=1.15)
    footer(s, page=pg())
    notes(s, "TEACHER · VOCABULARY (idee 21/22 · idee 19 timer voor snelle oproep). Verborgen vertaling: hoor het getal vóór het "
             "NL-gloss verschijnt. Trucs per laag: los blokjes / aan elkaar / machine met 'y'. 4 hoedjes in laag 2: dieciSÉis, "
             "veintiDÓS, veintiTRÉS, veintiSÉis (sluit aan bij §2!). Speel 'Bingo del mundo hispano' (ronde 2 = leerling is spelleider). "
             "Volgende dia: valstrikken + oefening leeftijd/telefoon.")

# ============================================================================
# DIA 11 · §3 — valstrikken + tener años (grammatica functioneel)
# ============================================================================
def s11_edad():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · ¡OJO! + TU EDAD", "Valstrikken + «tener … años»",
               "De kernvalstrik van U0/U1: leeftijd = tener, niet ser. En de substitutietabel om je edad te zeggen.")
    # valstrikken links
    card(s, Inches(0.5), Inches(1.45), Inches(6.1), Inches(4.5), fill=RGBColor(0xFD,0xEC,0xEC), line=RED, lw=1.4)
    text(s, Inches(0.7), Inches(1.58), Inches(5.7), Inches(0.4),
         [[("🔴 Trampas para neerlandeses", {"size": 15, "bold": True, "color": RED, "font": DISPLAY})]])
    vals = [
        ("Leeftijd = tener, niet ser.", "Tengo 14 años ✔  ·  ~Soy 14 años~ ✘ (NL «ik ben 14»)"),
        ("«y» alleen bij 30–100.", "dieciséis (1 woord) ↔ treinta y seis (3 woorden)"),
        ("«y» klinkt als /i/.", "cuarenta y cinco = [koe-a-REN-ta i SIN-ko]"),
        ("Hoedjes niet vergeten.", "~veintidos~ → veintidós · ~dieciseis~ → dieciséis"),
        ("100 = cien.", "cien años, cien euros (niet ciento voor exact 100)"),
        ("Lastige paren.", "seis↔siete · nueve↔nuevo → extra luisteren"),
    ]
    y = Inches(2.05)
    for kop, uitleg in vals:
        text(s, Inches(0.7), y, Inches(5.75), Inches(0.62),
             [[("• " + kop + "  ", {"size": 11.5, "bold": True, "color": INK}),
               (uitleg, {"size": 10.5, "color": GD})]], line=1.05)
        y = y + Inches(0.63)
    # tener tabel rechts
    text(s, Inches(6.9), Inches(1.5), Inches(6), Inches(0.4),
         [[("Substitutietabel — ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("tener + número + años", {"size": 13, "bold": True, "color": F_VERB, "font": DISPLAY})]])
    # header
    heads = [("Persoon", F_SUBJ), ("tener", F_VERB), ("número + años", F_TIME)]
    x = Inches(6.9); colw = [Inches(1.9), Inches(1.5), Inches(2.5)]
    for (h, col), w in zip(heads, colw):
        b = rect(s, x, Inches(1.95), w, Inches(0.42), fill=col, round=False)
        text(s, x, Inches(1.95), w, Inches(0.42), [[(h, {"size": 11.5, "bold": True, "color": WHITE})]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        x = x + w
    rows = [("Yo", "tengo", "catorce años"), ("Tú", "tienes", "quince años"),
            ("Lucía", "tiene", "dieciséis años"), ("Mi hermano", "tiene", "veinte años")]
    y = Inches(2.37)
    for a, b, c in rows:
        x = Inches(6.9)
        for val, w, col in zip((a, b, c), colw, (F_SUBJ, F_VERB, F_TIME)):
            rect(s, x, y, w, Inches(0.44), fill=WHITE, line=LINE, lw=0.8)
            text(s, x, y, w, Inches(0.44), [[(val, {"size": 11.5, "color": col, "bold": (col==F_VERB)})]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
            x = x + w
        y = y + Inches(0.44)
    legend_func(s, Inches(6.9), Inches(4.3))
    solucion(s, Inches(6.9), Inches(4.7), Inches(5.9), Inches(1.25),
             [[("Vraag-antwoordspiegel:  ", {"bold": True, "color": GD}),
               ("¿Cuántos años tienes?", {"bold": True, "color": F_TIME}),
               (" → ", {"color": GD}), ("Tengo ___ años.", {"bold": True, "color": F_VERB})],
              [("🔴 Apocope: ", {"bold": True, "color": RED}),
               ("veintiún años, treinta y un años", {"bold": True, "color": G}),
               ("  (uno → un vóór «años»).", {"color": GD})]],
             title="MODELO · docent")
    footer(s, page=pg())
    notes(s, "TEACHER · GRAMMAR functioneel (idee 25 zinsbouwer · idee 30 grammaticakliniek). Context vóór vorm: we willen "
             "LEEFTIJDEN zeggen → daarvoor dient tener. Substitutietabel: kies één blok per kolom, spreek de zin hardop. "
             "Kernfout ser↔tener stevig inoefenen (keert terug in U1). Info-gap 'intercambio de teléfonos' (A/B): leerlingen "
             "moeten práten om elkaars nummer te weten. Communicatief slot §3: encuesta '¿Cuántos años tiene la clase?' + rapporteren in 3e p.")

# ============================================================================
# DIA 12 · §3 QUIZ/WRITING — escribe en letras (met oplossing)
# ============================================================================
def s12_quiz3():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · PRACTICA · ESCRIBE EN LETRAS", "Completa el número",
               "Let op: 16–29 = één woord · 30–100 = drie woorden met «y». Schrijf voluit.")
    items = [("18", "dieci______", "dieciocho"), ("24", "veinti______", "veinticuatro"),
             ("53", "cincuenta ___ ______", "cincuenta y tres"),
             ("71", "______ y ______", "setenta y uno"), ("96", "______ y ______", "noventa y seis"),
             ("47", "______ y ______", "cuarenta y siete")]
    x0, y0 = Inches(0.5), Inches(1.6); cw=Inches(3.95); ch=Inches(1.0); gx=Inches(0.2); gy=Inches(0.22)
    for i,(cij, gap, ans) in enumerate(items):
        r,c = divmod(i, 3)
        x = x0 + c*(cw+gx); y = y0 + r*(ch+gy)
        cardshp = card(s, x, y, cw, ch, fill=WHITE, line=LINE, lw=1.2)
        b = rect(s, x + Inches(0.12), y + Inches(0.22), Inches(0.7), Inches(0.55), fill=GT, round=True, radius=0.2)
        text(s, x + Inches(0.12), y + Inches(0.22), Inches(0.7), Inches(0.55), [[(cij, {"size": 20, "bold": True, "color": GD, "font": DISPLAY})]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(0.95), y, cw - Inches(1.05), ch, [[(gap, {"size": 15, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        # klik op de kaart → het voluit geschreven getal springt in
        check_badge(s, x + Inches(0.95), y + Inches(0.55), cardshp, label="✓ " + ans, w=cw - Inches(1.1))
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.6), Inches(12.3), Inches(1.3),
             [[("18 ", {"bold": True, "color": GD}), ("dieciocho", {"bold": True, "color": G}),
               ("  ·  24 ", {"bold": True, "color": GD}), ("veinticuatro", {"bold": True, "color": G}),
               ("  ·  53 ", {"bold": True, "color": GD}), ("cincuenta y tres", {"bold": True, "color": G})],
              [("71 ", {"bold": True, "color": GD}), ("setenta y uno", {"bold": True, "color": G}),
               ("  ·  96 ", {"bold": True, "color": GD}), ("noventa y seis", {"bold": True, "color": G}),
               ("  ·  47 ", {"bold": True, "color": GD}), ("cuarenta y siete", {"bold": True, "color": G})],
              [("Mini-transfer: ", {"bold": True, "color": GD}),
               ("schrijf jouw huisnummer en jouw schoenmaat voluit in letters.", {"italic": True, "color": GD})]],
             trigger=btn, title_doc="SOLUCIÓN · docent")
    footer(s, page=pg())
    notes(s, "TEACHER · WRITING (idee 42 schrijfopdracht · idee 36 microdictee). Leerling schrijft ECHT (antwoordruimte). "
             "16-29 aan elkaar (één woord), 30-100 met 'y' (drie woorden). Zelfcorrectie met de solución-laag. "
             "Uitbreiding dictee: 'Tengo dieciséis años', 'Vivo en el número veintidós', 'Somos treinta y tres en clase'. "
             "Getal in cijfers ÉN letters, mét juiste tilde (koppelt §3 + §2).")

# ============================================================================
# DIA 13 · §4 opener/SPEAKING — saludos y presentarse (chunks)
# ============================================================================
def s13_saludos():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · SALUDOS · SPEAKING", "Saludar y presentarse",
               "Kant-en-klare chunks: je leert ze als één geheel. Ze openen elke kennismaking op de reis.", num=4)
    # drie chunk-blokken
    def block(x, w, titel, tint, rows):
        card(s, x, Inches(1.45), w, Inches(4.5), fill=WHITE, line=tint, lw=1.5)
        rect(s, x, Inches(1.45), w, Inches(0.48), fill=tint)
        text(s, x + Inches(0.15), Inches(1.47), w - Inches(0.3), Inches(0.44),
             [[(titel, {"size": 13, "bold": True, "color": WHITE, "font": DISPLAY})]], anchor=MSO_ANCHOR.MIDDLE)
        y = Inches(2.05)
        for es, nl in rows:
            text(s, x + Inches(0.18), y, w - Inches(0.36), Inches(0.55),
                 [[(es, {"size": 12, "bold": True, "color": INK})],
                  [(nl, {"size": 10, "italic": True, "color": MUT})]], line=1.02)
            y = y + Inches(0.62)
    block(Inches(0.5), Inches(4.0), "🟠 Saludar / despedirse", F_VERB,
          [("¡Hola! · Buenos días", "Hallo! · Goedemorgen"),
           ("Buenas tardes / noches", "Goeimiddag / -avond"),
           ("¿Qué tal? · ¿Cómo estás?", "Hoe gaat het?"),
           ("(Muy) bien, gracias. ¿Y tú?", "(Heel) goed, dank je. En jij?"),
           ("Adiós · Hasta luego", "Dag · Tot straks"),
           ("Chao (informal)", "Doei (onder vrienden)")])
    block(Inches(4.65), Inches(4.0), "🔵 Presentarse", F_SUBJ,
          [("Me llamo … / Soy …", "Ik heet … / Ik ben …"),
           ("¿Cómo te llamas?", "Hoe heet jij?"),
           ("Encantado / Encantada", "Aangenaam (m / v)"),
           ("Mucho gusto · Igualmente", "Aangenaam · Insgelijks"),
           ("Este es… / Esta es…", "Dit is… (m / v)"),
           ("Soy de Bélgica.", "Ik kom uit België.")])
    block(Inches(8.8), Inches(4.0), "🟡 Lengua de clase", F_STRA,
          [("¿Cómo se dice … en español?", "Hoe zeg je … in het Spaans?"),
           ("¿Qué significa …?", "Wat betekent …?"),
           ("No entiendo.", "Ik begrijp het niet."),
           ("¿Puedes repetir, por favor?", "Kun je herhalen, a.u.b.?"),
           ("Más despacio, por favor.", "Trager, a.u.b."),
           ("¿Cómo se escribe?", "Hoe schrijf je dat?")])
    footer(s, page=pg())
    notes(s, "TEACHER · SPEAKING (idee 34 audiopaneel · idee 21 klikbare chunks). Chunks = één geheel, niet losse woorden. "
             "🔴 Valstrikken: Encantado (jongen) / Encantada (meisje) — volgt WIE spreekt. Buenos días/tardes/noches in MEERVOUD. "
             "Me llamo = wederkerend. ¿Qué tal? niet woord-voor-woord. h is stom. tú vs usted (usted enkel herkennen). "
             "Hang de klasposter 'Cartel de la clase' met de lengua de clase het hele jaar op (spreiding).")

# ============================================================================
# DIA 14 · §4 READING/SPEAKING — la dialoogkaart (Lucía ↔ Tú)
# ============================================================================
def s14_dialogo():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · DIÁLOGO · MODELO", "Presentarse en vivo",
               "Een kennismaking van begin tot eind. Route: saludar → presentarse → preguntar → reaccionar → despedirse.")
    lines = [
        ("lucia", "Lucía", "¡Hola! Buenos días. Me llamo Lucía. ¿Y tú, cómo te llamas?", "left"),
        ("tu", "Tú", "Hola, buenos días. Soy Tom. Soy de Bélgica.", "right"),
        ("lucia", "Lucía", "¡Encantada, Tom!", "left"),
        ("tu", "Tú", "Igualmente. ¿Qué tal?", "right"),
        ("lucia", "Lucía", "Muy bien, gracias. ¡Hasta luego!", "left"),
        ("tu", "Tú", "¡Adiós!", "right"),
    ]
    y = Inches(1.45)
    for nm, naam, txt, side in lines:
        if side == "left":
            avatar(s, nm, Inches(0.5), y, Inches(0.62))
            bx = Inches(1.25); bw = Inches(7.4)
        else:
            avatar(s, nm, Inches(12.2), y, Inches(0.62))
            bx = Inches(5.2); bw = Inches(6.9)
        bub = rect(s, bx, y, bw, Inches(0.72), fill=(GT if side=="left" else RGBColor(0xEA,0xEE,0xFC)),
                   line=(ACC[nm]), lw=1.2, round=True, radius=0.14)
        tf=bub.text_frame; tf.word_wrap=True; tf.vertical_anchor=MSO_ANCHOR.MIDDLE
        tf.margin_left=tf.margin_right=Pt(9)
        p=tf.paragraphs[0]; p.alignment=(PP_ALIGN.LEFT if side=="left" else PP_ALIGN.RIGHT)
        rn=p.add_run(); rn.text=naam+": "; rn.font.size=Pt(11); rn.font.bold=True; rn.font.name=BODY; rn.font.color.rgb=ACC[nm]
        rt=p.add_run(); rt.text=txt; rt.font.size=Pt(13); rt.font.name=BODY; rt.font.color.rgb=INK
        y = y + Inches(0.82)
    solucion(s, Inches(0.5), Inches(6.05), Inches(12.3), Inches(0.95),
             [[("Opmerken (betekenis vóór vorm): ", {"bold": True, "color": GD}),
               ("Lucía reageert op «Soy Tom» met ", {"color": GD}),
               ("«¡Encantada!»", {"bold": True, "color": G}),
               (". Tú antwoordt ", {"color": GD}), ("«Igualmente»", {"bold": True, "color": G}),
               (". Begin = saludo, einde = despedida (Hasta luego / Adiós).", {"color": GD})]],
             title="OBSERVAR · docent")
    footer(s, page=pg())
    notes(s, "TEACHER · READING→SPEAKING (idee 34 audiopaneel · idee 37 shadowing). Speel het model (2 stemmen). "
             "Shadowing in 4 stappen: volledige tekst → alleen sleutelwoorden → geen tekst → eigen variant "
             "('Me llamo [naam]. ¿Cómo te llamas?'). Opname → terugluisteren → 1 verbeterpunt → opnieuw (RecordReflectRetry). "
             "Substitutiecarrousel: naam · herkomst · leeftijd roteert. Cross-ref: HTML ShadowingPlayer.")

# ============================================================================
# DIA 15 · §4 lengua de clase — poster + ¿qué dices? (met oplossing)
# ============================================================================
def s15_lenguaclase():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · LENGUA DE CLASE", "¿Qué dices? — la reddingsboei",
               "Koppel elke situatie aan de juiste klastaal-chunk. Betekenis vóór vorm: kies je 'reddingsboei'.")
    banco = "Banco de frases:  ¿cómo se dice…?  ·  no entiendo  ·  ¿puedes repetir?  ·  más despacio  ·  ¿qué significa…?"
    chip(s, Inches(0.5), Inches(1.4), banco, fill=CREMA, tcolor=GD, size=11.5, w=Inches(11.0))
    sits = [
        ("De docent praat te snel.", "Más despacio, por favor."),
        ("Je kent een woord niet in het Spaans.", "¿Cómo se dice «…» en español?"),
        ("Je verstond de vraag niet.", "¿Puedes repetir, por favor?"),
        ("Je snapt de betekenis van «tarea» niet.", "¿Qué significa «tarea»?"),
    ]
    y = Inches(1.95)
    for i,(sit, sol) in enumerate(sits):
        cardshp = card(s, Inches(0.5), y, Inches(6.1), Inches(0.85), fill=WHITE, line=LINE, lw=1.1)
        b = rect(s, Inches(0.62), y + Inches(0.24), Inches(0.38), Inches(0.38), fill=G, round=True, radius=0.5)
        text(s, Inches(0.62), y + Inches(0.24), Inches(0.38), Inches(0.38), [[(str(i+1), {"size": 13, "bold": True, "color": WHITE})]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text(s, Inches(1.15), y, Inches(5.3), Inches(0.85), [[(sit, {"size": 12.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        # antwoordlijn + de chunk (= het antwoord)
        rect(s, Inches(6.75), y + Inches(0.5), Inches(6.05), Inches(0.02), fill=LINE)
        ans = text(s, Inches(6.75), y + Inches(0.02), Inches(6.0), Inches(0.4),
             [[("→ " + sol, {"size": 12.5, "bold": True, "color": G})]], anchor=MSO_ANCHOR.MIDDLE)
        # de juiste chunk (→) start verborgen en «springt in» bij de volgende klik
        register_reveal(s, ans)
        y = y + Inches(0.95)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.9), Inches(12.3), Inches(0.55),
             [[("Mini-rollenspel (geen steun): ", {"bold": True, "color": GD}),
               ("A speelt docent (praat te snel / zegt een nieuw woord); B reageert met de passende chunk. Wissel.", {"color": GD})]],
             trigger=btn, title_doc="COMUNICAR · docent")
    footer(s, page=pg())
    notes(s, "TEACHER · SPEAKING/interactie (idee 39 rollenkaart · idee 43 peerfeedback). De rechterkolom (→ chunk) is de "
             "oplossing: toon ze pas na de klaspoging. Klasposter 'Cartel de la clase' ophangen. Dit is compensatie-/strategie-taal "
             "(LPD lengua de clase) — laat leerlingen ze het hele jaar echt gebruiken i.p.v. NL. Encantad_ clínica del error kan hier ook: "
             "Diego zegt Encantado, Nina zegt Encantada (uitgang volgt wie spreekt).")

# ============================================================================
# DIA 16 · CULTURE — ¿Dónde se habla español?
# ============================================================================
def s16_cultura():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "CULTURA · IDENTIDAD EN DIVERSIDAD", "¿Dónde se habla español?",
               "Officiële taal in +20 landen. Je koppelt de reis aan de wereldkaart en aan de cast.", accent=GD)
    # 'kaart' als landenwolk
    card(s, Inches(0.5), Inches(1.45), Inches(7.7), Inches(4.5), fill=GT, line=G, lw=1.4)
    text(s, Inches(0.7), Inches(1.55), Inches(7.3), Inches(0.4),
         [[("🗺️ El mundo hispano — lengua oficial", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    paises = ["España","México","Guatemala","Honduras","El Salvador","Nicaragua","Costa Rica","Panamá",
              "Cuba","Rep. Dominicana","Puerto Rico","Colombia","Venezuela","Ecuador","Perú","Bolivia",
              "Paraguay","Uruguay","Argentina","Chile","Guinea Ecuatorial"]
    paradas = {"España","México","Colombia","Perú"}
    x0, y0 = Inches(0.72), Inches(2.0); cw=Inches(2.4); ch=Inches(0.42); gx=Inches(0.05); gy=Inches(0.06)
    for i,p in enumerate(paises):
        r,c = divmod(i, 3)
        x = x0 + c*(cw+gx); y = y0 + r*(ch+gy)
        ispar = p in paradas
        b = rect(s, x, y, cw, ch, fill=(G if ispar else WHITE), line=(GD if ispar else LINE), lw=1.0, round=True, radius=0.25)
        text(s, x, y, cw, ch, [[(("★ " if ispar else "") + p, {"size": 10.5, "bold": ispar, "color": (WHITE if ispar else INK)})]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.72), Inches(5.5), Inches(7.3), Inches(0.35),
         [[("★ = una parada de C5 (España · México · Colombia · Perú)  ·  🇺🇸 EE.UU. = millones de hispanohablantes", {"size": 9.5, "italic": True, "color": MUT})]])
    # weetjescapsules
    caps = [("~500 mln", "moedertaalsprekers"), ("+20 países", "lengua oficial"),
            ("2ª lengua", "materna del mundo"), ("español = castellano", "twee namen, één taal")]
    y = Inches(1.6)
    for groot, klein in caps:
        card(s, Inches(8.4), y, Inches(4.4), Inches(0.82), fill=WHITE, line=G, lw=1.3)
        text(s, Inches(8.6), y + Inches(0.06), Inches(4.0), Inches(0.42), [[(groot, {"size": 16, "bold": True, "color": G, "font": DISPLAY})]])
        text(s, Inches(8.6), y + Inches(0.46), Inches(4.0), Inches(0.3), [[(klein, {"size": 11, "color": MUT})]])
        y = y + Inches(0.92)
    card(s, Inches(8.4), Inches(5.3), Inches(4.4), Inches(0.65), fill=CREMA, line=AMBER, lw=1.3)
    text(s, Inches(8.55), Inches(5.36), Inches(4.15), Inches(0.6),
         [[("🟡 Cognados: ", {"size": 11, "bold": True, "color": AMBER}),
           ("hospital, animal, chocolate, familia, taxi… je herkent al véél Spaans!", {"size": 10.5, "color": INK})]], line=1.05)
    # LEER · comprensión lectora — expliciete leesvaardigheid (V/F con prueba) + reveal
    chip(s, Inches(0.5), Inches(6.08), "👀 LEER · comprensión lectora", fill=GT, tcolor=GD, size=10.5)
    text(s, Inches(0.5), Inches(6.5), Inches(8.0), Inches(0.5),
         [[("V/F · Lee la lista: «En Brasil se habla español.»  ", {"size": 11, "color": INK})]])
    rev = text(s, Inches(6.2), Inches(6.5), Inches(2.1), Inches(0.5),
         [[("→ FALSO (portugués)", {"size": 11, "bold": True, "color": RED})]], anchor=MSO_ANCHOR.MIDDLE)
    register_reveal(s, rev)
    chip(s, Inches(8.5), Inches(6.5), "🔗 Online: mapa clicable + flip cards", fill=CREMA, tcolor=GD, size=10)
    footer(s, page=pg())
    notes(s, "TEACHER · CULTURE (idee 2 klikbare kaart · idee 47 zoom). Component Identiteit in diversiteit (leerplan). "
             "Juist/fout met bewijs: 'In Brasil is español officieel?' (nee → portugués) · 'Perú está en Europa?' (nee). "
             "Coloca a la cast: Lucía→Sevilla, Diego→CDMX, Valen→Cartagena, Nina→Cusco. Strategie cognados. "
             "🔴 Spelling: landen mét hoofdletter (España), taal met kleine letter (el español). Volgende dia: variatie ES↔LatAm.")

# ============================================================================
# DIA 17 · CULTURE — variatie España vs Hispanoamérica
# ============================================================================
def s17_variatie():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "CULTURA · VARIACIÓN", "Mismo idioma, pequeñas diferencias",
               "Zelfde taal, kleine verschillen in woorden en klanken. Géén grammatica — enkel bewustwording (A1).", accent=GD)
    heads = ["🇪🇸 España", "🌎 Hispanoamérica", "🇳🇱 Nederlands"]
    rows = [("el coche","el carro","de auto"), ("el móvil","el celular","de gsm / mobiel"),
            ("el ordenador","la computadora","de computer"), ("el zumo","el jugo","het (vruchten)sap"),
            ("la patata","la papa","de aardappel"), ("vosotros","ustedes","jullie"),
            ("¡vale!","¡dale! / ¡listo!","oké!")]
    x0, y0 = Inches(0.5), Inches(1.5); colw = Inches(3.6); rh = Inches(0.5)
    # header
    for j,h in enumerate(heads):
        b = rect(s, x0 + j*colw, y0, colw, Inches(0.5), fill=(G if j<2 else CREMA), round=False)
        text(s, x0 + j*colw, y0, colw, Inches(0.5), [[(h, {"size": 13, "bold": True, "color": (WHITE if j<2 else GD)})]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    y = y0 + Inches(0.5)
    for i,(a,b,c) in enumerate(rows):
        fill = WHITE if i % 2 == 0 else GT
        for j,val in enumerate((a,b,c)):
            rect(s, x0 + j*colw, y, colw, rh, fill=fill, line=LINE, lw=0.6)
            text(s, x0 + j*colw + Inches(0.15), y, colw - Inches(0.2), rh,
                 [[(val, {"size": 12.5, "color": INK, "italic": (j==2)})]], anchor=MSO_ANCHOR.MIDDLE)
        y = y + rh
    # klank-weetje
    card(s, Inches(11.5), Inches(1.5), Inches(1.33), Inches(4.0), fill=CREMA, line=AMBER, lw=1.3)
    text(s, Inches(11.6), Inches(1.6), Inches(1.15), Inches(3.8),
         [[("🔊", {"size": 18})],
          [("seseo", {"size": 12, "bold": True, "color": AMBER})],
          [("c(e/i)/z", {"size": 10, "color": INK})],
          [("= /s/ in LatAm", {"size": 10, "color": INK})],
          [("= /θ/ «th»", {"size": 10, "color": INK})],
          [("in España.", {"size": 10, "color": INK})],
          [("Beide OK!", {"size": 10.5, "bold": True, "color": GD})]], line=1.2)
    solucion(s, Inches(0.5), Inches(5.6), Inches(10.7), Inches(0.85),
             [[("🔴 Valstrik (spelling): ", {"bold": True, "color": RED}),
               ("landen mét hoofdletter (España, México, Perú), maar de taal met kleine letter: ", {"color": GD}),
               ("el español", {"bold": True, "color": G}), (" (niet «el Español»).", {"color": GD})]],
             title="OJO · docent")
    footer(s, page=pg())
    notes(s, "TEACHER · CULTURE (idee 38 klankcontrast). Kernidee A1: dezelfde taal, kleine verschillen — bewustwording, geen toets. "
             "Woordparen matchen (met beginletter als cue): coche/carro, móvil/celular, patata/papa, zumo/jugo. "
             "Communicatief slot: mini-encuesta 'Yo prefiero «celular» porque suena bien' → verslag klas. "
             "Onze parada start in España → wij vertrekken van /θ/ (th), maar beide varianten zijn correct.")

# ============================================================================
# DIA 18 · FINAL_MISSION — Tarjeta de embarque
# ============================================================================
def s18_tarea():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "★ TAREA FINAL · EINDMISSIE", "Tu tarjeta de embarque",
               "Jouw instapkaart voor La Ruta. Alles komt samen: spellen · groeten · één klasvraag stellen.", accent=GD)
    # communicatief kader (afzender/ontvanger/doel...)
    kader = [("✈️ Situación", "Aan de gate stel je je kort voor voor de eerste etappe."),
             ("🗣️ Afzender", "jij (de reiziger)."),
             ("👥 Ontvanger", "een klasgenoot / de mochila / de klas."),
             ("🎯 Doel", "voorstellen + spellen · groeten · één klasvraag stellen."),
             ("🎁 Resultaat", "ingevulde tarjeta + korte gesproken kennismaking (live/opname).")]
    card(s, Inches(0.5), Inches(1.45), Inches(6.6), Inches(3.15), fill=WHITE, line=GD, lw=1.5)
    text(s, Inches(0.68), Inches(1.55), Inches(6.2), Inches(0.35),
         [[("Communicatief kader (§14)", {"size": 12.5, "bold": True, "color": GD, "font": DISPLAY})]])
    y = Inches(1.98)
    for lab, val in kader:
        text(s, Inches(0.68), y, Inches(2.05), Inches(0.5), [[(lab, {"size": 11.5, "bold": True, "color": G})]], anchor=MSO_ANCHOR.TOP)
        text(s, Inches(2.75), y, Inches(4.25), Inches(0.5), [[(val, {"size": 11, "color": INK})]], line=1.04)
        y = y + Inches(0.52)
    # mock-up tarjeta
    card(s, Inches(7.3), Inches(1.45), Inches(5.5), Inches(2.2), fill=GT, line=GD, lw=1.6)
    rect(s, Inches(7.3), Inches(1.45), Inches(5.5), Inches(0.5), fill=GD)
    text(s, Inches(7.45), Inches(1.47), Inches(5.2), Inches(0.46),
         [[("✈  TARJETA DE EMBARQUE · LA RUTA", {"size": 12.5, "bold": True, "color": WHITE, "font": DISPLAY})]], anchor=MSO_ANCHOR.MIDDLE)
    tarj = [("NOMBRE / NAAM", "___________"), ("DESTINO", "ESPAÑA"), ("RUTA", "EL MUNDO HISPANO"),
            ("PUERTA (gate)", "U0"), ("ASIENTO", "___")]
    y = Inches(2.1)
    for lab, val in tarj:
        text(s, Inches(7.5), y, Inches(2.6), Inches(0.3), [[(lab, {"size": 10, "bold": True, "color": MUT})]])
        text(s, Inches(10.1), y, Inches(2.6), Inches(0.3), [[(val, {"size": 11.5, "bold": True, "color": GD})]])
        y = y + Inches(0.28)
    text(s, Inches(7.5), Inches(3.5), Inches(5.0), Inches(0.2), [[("▮▮▯▮▯▮▮▯▮  ·  🎒", {"size": 10, "color": INK})]])
    # stappenroute
    text(s, Inches(7.3), Inches(3.85), Inches(5.5), Inches(0.3),
         [[("Pasos (steun bouwt af):", {"size": 12, "bold": True, "color": GD, "font": DISPLAY})]])
    pasos = ["1 Prepara tu tarjeta (MODEL)", "2 Ensaya tu nombre (alfabet)",
             "3 Escribe tu mini-diálogo (frame)", "4 Practica en duo (cue)", "5 Preséntate (SIN AYUDA)"]
    y = Inches(4.2)
    for p in pasos:
        chip(s, Inches(7.3), y, p, fill=WHITE, tcolor=GD, size=10.5, w=Inches(5.0))
        y = y + Inches(0.4)
    # modelo dialoog compact
    solucion(s, Inches(0.5), Inches(4.75), Inches(6.6), Inches(1.6),
             [[("Modelo (en la puerta):", {"bold": True, "color": G})],
              [("Lucía: ¡Hola! Yo soy Lucía. ¿Y tú?", {"color": GD, "size": 11})],
              [("Tú: ¡Hola! Yo soy Sam.  — Lucía: ¿Cómo se escribe?", {"color": GD, "size": 11})],
              [("Tú: Ese-a-eme. Sam.  Una pregunta: ¿cómo se dice «rugzak»?", {"color": GD, "size": 11})],
              [("Lucía: Se dice «la mochila». — Tú: ¡Gracias! ¡Hasta luego!", {"color": GD, "size": 11})]],
             title="MODELO · docent")
    footer(s, page=pg())
    notes(s, "TEACHER · FINAL_MISSION (idee 45 vier-vaardighedenmissie · idee 42 zelfopbouwende schrijftaak). "
             "Keten 3: model beluisteren → stappen ordenen → uitdrukkingen oefenen → eigen dialoog. Steun bouwt af per paso "
             "(MODEL→FRAME→CUE→GEEN). Succescriteria: spelt naam verstaanbaar · groet + afscheid · stelt 1 klasvraag. "
             "Feedback & herneming: na paso 5 één verbeterpunt kiezen → opnieuw inspreken (RecordReflectRetry). "
             "🔴 Spel-valstrikken NL→ES: W=uve doble, Y=i griega/ye, J=jota, H=hache (stom). Cross-ref: HTML VoiceMessageTask.")

# ============================================================================
# DIA 19 · QUIZ — «La mezcla» (gemengde ophaal, met oplossing)
# ============================================================================
def s19_mezcla():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "QUIZ · RETRIEVAL", "«La mezcla» — gemengde quiz",
               "Vijf mini-items, elk uit een ándere sectie. Kies zélf de juiste regel. (retrieval vóór herlezen, §14)", accent=AMBER)
    vragen = [
        ("1 · §2", "¿Lleva tilde: «Peru» o «Perú»?", "Perú"),
        ("2 · §1", "¿«h» klinkt of niet in «hola»?", "de h zwijgt"),
        ("3 · §3", "Escribe 47 en letras.", "cuarenta y siete"),
        ("4 · §4", "¿Encantado o encantada dice Nina?", "Encantada"),
        ("5 · §2", "Ordena: llana / esdrújula → «casa», «México».", "casa=llana · México=esdrújula"),
    ]
    y = Inches(1.5)
    for tag, v, ans in vragen:
        cardshp = card(s, Inches(0.5), y, Inches(12.3), Inches(0.62), fill=WHITE, line=LINE, lw=1.0)
        chip(s, Inches(0.62), y + Inches(0.15), tag, fill=GT, tcolor=GD, size=10, w=Inches(1.15))
        text(s, Inches(1.95), y, Inches(7.4), Inches(0.62), [[(v, {"size": 13.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        # klik op de vraagkaart → het antwoord springt in
        check_badge(s, Inches(9.5), y + Inches(0.14), cardshp, label="✓ " + ans, w=Inches(3.2))
        y = y + Inches(0.7)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.2), Inches(12.3), Inches(1.2),
             [[("1 ", {"bold": True, "color": GD}), ("Perú", {"bold": True, "color": G}), (" (aguda -ú)   ·   ", {"color": GD}),
               ("2 ", {"bold": True, "color": GD}), ("de h zwijgt", {"bold": True, "color": G}), (" (hola = «ola»)   ·   ", {"color": GD}),
               ("3 ", {"bold": True, "color": GD}), ("cuarenta y siete", {"bold": True, "color": G})],
              [("4 ", {"bold": True, "color": GD}), ("Encantada", {"bold": True, "color": G}), (" (Nina is een meisje — de uitgang volgt wie spreekt)   ·   ", {"color": GD}),
               ("5 ", {"bold": True, "color": GD}), ("casa = llana · México = esdrújula", {"bold": True, "color": G})]],
             trigger=btn, title_doc="SOLUCIÓN · docent")
    footer(s, page=pg())
    notes(s, "TEACHER · QUIZ (idee 17 Jeopardy-achtig · idee 18 oplopende reeks). Gemengde ophaal over de hele unit — "
             "geen aangeduide regel, leerling kiest zelf. Extra items: 'Pasaporte fonético' (Zaragoza·Málaga·Bogotá·Cáceres·Ecuador·Panamá "
             "hardop + familie benoemen) en 'Dictado mixto' (getal in cijfers+letters mét tilde). "
             "Sluit af met 'Check-in en la puerta' = generale repetitie van de Tarjeta de embarque.")

# ============================================================================
# DIA 20 · REPASO — lo esencial + semáforo
# ============================================================================
def s20_repaso():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "◎ REPASO", "Lo esencial de un vistazo + semáforo",
               "De hele U0 op één plaat + zelfevaluatie. Retrieval eerst (dia 19), dán terugbladeren.", accent=GD)
    quad = [
        ("🗺️ El mundo hispano", ["+20 landen · ~500 mln sprekers", "español = castellano", "kleine verschillen (coche/carro)"]),
        ("🔤 Sonar en español", ["27 letras (+ñ) · h zwijgt · b=v", "j+ge/gi=jota · ll/y=«j» · ñ=«nj»", "qu=«k» · z/ce/ci=«th» · r↔rr"]),
        ("🎩 La regla del sombrero", ["esdrújula → altijd ´", "aguda → ´ als -n/-s/klinker", "llana → ´ als NIET zo · monosíl. geen"]),
        ("🔢 Números & 👋 saludos", ["0-15 apart · 16-29 één woord", "30-100 decena+y+unidad", "edad = tener años (🔴 niet ser)"]),
    ]
    x0, y0 = Inches(0.5), Inches(1.45); tw=Inches(6.05); th=Inches(1.75); gx=Inches(0.2); gy=Inches(0.18)
    for i,(titel, lines) in enumerate(quad):
        r,c = divmod(i, 2)
        x = x0 + c*(tw+gx); y = y0 + r*(th+gy)
        card(s, x, y, tw, th, fill=WHITE, line=G, lw=1.4)
        rect(s, x, y, Inches(0.12), th, fill=G)
        text(s, x + Inches(0.25), y + Inches(0.08), tw - Inches(0.4), Inches(0.4),
             [[(titel, {"size": 14, "bold": True, "color": GD, "font": DISPLAY})]])
        yy = y + Inches(0.55)
        for ln in lines:
            text(s, x + Inches(0.28), yy, tw - Inches(0.45), Inches(0.35),
                 [[("• ", {"size": 11.5, "color": G, "bold": True}), (ln, {"size": 11.5, "color": INK})]], line=1.0)
            yy = yy + Inches(0.36)
    # semáforo
    card(s, Inches(0.5), Inches(5.45), Inches(12.33), Inches(1.05), fill=CREMA, line=AMBER, lw=1.3)
    text(s, Inches(0.68), Inches(5.52), Inches(4), Inches(0.35),
         [[("🚦 Semáforo — ¿cómo lo llevas?", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    text(s, Inches(0.68), Inches(5.9), Inches(12.0), Inches(0.55),
         [[("🔴 nog niet  ·  🟠 met steun  ·  🟢 zelfstandig — kleur per rij (receptief «ik herken» / productief «ik doe het zelf»). ",
            {"size": 11.5, "color": INK}),
           ("Volledige checklist in de PDF/HTML.", {"size": 11.5, "italic": True, "color": MUT})]], line=1.05)
    footer(s, page=pg())
    notes(s, "TEACHER · REPASO/FEEDBACK (idee 8 voortgangsmeter · idee 23 flashcards afbouw). SummaryQuadrant = spiekkaart. "
             "BESLIST 2026-07-26: het echte inoefen-repaso staat ONLINE (spellen + zelfcorrectie); print/PPT = spiekkaart + semáforo + "
             "'Repasa jugando (online)'. Laat leerlingen het semáforo eerlijk inkleuren (receptief/productief apart, statusladder 0-5). "
             "Vooruitblik U1 «¿Quién eres?» (Madrid): naam & e-mail spellen, edad met tener, saludos openen elke kennismaking (recycling).")

# ============================================================================
# DIA 21 · TEACHER_NOTES — timing + noodroute + cross-refs
# ============================================================================
def s21_teacher():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "TEACHER_NOTES · DOSSIER DEL DOCENTE", "Verloop · noodroute · cross-refs",
               "Alleen voor de leerkracht — niet projecteren. Timing 50 min, technische noodroute en verwijzingen.", accent=INK)
    # timing 50 min
    card(s, Inches(0.5), Inches(1.45), Inches(6.1), Inches(4.55), fill=WHITE, line=LINE, lw=1.2)
    text(s, Inches(0.68), Inches(1.55), Inches(5.7), Inches(0.35),
         [[("⏱ Verdeling over 50 min", {"size": 13.5, "bold": True, "color": GD, "font": DISPLAY})]])
    fases = [("Oriëntatie", "menu · cast · kaart", "5", "dia 2-3"),
             ("Begrijpen", "alfabet · klanktrampas", "8", "dia 4-5"),
             ("Opmerken", "sílaba tónica · sombrero", "7", "dia 7-8"),
             ("Oefenen (steun)", "quizzes · números", "12", "dia 6·9·10-12"),
             ("Productie", "saludos · diálogo · tarea", "10", "dia 13-18"),
             ("Feedback", "modelantwoord · peer", "5", "dia 19"),
             ("Exit", "repaso · semáforo · online", "3", "dia 20")]
    y = Inches(2.0)
    for fase, wat, mins, dias in fases:
        text(s, Inches(0.7), y, Inches(2.0), Inches(0.5), [[(fase, {"size": 11.5, "bold": True, "color": INK})]])
        text(s, Inches(2.6), y, Inches(2.5), Inches(0.5), [[(wat, {"size": 10.5, "color": MUT})]])
        text(s, Inches(5.05), y, Inches(0.7), Inches(0.5), [[(mins + "'", {"size": 11.5, "bold": True, "color": G})]])
        text(s, Inches(5.6), y, Inches(0.95), Inches(0.5), [[(dias, {"size": 8.5, "color": MUT})]])
        y = y + Inches(0.55)
    # noodroute + versies + crossrefs rechts
    card(s, Inches(6.85), Inches(1.45), Inches(5.95), Inches(2.15), fill=RGBColor(0xFD,0xEC,0xEC), line=RED, lw=1.2)
    text(s, Inches(7.05), Inches(1.55), Inches(5.6), Inches(0.35),
         [[("🆘 Noodroute (§5) — altijd beschikbaar", {"size": 12.5, "bold": True, "color": RED, "font": DISPLAY})]])
    text(s, Inches(7.05), Inches(1.98), Inches(5.6), Inches(1.55),
         [[("• Elke oefendia: knop ▶ Mostrar solución · ⏭ Saltar · ⌂ Menú (dia 2).", {"size": 11, "color": INK})],
          [("• Valt audio/video/internet weg → alle content staat óók als tekst/beeld op de dia (statische fallback).", {"size": 11, "color": INK})],
          [("• Docentversie .pptx = vrije navigatie + oplossing in de notities; leerlingversie .ppsx = gewone diavoorstelling (geen kiosk): elke klik onthult het volgende antwoord (fade). Geen docentnotities.", {"size": 11, "color": INK})]], line=1.12)
    card(s, Inches(6.85), Inches(3.75), Inches(5.95), Inches(2.25), fill=GT, line=G, lw=1.2)
    text(s, Inches(7.05), Inches(3.85), Inches(5.6), Inches(0.35),
         [[("🔗 Cross-refs (§16)", {"size": 12.5, "bold": True, "color": GD, "font": DISPLAY})]])
    text(s, Inches(7.05), Inches(4.28), Inches(5.6), Inches(1.65),
         [[("📄 Cursus (PDF/Word): ", {"size": 11, "bold": True, "color": GD}),
           ("U0 §1-§4 · Cultura · Tarea · Repaso · §V Vocabulario.", {"size": 11, "color": INK})],
          [("💻 Online (HTML): ", {"size": 11, "bold": True, "color": GD}),
           ("flip-cards (alfabet·getallen·cast) · ShadowingPlayer · info-gap teléfonos · bingo · ~10 spaans-motor-spellen.", {"size": 11, "color": INK})],
          [("➕ Extra-tab: ", {"size": 11, "bold": True, "color": GD}),
           ("profe-video «alfabeto» + «números 0-100» · Genially «saludos»/«sílaba tónica» (arche-ele) — links door leerkracht.", {"size": 11, "color": INK})]], line=1.1)
    footer(s, page=pg())
    notes(s, "TEACHER_NOTES. Deze dia niet projecteren (of overslaan in de leerlingversie .ppsx). "
             "Differentiatie / zij-instromers: U0 vertrekt van nul, dus geschikt voor iedereen. Con apoyo = frames open houden; "
             "desafío = frames dicht + tempo op. Beoordeling: de Tarjeta de embarque (dia 18) dekt spellen+groeten+klasvraag. "
             "Alle LPD-codes III-Spa-d nog concreet in te vullen (zie bron-md Bijlage C). "
             "Print-hygiëne / kleurlagen: cursusgroen = navigatie; functionele kleuren (blauw persoon · oranje werkw · paars tijd) enkel bij taalmarkering.")

# ---------------------------------------------------------------- build
# GEEN kioskmodus meer: beide decks openen als een gewone diavoorstelling waarin
# klikken vooruit gaat en elke klik de volgende reveal-shape onthult.


# ============================================================================
# RONDE 1 · twee dia's erbij: de leestekst en het luisterfragment
# Zelfde inhoud als de printcursus en de hub — de bron is gedeeld
# (lectura_data / escucha_data), zodat de drie dragers niet uit elkaar lopen.
# De oplossing staat in de docentenversie en verschijnt bij klik in de
# leerlingenversie, nooit meteen zichtbaar.
# ============================================================================
def s_lectura(t=None):
    t = t or _LEC
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§5 · LECTURA", "«%s»" % t["titulo"],
               "Een echte tekst. Je hoeft niet alles te begrijpen om de informatie eruit te halen.", num=5)
    # links: de tekst zelf
    card(s, Inches(0.5), Inches(1.45), Inches(6.1), Inches(4.55), fill=WHITE, line=G, lw=1.4)
    rect(s, Inches(0.5), Inches(1.45), Inches(6.1), Inches(0.42), fill=G)
    text(s, Inches(0.65), Inches(1.47), Inches(5.8), Inches(0.4),
         [[(t["tipo"], {"size": 11.5, "bold": True, "color": WHITE, "font": DISPLAY})]],
         anchor=MSO_ANCHOR.MIDDLE)
    lineas = []
    for soort, c in t["texto"]:
        if soort == "titulo":
            lineas.append([(c, {"size": 12.5, "bold": True, "color": GD, "font": DISPLAY})])
        elif soort == "lema":
            lineas.append([(c, {"size": 10.5, "italic": True, "color": MUT})])
        elif soort == "lista":
            for x in c:
                lineas.append([("• " + x, {"size": 10.5, "color": INK})])
        elif soort == "aviso":
            lineas.append([(c[0], {"size": 11, "bold": True, "color": GD})])
            lineas.append([(c[1], {"size": 10, "color": INK})])
        elif soort == "firma":
            lineas.append([(c, {"size": 9.5, "color": MUT})])
        else:
            lineas.append([(c, {"size": 10.5, "color": INK})])
    text(s, Inches(0.7), Inches(1.98), Inches(5.7), Inches(3.9), lineas, line=1.18)

    # rechts: scannen + juist/fout met bewijs
    card(s, Inches(6.85), Inches(1.45), Inches(5.98), Inches(2.15), fill=CREMA, line=LINE, lw=1.2)
    text(s, Inches(7.05), Inches(1.55), Inches(5.6), Inches(0.32),
         [[("Escanea — busca el dato", {"size": 12, "bold": True, "color": GD, "font": DISPLAY})]])
    text(s, Inches(7.05), Inches(1.92), Inches(5.6), Inches(1.6),
         [[("%d. %s" % (i + 1, e["q"]), {"size": 10.5, "color": INK})]
          for i, e in enumerate(t["escanear"])], line=1.25)

    card(s, Inches(6.85), Inches(3.75), Inches(5.98), Inches(2.25), fill=WHITE, line=LINE, lw=1.2)
    text(s, Inches(7.05), Inches(3.85), Inches(5.6), Inches(0.32),
         [[("¿Verdadero o falso? — y la prueba", {"size": 12, "bold": True, "color": GD, "font": DISPLAY})]])
    text(s, Inches(7.05), Inches(4.22), Inches(5.6), Inches(1.7),
         [[("%d. %s" % (i + 1, v["q"]), {"size": 10.5, "color": INK})]
          for i, v in enumerate(t["vf"])], line=1.25)

    sol = ["Escanear: " + " · ".join("%d) %s" % (i + 1, e["ans"]) for i, e in enumerate(t["escanear"]))]
    sol += ["%d) %s — «%s»" % (i + 1, "V" if v["ans"] else "F", v["prueba"]) for i, v in enumerate(t["vf"])]
    exercise_solucion(s, Inches(0.5), Inches(6.12), Inches(12.33), Inches(0.72), sol)
    footer(s, page=pg())
    notes(s, "TEACHER · READING. Route: voorspellen → globaal → scannen → juist/fout MET BEWIJS → betekenis uit "
             "context → zelf schrijven. Laat de tekst staan tijdens het scannen: informatie terugvinden is lezen, "
             "uit het hoofd opzeggen is iets anders. Eis bij elke V/F de zin uit de tekst — dat is de stap die "
             "gokken onmogelijk maakt. Dezelfde tekst staat in de cursus (met schrijfruimte) en op de hub "
             "(zelfcorrigerend, met vertaalknop).")


def s_escucha(f=None):
    f = f or _ESC
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§6 · ESCUCHA", "«%s»" % f["titulo"],
               "Eerst de situatie, dan luisteren. Het transcript komt pas ná de taken.", num=6)
    # situatie vooraf
    card(s, Inches(0.5), Inches(1.45), Inches(12.33), Inches(1.15), fill=GT, line=G, lw=1.2)
    text(s, Inches(0.7), Inches(1.55), Inches(11.9), Inches(0.95),
         [[("¿Dónde? ", {"size": 11, "bold": True, "color": GD}),
           (f["situacion"]["lugar"], {"size": 11, "color": INK}),
           ("     ¿Quién? ", {"size": 11, "bold": True, "color": GD}),
           (f["situacion"]["quien"], {"size": 11, "color": INK})],
          [("¿Qué pasa? ", {"size": 11, "bold": True, "color": GD}),
           (f["situacion"]["que"], {"size": 11, "color": INK})],
          [("Palabras clave: ", {"size": 10.5, "bold": True, "color": MUT}),
           (" · ".join(f["situacion"]["claves"]), {"size": 10.5, "italic": True, "color": INK})]], line=1.2)
    # vijf detailvragen
    card(s, Inches(0.5), Inches(2.75), Inches(6.1), Inches(3.25), fill=WHITE, line=LINE, lw=1.2)
    text(s, Inches(0.7), Inches(2.85), Inches(5.7), Inches(0.32),
         [[("Escucha con detalle", {"size": 12, "bold": True, "color": GD, "font": DISPLAY})]])
    text(s, Inches(0.7), Inches(3.22), Inches(5.7), Inches(2.6),
         [[("%d. %s" % (i + 1, d["q"]), {"size": 10.5, "color": INK})]
          for i, d in enumerate(f["detalle"])], line=1.35)
    # juist/fout met bewijs
    card(s, Inches(6.85), Inches(2.75), Inches(5.98), Inches(3.25), fill=CREMA, line=LINE, lw=1.2)
    text(s, Inches(7.05), Inches(2.85), Inches(5.6), Inches(0.32),
         [[("¿Verdadero o falso? — y la prueba", {"size": 12, "bold": True, "color": GD, "font": DISPLAY})]])
    text(s, Inches(7.05), Inches(3.22), Inches(5.6), Inches(1.6),
         [[("%d. %s" % (i + 1, v["q"]), {"size": 10.5, "color": INK})]
          for i, v in enumerate(f["vf"])], line=1.35)
    text(s, Inches(7.05), Inches(5.0), Inches(5.6), Inches(0.9),
         [[("Tu reacción: ", {"size": 10.5, "bold": True, "color": GD}),
           (f["produccion"]["prompt"], {"size": 10, "color": INK})]], line=1.2)

    sol = ["Detalle: " + " · ".join("%d) %s" % (i + 1, d["ans"]) for i, d in enumerate(f["detalle"]))]
    sol += ["%d) %s — «%s»" % (i + 1, "V" if v["ans"] else "F", v["prueba"]) for i, v in enumerate(f["vf"])]
    exercise_solucion(s, Inches(0.5), Inches(6.12), Inches(12.33), Inches(0.72), sol)
    footer(s, page=pg())
    notes(s, "TEACHER · LISTENING. Zes treden: situatie vooraf → globaal → vijf details → juist/fout MET BEWIJS → "
             "transcript pas ná de taken → productieve reactie. Speel het fragment minstens twee keer: één keer "
             "globaal (boeken dicht), daarna gericht. Het transcript staat op de hub en gaat daar pas open als de "
             "taken gedaan zijn — meelezen tijdens het luisteren maakt er een leesoefening van. Zolang er geen "
             "opname is, leest de computerstem het gesprek voor met een eigen stem per spreker. Noodroute: het "
             "fragment ook voorlezen kan, met twee leerlingen in de rollen.")


# ============================================================ RETOS · U0
# De drie retos die op het grote scherm leven (retos_data.py, soporte="ppt").
# De andere zeven staan in het boek of op de hub; die half naar een dia
# overzetten helpt niemand — een opnameoefening op een dia is geen oefening.
import retos_data as _RD

_RETOS = {r["num"]: r for r in _RD.RETOS}


def _reto_cabecera(s, r):
    """Kop, haakje en de beperking — voor elke reto identiek opgebouwd."""
    sectionbar(s, "RETO %d · %s" % (r["num"], r["lente"].split(" ", 1)[1].upper()),
               r["nombre"], r["consigna_nl"], num=r["num"])
    text(s, Inches(0.5), Inches(1.62), Inches(12.33), Inches(0.62),
         [[(r["gancho_es"], {"size": 17, "bold": True, "color": GD, "font": DISPLAY})],
          [(r["gancho_nl"], {"size": 11, "italic": True, "color": MUT})]], line=1.15)
    # de regla: zonder die beperking is het een gewone oefening
    # zelfde okerkader als in print (--amberbg), zodat de beperking overal
    # dezelfde kleur heeft: papier, scherm en dia
    rect(s, Inches(0.5), Inches(2.32), Inches(12.33), Inches(0.66),
         fill=RGBColor(0xFB, 0xF3, 0xD6), round=True, radius=0.05)
    rect(s, Inches(0.5), Inches(2.32), Inches(0.08), Inches(0.66), fill=AMBER)
    text(s, Inches(0.72), Inches(2.36), Inches(11.9), Inches(0.58),
         [[("LA REGLA DEL RETO   ", {"size": 9, "bold": True, "color": AMBER}),
           (r["regla"], {"size": 11.5, "color": INK})]], line=1.12)
    text(s, Inches(0.5), Inches(3.02), Inches(12.33), Inches(0.34),
         [[("  ·  ".join([r["forma"], r["skill"], r["tiempo"], r["dificultad"]]),
            {"size": 10, "color": MUT})]])


def s_reto_radio():
    """Reto 6 — Radio Nombres: spelshow op de letternamen."""
    r = _RETOS[6]; s = slide(); bg(s, PAPER); _reto_cabecera(s, r)
    y = Inches(3.5)
    for i, (es, nl) in enumerate(r["pasos"]):
        card(s, Inches(0.5) + Inches(3.12) * i, y, Inches(2.95), Inches(1.15))
        text(s, Inches(0.66) + Inches(3.12) * i, y + Inches(0.1), Inches(2.66), Inches(0.98),
             [[("%d" % (i + 1), {"size": 13, "bold": True, "color": G, "font": DISPLAY})],
              [(es, {"size": 10.5, "bold": True, "color": INK})],
              [(nl, {"size": 9, "italic": True, "color": MUT})]], line=1.1)
    d = r["datos"]
    text(s, Inches(0.5), Inches(4.84), Inches(6.0), Inches(0.3),
         [[("Las ciudades:  ", {"size": 11, "bold": True, "color": GD}),
           (" · ".join(d["ciudades"]), {"size": 11, "color": INK})]])
    text(s, Inches(0.5), Inches(5.18), Inches(6.0), Inches(0.3),
         [[("Las trampas:  ", {"size": 11, "bold": True, "color": RED}),
           (" · ".join(d["trampas"]), {"size": 11, "color": INK})]])
    x = Inches(6.9)
    card(s, x, Inches(4.76), Inches(5.93), Inches(1.62))
    text(s, x + Inches(0.2), Inches(4.84), Inches(5.5), Inches(0.3),
         [[("Las letras que cuestan", {"size": 11, "bold": True, "color": GD, "font": DISPLAY})]])
    for i, (le, nom, donde) in enumerate(d["letras_dificiles"]):
        col, fila = i % 3, i // 3
        text(s, x + Inches(0.2) + Inches(1.9) * col, Inches(5.18) + Inches(0.52) * fila,
             Inches(1.8), Inches(0.48),
             [[(le, {"size": 13, "bold": True, "color": G, "font": DISPLAY}),
               ("  " + nom, {"size": 10, "color": INK})],
              [(donde, {"size": 8.5, "italic": True, "color": MUT})]], line=1.06)
    exercise_solucion(s, Inches(0.5), Inches(6.5), Inches(12.33), Inches(0.62), r["clave"][:2])
    footer(s, page=pg())
    notes(s, "TEACHER · RETO 6 (mediaformat). " + r["nota"] + "  SLEUTEL: " + "  |  ".join(r["clave"]))


def s_reto_subasta():
    """Reto 2 — La subasta de sonidos: bieden op klankparen."""
    r = _RETOS[2]; s = slide(); bg(s, PAPER); _reto_cabecera(s, r)
    lotes = r["datos"]["lotes"]
    for i, (n, a, b, igual, regla, valor) in enumerate(lotes):
        col, fila = i % 4, i // 4
        x = Inches(0.5) + Inches(3.12) * col
        y = Inches(3.5) + Inches(1.52) * fila
        card(s, x, y, Inches(2.95), Inches(1.38))
        chip(s, x + Inches(0.14), y + Inches(0.12), "LOTE %d · %d pts" % (n, valor),
             fill=GT, tcolor=GD, size=9)
        text(s, x + Inches(0.14), y + Inches(0.52), Inches(2.7), Inches(0.42),
             [[(a, {"size": 15, "bold": True, "color": INK, "font": DISPLAY}),
               ("   ·   ", {"size": 13, "color": MUT}),
               (b, {"size": 15, "bold": True, "color": INK, "font": DISPLAY})]])
        # het antwoord verschijnt pas bij klik
        resp = rect(s, x + Inches(0.14), y + Inches(0.96), Inches(2.67), Inches(0.32),
                    fill=GT, round=True, radius=0.1)
        register_reveal(s, resp)
        lab = text(s, x + Inches(0.22), y + Inches(0.99), Inches(2.5), Inches(0.28),
                   [[("IGUAL" if igual else "DIFERENTE", {"size": 10, "bold": True,
                      "color": RED if igual else GD}),
                     ("  " + regla.split("·")[0].strip()[:26], {"size": 8, "color": MUT})]])
        register_reveal(s, lab)
    exercise_solucion(s, Inches(0.5), Inches(6.62), Inches(12.33), Inches(0.5), r["clave"][:1])
    footer(s, page=pg())
    notes(s, "TEACHER · RETO 2 (puzzel & escape). " + r["nota"] + "  SLEUTEL: " + "  |  ".join(r["clave"]))


def s_reto_semaforo():
    """Reto 5 — La tilde en el semáforo: de klas beweegt op de klemtoon."""
    r = _RETOS[5]; s = slide(); bg(s, PAPER); _reto_cabecera(s, r)
    zonas = [("IZQUIERDA", "aguda", "última sílaba", G),
             ("CENTRO", "llana", "penúltima sílaba", GD),
             ("DERECHA", "esdrújula", "antepenúltima", AMBER)]
    for i, (donde, tipo, expl, col) in enumerate(zonas):
        x = Inches(0.5) + Inches(4.16) * i
        card(s, x, Inches(3.46), Inches(3.98), Inches(1.06))
        rect(s, x, Inches(3.46), Inches(3.98), Inches(0.1), fill=col)
        text(s, x + Inches(0.18), Inches(3.62), Inches(3.6), Inches(0.86),
             [[(donde, {"size": 10, "bold": True, "color": MUT})],
              [(tipo, {"size": 17, "bold": True, "color": col, "font": DISPLAY})],
              [(expl, {"size": 9.5, "italic": True, "color": MUT})]], line=1.08)
    pal = r["datos"]["palabras"]
    for i, (w, tipo, sil) in enumerate(pal):
        col, fila = i % 5, i // 5
        x = Inches(0.5) + Inches(2.49) * col
        y = Inches(4.72) + Inches(0.62) * fila
        text(s, x, y, Inches(2.35), Inches(0.3),
             [[(w, {"size": 14, "bold": True, "color": INK, "font": DISPLAY})]])
        marca = text(s, x, y + Inches(0.28), Inches(2.35), Inches(0.26),
                     [[(tipo, {"size": 9.5, "bold": True, "color": G}),
                       ("  «%s»" % sil, {"size": 9.5, "color": MUT})]])
        register_reveal(s, marca)
    exercise_solucion(s, Inches(0.5), Inches(6.66), Inches(12.33), Inches(0.46), r["clave"][3:4])
    footer(s, page=pg())
    notes(s, "TEACHER · RETO 5 (puzzel & escape). " + r["nota"] + "  SLEUTEL: " + "  |  ".join(r["clave"]))


def _run_all_slides(include_teacher=True):
    s01_title(); s02_menu(); s03_cast()
    s04_alfabeto(); s05_trampas(); s06_quiz1()
    s_reto_radio(); s_reto_subasta()
    s07_tonica(); s08_sombrero(); s09_quiz2(); s_reto_semaforo()
    s10_numeros(); s11_edad(); s12_quiz3()
    s13_saludos(); s14_dialogo(); s15_lenguaclase()
    s16_cultura(); s17_variatie()
    s_lectura(); s_escucha()
    s18_tarea(); s19_mezcla(); s20_repaso()
    if include_teacher:
        s21_teacher()

def build(mode, out, include_teacher=True):
    global MODE
    MODE = mode
    new_presentation()
    _run_all_slides(include_teacher=include_teacher)
    ndia_timing, nreveals = apply_all_timing()
    apply_hyperlinks()
    prs.save(out)
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
    # Leerlingenversie = gewone .pptx (NOOIT .ppsx — CLAUDE.md §10, auteur 2026-07-26):
    # identieke dia's + klik-onthul-animaties; leerling drukt F5 voor de diavoorstelling.
    build("alumno", OUT_ALUMNO_PPTX, include_teacher=False)
    # Ruim een eventueel oud .ppsx op (deprecated leveringsformaat).
    if os.path.exists(OUT_ALUMNO):
        os.remove(OUT_ALUMNO)
    # Verifieer dat beide .pptx openen (round-trip).
    d = Presentation(OUT_DOCENTE); a = Presentation(OUT_ALUMNO_PPTX)
    print("round-trip OK · docente dia's:", len(d.slides._sldIdLst),
          "· alumno dia's:", len(a.slides._sldIdLst),
          "· alumno =", os.path.basename(OUT_ALUMNO_PPTX), "(.pptx, geen .ppsx)")
