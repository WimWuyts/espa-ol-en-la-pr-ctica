#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_c4u10_ppt.py — Interactieve PowerPoint C4 · Unidad 10 «Las tareas de casa»
================================================================================
Gedeelde builder (één bron) → TWEE decks:
  · C4_U10_docente.pptx  — docentversie: vrije navigatie; antwoorden verschijnen bij
    klik (fade) + volledige oplossing & didactiek in de spreker-notities.
  · C4_U10_alumno.ppsx   — leerlingversie: GEEN docentnotities, GEEN kiosk; gewone
    diavoorstelling waarin de antwoorden/oplossingen bij klik verschijnen.

ECHTE interactiviteit: op elke oefendia wordt <p:timing>-XML geïnjecteerd met
standaard SEQUENTIËLE on-click entrance-animaties (fade-in) in de hoofdsequentie
(mainSeq): elke klik onthult de volgende reveal-shape. + hyperlink-navigatie
(menutegels, ⌂ Menú). Cast-avatars = de ECHTE flat-vector SVG's.

Thema U10: Las tareas de casa · el léxico van de huistaken (limpiar el polvo ·
pasar la aspiradora · fregar los platos · ordenar los armarios · hacer la cama ·
planchar · cocinar) · «hay que + infinitivo» (het moet gebeuren, zónder persoon)
tegenover «tengo/tienes que + infinitivo» (ík/jíj moet) · «saber + infinitivo»
(iets kúnnen omdat je het geleerd hebt) tegenover «poder + infinitivo» (het
lukt/mag nu) · hulp aanbieden, afwijzen en om instructies vragen (yo te ayudo ·
¿te ayudo? · no es molestia · no tienes que molestarte · ¿qué tengo que hacer?).
Eindtaak «¿Quién hace qué?» — een cuadro de tareas.
Huisstijl: unitkleur rood #D64550 (C4). Spaans-eerst + NL-steun. Twee kleurlagen:
cursusrood (navigatie) + functionele taalsemantiek (persoon = blauw · WERKWOORD =
oranje #EA7317 — de dominante laag in deze unit · plaats = turquoise · rood =
valstrik/ontkenning). Visueel element: «La máquina de frases» met DRIE rijen
([Hay que / Tengo que / Sé] + [+ infinitivo] + [limpiar…]).

TWEE VALSTRIKKEN, elk in een eigen opvallend kader (§4-gramática + repaso):
  (1) «kunnen» is in het Spaans twee werkwoorden: saber (het geléérd hebben —
      sé cocinar) ↔ poder (het lukt/mag nu — no puede venir, está enferma);
  (2) «hay que» heeft nooit een persoon (nooit «hay que yo limpiar») en de «que»
      blijft staan vóór een werkwoord (tengo QUE fregar).

VIDEO: voor aflevering 10 bestaat GEEN YouTube-link. De bron is een Google-Drive-
bestand (file-id 1VbXY7Bjp2yEs0MTry3g-UmpBHKhtY5Qa, deelrechten reader/anyone).
De online-video-embed gebruikt daarom de Drive-/preview-URL; daarnaast staat er een
gewone hyperlink-knop «▶ Abrir en Drive» als gegarandeerde noodroute (browser).
Internet vereist.

C4-scope: «tengo que / tienes que», «hay que» en «sé / sabes / sabemos» zijn VASTE
CHUNKS, géén vervoegingsparadigma van «tener» of «saber» (dat systeem hoort in het
5de jaar, C5). De imperativo die Paul gebruikt («déjame») is enkel HERKENNEN — het
systeem komt in het 6de (C6). Géén futuro simple, condicional of subjuntivo.

Bron: 03-build/web/gen_c4u10_kgt.py · gen_c4u10_pdf.py · gen_c4u10_practica.py
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
OUT_DOCENTE = os.path.join(HERE, "C4_U10_docente.pptx")
OUT_ALUMNO_PPTX = os.path.join(HERE, "C4_U10_alumno.pptx")
OUT_ALUMNO = os.path.join(HERE, "C4_U10_alumno.ppsx")

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
F_VERB = RGBColor(0xEA, 0x73, 0x17)  # WERKWOORD          (oranje · U10: hay que / tener que / saber — dominante laag)
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

def footer(s, tab="U10 · TAREAS", page=None):
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
# C4 · UNIDAD 10 «Las tareas de casa» — slides (survival). Herbruikt de machinerie.
# ============================================================================
FTAB = "U10 · TAREAS"

