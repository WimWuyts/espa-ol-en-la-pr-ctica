#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_c4u11_ppt.py — Interactieve PowerPoint C4 · Unidad 11 «El tiempo y los gustos»
================================================================================
Gedeelde builder (één bron) → TWEE decks:
  · C4_U11_docente.pptx  — docentversie: vrije navigatie; antwoorden verschijnen bij
    klik (fade) + volledige oplossing & didactiek in de spreker-notities.
  · C4_U11_alumno.ppsx   — leerlingversie: GEEN docentnotities, GEEN kiosk; gewone
    diavoorstelling waarin de antwoorden/oplossingen bij klik verschijnen.

ECHTE interactiviteit: op elke oefendia wordt <p:timing>-XML geïnjecteerd met
standaard SEQUENTIËLE on-click entrance-animaties (fade-in) in de hoofdsequentie
(mainSeq): elke klik onthult de volgende reveal-shape. + hyperlink-navigatie
(menutegels, ⌂ Menú). Cast-avatars = de ECHTE flat-vector SVG's.

Thema U11: El tiempo y los gustos · het weer met «hace + sustantivo» (hace frío ·
hace calor · hace viento · hace sol · hace buen/mal tiempo — één vaste vorm, net als
hay) tegenover «tengo frío» (een persoon) · de estaciones · gustos met «me gusta» (één
ding of + infinitivo) ↔ «me gustan» (meervoud), plus te/le gusta en de reactie-chunks
(a mí también · a mí tampoco · a mí no · a mí sí) · adverbios de frecuencia (siempre ·
casi siempre · a veces · casi nunca · nunca + tres veces por semana · todos los años).
Eindtaak «Mi estación favorita» — een ficha + een enquête in de klas.
Huisstijl: unitkleur rood #D64550 (C4). Spaans-eerst + NL-steun. Twee kleurlagen:
cursusrood (navigatie) + functionele taalsemantiek (WERKWOORD = oranje #EA7317 ·
tijd/frecuencia = paars #7C3AED · persoon = blauw · rood = valstrik). Visueel element:
«La máquina de frases» met DRIE rijen (Hace / Me gusta / Me gustan + wat erop volgt).

TWEE VALSTRIKKEN, elk in een eigen opvallend kader (§4-gramática + repaso):
  (1) het weer «doet» iets: hace frío/calor — nooit «es frío»/«está frío»; en let op
      wie het koud heeft: hace frío (het weer) ↔ tengo frío (ík, U9);
  (2) me gusta draait de zin om («het bevalt mij»), dus HET DING kiest de vorm:
      me gusta el cine ↔ me gustan los deportes — nooit «yo gusto el cine».

VIDEO: voor aflevering 11 bestaat GEEN YouTube-link. De bron is een Google-Drive-
bestand (file-id 1saLd6_-eTVUTVbv1v8KbKwfYp3Ale6-D, deelrechten reader/anyone).
De online-video-embed gebruikt daarom de Drive-/preview-URL; daarnaast staat er een
gewone hyperlink-knop «▶ Abrir en Drive» als gegarandeerde noodroute (browser).
Internet vereist.

C4-scope: «me/te/le gusta(n)» zijn VASTE CHUNKS — géén volledig pronomensysteem en
géén gustar-paradigma (dat hoort in C6). «hace» presenteren als één onveranderlijke
vorm, niet als vervoeging van hacer (systeem = C5). Géén futuro/condicional/subjuntivo.

NB: in het bronscript van aflevering 11 stonden de sprekerlabels van escena 1 deels
verwisseld (bijna alles op «Julio»). De beurten zijn gereconstrueerd tot een coherente
drieluik-scène (Julio · camarero · clienta) — zie de docentnotitie bij de escucha-dia.

Bron: 03-build/web/gen_c4u11_kgt.py · gen_c4u11_pdf.py · gen_c4u11_practica.py
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
OUT_DOCENTE = os.path.join(HERE, "C4_U11_docente.pptx")
OUT_ALUMNO_PPTX = os.path.join(HERE, "C4_U11_alumno.pptx")
OUT_ALUMNO = os.path.join(HERE, "C4_U11_alumno.ppsx")

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
F_VERB = RGBColor(0xEA, 0x73, 0x17)  # WERKWOORD          (oranje · U11: hace / gustar — dominante laag)
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

def footer(s, tab="U11 · TIEMPO", page=None):
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
# C4 · UNIDAD 11 «El tiempo y los gustos» — slides (survival). Herbruikt de machinerie.
# ============================================================================
FTAB = "U11 · TIEMPO"

def s01_title():
    s = slide(); bg(s)
    rect(s, 0, 0, EMU_W, Inches(4.7), fill=G)
    rect(s, 0, Inches(4.62), EMU_W, Inches(0.08), fill=GD)
    chip(s, Inches(0.6), Inches(0.5), "C4 · LA RUTA · EL DESPEGUE · PARADA 11", fill=WHITE, tcolor=G, size=12)
    text(s, Inches(0.55), Inches(1.15), Inches(12.3), Inches(1.1),
         [[("El tiempo y los gustos", {"size": 44, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(0.6), Inches(2.25), Inches(11.8), Inches(0.7),
         [[("¡Uh, hace mucho viento! ", {"size": 26, "bold": True, "color": WHITE, "font": DISPLAY}),
           ("— A mí me gusta más el frío.", {"size": 17, "italic": True, "color": GT})]])
    text(s, Inches(0.6), Inches(3.2), Inches(11.5), Inches(1.1),
         [[("Praten over het ", {"size": 16, "color": WHITE}), ("weer", {"size": 16, "bold": True, "color": WHITE}),
           (", over wat je ", {"size": 16, "color": WHITE}), ("graag doet", {"size": 16, "bold": True, "color": WHITE}),
           (" en ", {"size": 16, "color": WHITE}), ("hoe vaak", {"size": 16, "bold": True, "color": WHITE}),
           (" (hace frío · me gusta · casi nunca).", {"size": 16, "color": WHITE})],
          [("Survival in Spanish — in een bar praten Julio en de camarero over hun vakantie… en een clienta mengt zich in het gesprek.", {"size": 13, "italic": True, "color": GT})]])
    avatar(s, "mochila", Inches(10.7), Inches(4.95), d=Inches(1.7))
    text(s, Inches(0.6), Inches(5.25), Inches(9), Inches(1.5),
         [[("En esta unidad vas a…", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})],
          [("• Hablar del tiempo  ", {"size": 13, "color": INK}), ("hace frío · hace calor · hace viento · ¿qué tiempo hace?", {"size": 11, "italic": True, "color": MUT})],
          [("• Nombrar las estaciones  ", {"size": 13, "color": INK}), ("la primavera · el verano · el otoño · el invierno", {"size": 11, "italic": True, "color": MUT})],
          [("• Expresar gustos  ", {"size": 13, "color": INK}), ("me gusta el cine ↔ me gustan los deportes · a mí también", {"size": 11, "italic": True, "color": MUT})],
          [("• Decir con qué frecuencia  ", {"size": 13, "color": INK}), ("siempre · a veces · casi nunca · tres veces por semana", {"size": 11, "italic": True, "color": MUT})]])
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
             ("2", "Suena bien", "la s siempre sorda", 3),
             ("3", "La máquina de frases", "hace / me gusta / me gustan", 4),
             ("4", "Kit", "el tiempo · los gustos", 5),
             ("5", "Gramática", "hace + sustantivo · gustar", 7),
             ("6", "Práctica", "oefenen samen", 9),
             ("7", "Hablar", "la encuesta de gustos", 10),
             ("8", "Cultura", "un idioma, 21 climas", 11),
             ("9", "Tarea", "Mi estación favorita", 12),
             ("10", "Repaso", "wat kun je nu?", 14)]
    x0, y0 = Inches(0.55), Inches(1.7)
    w = Inches(3.0); gx = Inches(0.18); gy = Inches(0.2)
    for i, t in enumerate(tiles):
        col = i % 4; row = i // 4
        _tile(s, x0 + col * (w + gx), y0 + row * (Inches(1.15) + gy), w, *t)
    text(s, Inches(0.6), Inches(5.95), Inches(12), Inches(0.9),
         [[("Consejo · Tip. ", {"size": 12, "bold": True, "color": GD, "font": DISPLAY}),
           ("Het weer «doet» iets: hace frío · hace calor (nooit «es frío»). En bij gustar kiest HET DING de vorm: me gusta el cine ↔ me gustan los deportes.", {"size": 12, "italic": True, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

# ── Online-video inbedden zodat hij ÍN PowerPoint afspeelt ────────────────────
# Bron U11 = GOOGLE DRIVE (net als U8–U10 bestaat er voor deze aflevering géén
# YouTube-link): file-id 1saLd6_-eTVUTVbv1v8KbKwfYp3Ale6-D, deelrechten
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
DRIVE_ID="1saLd6_-eTVUTVbv1v8KbKwfYp3Ale6-D"
VIDEO_URL="https://drive.google.com/file/d/%s/preview"%DRIVE_ID   # embed-URL (in-app speler)
VIDEO_WATCH="https://drive.google.com/file/d/%s/view"%DRIVE_ID    # browser-URL (noodroute)
VIDEO_TOP="Sitcom · Episodio 11"; VIDEO_MAIN="Aquí hace demasiado calor"
VIDEO_POSTER=os.path.join(HERE,"assets","video_poster_U11.png")
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
    """<url> = de VOLLEDIGE embed-URL (U1–U7: youtube.com/embed/<id> · U8–U11: de
    Drive-/preview-URL). De markup eronder is ongewijzigd t.o.v. U1–U10."""
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
    sectionbar(s, "§1 · ¡ESCUCHA!", "Bekijk la escena y escucha", "Kijk & luister — in de bar gaat het over vakantie, het weer en wat ze graag doen", num=1)
    card(s, Inches(0.55), Inches(1.55), Inches(7.4), Inches(4.9), fill=WHITE, line=LINE)
    dia = [("Camarero", "Ella se va de vacaciones a la playa, a Canarias.", F_PLAC),
           ("Camarero", "Siempre hace buen tiempo en Canarias.", F_VERB),
           ("Camarero", "Son cuatro cincuenta.", F_OBJ),
           ("Julio", "Yo no, yo voy al pueblo de mis padres, en Ávila.", F_PLAC),
           ("Julio", "Pero hace un frío… Nunca hace ese frío en Madrid.", F_VERB),
           ("Camarero", "Lo bueno es que puedes estar con tu familia.", F_SUBJ),
           ("Camarero", "Pasas las fiestas de Navidad con los tuyos: tus tíos, tus cuñados.", F_SUBJ),
           ("Julio", "A veces te cansas de restaurantes y playas. La familia es para siempre.", F_TIME),
           ("Julio", "¿Y tú te quedas en Madrid?", F_SUBJ),
           ("Camarero", "Yo voy todos los años al Caribe.", F_TIME),
           ("Camarero", "Es que me gusta hacer submarinismo.", F_VERB),
           ("Camarero", "A ella también le gusta hacer submarinismo.", F_VERB),
           ("Julio", "En Ávila es difícil, ¿sabes? Yo voy mucho al cine.", F_TIME),
           ("Clienta", "Me gusta el cine y me gusta la ópera.", F_VERB),
           ("Julio", "Casi nunca voy a la ópera.", F_TIME),
           ("Clienta", "Y los deportes: voy al gimnasio tres veces por semana.", F_TIME),
           ("Clienta", "¡Uh, hace mucho viento! En invierno hace frío.", F_VERB),
           ("Clienta", "En verano, en cambio, hace calor.", F_VERB),
           ("Julio", "A mí me gusta más el frío.", F_VERB),
           ("Clienta", "En mi casa hace calor.", F_VERB)]
    y = Inches(1.72)
    for sp, tx, col in dia:
        chip(s, Inches(0.72), y, sp, fill=col, tcolor=WHITE, size=9.5)
        text(s, Inches(1.78), y - Inches(0.02), Inches(6.1), Inches(0.42),
             [[(tx, {"size": 9.5, "color": INK})]])
        y = y + Inches(0.232)
    card(s, Inches(8.2), Inches(1.55), Inches(4.6), Inches(2.45), fill=GT, line=G)
    text(s, Inches(8.45), Inches(1.72), Inches(4.1), Inches(2.2),
         [[("Chunks para llevar 🎒", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})],
          [("Hace frío · hace calor · hace viento", {"size": 11.5, "color": INK})],
          [("Siempre hace buen tiempo · en cambio", {"size": 11.5, "color": INK})],
          [("Me gusta el cine · me gustan los deportes", {"size": 11.5, "color": INK})],
          [("A ella también le gusta · me gusta más", {"size": 11.5, "color": INK})],
          [("siempre · a veces · casi nunca · tres veces", {"size": 11.5, "color": INK})]])
    text(s, Inches(8.2), Inches(4.12), Inches(2.95), Inches(0.3),
         [[("🎬 Episodio 11 — klik om af te spelen", {"size": 11, "bold": True, "color": GD, "font": DISPLAY})]])
    btn, _bw = chip(s, Inches(11.2), Inches(4.09), "▶ Abrir en Drive", fill=G, tcolor=WHITE, size=9.5)
    try:
        btn.click_action.hyperlink.address = VIDEO_WATCH
    except Exception:
        pass
    add_online_video(s, VIDEO_URL, Inches(8.2), Inches(4.45), Inches(4.6), Inches(2.55), VIDEO_POSTER)
    notes(s, "De video van aflevering 11 komt uit GOOGLE DRIVE (er is voor deze aflevering géén YouTube-link): file-id 1saLd6_-eTVUTVbv1v8KbKwfYp3Ale6-D, deelrechten reader/anyone → INTERNET VEREIST. Klik op de poster om in PowerPoint af te spelen; lukt dat niet, klik dan de knop «▶ Abrir en Drive» (of open " + VIDEO_WATCH + " in een browser). LET OP: in het aangeleverde transcript stonden de sprekerlabels van escena 1 deels verwisseld (bijna alles op «Julio»); de beurten zijn hier gereconstrueerd tot een coherente scène met drie stemmen (Julio · camarero · clienta). Aanpak: eerst één keer kijken zónder transcript (globaal: wie gaat waarheen op vakantie, en welk weer is het daar?), daarna met het transcript. Laat de leerlingen drie kolommen maken: EL TIEMPO (hace buen tiempo · hace un frío · hace mucho viento · hace calor) ↔ LOS GUSTOS (me gusta hacer submarinismo · me gusta el cine · me gusta la ópera · me gusta más el frío) ↔ LA FRECUENCIA (siempre · nunca · a veces · casi nunca · todos los años · tres veces por semana · mucho). Wijs op «A ella también le gusta» — dezelfde chunk met een andere persoon. Doelcodes: C4-LU-1 · C4-STR-1 · C4-WS-1.")
    footer(s, tab=FTAB, page=pg())

def s04_kit():
    s = slide(); bg(s)
    sectionbar(s, "§2 · KIT", "El tiempo · las estaciones · el ocio", "Het weer beschrijven, de seizoenen benoemen en zeggen wat je graag doet", num=2)
    cols = [("¿Qué tiempo hace? 🌤️", [("Hace frío", "het is koud"), ("Hace calor", "het is warm"),
              ("Hace sol", "het is zonnig"), ("Hace viento", "het waait"),
              ("Hace buen / mal tiempo", "het is mooi / slecht weer"), ("¿Qué tiempo hace?", "wat voor weer is het?")]),
            ("Las estaciones 🍂", [("la primavera", "de lente"), ("el verano", "de zomer"),
              ("el otoño", "de herfst"), ("el invierno", "de winter"),
              ("en verano · en invierno", "in de zomer · in de winter"), ("demasiado calor", "te warm")]),
            ("Me gusta… · el ocio ❤️", [("Me gusta el cine", "ik hou van film"), ("Me gustan los deportes", "ik hou van sport"),
              ("Me gusta hacer yoga", "ik doe graag yoga"), ("el gimnasio", "de sportzaal"),
              ("hacer submarinismo", "duiken"), ("¿Te gusta…?", "hou jij van…?")])]
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
    sectionbar(s, "§2 · KIT", "La frecuencia · reaccionar a los gustos", "Zeggen hoe vaak je iets doet — en reageren op wat iemand graag heeft", num=2)
    left = [("siempre · casi siempre", "altijd · bijna altijd"), ("a veces", "soms"),
            ("casi nunca · nunca", "bijna nooit · nooit"), ("tres veces por semana", "drie keer per week"),
            ("todos los años", "elk jaar")]
    right = [("A mí también", "ik ook (bij een + zin)"), ("A mí tampoco", "ik ook niet (bij een − zin)"),
             ("A mí no", "ik niet"), ("A mí sí", "ik wel"),
             ("¡Qué bien! · en cambio", "wat goed! · daarentegen")]
    card(s, Inches(0.55), Inches(1.6), Inches(6.0), Inches(4.9), fill=GT, line=G)
    text(s, Inches(0.8), Inches(1.78), Inches(5.5), Inches(0.5),
         [[("¿Con qué frecuencia? 🔁", {"size": 13.5, "bold": True, "color": GD, "font": DISPLAY})]])
    y = Inches(2.5)
    for es, nl in left:
        text(s, Inches(0.8), y, Inches(5.4), Inches(0.6), [[(es, {"size": 15, "bold": True, "color": INK}), ("   " + nl, {"size": 11, "italic": True, "color": MUT})]])
        y = y + Inches(0.72)
    card(s, Inches(6.8), Inches(1.6), Inches(6.0), Inches(4.9), fill=WHITE, line=LINE)
    text(s, Inches(7.05), Inches(1.78), Inches(5.5), Inches(0.5),
         [[("Reaccionar 🙋", {"size": 13.5, "bold": True, "color": GD, "font": DISPLAY})]])
    y = Inches(2.5)
    for es, nl in right:
        text(s, Inches(7.05), y, Inches(5.4), Inches(0.6), [[(es, {"size": 15, "bold": True, "color": INK}), ("   " + nl, {"size": 11, "italic": True, "color": MUT})]])
        y = y + Inches(0.72)
    text(s, Inches(0.8), Inches(5.7), Inches(11.9), Inches(0.7),
         [[("¡Ojo! ", {"size": 12, "bold": True, "color": RED}),
           ("«siempre · nunca · a veces» staan vóór het werkwoord (nunca voy a la ópera) · «tres veces por semana» komt achteraan.", {"size": 12, "italic": True, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

def s06_gram_hace():
    s = slide(); bg(s)
    sectionbar(s, "§4 · GRAMÁTICA", "hace + sustantivo — hablar del tiempo", "Het weer «doet» iets: één vaste vorm die nooit verandert", num=4)
    legend_func(s, Inches(0.55), Inches(1.42))
    card(s, Inches(0.55), Inches(1.9), Inches(7.6), Inches(4.1), fill=WHITE, line=LINE)
    text(s, Inches(0.8), Inches(2.05), Inches(7.1), Inches(0.4), [[("hace  +  frío · calor · viento · sol · buen tiempo", {"size": 15, "bold": True, "color": GD, "font": DISPLAY})]])
    filas = [("hace frío / calor", "het is koud / warm", "En invierno hace frío."),
             ("hace viento / sol", "het waait / het is zonnig", "¡Hace mucho viento!"),
             ("hace buen/mal tiempo", "het is mooi/slecht weer", "Siempre hace buen tiempo en Canarias.")]
    y = Inches(2.6)
    for chunk, nl, ex in filas:
        rect(s, Inches(0.8), y, Inches(2.15), Inches(0.42), fill=RGBColor(0xFE,0xF1,0xE7), line=None, round=True, radius=0.2)
        text(s, Inches(0.8), y + Inches(0.02), Inches(2.15), Inches(0.38),
             [[(chunk, {"size": 12.5, "bold": True, "color": F_VERB, "font": DISPLAY})]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text(s, Inches(3.08), y + Inches(0.02), Inches(1.75), Inches(0.38),
             [[(nl, {"size": 11.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, Inches(4.9), y + Inches(0.02), Inches(3.1), Inches(0.38),
             [[(ex, {"size": 11, "italic": True, "color": MUT})]], anchor=MSO_ANCHOR.MIDDLE)
        y = y + Inches(0.52)
    rect(s, Inches(0.8), Inches(4.25), Inches(7.1), Inches(0.68), fill=GT, line=G, lw=1.4, round=True, radius=0.1)
    text(s, Inches(0.95), Inches(4.32), Inches(6.8), Inches(0.58),
         [[("«hace» no cambia nunca: ", {"size": 12.5, "bold": True, "color": GD}), ("hace ", {"size": 13, "bold": True, "color": F_VERB}),
           ("frío · calor · viento  —  ", {"size": 13, "color": INK}),
           ("net als «hay» en «hay que» (U10).", {"size": 12, "italic": True, "color": MUT})]])
    text(s, Inches(0.8), Inches(5.05), Inches(7.1), Inches(0.9),
         [[("⚠️ ", {"size": 12}), ("Nooit ", {"size": 12, "color": INK}), ("es frío", {"size": 12.5, "bold": True, "color": RED}),
           (" of ", {"size": 12, "color": INK}), ("está frío", {"size": 12.5, "bold": True, "color": RED}),
           (" voor het weer.", {"size": 12, "color": INK})],
          [("Y para preguntar: ", {"size": 12, "color": INK}), ("¿Qué tiempo hace hoy? · ¿Hace frío en Bélgica?", {"size": 12, "bold": True, "color": F_VERB})]])
    card(s, Inches(8.4), Inches(1.9), Inches(4.4), Inches(4.1), fill=GT, line=G)
    chip(s, Inches(8.6), Inches(1.76), "🔎 FÍJATE · EN LA ESCENA", fill=G, tcolor=WHITE, size=9.5)
    text(s, Inches(8.65), Inches(2.3), Inches(3.9), Inches(2.4),
         [[("Je hoorde het al:", {"size": 12, "bold": True, "color": GD, "font": DISPLAY})],
          [("«Siempre ", {"size": 13, "color": INK}), ("hace", {"size": 13, "bold": True, "color": F_VERB}), (" buen tiempo.»", {"size": 13, "color": INK})],
          [("«Pero ", {"size": 13, "color": INK}), ("hace", {"size": 13, "bold": True, "color": F_VERB}), (" un frío…»", {"size": 13, "color": INK})],
          [("«¡", {"size": 13, "color": INK}), ("Hace", {"size": 13, "bold": True, "color": F_VERB}), (" mucho viento!»", {"size": 13, "color": INK})],
          [("«En verano ", {"size": 13, "color": INK}), ("hace calor", {"size": 13, "bold": True, "color": F_VERB}), (".»", {"size": 13, "color": INK})]])
    rect(s, Inches(8.65), Inches(4.62), Inches(3.9), Inches(1.3), fill=RGBColor(0xFD,0xE8,0xE8), line=RED, lw=2.0, round=True, radius=0.08)
    text(s, Inches(8.8), Inches(4.72), Inches(3.65), Inches(1.15),
         [[("¡OJO! el tiempo ↔ la persona", {"size": 11, "bold": True, "color": RED, "font": DISPLAY})],
          [("hace frío", {"size": 13, "bold": True, "color": F_VERB}), (" = het ís koud", {"size": 12, "color": INK})],
          [("tengo frío", {"size": 13, "bold": True, "color": F_SUBJ}), (" = ík heb het koud", {"size": 12, "color": INK})],
          [("(tener + naamwoord, U9)", {"size": 10, "italic": True, "color": MUT})]])
    notes(s, "«hace + sustantivo» is de standaardmanier om over het weer te praten. Presenteer «hace» als ÉÉN onveranderlijke vorm — niet als vervoeging van «hacer» (dat systeem hoort in het 5de jaar, C5). De parallel met «hay» en «hay que» (U10) is didactisch handig: drie vaste vormen zonder persoon. DE VALSTRIK voor Nederlandstaligen: wij zeggen «het IS koud», dus leerlingen produceren spontaan «es frío» of «está frío» — beide fout voor het weer. Zet daar ook meteen het contrast met de persoon naast: «hace frío» (het weer) ↔ «tengo frío» (ík heb het koud, recycling U9 tener + naamwoord); dat onderscheid is een klassieke bron van fouten. Extra chunks: «hace un frío» (met un = versterkend: het is ijskoud) en «demasiado calor» (te warm). Doelcodes: C4-WS-1 · C4-TS-3 · C4-LU-1.")
    footer(s, tab=FTAB, page=pg())

def s07_gram_gustar():
    s = slide(); bg(s)
    sectionbar(s, "§4 · GRAMÁTICA", "me gusta ↔ me gustan — expresar gustos", "«Het bevalt mij»: het ding kiest de vorm, niet jij", num=4)
    card(s, Inches(0.55), Inches(1.42), Inches(6.05), Inches(1.62), fill=WHITE, line=LINE)
    text(s, Inches(0.8), Inches(1.54), Inches(5.6), Inches(0.35), [[("me gusta · me gustan · te / le gusta", {"size": 13.5, "bold": True, "color": GD, "font": DISPLAY})]])
    filas = [("me gusta", "ik hou van (1 ding / werkwoord)", "Me gusta el cine."),
             ("me gustan", "ik hou van (meervoud)", "Me gustan los deportes."),
             ("te / le gusta", "jij / hij-zij houdt van", "A ella también le gusta.")]
    y = Inches(1.92)
    for chunk, nl, ex in filas:
        text(s, Inches(0.8), y, Inches(5.6), Inches(0.36),
             [[(chunk + "  ", {"size": 13.5, "bold": True, "color": F_VERB, "font": DISPLAY}),
               (nl + "   ", {"size": 10.5, "color": INK}), (ex, {"size": 10.5, "italic": True, "color": MUT})]])
        y = y + Inches(0.36)
    text(s, Inches(0.8), Inches(2.76), Inches(5.6), Inches(0.3),
         [[("Letterlijk: «het ", {"size": 11, "italic": True, "color": MUT}), ("bevalt", {"size": 11, "bold": True, "color": GD}), (" mij» → daarom kiest het ding de vorm.", {"size": 11, "italic": True, "color": MUT})]])
    card(s, Inches(6.75), Inches(1.42), Inches(6.05), Inches(1.62), fill=CREMA, line=LINE)
    text(s, Inches(7.0), Inches(1.54), Inches(5.6), Inches(0.35), [[("¿Uno o varios? · el truco", {"size": 13.5, "bold": True, "color": GD, "font": DISPLAY})]])
    mv1 = rect(s, Inches(7.0), Inches(1.96), Inches(2.85), Inches(0.92), fill=RGBColor(0xFE,0xF1,0xE7), line=None, round=True, radius=0.1)
    text(s, Inches(7.12), Inches(2.02), Inches(2.65), Inches(0.85),
         [[("☝️ 1 ding / werkwoord", {"size": 9.5, "bold": True, "color": RGBColor(0xB4,0x53,0x0E)})],
          [("Me gusta el cine.", {"size": 12, "bold": True, "color": INK})],
          [("Me gusta hacer yoga.", {"size": 12, "bold": True, "color": INK})]])
    mv2 = rect(s, Inches(9.95), Inches(1.96), Inches(2.85), Inches(0.92), fill=RGBColor(0xE8,0xF0,0xFE), line=None, round=True, radius=0.1)
    text(s, Inches(10.07), Inches(2.02), Inches(2.65), Inches(0.85),
         [[("✌️ meervoud", {"size": 9.5, "bold": True, "color": RGBColor(0x1E,0x40,0xAF)})],
          [("Me gustan los deportes.", {"size": 12, "color": INK})],
          [("No me gustan los hoteles.", {"size": 12, "color": INK})]])
    card(s, Inches(0.55), Inches(3.16), Inches(6.05), Inches(1.28), fill=RGBColor(0xFD,0xE8,0xE8), line=RED, lw=2.4)
    chip(s, Inches(0.75), Inches(3.02), "¡OJO! · LA TRAMPA 1", fill=RED, tcolor=WHITE, size=9.5)
    text(s, Inches(0.8), Inches(3.42), Inches(5.6), Inches(1.0),
         [[("«ik hou van film» = ", {"size": 13, "color": INK}), ("me gusta el cine", {"size": 16, "bold": True, "color": F_VERB, "font": DISPLAY})],
          [("nooit ", {"size": 12, "color": INK}), ("yo gusto el cine", {"size": 12.5, "bold": True, "color": RED}),
           (" — dat betekent «ik val in de smaak».", {"size": 12, "color": INK})]])
    card(s, Inches(6.75), Inches(3.16), Inches(6.05), Inches(1.28), fill=RGBColor(0xFD,0xE8,0xE8), line=RED, lw=2.4)
    chip(s, Inches(6.95), Inches(3.02), "¡OJO! · LA TRAMPA 2", fill=RED, tcolor=WHITE, size=9.5)
    text(s, Inches(7.0), Inches(3.42), Inches(5.6), Inches(1.0),
         [[("het ", {"size": 12, "color": INK}), ("ding", {"size": 12.5, "bold": True, "color": RED}),
           (" kiest de vorm: me gusta ", {"size": 12, "color": INK}), ("el frío", {"size": 12.5, "bold": True, "color": INK}),
           (" ↔ me gustan ", {"size": 12, "color": INK}), ("los deportes", {"size": 12.5, "bold": True, "color": INK})],
          [("dus niet ", {"size": 12, "color": INK}), ("me gusta los deportes", {"size": 11.5, "bold": True, "color": RED}),
           (" · niet ", {"size": 12, "color": INK}), ("me gustan el cine", {"size": 11.5, "bold": True, "color": RED})]])
    card(s, Inches(0.55), Inches(4.56), Inches(12.25), Inches(0.78), fill=GT, line=G)
    text(s, Inches(0.8), Inches(4.64), Inches(11.8), Inches(0.65),
         [[("Reaccionar · ", {"size": 12.5, "bold": True, "color": GD, "font": DISPLAY}),
           ("«— Me gusta el cine. — ", {"size": 12, "color": INK}),
           ("A mí también", {"size": 12.5, "bold": True, "color": F_VERB}), (".»   ·   «— No me gusta la ópera. — ", {"size": 12, "color": INK}),
           ("A mí tampoco", {"size": 12.5, "bold": True, "color": F_VERB}), (".»", {"size": 12, "color": INK})],
          [("Bij een ", {"size": 11.5, "color": INK}), ("+ zin", {"size": 11.5, "bold": True, "color": GD}),
           (": a mí también / a mí no   ·   bij een ", {"size": 11.5, "color": INK}), ("− zin", {"size": 11.5, "bold": True, "color": GD}),
           (": a mí tampoco / a mí sí", {"size": 11.5, "color": INK})]])
    text(s, Inches(0.6), Inches(5.45), Inches(12.2), Inches(0.4),
         [[("Completa · vul aan (klik voor de oplossing): ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("Me gust___ los deportes.   Me gust___ hacer yoga.   — No me gusta el calor. — ¡A mí ___! (jij wel)", {"size": 13, "color": INK})]])
    exercise_solucion(s, Inches(0.8), Inches(5.88), Inches(11.7), Inches(0.5),
        [[("gustan · gusta · sí", {"bold": True, "color": GD, "size": 13})]])
    noodroute(s)
    notes(s, "«gustar» werkt omgekeerd aan ons «houden van»: letterlijk «het bevalt mij». Daarom bepaalt HET DING de vorm — niet de spreker. Vuistregel voor de klas: één ding of een heel werkwoord → gusta · meervoud → gustan. TWEE VALSTRIKKEN: (1) nooit «yo gusto el cine» (dat betekent «ik val in de smaak»); (2) de vorm volgt het ding, dus niet «me gusta los deportes». Houd het bij VASTE CHUNKS: me gusta / me gustan / te gusta / le gusta — géén volledig pronomensysteem en géén gustar-paradigma (dat hoort in C6). De reactiechunks (a mí también · a mí tampoco · a mí no · a mí sí) zijn goud voor interactie: laat ze meteen in de enquête gebruiken. Let op: bij een negatieve zin is «tampoco» de juiste reactie — dat is voor Nederlandstaligen niet intuïtief («ik ook niet»). Oplossing: gustan · gusta · sí. Doelcodes: C4-SP-2 · C4-GE-3 · C4-TS-3.")
    footer(s, tab=FTAB, page=pg())

def s08_practica():
    s = slide(); bg(s)
    sectionbar(s, "§3 · PRÁCTICA", "Completa el diálogo", "Vul samen aan — klik voor de oplossing", num=3)
    card(s, Inches(0.55), Inches(1.7), Inches(7.6), Inches(4.5), fill=WHITE, line=LINE)
    lines = ["— ¡Uf! Aquí ___ demasiado calor.",
             "— A mí me ___ más el frío.",
             "— ¿Y los deportes?",
             "— Sí, me ___ mucho.",
             "— Voy al gimnasio tres ___ por semana.",
             "— ¡A mí ___!"]
    y = Inches(1.95)
    for q in lines:
        text(s, Inches(0.8), y, Inches(7.1), Inches(0.6), [[(q, {"size": 16, "color": INK})]])
        y = y + Inches(0.7)
    exercise_solucion(s, Inches(8.4), Inches(1.9), Inches(4.4), Inches(4.0),
        [[("1. hace", {"color": GD, "size": 14})], [("2. gusta", {"color": GD, "size": 14})],
         [("3. gustan", {"color": GD, "size": 14})], [("4. veces", {"color": GD, "size": 14})],
         [("5. también", {"color": GD, "size": 14})]],
        title_doc="SOLUCIÓN · docent")
    noodroute(s)
    notes(s, "Laat leerlingen eerst zelf proberen (in duo, hardop). Klik daarna de oplossing open. Let op: «hace demasiado calor» — het weer, dus hace; «me gusta más el frío» — één ding; «me gustan mucho» verwijst naar «los deportes» (meervoud!) — precies de valstrik; «tres veces por semana» staat achteraan; «¡a mí también!» reageert op een positieve zin. Oplossing: hace · gusta · gustan · veces · también.")
    footer(s, tab=FTAB, page=pg())

def s09_speaking():
    s = slide(); bg(s)
    sectionbar(s, "§3 · HABLAR", "La encuesta de gustos", "Vraag rond, reageer en zoek iemand met dezelfde smaak — sin leer", num=3)
    card(s, Inches(0.55), Inches(1.7), Inches(7.6), Inches(3.4), fill=GT, line=G)
    text(s, Inches(0.85), Inches(1.95), Inches(7.1), Inches(3.0),
         [[("Modelo · zeg dit hardop:", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})],
          [("«— ¿Te gusta el cine?  — Sí, me gusta mucho.", {"size": 16, "color": INK})],
          [("— ¡A mí también! ¿Y te gustan los deportes?", {"size": 16, "color": INK})],
          [("— No, no me gustan.  — A mí sí. Voy al gimnasio.", {"size": 16, "color": INK})],
          [("— ¿Y cuándo hace frío?  — Casi nunca salgo.»", {"size": 16, "color": INK})]])
    card(s, Inches(8.4), Inches(1.7), Inches(4.4), Inches(3.4), fill=WHITE, line=LINE)
    text(s, Inches(8.65), Inches(1.95), Inches(3.9), Inches(3.0),
         [[("¿Cómo? · Werkvorm", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})],
          [("1. Pregunta: «¿Te gusta…?» · «¿Te gustan…?».", {"size": 12.5, "color": INK})],
          [("2. Responde: «Sí, me gusta» / «No, no me gustan».", {"size": 12.5, "color": INK})],
          [("3. Reacciona: «a mí también / tampoco / no / sí».", {"size": 12.5, "color": INK})],
          [("4. Añade frecuencia: «voy… tres veces por semana».", {"size": 12.5, "color": INK})],
          [("5. Busca a alguien con los mismos gustos.", {"size": 12.5, "color": INK})]])
    text(s, Inches(0.6), Inches(5.4), Inches(12), Inches(0.7),
         [[("Interactie ", {"size": 12, "bold": True, "color": GD, "font": DISPLAY}),
           ("= vragen, reageren én doorvragen. Elke leerling bevraagt 3 klasgenoten. Wie vindt een «gemelo de gustos»? Verstaan? Zeg: «¿Cómo? / ¿Puedes repetir?»", {"size": 12, "italic": True, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

def s10_musica():
    s = slide(); bg(s)
    sectionbar(s, "CULTURA", "Un idioma, 21 climas", "Van eeuwige lente tot omgekeerde seizoenen — en muziek erbij", num=None)
    bandas = [("Manu Chao", "Me Gustas Tú", "🇪🇸/🇫🇷"), ("Álvaro Soler", "El Mismo Sol", "🇪🇸 España"),
              ("Juan Luis Guerra", "Ojalá Que Llueva Café", "🇩🇴 R. Dominicana"), ("Carlos Vives & Shakira", "La Bicicleta", "🇨🇴 Colombia"),
              ("Jarabe de Palo", "Bonito", "🇪🇸 España"), ("Gente de Zona & Marc Anthony", "La Gozadera", "🇨🇺 Cuba")]
    x0, y0 = Inches(0.55), Inches(1.75); w = Inches(4.0)
    for i, (ar, sg, ge) in enumerate(bandas):
        col = i % 3; row = i // 3
        x = x0 + col * (w + Inches(0.18)); y = y0 + row * (Inches(1.5) + Inches(0.18))
        card(s, x, y, w, Inches(1.5), fill=WHITE, line=LINE)
        text(s, x + Inches(0.25), y + Inches(0.2), w - Inches(0.4), Inches(1.2),
             [[(ar, {"size": 14, "bold": True, "color": INK, "font": DISPLAY})],
              [("🎵 " + sg, {"size": 12, "color": MUT})], [(ge, {"size": 11, "color": GD})]])
    card(s, Inches(0.55), Inches(5.5), Inches(12.25), Inches(1.05), fill=GT, line=G)
    text(s, Inches(0.85), Inches(5.62), Inches(11.7), Inches(0.9),
         [[("🌞 Un idioma, 21 climas ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("Julio heeft gelijk: op de ", {"size": 12, "color": INK}), ("Canarias", {"size": 12, "bold": True, "color": F_PLAC}),
           (" is het het hele jaar 20–24 °C, en ", {"size": 12, "color": INK}), ("Guatemala", {"size": 12, "bold": True, "color": F_PLAC}),
           (" heet «el país de la eterna primavera». Maar ", {"size": 12, "color": INK}), ("Ávila", {"size": 12, "bold": True, "color": F_PLAC}),
           (" is de koudste provincie van Spanje (1.130 m).", {"size": 12, "color": INK})],
          [("En ", {"size": 12, "color": INK}), ("Argentina, Chile y Uruguay", {"size": 12, "bold": True, "color": F_PLAC}),
           (" staan de estaciones ", {"size": 12, "color": INK}), ("al revés", {"size": 12, "bold": True, "color": GD}),
           (": in diciembre is het verano en viert men Navidad in de hitte. In Costa Rica betekent «invierno» het regenseizoen, niet kou. «Me gustas tú» = één lange me-gusta-oefening (LyricsTraining op de hub).", {"size": 12, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

def s11_tarea():
    s = slide(); bg(s)
    sectionbar(s, "§5 · TAREA FINAL", "Mi estación favorita", "Jouw ficha: het weer, twee smaken en hoe vaak — daarna de enquête", num=5)
    card(s, Inches(0.55), Inches(1.7), Inches(6.6), Inches(3.6), fill=WHITE, line=G, lw=1.6)
    rect(s, Inches(0.55), Inches(1.7), Inches(6.6), Inches(0.5), fill=G)
    text(s, Inches(0.75), Inches(1.76), Inches(6.2), Inches(0.4), [[("MI FICHA · El tiempo y yo", {"size": 12, "bold": True, "color": WHITE, "font": DISPLAY})]])
    filas = [("🌤️", "Mi estación favorita es…"), ("🌡️", "En … hace…"), ("❤️", "Me gusta… (1 ding)"),
             ("❤️", "Me gustan… (meervoud)"), ("🔁", "…, X veces por semana")]
    ry = Inches(2.42)
    for ic, lab in filas:
        rect(s, Inches(0.68), ry, Inches(2.7), Inches(0.48), fill=CREMA, line=LINE, lw=1.0, round=True, radius=0.08)
        text(s, Inches(0.8), ry + Inches(0.03), Inches(2.5), Inches(0.42),
             [[(ic + "  " + lab, {"size": 10, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        rect(s, Inches(3.44), ry, Inches(3.76), Inches(0.48), fill=PAPER, line=LINE, lw=1.0, round=True, radius=0.08)
        ry = ry + Inches(0.52)
    text(s, Inches(0.75), Inches(5.02), Inches(6.2), Inches(0.45),
         [[("🤝 Mi gemelo de gustos: ", {"size": 11.5, "bold": True, "color": INK}), ("____________ ", {"size": 11.5, "color": LINE}),
           ("(a los dos nos gusta ", {"size": 11.5, "bold": True, "color": INK}), ("__________ )", {"size": 11.5, "color": LINE})]])
    card(s, Inches(7.4), Inches(1.7), Inches(5.4), Inches(3.6), fill=GT, line=G)
    text(s, Inches(7.65), Inches(1.88), Inches(4.9), Inches(3.3),
         [[("Los pasos · stappen", {"size": 14, "bold": True, "color": GD, "font": DISPLAY})],
          [("1. Elige tu estación y di el tiempo: «En verano hace calor».", {"size": 12, "color": INK})],
          [("2. Dos gustos: één met «me gusta», één met «me gustan».", {"size": 12, "color": INK})],
          [("3. Añade la frecuencia: «siempre / a veces / casi nunca» + «X veces por semana».", {"size": 12, "color": INK})],
          [("4. La encuesta: pregunta a tres compañeros «¿Te gusta…?» y reacciona («a mí también / tampoco»).", {"size": 12, "color": INK})],
          [("5. Presenta: «A Sara y a mí nos gusta el cine» — sin leer.", {"size": 12, "color": INK})]])
    text(s, Inches(0.6), Inches(5.45), Inches(7.6), Inches(1.0),
         [[("🏁 Klaar als… ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("je het weer van je seizoen zegt met «hace + naamwoord», twee smaken geeft (één keer gusta, één keer gustan), één frecuencia-woord gebruikt en in de enquête minstens één keer «a mí también / a mí tampoco» zegt — zónder af te lezen.", {"size": 12, "color": INK})]])
    card(s, Inches(8.4), Inches(5.42), Inches(4.4), Inches(1.05), fill=WHITE, line=LINE)
    text(s, Inches(8.6), Inches(5.5), Inches(4.0), Inches(0.9),
         [[("Evaluatie · 🟢🟡🔴", {"size": 11.5, "bold": True, "color": GD, "font": DISPLAY})],
          [("· hace + naamwoord correct (het weer)", {"size": 10.5, "color": INK})],
          [("· me gusta ↔ me gustan correct", {"size": 10.5, "color": INK})],
          [("· frecuencia + reageren in de enquête", {"size": 10.5, "color": INK})]])
    footer(s, tab=FTAB, page=pg())

def s12_repaso():
    s = slide(); bg(s)
    sectionbar(s, "REPASO", "Lo esencial de un vistazo", "Wat je nu kunt — semáforo", num=None)
    card(s, Inches(0.55), Inches(1.7), Inches(7.6), Inches(3.3), fill=WHITE, line=LINE)
    text(s, Inches(0.85), Inches(1.85), Inches(7.1), Inches(3.1),
         [[("Zo praat je over het weer", {"size": 14, "bold": True, "color": GD, "font": DISPLAY})],
          [("Hace frío · hace calor · hace viento · hace buen tiempo", {"size": 13.5, "color": INK})],
          [("¿Qué tiempo hace? — hace verandert nooit (net als hay)", {"size": 12, "italic": True, "color": MUT})],
          [("", {"size": 6})],
          [("Zo zeg je wat je graag hebt", {"size": 14, "bold": True, "color": GD, "font": DISPLAY})],
          [("Me gusta el cine · Me gusta hacer yoga · Me gustan los deportes", {"size": 13, "color": INK})],
          [("A mí también · A mí tampoco · A mí no · A mí sí", {"size": 13, "color": INK})],
          [("", {"size": 6})],
          [("Zo zeg je hoe vaak", {"size": 14, "bold": True, "color": GD, "font": DISPLAY})],
          [("siempre → casi siempre → a veces → casi nunca → nunca · tres veces por semana", {"size": 13, "color": INK})]])
    card(s, Inches(0.55), Inches(5.15), Inches(7.6), Inches(1.0), fill=RGBColor(0xFD,0xE8,0xE8), line=RED, lw=2.0)
    text(s, Inches(0.85), Inches(5.23), Inches(7.1), Inches(0.9),
         [[("¡Ojo! · las dos trampas ", {"size": 12.5, "bold": True, "color": RED, "font": DISPLAY}),
           ("het weer: ", {"size": 12, "color": INK}), ("hace frío", {"size": 12.5, "bold": True, "color": F_VERB}),
           (" (nooit «es frío») ↔ de persoon: ", {"size": 12, "color": INK}), ("tengo frío", {"size": 12.5, "bold": True, "color": F_SUBJ}), (".", {"size": 12, "color": INK})],
          [("En bij gustar kiest ", {"size": 12, "color": INK}), ("het ding", {"size": 12.5, "bold": True, "color": RED}),
           (" de vorm: me gusta el cine ↔ me gustan los deportes — nooit «yo gusto».", {"size": 12, "color": INK})]])
    card(s, Inches(8.4), Inches(1.7), Inches(4.4), Inches(4.45), fill=GT, line=G)
    text(s, Inches(8.65), Inches(1.9), Inches(3.9), Inches(0.5), [[("Puedo… · Ik kan…", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    items = ["over het weer praten (hace frío · hace calor)", "de estaciones benoemen",
             "zeggen wat ik graag heb (me gusta / me gustan)", "reageren (a mí también / tampoco)",
             "zeggen hoe vaak (siempre · a veces · nunca)", "vragen «¿te gusta…?» in een enquête"]
    y = Inches(2.5)
    for it in items:
        text(s, Inches(8.65), y, Inches(3.9), Inches(0.7), [[("🟢🟡🔴  ", {"size": 12}), (it, {"size": 11, "color": INK})]])
        y = y + Inches(0.55)
    text(s, Inches(8.65), Inches(5.65), Inches(3.9), Inches(0.7), [[("🎮 Repasa jugando", {"size": 12, "bold": True, "color": GD, "font": DISPLAY})], [("online op de hub · el gustómetro · ¿gusta o gustan?", {"size": 11, "italic": True, "color": MUT})]])
    footer(s, tab=FTAB, page=pg())

def s13_teacher():
    s = slide(); bg(s, color=RGBColor(0x24,0x1C,0x1B))
    text(s, Inches(0.6), Inches(0.5), Inches(12), Inches(0.7), [[("Docentendossier · Unidad 11 «El tiempo y los gustos»", {"size": 22, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(0.6), Inches(1.3), Inches(12.1), Inches(5.6),
         [[("Timing (2 lesuren van 50 min).", {"size": 14, "bold": True, "color": RGBColor(0xFB,0xEA,0xEC), "font": DISPLAY})],
          [("Les 1: Escucha (sitcom ep. 11 — in de bar praten Julio en de camarero over de vakantie: Canarias met «siempre hace buen tiempo» tegenover het ijskoude Ávila; een clienta vertelt wat ze allemaal graag doet) + Suena bien (la s siempre sorda · de -s van het meervoud · ¿s of c/z? · el acento en los precios) + La máquina de frases (hace / me gusta / me gustan) + Kit (el tiempo · las estaciones · el ocio · la frecuencia · reaccionar). Les 2: gramática functioneel (hace + sustantivo ↔ tengo frío · me gusta ↔ me gustan · reaccionar), práctica, hablar «La encuesta de gustos», tarea «Mi estación favorita» + cultura (un idioma, 21 climas).", {"size": 12, "color": RGBColor(0xEC,0xEA,0xE3)})],
          [("", {"size": 5})],
          [("VIDEO = GOOGLE DRIVE (geen YouTube voor deze aflevering).", {"size": 14, "bold": True, "color": RGBColor(0xFB,0xEA,0xEC), "font": DISPLAY})],
          [("File-id 1saLd6_-eTVUTVbv1v8KbKwfYp3Ale6-D (deelrechten reader/anyone). INTERNET VEREIST. In de escucha-dia klik je op de poster om in PowerPoint af te spelen; lukt dat niet, gebruik de knop «▶ Abrir en Drive» of open " + VIDEO_WATCH + " in een browser. NB: in het aangeleverde transcript stonden de sprekerlabels van escena 1 deels verwisseld (bijna alles op «Julio»); de beurten zijn gereconstrueerd tot een coherente scène met drie stemmen (Julio · camarero · clienta). Test de verbinding vóór de les.", {"size": 12, "color": RGBColor(0xEC,0xEA,0xE3)})],
          [("", {"size": 5})],
          [("Aanpak C4 (survival).", {"size": 14, "bold": True, "color": RGBColor(0xFB,0xEA,0xEC), "font": DISPLAY})],
          [("Chunks komen auditief binnen (luisteren → naspreken). «hace» presenteren als ÉÉN onveranderlijke vorm (zoals hay/hay que), niet als vervoeging van hacer — dat systeem hoort in het 5de jaar (C5). «me/te/le gusta(n)» blijven VASTE CHUNKS: géén volledig pronomensysteem en géén gustar-paradigma (C6). Géén futuro/condicional/subjuntivo. TWEE KERNVALSTRIKKEN: (1) wij zeggen «het IS koud», dus leerlingen produceren «es frío»/«está frío» — het weer «doet» iets: hace frío; en zet daar het contrast met de persoon naast (tengo frío = ík heb het koud, recycling U9); (2) gustar draait de zin om («het bevalt mij»), dus HET DING kiest de vorm: me gusta el cine ↔ me gustan los deportes — nooit «yo gusto el cine». Voor de reacties: bij een negatieve zin is «a mí tampoco» de juiste keuze — voor Nederlandstaligen niet intuïtief. Frecuencia: siempre/nunca/a veces staan vóór het werkwoord, «tres veces por semana» achteraan. Uitspraak: de Spaanse s is ALTIJD stemloos — ook tussen klinkers en in de -s van het meervoud («los años» nooit als /z/); herhaling U3 voor c+e/i en z = /θ/; acentuación-laag = de klemtoon in prijzen en getallen (uit «son cuatro cincuenta»). Doelcodes: C4-WS-1 · C4-SP-2 · C4-TS-3/5 · C4-LU-1 · C4-GE-3 · C4-STR-1 · C4-MEC-1/2 · C4-CU-1.", {"size": 12, "color": RGBColor(0xEC,0xEA,0xE3)})],
          [("", {"size": 5})],
          [("Evaluatie.", {"size": 14, "bold": True, "color": RGBColor(0xFB,0xEA,0xEC), "font": DISPLAY})],
          [("Mondelinge mini-taak «Mi estación favorita»: het weer van je favoriete seizoen zeggen met «hace + naamwoord», twee smaken geven (één keer gusta, één keer gustan), één frecuencia-woord gebruiken, en in de enquête drie klasgenoten bevragen met «¿Te gusta…?» + reageren met «a mí también / tampoco / no / sí». Geen leerplan → focus op «kunnen gebruiken in de praktijk». Rubric: hace + naamwoord correct · me gusta ↔ me gustan correct · frecuencia + reageren in de enquête.", {"size": 12, "color": RGBColor(0xEC,0xEA,0xE3)})],
          [("", {"size": 5})],
          [("Oplossingen staan bij elke oefendia in de presenter-notities; antwoorden verschijnen bij klik.", {"size": 11, "italic": True, "color": RGBColor(0xA6,0xA2,0x9A)})]])
    footer(s, tab=FTAB, page=pg())

def s_uitspraak():
    s = slide(); bg(s)
    sectionbar(s, "SUENA BIEN", "La s siempre es sorda · el acento en los precios", "De Spaanse s is altijd scherp — nooit onze z", num=None)
    card(s,Inches(0.55),Inches(1.6),Inches(6.05),Inches(2.15),fill=WHITE,line=LINE)
    rect(s,Inches(0.55),Inches(1.6),Inches(6.05),Inches(0.14),fill=G)
    text(s,Inches(0.8),Inches(1.85),Inches(5.6),Inches(0.4),[[("① La s sorda · siempre /s/",{"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
    text(s,Inches(0.8),Inches(2.35),Inches(5.6),Inches(1.3),
         [[("s",{"size":14.5,"bold":True,"color":G}),("iempre · ca",{"size":14.5,"color":INK}),("s",{"size":14.5,"bold":True,"color":G}),("i · gu",{"size":14.5,"color":INK}),("s",{"size":14.5,"bold":True,"color":G}),("ta · e",{"size":14.5,"color":INK}),("s",{"size":14.5,"bold":True,"color":G}),("tacione",{"size":14.5,"color":INK}),("s",{"size":14.5,"bold":True,"color":G}),(" · vacacione",{"size":14.5,"color":INK}),("s",{"size":14.5,"bold":True,"color":G})],
          [("Zoals in «sok» — nooit zoals onze z in «zomer».",{"size":11,"italic":True,"color":MUT})]])
    card(s,Inches(6.75),Inches(1.6),Inches(6.05),Inches(2.15),fill=WHITE,line=LINE)
    rect(s,Inches(6.75),Inches(1.6),Inches(6.05),Inches(0.14),fill=G)
    text(s,Inches(7.0),Inches(1.85),Inches(5.6),Inches(0.4),[[("② También la -s del plural",{"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
    text(s,Inches(7.0),Inches(2.35),Inches(5.6),Inches(1.3),
         [[("lo",{"size":14.5,"color":INK}),("s",{"size":14.5,"bold":True,"color":G}),(" año",{"size":14.5,"color":INK}),("s",{"size":14.5,"bold":True,"color":G}),(" · tre",{"size":14.5,"color":INK}),("s",{"size":14.5,"bold":True,"color":G}),(" vece",{"size":14.5,"color":INK}),("s",{"size":14.5,"bold":True,"color":G}),(" · mi",{"size":14.5,"color":INK}),("s",{"size":14.5,"bold":True,"color":G}),(" primo",{"size":14.5,"color":INK}),("s",{"size":14.5,"bold":True,"color":G})],
          [("Ook tussen twee klinkers blijft ze scherp: «los años», niet «loz añoz».",{"size":11,"italic":True,"color":MUT})]])
    card(s,Inches(0.55),Inches(3.9),Inches(12.25),Inches(0.85),fill=GT,line=G)
    text(s,Inches(0.85),Inches(4.05),Inches(11.7),Inches(0.6),
         [[("¡Ojo! ",{"size":13,"bold":True,"color":RED,"font":DISPLAY}),("Nederlandstaligen maken van «lo",{"size":13,"color":INK}),("s",{"size":13,"bold":True,"color":GD}),(" año",{"size":13,"color":INK}),("s",{"size":13,"bold":True,"color":GD}),("» vaak «lo",{"size":13,"color":INK}),("z",{"size":13,"bold":True,"color":RED}),(" año",{"size":13,"color":INK}),("z",{"size":13,"bold":True,"color":RED}),("». Herhaling U3: ",{"size":13,"color":INK}),("c+e/i en z",{"size":13,"bold":True,"color":GD}),(" klinken in Spanje als ",{"size":13,"color":INK}),("/θ/",{"size":13,"bold":True,"color":RED}),(" (cielo · cinco · doce · zona).",{"size":13,"color":INK})]])
    text(s,Inches(0.6),Inches(5.0),Inches(12),Inches(0.4),[[("③ El acento en los precios · uit de scène: «Son cuatro cincuenta»",{"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
    text(s,Inches(0.6),Inches(5.55),Inches(12.2),Inches(0.7),
         [[("cua·",{}),("TRO",{"color":G,"bold":True}),(" cin·",{}),("CUEN",{"color":G,"bold":True}),("·ta      vein·ti·",{}),("CIN",{"color":G,"bold":True}),("·co      ",{}),("TREIN",{"color":G,"bold":True}),("·ta y ",{}),("DOS",{"color":G,"bold":True})]],size=19,font=DISPLAY)
    text(s,Inches(0.6),Inches(6.28),Inches(12.2),Inches(0.5),
         [[("Getallen op -enta hebben de klemtoon op die lettergreep: cin·CUEN·ta · se·SEN·ta · o·CHEN·ta.",{"size":11,"color":INK})],
          [("🔊 Oefen de klanken online op de hub (tabblad Kit · Suena bien) — daar staat ook het dictado de precios.",{"size":11,"italic":True,"color":MUT})]])
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
    sectionbar(s, "§4 · LA MÁQUINA DE FRASES", "Hace / Me gusta / Me gustan", "Drie formules — klik en de zin verschijnt", num=4)
    legend_func(s, Inches(0.55), Inches(1.42))
    _maq_row(s, Inches(1.66), "Hace", "het weer «doet»", "frío · calor · viento",
             "Hace frío.", "Het is koud.", h=Inches(0.92))
    _maq_row(s, Inches(2.64), "Me gusta", "1 ding / werkwoord", "el cine · hacer yoga",
             "Me gusta el cine.", "Ik hou van film.", h=Inches(0.92))
    _maq_row(s, Inches(3.62), "Me gustan", "meervoud", "los deportes",
             "Me gustan los deportes.", "Ik hou van sport.", h=Inches(0.92))
    card(s, Inches(0.55), Inches(4.66), Inches(12.25), Inches(0.72), fill=GT, line=G)
    text(s, Inches(0.85), Inches(4.74), Inches(11.7), Inches(0.62),
         [[("Cómo funciona · ", {"size": 12.5, "bold": True, "color": GD, "font": DISPLAY}),
           ("bij ", {"size": 12.5, "color": INK}), ("hace", {"size": 13, "bold": True, "color": F_VERB}),
           (" komt een ", {"size": 12.5, "color": INK}), ("naamwoord", {"size": 13, "bold": True, "color": GD}),
           (" (frío · calor · viento) — de vorm verandert nooit. Bij ", {"size": 12.5, "color": INK}),
           ("gustar", {"size": 13, "bold": True, "color": F_VERB}), (" kiest ", {"size": 12.5, "color": INK}),
           ("het ding", {"size": 13, "bold": True, "color": GD}), (" de vorm: 1 → gusta · meervoud → gustan.", {"size": 12.5, "color": INK})],
          [("Ook zo: ", {"size": 11.5, "color": INK}), ("te gusta · le gusta · no me gustan · me gusta más el frío",  {"size": 12, "bold": True, "color": F_VERB}),
           ("   —   en vergeet ", {"size": 11.5, "color": INK}), ("el / la / los / las", {"size": 12.5, "bold": True, "color": RED}),
           (" niet: me gusta EL cine.", {"size": 11.5, "color": INK})]])
    text(s, Inches(0.6), Inches(5.52), Inches(12.2), Inches(0.35),
         [[("Construye · bouw zelf (klik voor de oplossing): ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("weer + viento  ·  gusta + hacer submarinismo  ·  meervoud + las vacaciones", {"size": 13, "color": INK})]])
    exercise_solucion(s, Inches(0.8), Inches(5.95), Inches(11.7), Inches(0.5),
        [[("Hace viento. · Me gusta hacer submarinismo. · Me gustan las vacaciones.", {"bold": True, "color": GD, "size": 13})]])
    noodroute(s)
    notes(s, "Werkvorm: bouw hardop in koor. Wijs blok 1 aan (hace / me gusta / me gustan), dan blok 3, en de klas zegt de volledige zin; klik daarna de zin open ter controle. Kernidee: blok 1 is een VASTE CHUNK en blok 2 zegt wat erop volgt (een naamwoord bij hace; el/la + naamwoord of een infinitivo bij gusta; los/las + meervoud bij gustan). Zo hoeven leerlingen niets te vervoegen (het paradigma van hacer en gustar komt later). Verbind expliciet met U10 (hay que + infinitivo) en U9 (voy a / tengo que): de reeks onveranderlijke vormen groeit — hay · hay que · hace. Let op het lidwoord: «me gusta EL cine» (niet «me gusta cine»). Oplossing: Hace viento. · Me gusta hacer submarinismo. · Me gustan las vacaciones. Doelcodes: C4-WS-1 · C4-SP-2 · C4-TS-3 · C4-MEC-2.")
    footer(s, tab=FTAB, page=pg())

# ── Funciones-comunicativas-dia (matrix C) — leest de gedeelde funciones_data ──
import sys as _sys
_sys.path.insert(0, os.path.join(os.path.dirname(HERE), "web"))
import funciones_data as FD
FUNC_UNIT = 11

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
    # vanaf 23 functies: DRIE kolommen (bij twee kolommen zou een rij van de dia vallen)
    ncols = 3 if have >= 23 else 2
    if ncols == 3:
        cols_x=[Inches(0.55), Inches(4.83), Inches(9.11)]; w=Inches(3.9)
    else:
        cols_x=[Inches(0.55), Inches(6.85)]; w=Inches(5.9)
    nrows = (len(fs) + ncols - 1) // ncols
    top = 1.82; bottom = 7.0
    pitch = min(1.32, (bottom - top) / nrows)
    ch = pitch - (0.16 if pitch > 0.80 else 0.10)
    off = 0.05 if pitch > 0.80 else 0.03
    tsz = 11 if ncols == 2 else 10
    exsz = 8.5 if have <= 14 else (7.0 if have <= 16 else (6.3 if ncols == 2 else 6.6))
    excap = 300 if have <= 16 else (235 if have <= 18 else (205 if ncols == 2 else 150))
    for i,f in enumerate(fs):
        col=i%ncols; row=i//ncols
        x=cols_x[col]; y=Inches(top+row*pitch)
        st=FD.status(f,FUNC_UNIT); hot = st in ("nueva","nivel")
        card(s,x,y,w,Inches(ch),fill=(GT if hot else WHITE),line=(G if hot else LINE))
        badge = "  ● NUEVA" if st=="nueva" else ("  ▲ nivel+" if st=="nivel" else "")
        text(s,x+Inches(0.18),y+Inches(off),w-Inches(0.36),Inches(min(0.28, ch*0.5)),
             [[(f["es"], {"size":tsz,"bold":True,"color":INK,"font":DISPLAY}),(badge,{"size":8.5,"bold":True,"color":GD})]])
        exps=" · ".join(e for u in sorted(k for k in f["exp"] if k<=FUNC_UNIT) for e in f["exp"][u])
        text(s,x+Inches(0.18),y+Inches(off)+Inches(ch*0.44),w-Inches(0.36),Inches(max(0.12, ch*0.5)),
             [[(_cap_exps(exps, excap),{"size":exsz,"color":MUT})]])
    footer(s, tab=FTAB, page=pg())

def _run_all_slides(include_teacher=True):
    # dia-indexen (0-based) = de hyperlink-targets van de menutegels in s02_menu:
    # 0 título · 1 menú · 2 escucha · 3 suena bien · 4 la máquina de frases ·
    # 5 kit · 6 kit (frecuencia / reaccionar) · 7 gram hace · 8 gram gustar ·
    # 9 práctica · 10 hablar · 11 cultura · 12 tarea · 13 funciones · 14 repaso ·
    # (15 docentendossier)
    s01_title(); s02_menu(); s03_escucha(); s_uitspraak(); s_maquina()
    s04_kit(); s05_kit2(); s06_gram_hace()
    s07_gram_gustar(); s08_practica(); s09_speaking()
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
