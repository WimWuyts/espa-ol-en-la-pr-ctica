#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_c6plus_u6_docente.py — Interactieve PowerPoint C6+ · Unidad 6 «Cuando era pequeño»
======================================================================================
Zelfde engine/pijplijn als de golden sample (gen_u0_docente = de engine). Cursuskleur = PAARS.
Twee decks (.pptx): docente (oplossingen + notities) + alumno (F5, klik onthult).
Grammatica: pretérito imperfecto · contraste indef./imperf. · comparativos + que.
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

E.G  = RGBColor(0x7C, 0x56, 0xA9)
E.GD = RGBColor(0x5B, 0x3E, 0x83)
E.GT = RGBColor(0xEE, 0xE8, 0xF5)
G, GD, GT = E.G, E.GD, E.GT
E.F_OBJ  = RGBColor(0xB4, 0x30, 0x9A)
E.F_PLAC = RGBColor(0x64, 0x74, 0x8B)
F_OBJ, F_PLAC = E.F_OBJ, E.F_PLAC

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DOCENTE = os.path.join(HERE, "C6plus_U6_docente.pptx")
OUT_ALUMNO_PPTX = os.path.join(HERE, "C6plus_U6_alumno.pptx")
TAB = "U6 · CUANDO ERA PEQUEÑO"

def foot(s): footer(s, tab=TAB, page=pg())