def s01_title():
    s = slide(); bg(s)
    rect(s, 0, 0, EMU_W, Inches(4.7), fill=G)
    rect(s, 0, Inches(4.62), EMU_W, Inches(0.08), fill=GD)
    chip(s, Inches(0.6), Inches(0.5), "C4 · LA RUTA · EL DESPEGUE · PARADA 10", fill=WHITE, tcolor=G, size=12)
    text(s, Inches(0.55), Inches(1.15), Inches(12.3), Inches(1.1),
         [[("Las tareas de casa", {"size": 46, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(0.6), Inches(2.25), Inches(11.8), Inches(0.7),
         [[("Hay que limpiar esto. ", {"size": 26, "bold": True, "color": WHITE, "font": DISPLAY}),
           ("— Yo te ayudo. ¿Qué tengo que hacer?", {"size": 17, "italic": True, "color": GT})]])
    text(s, Inches(0.6), Inches(3.2), Inches(11.5), Inches(1.1),
         [[("Zeggen wat er ", {"size": 16, "color": WHITE}), ("moet gebeuren", {"size": 16, "bold": True, "color": WHITE}),
           (", wat je ", {"size": 16, "color": WHITE}), ("kunt", {"size": 16, "bold": True, "color": WHITE}),
           (" — en ", {"size": 16, "color": WHITE}), ("hulp aanbieden", {"size": 16, "bold": True, "color": WHITE}),
           (" (hay que · sé · yo te ayudo).", {"size": 16, "color": WHITE})],
          [("Survival in Spanish — la asistenta está enferma, dus Julio, María y Paul moeten de academie zélf schoonmaken.", {"size": 13, "italic": True, "color": GT})]])
    avatar(s, "mochila", Inches(10.7), Inches(4.95), d=Inches(1.7))
    text(s, Inches(0.6), Inches(5.25), Inches(9), Inches(1.5),
         [[("En esta unidad vas a…", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})],
          [("• Nombrar las tareas de casa  ", {"size": 13, "color": INK}), ("limpiar el polvo · pasar la aspiradora · fregar los platos", {"size": 11, "italic": True, "color": MUT})],
          [("• Decir lo que hay que hacer  ", {"size": 13, "color": INK}), ("hay que limpiar (algemeen) ↔ tengo que limpiar (ík)", {"size": 11, "italic": True, "color": MUT})],
          [("• Decir lo que sabes hacer  ", {"size": 13, "color": INK}), ("sé pasar la aspiradora · no sé cocinar · ¿sabes…?", {"size": 11, "italic": True, "color": MUT})],
          [("• Ofrecer y pedir ayuda  ", {"size": 13, "color": INK}), ("yo te ayudo · no es molestia · ¿qué tengo que hacer?", {"size": 11, "italic": True, "color": MUT})]])
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
             ("2", "Suena bien", "la g fuerte · gue / gui", 3),
             ("3", "La máquina de frases", "hay que / tengo que / sé + inf.", 4),
             ("4", "Kit", "las tareas · ofrecer ayuda", 5),
             ("5", "Gramática", "hay que · saber", 7),
             ("6", "Práctica", "oefenen samen", 9),
             ("7", "Hablar", "ofrece ayuda", 10),
             ("8", "Cultura", "el reparto de las tareas", 11),
             ("9", "Tarea", "¿Quién hace qué?", 12),
             ("10", "Repaso", "wat kun je nu?", 14)]
    x0, y0 = Inches(0.55), Inches(1.7)
    w = Inches(3.0); gx = Inches(0.18); gy = Inches(0.2)
    for i, t in enumerate(tiles):
        col = i % 4; row = i // 4
        _tile(s, x0 + col * (w + gx), y0 + row * (Inches(1.15) + gy), w, *t)
    text(s, Inches(0.6), Inches(5.95), Inches(12), Inches(0.9),
         [[("Consejo · Tip. ", {"size": 12, "bold": True, "color": GD, "font": DISPLAY}),
           ("Ná «hay que», «tengo que» en «sé» komt áltijd het hele werkwoord: hay que limpiar · tengo que fregar · sé cocinar. En «kunnen» = saber (geleerd) óf poder (het lukt nu)!", {"size": 12, "italic": True, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

# ── Online-video inbedden zodat hij ÍN PowerPoint afspeelt ────────────────────
# Bron U10 = GOOGLE DRIVE (net als U8/U9 bestaat er voor deze aflevering géén
# YouTube-link): file-id 1VbXY7Bjp2yEs0MTry3g-UmpBHKhtY5Qa, deelrechten
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
DRIVE_ID="1VbXY7Bjp2yEs0MTry3g-UmpBHKhtY5Qa"
VIDEO_URL="https://drive.google.com/file/d/%s/preview"%DRIVE_ID   # embed-URL (in-app speler)
VIDEO_WATCH="https://drive.google.com/file/d/%s/view"%DRIVE_ID    # browser-URL (noodroute)
VIDEO_TOP="Sitcom · Episodio 10"; VIDEO_MAIN="¡No tenemos asistenta!"
VIDEO_POSTER=os.path.join(HERE,"assets","video_poster_U10.png")
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
    """<url> = de VOLLEDIGE embed-URL (U1–U7: youtube.com/embed/<id> · U8–U10: de
    Drive-/preview-URL). De markup eronder is ongewijzigd t.o.v. U1–U9."""
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
    sectionbar(s, "§1 · ¡ESCUCHA!", "Bekijk la escena y escucha", "Kijk & luister — de asistenta is ziek, dus de academie moet zélf gepoetst worden", num=1)
    card(s, Inches(0.55), Inches(1.55), Inches(7.4), Inches(4.9), fill=WHITE, line=LINE)
    dia = [("Julio", "Perdona, ¿qué haces?", F_SUBJ),
           ("María", "Limpiar el polvo, la asistenta está enferma.", F_OBJ),
           ("María", "Hay que limpiar esto.", F_VERB),
           ("Julio", "Yo te ayudo.", F_VERB),
           ("María", "No tienes que molestarte.", F_NEG),
           ("Julio", "No es molestia, te ayudo.", F_VERB),
           ("Julio", "¿Qué tengo que hacer?", F_VERB),
           ("María", "Pues puedes ordenar los armarios, las estanterías.", F_PLAC),
           ("Julio", "También puedo pasar la aspiradora.", F_VERB),
           ("Julio", "Yo no soy machista: los hombres también sabemos limpiar.", F_VERB),
           ("María", "Ahí está la aspiradora.", F_PLAC),
           ("Paul", "¿Qué hacéis?", F_SUBJ),
           ("Julio", "Limpiar un poco. Hoy no tenemos asistenta.", F_NEG),
           ("María", "No puede venir en toda la semana, está enferma.", F_NEG),
           ("Paul", "Déjame, lo hago yo.", F_VERB),
           ("Julio", "Pero, ¿sabes pasar la aspiradora?", F_VERB),
           ("María", "¿Sabes cómo funciona?", F_VERB),
           ("Paul", "Claro que sé cómo funciona.", F_VERB),
           ("Paul", "Lo que pasa es que esto no funciona. ¡Ahí está!", F_NEG),
           ("Josefina", "Van a dejar la academia muy muy limpia.", F_SUBJ)]
    y = Inches(1.72)
    for sp, tx, col in dia:
        chip(s, Inches(0.72), y, sp, fill=col, tcolor=WHITE, size=9.5)
        text(s, Inches(1.62), y - Inches(0.02), Inches(6.25), Inches(0.42),
             [[(tx, {"size": 9.5, "color": INK})]])
        y = y + Inches(0.232)
    card(s, Inches(8.2), Inches(1.55), Inches(4.6), Inches(2.45), fill=GT, line=G)
    text(s, Inches(8.45), Inches(1.72), Inches(4.1), Inches(2.2),
         [[("Chunks para llevar 🎒", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})],
          [("Hay que limpiar · tengo que fregar", {"size": 11.5, "color": INK})],
          [("Yo te ayudo · ¿Te ayudo? · No es molestia", {"size": 11.5, "color": INK})],
          [("¿Qué tengo que hacer? · ¿Y ahora?", {"size": 11.5, "color": INK})],
          [("¿Sabes…? · Claro que sé · No sé cocinar", {"size": 11.5, "color": INK})],
          [("está enferma · no funciona · ¡Ahí está!", {"size": 11.5, "color": INK})]])
    text(s, Inches(8.2), Inches(4.12), Inches(2.95), Inches(0.3),
         [[("🎬 Episodio 10 — klik om af te spelen", {"size": 11, "bold": True, "color": GD, "font": DISPLAY})]])
    btn, _bw = chip(s, Inches(11.2), Inches(4.09), "▶ Abrir en Drive", fill=G, tcolor=WHITE, size=9.5)
    try:
        btn.click_action.hyperlink.address = VIDEO_WATCH
    except Exception:
        pass
    add_online_video(s, VIDEO_URL, Inches(8.2), Inches(4.45), Inches(4.6), Inches(2.55), VIDEO_POSTER)
    notes(s, "De video van aflevering 10 komt uit GOOGLE DRIVE (er is voor deze aflevering géén YouTube-link): file-id 1VbXY7Bjp2yEs0MTry3g-UmpBHKhtY5Qa, deelrechten reader/anyone → INTERNET VEREIST. Klik op de poster om in PowerPoint af te spelen; lukt dat niet, klik dan de knop «▶ Abrir en Drive» (of open de Drive-link zelf in een browser: " + VIDEO_WATCH + ") — dan speelt de video in het browsertabblad. Aanpak: eerst één keer kijken zónder transcript (globaal begrijpen: de poetshulp is ziek, dus Julio, María en Paul poetsen zelf; Paul beweert dat hij weet hoe de stofzuiger werkt), daarna met het transcript. Laat de leerlingen drie kolommen maken: TAREAS (limpiar el polvo · pasar la aspiradora · ordenar los armarios) ↔ AYUDA (yo te ayudo · no es molestia · ¿qué tengo que hacer?) ↔ SABER/PODER (¿sabes…? · claro que sé · no puede venir). Let ook op het contrast «hay que limpiar» (algemeen) tegenover «tengo que hacer» (ík). Paul zegt «déjame» — imperativo, enkel herkennen. Doelcodes: C4-LU-1 · C4-STR-1 · C4-WS-1.")
    footer(s, tab=FTAB, page=pg())

def s04_kit():
    s = slide(); bg(s)
    sectionbar(s, "§2 · KIT", "Las tareas · ofrecer ayuda · saber hacerlo", "De huistaken benoemen, hulp aanbieden en zeggen wat je kunt", num=2)
    cols = [("Las tareas de casa 🧹", [("limpiar el polvo", "afstoffen"), ("pasar la aspiradora", "stofzuigen"),
              ("fregar los platos", "de vaat doen"), ("ordenar los armarios", "de kasten opruimen"),
              ("hacer la cama", "het bed opmaken"), ("planchar · cocinar", "strijken · koken")]),
            ("Ofrecer y pedir ayuda 🤝", [("Yo te ayudo", "ik help je"), ("¿Te ayudo?", "help ik je?"),
              ("No es molestia", "het is geen moeite"), ("¿Qué tengo que hacer?", "wat moet ik doen?"),
              ("¿Me ayudas?", "help je me?"), ("Déjame, lo hago yo", "laat mij maar")]),
            ("¿Sabes hacerlo? 💡", [("Sé pasar la aspiradora", "ik kan stofzuigen"), ("¿Sabes…?", "kan jij…?"),
              ("Claro que sé", "natuurlijk kan ik dat"), ("No sé cocinar", "ik kan niet koken"),
              ("Sabemos limpiar", "wij kunnen poetsen"), ("¿Sabes cómo funciona?", "weet je hoe het werkt?")])]
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
    sectionbar(s, "§2 · KIT", "Hay que… · problemitas en la academia", "Zeggen dat iets moet gebeuren — en de taal voor als iets misloopt", num=2)
    left = [("Hay que limpiar", "er moet gepoetst worden"), ("Hay que ordenar esto", "dit moet opgeruimd worden"),
            ("Tengo que fregar", "ík moet de vaat doen"), ("Tienes que planchar", "jíj moet strijken"),
            ("No tienes que molestarte", "je hoeft geen moeite te doen")]
    right = [("La asistenta está enferma", "de poetshulp is ziek"), ("No puede venir", "ze kan niet komen"),
             ("Esto no funciona", "dit werkt niet"), ("¡Qué desorden!", "wat een rommel!"),
             ("¡Ahí está!", "daar is het! / gelukt!")]
    card(s, Inches(0.55), Inches(1.6), Inches(6.0), Inches(4.9), fill=GT, line=G)
    text(s, Inches(0.8), Inches(1.78), Inches(5.5), Inches(0.5),
         [[("Hay que… · «het moet gebeuren» ✅", {"size": 13.5, "bold": True, "color": GD, "font": DISPLAY})]])
    y = Inches(2.5)
    for es, nl in left:
        text(s, Inches(0.8), y, Inches(5.4), Inches(0.6), [[(es, {"size": 15, "bold": True, "color": INK}), ("   " + nl, {"size": 11, "italic": True, "color": MUT})]])
        y = y + Inches(0.72)
    card(s, Inches(6.8), Inches(1.6), Inches(6.0), Inches(4.9), fill=WHITE, line=LINE)
    text(s, Inches(7.05), Inches(1.78), Inches(5.5), Inches(0.5),
         [[("En la academia · problemitas 🔧", {"size": 13.5, "bold": True, "color": GD, "font": DISPLAY})]])
    y = Inches(2.5)
    for es, nl in right:
        text(s, Inches(7.05), y, Inches(5.4), Inches(0.6), [[(es, {"size": 15, "bold": True, "color": INK}), ("   " + nl, {"size": 11, "italic": True, "color": MUT})]])
        y = y + Inches(0.72)
    text(s, Inches(0.8), Inches(5.7), Inches(11.9), Inches(0.7),
         [[("¡Ojo! ", {"size": 12, "bold": True, "color": RED}),
           ("«hay que» zegt níet wie · «no puede venir» = het lukt niet (poder), «no sabe cocinar» = ze heeft het nooit geleerd (saber).", {"size": 12, "italic": True, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

def s06_gram_hayque():
    s = slide(); bg(s)
    sectionbar(s, "§4 · GRAMÁTICA", "hay que + infinitivo ↔ tener que + infinitivo", "Zeggen wat er moet gebeuren: mét of zónder een persoon", num=4)
    legend_func(s, Inches(0.55), Inches(1.42))
    card(s, Inches(0.55), Inches(1.9), Inches(7.6), Inches(4.1), fill=WHITE, line=LINE)
    text(s, Inches(0.8), Inches(2.05), Inches(7.1), Inches(0.4), [[("hay que  ·  tengo que  ·  tienes que  +  infinitivo", {"size": 15, "bold": True, "color": GD, "font": DISPLAY})]])
    filas = [("hay que", "het moet gebeuren", "Hay que limpiar esto."),
             ("tengo que", "ík moet", "Tengo que fregar los platos."),
             ("tienes que", "jíj moet", "Tienes que ordenar los armarios.")]
    y = Inches(2.6)
    for chunk, nl, ex in filas:
        rect(s, Inches(0.8), y, Inches(1.75), Inches(0.42), fill=RGBColor(0xFE,0xF1,0xE7), line=None, round=True, radius=0.2)
        text(s, Inches(0.8), y + Inches(0.02), Inches(1.75), Inches(0.38),
             [[(chunk, {"size": 14, "bold": True, "color": F_VERB, "font": DISPLAY})]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text(s, Inches(2.68), y + Inches(0.02), Inches(1.6), Inches(0.38),
             [[(nl, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, Inches(4.32), y + Inches(0.02), Inches(3.7), Inches(0.38),
             [[(ex, {"size": 12, "italic": True, "color": MUT})]], anchor=MSO_ANCHOR.MIDDLE)
        y = y + Inches(0.52)
    rect(s, Inches(0.8), Inches(4.3), Inches(7.1), Inches(0.62), fill=GT, line=G, lw=1.4, round=True, radius=0.1)
    text(s, Inches(0.95), Inches(4.38), Inches(6.8), Inches(0.5),
         [[("«hay que» no cambia nunca: ", {"size": 12.5, "bold": True, "color": GD}), ("hay que ", {"size": 13, "bold": True, "color": F_VERB}),
           ("limpiar · fregar · planchar  —  ", {"size": 13, "color": INK}),
           ("net als «hay» (er is/er zijn).", {"size": 12, "italic": True, "color": MUT})]])
    text(s, Inches(0.8), Inches(5.05), Inches(7.1), Inches(0.85),
         [[("💡 ", {"size": 12}), ("Wil je ", {"size": 12, "color": INK}),
           ("niet zeggen wie", {"size": 12, "bold": True, "color": GD}), (" het moet doen? Gebruik ", {"size": 12, "color": INK}),
           ("hay que", {"size": 12, "bold": True, "color": F_VERB}), (". Wil je het wél duidelijk maken? ", {"size": 12, "color": INK}),
           ("tengo / tienes que", {"size": 12, "bold": True, "color": F_SUBJ}), (".", {"size": 12, "color": INK})],
          [("Y para preguntar: ", {"size": 12, "color": INK}), ("¿Qué tengo que hacer? · ¿Qué hay que limpiar?", {"size": 12, "bold": True, "color": F_VERB})]])
    card(s, Inches(8.4), Inches(1.9), Inches(4.4), Inches(4.1), fill=GT, line=G)
    chip(s, Inches(8.6), Inches(1.76), "🔎 FÍJATE · EN LA ESCENA", fill=G, tcolor=WHITE, size=9.5)
    text(s, Inches(8.65), Inches(2.3), Inches(3.9), Inches(2.4),
         [[("Je hoorde het al:", {"size": 12, "bold": True, "color": GD, "font": DISPLAY})],
          [("«", {"size": 13, "color": INK}), ("Hay que", {"size": 13, "bold": True, "color": F_VERB}), (" limpiar esto.»", {"size": 13, "color": INK})],
          [("«¿Qué ", {"size": 13, "color": INK}), ("tengo que", {"size": 13, "bold": True, "color": F_VERB}), (" hacer?»", {"size": 13, "color": INK})],
          [("«No ", {"size": 13, "color": INK}), ("tienes que", {"size": 13, "bold": True, "color": F_VERB}), (" molestarte.»", {"size": 13, "color": INK})],
          [("«", {"size": 13, "color": INK}), ("Puedes", {"size": 13, "bold": True, "color": F_VERB}), (" ordenar los armarios.»", {"size": 13, "color": INK})]])
    text(s, Inches(8.65), Inches(4.75), Inches(3.9), Inches(1.2),
         [[("¿Y tú? · En jij?", {"size": 12, "bold": True, "color": GD, "font": DISPLAY})],
          [("¿Qué hay que hacer en tu casa?", {"size": 13, "bold": True, "color": INK})],
          [("Antwoord met «Hay que…» + het hele werkwoord.", {"size": 11, "italic": True, "color": MUT})]])
    notes(s, "Functioneel contrast op één dia. «hay que + infinitivo» = onpersoonlijke verplichting: het moet gebeuren, maar je zegt niet wie het doet — de vorm verandert NOOIT (net als «hay»). «tengo que / tienes que + infinitivo» = wél een persoon. Presenteer alle drie als VASTE CHUNKS, niet als paradigma van «tener» (tengo/tienes/tiene/tenemos/tenéis/tienen) — dat systeem hoort in het 5de jaar (C5). Didactisch sterk: laat leerlingen eerst een lijstje «hay que…» maken voor het klaslokaal (neutraal, geen gezichtsverlies), en pas daarna verdelen met «tú tienes que… / yo tengo que…». De «que» blijft altijd staan vóór het werkwoord. Doelcodes: C4-WS-1 · C4-TS-3 · C4-SP-1 · C4-GE-3.")
    footer(s, tab=FTAB, page=pg())

def s07_gram_saber():
    s = slide(); bg(s)
    sectionbar(s, "§4 · GRAMÁTICA", "saber + infinitivo ↔ poder + infinitivo", "Twee soorten «kunnen»: het geléérd hebben ↔ de kans/mogelijkheid hebben", num=4)
    card(s, Inches(0.55), Inches(1.42), Inches(6.05), Inches(1.62), fill=WHITE, line=LINE)
    text(s, Inches(0.8), Inches(1.54), Inches(5.6), Inches(0.35), [[("saber + infinitivo · iets kúnnen (geleerd)", {"size": 13.5, "bold": True, "color": GD, "font": DISPLAY})]])
    filas = [("sé", "ik kan / ik weet", "Sé pasar la aspiradora."),
             ("¿sabes…?", "kan jij…?", "¿Sabes cómo funciona?"),
             ("sabemos", "wij kunnen", "Los hombres también sabemos limpiar.")]
    y = Inches(1.92)
    for chunk, nl, ex in filas:
        text(s, Inches(0.8), y, Inches(5.6), Inches(0.36),
             [[(chunk + "  ", {"size": 14, "bold": True, "color": F_VERB, "font": DISPLAY}),
               (nl + "   ", {"size": 11.5, "color": INK}), (ex, {"size": 10.5, "italic": True, "color": MUT})]])
        y = y + Inches(0.36)
    text(s, Inches(0.8), Inches(2.76), Inches(5.6), Inches(0.3),
         [[("Letterlijk: «ik ", {"size": 11, "italic": True, "color": MUT}), ("weet", {"size": 11, "bold": True, "color": GD}), (" stofzuigen» → ik heb het geleerd.", {"size": 11, "italic": True, "color": MUT})]])
    card(s, Inches(6.75), Inches(1.42), Inches(6.05), Inches(1.62), fill=CREMA, line=LINE)
    text(s, Inches(7.0), Inches(1.54), Inches(5.6), Inches(0.35), [[("poder + infinitivo · het lukt / het mag", {"size": 13.5, "bold": True, "color": GD, "font": DISPLAY})]])
    mv1 = rect(s, Inches(7.0), Inches(1.96), Inches(2.85), Inches(0.92), fill=RGBColor(0xFE,0xF1,0xE7), line=None, round=True, radius=0.1)
    text(s, Inches(7.12), Inches(2.02), Inches(2.65), Inches(0.85),
         [[("💡 saber = geleerd", {"size": 9.5, "bold": True, "color": RGBColor(0xB4,0x53,0x0E)})],
          [("Sé cocinar.", {"size": 12, "bold": True, "color": INK})],
          [("No sé planchar.", {"size": 12, "bold": True, "color": INK})]])
    mv2 = rect(s, Inches(9.95), Inches(1.96), Inches(2.85), Inches(0.92), fill=RGBColor(0xE8,0xF0,0xFE), line=None, round=True, radius=0.1)
    text(s, Inches(10.07), Inches(2.02), Inches(2.65), Inches(0.85),
         [[("🔓 poder = het lukt/mag", {"size": 9.5, "bold": True, "color": RGBColor(0x1E,0x40,0xAF)})],
          [("No puede venir.", {"size": 12, "color": INK})],
          [("Puedes ordenar los armarios.", {"size": 12, "color": INK})]])
    card(s, Inches(0.55), Inches(3.16), Inches(6.05), Inches(1.28), fill=RGBColor(0xFD,0xE8,0xE8), line=RED, lw=2.4)
    chip(s, Inches(0.75), Inches(3.02), "¡OJO! · LA TRAMPA 1", fill=RED, tcolor=WHITE, size=9.5)
    text(s, Inches(0.8), Inches(3.42), Inches(5.6), Inches(1.0),
         [[("«ik kan koken» = ", {"size": 13, "color": INK}), ("sé cocinar", {"size": 17, "bold": True, "color": F_VERB, "font": DISPLAY})],
          [("niet ", {"size": 12, "color": INK}), ("puedo cocinar", {"size": 12.5, "bold": True, "color": RED}),
           (" — dat betekent «het lukt me vandaag».", {"size": 12, "color": INK})]])
    card(s, Inches(6.75), Inches(3.16), Inches(6.05), Inches(1.28), fill=RGBColor(0xFD,0xE8,0xE8), line=RED, lw=2.4)
    chip(s, Inches(6.95), Inches(3.02), "¡OJO! · LA TRAMPA 2", fill=RED, tcolor=WHITE, size=9.5)
    text(s, Inches(7.0), Inches(3.42), Inches(5.6), Inches(1.0),
         [[("«hay que» heeft ", {"size": 12, "color": INK}), ("geen persoon", {"size": 12.5, "bold": True, "color": RED}),
           (": ", {"size": 12, "color": INK}), ("hay que limpiar", {"size": 13, "bold": True, "color": INK}),
           ("  (niet ", {"size": 11.5, "color": INK}), ("hay que yo limpiar", {"size": 11.5, "bold": True, "color": RED}), (")", {"size": 11.5, "color": INK})],
          [("en de ", {"size": 12, "color": INK}), ("que", {"size": 14, "bold": True, "color": RED}),
           (" blijft: tengo ", {"size": 12, "color": INK}), ("que", {"size": 13, "bold": True, "color": RED}),
           (" fregar  (niet ", {"size": 12, "color": INK}), ("tengo fregar", {"size": 11.5, "bold": True, "color": RED}), (")", {"size": 11.5, "color": INK})]])
    card(s, Inches(0.55), Inches(4.56), Inches(12.25), Inches(0.78), fill=GT, line=G)
    text(s, Inches(0.8), Inches(4.64), Inches(11.8), Inches(0.65),
         [[("Ofrecer ayuda · ", {"size": 12.5, "bold": True, "color": GD, "font": DISPLAY}),
           ("«— ¿Qué haces? — ", {"size": 12, "color": INK}),
           ("Yo te ayudo", {"size": 12.5, "bold": True, "color": F_VERB}), (". — ", {"size": 12, "color": INK}),
           ("No tienes que molestarte", {"size": 12.5, "bold": True, "color": F_NEG}), (". — ", {"size": 12, "color": INK}),
           ("No es molestia", {"size": 12.5, "bold": True, "color": GD}), (". ¿Qué tengo que hacer?»", {"size": 12, "color": INK})],
          [("Tres pasos: ", {"size": 11.5, "color": INK}), ("ofrecer", {"size": 11.5, "bold": True, "color": F_VERB}),
           (" → ", {"size": 11.5, "color": INK}), ("insistir (no es molestia)", {"size": 11.5, "bold": True, "color": GD}),
           (" → ", {"size": 11.5, "color": INK}), ("pedir instrucciones (¿qué tengo que hacer?)", {"size": 11.5, "bold": True, "color": F_SUBJ})]])
    text(s, Inches(0.6), Inches(5.45), Inches(12.2), Inches(0.4),
         [[("Completa · vul aan (klik voor de oplossing): ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("¡Qué desorden! ___ que limpiar.   Yo ___ cocinar (geleerd).   Ella no ___ venir, está enferma.", {"size": 13, "color": INK})]])
    exercise_solucion(s, Inches(0.8), Inches(5.88), Inches(11.7), Inches(0.5),
        [[("hay · sé · puede", {"bold": True, "color": GD, "size": 13})]])
    noodroute(s)
    notes(s, "Twee contrasten op één dia. (1) «saber + infinitivo» = kunnen omdat je het geléérd hebt (sé cocinar · no sé planchar · ¿sabes pasar la aspiradora?); «poder + infinitivo» = kunnen omdat het lukt of mag (no puede venir, está enferma · puedes ordenar los armarios). DE KERNVALSTRIK voor Nederlandstaligen: ons ene woord «kunnen» dekt beide, dus «ik kan koken» wordt fout «puedo cocinar» — juist is «sé cocinar». Vuistregel voor de klas: heb je het geléérd? → saber. Lukt het (nu)? → poder. (2) «hay que» krijgt nooit een persoon (nooit «hay que yo limpiar») en de «que» blijft staan vóór het werkwoord (tengo QUE fregar, niet «tengo fregar»). C4-scope: «sé / sabes / sabemos» en «tengo que / tienes que» zijn VASTE CHUNKS — géén vervoegingsparadigma van «saber» of «tener»; dat systeem komt in het 5de jaar (C5). Paul gebruikt in de scène ook «déjame» (imperativo): enkel HERKENNEN, het systeem hoort in C6. Oplossing: hay · sé · puede.")
    footer(s, tab=FTAB, page=pg())

def s08_practica():
    s = slide(); bg(s)
    sectionbar(s, "§3 · PRÁCTICA", "Completa el diálogo", "Vul samen aan — klik voor de oplossing", num=3)
    card(s, Inches(0.55), Inches(1.7), Inches(7.6), Inches(4.5), fill=WHITE, line=LINE)
    lines = ["— ¡Qué desorden! ___ que limpiar esto.",
             "— Yo te ___. ¿Qué ___ que hacer?",
             "— No tienes que molestarte.",
             "— No es ___.",
             "— ¿___ pasar la aspiradora?",
             "— Claro que ___. ¡Ahí está!"]
    y = Inches(1.95)
    for q in lines:
        text(s, Inches(0.8), y, Inches(7.1), Inches(0.6), [[(q, {"size": 15.5, "color": INK})]])
        y = y + Inches(0.7)
    exercise_solucion(s, Inches(8.4), Inches(1.9), Inches(4.4), Inches(4.0),
        [[("1. Hay", {"color": GD, "size": 14})], [("2. ayudo", {"color": GD, "size": 14})],
         [("3. tengo", {"color": GD, "size": 14})], [("4. molestia", {"color": GD, "size": 14})],
         [("5. Sabes", {"color": GD, "size": 14})], [("6. sé", {"color": GD, "size": 14})]],
        title_doc="SOLUCIÓN · docent")
    noodroute(s)
    notes(s, "Laat leerlingen eerst zelf proberen (in duo, hardop). Klik daarna de oplossing open. Let op: «Hay que limpiar» — onpersoonlijk, geen persoon; «Yo te ayudo» — het aanbod; «¿Qué tengo que hacer?» — de «que» is verplicht vóór het werkwoord; «No es molestia» — de vaste formule om aan te dringen; «¿Sabes pasar la aspiradora?» / «Claro que sé» — saber, want het gaat om iets geleerd hebben. Oplossing: Hay · ayudo · tengo · molestia · Sabes · sé.")
    footer(s, tab=FTAB, page=pg())

def s09_speaking():
    s = slide(); bg(s)
    sectionbar(s, "§3 · HABLAR", "Ofrece ayuda", "Bied hulp aan, dring vriendelijk aan en vraag wat je moet doen — sin leer", num=3)
    card(s, Inches(0.55), Inches(1.7), Inches(7.6), Inches(3.4), fill=GT, line=G)
    text(s, Inches(0.85), Inches(1.95), Inches(7.1), Inches(3.0),
         [[("Modelo · zeg dit hardop:", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})],
          [("«— ¡Qué desorden! Hay que limpiar esto.", {"size": 16, "color": INK})],
          [("— Yo te ayudo. ¿Qué tengo que hacer?", {"size": 16, "color": INK})],
          [("— No tienes que molestarte. — No es molestia.", {"size": 16, "color": INK})],
          [("— Pues, ¿sabes pasar la aspiradora? — Claro que sé.»", {"size": 16, "color": INK})]])
    card(s, Inches(8.4), Inches(1.7), Inches(4.4), Inches(3.4), fill=WHITE, line=LINE)
    text(s, Inches(8.65), Inches(1.95), Inches(3.9), Inches(3.0),
         [[("¿Cómo? · Werkvorm", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})],
          [("1. Constata: «¡Qué desorden! Hay que…».", {"size": 12.5, "color": INK})],
          [("2. Ofrece: «Yo te ayudo» · «¿Te ayudo?».", {"size": 12.5, "color": INK})],
          [("3. Insiste: «No es molestia».", {"size": 12.5, "color": INK})],
          [("4. Pide instrucciones: «¿Qué tengo que hacer?».", {"size": 12.5, "color": INK})],
          [("5. Di lo que sabes: «Sé…» / «No sé…».", {"size": 12.5, "color": INK})]])
    text(s, Inches(0.6), Inches(5.4), Inches(12), Inches(0.7),
         [[("Interactie ", {"size": 12, "bold": True, "color": GD, "font": DISPLAY}),
           ("= hulp aanbieden, vriendelijk aandringen én afspreken wie wat doet. Bied 3× hulp aan; je buur weigert 1× («no tienes que molestarte»). Verstaan? Zeg: «¿Cómo? / ¿Puedes repetir?»", {"size": 12, "italic": True, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

def s10_musica():
    s = slide(); bg(s)
    sectionbar(s, "CULTURA", "El reparto de las tareas", "Wie doet wat in huis? — en muziek erbij", num=None)
    bandas = [("Rosalía", "Malamente", "🇪🇸 España"), ("Bebe", "Ella", "🇪🇸 España"),
              ("Ana Tijoux", "1977", "🇨🇱 Chile"), ("Manu Chao", "Me Gustas Tú", "🇪🇸/🇫🇷"),
              ("Natalia Lafourcade", "Hasta la Raíz", "🇲🇽 México"), ("Juanes", "La Camisa Negra", "🇨🇴 Colombia")]
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
         [[("🧹 El reparto de las tareas ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("Julio zegt het zelf: «yo no soy machista: ", {"size": 12, "color": INK}),
           ("los hombres también sabemos pasar la aspiradora", {"size": 12, "bold": True, "color": F_VERB}),
           ("». De eerlijke verdeling van huistaken is in Spanje en Latijns-Amerika een levend gespreksonderwerp.", {"size": 12, "color": INK})],
          [("Een ", {"size": 12, "color": INK}), ("asistenta", {"size": 12, "bold": True, "color": GD}),
           (" (poetshulp) is er gewoner dan bij ons, ook in gewone gezinnen. Vrouwen doen er nog altijd méér huishouden dan mannen, maar bij jonge koppels loopt dat verschil zichtbaar terug. Playlist + LyricsTraining op de hub → tabblad Música.", {"size": 12, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

def s11_tarea():
    s = slide(); bg(s)
    sectionbar(s, "§5 · TAREA FINAL", "¿Quién hace qué?", "Maak samen een cuadro de tareas: wat moet gebeuren, wie doet het, wie kán het", num=5)
    card(s, Inches(0.55), Inches(1.7), Inches(6.6), Inches(3.6), fill=WHITE, line=G, lw=1.6)
    rect(s, Inches(0.55), Inches(1.7), Inches(6.6), Inches(0.5), fill=G)
    text(s, Inches(0.75), Inches(1.76), Inches(6.2), Inches(0.4), [[("CUADRO DE TAREAS · Academia «Bienvenidos al español»", {"size": 12, "bold": True, "color": WHITE, "font": DISPLAY})]])
    heads = [("Hay que…", Inches(2.4)), ("¿Quién? (tengo/tienes que)", Inches(2.1)), ("¿Sabe? (sé/no sé)", Inches(1.9))]
    hx = Inches(0.68)
    for h, hw in heads:
        rect(s, hx, Inches(2.32), hw, Inches(0.32), fill=GT, line=LINE, lw=1.0, round=True, radius=0.16)
        text(s, hx, Inches(2.34), hw, Inches(0.28),
             [[(h, {"size": 9, "bold": True, "color": GD, "font": DISPLAY})]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        hx = hx + hw + Inches(0.06)
    iconos = ["🧹", "🍽️", "👕", "🚪"]
    ry = Inches(2.7)
    for ic in iconos:
        rect(s, Inches(0.68), ry, Inches(2.4), Inches(0.48), fill=CREMA, line=LINE, lw=1.0, round=True, radius=0.08)
        text(s, Inches(0.78), ry + Inches(0.03), Inches(2.2), Inches(0.42),
             [[(ic + "  hay que ______", {"size": 10, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        rect(s, Inches(3.14), ry, Inches(2.1), Inches(0.48), fill=PAPER, line=LINE, lw=1.0, round=True, radius=0.08)
        rect(s, Inches(5.3), ry, Inches(1.9), Inches(0.48), fill=PAPER, line=LINE, lw=1.0, round=True, radius=0.08)
        ry = ry + Inches(0.52)
    text(s, Inches(0.75), Inches(4.85), Inches(6.2), Inches(0.45),
         [[("🤝 Nuestro reparto: Tú tienes que ", {"size": 11.5, "bold": True, "color": INK}), ("______ ", {"size": 11.5, "color": LINE}),
           ("y yo tengo que ", {"size": 11.5, "bold": True, "color": INK}), ("______ ", {"size": 11.5, "color": LINE}),
           (". ¡Yo te ayudo!", {"size": 11.5, "bold": True, "color": GD})]])
    card(s, Inches(7.4), Inches(1.7), Inches(5.4), Inches(3.6), fill=GT, line=G)
    text(s, Inches(7.65), Inches(1.88), Inches(4.9), Inches(3.3),
         [[("Los pasos · stappen", {"size": 14, "bold": True, "color": GD, "font": DISPLAY})],
          [("1. ¿Qué hay que hacer? Noteer met je groep 4 taken: «Hay que + infinitivo».", {"size": 12, "color": INK})],
          [("2. ¿Qué sabes hacer? Zeg wat jíj kunt en vraag het je groepsgenoten: «Yo sé…» · «¿Sabes…?» · «No sé…».", {"size": 12, "color": INK})],
          [("3. Repartid las tareas: «Tú tienes que… y yo tengo que…» · «Yo te ayudo».", {"size": 12, "color": INK})],
          [("4. Presentad el cuadro aan de klas — sin leer del papel.", {"size": 12, "color": INK})]])
    text(s, Inches(0.6), Inches(5.45), Inches(7.6), Inches(1.0),
         [[("🏁 Klaar als… ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("je 4 taken noemt met «hay que + werkwoord», zegt wat je wél/niet kunt met «(no) sé + werkwoord», de taken verdeelt met «tengo/tienes que» en één keer hulp aanbiedt met «yo te ayudo» — zónder af te lezen.", {"size": 12, "color": INK})]])
    card(s, Inches(8.4), Inches(5.42), Inches(4.4), Inches(1.05), fill=WHITE, line=LINE)
    text(s, Inches(8.6), Inches(5.5), Inches(4.0), Inches(0.9),
         [[("Evaluatie · 🟢🟡🔴", {"size": 11.5, "bold": True, "color": GD, "font": DISPLAY})],
          [("· hay que + infinitivo correct", {"size": 10.5, "color": INK})],
          [("· saber + infinitivo correct (sé / no sé)", {"size": 10.5, "color": INK})],
          [("· hulp aanbieden & taken verdelen", {"size": 10.5, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

def s12_repaso():
    s = slide(); bg(s)
    sectionbar(s, "REPASO", "Lo esencial de un vistazo", "Wat je nu kunt — semáforo", num=None)
    card(s, Inches(0.55), Inches(1.7), Inches(7.6), Inches(3.3), fill=WHITE, line=LINE)
    text(s, Inches(0.85), Inches(1.85), Inches(7.1), Inches(3.1),
         [[("Zo zeg je wat er moet gebeuren", {"size": 14, "bold": True, "color": GD, "font": DISPLAY})],
          [("Hay que limpiar · Hay que fregar los platos (zónder persoon)", {"size": 13.5, "color": INK})],
          [("Tengo que planchar · Tienes que ordenar (mét persoon)", {"size": 13, "color": INK})],
          [("", {"size": 6})],
          [("Zo zeg je wat je kunt", {"size": 14, "bold": True, "color": GD, "font": DISPLAY})],
          [("Sé pasar la aspiradora · ¿Sabes cómo funciona? · No sé cocinar", {"size": 13, "color": INK})],
          [("Sabemos limpiar · Claro que sé", {"size": 13, "color": INK})],
          [("", {"size": 6})],
          [("Zo bied je hulp aan", {"size": 14, "bold": True, "color": GD, "font": DISPLAY})],
          [("Yo te ayudo · ¿Te ayudo? · No es molestia · ¿Qué tengo que hacer?", {"size": 13, "color": INK})]])
    card(s, Inches(0.55), Inches(5.15), Inches(7.6), Inches(1.0), fill=RGBColor(0xFD,0xE8,0xE8), line=RED, lw=2.0)
    text(s, Inches(0.85), Inches(5.23), Inches(7.1), Inches(0.9),
         [[("¡Ojo! · las dos trampas ", {"size": 12.5, "bold": True, "color": RED, "font": DISPLAY}),
           ("«ik kan koken» = ", {"size": 12, "color": INK}), ("sé cocinar", {"size": 12.5, "bold": True, "color": F_VERB}),
           (" (geleerd) ↔ ", {"size": 12, "color": INK}), ("no puede venir", {"size": 12.5, "bold": True, "color": F_VERB}), (" (het lukt niet).", {"size": 12, "color": INK})],
          [("En: ", {"size": 12, "color": INK}), ("hay que", {"size": 12.5, "bold": True, "color": RED}),
           (" krijgt nooit een persoon · de ", {"size": 12, "color": INK}), ("que", {"size": 12.5, "bold": True, "color": RED}),
           (" blijft staan: tengo que fregar.", {"size": 12, "color": INK})]])
    card(s, Inches(8.4), Inches(1.7), Inches(4.4), Inches(4.45), fill=GT, line=G)
    text(s, Inches(8.65), Inches(1.9), Inches(3.9), Inches(0.5), [[("Puedo… · Ik kan…", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    items = ["de huistaken benoemen (limpiar el polvo…)", "zeggen wat moet (hay que + inf.)",
             "zeggen wie het moet (tengo/tienes que)", "zeggen wat ik kan (sé / no sé + inf.)",
             "hulp aanbieden (yo te ayudo · no es molestia)", "om instructies vragen (¿qué tengo que hacer?)"]
    y = Inches(2.5)
    for it in items:
        text(s, Inches(8.65), y, Inches(3.9), Inches(0.7), [[("🟢🟡🔴  ", {"size": 12}), (it, {"size": 11, "color": INK})]])
        y = y + Inches(0.55)
    text(s, Inches(8.65), Inches(5.65), Inches(3.9), Inches(0.7), [[("🎮 Repasa jugando", {"size": 12, "bold": True, "color": GD, "font": DISPLAY})], [("online op de hub · el reparto de tareas · ¿saber o poder?", {"size": 11, "italic": True, "color": MUT})]])
    footer(s, tab=FTAB, page=pg())

def s13_teacher():
    s = slide(); bg(s, color=RGBColor(0x24,0x1C,0x1B))
    text(s, Inches(0.6), Inches(0.5), Inches(12), Inches(0.7), [[("Docentendossier · Unidad 10 «Las tareas de casa»", {"size": 22, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(0.6), Inches(1.3), Inches(12.1), Inches(5.6),
         [[("Timing (2 lesuren van 50 min).", {"size": 14, "bold": True, "color": RGBColor(0xFB,0xEA,0xEC), "font": DISPLAY})],
          [("Les 1: Escucha (sitcom ep. 10 — de asistenta is ziek, dus María staat af te stoffen; Julio biedt hulp aan, Paul wil het overnemen en beweert dat hij weet hoe de stofzuiger werkt) + Suena bien (la g fuerte · gue/gui met stille u · ¿/g/ o jota? · repaso aguda/llana) + La máquina de frases (hay que / tengo que / sé + infinitivo) + Kit (las tareas · ofrecer y pedir ayuda · saber hacerlo · hay que · problemitas). Les 2: gramática functioneel (hay que ↔ tener que · saber ↔ poder · ofrecer ayuda), práctica, hablar «Ofrece ayuda», tarea «¿Quién hace qué?» + cultura (el reparto de las tareas).", {"size": 12, "color": RGBColor(0xEC,0xEA,0xE3)})],
          [("", {"size": 5})],
          [("VIDEO = GOOGLE DRIVE (geen YouTube voor deze aflevering).", {"size": 14, "bold": True, "color": RGBColor(0xFB,0xEA,0xEC), "font": DISPLAY})],
          [("File-id 1VbXY7Bjp2yEs0MTry3g-UmpBHKhtY5Qa (deelrechten reader/anyone). INTERNET VEREIST. In de escucha-dia klik je op de poster om in PowerPoint af te spelen; lukt dat niet, gebruik de knop «▶ Abrir en Drive» of open " + VIDEO_WATCH + " zelf in een browser. Test de verbinding vóór de les.", {"size": 12, "color": RGBColor(0xEC,0xEA,0xE3)})],
          [("", {"size": 5})],
          [("Aanpak C4 (survival).", {"size": 14, "bold": True, "color": RGBColor(0xFB,0xEA,0xEC), "font": DISPLAY})],
          [("Chunks komen auditief binnen (luisteren → naspreken). «hay que», «tengo que / tienes que» en «sé / sabes / sabemos» presenteren als VASTE CHUNKS uit de scène — géén vervoegingsparadigma van «tener» of «saber»; het volledige werkwoordsysteem komt in het 5de jaar (C5). De imperativo die Paul gebruikt («déjame, lo hago yo») is enkel HERKENNEN — het systeem hoort in het 6de (C6). Géén futuro simple, condicional of subjuntivo. TWEE KERNVALSTRIKKEN: (1) ons ene woord «kunnen» is in het Spaans saber (het geléérd hebben — sé cocinar) óf poder (het lukt/mag nu — no puede venir, está enferma); vuistregel voor de klas: «geleerd? → saber · lukt het? → poder»; (2) «hay que» krijgt nooit een persoon (nooit «hay que yo limpiar») en de «que» blijft staan vóór een werkwoord (tengo QUE fregar, niet «tengo fregar»). Didactische tip: laat leerlingen eerst neutraal opsommen met «hay que…» (niemand wordt aangewezen, dus geen gezichtsverlies) en pas dán verdelen met «tú tienes que… / yo tengo que…». Uitspraak: g + a/o/u = /g/ zoals in «goal» (guapo · agua · luego); vóór e/i schrijf je gue/gui voor dezelfde klank en is de u STIL (guitarra = «gi-tarra») — precies dezelfde schrijftruc als qu (recycling U7); zonder die u wordt het de jota /x/ (gente · gimnasio, recycling U2). Doelcodes: C4-WS-1 · C4-TS-3 · C4-SP-2 · C4-LU-1 · C4-GE-3 · C4-STR-1 · C4-MEC-1/2 · C4-CU-1.", {"size": 12, "color": RGBColor(0xEC,0xEA,0xE3)})],
          [("", {"size": 5})],
          [("Evaluatie.", {"size": 14, "bold": True, "color": RGBColor(0xFB,0xEA,0xEC), "font": DISPLAY})],
          [("Mondelinge mini-taak «¿Quién hace qué?»: in groep een cuadro de tareas maken en voorstellen — 4 taken met «hay que + infinitivo», zeggen wat elk wél/niet kan met «(no) sé + infinitivo», de taken verdelen met «tengo/tienes que» en één keer hulp aanbieden met «yo te ayudo». Geen leerplan → focus op «kunnen gebruiken in de praktijk». Rubric: hay que + infinitivo correct · saber + infinitivo correct · hulp aanbieden & taken verdelen.", {"size": 12, "color": RGBColor(0xEC,0xEA,0xE3)})],
          [("", {"size": 5})],
          [("Oplossingen staan bij elke oefendia in de presenter-notities; antwoorden verschijnen bij klik.", {"size": 11, "italic": True, "color": RGBColor(0xA6,0xA2,0x9A)})]])
    footer(s, tab=FTAB, page=pg())

def s_uitspraak():
    s = slide(); bg(s)
    sectionbar(s, "SUENA BIEN", "La g fuerte · gue / gui · ¿/g/ o jota?", "Vóór a/o/u klinkt g als «goal» — en vóór e/i is de u van gue/gui STIL", num=None)
    card(s,Inches(0.55),Inches(1.6),Inches(6.05),Inches(2.15),fill=WHITE,line=LINE)
    rect(s,Inches(0.55),Inches(1.6),Inches(6.05),Inches(0.14),fill=G)
    text(s,Inches(0.8),Inches(1.85),Inches(5.6),Inches(0.4),[[("① La g fuerte · g + a / o / u",{"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
    text(s,Inches(0.8),Inches(2.35),Inches(5.6),Inches(1.3),
         [[("g",{"size":14.5,"bold":True,"color":G}),("uapo · a",{"size":14.5,"color":INK}),("g",{"size":14.5,"bold":True,"color":G}),("ua · lue",{"size":14.5,"color":INK}),("g",{"size":14.5,"bold":True,"color":G}),("o · ",{"size":14.5,"color":INK}),("g",{"size":14.5,"bold":True,"color":G}),("ato · al",{"size":14.5,"color":INK}),("g",{"size":14.5,"bold":True,"color":G}),("o · ami",{"size":14.5,"color":INK}),("g",{"size":14.5,"bold":True,"color":G}),("o",{"size":14.5,"color":INK})],
          [("Zoals in het Nederlandse «goal» — een harde g, geen keelklank.",{"size":11,"italic":True,"color":MUT})]])
    card(s,Inches(6.75),Inches(1.6),Inches(6.05),Inches(2.15),fill=WHITE,line=LINE)
    rect(s,Inches(6.75),Inches(1.6),Inches(6.05),Inches(0.14),fill=G)
    text(s,Inches(7.0),Inches(1.85),Inches(5.6),Inches(0.4),[[("② gue / gui · la u muda",{"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
    text(s,Inches(7.0),Inches(2.35),Inches(5.6),Inches(1.3),
         [[("gui",{"size":14.5,"bold":True,"color":G}),("tarra · se",{"size":14.5,"color":INK}),("gui",{"size":14.5,"bold":True,"color":G}),("r · ju",{"size":14.5,"color":INK}),("gue",{"size":14.5,"bold":True,"color":G}),("te · ",{"size":14.5,"color":INK}),("gue",{"size":14.5,"bold":True,"color":G}),("rra · Mi",{"size":14.5,"color":INK}),("gue",{"size":14.5,"bold":True,"color":G}),("l",{"size":14.5,"color":INK})],
          [("«guitarra» klinkt als «gi-tarra» — de u hóór je niet.",{"size":11,"italic":True,"color":MUT})]])
    card(s,Inches(0.55),Inches(3.9),Inches(12.25),Inches(0.85),fill=GT,line=G)
    text(s,Inches(0.85),Inches(4.05),Inches(11.7),Inches(0.6),
         [[("¡Ojo! ",{"size":13,"bold":True,"color":RED,"font":DISPLAY}),("De u van ",{"size":13,"color":INK}),("gue / gui",{"size":13,"bold":True,"color":GD}),(" is een ",{"size":13,"color":INK}),("schrijftruc",{"size":13,"bold":True,"color":RED}),(" — precies zoals bij ",{"size":13,"color":INK}),("que / qui",{"size":13,"bold":True,"color":GD}),(" (U7). Laat je die u weg, dan wordt het de ",{"size":13,"color":INK}),("jota /x/",{"size":13,"bold":True,"color":RED}),(": gente · gimnasio (U2).",{"size":13,"color":INK})]])
    text(s,Inches(0.6),Inches(5.0),Inches(12),Inches(0.4),[[("③ ¿/g/ o jota? · hoor het verschil",{"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
    text(s,Inches(0.6),Inches(5.5),Inches(12.2),Inches(0.65),
         [[("g",{"color":G,"bold":True}),("ato   ",{}),("g",{"color":G,"bold":True}),("uapo   ",{}),("gui",{"color":G,"bold":True}),("tarra      ↔      ",{}),("ge",{"color":RED,"bold":True}),("nte   ",{}),("gi",{"color":RED,"bold":True}),("mnasio   ",{}),("ge",{"color":RED,"bold":True}),("neral",{})]],size=19,font=DISPLAY)
    text(s,Inches(0.6),Inches(6.15),Inches(12.2),Inches(0.6),
         [[("④ Repaso · aguda o llana? ",{"size":13,"bold":True,"color":GD,"font":DISPLAY}),("as·pi·ra·DO·ra (llana) · or·de·NAR (aguda) · ar·MA·rio (llana) · lim·PIAR (aguda)",{"size":13,"color":INK})],
          [("🔊 Oefen de klanken online op de hub (tabblad Kit · Suena bien).",{"size":11,"italic":True,"color":MUT})]])
    footer(s, tab=FTAB, page=pg())

# ── «La máquina de frases» — zinbouwer in 3 blokken (U10: DRIE rijen) ──
def _maq_row(s, y, chunk, chunk_nl, opts, result, result_nl, h=Inches(1.0)):
    """Eén rij van de zinbouwer: [chunk] + [+ infinitivo] + [opties]  →  resultaat.
    Blok 1 = oranje-tint (werkwoord-semantiek), blok 2 = de rode huistint, blok 3 = wit.
    Het resultaat verschijnt bij klik (on-click reveal)."""
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
    sectionbar(s, "§4 · LA MÁQUINA DE FRASES", "Hay que / Tengo que / Sé + infinitivo", "Drie formules, altijd hetzelfde patroon — klik en de zin verschijnt", num=4)
    legend_func(s, Inches(0.55), Inches(1.42))
    _maq_row(s, Inches(1.66), "Hay que", "het moet gebeuren", "limpiar · fregar",
             "Hay que limpiar.", "Er moet gepoetst worden.", h=Inches(0.92))
    _maq_row(s, Inches(2.64), "Tengo que", "ík moet", "planchar · fregar",
             "Tengo que planchar.", "Ik moet strijken.", h=Inches(0.92))
    _maq_row(s, Inches(3.62), "Sé", "ik kán het (geleerd)", "cocinar · limpiar",
             "Sé cocinar.", "Ik kan koken.", h=Inches(0.92))
    card(s, Inches(0.55), Inches(4.66), Inches(12.25), Inches(0.72), fill=GT, line=G)
    text(s, Inches(0.85), Inches(4.74), Inches(11.7), Inches(0.62),
         [[("Cómo funciona · ", {"size": 12.5, "bold": True, "color": GD, "font": DISPLAY}),
           ("blok 1 (", {"size": 12.5, "color": INK}), ("hay que", {"size": 13, "bold": True, "color": F_VERB}),
           (" · ", {"size": 12.5, "color": INK}), ("tengo que", {"size": 13, "bold": True, "color": F_VERB}),
           (" · ", {"size": 12.5, "color": INK}), ("sé", {"size": 13, "bold": True, "color": F_VERB}),
           (") + blok 2 = altijd het ", {"size": 12.5, "color": INK}), ("hele werkwoord", {"size": 13, "bold": True, "color": GD}),
           (" (el infinitivo: -ar · -er · -ir). Nooit een vervoegde vorm!", {"size": 12.5, "color": INK})],
          [("Ook zo: ", {"size": 11.5, "color": INK}), ("voy a limpiar (U9) · puedo limpiar (U6) · tienes que limpiar",  {"size": 12, "bold": True, "color": F_VERB}),
           ("   —   en de ", {"size": 11.5, "color": INK}), ("que", {"size": 12.5, "bold": True, "color": RED}),
           (" mag nooit weg na hay / tengo / tienes.", {"size": 11.5, "color": INK})]])
    text(s, Inches(0.6), Inches(5.52), Inches(12.2), Inches(0.35),
         [[("Construye · bouw zelf (klik voor de oplossing): ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("algemeen + ordenar los armarios  ·  ík + fregar los platos  ·  geleerd + planchar", {"size": 13, "color": INK})]])
    exercise_solucion(s, Inches(0.8), Inches(5.95), Inches(11.7), Inches(0.5),
        [[("Hay que ordenar los armarios. · Tengo que fregar los platos. · Sé planchar.", {"bold": True, "color": GD, "size": 13})]])
    noodroute(s)
    notes(s, "Werkvorm: bouw hardop in koor. Wijs blok 1 aan (hay que / tengo que / sé), dan blok 3 (het infinitivo) en de klas zegt de volledige zin; klik daarna de zin open ter controle. Daarna variëren: laat leerlingen zelf een tarea roepen. Kernidee van de máquina: blok 1 is een VASTE CHUNK (hay que · tengo que · tienes que · sé) en blok 2 dwingt het HELE werkwoord af — zo hoeven leerlingen niets te vervoegen (de paradigma's van «tener» en «saber» komen in C5). Verbind expliciet met U6 (puedo + infinitivo) en U9 (voy a + infinitivo): vijf formules, één patroon. Kleurcode: werkwoord = oranje (§13); de rode middenblok = de huisstijlkleur van C4. Oplossing: Hay que ordenar los armarios. · Tengo que fregar los platos. · Sé planchar. Doelcodes: C4-WS-1 · C4-TS-3 · C4-SP-2 · C4-MEC-2.")
    footer(s, tab=FTAB, page=pg())

# ── Funciones-comunicativas-dia (matrix C) — leest de gedeelde funciones_data ──
import sys as _sys
_sys.path.insert(0, os.path.join(os.path.dirname(HERE), "web"))
import funciones_data as FD
FUNC_UNIT = 10

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
    # adaptieve rijhoogte: bij 22 funciones (U10, incl. de nieuwe F21/F22) mag geen
    # rij van de dia vallen → pitch schaalt met het aantal rijen (blijft ≤ 1.32);
    # bij veel funciones zakken ook de binnenmarge én de fontgrootte van de
    # exponentes-regel mee (en wordt die regel op een «·»-grens ingekort).
    nrows = (len(fs) + 1) // 2
    top = 1.82; bottom = 7.0
    pitch = min(1.32, (bottom - top) / nrows)
    ch = pitch - (0.16 if pitch > 0.80 else 0.10)
    off = 0.05 if pitch > 0.80 else 0.03
    tsz = 11 if have <= 16 else (10.5 if have <= 18 else (10 if have <= 20 else 9.5))
    exsz = 8.5 if have <= 14 else (7.0 if have <= 16 else (6.3 if have <= 18 else (6.0 if have <= 20 else 5.6)))
    excap = 300 if have <= 16 else (235 if have <= 18 else (205 if have <= 20 else 175))
    for i,f in enumerate(fs):
        col=i%2; row=i//2
        x=cols_x[col]; y=Inches(top+row*pitch)
        st=FD.status(f,FUNC_UNIT); hot = st in ("nueva","nivel")
        card(s,x,y,w,Inches(ch),fill=(GT if hot else WHITE),line=(G if hot else LINE))
        badge = "  ● NUEVA" if st=="nueva" else ("  ▲ nivel+" if st=="nivel" else "")
        text(s,x+Inches(0.22),y+Inches(off),w-Inches(0.44),Inches(min(0.28, ch*0.5)),
             [[(f["es"], {"size":tsz,"bold":True,"color":INK,"font":DISPLAY}),(badge,{"size":9,"bold":True,"color":GD})]])
        exps=" · ".join(e for u in sorted(k for k in f["exp"] if k<=FUNC_UNIT) for e in f["exp"][u])
        text(s,x+Inches(0.22),y+Inches(off)+Inches(ch*0.42),w-Inches(0.44),Inches(max(0.12, ch*0.5)),
             [[(_cap_exps(exps, excap),{"size":exsz,"color":MUT})]])
    footer(s, tab=FTAB, page=pg())

def _run_all_slides(include_teacher=True):
    # dia-indexen (0-based) = de hyperlink-targets van de menutegels in s02_menu:
    # 0 título · 1 menú · 2 escucha · 3 suena bien · 4 la máquina de frases ·
    # 5 kit · 6 kit (hay que / problemitas) · 7 gram hay que · 8 gram saber ·
    # 9 práctica · 10 hablar · 11 cultura · 12 tarea · 13 funciones · 14 repaso ·
    # (15 docentendossier)
    s01_title(); s02_menu(); s03_escucha(); s_uitspraak(); s_maquina()
    s04_kit(); s05_kit2(); s06_gram_hayque()
    s07_gram_saber(); s08_practica(); s09_speaking()
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
