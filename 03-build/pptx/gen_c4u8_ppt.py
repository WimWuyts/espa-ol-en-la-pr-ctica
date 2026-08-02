#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_c4u8_ppt.py — Interactieve PowerPoint C4 · Unidad 8 «La hora y los días»
================================================================================
Gedeelde builder (één bron) → TWEE decks:
  · C4_U8_docente.pptx  — docentversie: vrije navigatie; antwoorden verschijnen bij
    klik (fade) + volledige oplossing & didactiek in de spreker-notities.
  · C4_U8_alumno.ppsx   — leerlingversie: GEEN docentnotities, GEEN kiosk; gewone
    diavoorstelling waarin de antwoorden/oplossingen bij klik verschijnen.

ECHTE interactiviteit: op elke oefendia wordt <p:timing>-XML geïnjecteerd met
standaard SEQUENTIËLE on-click entrance-animaties (fade-in) in de hoofdsequentie
(mainSeq): elke klik onthult de volgende reveal-shape. + hyperlink-navigatie
(menutegels, ⌂ Menú). Cast-avatars = de ECHTE flat-vector SVG's.

Thema U8: La hora y los días · ¿qué hora es? (es la una ↔ son las dos/ocho ·
y cuarto · y media · menos cuarto · en punto) · ¿a qué hora? (a la una · a las doce
= «om») · los días de la semana (el lunes ↔ los lunes, géén «en», kleine letter) ·
quedar (¿quieres quedar? · quedamos a las… · ¿dónde quedamos?). Eindtaak «Mi horario».
Huisstijl: unitkleur rood #D64550 (C4). Spaans-eerst + NL-steun. Twee kleurlagen:
cursusrood (navigatie) + functionele taalsemantiek (persoon = blauw · werkwoord =
oranje · TIJD = paars #7C3AED — de dominante laag in deze unit · plaats = turquoise).
Nieuw visueel element: getekende analoge klokjes (MSO_SHAPE.OVAL + twee connectoren
als wijzers) op een eigen «Los relojes»-dia.

VIDEO: voor aflevering 8 bestaat GEEN YouTube-link. De bron is een Google-Drive-
bestand («Spanish Sitcom 8_1080p.mp4», file-id 1zS4KXwLAnG9XrDxH2toHqlNHrGyd9Qv_,
deelrechten reader/anyone). De online-video-embed gebruikt daarom de Drive-
/preview-URL; daarnaast staat er een gewone hyperlink-knop «▶ Abrir en Drive» als
gegarandeerde noodroute (browser). Internet vereist.

Bron: 03-build/web/gen_c4u8_kgt.py · gen_c4u8_pdf.py · gen_c4u8_practica.py ·
gen_c4u8_escucha.py
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
OUT_DOCENTE = os.path.join(HERE, "C4_U8_docente.pptx")
OUT_ALUMNO_PPTX = os.path.join(HERE, "C4_U8_alumno.pptx")
OUT_ALUMNO = os.path.join(HERE, "C4_U8_alumno.ppsx")

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
F_VERB = RGBColor(0xEA, 0x73, 0x17)  # werkwoord          (oranje · U8: quedar/poder/querer)
F_OBJ  = RGBColor(0x1E, 0x9E, 0x74)  # voorwerp           (groen)
F_TIME = RGBColor(0x7C, 0x3A, 0xED)  # TIJD               (paars · dominante laag in U8)
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

def footer(s, tab="U8 · LA HORA", page=None):
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
# C4 · UNIDAD 8 «La hora y los días» — slides (survival). Herbruikt de machinerie.
# ============================================================================
FTAB = "U8 · LA HORA"

def s01_title():
    s = slide(); bg(s)
    rect(s, 0, 0, EMU_W, Inches(4.7), fill=G)
    rect(s, 0, Inches(4.62), EMU_W, Inches(0.08), fill=GD)
    chip(s, Inches(0.6), Inches(0.5), "C4 · LA RUTA · EL DESPEGUE · PARADA 8", fill=WHITE, tcolor=G, size=12)
    text(s, Inches(0.55), Inches(1.15), Inches(12.3), Inches(1.1),
         [[("La hora y los días", {"size": 46, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(0.6), Inches(2.25), Inches(11.8), Inches(0.7),
         [[("¿Qué hora es? ", {"size": 26, "bold": True, "color": WHITE, "font": DISPLAY}),
           ("— Son las ocho y media.", {"size": 17, "italic": True, "color": GT})]])
    text(s, Inches(0.6), Inches(3.2), Inches(11.5), Inches(1.1),
         [[("Zeggen ", {"size": 16, "color": WHITE}), ("hoe laat", {"size": 16, "bold": True, "color": WHITE}),
           (" het is en ", {"size": 16, "color": WHITE}), ("afspreken", {"size": 16, "bold": True, "color": WHITE}),
           (" (es la una · son las ocho · a las doce · el lunes · quedar).", {"size": 16, "color": WHITE})],
          [("Survival in Spanish — Julio telefoneert met «Laura»… en noemt álle uren.", {"size": 13, "italic": True, "color": GT})]])
    # mochila-gids
    avatar(s, "mochila", Inches(10.7), Inches(4.95), d=Inches(1.7))
    text(s, Inches(0.6), Inches(5.25), Inches(9), Inches(1.5),
         [[("En esta unidad vas a…", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})],
          [("• Decir la hora  ", {"size": 13, "color": INK}), ("es la una · son las ocho · y cuarto · y media · menos cuarto · en punto", {"size": 11, "italic": True, "color": MUT})],
          [("• Preguntar ¿a qué hora?  ", {"size": 13, "color": INK}), ("a la una · a las doce = «om…»", {"size": 11, "italic": True, "color": MUT})],
          [("• Los días de la semana  ", {"size": 13, "color": INK}), ("el lunes (op maandag) · los lunes (elke maandag) — kleine letter!", {"size": 11, "italic": True, "color": MUT})],
          [("• Quedar con alguien  ", {"size": 13, "color": INK}), ("¿quieres quedar? · quedamos a las… · ¿dónde quedamos?", {"size": 11, "italic": True, "color": MUT})]])
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
             ("2", "Suena bien", "la d suave · los números", 3),
             ("3", "Los relojes", "¿qué hora es? · de klokjes", 4),
             ("4", "Kit", "la hora · los días · quedar", 5),
             ("5", "Gramática", "es la/son las · a las · el lunes", 7),
             ("6", "Práctica", "oefenen samen", 9),
             ("7", "Hablar", "queda con un compañero", 10),
             ("8", "Cultura", "los horarios en el mundo hispano", 11),
             ("9", "Tarea", "Mi horario", 12),
             ("10", "Repaso", "wat kun je nu?", 14)]
    x0, y0 = Inches(0.55), Inches(1.7)
    w = Inches(3.0); gx = Inches(0.18); gy = Inches(0.2)
    for i, t in enumerate(tiles):
        col = i % 4; row = i // 4
        _tile(s, x0 + col * (w + gx), y0 + row * (Inches(1.15) + gy), w, *t)
    text(s, Inches(0.6), Inches(5.95), Inches(12), Inches(0.9),
         [[("Consejo · Tip. ", {"size": 12, "bold": True, "color": GD, "font": DISPLAY}),
           ("Eén uur is enkelvoud («es la una»), álle andere uren meervoud («son las ocho»). En «half negen» = las ocho y media!", {"size": 12, "italic": True, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

# ── Online-video inbedden zodat hij ÍN PowerPoint afspeelt ────────────────────
# Bron U8 = GOOGLE DRIVE (voor aflevering 8 bestaat géén YouTube-link):
#   «Spanish Sitcom 8_1080p.mp4» · file-id 1zS4KXwLAnG9XrDxH2toHqlNHrGyd9Qv_
#   deelrechten reader/anyone → de /preview-embed is openbaar bereikbaar.
# Dus een ONLINE-video: PowerPoint desktop (2016+/365) probeert hem in-app af te
# spelen via de ingebedde speler (internet vereist). De helper is minimaal
# aangepast: hij aanvaardt nu een VOLLEDIGE URL i.p.v. enkel een YouTube-id; álle
# OOXML-markup blijft identiek (poster-picture + a:hlinkClick action="ppaction://media"
# + a:videoFile r:link + p14:media r:embed). Poster = PIL-render.
from PIL import Image as _Img, ImageDraw as _Dw, ImageFont as _Ft
_VIDEO_REL="http://schemas.openxmlformats.org/officeDocument/2006/relationships/video"
_MEDIA_REL="http://schemas.microsoft.com/office/2007/relationships/media"
_P14="http://schemas.microsoft.com/office/powerpoint/2010/main"
DRIVE_ID="1zS4KXwLAnG9XrDxH2toHqlNHrGyd9Qv_"
VIDEO_URL="https://drive.google.com/file/d/%s/preview"%DRIVE_ID   # embed-URL (in-app speler)
VIDEO_WATCH="https://drive.google.com/file/d/%s/view"%DRIVE_ID    # browser-URL (noodroute)
VIDEO_TOP="Sitcom · Episodio 8"; VIDEO_MAIN="La hora y los días"
VIDEO_POSTER=os.path.join(HERE,"assets","video_poster_U8.png")
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
    dr.text((70,626),"▶ Klik om af te spelen · Spanish Sitcom (Google Drive)",font=_load_font(28,False),fill=(255,255,255))
    im.save(png)
make_video_poster(VIDEO_POSTER,VIDEO_TOP,VIDEO_MAIN)
def add_online_video(s,url,x,y,w,h,poster_png):
    """<url> = de VOLLEDIGE embed-URL (U1–U7: youtube.com/embed/<id> · U8: de
    Drive-/preview-URL). De markup eronder is ongewijzigd t.o.v. U1–U7."""
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
    sectionbar(s, "§1 · ¡ESCUCHA!", "Bekijk la escena y escucha", "Kijk & luister — Julio doet alsof hij met «Laura» telefoneert… en noemt álle uren", num=1)
    card(s, Inches(0.55), Inches(1.55), Inches(7.4), Inches(4.9), fill=WHITE, line=LINE)
    dia = [("Julio", "¿Sí? Laura, ¿cómo estás? ¿Qué? No te oigo nada.", F_SUBJ),
           ("Julio", "¿Esta noche? ¿Quieres quedar esta noche?", F_TIME),
           ("Julio", "Estoy en una fiesta. ¿Puedes hablar más despacio?", F_VERB),
           ("Julio", "Más tarde sí, más tarde puede ser.", F_TIME),
           ("Julio", "Entonces, quedamos en mi casa. ¿A qué hora?", F_VERB),
           ("Julio", "No, a las once no, mejor a las doce.", F_TIME),
           ("Julio", "¿Qué hora es ahora? ¿Las ocho y media?", F_TIME),
           ("Julio", "Ahora mismo no puedo quedar.", F_VERB),
           ("Julio", "Pues no sé, un cine, un restaurante. Es un poco pronto.", F_PLAC),
           ("Julio", "Te veo en veinte minutos. Hasta ahora. Un beso.", F_TIME),
           ("Julio", "Bueno, me voy, es un poco tarde.", F_TIME),
           ("María", "Venga, vámonos… A tomar una cerveza.", F_SUBJ)]
    y = Inches(1.78)
    for sp, tx, col in dia:
        chip(s, Inches(0.75), y, sp, fill=col, tcolor=WHITE, size=10)
        text(s, Inches(1.95), y - Inches(0.02), Inches(5.8), Inches(0.5),
             [[(tx, {"size": 10.5, "color": INK})]])
        y = y + Inches(0.385)
    # chunks-kaart rechts (ingekort om plaats te maken voor de video)
    card(s, Inches(8.2), Inches(1.55), Inches(4.6), Inches(2.45), fill=GT, line=G)
    text(s, Inches(8.45), Inches(1.72), Inches(4.1), Inches(2.2),
         [[("Chunks para llevar 🎒", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})],
          [("¿Qué hora es? · las ocho y media", {"size": 11.5, "color": INK})],
          [("¿A qué hora? · a las once · a las doce", {"size": 11.5, "color": INK})],
          [("¿Quieres quedar? · quedamos en mi casa", {"size": 11.5, "color": INK})],
          [("esta noche · más tarde · ahora mismo", {"size": 11.5, "color": INK})],
          [("No te oigo nada · hasta ahora · un beso", {"size": 11.5, "color": INK})]])
    # echte, afspeelbare video (online-embed met de Drive-/preview-URL) + hyperlink-noodroute
    text(s, Inches(8.2), Inches(4.12), Inches(2.95), Inches(0.3),
         [[("🎬 Episodio 8 — klik om af te spelen", {"size": 11, "bold": True, "color": GD, "font": DISPLAY})]])
    btn, _bw = chip(s, Inches(11.2), Inches(4.09), "▶ Abrir en Drive", fill=G, tcolor=WHITE, size=9.5)
    try:
        btn.click_action.hyperlink.address = VIDEO_WATCH
    except Exception:
        pass
    add_online_video(s, VIDEO_URL, Inches(8.2), Inches(4.45), Inches(4.6), Inches(2.55), VIDEO_POSTER)
    notes(s, "De video van aflevering 8 komt uit GOOGLE DRIVE (er is voor deze aflevering géén YouTube-link): «Spanish Sitcom 8_1080p.mp4», file-id 1zS4KXwLAnG9XrDxH2toHqlNHrGyd9Qv_, deelrechten reader/anyone → INTERNET VEREIST. Klik op de poster om in PowerPoint af te spelen; lukt dat niet, klik dan de knop «▶ Abrir en Drive» (of open de Drive-link zelf in een browser: " + VIDEO_WATCH + ") — dan speelt de video in het browsertabblad. Aanpak: eerst één keer kijken zónder transcript (globaal begrijpen: Julio doet alsof hij telefoneert om María jaloers te maken), daarna met het transcript en de uren laten noteren. Focus: álle tijdaanduidingen (paars) — «¿qué hora es?», «las ocho y media», «a las once», «a las doce», «esta noche», «más tarde», «ahora mismo», «en veinte minutos». Doelcodes: C4-LU-1 · C4-STR-1 · C4-WS-1.")
    footer(s, tab=FTAB, page=pg())

def s04_kit():
    s = slide(); bg(s)
    sectionbar(s, "§2 · KIT", "La hora · los días · los momentos del día", "De tijd zeggen, de dagen van de week & wanneer op de dag", num=2)
    cols = [("¿Qué hora es? 🕐", [("Es la una", "het is één uur"), ("Son las ocho", "het is acht uur"),
              ("y cuarto · y media", "kwart over · half"), ("menos cuarto", "kwart voor"),
              ("en punto", "precies (op het uur)"), ("¿A qué hora?", "hoe laat? (afspraak)")]),
            ("Los días de la semana 📅", [("lunes · martes · miércoles", "ma · di · wo"), ("jueves · viernes", "do · vr"),
              ("sábado · domingo", "za · zo"), ("el fin de semana", "het weekend"),
              ("hoy · mañana", "vandaag · morgen"), ("el lunes · los lunes", "op maandag · elke maandag")]),
            ("Los momentos del día 🌗", [("por la mañana", "'s ochtends"), ("por la tarde", "'s middags/'s avonds"),
              ("por la noche", "'s nachts/laat op de avond"), ("esta noche", "vanavond"),
              ("más tarde · ahora mismo", "later · nu meteen"), ("pronto · tarde", "vroeg · laat")])]
    x = Inches(0.55); w = Inches(4.0)
    for title, items in cols:
        card(s, x, Inches(1.6), w, Inches(4.9), fill=WHITE, line=LINE)
        text(s, x + Inches(0.25), Inches(1.78), w - Inches(0.4), Inches(0.5),
             [[(title, {"size": 13.5, "bold": True, "color": GD, "font": DISPLAY})]])
        y = Inches(2.45)
        for es, nl in items:
            text(s, x + Inches(0.25), y, w - Inches(0.5), Inches(0.6),
                 [[(es, {"size": 13, "bold": True, "color": INK}), ("   " + nl, {"size": 10, "italic": True, "color": MUT})]])
            y = y + Inches(0.65)
        x = x + w + Inches(0.2)
    footer(s, tab=FTAB, page=pg())

def s05_quedar():
    s = slide(); bg(s)
    sectionbar(s, "§2 · KIT", "Quedar & por teléfono", "Afspreken maken & je redden aan de telefoon (zoals Julio)", num=2)
    left = [("¿Quieres quedar?", "wil je afspreken?"), ("¿A qué hora?", "hoe laat?"), ("Quedamos a las siete", "we spreken af om zeven uur"),
            ("¿Dónde quedamos?", "waar spreken we af?"), ("Vale · perfecto", "oké · perfect")]
    right = [("¿Sí?", "ja? (de telefoon opnemen)"), ("No te oigo (nada)", "ik hoor je (helemaal) niet"), ("¿Puedes hablar más despacio?", "kan je langzamer spreken?"),
             ("Hasta ahora", "tot straks"), ("Un beso", "kusje (afscheid)")]
    card(s, Inches(0.55), Inches(1.6), Inches(6.0), Inches(4.9), fill=GT, line=G)
    text(s, Inches(0.8), Inches(1.78), Inches(5.5), Inches(0.5),
         [[("Quedar · afspreken 🤝", {"size": 13.5, "bold": True, "color": GD, "font": DISPLAY})]])
    y = Inches(2.5)
    for es, nl in left:
        text(s, Inches(0.8), y, Inches(5.4), Inches(0.6), [[(es, {"size": 15, "bold": True, "color": INK}), ("   " + nl, {"size": 11, "italic": True, "color": MUT})]])
        y = y + Inches(0.72)
    card(s, Inches(6.8), Inches(1.6), Inches(6.0), Inches(4.9), fill=WHITE, line=LINE)
    text(s, Inches(7.05), Inches(1.78), Inches(5.5), Inches(0.5),
         [[("Por teléfono 📞", {"size": 13.5, "bold": True, "color": GD, "font": DISPLAY})]])
    y = Inches(2.5)
    for es, nl in right:
        text(s, Inches(7.05), y, Inches(5.4), Inches(0.6), [[(es, {"size": 14, "bold": True, "color": INK}), ("   " + nl, {"size": 11, "italic": True, "color": MUT})]])
        y = y + Inches(0.72)
    text(s, Inches(0.8), Inches(5.7), Inches(11.9), Inches(0.7),
         [[("¡Ojo! ", {"size": 12, "bold": True, "color": RED}),
           ("Hasta ahora = «tot straks» (niet «tot nu»!) · quedar = afspreken, niet «blijven» · quedamos a las… mét a.", {"size": 12, "italic": True, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

def s06_gram_hora():
    s = slide(); bg(s)
    sectionbar(s, "§4 · GRAMÁTICA", "¿Qué hora es? — es la una ↔ son las dos", "Eén uur = enkelvoud, alle andere uren = meervoud + y cuarto/y media/menos cuarto", num=4)
    legend_func(s, Inches(0.55), Inches(1.42))
    # es la / son las-kaart (links, breed)
    card(s, Inches(0.55), Inches(1.9), Inches(7.6), Inches(4.1), fill=WHITE, line=LINE)
    text(s, Inches(0.8), Inches(2.05), Inches(7.1), Inches(0.4), [[("es la una  ↔  son las ocho", {"size": 15, "bold": True, "color": GD, "font": DISPLAY})]])
    # twee contrastvlakken (paars = tijd · turquoise-vlak voor het meervoud)
    box1 = rect(s, Inches(0.8), Inches(2.55), Inches(3.4), Inches(1.0), fill=RGBColor(0xED,0xE9,0xFE), line=None, round=True, radius=0.09)
    text(s, Inches(0.95), Inches(2.62), Inches(3.1), Inches(0.9),
         [[("🕐 alleen 1 uur", {"size": 11, "bold": True, "color": RGBColor(0x5B,0x21,0xB6)})],
          [("Es la ", {"size": 15, "bold": True, "color": F_TIME}), ("una.", {"size": 15, "color": INK})],
          [("Es la ", {"size": 13, "bold": True, "color": F_TIME}), ("una y media.", {"size": 13, "color": INK})]])
    box2 = rect(s, Inches(4.5), Inches(2.55), Inches(3.5), Inches(1.0), fill=RGBColor(0xE6,0xF7,0xF5), line=None, round=True, radius=0.09)
    text(s, Inches(4.65), Inches(2.62), Inches(3.2), Inches(0.9),
         [[("🕑 alle andere uren", {"size": 11, "bold": True, "color": RGBColor(0x0B,0x7A,0x73)})],
          [("Son las ", {"size": 15, "bold": True, "color": F_TIME}), ("dos · tres · ocho…", {"size": 15, "color": INK})],
          [("Son las ", {"size": 13, "bold": True, "color": F_TIME}), ("doce en punto.", {"size": 13, "color": INK})]])
    filas = [("Son las tres y cuarto", "3.15", "kwart over drie"),
             ("Son las tres y media", "3.30", "half vier (!)"),
             ("Son las cuatro menos cuarto", "3.45", "kwart voor vier — het vólgende uur"),
             ("Son las tres en punto", "3.00", "precies drie uur")]
    y = Inches(3.75)
    for es, dig, nl in filas:
        text(s, Inches(0.8), y, Inches(7.2), Inches(0.4),
             [[(es + "   ", {"size": 13, "bold": True, "color": F_TIME}), (dig, {"size": 12.5, "bold": True, "color": INK}), ("   " + nl, {"size": 11, "italic": True, "color": MUT})]])
        y = y + Inches(0.44)
    text(s, Inches(0.8), Inches(5.6), Inches(7.1), Inches(0.4),
         [[("💡 ", {"size": 12}), ("Tot :30 → ", {"size": 12, "color": INK}), ("y", {"size": 12, "bold": True, "color": F_TIME}),
           (" (erbij). Daarna → ", {"size": 12, "color": INK}), ("menos", {"size": 12, "bold": True, "color": F_TIME}),
           (" (eraf) mét het vólgende uur.", {"size": 12, "color": INK})]])
    # DE VALSTRIK — eigen, opvallend kader (rechts)
    card(s, Inches(8.4), Inches(1.9), Inches(4.4), Inches(4.1), fill=RGBColor(0xFD,0xE8,0xE8), line=RED, lw=2.4)
    chip(s, Inches(8.6), Inches(1.76), "¡OJO! · LA TRAMPA", fill=RED, tcolor=WHITE, size=10)
    text(s, Inches(8.65), Inches(2.25), Inches(3.9), Inches(0.6),
         [[("«half negen»", {"size": 20, "bold": True, "color": RED, "font": DISPLAY})]])
    text(s, Inches(8.65), Inches(2.85), Inches(3.9), Inches(0.6),
         [[("= las ocho y media", {"size": 19, "bold": True, "color": F_TIME, "font": DISPLAY})],
          [("(8 + 30)", {"size": 13, "bold": True, "color": INK})]])
    text(s, Inches(8.65), Inches(3.85), Inches(3.9), Inches(1.2),
         [[("🇪🇸 Spaans kijkt ", {"size": 12.5, "color": INK}), ("TERUG", {"size": 12.5, "bold": True, "color": F_TIME}),
           (" naar het vórige uur.", {"size": 12.5, "color": INK})],
          [("🇳🇱 Nederlands kijkt ", {"size": 12.5, "color": INK}), ("VOORUIT", {"size": 12.5, "bold": True, "color": RED}),
           (" naar het vólgende.", {"size": 12.5, "color": INK})]])
    text(s, Inches(8.65), Inches(4.95), Inches(3.9), Inches(1.0),
         [[("Dus:", {"size": 12, "bold": True, "color": GD, "font": DISPLAY})],
          [("half tien = ", {"size": 13, "color": INK}), ("las nueve y media", {"size": 13, "bold": True, "color": F_TIME})],
          [("half zeven = ", {"size": 13, "color": INK}), ("las seis y media", {"size": 13, "bold": True, "color": F_TIME})]])
    notes(s, "Functioneel: één uur = enkelvoud (es la una · es la una y media), álle andere uren = meervoud (son las dos/ocho/doce). Tot :30 gebruik je «y» (erbij), vanaf :31 «menos» mét het VOLGENDE uur (3.45 = son las cuatro menos cuarto). DE KERNVALSTRIK voor Nederlandstaligen: «half negen» = las ocho y media — het Spaans kijkt terug naar het vórige uur (8 + 30), het Nederlands vooruit (negen). Laat leerlingen dit hardop oefenen met de klokjes-dia. Kleurcode: tijd = paars (§13). Doelcodes: C4-WS-1 · C4-TS-3 · C4-SP-1.")
    footer(s, tab=FTAB, page=pg())

def s07_gram_aque():
    s = slide(); bg(s)
    sectionbar(s, "§4 · GRAMÁTICA", "¿A qué hora? · el lunes ↔ los lunes", "«Om…» met a las + de dagen met een lidwoord (géén «en», kleine letter)", num=4)
    # ¿a qué hora?-kaart
    card(s, Inches(0.55), Inches(1.65), Inches(7.6), Inches(2.5), fill=WHITE, line=LINE)
    text(s, Inches(0.8), Inches(1.8), Inches(7.1), Inches(0.4), [[("¿A qué hora? — a la una · a las doce", {"size": 15, "bold": True, "color": GD, "font": DISPLAY})]])
    filas = [("Son las ocho.", "Het IS 8 u.", "(hoe laat het nú is)"),
             ("A las ocho.", "OM 8 u.", "(wanneer iets gebeurt)"),
             ("¿A qué hora quedamos?", "Hoe laat spreken we af?", "— A la una y media.")]
    y = Inches(2.35)
    for p, nl, ex in filas:
        text(s, Inches(0.8), y, Inches(7.2), Inches(0.4),
             [[(p + "  ", {"size": 13.5, "bold": True, "color": F_TIME}), (nl, {"size": 12.5, "color": INK}), ("   " + ex, {"size": 11, "italic": True, "color": MUT})]])
        y = y + Inches(0.52)
    text(s, Inches(0.8), Inches(3.85), Inches(7.1), Inches(0.3),
         [[("a la ", {"size": 12, "bold": True, "color": F_TIME}), ("una  ·  ", {"size": 12, "color": INK}),
           ("a las ", {"size": 12, "bold": True, "color": F_TIME}), ("dos · a las doce  →  «om…»", {"size": 12, "color": INK})]])
    # el lunes / los lunes-kaart
    card(s, Inches(8.4), Inches(1.65), Inches(4.4), Inches(2.5), fill=GT, line=G)
    text(s, Inches(8.65), Inches(1.8), Inches(3.9), Inches(0.4), [[("el lunes ↔ los lunes", {"size": 15, "bold": True, "color": GD, "font": DISPLAY})]])
    text(s, Inches(8.65), Inches(2.32), Inches(3.9), Inches(1.3),
         [[("el ", {"size": 14, "bold": True, "color": F_PLAC}), ("lunes ", {"size": 14, "bold": True, "color": INK}), ("op maandag", {"size": 11, "italic": True, "color": MUT})],
          [("los ", {"size": 14, "bold": True, "color": F_PLAC}), ("lunes ", {"size": 14, "bold": True, "color": INK}), ("elke maandag", {"size": 11, "italic": True, "color": MUT})],
          [("El lunes quedamos a las seis.", {"size": 11.5, "italic": True, "color": MUT})]])
    text(s, Inches(8.65), Inches(3.62), Inches(3.9), Inches(0.5),
         [[("¡Ojo! ", {"size": 11.5, "bold": True, "color": RED}),
           ("géén «en lunes» · kleine letter: lunes, martes…", {"size": 11.5, "italic": True, "color": INK})]])
    # mini-quiz met reveal
    card(s, Inches(0.55), Inches(4.35), Inches(12.25), Inches(1.7), fill=GT, line=G)
    text(s, Inches(0.8), Inches(4.5), Inches(11.7), Inches(0.5),
         [[("Completa · vul aan (klik voor de oplossing): ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("___ una y cuarto.   ___ siete.   Quedamos ___ nueve.", {"size": 13, "color": INK})]])
    exercise_solucion(s, Inches(0.8), Inches(5.15), Inches(11.7), Inches(0.7),
        [[("Es la · Son las · a las", {"bold": True, "color": GD, "size": 13})]])
    noodroute(s)
    notes(s, "Functioneel contrast: «son las ocho» = het IS 8 u (hoe laat het nú is) ↔ «a las ocho» = OM 8 u (wanneer iets gebeurt, dus bij een afspraak). Enkelvoud blijft ook hier: a LA una. Dagen: el lunes = op (deze) maandag ↔ los lunes = elke maandag; NOOIT «en lunes» (typische NL-transfer) en dagen krijgen in het Spaans een kleine letter. «quedamos» en «quieres» blijven CHUNKS — géén vervoegingsparadigma van quedar/querer aanleren; het werkwoordsysteem komt in het 5de jaar (C5). Oplossing: Es la · Son las · a las.")
    footer(s, tab=FTAB, page=pg())

def s08_practica():
    s = slide(); bg(s)
    sectionbar(s, "§3 · PRÁCTICA", "Completa el diálogo", "Vul samen aan — klik voor de oplossing", num=3)
    card(s, Inches(0.55), Inches(1.7), Inches(7.6), Inches(4.5), fill=WHITE, line=LINE)
    lines = [("— ¿Quieres ___ esta noche?", "quedar"),
             ("— Sí, vale. ¿A qué ___?", "hora"),
             ("— ¿A ___ nueve?", "las"),
             ("— Mejor a las nueve y ___.  (9.30)", "media"),
             ("— Perfecto. ¡Hasta ___!", "ahora")]
    y = Inches(1.95)
    for q, _a in lines:
        text(s, Inches(0.8), y, Inches(7.1), Inches(0.6), [[(q, {"size": 16, "color": INK})]])
        y = y + Inches(0.8)
    exercise_solucion(s, Inches(8.4), Inches(1.9), Inches(4.4), Inches(4.0),
        [[("1. quedar", {"color": GD, "size": 14})], [("2. hora", {"color": GD, "size": 14})],
         [("3. las", {"color": GD, "size": 14})], [("4. media", {"color": GD, "size": 14})],
         [("5. ahora", {"color": GD, "size": 14})]],
        title_doc="SOLUCIÓN · docent")
    noodroute(s)
    notes(s, "Laat leerlingen eerst zelf proberen (in duo, hardop). Klik daarna de oplossing open. Let op: «¿quieres quedar?» = de vaste uitnodiging (chunk); «¿a qué hora?» = hoe laat (afspraak); «a las nueve» mét a; «y media» = +30 (9.30 = las nueve y media, NIET «half tien» vertalen als «nueve y media» denken vanuit het NL — het cijfer blijft 9); «hasta ahora» = tot straks. Oplossing: quedar · hora · las · media · ahora.")
    footer(s, tab=FTAB, page=pg())

def s09_speaking():
    s = slide(); bg(s)
    sectionbar(s, "§3 · HABLAR", "Queda con un compañero", "Maak samen een afspraak: dag + uur + plaats — sin leer", num=3)
    card(s, Inches(0.55), Inches(1.7), Inches(7.6), Inches(3.4), fill=GT, line=G)
    text(s, Inches(0.85), Inches(1.95), Inches(7.1), Inches(3.0),
         [[("Modelo · zeg dit hardop:", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})],
          [("«— ¿Quieres quedar el sábado?", {"size": 17, "color": INK})],
          [("— ¿A qué hora?", {"size": 17, "color": INK})],
          [("— Quedamos a las once y media en el centro.", {"size": 17, "color": INK})],
          [("— ¡Vale, hasta el sábado!»", {"size": 17, "color": INK})]])
    card(s, Inches(8.4), Inches(1.7), Inches(4.4), Inches(3.4), fill=WHITE, line=LINE)
    text(s, Inches(8.65), Inches(1.95), Inches(3.9), Inches(3.0),
         [[("¿Cómo? · Werkvorm", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})],
          [("1. Kies een dag: el lunes… el sábado.", {"size": 13, "color": INK})],
          [("2. Stel een uur voor: «¿a las siete?».", {"size": 13, "color": INK})],
          [("3. Onderhandel: «mejor a las ocho y media».", {"size": 13, "color": INK})],
          [("4. Spreek de plaats af: «en el centro».", {"size": 13, "color": INK})],
          [("5. Bevestig: «vale · perfecto · hasta…».", {"size": 13, "color": INK})]])
    text(s, Inches(0.6), Inches(5.4), Inches(12), Inches(0.7),
         [[("Interactie ", {"size": 12, "bold": True, "color": GD, "font": DISPLAY}),
           ("= voorstellen, onderhandelen en bevestigen. Hoor je het uur niet? Zeg: «¿Cómo? / ¿Puedes hablar más despacio?»", {"size": 12, "italic": True, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

def s10_musica():
    s = slide(); bg(s)
    sectionbar(s, "CULTURA", "Los horarios en el mundo hispano", "De klok tikt anders in de Spaanstalige wereld + muziek die jullie kennen", num=None)
    bandas = [("Quevedo", "Bzrp #52", "🇪🇸 España"), ("Rosalía", "Despechá", "🇪🇸 España"),
              ("Manuel Turizo", "La Bachata", "🇨🇴 Colombia"), ("Marc Anthony", "Vivir Mi Vida", "🇵🇷 P. Rico"),
              ("Álvaro Soler", "Sofía", "🇪🇸 España"), ("Camilo", "Vida de Rico", "🇨🇴 Colombia")]
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
         [[("🕐 Los horarios en el mundo hispano ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("In España eet men warm rond ", {"size": 12, "color": INK}), ("las dos (14 u)", {"size": 12, "bold": True, "color": F_TIME}),
           (" en avondmaal pas om ", {"size": 12, "color": INK}), ("las nueve o las diez (21–22 u)", {"size": 12, "bold": True, "color": F_TIME}),
           (". In México is de lunch (14–15 u) de hoofdmaaltijd. De ", {"size": 12, "color": INK}),
           ("tarde", {"size": 12, "bold": True, "color": GD}), (" duurt tot 20–21 u — daarom zeg je om 19 u nog «buenas tardes».", {"size": 12, "color": INK})],
          [("En de dagen? Altijd met een ", {"size": 12, "color": INK}), ("kleine letter", {"size": 12, "bold": True, "color": RED}),
           (": lunes, martes, sábado… Playlist + LyricsTraining op de digitale hub → tabblad Música.", {"size": 12, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

def s11_tarea():
    s = slide(); bg(s)
    sectionbar(s, "§5 · TAREA FINAL", "Mi horario", "Vul je weekschema in (4 dagen) en maak samen een afspraak", num=5)
    # FICHA · mini-weekschema met invulkolommen
    card(s, Inches(0.55), Inches(1.7), Inches(6.6), Inches(3.6), fill=WHITE, line=G, lw=1.6)
    rect(s, Inches(0.55), Inches(1.7), Inches(6.6), Inches(0.55), fill=G)
    text(s, Inches(0.75), Inches(1.78), Inches(6.2), Inches(0.4), [[("MI HORARIO · Academia «Bienvenidos al español»", {"size": 12, "bold": True, "color": WHITE, "font": DISPLAY})]])
    dias = ["el lunes", "el miércoles", "el viernes", "el sábado"]
    cw = Inches(1.55); cx = Inches(0.68)
    for d in dias:
        rect(s, cx, Inches(2.42), cw, Inches(0.38), fill=GT, line=LINE, lw=1.0, round=True, radius=0.14)
        text(s, cx, Inches(2.44), cw, Inches(0.34),
             [[(d, {"size": 11, "bold": True, "color": GD, "font": DISPLAY})]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        rect(s, cx, Inches(2.88), cw, Inches(1.35), fill=PAPER, line=LINE, lw=1.0, round=True, radius=0.06)
        text(s, cx + Inches(0.07), Inches(2.95), cw - Inches(0.14), Inches(1.2),
             [[("a las ______", {"size": 10.5, "color": MUT})], [("", {"size": 5})],
              [("_____________", {"size": 10.5, "color": LINE})], [("_____________", {"size": 10.5, "color": LINE})]])
        cx = cx + cw + Inches(0.13)
    text(s, Inches(0.75), Inches(4.35), Inches(6.2), Inches(0.85),
         [[("🤝 Mi cita: ¿Quieres quedar ", {"size": 12.5, "bold": True, "color": INK}), ("el ______ ", {"size": 12.5, "color": LINE}),
           ("? Quedamos ", {"size": 12.5, "bold": True, "color": INK}), ("a las ______ ", {"size": 12.5, "color": LINE}),
           ("en ", {"size": 12.5, "bold": True, "color": INK}), ("__________ .", {"size": 12.5, "color": LINE})],
          [("Zeg elk uur hardop — let op «es la una» ↔ «son las…».", {"size": 10.5, "italic": True, "color": MUT})]])
    # pasos
    card(s, Inches(7.4), Inches(1.7), Inches(5.4), Inches(3.6), fill=GT, line=G)
    text(s, Inches(7.65), Inches(1.9), Inches(4.9), Inches(3.2),
         [[("Los pasos · stappen", {"size": 14, "bold": True, "color": GD, "font": DISPLAY})],
          [("1. Rellena tu horario: 4 dagen, per dag één activiteit met «el + dag» + «a las + uur».", {"size": 12.5, "color": INK})],
          [("2. Di la hora en voz alta: zeg elk uur hardop (es la una ↔ son las…).", {"size": 12.5, "color": INK})],
          [("3. Queda con un compañero: zoek een moment waarop jullie béíden vrij zijn.", {"size": 12.5, "color": INK})],
          [("4. Presenta: vertel je week + jullie afspraak aan de klas — sin leer.", {"size": 12.5, "color": INK})]])
    text(s, Inches(0.6), Inches(5.45), Inches(7.6), Inches(1.0),
         [[("🏁 Klaar als… ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("je 4 momenten zegt met «el + dag» én «a las + uur» (juiste es la/son las), en samen een afspraak maakt met «¿quieres quedar?» — zónder af te lezen.", {"size": 12, "color": INK})]])
    card(s, Inches(8.4), Inches(5.42), Inches(4.4), Inches(1.05), fill=WHITE, line=LINE)
    text(s, Inches(8.6), Inches(5.5), Inches(4.0), Inches(0.9),
         [[("Evaluatie · 🟢🟡🔴", {"size": 11.5, "bold": True, "color": GD, "font": DISPLAY})],
          [("· la hora correct (es la/son las · y media)", {"size": 10.5, "color": INK})],
          [("· el + día en a las + hora correct", {"size": 10.5, "color": INK})],
          [("· quedar (afspraak maken) & durf", {"size": 10.5, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

def s12_repaso():
    s = slide(); bg(s)
    sectionbar(s, "REPASO", "Lo esencial de un vistazo", "Wat je nu kunt — semáforo", num=None)
    card(s, Inches(0.55), Inches(1.7), Inches(7.6), Inches(3.3), fill=WHITE, line=LINE)
    text(s, Inches(0.85), Inches(1.85), Inches(7.1), Inches(3.1),
         [[("Zo zeg je hoe laat het is", {"size": 14, "bold": True, "color": GD, "font": DISPLAY})],
          [("¿Qué hora es? — Es la una · Son las ocho", {"size": 13.5, "color": INK})],
          [("y cuarto · y media · menos cuarto · en punto", {"size": 13, "color": INK})],
          [("alleen 1 uur = enkelvoud · tot :30 «y», daarna «menos» + volgend uur", {"size": 12, "italic": True, "color": MUT})],
          [("", {"size": 6})],
          [("Zo maak je een afspraak", {"size": 14, "bold": True, "color": GD, "font": DISPLAY})],
          [("¿Quieres quedar el sábado? — ¿A qué hora? — Quedamos a las siete.", {"size": 13, "color": INK})],
          [("a las + uur = «om…» · el lunes (op maandag) · los lunes (elke maandag)", {"size": 13, "color": INK})],
          [("géén «en lunes» · dagen met een kleine letter · hasta ahora = tot straks", {"size": 12, "italic": True, "color": MUT})]])
    # de valstrik keert terug (§13: spreiding & recycling)
    card(s, Inches(0.55), Inches(5.15), Inches(7.6), Inches(1.0), fill=RGBColor(0xFD,0xE8,0xE8), line=RED, lw=2.0)
    text(s, Inches(0.85), Inches(5.25), Inches(7.1), Inches(0.85),
         [[("¡Ojo! · de valstrik ", {"size": 12.5, "bold": True, "color": RED, "font": DISPLAY}),
           ("«half negen» = ", {"size": 12.5, "color": INK}), ("las ocho y media", {"size": 13, "bold": True, "color": F_TIME}), (" (8 + 30).", {"size": 12.5, "color": INK})],
          [("Spaans kijkt TERUG naar het vórige uur, Nederlands VOORUIT → half tien = las nueve y media.", {"size": 11.5, "italic": True, "color": INK})]])
    card(s, Inches(8.4), Inches(1.7), Inches(4.4), Inches(4.45), fill=GT, line=G)
    text(s, Inches(8.65), Inches(1.9), Inches(3.9), Inches(0.5), [[("Puedo… · Ik kan…", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    items = ["de tijd zeggen (es la una · son las ocho)", "y cuarto · y media · menos cuarto gebruiken",
             "«half negen» juist zeggen (las ocho y media)", "¿a qué hora? · a las doce gebruiken",
             "de dagen zeggen (el lunes · los lunes)", "een afspraak maken (¿quieres quedar?)"]
    y = Inches(2.5)
    for it in items:
        text(s, Inches(8.65), y, Inches(3.9), Inches(0.7), [[("🟢🟡🔴  ", {"size": 12}), (it, {"size": 11, "color": INK})]])
        y = y + Inches(0.55)
    text(s, Inches(8.65), Inches(5.65), Inches(3.9), Inches(0.7), [[("🎮 Repasa jugando", {"size": 12, "bold": True, "color": GD, "font": DISPLAY})], [("online op de hub · los relojes · quedar", {"size": 11, "italic": True, "color": MUT})]])
    footer(s, tab=FTAB, page=pg())

def s13_teacher():
    s = slide(); bg(s, color=RGBColor(0x24,0x1C,0x1B))
    text(s, Inches(0.6), Inches(0.5), Inches(12), Inches(0.7), [[("Docentendossier · Unidad 8 «La hora y los días»", {"size": 22, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(0.6), Inches(1.3), Inches(12.1), Inches(5.6),
         [[("Timing (2 lesuren van 50 min).", {"size": 14, "bold": True, "color": RGBColor(0xFB,0xEA,0xEC), "font": DISPLAY})],
          [("Les 1: Escucha (sitcom ep. 8 «Las horas» — Julio doet op een feestje alsof hij met «Laura» telefoneert om María jaloers te maken en noemt daarbij álle uren: a las once, a las doce, las ocho y media…) + Suena bien (la d suave tussen klinkers ↔ la d inicial + de klemtoon in getallen) + Los relojes + Kit (la hora · los días · los momentos del día · quedar · por teléfono). Les 2: gramática functioneel (es la una ↔ son las… + y cuarto/y media/menos cuarto/en punto · ¿a qué hora? · el lunes ↔ los lunes), práctica, hablar «Queda con un compañero», tarea «Mi horario» + cultura.", {"size": 12, "color": RGBColor(0xEC,0xEA,0xE3)})],
          [("", {"size": 5})],
          [("VIDEO = GOOGLE DRIVE (geen YouTube voor deze aflevering).", {"size": 14, "bold": True, "color": RGBColor(0xFB,0xEA,0xEC), "font": DISPLAY})],
          [("«Spanish Sitcom 8_1080p.mp4», file-id 1zS4KXwLAnG9XrDxH2toHqlNHrGyd9Qv_ (deelrechten reader/anyone). INTERNET VEREIST. In de escucha-dia klik je op de poster om in PowerPoint af te spelen; lukt dat niet, gebruik de knop «▶ Abrir en Drive» of open " + VIDEO_WATCH + " zelf in een browser. Test de verbinding vóór de les.", {"size": 12, "color": RGBColor(0xEC,0xEA,0xE3)})],
          [("", {"size": 5})],
          [("Aanpak C4 (survival).", {"size": 14, "bold": True, "color": RGBColor(0xFB,0xEA,0xEC), "font": DISPLAY})],
          [("Chunks komen auditief binnen (luisteren → naspreken). «quedamos», «quieres quedar», «puedes hablar» presenteren als CHUNKS uit de scène — géén vervoegingsparadigma van quedar/querer/poder; het volledige werkwoordsysteem komt in het 5de jaar (C5). DE KERNVALSTRIK: «half negen» = las ocho y media (8 + 30) — het Spaans kijkt terug naar het vórige uur, het Nederlands vooruit; laat leerlingen dit hardop drillen met de klokjes. Andere valstrikken: alleen 1 uur is enkelvoud (es la una · a la una); tot :30 «y», daarna «menos» mét het VOLGENDE uur; «son las ocho» (het IS 8 u) ↔ «a las ocho» (OM 8 u); el lunes / los lunes zonder «en» en met een kleine letter; hasta ahora = tot straks. Uitspraak: d suave tussen klinkers (na-da, me-dia, sá-ba-do ≈ Engelse «th» in this) ↔ d inicial steviger (día, doce, domingo); accent in getallen: dieciSÉIS · veintiDÓS (mét tilde) ↔ caTORce · cuaRENta (zonder). Doelcodes: C4-WS-1 · C4-TS-3 · C4-SP-1 · C4-LU-1 · C4-GE-3 · C4-STR-1 · C4-MEC-1/2 · C4-CU-1.", {"size": 12, "color": RGBColor(0xEC,0xEA,0xE3)})],
          [("", {"size": 5})],
          [("Evaluatie.", {"size": 14, "bold": True, "color": RGBColor(0xFB,0xEA,0xEC), "font": DISPLAY})],
          [("Mondelinge mini-taak «Mi horario»: weekschema van 4 dagen (el + dag + a las + uur) presenteren en samen één afspraak maken. Geen leerplan → focus op «kunnen gebruiken in de praktijk». Rubric: la hora correct (es la/son las · y media) · el + día en a las + hora correct · quedar (afspraak maken) & durf.", {"size": 12, "color": RGBColor(0xEC,0xEA,0xE3)})],
          [("", {"size": 5})],
          [("Oplossingen staan bij elke oefendia in de presenter-notities; antwoorden verschijnen bij klik.", {"size": 11, "italic": True, "color": RGBColor(0xA6,0xA2,0x9A)})]])
    footer(s, tab=FTAB, page=pg())

def s_uitspraak():
    s = slide(); bg(s)
    sectionbar(s, "SUENA BIEN", "La d suave ↔ la d inicial · el acento en los números", "De zachte d tussen klinkers & waar de klemtoon valt bij getallen", num=None)
    # d suave-kaart
    card(s,Inches(0.55),Inches(1.6),Inches(6.05),Inches(2.15),fill=WHITE,line=LINE)
    rect(s,Inches(0.55),Inches(1.6),Inches(6.05),Inches(0.14),fill=G)
    text(s,Inches(0.8),Inches(1.85),Inches(5.6),Inches(0.4),[[("① La d suave · tussen klinkers",{"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
    text(s,Inches(0.8),Inches(2.35),Inches(5.6),Inches(1.3),
         [[("na·da · ca·da · me·dia · sá·ba·do · que·dar · adiós",{"size":14.5,"bold":True,"color":INK})],
          [("Tussen klinkers is de d héél zacht — bijna als de Engelse «th» in this.",{"size":11,"italic":True,"color":MUT})]])
    # d inicial-kaart
    card(s,Inches(6.75),Inches(1.6),Inches(6.05),Inches(2.15),fill=WHITE,line=LINE)
    rect(s,Inches(6.75),Inches(1.6),Inches(6.05),Inches(0.14),fill=G)
    text(s,Inches(7.0),Inches(1.85),Inches(5.6),Inches(0.4),[[("② La d inicial · steviger",{"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
    text(s,Inches(7.0),Inches(2.35),Inches(5.6),Inches(1.3),
         [[("día · dos · doce · domingo · después · despacio",{"size":14.5,"bold":True,"color":INK})],
          [("Aan het begin van een woord is de d stevig (zoals in het Nederlands).",{"size":11,"italic":True,"color":MUT})]])
    card(s,Inches(0.55),Inches(3.9),Inches(12.25),Inches(0.85),fill=GT,line=G)
    text(s,Inches(0.85),Inches(4.05),Inches(11.7),Inches(0.6),
         [[("¡Ojo! ",{"size":13,"bold":True,"color":RED,"font":DISPLAY}),("Zeg «me",{"size":13,"color":INK}),("d",{"size":13,"bold":True,"color":GD}),("ia» héél zacht — niet als de harde NL «d» in «medisch». Vergelijk: ",{"size":13,"color":INK}),("d",{"size":13,"bold":True,"color":GD}),("oce (stevig)  ↔  na",{"size":13,"color":INK}),("d",{"size":13,"bold":True,"color":GD}),("a (zacht).",{"size":13,"color":INK})]])
    text(s,Inches(0.6),Inches(5.0),Inches(12),Inches(0.4),[[("③ El acento en los números · mét of zónder tilde? (helpt je de uren correct zeggen)",{"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
    text(s,Inches(0.6),Inches(5.55),Inches(12.2),Inches(0.7),
         [[("die·ci·",{}),("SÉIS",{"color":G,"bold":True}),("      vein·ti·",{}),("DÓS",{"color":G,"bold":True}),("      ↔      ca·",{}),("TOR",{"color":F_TIME,"bold":True}),("·ce      cua·",{}),("REN",{"color":F_TIME,"bold":True}),("·ta",{})]],size=20,font=DISPLAY)
    text(s,Inches(0.6),Inches(6.28),Inches(12.2),Inches(0.5),
         [[("Klemtoon op de láátste lettergreep → tilde (dieciséis, veintidós, veintitrés) · klemtoon op de voorlaatste → géén tilde (catorce, cuarenta, treinta).",{"size":11,"color":INK})],
          [("🔊 Oefen de klanken online op de hub (tabblad Kit · Suena bien).",{"size":11,"italic":True,"color":MUT})]])
    footer(s, tab=FTAB, page=pg())

# ── NIEUW in U8: getekende analoge klokjes (OVAL + twee connectoren als wijzers) ──
def _clock(s, cx, cy, r, h, m, hand_hour=INK, hand_min=G, face=WHITE, ring=LINE, ringw=1.6):
    """Tekent één analoge klok. Wijzerhoeken (identiek aan gen_c4u8_kgt.py /
    gen_c4u8_pdf.py): uurwijzer = (h%12)*30 + m*0.5 graden · minuutwijzer = m*6 graden,
    gemeten vanaf 12 uur, met de klok mee."""
    dial = s.shapes.add_shape(MSO_SHAPE.OVAL, cx - r, cy - r, 2 * r, 2 * r)
    _set_fill(dial, face); _set_line(dial, ring, ringw); dial.shadow.inherit = False
    # uur-/minuutstreepjes op 12·3·6·9 (grijswaarden-veilig oriëntatiepunt)
    for a in (0, 90, 180, 270):
        rad = math.radians(a)
        x1 = cx + int((r * 0.80) * math.sin(rad)); y1 = cy - int((r * 0.80) * math.cos(rad))
        x2 = cx + int((r * 0.94) * math.sin(rad)); y2 = cy - int((r * 0.94) * math.cos(rad))
        tick = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, x1, y1, x2, y2)
        tick.line.color.rgb = LINE; tick.line.width = Pt(1.4)
    def hand(ang_deg, length, color, width):
        rad = math.radians(ang_deg)
        x2 = cx + int(length * math.sin(rad)); y2 = cy - int(length * math.cos(rad))
        ln = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, cx, cy, x2, y2)
        ln.line.color.rgb = color; ln.line.width = Pt(width)
        return ln
    hand(m * 6, r * 0.74, hand_min, 2.4)                     # minuutwijzer (lang, unitkleur)
    hand((h % 12) * 30 + m * 0.5, r * 0.52, hand_hour, 3.6)  # uurwijzer (kort, dik)
    pin = s.shapes.add_shape(MSO_SHAPE.OVAL, cx - Inches(0.045), cy - Inches(0.045), Inches(0.09), Inches(0.09))
    _set_fill(pin, GD); _set_line(pin, None); pin.shadow.inherit = False
    return dial

def s_relojes():
    s = slide(); bg(s)
    sectionbar(s, "§4 · LOS RELOJES", "¿Qué hora es? — mira los relojes", "Lees de klok in het Spaans — let goed op «y media»!", num=4)
    relojes = [(1, 0, "1.00", "Es la una", False),
               (3, 15, "3.15", "Son las tres y cuarto", False),
               (8, 30, "8.30", "Son las ocho y media", True),
               (6, 45, "6.45", "Son las siete menos cuarto", False),
               (12, 0, "12.00", "Son las doce en punto", False),
               (9, 10, "9.10", "Son las nueve y diez", False)]
    x = Inches(0.55); cw = Inches(1.95); gap = Inches(0.1); ytop = Inches(1.66)
    for h, m, dig, lab, trap in relojes:
        card(s, x, ytop, cw, Inches(2.95),
             fill=(RGBColor(0xFD,0xE8,0xE8) if trap else WHITE),
             line=(RED if trap else LINE), lw=(2.2 if trap else 1.2))
        _clock(s, x + cw // 2, ytop + Inches(0.86), Inches(0.62), h, m,
               face=(WHITE if not trap else WHITE), ring=(RED if trap else LINE), ringw=(2.0 if trap else 1.6))
        text(s, x, ytop + Inches(1.62), cw, Inches(0.32),
             [[(dig, {"size": 15, "bold": True, "color": GD, "font": DISPLAY})]],
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(0.08), ytop + Inches(1.98), cw - Inches(0.16), Inches(0.85),
             [[(lab, {"size": 11, "bold": True, "color": (RED if trap else F_TIME), "font": DISPLAY})]],
             align=PP_ALIGN.CENTER)
        if trap:
            chip(s, x + Inches(0.12), ytop - Inches(0.15), "¡OJO! half negen", fill=RED, tcolor=WHITE, size=8.5, w=cw - Inches(0.24))
        x = x + cw + gap
    # regel-strip
    card(s, Inches(0.55), Inches(4.75), Inches(12.25), Inches(0.72), fill=GT, line=G)
    text(s, Inches(0.85), Inches(4.85), Inches(11.7), Inches(0.55),
         [[("Cómo funciona · ", {"size": 12.5, "bold": True, "color": GD, "font": DISPLAY}),
           ("tot :30 → ", {"size": 12.5, "color": INK}), ("y", {"size": 13, "bold": True, "color": F_TIME}),
           (" cuarto / media (erbij)   ·   vanaf :31 → ", {"size": 12.5, "color": INK}),
           ("menos", {"size": 13, "bold": True, "color": F_TIME}),
           (" cuarto mét het VÓLGENDE uur (6.45 = son las siete menos cuarto)   ·   exact op het uur → ", {"size": 12.5, "color": INK}),
           ("en punto", {"size": 13, "bold": True, "color": F_TIME}), (".", {"size": 12.5, "color": INK})]])
    # mini-oefening met reveal
    text(s, Inches(0.6), Inches(5.62), Inches(12.2), Inches(0.4),
         [[("Di la hora · zeg hardop (klik voor de oplossing): ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("2.30  ·  5.45  ·  1.15  ·  9.00", {"size": 15, "bold": True, "color": INK})]])
    exercise_solucion(s, Inches(0.8), Inches(6.05), Inches(11.7), Inches(0.5),
        [[("son las dos y media · son las seis menos cuarto · es la una y cuarto · son las nueve en punto",
           {"bold": True, "color": GD, "size": 12.5})]])
    noodroute(s)
    notes(s, "Werkvorm: wijs een klok aan, de klas zegt de tijd in koor (choral drill), daarna individueel. Laat de klok van 8.30 apart terugkeren — dat is DE valstrik («half negen» = las ocho y media). Wijzerhoeken identiek aan de print/HTML-versie: uurwijzer (h%12)*30 + m*0.5 graden, minuutwijzer m*6 graden. Grijswaarden-veilig: naast de klok staat altijd ook de digitale tijd. Oplossing: 2.30 = son las dos y media · 5.45 = son las seis menos cuarto · 1.15 = es la una y cuarto · 9.00 = son las nueve en punto. Doelcodes: C4-WS-1 · C4-SP-1 · C4-MEC-2.")
    footer(s, tab=FTAB, page=pg())

# ── Funciones-comunicativas-dia (matrix C) — leest de gedeelde funciones_data ──
import sys as _sys
_sys.path.insert(0, os.path.join(os.path.dirname(HERE), "web"))
import funciones_data as FD
FUNC_UNIT = 8

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
    # adaptieve rijhoogte: bij 18 funciones (U8, incl. de nieuwe F17/F18) mag geen
    # rij van de dia vallen → pitch schaalt met het aantal rijen (blijft ≤ 1.32);
    # bij veel funciones zakken ook de binnenmarge én de fontgrootte van de
    # exponentes-regel mee (en wordt die regel op een «·»-grens ingekort).
    nrows = (len(fs) + 1) // 2
    top = 1.82; bottom = 7.0
    pitch = min(1.32, (bottom - top) / nrows)
    ch = pitch - (0.16 if pitch > 0.80 else 0.10)
    off = 0.05 if pitch > 0.80 else 0.03
    tsz = 11 if have <= 16 else 10.5
    exsz = 8.5 if have <= 14 else (7.0 if have <= 16 else 6.3)
    excap = 300 if have <= 16 else 235
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
    # 0 título · 1 menú · 2 escucha · 3 suena bien · 4 relojes · 5 kit · 6 quedar ·
    # 7 gram hora · 8 gram ¿a qué hora? · 9 práctica · 10 hablar · 11 cultura ·
    # 12 tarea · 13 funciones · 14 repaso · (15 docentendossier)
    s01_title(); s02_menu(); s03_escucha(); s_uitspraak(); s_relojes()
    s04_kit(); s05_quedar(); s06_gram_hora()
    s07_gram_aque(); s08_practica(); s09_speaking()
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
