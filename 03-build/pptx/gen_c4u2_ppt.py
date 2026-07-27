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
OUT_DOCENTE = os.path.join(HERE, "C4_U2_docente.pptx")
OUT_ALUMNO_PPTX = os.path.join(HERE, "C4_U2_alumno.pptx")
OUT_ALUMNO = os.path.join(HERE, "C4_U2_alumno.ppsx")

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

def footer(s, tab="U0 · ¡EMPEZAMOS!", page=None):
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
# C4 · UNIDAD 1 «Presentaciones» — slides (survival). Herbruikt de U0-machinerie.
# ============================================================================
FTAB = "U2 · SALUDOS"

def s01_title():
    s = slide(); bg(s)
    rect(s, 0, 0, EMU_W, Inches(4.7), fill=G)
    rect(s, 0, Inches(4.62), EMU_W, Inches(0.08), fill=GD)
    chip(s, Inches(0.6), Inches(0.55), "C4 · LA RUTA · EL DESPEGUE · PARADA 2", fill=WHITE, tcolor=G, size=12)
    text(s, Inches(0.55), Inches(1.35), Inches(12), Inches(1.8),
         [[("Saludos", {"size": 66, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(0.6), Inches(3.15), Inches(11.5), Inches(1.1),
         [[("¡Buenos días! Groeten volgens het moment van de dag en zeggen ", {"size": 17, "color": WHITE}),
           ("hoe je je voelt.", {"size": 17, "bold": True, "color": WHITE})],
          [("Survival in Spanish — todo lo que oyes, lo puedes usar enseguida.", {"size": 13, "italic": True, "color": GT})]])
    # mochila-gids
    avatar(s, "mochila", Inches(10.7), Inches(4.95), d=Inches(1.7))
    text(s, Inches(0.6), Inches(5.25), Inches(9), Inches(1.4),
         [[("En esta unidad vas a…", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})],
          [("• Saludar según el momento del día  ", {"size": 13, "color": INK}), ("días · tardes · noches", {"size": 11, "italic": True, "color": MUT})],
          [("• Decir cómo estás  ", {"size": 13, "color": INK}), ("estar + estado (bien, cansado…)", {"size": 11, "italic": True, "color": MUT})],
          [("• Despedirte  ", {"size": 13, "color": INK}), ("adiós · hasta luego · hasta mañana", {"size": 11, "italic": True, "color": MUT})]])
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
    tiles = [("1", "¡Escucha!", "de scène + chunks", 2),
             ("2", "Suena bien", "jota · h muda · acento", 3),
             ("3", "Kit", "saludos por el día", 4),
             ("4", "Gramática", "estar · saludo por hora", 6),
             ("5", "Práctica", "oefenen samen", 8),
             ("6", "Hablar", "un día de saludos", 9),
             ("7", "Música", "banda sonora", 10),
             ("8", "Tarea", "un día de saludos", 11),
             ("9", "Repaso", "wat kun je nu?", 12)]
    x0, y0 = Inches(0.55), Inches(1.7)
    w = Inches(3.0); gx = Inches(0.18); gy = Inches(0.2)
    for i, t in enumerate(tiles):
        col = i % 4; row = i // 4
        _tile(s, x0 + col * (w + gx), y0 + row * (Inches(1.15) + gy), w, *t)
    text(s, Inches(0.6), Inches(5.95), Inches(12), Inches(0.9),
         [[("Consejo · Tip. ", {"size": 12, "bold": True, "color": GD, "font": DISPLAY}),
           ("Luister eerst, spreek na, en durf zelf te praten. Fouten maken hoort erbij.", {"size": 12, "italic": True, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

def s03_escucha():
    s = slide(); bg(s)
    sectionbar(s, "§1 · ¡ESCUCHA!", "Bekijk la escena y escucha", "Kijk & luister — de scène speelt op 09.00 · 16.00 · 21.05 u", num=1)
    card(s, Inches(0.55), Inches(1.55), Inches(7.4), Inches(4.9), fill=WHITE, line=LINE)
    dia = [("Julio", "Josefina… Buenos días.", F_VERB), ("Josefina", "¿Cómo estás?", F_SUBJ),
           ("Julio", "Bien, bien. Es María, la nueva profesora.", F_VERB), ("Josefina", "Yo estoy ocupada. Muy ocupada.", F_SUBJ),
           ("María", "Buenas tardes. ¿Cómo estás?", F_TIME),
           ("Josefina", "Estoy enferma. Un poco enferma.", F_SUBJ), ("Fernando", "Y tú, ¿cómo estás?", F_PLAC),
           ("Josefina", "Uf, cansada, muy cansada.", F_SUBJ)]
    y = Inches(1.8)
    for sp, tx, col in dia:
        chip(s, Inches(0.75), y, sp, fill=col, tcolor=WHITE, size=10)
        text(s, Inches(2.35), y - Inches(0.02), Inches(5.4), Inches(0.5),
             [[(tx, {"size": 13, "color": INK})]])
        y = y + Inches(0.58)
    # chunks-kaart rechts
    card(s, Inches(8.2), Inches(1.55), Inches(4.6), Inches(3.4), fill=GT, line=G)
    text(s, Inches(8.45), Inches(1.75), Inches(4.1), Inches(3.1),
         [[("Chunks para llevar 🎒", {"size": 14, "bold": True, "color": GD, "font": DISPLAY})],
          [("Buenos días · Buenas tardes", {"size": 13, "color": INK})],
          [("Buenas noches · ¿Cómo estás?", {"size": 13, "color": INK})],
          [("Estoy bien / cansado-a / ocupado-a", {"size": 13, "color": INK})],
          [("enfermo-a · nervioso-a · regular", {"size": 13, "color": INK})],
          [("Hasta luego · Adiós · Hasta mañana", {"size": 13, "color": INK})]])
    card(s, Inches(8.2), Inches(5.1), Inches(4.6), Inches(1.35), fill=WHITE, line=LINE)
    text(s, Inches(8.45), Inches(5.25), Inches(4.1), Inches(1.1),
         [[("🎬 Vídeo online", {"size": 12, "bold": True, "color": GD, "font": DISPLAY})],
          [("Scan de QR op de cursus of open de digitale hub → tabblad Escucha.", {"size": 11, "color": MUT})]])
    footer(s, tab=FTAB, page=pg())

def s04_kit():
    s = slide(); bg(s)
    sectionbar(s, "§2 · KIT", "Saludar por el día y despedirse", "Groeten volgens het moment & afscheid nemen", num=2)
    cols = [("Saludar · begroeten", [("Buenos días", "goedemorgen"), ("Buenas tardes", "goedemiddag"),
              ("Buenas noches", "goedenavond"), ("¡Hola!", "hallo"), ("¡Buenas!", "hoi (informeel)")]),
            ("Preguntar · vragen", [("¿Qué tal?", "hoe gaat het?"), ("¿Cómo estás?", "hoe gaat het? (jij)"),
              ("¿Cómo está usted?", "… met u?"), ("¿Y tú?", "en jij?")]),
            ("Despedirse · afscheid", [("Adiós", "dag"), ("Hasta luego", "tot straks"),
              ("Hasta mañana", "tot morgen"), ("¡Nos vemos!", "we zien elkaar!"), ("Chao", "doei")])]
    x = Inches(0.55); w = Inches(4.0)
    for title, items in cols:
        card(s, x, Inches(1.6), w, Inches(4.9), fill=WHITE, line=LINE)
        text(s, x + Inches(0.25), Inches(1.78), w - Inches(0.4), Inches(0.5),
             [[(title, {"size": 13.5, "bold": True, "color": GD, "font": DISPLAY})]])
        y = Inches(2.45)
        for es, nl in items:
            text(s, x + Inches(0.25), y, w - Inches(0.5), Inches(0.6),
                 [[(es, {"size": 14, "bold": True, "color": INK}), ("   " + nl, {"size": 11, "italic": True, "color": MUT})]])
            y = y + Inches(0.72)
        x = x + w + Inches(0.2)
    footer(s, tab=FTAB, page=pg())

def s05_presentarse():
    s = slide(); bg(s)
    sectionbar(s, "§2 · KIT", "Decir cómo estoy", "Zeggen hoe je je voelt · estar + estado", num=2)
    left = [("Estoy bien", "ik voel me goed"), ("Muy bien", "heel goed"), ("Regular", "gaat wel"),
            ("Estoy cansado / cansada", "ik ben moe"), ("Estoy ocupado / ocupada", "ik heb het druk")]
    right = [("Estoy nervioso / nerviosa", "ik ben nerveus"), ("Estoy enfermo / enferma", "ik ben ziek"),
             ("Estoy fatal", "heel slecht"), ("¿Y tú?", "en jij?")]
    card(s, Inches(0.55), Inches(1.6), Inches(6.0), Inches(4.9), fill=GT, line=G)
    text(s, Inches(0.8), Inches(1.78), Inches(5.5), Inches(0.5),
         [[("¿Cómo estás? → Estoy…", {"size": 13.5, "bold": True, "color": GD, "font": DISPLAY})]])
    y = Inches(2.5)
    for es, nl in left:
        text(s, Inches(0.8), y, Inches(5.4), Inches(0.6), [[(es, {"size": 15, "bold": True, "color": INK}), ("   " + nl, {"size": 11, "italic": True, "color": MUT})]])
        y = y + Inches(0.72)
    card(s, Inches(6.8), Inches(1.6), Inches(6.0), Inches(4.9), fill=WHITE, line=LINE)
    text(s, Inches(7.05), Inches(1.78), Inches(5.5), Inches(0.5),
         [[("Más estados · meer toestanden", {"size": 13.5, "bold": True, "color": GD, "font": DISPLAY})]])
    y = Inches(2.5)
    for es, nl in right:
        text(s, Inches(7.05), y, Inches(5.4), Inches(0.6), [[(es, {"size": 15, "bold": True, "color": INK}), ("   " + nl, {"size": 11, "italic": True, "color": MUT})]])
        y = y + Inches(0.72)
    text(s, Inches(7.05), Inches(5.7), Inches(5.5), Inches(0.7),
         [[("¡Ojo! ", {"size": 12, "bold": True, "color": RED}),
           ("Estoy bien (niet «Soy bien»). Man: -o · vrouw: -a.", {"size": 12, "italic": True, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

def s06_gram_ser():
    s = slide(); bg(s)
    sectionbar(s, "§4 · GRAMÁTICA", "estar · saludo por la hora", "Hoe je je voelt & groeten volgens de klok — functioneel", num=4)
    legend_func(s, Inches(0.55), Inches(1.42))
    # estar
    card(s, Inches(0.55), Inches(1.9), Inches(6.0), Inches(2.2), fill=WHITE, line=LINE)
    text(s, Inches(0.8), Inches(2.05), Inches(5.5), Inches(0.4), [[("estar — hoe je je voelt", {"size": 15, "bold": True, "color": GD, "font": DISPLAY})]])
    est = [("yo", "estoy", "ik ben / voel me"), ("tú", "estás", "jij bent / voelt je"), ("él/ella/usted", "está", "hij/zij is · u bent")]
    y = Inches(2.55)
    for p, v, nl in est:
        text(s, Inches(0.8), y, Inches(5.6), Inches(0.4),
             [[(p + "  ", {"size": 13, "bold": True, "color": F_SUBJ}), (v, {"size": 13, "bold": True, "color": F_VERB}), ("   " + nl, {"size": 11, "italic": True, "color": MUT})]])
        y = y + Inches(0.48)
    # saludo por hora
    card(s, Inches(6.8), Inches(1.9), Inches(6.0), Inches(2.2), fill=WHITE, line=LINE)
    text(s, Inches(7.05), Inches(2.05), Inches(5.5), Inches(0.4), [[("saludo según la hora", {"size": 15, "bold": True, "color": GD, "font": DISPLAY})]])
    hor = [("🌅 la mañana", "Buenos días", "~6–12 u"), ("☀️ la tarde", "Buenas tardes", "~12–20 u"), ("🌙 la noche", "Buenas noches", "~20–6 u")]
    y = Inches(2.55)
    for m, v, nl in hor:
        text(s, Inches(7.05), y, Inches(5.6), Inches(0.4),
             [[(m + "  ", {"size": 13, "bold": True, "color": INK}), (v, {"size": 13, "bold": True, "color": GD}), ("   " + nl, {"size": 11, "italic": True, "color": MUT})]])
        y = y + Inches(0.48)
    # mini-quiz met reveal
    card(s, Inches(0.55), Inches(4.35), Inches(12.25), Inches(1.7), fill=GT, line=G)
    text(s, Inches(0.8), Inches(4.5), Inches(11.7), Inches(0.5),
         [[("Completa · vul aan (klik voor de oplossing): ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("Yo ___ bien.  ¿Cómo ___ (tú)?  María ___ cansada.  08.30 → ___ ", {"size": 13, "color": INK})]])
    exercise_solucion(s, Inches(0.8), Inches(5.15), Inches(11.7), Inches(0.7),
        [[("estoy · estás · está · Buenos días", {"bold": True, "color": GD, "size": 13})]])
    noodroute(s)
    notes(s, "Functioneel: enkel estoy/estás/está (estar voor toestand/gevoel). Geen volledige conjugatie. Saludo volgens de klok (días/tardes/noches). Geen ser/estar-contrast als systeem — dat is C5/C6.")
    footer(s, tab=FTAB, page=pg())

def s07_gram_mv():
    s = slide(); bg(s)
    sectionbar(s, "§4 · GRAMÁTICA", "-o / -a · tú / usted", "Man/vrouw (op de estados) & informeel/beleefd", num=4)
    card(s, Inches(0.55), Inches(1.7), Inches(6.0), Inches(2.3), fill=RGBColor(0xE8,0xF0,0xFE), line=LINE)
    text(s, Inches(0.8), Inches(1.9), Inches(5.5), Inches(2.0),
         [[("♂ Un chico dice…", {"size": 14, "bold": True, "color": RGBColor(0x1E,0x40,0xAF), "font": DISPLAY})],
          [("Estoy cansado", {"size": 18, "bold": True, "color": RGBColor(0x1E,0x40,0xAF)})],
          [("ocupado · nervioso · enfermo", {"size": 14, "bold": True, "color": RGBColor(0x1E,0x40,0xAF)})]])
    card(s, Inches(6.8), Inches(1.7), Inches(6.0), Inches(2.3), fill=RGBColor(0xFC,0xE7,0xF0), line=LINE)
    text(s, Inches(7.05), Inches(1.9), Inches(5.5), Inches(2.0),
         [[("♀ Una chica dice…", {"size": 14, "bold": True, "color": RGBColor(0x9D,0x17,0x4D), "font": DISPLAY})],
          [("Estoy cansada", {"size": 18, "bold": True, "color": RGBColor(0x9D,0x17,0x4D)})],
          [("ocupada · nerviosa · enferma", {"size": 14, "bold": True, "color": RGBColor(0x9D,0x17,0x4D)})]])
    card(s, Inches(0.55), Inches(4.2), Inches(12.25), Inches(1.8), fill=WHITE, line=LINE)
    text(s, Inches(0.8), Inches(4.4), Inches(11.7), Inches(1.5),
         [[("tú  ↔  usted", {"size": 15, "bold": True, "color": GD, "font": DISPLAY})],
          [("Met vrienden en klasgenoten: ", {"size": 13, "color": INK}), ("tú", {"size": 13, "bold": True, "color": F_VERB}),
           ("  (¿Cómo estás? · ¿Qué tal?).", {"size": 13, "color": INK})],
          [("Formeel, met een onbekende volwassene / de directeur: ", {"size": 13, "color": INK}), ("usted", {"size": 13, "bold": True, "color": F_VERB}),
           ("  (¿Cómo está usted?).", {"size": 13, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

def s08_practica():
    s = slide(); bg(s)
    sectionbar(s, "§3 · PRÁCTICA", "Completa el diálogo", "Vul samen aan — klik voor de oplossing", num=3)
    card(s, Inches(0.55), Inches(1.7), Inches(7.6), Inches(4.5), fill=WHITE, line=LINE)
    lines = [("— Buenos ___, ¿cómo ___?", "días · estás"),
             ("— ___ bien, gracias. ¿Y tú?", "Estoy"),
             ("— Regular… ___ un poco cansada.", "estoy"),
             ("— Vaya. ¡Hasta ___!", "luego")]
    y = Inches(2.0)
    for q, _a in lines:
        text(s, Inches(0.8), y, Inches(7.1), Inches(0.6), [[(q, {"size": 16, "color": INK})]])
        y = y + Inches(0.9)
    exercise_solucion(s, Inches(8.4), Inches(1.9), Inches(4.4), Inches(4.0),
        [[("1. días · estás", {"color": GD, "size": 14})], [("2. Estoy", {"color": GD, "size": 14})],
         [("3. estoy", {"color": GD, "size": 14})], [("4. luego", {"color": GD, "size": 14})]],
        title_doc="SOLUCIÓN · docent")
    noodroute(s)
    notes(s, "Laat leerlingen eerst zelf proberen (in duo). Klik daarna de oplossing open. Let op estar (estoy/estás) + saludo por hora.")
    footer(s, tab=FTAB, page=pg())

def s09_speaking():
    s = slide(); bg(s)
    sectionbar(s, "§3 · HABLAR", "Un día de saludos", "Groet volgens het uur en zeg hoe het gaat — sin leer", num=3)
    card(s, Inches(0.55), Inches(1.7), Inches(7.6), Inches(3.4), fill=GT, line=G)
    text(s, Inches(0.85), Inches(1.95), Inches(7.1), Inches(3.0),
         [[("Modelo · zeg dit hardop (por la mañana):", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})],
          [("«¡Buenos días! ¿Qué tal?", {"size": 18, "color": INK})],
          [("— Estoy bien, ¿y tú?", {"size": 18, "color": INK})],
          [("— Regular, estoy un poco cansado.", {"size": 18, "color": INK})],
          [("— Vaya. ¡Hasta luego!»", {"size": 18, "color": INK})]])
    card(s, Inches(8.4), Inches(1.7), Inches(4.4), Inches(3.4), fill=WHITE, line=LINE)
    text(s, Inches(8.65), Inches(1.95), Inches(3.9), Inches(3.0),
         [[("¿Cómo? · Werkvorm", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})],
          [("1. Kies een moment (🌅☀️🌙).", {"size": 13, "color": INK})],
          [("2. Groet gepast + vraag ¿cómo estás?", {"size": 13, "color": INK})],
          [("3. Antwoord met estar + estado.", {"size": 13, "color": INK})],
          [("4. Neem afscheid. Wissel (3×).", {"size": 13, "color": INK})]])
    text(s, Inches(0.6), Inches(5.4), Inches(12), Inches(0.7),
         [[("Interactie ", {"size": 12, "bold": True, "color": GD, "font": DISPLAY}),
           ("= beurt nemen, luisteren en reageren. Begrijp je iets niet? Zeg: «¿Cómo? / Otra vez, por favor.»", {"size": 12, "italic": True, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

def s10_musica():
    s = slide(); bg(s)
    sectionbar(s, "CULTURA", "Saludos & banda sonora", "Warme begroetingen (dos besos) + muziek die jullie kennen", num=None)
    bandas = [("Rosalía", "La Perla", "🇪🇸 flamenco+pop"), ("Luis Fonsi", "Despacito", "🇵🇷 pop"),
              ("Manu Chao", "Me gustas tú", "🌎 clásico"), ("Aitana", "6 de febrero", "🇪🇸 pop"),
              ("Karol G", "TQG", "🇨🇴 reggaetón"), ("Quevedo", "Bzrp #52", "🇪🇸 urban")]
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
         [[("🎧 La playlist de la clase (Spotify) ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("+ LyricsTraining (vul de tekst aan terwijl je luistert). Alles op de digitale hub → tabblad Música.", {"size": 12, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

def s11_tarea():
    s = slide(); bg(s)
    sectionbar(s, "§5 · TAREA FINAL", "Un día de saludos", "Speel 3 mini-gesprekjes, één per moment van de dag", num=5)
    card(s, Inches(0.55), Inches(1.7), Inches(6.0), Inches(3.5), fill=WHITE, line=G, lw=1.6)
    rect(s, Inches(0.55), Inches(1.7), Inches(6.0), Inches(0.55), fill=G)
    text(s, Inches(0.75), Inches(1.78), Inches(5.6), Inches(0.4), [[("DIARIO DE SALUDOS · noteer je gesprekjes", {"size": 12, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(0.85), Inches(2.5), Inches(5.4), Inches(2.5),
         [[("🌅 Saludo  ", {"size": 14, "bold": True, "color": INK}), ("____________  Estoy ______", {"size": 14, "color": LINE})],
          [("☀️ Saludo  ", {"size": 14, "bold": True, "color": INK}), ("____________  Estoy ______", {"size": 14, "color": LINE})],
          [("🌙 Saludo  ", {"size": 14, "bold": True, "color": INK}), ("____________  Estoy ______", {"size": 14, "color": LINE})]])
    card(s, Inches(6.8), Inches(1.7), Inches(6.0), Inches(3.5), fill=GT, line=G)
    text(s, Inches(7.05), Inches(1.9), Inches(5.5), Inches(3.1),
         [[("Los pasos · stappen", {"size": 14, "bold": True, "color": GD, "font": DISPLAY})],
          [("1. Kies een moment: mañana / tarde / noche.", {"size": 13, "color": INK})],
          [("2. Groet gepast + «¿cómo estás?»", {"size": 13, "color": INK})],
          [("3. Antwoord met estar: «Estoy ___» (‑o/‑a).", {"size": 13, "color": INK})],
          [("4. Sluit af: «Hasta luego / mañana. Adiós.»", {"size": 13, "color": INK})]])
    text(s, Inches(0.6), Inches(5.5), Inches(12), Inches(0.9),
         [[("🏁 Klaar als… ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("je op elk moment de juiste groet kiest (días/tardes/noches), met estar zegt hoe je je voelt (juiste ‑o/‑a) en netjes afscheid neemt — zónder af te lezen.", {"size": 12.5, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

def s12_repaso():
    s = slide(); bg(s)
    sectionbar(s, "REPASO", "Lo esencial de un vistazo", "Wat je nu kunt — semáforo", num=None)
    card(s, Inches(0.55), Inches(1.7), Inches(7.6), Inches(4.4), fill=WHITE, line=LINE)
    text(s, Inches(0.85), Inches(1.9), Inches(7.1), Inches(4.0),
         [[("Zo groet je volgens het uur", {"size": 14, "bold": True, "color": GD, "font": DISPLAY})],
          [("🌅 Buenos días · ☀️ Buenas tardes · 🌙 Buenas noches", {"size": 14, "color": INK})],
          [("Afscheid: Adiós · Hasta luego · Hasta mañana", {"size": 14, "color": INK})],
          [("", {"size": 6})],
          [("Zo zeg je hoe het gaat", {"size": 14, "bold": True, "color": GD, "font": DISPLAY})],
          [("¿Cómo estás? → Estoy bien / cansad_ / ocupad_.", {"size": 13, "color": INK})],
          [("estar: estoy · estás · está", {"size": 13, "color": INK})],
          [("-o = ♂ · -a = ♀   |   tú = vriend · usted = beleefd", {"size": 13, "color": INK})]])
    card(s, Inches(8.4), Inches(1.7), Inches(4.4), Inches(4.4), fill=GT, line=G)
    text(s, Inches(8.65), Inches(1.9), Inches(3.9), Inches(0.5), [[("Puedo… · Ik kan…", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    items = ["groeten volgens het moment", "hoe het gaat zeggen (estar)", "afscheid nemen", "-o/-a & tú/usted kiezen"]
    y = Inches(2.55)
    for it in items:
        text(s, Inches(8.65), y, Inches(3.9), Inches(0.5), [[("🟢🟡🔴  ", {"size": 12}), (it, {"size": 12, "color": INK})]])
        y = y + Inches(0.62)
    text(s, Inches(8.65), Inches(5.35), Inches(3.9), Inches(0.7), [[("🎮 Repasa jugando", {"size": 12, "bold": True, "color": GD, "font": DISPLAY})], [("online op de hub", {"size": 11, "italic": True, "color": MUT})]])
    footer(s, tab=FTAB, page=pg())

def s13_teacher():
    s = slide(); bg(s, color=RGBColor(0x24,0x1C,0x1B))
    text(s, Inches(0.6), Inches(0.5), Inches(12), Inches(0.7), [[("Docentendossier · Unidad 2 «Saludos»", {"size": 22, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(0.6), Inches(1.4), Inches(12.1), Inches(5.4),
         [[("Timing (2 lesuren van 50 min).", {"size": 14, "bold": True, "color": RGBColor(0xFB,0xEA,0xEC), "font": DISPLAY})],
          [("Les 1: Escucha (sitcom ep. 2, 3 momenten) + Suena bien (jota/h muda) + Kit (saludos por el día · estar+estado). Les 2: gramática functioneel (estar · saludo por hora), hablar, tarea + música.", {"size": 12.5, "color": RGBColor(0xEC,0xEA,0xE3)})],
          [("", {"size": 6})],
          [("Aanpak C4 (survival).", {"size": 14, "bold": True, "color": RGBColor(0xFB,0xEA,0xEC), "font": DISPLAY})],
          [("Chunks komen auditief binnen (luisteren → naspreken). estar enkel functioneel (estoy/estás/está voor toestand), géén ser/estar-contrast als systeem en géén volledige conjugatie — dat is C5/C6. Doelcodes: C4-GE-1/2 · C4-WS-2 · C4-MEC-3 · C4-CU-2.", {"size": 12.5, "color": RGBColor(0xEC,0xEA,0xE3)})],
          [("", {"size": 6})],
          [("Evaluatie.", {"size": 14, "bold": True, "color": RGBColor(0xFB,0xEA,0xEC), "font": DISPLAY})],
          [("Mondelinge mini-taak («un día de saludos»: 3 momenten groeten + estar) + herkennen van saludos/estados. Geen leerplan → focus op «kunnen gebruiken in de praktijk».", {"size": 12.5, "color": RGBColor(0xEC,0xEA,0xE3)})],
          [("", {"size": 6})],
          [("Oplossingen staan bij elke oefendia in de presenter-notities; antwoorden verschijnen bij klik.", {"size": 11.5, "italic": True, "color": RGBColor(0xA6,0xA2,0x9A)})]])
    footer(s, tab=FTAB, page=pg())

def s_uitspraak():
    s = slide(); bg(s)
    sectionbar(s, "SUENA BIEN", "La jota /x/ · la h muda · el acento", "De jota, de stille h & de klemtoon — luister en spreek na", num=None)
    # jota-kaart
    card(s,Inches(0.55),Inches(1.6),Inches(6.05),Inches(2.15),fill=WHITE,line=LINE)
    rect(s,Inches(0.55),Inches(1.6),Inches(6.05),Inches(0.14),fill=G)
    text(s,Inches(0.8),Inches(1.85),Inches(5.6),Inches(0.4),[[("La jota /x/ · j en g+e,i",{"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
    text(s,Inches(0.8),Inches(2.35),Inches(5.6),Inches(1.3),
         [[("Josefina · jueves · gente · gimnasio · trabajo · mujer",{"size":15,"bold":True,"color":INK})],
          [("Keelklank, zoals de NL «g» maar krachtiger.",{"size":11,"italic":True,"color":MUT})]])
    # h muda-kaart
    card(s,Inches(6.75),Inches(1.6),Inches(6.05),Inches(2.15),fill=WHITE,line=LINE)
    rect(s,Inches(6.75),Inches(1.6),Inches(6.05),Inches(0.14),fill=G)
    text(s,Inches(7.0),Inches(1.85),Inches(5.6),Inches(0.4),[[("La h muda · de stille h",{"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
    text(s,Inches(7.0),Inches(2.35),Inches(5.6),Inches(1.3),
         [[("hola · hasta · hija · ahora · hombre · hospital",{"size":15,"bold":True,"color":INK})],
          [("Je schrijft de h wél, maar je hóórt ze niet: «hola» = «ola».",{"size":11,"italic":True,"color":MUT})]])
    card(s,Inches(0.55),Inches(3.9),Inches(12.25),Inches(0.85),fill=GT,line=G)
    text(s,Inches(0.85),Inches(4.05),Inches(11.7),Inches(0.6),
         [[("¡Ojo! ",{"size":13,"bold":True,"color":RED,"font":DISPLAY}),("g + a/o/u = /g/ (gato, gusto)  ·  maar g + e/i = /x/ (gente, gimnasio) — net als de j.",{"size":13,"color":INK})]])
    text(s,Inches(0.6),Inches(5.0),Inches(12),Inches(0.4),[[("El acento en los saludos · waar ligt de klemtoon?",{"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
    text(s,Inches(0.6),Inches(5.55),Inches(12.2),Inches(0.7),
         [[("bue·nos ",{}),("DÍ",{"color":G,"bold":True}),("·as      bue·nas ",{}),("TAR",{"color":G,"bold":True}),
           ("·des      bue·nas ",{}),("NO",{"color":G,"bold":True}),("·ches",{})]],size=20,font=DISPLAY)
    text(s,Inches(0.6),Inches(6.35),Inches(12),Inches(0.4),[[("🔊 Oefen de klanken online op de hub (tabblad Kit · Suena bien).",{"size":11,"italic":True,"color":MUT})]])
    footer(s, tab=FTAB, page=pg())

def _run_all_slides(include_teacher=True):
    s01_title(); s02_menu(); s03_escucha(); s_uitspraak()
    s04_kit(); s05_presentarse(); s06_gram_ser()
    s07_gram_mv(); s08_practica(); s09_speaking()
    s10_musica(); s11_tarea(); s12_repaso()
    if include_teacher:
        s13_teacher()


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
    # Leerlingenversie: gewone diavoorstelling (geen kiosk), antwoorden bij klik → .ppsx.
    build_alumno()