# ============================================================ DIA 1 · TITLE
def s01_title():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(4.7), fill=G)
    rect(s, 0, Inches(4.7), EMU_W, Inches(0.09), fill=GD)
    text(s, Inches(0.6), Inches(0.35), Inches(3.4), Inches(3.6),
         [[("6", {"size": 260, "bold": True, "color": RGBColor(0x93, 0x74, 0xC2), "font": DISPLAY})]], anchor=MSO_ANCHOR.MIDDLE)
    chip(s, Inches(4.35), Inches(0.85), "LA RUTA · CUSCO 🇵🇪 · CUANDO ERA PEQUEÑO 🧸", fill=WHITE, tcolor=GD, size=12)
    text(s, Inches(4.3), Inches(1.35), Inches(8.6), Inches(1.5), [[("Cuando era pequeño", {"size": 46, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(4.35), Inches(2.7), Inches(8.4), Inches(0.6),
         [[("Recuerdos: el imperfecto (era, jugaba) · contraste · comparativos.", {"size": 15, "italic": True, "color": GT})]])
    text(s, Inches(4.35), Inches(3.35), Inches(8.4), Inches(0.9),
         [[("¿Cómo era tu vida de pequeño/a?", {"size": 22, "bold": True, "color": WHITE, "font": DISPLAY})],
          [("Hoe was je leven toen je klein was?", {"size": 13, "italic": True, "color": GT})]])
    text(s, Inches(0.6), Inches(4.95), Inches(6), Inches(0.4),
         [[("La gente de la ruta — parada 6: Cusco (Nina)", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    x = Inches(0.6)
    for nm, city in [("diego","CDMX 🇲🇽"),("valen","Cartagena 🇨🇴"),("mateo","BsAs 🇦🇷"),
                     ("nina","Cusco 🇵🇪"),("tu","Tú · Flandes 🇧🇪"),("mochila","La mochila")]:
        avatar(s, nm, x, Inches(5.4), Inches(1.0))
        text(s, x - Inches(0.15), Inches(6.42), Inches(1.3), Inches(0.5),
             [[(nm.capitalize() if nm != "tu" else "Tú", {"size": 10.5, "bold": True, "color": INK})],
              [(city.split("·")[-1].strip() if nm != "tu" else "de reiziger = jij", {"size": 8.5, "color": MUT})]], align=PP_ALIGN.CENTER)
        x = x + Inches(2.05)
    foot(s)
    notes(s, "TEACHER · TITLE. U6 = de onvoltooid verleden tijd. Kerngrammatica: imperfecto (era/iba/veía) + contraste indef./imperf. + comparativos. "
             "Parada 6 = Cusco (Nina). Kernvalstrikken: imperfecto = achtergrond/gewoonte ≠ indefinido (feit) · accent op -ía · mejor/peor (niet «más bueno»). "
             "Docentdeck = oplossing; leerlingdeck (.pptx, F5) = klik onthult.")

# ============================================================ DIA 2 · MENU
def s02_menu():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "MENÚ DE LA LECCIÓN", "El mapa de la Unidad 6",
               "Kies je route — klik een tegel. Alles oefent naar de Tarea «Cuando era pequeño/a» toe.", num=6)
    tiles = [
        ("§1", "La infancia", "recuerdos · escuela", G, 3),
        ("§2", "El imperfecto", "era · tenía · jugaba", G, 4),
        ("§3", "Contraste", "indef. ↔ imperf.", G, 6),
        ("§4", "Comparativos", "más/menos … que", G, 7),
        ("§4b", "Que / donde", "relativo", G, 11),
        ("★", "Lectura + escucha", "el pueblo de mi abuela", GD, 9),
        ("👵", "Cultura", "la infancia hispana", GD, 17),
        ("🧸", "Tarea · Mi infancia", "recuerdo + opinión", GD, 18),
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
        rr = p.add_run(); rr.text = tag; rr.font.size = Pt(11); rr.font.bold = True; rr.font.name = DISPLAY; rr.font.color.rgb = col
        text(s, x + Inches(0.58), y + Inches(0.06), tw - Inches(0.7), Inches(0.4), [[(es, {"size": 14, "bold": True, "color": WHITE, "font": DISPLAY})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(0.18), y + Inches(0.68), tw - Inches(0.36), Inches(1.2), [[(nl, {"size": 11.5, "color": INK})]], line=1.12)
        chip(s, x + Inches(0.18), y + th - Inches(0.45), f"→ dia {dia}", fill=GT, tcolor=GD, size=9.5)
    foot(s)
    notes(s, "TEACHER · LESSON_MENU. Kern = §2 imperfecto + §3 contraste. Kruisverwijzing: «oefen online — 12 juegos + 100+ oefeningen».")

# ============================================================ DIA 3 · VOCAB
def s03_vocab():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · VOCABULARIO", "La infancia", "De woorden van de jeugd — observa. Herken ze, dan gebruik je ze.", num=1)
    legend_func(s, Inches(9.7), Inches(0.55))
    rows = [("de pequeño", "als kind", "el recuerdo"), ("el juguete", "het speelgoed", "jugar"),
            ("la escuela", "de school", "el patio, el recreo"), ("la maestra", "de juf", "el compañero"),
            ("los abuelos", "de grootouders", "el pueblo"), ("la mascota", "het huisdier", "cuidar"),
            ("antes ↔ ahora", "vroeger ↔ nu", "ya no / todavía"), ("a menudo", "vaak", "siempre")]
    x0, y0 = Inches(0.5), Inches(1.6); cw = Inches(6.1); rh = Inches(0.6)
    for i, (k, v, nl) in enumerate(rows):
        c = 0 if i < 4 else 1; r = i % 4
        x = x0 + c * (cw + Inches(0.15)); y = y0 + r * (rh + Inches(0.12))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(2.4), rh, [[(k, {"size": 13, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(2.5), y, Inches(2.1), rh, [[(v, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(4.5), y, Inches(1.5), rh, [[(nl, {"size": 9, "italic": True, "color": MUT})]], anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(4.75), Inches(12.3), Inches(0.5),
         [[("Markers → imperfecto: ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("siempre · a menudo · todos los días · antes (gewoonte, achtergrond).", {"size": 13, "color": INK})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.35), Inches(12.3), Inches(0.95),
             [[("Antes ↔ ahora: ", {"bold": True, "color": GD}), ("antes ↔ ahora · ya no ↔ todavía. Echo de menos = ik mis. Me acuerdo de = ik herinner me.", {"color": GD})],
              [("Infancia: el recuerdo, el juguete, jugar, soñar, pasarlo bien.", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCABULARY. Laat de jeugdwoorden raden. Online: memoria de la infancia + antes/ahora.")

# ============================================================ DIA 4 · GRAMMAR imperfecto (color)
def s04_imperf():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · GRAMÁTICA VISUAL", "El pretérito imperfecto", "-ar → -aba · -er/-ir → -ía. Voor gewoontes en beschrijving.", num=2)
    legend_func(s, Inches(9.7), Inches(0.55))
    seg = [("De pequeña ", F_TIME), ("Nina ", F_SUBJ), ("vivía ", F_VERB), ("en un pueblo", F_PLAC)]
    runs = [[(t, {"size": 21, "bold": True, "color": c, "font": DISPLAY}) for t, c in seg]]
    card(s, Inches(0.5), Inches(1.7), Inches(12.3), Inches(1.2), fill=GT, line=None)
    text(s, Inches(0.8), Inches(1.7), Inches(11.7), Inches(1.2), runs, anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(3.15), Inches(12), Inches(0.4), [[("Las terminaciones (+ 3 irregulares)", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    frame = [("-ar → aba", "jugaba"), ("-er/-ir → ía", "comía / vivía"), ("nos. -ábamos/-íamos", "jugábamos"),
             ("ser → era", "era/eras/era…"), ("ir → iba", "iba/ibas/iba…"), ("ver → veía", "veía/veías…")]
    x0, y0 = Inches(0.5), Inches(3.6); cw = Inches(4.0); rh = Inches(0.62)
    for i, (a, b) in enumerate(frame):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.12))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(2.1), rh, [[(a, {"size": 11, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(2.25), y, cw - Inches(2.4), rh, [[(b, {"size": 10.5, "color": F_VERB, "bold": True})]], anchor=MSO_ANCHOR.MIDDLE)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.75), Inches(12.3), Inches(0.6),
             [[("Regla: ", {"bold": True, "color": GD}), ("yo = él/ella (jugaba, comía). Slechts 3 irregulares: era · iba · veía. Accent op -ía. Markers: siempre, a menudo.", {"color": GD})]],
             trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR imperfecto. Toon raíz + uitgang. Online: completa el imperfecto (cloze) + imperfecto Tetris.")

# ============================================================ DIA 5 · QUIZ imperfecto (reveal)
def s05_imperf_quiz():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · QUIZ", "¿Qué forma del imperfecto?", "Klik een zin → de juiste vorm.", num=2)
    items = [("Nina ___ (vivir) en un pueblo.", "vivía"), ("(Ella) ___ (ser) tímida.", "era"),
             ("Todos los días ___ (ir).", "iba"), ("(Yo) ___ (jugar) en el patio.", "jugaba"),
             ("(Yo) ___ (ver) dibujos.", "veía"), ("Nosotros ___ (comer) en casa.", "comíamos")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.78)
    for i, (q, a) in enumerate(items):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(4.0), rh, [[(q, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.2), y, cw - Inches(4.3), rh, [[("→ " + a, {"size": 12.5, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Truc: ", {"bold": True, "color": RED}), ("-ar → aba · -er/-ir → ía · era/iba/veía. yo = él/ella.", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ imperfecto (retrieval). Klas roept vóór de klik. Online: cloze el imperfecto.")

# ============================================================ DIA 6 · GRAMMAR contraste (reveal)
def s06_contraste():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · GRAMÁTICA", "Contraste — indefinido ↔ imperfecto", "Klik → de tijd. imperfecto = fondo · indefinido = acción.", num=3)
    items = [("Era de noche (decor)", "imperfecto"), ("Sonó el teléfono (feit)", "indefinido"),
             ("Siempre jugaba (gewoonte)", "imperfecto"), ("Un día llegó (feit)", "indefinido"),
             ("Tenía cinco años (beschr.)", "imperfecto"), ("De repente empezó (feit)", "indefinido")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.78)
    for i, (q, a) in enumerate(items):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(4.0), rh, [[(q, {"size": 11.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.2), y, cw - Inches(4.3), rh, [[("→ " + a, {"size": 12, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Vaak samen: ", {"bold": True, "color": GD}), ("Jugaba (imperf. = achtergrond) cuando, de repente, empezó (indef. = gebeurtenis) a llover.", {"color": GD})]], trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR contraste (kernpunt A2). Coro vóór de klik. Online: ¿indefinido o imperfecto? (classify).")

# ============================================================ DIA 7 · GRAMMAR comparativos (color)
def s07_comparativos():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · GRAMÁTICA VISUAL", "Comparativos + que", "más/menos … que · tan … como · irr. mejor/peor/mayor/menor.", num=4)
    legend_func(s, Inches(9.7), Inches(0.55))
    card(s, Inches(0.5), Inches(1.7), Inches(12.3), Inches(1.1), fill=GT, line=None)
    text(s, Inches(0.8), Inches(1.7), Inches(11.7), Inches(1.1),
         [[("El pueblo era ", {"size": 16, "color": INK}), ("más ", {"size": 18, "bold": True, "color": F_VERB}),
           ("tranquilo ", {"size": 16, "color": INK}), ("que ", {"size": 18, "bold": True, "color": F_OBJ}), ("la ciudad.", {"size": 16, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
    frame = [("más … que", "más alto que"), ("menos … que", "menos caro que"), ("tan … como", "tan alto como"),
             ("mejor / peor", "beter / slechter"), ("mayor / menor", "ouder / jonger"), ("el/la más …", "de meeste")]
    x0, y0 = Inches(0.5), Inches(3.15); cw = Inches(4.0); rh = Inches(0.62)
    for i, (a, b) in enumerate(frame):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.12))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(2.0), rh, [[(a, {"size": 11.5, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(2.15), y, cw - Inches(2.3), rh, [[(b, {"size": 10.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.75),
             [[("Regla: ", {"bold": True, "color": GD}), ("más/menos + adj + que · tan + adj + como. 🔴 mejor (niet «más bueno») · mayor/menor voor personen.", {"color": GD})]],
             trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR comparativos. Toon de balk (más/menos/tan). Online: ¿más, menos o tan? (classify).")

# ============================================================ DIA 8 · QUIZ comparativos (reveal)
def s08_comp_quiz():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · QUIZ", "Comparativos", "Klik een zin → de juiste optie.", num=4)
    items = [("La ciudad es ___ grande ___ el pueblo. (groter)", "más … que"), ("Es ___ alto ___ yo. (even)", "tan … como"),
             ("bueno → comparativo", "mejor"), ("malo → comparativo", "peor"),
             ("Mi hermana (viejo) es ___ que yo.", "mayor"), ("Soy (joven) ___ que mi primo.", "menor")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.78)
    for i, (q, a) in enumerate(items):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(3.9), rh, [[(q, {"size": 11.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.1), y, cw - Inches(4.2), rh, [[("→ " + a, {"size": 12, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Irregulares: ", {"bold": True, "color": GD}), ("mejor · peor · mayor · menor. Nooit «más bueno/malo».", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ comparativos (retrieval). Online: ¿más, menos o tan? (classify).")

# ============================================================ DIA 9 · READING
def s09_reading():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§5 · LEER · COMPRENSIÓN", "Dos infancias — «El pueblo de mi abuela»", "Lees. Klik een vraag → het antwoord verschijnt.", num=5)
    card(s, Inches(0.5), Inches(1.65), Inches(5.6), Inches(3.9), fill=GT, line=G, lw=1.4)
    avatar(s, "nina", Inches(0.85), Inches(1.95), Inches(1.0))
    text(s, Inches(2.05), Inches(1.98), Inches(3.9), Inches(1.5),
         [[("«De pequeña vivía en un pueblo cerca de Cusco. La casa de mi abuela era de adobe y tenía un patio. Iba a la escuela a pie. Había menos coches y todo era más tranquilo que ahora.»", {"size": 11, "italic": True, "color": INK})]], line=1.16)
    avatar(s, "diego", Inches(0.85), Inches(3.65), Inches(1.0))
    text(s, Inches(2.05), Inches(3.68), Inches(3.9), Inches(1.5),
         [[("«Yo crecí en la ciudad. De niño veía mucha tele y jugaba a videojuegos. Mi barrio era más ruidoso que el de Nina. Un día gané un concurso de dibujo.»", {"size": 11, "italic": True, "color": INK})]], line=1.16)
    qa = [("¿Dónde vivía Nina?", "En un pueblo"), ("¿Cómo era todo (Nina)?", "Más tranquilo"),
          ("¿Dónde creció Diego?", "En la ciudad"), ("¿Qué ganó Diego un día?", "Un concurso de dibujo")]
    x = Inches(6.4); y = Inches(1.7)
    for q, a in qa:
        card(s, x, y, Inches(6.4), Inches(0.85), fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y + Inches(0.06), Inches(6.1), Inches(0.4), [[(q, {"size": 12.5, "bold": True, "color": GD})]])
        rev = text(s, x + Inches(0.15), y + Inches(0.44), Inches(6.1), Inches(0.35), [[("→ " + a, {"size": 12, "color": INK})]])
        register_reveal(s, rev); y = y + Inches(0.98)
    btn = noodroute(s)
    exercise_solucion(s, Inches(6.4), Inches(5.65), Inches(6.4), Inches(0.6),
             [[("🎯 Leesdoel: ", {"bold": True, "color": GD}), ("scannen naar het imperfecto (era, tenía…) + una comparación.", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · READING (lezen→schrijven). Eerst globaal, dan scannen. Daarna: eigen jeugd met het imperfecto.")

# ============================================================ DIA 10 · LISTENING
def s10_listening():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · ESCUCHAR · INTERACCIÓN", "¿Cómo era tu infancia?", "Volg het verhaal. Klik un dato → de info. (audio + script op de web)", num=2)
    pasos = [("🔊 ¿Dónde vivía?", "En un pueblo"), ("🔊 ¿Qué tenía?", "Un perro"),
             ("🔊 ¿Qué hacía?", "Jugaba en la calle"), ("🔊 ¿Cómo era?", "Todo más tranquilo")]
    x0, y0 = Inches(0.7), Inches(1.9); cw = Inches(2.95); ch = Inches(2.4)
    for i, (mom, det) in enumerate(pasos):
        x = x0 + i * (cw + Inches(0.1))
        card(s, x, y0, cw, ch, fill=WHITE, line=LINE, lw=1.2); rect(s, x, y0, cw, Inches(0.5), fill=GT)
        text(s, x, y0, cw, Inches(0.5), [[("dato " + str(i+1), {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(0.15), y0 + Inches(0.7), cw - Inches(0.3), Inches(0.7), [[(mom, {"size": 13, "bold": True, "color": INK, "font": DISPLAY})]], line=1.05)
        rev = text(s, x + Inches(0.15), y0 + Inches(1.5), cw - Inches(0.3), Inches(0.7), [[(det, {"size": 11, "color": G})]], line=1.05)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.85),
             [[("Modelo-audio (docent/TTS): ", {"bold": True, "color": GD}),
               ("«De pequeña vivía en un pueblo. Tenía un perro y jugaba en la calle. Todo era más tranquilo.» ", {"color": GD})],
              [("Daarna: A vertelt zijn jeugd, B vergelijkt (info-gap).", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · LISTENING (luisteren→spreken). Lees voor (of TTS); klas noteert. Online: ¿cómo era tu infancia? (audio).")

# ============================================================ DIA 11 · GRAMMAR relativo (reveal)
def s11_relativo():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4b · GRAMÁTICA", "La frase con que / donde", "Klik een cue → de vorm. Verbind twee zinnen.", num=4)
    items = [("die/dat (persoon/ding)", "que"), ("waar (plaats)", "donde"),
             ("El niño ___ jugaba", "que"), ("La casa ___ vivía", "donde"),
             ("vroeger", "antes"), ("nu", "ahora"), ("niet meer", "ya no"), ("nog steeds", "todavía")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.72)
    for i, (q, a) in enumerate(items):
        c = i // 4; r = i % 4; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.14))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(3.0), rh, [[(q, {"size": 12, "color": MUT})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(3.2), y, cw - Inches(3.3), rh, [[("→ " + a, {"size": 13, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.85), Inches(12.3), Inches(0.85),
             [[("Relativo: ", {"bold": True, "color": GD}), ("que = die/dat · donde = waar. «El niño que jugaba en el patio era yo.»", {"color": GD})],
              [("Antes ↔ ahora: en cambio, mientras, sin embargo (conectores de contraste).", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR relativo que/donde + antes/ahora. Online: que/donde in de cloze/order.")

# ============================================================ DIA 12 · QUIZ mezcla (reveal)
def s12_mezcla_imp():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2–§4 · QUIZ", "Imperfecto + contraste + comparativos", "Klik → het antwoord.", num=2)
    items = [("ser → imperfecto (él)", "era"), ("ir → imperfecto (yo)", "iba"),
             ("Un día ___ (llegar)", "llegó"), ("«groter dan»", "más grande que"),
             ("bueno → comparativo", "mejor"), ("El niño ___ jugaba era yo", "que")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.78)
    for i, (q, a) in enumerate(items):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(3.9), rh, [[(q, {"size": 11.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.1), y, cw - Inches(4.2), rh, [[("→ " + a, {"size": 12, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Alles komt terug: ", {"bold": True, "color": G}), ("imperfecto (era/iba/veía) · contraste · comparativos · que/donde.", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ mezcla (retrieval). Door elkaar. Online: cloze + imperfecto Tetris.")

# ============================================================ DIA 13 · SPEAKING
def s13_speaking():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · SPEAKING · INTERACCIÓN", "Cuenta cómo era tu infancia", "Speel de scène met de frames. Steun bouwt af: kaarten → beginwoorden → uit het hoofd.", num=2)
    avatar(s, "tu", Inches(11.4), Inches(1.7), Inches(1.3))
    labels = ["¿Dónde vivías?", "¿Qué tenías?", "¿Qué hacías?", "Un día…", "Antes ↔ ahora", "Tu opinión"]
    frames = ["Vivía en…", "Tenía…", "Jugaba / iba…", "Un día, de repente…", "Antes era más… que ahora", "Creo que antes…"]
    x0, y0 = Inches(0.5), Inches(1.8); cw = Inches(3.4); rh = Inches(0.8)
    for i, (lab, fr) in enumerate(zip(labels, frames)):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=G, lw=1.2, shadow=False)
        text(s, x + Inches(0.15), y + Inches(0.05), cw - Inches(0.3), Inches(0.32), [[(lab, {"size": 10, "color": MUT})]])
        text(s, x + Inches(0.15), y + Inches(0.36), cw - Inches(0.3), Inches(0.4), [[(fr, {"size": 11.5, "bold": True, "color": GD, "font": DISPLAY})]])
    chip(s, Inches(0.5), Inches(4.65), "🎙️ Grábate online · «Mensaje de voz: mi infancia / antes y ahora»", fill=GT, tcolor=GD, size=11)
    text(s, Inches(0.5), Inches(5.05), Inches(10.5), Inches(0.9),
         [[("Ronda 1: ", {"size": 12, "bold": True, "color": GD}), ("met de kaarten. ", {"size": 12, "color": INK}),
           ("Ronda 2: ", {"size": 12, "bold": True, "color": GD}), ("beginwoorden. ", {"size": 12, "color": INK}),
           ("Ronda 3: ", {"size": 12, "bold": True, "color": GD}), ("uit het hoofd. ", {"size": 12, "color": INK}),
           ("Ronda 4: ", {"size": 12, "bold": True, "color": GD}), ("grábate.", {"size": 12, "color": INK})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.6), Inches(12.3), Inches(0.65),
             [[("Modelo: ", {"bold": True, "color": GD}), ("«De pequeño vivía en un pueblo. Tenía un perro y jugaba en la calle. Un día llegó mi tío con una bici. Antes todo era más tranquilo que ahora.»", {"color": GD})]],
             trigger=btn, title_doc="MODELO · docent")
    foot(s)
    notes(s, "TEACHER · SPEAKING (interactie). Rondes met afbouwende steun. Online: recorder (mi infancia + antes/ahora).")

# ============================================================ DIA 14 · WRITING
def s14_writing():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "WRITING · PRODUCCIÓN", "Cuando era pequeño/a", "Schrijf een jeugdherinnering. Klik → een modeltekst verschijnt.", num=5)
    card(s, Inches(0.5), Inches(1.7), Inches(6.0), Inches(3.9), fill=WHITE, line=LINE, lw=1.2)
    text(s, Inches(0.7), Inches(1.85), Inches(5.6), Inches(0.4), [[("✍️ Escribe tu recuerdo:", {"size": 12, "bold": True, "color": GD})]])
    for i in range(6):
        rect(s, Inches(0.7), Inches(2.4) + i * Inches(0.5), Inches(5.6), Inches(0.01), fill=LINE)
    chk = ["cómo era todo (imperfecto)", "un día especial (indefinido)", "un contraste (era… cuando… pasó)", "una comparación (más/menos que)", "una opinión (creo que antes…)", "6–8 frases"]
    x = Inches(6.9); y = Inches(1.7)
    text(s, x, y, Inches(6), Inches(0.4), [[("Checklist:", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    for i, c in enumerate(chk):
        text(s, x, y + Inches(0.5) + i * Inches(0.45), Inches(6), Inches(0.4), [[("☐  " + c, {"size": 13, "color": INK})]])
    rev = card(s, x, Inches(4.35), Inches(6.0), Inches(1.25), fill=GT, line=G, lw=1.2)
    text(s, x + Inches(0.15), Inches(4.4), Inches(5.7), Inches(1.2),
         [[("Modelo: ", {"size": 12, "bold": True, "color": GD}),
           ("«De pequeña vivía en un pueblo. Tenía un perro y jugaba en la calle. Un día, de repente, empezó a llover y corrimos a casa. Antes todo era más tranquilo. Creo que era una época feliz.»", {"size": 11, "italic": True, "color": INK})]], line=1.13)
    register_reveal(s, rev)
    noodroute(s); foot(s)
    notes(s, "TEACHER · WRITING (lezen→schrijven). Checklist = zichtbare steun; onthul het model pas na het schrijven. Nakijkfocus: imperfecto, contraste, comparación, opinión. Voedt de Tarea.")

# ============================================================ DIA 15 · VOCAB antes/ahora (reveal)
def s15_antes():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · VOCABULARIO", "Antes y ahora", "Klik een kaart → la respuesta. Bouw je woordnetwerk.", num=1)
    data = [("antes", "vroeger"), ("ahora", "nu"), ("ya no", "niet meer"), ("todavía", "nog steeds"),
            ("siempre", "altijd"), ("a menudo", "vaak"), ("de repente", "plots"), ("la época", "de tijd"),
            ("echar de menos", "missen"), ("feliz", "gelukkig"), ("tranquilo", "rustig"), ("diferente", "anders")]
    x0, y0 = Inches(0.5), Inches(1.7); cw = Inches(3.0); rh = Inches(0.7)
    for i, (es, nl) in enumerate(data):
        c = i % 4; r = i // 4; x = x0 + c * (cw + Inches(0.1)); y = y0 + r * (rh + Inches(0.14))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.12), y, Inches(1.8), rh, [[(es, {"size": 11, "bold": True, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(1.75), y, cw - Inches(1.85), rh, [[("→ " + nl, {"size": 10.5, "color": G})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.9),
             [[("Markers → imperfecto: ", {"bold": True, "color": GD}), ("siempre · a menudo · todos los días (gewoonte). De repente → indefinido.", {"color": GD})],
              [("Contrast: antes ↔ ahora · ya no ↔ todavía.", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCAB antes/ahora. Klik onthult. Online: antes y ahora (memory) + señala.")

# ============================================================ DIA 16 · TALLER
def s16_taller():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "TALLER DE LENGUA", "El acento -ía + conectores", "Klik een item → correcte vorm. Gereedschap voor spelling en contrast.", num=1)
    text(s, Inches(0.5), Inches(1.5), Inches(6), Inches(0.35), [[("A · ortografía: el acento en -ía", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    fixes = [("tenia →", "tenía"), ("vivia →", "vivía"), ("comiamos →", "comíamos"), ("jugabamos →", "jugábamos")]
    y = Inches(1.95)
    for q, a in fixes:
        card(s, Inches(0.5), y, Inches(6.0), Inches(0.6), fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, Inches(0.62), y, Inches(3.0), Inches(0.6), [[(q, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, Inches(3.7), y, Inches(2.7), Inches(0.6), [[("→ " + a, {"size": 12, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y = y + Inches(0.72)
    text(s, Inches(6.9), Inches(1.5), Inches(6), Inches(0.35), [[("B · conectores de contraste", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    conn = [("en cambio", "daarentegen"), ("mientras", "terwijl"), ("sin embargo", "echter"), ("pero", "maar")]
    y = Inches(1.95)
    for q, a in conn:
        card(s, Inches(6.9), y, Inches(5.9), Inches(0.6), fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, Inches(7.02), y, Inches(3.0), Inches(0.6), [[(q, {"size": 12, "bold": True, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, Inches(10.1), y, Inches(2.6), Inches(0.6), [[("→ " + a, {"size": 11, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y = y + Inches(0.72)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.85),
             [[("A: ", {"bold": True, "color": GD}), ("-er/-ir in het imperfecto dragen altijd accent op í: tenía, vivía, comíamos, veía.", {"color": GD})],
              [("B: antes… en cambio, ahora… · mientras (terwijl, gelijktijdig) · sin embargo (echter).", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · TALLER. Accent -ía + contrast-connectoren. Online: drills in de hub.")

# ============================================================ DIA 17 · CULTURE
def s17_cultura():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "CULTURA · PARADA 6: CUSCO", "La infancia en el mundo hispano", "Klik een kaart → het weetje. Quinceañera, juegos y abuelos.", num=1)
    cards = [("🎉 La quinceañera", "In veel Latijns-Amerikaanse landen viert een meisje haar 15de verjaardag met een groot feest: de quinceañera. Overgang van kind naar jongvolwassene.", "un rito de paso"),
             ("🪀 Los juegos tradicionales", "Vroeger speelden kinderen la rayuela (hinkelen), el trompo (tol) en las canicas (knikkers) op straat. Nina «jugaba» ze in het dorp.", "en la calle"),
             ("👵 Los abuelos", "In de hispanofoon spelen de abuelos een grote rol: ze passen op, vertellen verhalen en geven de traditie door. «Iba a casa de mi abuela».", "la familia extensa")]
    x0, y0 = Inches(0.5), Inches(1.7); cw = Inches(4.05); ch = Inches(3.4)
    for i, (t, f, nl) in enumerate(cards):
        x = x0 + i * (cw + Inches(0.13))
        card(s, x, y0, cw, ch, fill=WHITE, line=G, lw=1.3); rect(s, x, y0, cw, Inches(0.6), fill=GT)
        text(s, x + Inches(0.15), y0, cw - Inches(0.3), Inches(0.6), [[(t, {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(0.2), y0 + Inches(0.8), cw - Inches(0.4), Inches(1.9), [[(f, {"size": 11.5, "color": INK})]], line=1.2)
        register_reveal(s, rev)
        text(s, x + Inches(0.2), y0 + Inches(2.75), cw - Inches(0.4), Inches(0.6), [[(nl, {"size": 10.5, "italic": True, "color": MUT})]], line=1.1)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.35), Inches(12.3), Inches(0.6),
             [[("Actividad: ", {"bold": True, "color": GD}), ("¿a qué jugabas de pequeño/a? Compara con los juegos hispanos (imperfecto + más… que).", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · CULTURE (LPD 5). Onthul per kaart. Bruggetje: La Ruta parada 6 = Perú (★, familia). Online: klik op Perú op de kaart.")

# ============================================================ DIA 18 · FINAL_MISSION
def s18_tarea():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(1.35), fill=GD)
    text(s, Inches(0.5), Inches(0.18), Inches(9), Inches(1.0),
         [[("🧸 Tarea final · Cuando era pequeño/a", {"size": 26, "bold": True, "color": WHITE, "font": DISPLAY})],
          [("Escribe un recuerdo con el imperfecto, un contraste y una comparación.", {"size": 13, "italic": True, "color": GT})]])
    avatar(s, "mochila", Inches(11.6), Inches(0.2), Inches(1.0))
    pasos = [("1", "Describe cómo era todo", "«De pequeño/a vivía… tenía… jugaba…»"),
             ("2", "Cuenta un día especial", "«Un día, de repente,…» (indefinido)"),
             ("3", "Compara antes ↔ ahora", "«Antes era más… que ahora»"),
             ("4", "Añade tu opinión", "«Creo que antes era… porque…»"),
             ("5", "Preséntalo y graba", "en la web (recorder) — escúchate y mejora")]
    y = Inches(1.7)
    for n, es, nl in pasos:
        b = rect(s, Inches(0.5), y, Inches(0.5), Inches(0.5), fill=G, round=True, radius=0.5)
        tf = b.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE; p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        rr = p.add_run(); rr.text = n; rr.font.size = Pt(15); rr.font.bold = True; rr.font.name = DISPLAY; rr.font.color.rgb = WHITE
        text(s, Inches(1.2), y, Inches(4.4), Inches(0.55), [[(es, {"size": 14, "bold": True, "color": GD, "font": DISPLAY})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, Inches(5.7), y, Inches(7.0), Inches(0.55), [[(nl, {"size": 11.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        y = y + Inches(0.62)
    text(s, Inches(0.5), Inches(5.0), Inches(12), Inches(0.35), [[("Rúbrica · ¿lo logré?", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    crit = ["imperfecto", "un contraste", "una comparación", "una opinión"]
    x = Inches(0.5)
    for c in crit:
        chip(s, x, Inches(5.45), "☐ " + c, fill=GT, tcolor=GD, size=10, w=Inches(3.05)); x = x + Inches(3.15)
    text(s, Inches(0.5), Inches(6.05), Inches(12), Inches(0.4),
         [[("🎯 ", {"size": 12}), ("Afzender jij · ontvanger de klas · doel je jeugd delen · situatie een herinnering · resultaat: recuerdo + presentación oral.", {"size": 11.5, "italic": True, "color": MUT})]])
    foot(s)
    notes(s, "TEACHER · FINAL_MISSION (communicatieve eindtaak). Beoordeel met de rúbrica; opname op de web.")

# ============================================================ DIA 19 · MEZCLA
def s19_mezcla():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "QUIZ · LA MEZCLA", "Ophaal door elkaar", "Gemengde ophaal van de hele unit. Klik → het antwoord. (retrieval)", num=1)
    items = [("jugar → imperfecto (yo)", "jugaba"), ("ser → imperfecto (él)", "era"),
             ("ir → imperfecto (yo)", "iba"), ("Un día ___ (llegar)", "llegó"),
             ("«groter dan»", "más grande que"), ("bueno → comparativo", "mejor"),
             ("«nog steeds»", "todavía"), ("El niño ___ jugaba", "que")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.62)
    for i, (q, a) in enumerate(items):
        c = i // 4; r = i % 4; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.16))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(4.0), rh, [[(q, {"size": 11.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.15), y, cw - Inches(4.3), rh, [[("→ " + a, {"size": 12, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.05), Inches(12.3), Inches(0.55),
             [[("Alles komt terug: ", {"bold": True, "color": GD}), ("imperfecto · contraste indef/imperf · comparativos · que/donde.", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ mezcla (retrieval vóór herlezen). Exit-ticket. Zwakke punten → terug via menu.")

# ============================================================ DIA 20 · REPASO
def s20_repaso():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "REPASO · LO ESENCIAL", "Lo esencial de un vistazo", "De volledige herhaling (12 spellen, drills) staat online. Hier: de kern + semáforo.", num=1)
    ess = ["Imperfecto: -ar → aba/abas/aba/ábamos/abais/aban · -er/-ir → ía/ías/ía/íamos/íais/ían.",
           "Sólo 3 irregulares: ser → era · ir → iba · ver → veía.",
           "Contraste: imperfecto = achtergrond/gewoonte (era, jugaba) · indefinido = gebeurtenis (llegó).",
           "Comparativos: más/menos … que · tan … como · irr. mejor/peor/mayor/menor.",
           "🔴 Trampas: accent op -ía (tenía) · imperf. ≠ indef. · mejor (niet «más bueno»)."]
    card(s, Inches(0.5), Inches(1.6), Inches(12.3), Inches(2.5), fill=CREMA, line=None)
    y = Inches(1.8)
    for e in ess:
        text(s, Inches(0.8), y, Inches(11.8), Inches(0.45), [[("• ", {"size": 13, "bold": True, "color": GD}), (e, {"size": 12, "color": INK})]])
        y = y + Inches(0.46)
    text(s, Inches(0.5), Inches(4.3), Inches(12), Inches(0.35), [[("Semáforo — ¿cómo lo llevas?", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    can = ["over mijn jeugd praten (recuerdos)", "het imperfecto vormen (era, tenía, jugaba)", "het contrast indef/imperf gebruiken", "vergelijken met más/menos/tan", "zinnen koppelen met que/donde"]
    y = Inches(4.75)
    for c in can:
        text(s, Inches(0.8), y, Inches(7.0), Inches(0.4), [[(c, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        for j, (em, col) in enumerate([("🔴", RED), ("🟠", AMBER), ("🟢", G)]):
            chip(s, Inches(8.0) + j * Inches(1.5), y + Inches(0.03), em + " ", fill=WHITE, tcolor=col, size=12, w=Inches(1.3))
        y = y + Inches(0.42)
    foot(s)
    notes(s, "TEACHER · FEEDBACK/REPASO. Semáforo = zelfevaluatie. Repaso-drills online. Bruggetje: U7 «¡Opina y cuídate!» — imperativo + mening/argumentatie (Costa Rica, salud/milieu).")

# ============================================================ DIA 21 · TEACHER
def s21_teacher():
    s = slide(); bg(s, GD)
    text(s, Inches(0.6), Inches(0.4), Inches(12), Inches(0.8), [[("TEACHER_NOTES · U6 «Cuando era pequeño»", {"size": 24, "bold": True, "color": WHITE, "font": DISPLAY})]])
    blocks = [("Timing (50 min)", "Menu 2' · infancia 6' · imperfecto 12' · contraste 8' · comparativos 8' · que/escucha 6' · Tarea-briefing 4'."),
              ("Kernvalstrikken", "imperfecto = achtergrond/gewoonte (siempre, era) ≠ indefinido (un día, feit) · accent op -ía (tenía) · slechts 3 irr (era/iba/veía) · comparativos irr (mejor/peor/mayor/menor, niet «más bueno»)."),
              ("Differentiatie", "Sterker: volledig jeugdverhaal + contraste + comparación + una opinión. Zwakker: imperfecto-tabel + contrast-beslisboom langer open, frames houden; comparativos met vaste voorbeeldparen."),
              ("Digitaal", "12 spellen + flip cards + gramática interactiva (imperfecto · contraste · comparativos) + recorder (mi infancia · antes/ahora) + Lectura (Nina/Diego) + klikbare kaart (Perú ★, familia) op de página digital. QR's → juiste anker."),
              ("Evaluatie & LPD", "Tarea «Cuando era pequeño/a» met rúbrica (4 criteria). LPD (III-Spa-d): infancia 7 · imperfecto/contraste/comparativos 8 · beschrijven 3 · interactie 4 · lezen 1·2·5 · cultuur 5. Sluit de verleden-tijdenboog (U4–U6).")]
    y = Inches(1.4)
    for t, b in blocks:
        card(s, Inches(0.5), y, Inches(12.3), Inches(1.0), fill=RGBColor(0x47, 0x30, 0x69), line=None)
        text(s, Inches(0.75), y + Inches(0.08), Inches(11.8), Inches(0.4), [[(t, {"size": 14, "bold": True, "color": WHITE, "font": DISPLAY})]])
        text(s, Inches(0.75), y + Inches(0.48), Inches(11.8), Inches(0.5), [[(b, {"size": 11, "color": GT})]], line=1.1)
        y = y + Inches(1.12)
    footer(s, tab=TAB, page=pg())
    notes(s, "Alleen in het docentdeck. Volledige LPD-dekking en didactische route staan in het cursusdossier (cocktail + outline).")

# ============================================================ RUN + BUILD
def _run_all(include_teacher=True):
    s01_title(); s02_menu(); s03_vocab(); s04_imperf(); s05_imperf_quiz(); s06_contraste(); s07_comparativos()
    s08_comp_quiz(); s09_reading(); s10_listening(); s11_relativo(); s12_mezcla_imp(); s13_speaking(); s14_writing()
    s15_antes(); s16_taller(); s17_cultura(); s18_tarea(); s19_mezcla(); s20_repaso()
    if include_teacher:
        s21_teacher()

def _repaint(path):
    import zipfile, os as _os
    reps = [("1E9E74", "7C56A9"), ("1e9e74", "7c56a9"), ("2EB085", "9374C2"), ("2eb085", "9374c2"),
            ("C5 · A1 · La Ruta", "C6+ · cuando era pequeño")]
    tmp = path + ".tmp"
    with zipfile.ZipFile(path, "r") as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename.startswith("ppt/slides/") and item.filename.endswith(".xml"):
                t = data.decode("utf-8")
                for a, b in reps:
                    t = t.replace(a, b)
                data = t.encode("utf-8")
            zout.writestr(item, data)
    _os.replace(tmp, path)

def build(mode, out, include_teacher=True):
    E.MODE = mode
    E.new_presentation()
    _run_all(include_teacher=include_teacher)
    ndia_timing, nreveals = E.apply_all_timing()
    E.apply_hyperlinks()
    E.prs.save(out)
    _repaint(out)
    ndias = len(E.prs.slides._sldIdLst)
    print(f"opgeslagen: {out} · {ndias} dia's · {ndia_timing} met animaties · {nreveals} onthullingen · {len(E.MENU_LINKS)} hyperlinks")
    return out, ndias

if __name__ == "__main__":
    build("docente", OUT_DOCENTE, include_teacher=True)
    build("alumno", OUT_ALUMNO_PPTX, include_teacher=False)
    from pptx import Presentation
    d = Presentation(OUT_DOCENTE); a = Presentation(OUT_ALUMNO_PPTX)
    print("docente dia's:", len(d.slides._sldIdLst), "· alumno dia's:", len(a.slides._sldIdLst))
