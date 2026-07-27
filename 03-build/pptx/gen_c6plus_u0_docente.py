#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_c6plus_u0_docente.py — Interactieve PowerPoint C6+ · Unidad 0 «¡Volvemos!» (reencuentro)
=============================================================================================
Zelfde engine/pijplijn als de golden sample (gen_u0_docente = de engine: low-level helpers,
on-click <p:timing>-animaties, hyperlink-navigatie). Enkel de SLIDES zijn C6+·U0-specifiek.
Cursuskleur = PAARS (C6+): engine-kleuren worden overschreven. Twee decks (beide .pptx):
  · C6plus_U0_docente.pptx — vrije navigatie, oplossingen bij klik + didactiek in notities.
  · C6plus_U0_alumno.pptx  — gewone diavoorstelling, antwoorden bij klik (F5, geen kiosk).
Spaans-eerst + NL-steun. ≥20 dia's. Dekt de vier vaardigheden. Diagnostische repaso.
"""
import os
import gen_u0_docente as E
from gen_u0_docente import (
    slide, bg, rect, text, chip, avatar, card, sectionbar, footer, noodroute,
    exercise_solucion, check_badge, legend_func, link_to, register_reveal, notes, pg,
    INK, MUT, PAPER, CREMA, LINE, RED, AMBER, WHITE,
    F_SUBJ, F_VERB, F_OBJ, F_TIME, F_PLAC, F_NEG, F_STRA, ACC,
    DISPLAY, BODY, HAND, EMU_W, EMU_H,
    Inches, Pt, RGBColor, PP_ALIGN, MSO_ANCHOR,
)

# ---- PAARS-override (C6+): engine + lokaal ----
E.G  = RGBColor(0x7C, 0x56, 0xA9)
E.GD = RGBColor(0x5B, 0x3E, 0x83)
E.GT = RGBColor(0xEE, 0xE8, 0xF5)
G, GD, GT = E.G, E.GD, E.GT

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DOCENTE = os.path.join(HERE, "C6plus_U0_docente.pptx")
OUT_ALUMNO_PPTX = os.path.join(HERE, "C6plus_U0_alumno.pptx")
TAB = "U0 · ¡VOLVEMOS!"

def foot(s): footer(s, tab=TAB, page=pg())

# ============================================================ DIA 1 · TITLE
def s01_title():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(4.7), fill=G)
    rect(s, 0, Inches(4.7), EMU_W, Inches(0.09), fill=GD)
    text(s, Inches(0.6), Inches(0.35), Inches(3.4), Inches(3.6),
         [[("0", {"size": 260, "bold": True, "color": RGBColor(0x93, 0x74, 0xC2), "font": DISPLAY})]],
         anchor=MSO_ANCHOR.MIDDLE)
    chip(s, Inches(4.35), Inches(0.85), "LA RUTA · EL REENCUENTRO · EL MUNDO HISPANO 🧭", fill=WHITE, tcolor=GD, size=12)
    text(s, Inches(4.3), Inches(1.35), Inches(8.6), Inches(1.5),
         [[("¡Volvemos!", {"size": 66, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(4.35), Inches(2.7), Inches(8.4), Inches(0.6),
         [[("Otra vez juntos: saludar, presentarte y activar tu base (presente · género · países).", {"size": 15, "italic": True, "color": GT})]])
    text(s, Inches(4.35), Inches(3.35), Inches(8.4), Inches(0.9),
         [[("¿Quién eres… otra vez?", {"size": 24, "bold": True, "color": WHITE, "font": DISPLAY})],
          [("Wie ben je… opnieuw?", {"size": 13, "italic": True, "color": GT})]])
    text(s, Inches(0.6), Inches(4.95), Inches(6), Inches(0.4),
         [[("La gente de la ruta — je reisgezellen", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    x = Inches(0.6)
    for nm, city in [("lucia","Sevilla 🇪🇸"),("diego","CDMX 🇲🇽"),("valen","Cartagena 🇨🇴"),
                     ("nina","Cusco 🇵🇪"),("tu","Tú · Flandes 🇧🇪"),("mochila","La mochila")]:
        avatar(s, nm, x, Inches(5.4), Inches(1.0))
        text(s, x - Inches(0.15), Inches(6.42), Inches(1.3), Inches(0.5),
             [[(nm.capitalize() if nm != "tu" else "Tú", {"size": 10.5, "bold": True, "color": INK})],
              [(city.split("·")[-1].strip() if nm != "tu" else "de reiziger = jij", {"size": 8.5, "color": MUT})]],
             align=PP_ALIGN.CENTER)
        x = x + Inches(2.05)
    foot(s)
    notes(s, "TEACHER · TITLE. U0 = het reencuentro (huidige cohorte, C6+). Diagnostische repaso: geen heronderwijs, wél activeren. "
             "Doel: saludar/presentarse (formeel/informeel), el presente (regular + ser/estar/tener/ir/hacer/venir/dar), género & concordancia, "
             "países/nacionalidades/lenguas, números. Kernvalstrik: soy ≠ estoy · porque = want én omdat · nacionalidades met kleine letter. "
             "Docentdeck = vrije navigatie + oplossing in notities; leerlingdeck (.pptx, F5) = elke klik onthult het volgende antwoord.")

# ============================================================ DIA 2 · LESSON_MENU
def s02_menu():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "MENÚ DE LA LECCIÓN", "El mapa de la Unidad 0",
               "Kies je route — klik een tegel. Alles oefent naar de Tarea «Tarjeta de reencuentro» toe.", num=0)
    tiles = [
        ("§1", "Saludos", "presentarse · tú/usted", G, 3),
        ("§2", "El presente", "regular + ser/estar/ir…", G, 4),
        ("§3", "Género y adj.", "el/la · -o/-a", G, 7),
        ("§4", "Países", "nacionalidad · lengua", G, 14),
        ("§5", "Lectura + escucha", "dos perfiles", G, 9),
        ("★", "Cultura", "el mundo hispano", GD, 16),
        ("🪪", "Tarea · Tarjeta", "preséntate", GD, 18),
        ("◎", "Repaso + semáforo", "lo esencial · zelfevaluatie", GD, 20),
    ]
    cols, x0, y0 = 4, Inches(0.5), Inches(1.55)
    tw, th, gx, gy = Inches(3.0), Inches(2.45), Inches(0.14), Inches(0.2)
    for i, (tag, es, nl, col, dia) in enumerate(tiles):
        r, c = divmod(i, cols)
        x = x0 + c * (tw + gx); y = y0 + r * (th + gy)
        cardshp = card(s, x, y, tw, th, fill=WHITE, line=col, lw=1.6); link_to(cardshp, dia - 1)
        hdr = rect(s, x, y, tw, Inches(0.5), fill=col); link_to(hdr, dia - 1)
        b = rect(s, x + Inches(0.12), y + Inches(0.08), Inches(0.34), Inches(0.34), fill=WHITE, round=True, radius=0.5)
        tf = b.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE; p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        rr = p.add_run(); rr.text = tag; rr.font.size = Pt(12); rr.font.bold = True; rr.font.name = DISPLAY; rr.font.color.rgb = col
        text(s, x + Inches(0.58), y + Inches(0.06), tw - Inches(0.7), Inches(0.4),
             [[(es, {"size": 14.5, "bold": True, "color": WHITE, "font": DISPLAY})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(0.18), y + Inches(0.68), tw - Inches(0.36), Inches(1.2), [[(nl, {"size": 11.5, "color": INK})]], line=1.12)
        chip(s, x + Inches(0.18), y + th - Inches(0.45), f"→ dia {dia}", fill=GT, tcolor=GD, size=9.5)
    foot(s)
    notes(s, "TEACHER · LESSON_MENU. Elke tegel = hyperlink; op elke oefendia staat ⌂ Menú terug. Richttijd 50 min. "
             "Kern = §2 el presente (diagnostisch). Kruisverwijzing print/HTML: «oefen online — 13 juegos + ~100 oefeningen».")

# ============================================================ DIA 3 · VOCABULARY — saludos & presentarse
def s03_vocab():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · VOCABULARIO", "Saludar y presentarse", "De woorden van het reencuentro — observa. Herken ze, dan gebruik je ze.", num=1)
    legend_func(s, Inches(9.7), Inches(0.55))
    rows = [("hola / adiós", "hallo / dag", "saludo · despedida"), ("buenos días", "goedemorgen", "buenas tardes/noches"),
            ("me llamo…", "ik heet…", "¿cómo te llamas?"), ("soy de…", "ik kom uit…", "¿de dónde eres?"),
            ("tengo … años", "ik ben … jaar", "¿cuántos años tienes?"), ("vivo en…", "ik woon in…", "¿dónde vives?"),
            ("hablo…", "ik spreek…", "la lengua / el idioma"), ("encantado/-a", "aangenaam", "mucho gusto")]
    x0, y0 = Inches(0.5), Inches(1.6); cw = Inches(6.1); rh = Inches(0.6)
    for i, (k, v, nl) in enumerate(rows):
        c = 0 if i < 4 else 1; r = i % 4
        x = x0 + c * (cw + Inches(0.15)); y = y0 + r * (rh + Inches(0.12))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(2.4), rh, [[(k, {"size": 13, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(2.5), y, Inches(2.1), rh, [[(v, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(4.5), y, Inches(1.5), rh, [[(nl, {"size": 9, "italic": True, "color": MUT})]], anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(4.75), Inches(12.3), Inches(0.5),
         [[("Formal vs. informal: ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("tú ", {"size": 13, "bold": True, "color": F_SUBJ}), ("(¿cómo estás?) · ", {"size": 13, "color": INK}),
           ("usted ", {"size": 13, "bold": True, "color": F_SUBJ}), ("(¿cómo está?)", {"size": 13, "color": INK})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.35), Inches(12.3), Inches(0.95),
             [[("Presentarte (3 werkwoorden): ", {"bold": True, "color": GD}), ("me llamo · soy (de) · tengo … años · vivo en · hablo …", {"bold": True, "color": GD})],
              [("🔴 nacionaliteiten met kleine letter: soy belga, es española (niet Belga/Española).", {"color": RED})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCABULARY. Laat presentarse raden zónder de NL-gloss. Contrast tú/usted meteen. "
             "Online: flip cards + memoria del reencuentro + ¿formal o informal? (classify).")

# ============================================================ DIA 4 · GRAMMAR — el presente (color)
def s04_presente():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · GRAMÁTICA VISUAL", "El presente — ¿quién hace qué?", "Kleur = de functie. Het werkwoord past zich aan de persoon aan.", num=2)
    legend_func(s, Inches(9.7), Inches(0.55))
    seg = [("(Yo) ", F_SUBJ), ("hablo ", F_VERB), ("español ", F_OBJ), ("y ", INK), ("vivo ", F_VERB), ("en Gante.", F_PLAC)]
    runs = [[(t, {"size": 22, "bold": True, "color": c, "font": DISPLAY}) for t, c in seg]]
    card(s, Inches(0.5), Inches(1.7), Inches(12.3), Inches(1.2), fill=GT, line=None)
    text(s, Inches(0.8), Inches(1.7), Inches(11.7), Inches(1.2), runs, anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(3.15), Inches(12), Inches(0.4), [[("Las terminaciones regulares", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    frame = [("-ar hablar", "o · as · a · amos · áis · an"), ("-er comer", "o · es · e · emos · éis · en"),
             ("-ir vivir", "o · es · e · imos · ís · en")]
    x0, y0 = Inches(0.5), Inches(3.6); cw = Inches(4.0); rh = Inches(0.9)
    for i, (a, b) in enumerate(frame):
        x = x0 + i * (cw + Inches(0.15)); y = y0
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y + Inches(0.1), cw - Inches(0.3), Inches(0.35), [[(a, {"size": 13, "bold": True, "color": GD})]])
        text(s, x + Inches(0.15), y + Inches(0.46), cw - Inches(0.3), Inches(0.4), [[(b, {"size": 12, "color": F_VERB, "bold": True})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.9),
             [[("Regla: ", {"bold": True, "color": GD}), ("raíz (habl-) + terminación. De terminación verandert met de persoon: yo hablo, tú hablas, él habla…", {"color": GD})],
              [("De 7 onregelmatige (yo): soy · estoy · tengo · voy · hago · vengo · doy (vaak -oy of -go).", {"color": GD})]],
             trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR (color-coding). Maak de raíz+terminación zichtbaar. Kleur nooit als enige drager. "
             "Online: «completa: el presente» (cloze) + vervoegingscirkel.")

# ============================================================ DIA 5 · QUIZ — el presente (reveal)
def s05_presente_quiz():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · QUIZ", "Completa el presente", "Klik een zin → de juiste vorm verschijnt. Kijk naar de persoon.", num=2)
    items = [("Yo ___ (ser) de Bélgica.", "soy"), ("¿Tú ___ (vivir) en Gante?", "vives"),
             ("Nina ___ (tener) 16 años.", "tiene"), ("Nosotros ___ (hablar) español.", "hablamos"),
             ("Diego ___ (ir) al mercado.", "va"), ("Ellos ___ (venir) de México.", "vienen")]
    x0, y0 = Inches(0.5), Inches(1.7); cw = Inches(6.05); rh = Inches(0.7)
    for i, (q, ans) in enumerate(items):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(4.3), rh, [[(q, {"size": 12.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.5), y, cw - Inches(4.6), rh, [[("→ " + ans, {"size": 14, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.95),
             [[("yo → -o (hablo, vivo) · soy/estoy/tengo/voy/vengo/hago/doy. ", {"bold": True, "color": G}),
               ("tú → -s · él/ella → -a/-e · nosotros → -mos · ellos → -n.", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ (reveal). Laat de klas de vorm roepen vóór de klik. Online: «completa: el presente» (cloze) + señala (yo/tú).")

# ============================================================ DIA 6 · GRAMMAR — ser (reveal) + soy/estoy
def s06_ser():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · GRAMÁTICA", "El verbo «ser» + ¡ojo! soy / estoy", "Klik een kaart → de vorm verschijnt. ser = wie/wat je bent.", num=2)
    pers = ["yo", "tú", "él/ella", "nosotros", "vosotros", "ellos"]
    forms = ["soy", "eres", "es", "somos", "sois", "son"]
    x0, y0 = Inches(1.6), Inches(1.9); cw = Inches(3.4); ch = Inches(1.0)
    for i, (p, f) in enumerate(zip(pers, forms)):
        c = i % 3; r = i // 3; x = x0 + c * (cw + Inches(0.3)); y = y0 + r * (ch + Inches(0.22))
        card(s, x, y, cw, ch, fill=WHITE, line=G, lw=1.4)
        text(s, x, y + Inches(0.1), cw, Inches(0.32), [[(p, {"size": 12, "color": MUT})]], align=PP_ALIGN.CENTER)
        rev = text(s, x, y + Inches(0.44), cw, Inches(0.5), [[(f, {"size": 22, "bold": True, "color": GD, "font": DISPLAY})]], align=PP_ALIGN.CENTER)
        register_reveal(s, rev)
    text(s, Inches(0.5), Inches(5.05), Inches(12.3), Inches(0.5),
         [[("🟡 ", {"size": 12}), ("soy ", {"size": 13, "bold": True, "color": F_SUBJ}), ("= identiteit (soy belga, soy estudiante) · ", {"size": 12, "color": INK}),
           ("estoy ", {"size": 13, "bold": True, "color": F_PLAC}), ("= plaats/gevoel (estoy en clase, estoy bien).", {"size": 12, "color": INK})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.65), Inches(12.3), Inches(0.7),
             [[("Truc: ", {"bold": True, "color": GD}), ("permanent/eigenschap → ser (soy) · tijdelijk/plaats → estar (estoy). Contrast komt uitgebreid in U1.", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR ser (reveal). Coro vóór de klik. soy/estoy is dé U0-valstrik; het volledige ser/estar-contrast is U1. "
             "Online: «¿soy o estoy?» (classify).")

# ============================================================ DIA 7 · GRAMMAR — género & concordancia
def s07_genero():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · GRAMÁTICA VISUAL", "Género y concordancia — el/la · -o/-a", "Lidwoord én adjectief volgen het zelfstandig naamwoord (m/v · ev/mv).", num=3)
    legend_func(s, Inches(9.7), Inches(0.55))
    card(s, Inches(0.5), Inches(1.7), Inches(6.0), Inches(1.1), fill=GT, line=None)
    text(s, Inches(0.7), Inches(1.7), Inches(5.6), Inches(1.1),
         [[("el ", {"size": 20, "bold": True, "color": F_SUBJ}), ("chic", {"size": 20, "bold": True, "color": INK}), ("o ", {"size": 20, "bold": True, "color": F_VERB}),
           ("alt", {"size": 20, "bold": True, "color": INK}), ("o", {"size": 20, "bold": True, "color": F_VERB})]], anchor=MSO_ANCHOR.MIDDLE)
    card(s, Inches(6.8), Inches(1.7), Inches(6.0), Inches(1.1), fill=GT, line=None)
    text(s, Inches(7.0), Inches(1.7), Inches(5.6), Inches(1.1),
         [[("la ", {"size": 20, "bold": True, "color": F_SUBJ}), ("chic", {"size": 20, "bold": True, "color": INK}), ("a ", {"size": 20, "bold": True, "color": F_NEG}),
           ("alt", {"size": 20, "bold": True, "color": INK}), ("a", {"size": 20, "bold": True, "color": F_NEG})]], anchor=MSO_ANCHOR.MIDDLE)
    frame = [("el / un", "masculino (-o)"), ("la / una", "femenino (-a)"), ("los / las", "plural (+ -s)"),
             ("-o → -a", "chico → chica"), ("🔴 el problema", "-ma = m."), ("🔴 la mano", "-o = f.")]
    x0, y0 = Inches(0.5), Inches(3.15); cw = Inches(4.0); rh = Inches(0.62)
    for i, (a, b) in enumerate(frame):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.12))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(1.9), rh, [[(a, {"size": 12.5, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(2.05), y, cw - Inches(2.2), rh, [[(b, {"size": 11, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.35), Inches(12.3), Inches(0.75),
             [[("Regla: ", {"bold": True, "color": GD}), ("lidwoord + adjectief komen overeen in geslacht én getal. Uitzonderingen: el día/mapa/problema (m), la mano/foto (f).", {"color": GD})]],
             trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR género. Toon concordantie fysiek (el chico alto / la chica alta). Online: «¿el o la?» (classify) + concordancia Tetris.")

# ============================================================ DIA 8 · QUIZ — ¿el o la? (reveal)
def s08_genero_quiz():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · QUIZ", "¿el o la?", "Klik een woord → het juiste lidwoord. Let op de valstrikken.", num=3)
    items = [("___ casa", "la"), ("___ problema", "el"), ("___ día", "el"),
             ("___ mano", "la"), ("___ ciudad", "la"), ("___ mapa", "el")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.78)
    for i, (q, a) in enumerate(items):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(3.6), rh, [[(q, {"size": 13, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(3.8), y, cw - Inches(3.9), rh, [[("→ " + a, {"size": 14, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Valstrikken: ", {"bold": True, "color": RED}), ("-ma → m (el problema, el idioma) · la mano, la foto (f ondanks -o) · -dad → f (la ciudad).", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ género (retrieval). Klas roept el/la vóór de klik. Online: «¿el o la?» (classify).")

# ============================================================ DIA 9 · READING — dos perfiles
def s09_reading():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§5 · LEER · COMPRENSIÓN", "Dos perfiles — «De vuelta al insti»", "Lees en beantwoord. Klik een vraag → het antwoord verschijnt.", num=5)
    card(s, Inches(0.5), Inches(1.65), Inches(5.6), Inches(3.9), fill=GT, line=G, lw=1.4)
    avatar(s, "diego", Inches(0.85), Inches(1.95), Inches(1.0))
    text(s, Inches(2.05), Inches(1.98), Inches(3.9), Inches(1.5),
         [[("«Me llamo Diego, soy de la Ciudad de México. Tengo 16 años. Vivo con mi madre y mi hermana. En clase soy alegre. Hablo español y estudio neerlandés.»", {"size": 11.5, "italic": True, "color": INK})]], line=1.18)
    avatar(s, "nina", Inches(0.85), Inches(3.65), Inches(1.0))
    text(s, Inches(2.05), Inches(3.68), Inches(3.9), Inches(1.5),
         [[("«Soy Nina, peruana, de Cusco. Tengo 16 años y un hermano pequeño. Soy tranquila. Hablo español y un poco de quechua.»", {"size": 11.5, "italic": True, "color": INK})]], line=1.18)
    qa = [("¿De dónde es Diego?", "De México (CDMX)"), ("¿Qué lengua habla Nina además del español?", "Un poco de quechua"),
          ("¿Cuántos años tienen los dos?", "Dieciséis"), ("¿Cómo es Nina?", "Tranquila")]
    x = Inches(6.4); y = Inches(1.7)
    for q, a in qa:
        card(s, x, y, Inches(6.4), Inches(0.85), fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y + Inches(0.06), Inches(6.1), Inches(0.4), [[(q, {"size": 12.5, "bold": True, "color": GD})]])
        rev = text(s, x + Inches(0.15), y + Inches(0.44), Inches(6.1), Inches(0.35), [[("→ " + a, {"size": 12, "color": INK})]])
        register_reveal(s, rev)
        y = y + Inches(0.98)
    btn = noodroute(s)
    exercise_solucion(s, Inches(6.4), Inches(5.65), Inches(6.4), Inches(0.6),
             [[("🎯 Leesdoel: ", {"bold": True, "color": GD}), ("scannen naar datos (país, edad, lengua, carácter) — niet élk woord.", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · READING (lezen→schrijven-keten). Eerst globaal, dan scannen. Onthul antwoorden pas na de klas. "
             "Daarna: leerlingen zeggen met wie ze meer gemeen hebben (transfer → Tarea).")

# ============================================================ DIA 10 · LISTENING — presentaciones
def s10_listening():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · ESCUCHAR", "Escucha las presentaciones", "Vier personas se presentan. Klik un nombre → país + dato. (audio op de digitale pagina)", num=4)
    people = [("Lucía", "España 🇪🇸", "16 · alegre"), ("Diego", "México 🇲🇽", "16 · hablador"),
              ("Valen", "Colombia 🇨🇴", "15 · costeña"), ("Mateo", "Argentina 🇦🇷", "17 · voseo")]
    x0, y0 = Inches(0.7), Inches(1.9); cw = Inches(2.95); ch = Inches(2.4)
    for i, (nm, pais, dato) in enumerate(people):
        x = x0 + i * (cw + Inches(0.1))
        card(s, x, y0, cw, ch, fill=WHITE, line=LINE, lw=1.2)
        rect(s, x, y0, cw, Inches(0.5), fill=GT)
        text(s, x, y0, cw, Inches(0.5), [[("🔊  " + nm, {"size": 14, "bold": True, "color": GD, "font": DISPLAY})]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(0.15), y0 + Inches(0.65), cw - Inches(0.3), Inches(0.4), [[("Es de:", {"size": 12, "color": MUT})]])
        rev1 = text(s, x + Inches(0.15), y0 + Inches(1.0), cw - Inches(0.3), Inches(0.5), [[(pais, {"size": 13, "bold": True, "color": INK})]], line=1.05)
        text(s, x + Inches(0.15), y0 + Inches(1.6), cw - Inches(0.3), Inches(0.4), [[("Edad · carácter:", {"size": 11, "color": MUT})]])
        rev2 = text(s, x + Inches(0.15), y0 + Inches(1.95), cw - Inches(0.3), Inches(0.4), [[(dato, {"size": 13, "bold": True, "color": G})]])
        register_reveal(s, rev1); register_reveal(s, rev2)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.85),
             [[("Modelo-audio (docent leest of TTS): ", {"bold": True, "color": GD}),
               ("«Hola, me llamo Lucía, soy de España. Tengo dieciséis años y soy alegre.» …", {"color": GD})],
              [("Daarna spreken: elke leerling presenteert zich zoals het model.", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · LISTENING (selectief → spreken). Lees elke presentatie voor (of TTS). Klas noteert país + edad; onthul per klik. "
             "Koppel meteen aan de eigen presentación.")

# ============================================================ DIA 11 · GRAMMAR — ¿soy o estoy? (reveal)
def s11_ser_estar():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · GRAMÁTICA", "¿soy o estoy?", "Klik een zin → de juiste vorm. ser = identiteit · estar = plaats/gevoel.", num=2)
    R = [("___ de Bélgica.", "soy"), ("___ en clase.", "estoy"), ("___ estudiante.", "soy"),
         ("Hoy ___ contento.", "estoy"), ("___ belga.", "soy"), ("___ muy bien, gracias.", "estoy")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(3.95); ch = Inches(1.15)
    for i, (p, v) in enumerate(R):
        c = i % 3; r = i // 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (ch + Inches(0.2))
        card(s, x, y, cw, ch, fill=WHITE, line=G, lw=1.4)
        text(s, x + Inches(0.12), y + Inches(0.12), cw - Inches(0.24), Inches(0.4), [[(p, {"size": 12.5, "color": MUT})]], align=PP_ALIGN.CENTER)
        rev = text(s, x, y + Inches(0.5), cw, Inches(0.55), [[("→ " + v, {"size": 24, "bold": True, "color": GD, "font": DISPLAY})]], align=PP_ALIGN.CENTER)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.65),
             [[("ser (soy): ", {"bold": True, "color": GD}), ("herkomst · nationaliteit · beroep · karakter. ", {"color": GD}),
               ("estar (estoy): ", {"bold": True, "color": GD}), ("plaats · gevoel · toestand.", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR soy/estoy (reveal). Coro vóór de klik. Diagnostisch: enkel yo-vormen. Online: «¿soy o estoy?» (classify).")

# ============================================================ DIA 12 · SPEAKING — preséntate
def s12_speaking():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · SPEAKING · INTERACCIÓN", "¡Preséntate!", "Speel de scène met de frames. Steun bouwt af: kaarten → beginwoorden → uit het hoofd.", num=1)
    avatar(s, "tu", Inches(11.4), Inches(1.7), Inches(1.3))
    labels = ["Saludar", "Nombre", "Origen", "Edad", "Dónde vives", "Lengua"]
    frames = ["¡Hola! / Buenos días.", "Me llamo …", "Soy de …", "Tengo … años.", "Vivo en …", "Hablo …"]
    x0, y0 = Inches(0.5), Inches(1.8); cw = Inches(3.4); rh = Inches(0.8)
    for i, (lab, fr) in enumerate(zip(labels, frames)):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=G, lw=1.2, shadow=False)
        text(s, x + Inches(0.15), y + Inches(0.05), cw - Inches(0.3), Inches(0.32), [[(lab, {"size": 10, "color": MUT})]])
        text(s, x + Inches(0.15), y + Inches(0.36), cw - Inches(0.3), Inches(0.4), [[(fr, {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    chip(s, Inches(0.5), Inches(4.65), "🎙️ Grábate online · «Mensaje de voz: preséntate»", fill=GT, tcolor=GD, size=11)
    text(s, Inches(0.5), Inches(5.05), Inches(10.5), Inches(0.9),
         [[("Ronda 1: ", {"size": 12, "bold": True, "color": GD}), ("met de kaarten. ", {"size": 12, "color": INK}),
           ("Ronda 2: ", {"size": 12, "bold": True, "color": GD}), ("alleen beginwoorden. ", {"size": 12, "color": INK}),
           ("Ronda 3: ", {"size": 12, "bold": True, "color": GD}), ("uit het hoofd. ", {"size": 12, "color": INK}),
           ("Ronda 4: ", {"size": 12, "bold": True, "color": GD}), ("grábate.", {"size": 12, "color": INK})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.6), Inches(12.3), Inches(0.65),
             [[("Modelo: ", {"bold": True, "color": GD}), ("«¡Hola! Me llamo … Soy de … Tengo … años. Vivo en … Hablo … ¡Mucho gusto!»", {"color": GD})]],
             trigger=btn, title_doc="MODELO · docent")
    foot(s)
    notes(s, "TEACHER · SPEAKING (interactie). Automatiseer presentarse in rondes met afbouwende steun. "
             "Online: recorder (opname + zelfevaluatie). Print blijft bruikbaar zonder opname.")

# ============================================================ DIA 13 · WRITING — mi tarjeta
def s13_writing():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "WRITING · PRODUCCIÓN", "Mi tarjeta de reencuentro", "Schrijf je kaartje. Klik → een modeltekst verschijnt.", num=1)
    card(s, Inches(0.5), Inches(1.7), Inches(6.0), Inches(3.9), fill=WHITE, line=LINE, lw=1.2)
    text(s, Inches(0.7), Inches(1.85), Inches(5.6), Inches(0.4), [[("✍️ Escribe aquí tu tarjeta:", {"size": 12, "bold": True, "color": GD})]])
    for i in range(6):
        rect(s, Inches(0.7), Inches(2.4) + i * Inches(0.5), Inches(5.6), Inches(0.01), fill=LINE)
    chk = ["nombre + edad", "de dónde eres (origen)", "dónde vives", "una lengua que hablas", "un adjetivo de carácter", "un conector (y/pero/porque)"]
    x = Inches(6.9); y = Inches(1.7)
    text(s, x, y, Inches(6), Inches(0.4), [[("Checklist:", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    for i, c in enumerate(chk):
        text(s, x, y + Inches(0.5) + i * Inches(0.45), Inches(6), Inches(0.4), [[("☐  " + c, {"size": 13, "color": INK})]])
    rev = card(s, x, Inches(4.35), Inches(6.0), Inches(1.25), fill=GT, line=G, lw=1.2)
    text(s, x + Inches(0.15), Inches(4.4), Inches(5.7), Inches(1.2),
         [[("Modelo: ", {"size": 12, "bold": True, "color": GD}),
           ("«¡Hola! Me llamo Sara. Soy de Bélgica y tengo 16 años. Vivo en Gante. Soy alegre y trabajadora, y hablo neerlandés y español. ¡Mucho gusto!»", {"size": 12, "italic": True, "color": INK})]], line=1.15)
    register_reveal(s, rev)
    noodroute(s); foot(s)
    notes(s, "TEACHER · WRITING (lezen→schrijven). Checklist = zichtbare steun; onthul het model pas na het schrijven (retrieval). "
             "Nakijkfocus: presente correct, concordancia, één conector. Dit voedt de Tarea «Tarjeta de reencuentro».")

# ============================================================ DIA 14 · VOCAB — países/nacionalidades/números (reveal)
def s14_paises():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · VOCABULARIO", "Países, nacionalidades y números", "Klik een woord → de vertaling/vorm. Bouw je woordnetwerk.", num=4)
    data = [("España", "español/a"), ("México", "mexicano/a"), ("Colombia", "colombiano/a"), ("Perú", "peruano/a"),
            ("Argentina", "argentino/a"), ("Bélgica", "belga"), ("veinte", "20"), ("cincuenta", "50"),
            ("cien", "100"), ("la lengua", "de taal"), ("el idioma", "de taal (m!)"), ("la nacionalidad", "nationaliteit")]
    x0, y0 = Inches(0.5), Inches(1.7); cw = Inches(3.0); rh = Inches(0.7)
    for i, (es, nl) in enumerate(data):
        c = i % 4; r = i // 4; x = x0 + c * (cw + Inches(0.1)); y = y0 + r * (rh + Inches(0.14))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.12), y, Inches(1.7), rh, [[(es, {"size": 12, "bold": True, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(1.8), y, cw - Inches(1.9), rh, [[("→ " + nl, {"size": 11.5, "color": G})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.9),
             [[("Zin: ", {"bold": True, "color": GD}), ("Soy de España, soy español/a y hablo español. ", {"color": GD}),
               ("🔴 nacionalidades met kleine letter; landen met hoofdletter.", {"color": RED})],
              [("Números: veinte (20) · cincuenta (50) · cien (100).", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCAB países. Klik onthult; koppel país → nacionalidad → lengua. Online: «país ↔ nacionalidad» (match) + banderas (memory).")

# ============================================================ DIA 15 · TALLER — acentuación + conectores
def s15_taller():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "TALLER DE LENGUA", "Acentuación + conectores", "Klik een item → correcte vorm. Gereedschap voor uitspraak en verbinden.", num=1)
    text(s, Inches(0.5), Inches(1.5), Inches(6), Inches(0.35), [[("A · acento: aguda / llana / esdrújula", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    fixes = [("Ma-drid", "aguda (laatste)"), ("ca-sa", "llana (voorlaatste)"), ("mú-si-ca", "esdrújula (tilde!)"), ("es-pa-ñol", "aguda")]
    y = Inches(1.95)
    for q, a in fixes:
        card(s, Inches(0.5), y, Inches(6.0), Inches(0.6), fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, Inches(0.62), y, Inches(2.6), Inches(0.6), [[(q, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, Inches(3.3), y, Inches(3.1), Inches(0.6), [[("→ " + a, {"size": 12, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y = y + Inches(0.72)
    text(s, Inches(6.9), Inches(1.5), Inches(6), Inches(0.35), [[("B · conectores: y · pero · porque · también", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    conn = [("Soy de Bélgica ___ hablo NL.", "y"), ("Estudio español ___ me gusta.", "porque"),
            ("Nina es tranquila, ___ Diego habla mucho.", "pero"), ("Tengo un hermano ___ una hermana.", "y")]
    y = Inches(1.95)
    for q, a in conn:
        card(s, Inches(6.9), y, Inches(5.9), Inches(0.6), fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, Inches(7.02), y, Inches(4.3), Inches(0.6), [[(q, {"size": 11, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, Inches(11.4), y, Inches(1.3), Inches(0.6), [[("→ " + a, {"size": 12, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y = y + Inches(0.72)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.85),
             [[("A: ", {"bold": True, "color": GD}), ("de meeste woorden zijn llana; draagt het een tilde, volg de tilde (mú-si-ca).", {"color": GD})],
              [("🔴 B: ", {"bold": True, "color": RED}), ("«want» én «omdat» = porque · «maar» = pero · «dus» = así que/por eso (niet luego).", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · TALLER. Acentuación = EELP-sterk, kort ophalen. porque/pero = kernvalstrik NL. Online: drills in de hub.")

# ============================================================ DIA 16 · CULTURE — el mundo hispano
def s16_cultura():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "CULTURA · EL REENCUENTRO", "El mundo hispano", "Klik een kaart → het weetje verschijnt. 21 países, 500+ miljoen sprekers.", num=1)
    cards = [("🇪🇸 Europa", "España is het enige Spaanstalige land in Europa. Ook catalán, gallego y euskera. Madrid = hoofdstad.", "castellano = español"),
             ("🌎 América", "De meeste hispanohablantes wonen in Latijns-Amerika: van México (~130 mln) tot Argentina (voseo).", "19 landen, veel accenten"),
             ("🌍 ¿Sabías que…?", "Ook in Guinea Ecuatorial (Afrika) is Spaans officieel. En in de VS ~40 mln hispanohablantes.", "2ª lengua materna del mundo")]
    x0, y0 = Inches(0.5), Inches(1.7); cw = Inches(4.05); ch = Inches(3.4)
    for i, (t, f, nl) in enumerate(cards):
        x = x0 + i * (cw + Inches(0.13))
        card(s, x, y0, cw, ch, fill=WHITE, line=G, lw=1.3)
        rect(s, x, y0, cw, Inches(0.6), fill=GT)
        text(s, x + Inches(0.15), y0, cw - Inches(0.3), Inches(0.6), [[(t, {"size": 14, "bold": True, "color": GD, "font": DISPLAY})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(0.2), y0 + Inches(0.8), cw - Inches(0.4), Inches(1.9), [[(f, {"size": 12, "color": INK})]], line=1.2)
        register_reveal(s, rev)
        text(s, x + Inches(0.2), y0 + Inches(2.75), cw - Inches(0.4), Inches(0.6), [[(nl, {"size": 10.5, "italic": True, "color": MUT})]], line=1.1)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.35), Inches(12.3), Inches(0.6),
             [[("Actividad: ", {"bold": True, "color": GD}), ("¿Qué país quieres visitar y por qué? Schrijf één zin met «Quiero visitar … porque …».", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · CULTURE (identiteit in diversiteit, LPD 5). Onthul per kaart. Bruggetje naar La Ruta (U1 begint de reis). "
             "Online: klikbare wereldkaart.")

# ============================================================ DIA 17 · QUIZ — completa (presentarse)
def s17_quiz_pres():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · QUIZ · INTERACCIÓN", "Completa la presentación", "Wat past? Klik → het antwoord verschijnt.", num=1)
    items = [("¿Cómo te ___? (heten)", "llamas"), ("___ de Bélgica. (ik kom uit)", "Soy"),
             ("Tengo dieciséis ___.", "años"), ("¿De ___ eres? (waar)", "dónde"),
             ("Yo ___ en Gante. (wonen)", "vivo"), ("Mucho ___. (aangenaam)", "gusto")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.78)
    for i, (q, ans) in enumerate(items):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(3.9), rh, [[(q, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.1), y, cw - Inches(4.25), rh, [[("→ " + ans, {"size": 12, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Presentarse: ", {"bold": True, "color": GD}), ("¿Cómo te llamas? · Soy de … · Tengo … años · ¿De dónde eres? · Vivo en … · Mucho gusto.", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ interactie. Klas vult vóór de klik. Daarna de presentación in parejas.")

# ============================================================ DIA 18 · FINAL_MISSION — Tarjeta de reencuentro
def s18_tarea():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(1.35), fill=GD)
    text(s, Inches(0.5), Inches(0.18), Inches(9), Inches(1.0),
         [[("🪪 Tarea final · Tarjeta de reencuentro", {"size": 28, "bold": True, "color": WHITE, "font": DISPLAY})],
          [("Maak je terugkeer-kaartje voor de klasmuur y preséntate en pareja.", {"size": 13, "italic": True, "color": GT})]])
    avatar(s, "mochila", Inches(11.6), Inches(0.2), Inches(1.0))
    pasos = [("1", "Planifica tus datos", "nombre · edad · origen · lengua · carácter"),
             ("2", "Escribe la tarjeta", "4–5 frases con me llamo / soy / tengo / vivo / hablo + conector"),
             ("3", "Preséntate en pareja", "lee en voz alta; tu compañero/a anota un dato y pregunta"),
             ("4", "Graba tu presentación", "en la web (recorder) — escúchate y mejora"),
             ("5", "Cuelga la tarjeta", "en el muro de la clase")]
    y = Inches(1.7)
    for n, es, nl in pasos:
        b = rect(s, Inches(0.5), y, Inches(0.5), Inches(0.5), fill=G, round=True, radius=0.5)
        tf = b.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE; p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        rr = p.add_run(); rr.text = n; rr.font.size = Pt(15); rr.font.bold = True; rr.font.name = DISPLAY; rr.font.color.rgb = WHITE
        text(s, Inches(1.2), y, Inches(4.2), Inches(0.55), [[(es, {"size": 14, "bold": True, "color": GD, "font": DISPLAY})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, Inches(5.5), y, Inches(7.2), Inches(0.55), [[(nl, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        y = y + Inches(0.62)
    text(s, Inches(0.5), Inches(5.0), Inches(12), Inches(0.35), [[("Rúbrica · ¿lo logré?", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    crit = ["5 datos (nombre·edad·origen·lengua·carácter)", "presente correcto (soy/tengo/vivo)", "un conector (y/pero/porque)", "presentar en pareja"]
    x = Inches(0.5)
    for c in crit:
        chip(s, x, Inches(5.45), "☐ " + c, fill=GT, tcolor=GD, size=10, w=Inches(3.05)); x = x + Inches(3.15)
    text(s, Inches(0.5), Inches(6.05), Inches(12), Inches(0.4),
         [[("🎯 ", {"size": 12}), ("Afzender jij · ontvanger de klas (el muro) · doel jezelf (opnieuw) voorstellen · situatie de eerste les · resultaat: tarjeta + presentación oral.", {"size": 11.5, "italic": True, "color": MUT})]])
    foot(s)
    notes(s, "TEACHER · FINAL_MISSION (communicatieve eindtaak). Afzender/ontvanger/doel/situatie/resultaat expliciet. Beoordeel met de rúbrica; "
             "opname + zelfevaluatie op de digitale pagina.")

# ============================================================ DIA 19 · QUIZ — la mezcla (retrieval)
def s19_mezcla():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "QUIZ · LA MEZCLA", "Ophaal door elkaar", "Gemengde ophaal van de hele unit. Klik een vraag → het antwoord. (retrieval)", num=1)
    items = [("yo (ser)", "soy"), ("tú (tener)", "tienes"), ("nosotros (vivir)", "vivimos"),
             ("España → nacionalidad", "español/a"), ("la chica (alto)", "alta"), ("el ___ problema", "el"),
             ("«want/omdat» =", "porque"), ("en clase → soy/estoy?", "estoy")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.62)
    for i, (q, a) in enumerate(items):
        c = i // 4; r = i % 4; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.16))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(3.4), rh, [[(q, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(3.55), y, cw - Inches(3.7), rh, [[("→ " + a, {"size": 12, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.05), Inches(12.3), Inches(0.55),
             [[("Alles komt terug: ", {"bold": True, "color": GD}), ("el presente · género/concordancia · ser/estar · países/nacionalidades · conectores.", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ mezcla (retrieval vóór herlezen). Zonder waarschuwing door elkaar. Exit-ticket. Zwakke punten → terug via menu.")

# ============================================================ DIA 20 · FEEDBACK/REPASO
def s20_repaso():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "REPASO · LO ESENCIAL", "Lo esencial de un vistazo", "De volledige herhaling (13 spellen, drills) staat online. Hier: de kern + semáforo.", num=1)
    ess = ["Presentarte: me llamo · soy (de) · tengo … años · vivo en · hablo …",
           "El presente: -ar → o/as/a/amos/áis/an · -er/-ir gelijkaardig · 7 onreg. (soy·estoy·tengo·voy·hago·vengo·doy).",
           "Concordancia: el chico alto / la chica alta · los/las + -os/-as.",
           "Países/nacionalidades: soy de España, soy español/a (kleine letter), hablo español.",
           "🔴 Trampas: soy ≠ estoy · porque = want én omdat · nacionalidad = kleine letter · belga = m/v gelijk."]
    card(s, Inches(0.5), Inches(1.6), Inches(12.3), Inches(2.5), fill=CREMA, line=None)
    y = Inches(1.8)
    for e in ess:
        text(s, Inches(0.8), y, Inches(11.8), Inches(0.45), [[("• ", {"size": 13, "bold": True, "color": GD}), (e, {"size": 12, "color": INK})]])
        y = y + Inches(0.46)
    text(s, Inches(0.5), Inches(4.3), Inches(12), Inches(0.35), [[("Semáforo — ¿cómo lo llevas?", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    can = ["saludar + presentarse", "el presente (regular + ser/estar/tener/ir)", "género + concordancia", "país/nacionalidad/lengua", "leer un perfil + escribir una tarjeta"]
    y = Inches(4.75)
    for c in can:
        text(s, Inches(0.8), y, Inches(7.0), Inches(0.4), [[(c, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        for j, (em, col) in enumerate([("🔴", RED), ("🟠", AMBER), ("🟢", G)]):
            chip(s, Inches(8.0) + j * Inches(1.5), y + Inches(0.03), em + " ", fill=WHITE, tcolor=col, size=12, w=Inches(1.3))
        y = y + Inches(0.42)
    foot(s)
    notes(s, "TEACHER · FEEDBACK/REPASO. Semáforo = zelfevaluatie. Repaso-drills online (13 spellen). Bruggetje: U1 «El día a día» — "
             "rutina, gustos (me gusta) en ser vs estar.")

# ============================================================ DIA 21 · TEACHER_NOTES
def s21_teacher():
    s = slide(); bg(s, GD)
    text(s, Inches(0.6), Inches(0.4), Inches(12), Inches(0.8), [[("TEACHER_NOTES · U0 «¡Volvemos!»", {"size": 26, "bold": True, "color": WHITE, "font": DISPLAY})]])
    blocks = [("Timing (50 min)", "Menu 2' · saludos/presentarse 8' · el presente 12' · género 8' · ser/estar 5' · lectura/escucha 8' · cultura 3' · Tarea-briefing 4'."),
              ("Kernvalstrikken", "soy ≠ estoy (identiteit vs plaats/gevoel) · porque = want én omdat · nacionalidades met kleine letter · belga = m/v gelijk · el problema/día/mapa (m), la mano/foto (f)."),
              ("Differentiatie (zij-instromers)", "U0 = diagnostisch, geen heronderwijs. Sterker: volledige presentación + tarjeta + perfil beschrijven. Zwakker: presente-tabel + soy/estoy-kaart langer open, frames houden."),
              ("Digitaal", "13 spellen + flip cards + klikbare wereldkaart + recorder (Hablar) + Lectura (dos perfiles) op de página digital. QR's in het boek → juiste anker. Conjugador = aparte tool."),
              ("Evaluatie", "Tarea «Tarjeta de reencuentro» met rúbrica (4 criteria). LPD 1·2·3·4·7 + 5 (cultura). U0 = opstap, geen zware toetsing.")]
    y = Inches(1.4)
    for t, b in blocks:
        card(s, Inches(0.5), y, Inches(12.3), Inches(1.0), fill=RGBColor(0x47, 0x30, 0x69), line=None)
        text(s, Inches(0.75), y + Inches(0.08), Inches(11.8), Inches(0.4), [[(t, {"size": 14, "bold": True, "color": WHITE, "font": DISPLAY})]])
        text(s, Inches(0.75), y + Inches(0.48), Inches(11.8), Inches(0.5), [[(b, {"size": 11.5, "color": GT})]], line=1.12)
        y = y + Inches(1.12)
    footer(s, tab=TAB, page=pg())
    notes(s, "Alleen in het docentdeck. Volledige LPD-dekking en didactische route staan in het cursusdossier (cocktail + outline).")

# ============================================================ RUN + BUILD
def _run_all(include_teacher=True):
    s01_title(); s02_menu(); s03_vocab(); s04_presente(); s05_presente_quiz(); s06_ser(); s07_genero()
    s08_genero_quiz(); s09_reading(); s10_listening(); s11_ser_estar(); s12_speaking(); s13_writing()
    s14_paises(); s15_taller(); s16_cultura(); s17_quiz_pres(); s18_tarea(); s19_mezcla(); s20_repaso()
    if include_teacher:
        s21_teacher()

def build(mode, out, include_teacher=True):
    E.MODE = mode
    E.new_presentation()
    _run_all(include_teacher=include_teacher)
    ndia_timing, nreveals = E.apply_all_timing()
    E.apply_hyperlinks()
    E.prs.save(out)
    ndias = len(E.prs.slides._sldIdLst)
    print(f"opgeslagen: {out} · {ndias} dia's · {ndia_timing} met animaties · {nreveals} onthullingen · {len(E.MENU_LINKS)} hyperlinks")
    return out, ndias

if __name__ == "__main__":
    build("docente", OUT_DOCENTE, include_teacher=True)
    build("alumno", OUT_ALUMNO_PPTX, include_teacher=False)
    from pptx import Presentation
    d = Presentation(OUT_DOCENTE); a = Presentation(OUT_ALUMNO_PPTX)
    print("docente dia's:", len(d.slides._sldIdLst), "· alumno dia's:", len(a.slides._sldIdLst))
