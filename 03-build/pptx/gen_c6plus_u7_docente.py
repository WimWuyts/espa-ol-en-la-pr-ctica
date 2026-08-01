#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_c6plus_u7_docente.py — Interactieve PowerPoint C6+ · Unidad 7 «¡Opina y cuídate!»
======================================================================================
Zelfde engine/pijplijn als de golden sample (gen_u0_docente = de engine). Cursuskleur = PAARS.
Twee decks (.pptx): docente (oplossingen + notities) + alumno (F5, klik onthult).
Grammatica: imperativo afirmativo (tú) + pronombres · opinar y argumentar (indicativo + conectores).
Parada 7 = Costa Rica («pura vida») · fin de la ruta.
"""
import os
import gen_u0_docente as E
import lectura_data as _LD, escucha_data as _ED
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
OUT_DOCENTE = os.path.join(HERE, "C6plus_U7_docente.pptx")
OUT_ALUMNO_PPTX = os.path.join(HERE, "C6plus_U7_alumno.pptx")
TAB = "U7 · ¡OPINA Y CUÍDATE!"

def foot(s): footer(s, tab=TAB, page=pg())

# ============================================================ DIA 1 · TITLE
def s01_title():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(4.7), fill=G)
    rect(s, 0, Inches(4.7), EMU_W, Inches(0.09), fill=GD)
    text(s, Inches(0.6), Inches(0.35), Inches(3.4), Inches(3.6),
         [[("7", {"size": 260, "bold": True, "color": RGBColor(0x93, 0x74, 0xC2), "font": DISPLAY})]], anchor=MSO_ANCHOR.MIDDLE)
    chip(s, Inches(4.35), Inches(0.85), "LA RUTA · COSTA RICA 🇨🇷 · ¡PURA VIDA! 🌿", fill=WHITE, tcolor=GD, size=12)
    text(s, Inches(4.3), Inches(1.35), Inches(8.6), Inches(1.5), [[("¡Opina y cuídate!", {"size": 46, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(4.35), Inches(2.7), Inches(8.4), Inches(0.6),
         [[("Consejos: el imperativo (cuida, come, haz) · opinar y argumentar.", {"size": 15, "italic": True, "color": GT})]])
    text(s, Inches(4.35), Inches(3.35), Inches(8.4), Inches(0.9),
         [[("¿Qué haces para cuidarte y cuidar el planeta?", {"size": 22, "bold": True, "color": WHITE, "font": DISPLAY})],
          [("Wat doe jij om voor jezelf én de planeet te zorgen?", {"size": 13, "italic": True, "color": GT})]])
    text(s, Inches(0.6), Inches(4.95), Inches(8), Inches(0.4),
         [[("La gente de la ruta — parada 7: Costa Rica (¡la última!)", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    x = Inches(0.6)
    for nm, city in [("lucia","Sevilla 🇪🇸"),("diego","CDMX 🇲🇽"),("valen","Cartagena 🇨🇴"),
                     ("nina","Cusco 🇵🇪"),("tu","Tú · Flandes 🇧🇪"),("mochila","La mochila")]:
        avatar(s, nm, x, Inches(5.4), Inches(1.0))
        text(s, x - Inches(0.15), Inches(6.42), Inches(1.3), Inches(0.5),
             [[(nm.capitalize() if nm != "tu" else "Tú", {"size": 10.5, "bold": True, "color": INK})],
              [(city.split("·")[-1].strip() if nm != "tu" else "de reiziger = jij", {"size": 8.5, "color": MUT})]], align=PP_ALIGN.CENTER)
        x = x + Inches(2.05)
    foot(s)
    notes(s, "TEACHER · TITLE. U7 = de laatste unit (capstone). Kerngrammatica: imperativo afirmativo (tú) + pronombres · opinar y argumentar (creo que + indicativo · conectores). "
             "Parada 7 = Costa Rica («pura vida»). Kernvalstrikken: imperativo tú -a/-e + 8 irr (ten/ven/pon/haz/di/sal/sé/ve) · cuídate (accent) · creo que + INDICATIVO (géén subjuntivo) · want/omdat = porque, dus = por eso. "
             "Docentdeck = oplossing; leerlingdeck (.pptx, F5) = klik onthult. ¡Fin de la ruta!")

# ============================================================ DIA 2 · MENU
def s02_menu():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "MENÚ DE LA LECCIÓN", "El mapa de la Unidad 7",
               "Kies je route — klik een tegel. Alles oefent naar de Tarea «Mi cartel de opinión» toe.", num=7)
    tiles = [
        ("§1", "Salud y planeta", "el cuerpo · reciclar", G, 3),
        ("§2", "El imperativo", "cuida · come · haz", G, 4),
        ("§2b", "+ pronombre", "cuídate · hazlo", G, 11),
        ("§3", "Opinar", "creo que + indicativo", G, 6),
        ("§4", "Conectores", "porque · además · por eso", G, 7),
        ("★", "Lectura + escucha", "diez consejos", GD, 9),
        ("🌿", "Cultura", "Costa Rica · pura vida", GD, 17),
        ("📢", "Tarea · Cartel", "consejos + opinión", GD, 18),
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
    notes(s, "TEACHER · LESSON_MENU. Kern = §2 imperativo + §3 opinar. Kruisverwijzing: «oefen online — 12 juegos + 100+ oefeningen».")

# ============================================================ DIA 3 · VOCAB
def s03_vocab():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · VOCABULARIO", "La salud y el medio ambiente", "De woorden van gezondheid en milieu — observa. Herken ze, dan gebruik je ze.", num=1)
    legend_func(s, Inches(9.7), Inches(0.55))
    rows = [("la salud", "de gezondheid", "sano ↔ enfermo"), ("el ejercicio", "de beweging", "hacer deporte"),
            ("la dieta", "de voeding", "comer sano"), ("descansar", "rusten", "dormir · el estrés"),
            ("el medio ambiente", "het milieu", "el planeta"), ("reciclar", "recyclen", "la basura"),
            ("ahorrar", "besparen", "la energía · el agua"), ("proteger", "beschermen", "el árbol · el bosque")]
    x0, y0 = Inches(0.5), Inches(1.6); cw = Inches(6.1); rh = Inches(0.6)
    for i, (k, v, nl) in enumerate(rows):
        c = 0 if i < 4 else 1; r = i % 4
        x = x0 + c * (cw + Inches(0.15)); y = y0 + r * (rh + Inches(0.12))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(2.4), rh, [[(k, {"size": 13, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(2.5), y, Inches(2.1), rh, [[(v, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(4.5), y, Inches(1.5), rh, [[(nl, {"size": 9, "italic": True, "color": MUT})]], anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(4.75), Inches(12.3), Inches(0.5),
         [[("Contrarios: ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("sano ↔ enfermo · limpio ↔ sucio · ahorrar ↔ gastar · proteger ↔ contaminar.", {"size": 13, "color": INK})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.35), Inches(12.3), Inches(0.95),
             [[("Salud: ", {"bold": True, "color": GD}), ("el cuerpo, sano, el deporte, la dieta, dormir, cuidarse, el estrés.", {"color": GD})],
              [("Medio ambiente: ", {"bold": True, "color": GD}), ("el planeta, reciclar, la basura, ahorrar, la energía, proteger, el árbol.", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCABULARY. Laat de woorden raden. Online: memoria de la salud + el planeta.")

# ============================================================ DIA 4 · GRAMMAR imperativo (color)
def s04_imperf():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · GRAMÁTICA VISUAL", "El imperativo (tú) — dar consejos", "-ar → -a · -er/-ir → -e. Voor advies en instructies.", num=2)
    legend_func(s, Inches(9.7), Inches(0.55))
    seg = [("Recicla ", F_VERB), ("el papel ", F_OBJ), ("porque ", F_TIME), ("es importante", F_SUBJ)]
    runs = [[(t, {"size": 21, "bold": True, "color": c, "font": DISPLAY}) for t, c in seg]]
    card(s, Inches(0.5), Inches(1.7), Inches(12.3), Inches(1.2), fill=GT, line=None)
    text(s, Inches(0.8), Inches(1.7), Inches(11.7), Inches(1.2), runs, anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(3.15), Inches(12), Inches(0.4), [[("Las formas (+ 8 irregulares)", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    frame = [("-ar → -a", "cuida / recicla"), ("-er/-ir → -e", "come / vive"), ("o→ue / e→ie", "duerme / cierra"),
             ("hacer → haz", "haz deporte"), ("ir → ve · ser → sé", "ve / sé"), ("ten·ven·pon·di·sal", "irregulares")]
    x0, y0 = Inches(0.5), Inches(3.6); cw = Inches(4.0); rh = Inches(0.62)
    for i, (a, b) in enumerate(frame):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.12))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(2.1), rh, [[(a, {"size": 11, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(2.25), y, cw - Inches(2.4), rh, [[(b, {"size": 10.5, "color": F_VERB, "bold": True})]], anchor=MSO_ANCHOR.MIDDLE)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.75), Inches(12.3), Inches(0.6),
             [[("Regla: ", {"bold": True, "color": GD}), ("-ar → -a · -er/-ir → -e. 8 irregulares: ten·ven·pon·haz·di·sal·sé·ve. Advies/instructie.", {"color": GD})]],
             trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR imperativo. Toon raíz + uitgang. Online: completa el imperativo (cloze) + imperativo Tetris.")

# ============================================================ DIA 5 · QUIZ imperativo (reveal)
def s05_imperf_quiz():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · QUIZ", "¿Qué forma del imperativo?", "Klik een zin → de juiste vorm.", num=2)
    items = [("___ (comer) más verdura.", "Come"), ("___ (beber) agua.", "Bebe"),
             ("___ (hacer) deporte.", "Haz ⭐"), ("___ (reciclar) el papel.", "Recicla"),
             ("___ (ir) al médico.", "Ve ⭐"), ("___ (ser) responsable.", "Sé ⭐")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.78)
    for i, (q, a) in enumerate(items):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(4.0), rh, [[(q, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.2), y, cw - Inches(4.3), rh, [[("→ " + a, {"size": 12.5, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Truc: ", {"bold": True, "color": RED}), ("-ar → -a · -er/-ir → -e · 8 irregulares (haz, ve, sé, di, ten…).", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ imperativo (retrieval). Klas roept vóór de klik. Online: cloze el imperativo.")

# ============================================================ DIA 6 · GRAMMAR opinar (reveal)
def s06_contraste():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · GRAMÁTICA", "Opinar y argumentar", "Klik → wat volgt. creo que + indicativo (géén subjuntivo).", num=3)
    items = [("Creo que … importante", "es (indicativo)"), ("Pienso que … reciclar", "debemos (indicativo)"),
             ("En mi …, hay basura", "opinión"), ("(No) estoy de … contigo", "acuerdo"),
             ("Me … que tienes razón", "parece"), ("Tienes …", "razón")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.78)
    for i, (q, a) in enumerate(items):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(4.0), rh, [[(q, {"size": 11.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.2), y, cw - Inches(4.3), rh, [[("→ " + a, {"size": 12, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Regla: ", {"bold": True, "color": GD}), ("Creo que / Pienso que / En mi opinión + INDICATIVO (es, debemos). Reageren: (no) estoy de acuerdo · tienes razón.", {"color": GD})]], trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR opinar (P3-kern). 🔴 Géén subjuntivo: creo que ES. Coro vóór de klik. Online: opinar (cloze).")

# ============================================================ DIA 7 · GRAMMAR conectores (color)
def s07_comparativos():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · GRAMÁTICA VISUAL", "Conectores — argumentar", "porque (reden) · además (toevoeging) · por eso (gevolg) · sin embargo (tegenstelling).", num=4)
    legend_func(s, Inches(9.7), Inches(0.55))
    card(s, Inches(0.5), Inches(1.7), Inches(12.3), Inches(1.1), fill=GT, line=None)
    text(s, Inches(0.8), Inches(1.7), Inches(11.7), Inches(1.1),
         [[("Reciclo ", {"size": 16, "color": INK}), ("porque ", {"size": 18, "bold": True, "color": F_TIME}),
           ("es sano. ", {"size": 16, "color": INK}), ("Además, ", {"size": 18, "bold": True, "color": F_OBJ}), ("ahorra dinero.", {"size": 16, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
    frame = [("porque", "want/omdat (reden)"), ("además", "bovendien"), ("por eso", "daarom (gevolg)"),
             ("sin embargo", "echter"), ("por un lado", "enerzijds"), ("por otro lado", "anderzijds")]
    x0, y0 = Inches(0.5), Inches(3.15); cw = Inches(4.0); rh = Inches(0.62)
    for i, (a, b) in enumerate(frame):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.12))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(2.0), rh, [[(a, {"size": 11.5, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(2.15), y, cw - Inches(2.3), rh, [[(b, {"size": 10.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.75),
             [[("Regla: ", {"bold": True, "color": GD}), ("porque = reden · además = toevoeging · por eso = gevolg. 🔴 want/omdat = porque · dus = por eso (niet «luego»). Komma na además/por eso/sin embargo.", {"color": GD})]],
             trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR conectores. Toon reden/toevoeging/gevolg. Online: ¿porque, además o por eso? (cloze).")

# ============================================================ DIA 8 · QUIZ a favor/en contra (reveal)
def s08_comp_quiz():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · QUIZ", "¿A favor o en contra? (del coche)", "Klik een argument → a favor / en contra.", num=4)
    items = [("Es rápido.", "a favor"), ("Contamina el aire.", "en contra"),
             ("Es cómodo cuando llueve.", "a favor"), ("Hace mucho ruido.", "en contra"),
             ("Da libertad para viajar.", "a favor"), ("Gasta gasolina.", "en contra")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.78)
    for i, (q, a) in enumerate(items):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(3.9), rh, [[(q, {"size": 11.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.1), y, cw - Inches(4.2), rh, [[("→ " + a, {"size": 12, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Debate: ", {"bold": True, "color": GD}), ("un argumento a favor + uno en contra + tu opinión (creo que… porque…).", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ a favor/en contra (retrieval). Online: ¿a favor o en contra? (classify).")

# ============================================================ DIA 9 · READING
def s09_reading():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§5 · LEER · COMPRENSIÓN", "«Diez consejos para el planeta»", "Lees. Klik een vraag → het antwoord verschijnt.", num=5)
    card(s, Inches(0.5), Inches(1.65), Inches(5.6), Inches(3.9), fill=GT, line=G, lw=1.4)
    avatar(s, "valen", Inches(0.85), Inches(1.95), Inches(1.0))
    text(s, Inches(2.05), Inches(1.98), Inches(3.9), Inches(1.5),
         [[("«Creo que todos podemos ayudar. Recicla el papel. Ahorra agua: cierra el grifo. Usa la bici, porque el coche contamina. Come más verdura. No tires basura al suelo. ¡Por eso, cuida el planeta hoy!»", {"size": 11, "italic": True, "color": INK})]], line=1.16)
    avatar(s, "tu", Inches(0.85), Inches(3.65), Inches(1.0))
    text(s, Inches(2.05), Inches(3.68), Inches(3.9), Inches(1.5),
         [[("«Estoy de acuerdo. Yo voy en bici porque es sano y no contamina. Además, ahorro dinero. Sin embargo, en mi pueblo no hay carril bici. ¡Pura vida!»", {"size": 11, "italic": True, "color": INK})]], line=1.16)
    qa = [("¿Qué transporte recomienda?", "la bici"), ("¿Por qué usar la bici?", "el coche contamina"),
          ("¿Está de acuerdo el lector?", "Sí"), ("¿Qué falta en su pueblo?", "un carril bici")]
    x = Inches(6.4); y = Inches(1.7)
    for q, a in qa:
        card(s, x, y, Inches(6.4), Inches(0.85), fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y + Inches(0.06), Inches(6.1), Inches(0.4), [[(q, {"size": 12.5, "bold": True, "color": GD})]])
        rev = text(s, x + Inches(0.15), y + Inches(0.44), Inches(6.1), Inches(0.35), [[("→ " + a, {"size": 12, "color": INK})]])
        register_reveal(s, rev); y = y + Inches(0.98)
    btn = noodroute(s)
    exercise_solucion(s, Inches(6.4), Inches(5.65), Inches(6.4), Inches(0.6),
             [[("🎯 Leesdoel: ", {"bold": True, "color": GD}), ("scannen naar de imperativos (recicla, usa…) + una opinión.", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · READING (lezen→schrijven). Eerst globaal, dan scannen. Daarna: eigen cartel de consejos.")

# ============================================================ DIA 10 · LISTENING
def s10_listening():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · ESCUCHAR · INTERACCIÓN", "¿Qué opinas del medio ambiente?", "Volg het gesprek. Klik un dato → de info. (audio + script op de web)", num=2)
    pasos = [("🔊 ¿De qué hablan?", "del medio ambiente"), ("🔊 ¿Qué opina Valen?", "hay que reciclar"),
             ("🔊 ¿Qué consejo dan?", "usa la bici"), ("🔊 ¿Están de acuerdo?", "Sí, los dos")]
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
               ("«Creo que debemos reciclar más. Usa la bici porque el coche contamina. Estoy de acuerdo.» ", {"color": GD})],
              [("Daarna: A geeft zijn mening, B reageert (de acuerdo / no).", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · LISTENING (luisteren→spreken). Lees voor (of TTS); klas noteert. Online: ¿qué opinas del medio ambiente? (audio).")

# ============================================================ DIA 11 · GRAMMAR pronombres enclíticos (reveal)
def s11_relativo():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2b · GRAMÁTICA", "El imperativo + pronombre", "Klik een cue → de vorm. Het pronomen plakt vast (let op het accent).", num=2)
    items = [("cuida + te", "cuídate"), ("haz + lo", "hazlo"),
             ("recicla + lo", "recíclalo"), ("bebe + la", "bébela"),
             ("di + me", "dime"), ("protege + lo", "protégelo"), ("di + me + lo", "dímelo"), ("pon + lo", "ponlo")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.72)
    for i, (q, a) in enumerate(items):
        c = i // 4; r = i % 4; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.14))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(3.0), rh, [[(q, {"size": 12, "color": MUT})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(3.2), y, cw - Inches(3.3), rh, [[("→ " + a, {"size": 13, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.85), Inches(12.3), Inches(0.85),
             [[("Enclíticos: ", {"bold": True, "color": GD}), ("het pronomen plakt achteraan. Langer woord → accent: cuídate, recíclalo, dímelo.", {"color": GD})],
              [("Korte vormen géén accent: hazlo, dime, ponlo, dilo.", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR pronombres enclíticos. Accent bij langere vormen. Online: añade el pronombre (drill).")

# ============================================================ DIA 12 · QUIZ mezcla (reveal)
def s12_mezcla_imp():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2–§4 · QUIZ", "Imperativo + opinar + conectores", "Klik → het antwoord.", num=2)
    items = [("hacer → imperativo (tú)", "haz"), ("cuida + te", "cuídate"),
             ("Creo que … importante", "es (indicativo)"), ("«ik ben het eens»", "estoy de acuerdo"),
             ("«want / omdat»", "porque"), ("«daarom»", "por eso")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.78)
    for i, (q, a) in enumerate(items):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(3.9), rh, [[(q, {"size": 11.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.1), y, cw - Inches(4.2), rh, [[("→ " + a, {"size": 12, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Alles komt terug: ", {"bold": True, "color": G}), ("imperativo (+ pronombre) · opinar (creo que + indicativo) · conectores.", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ mezcla (retrieval). Door elkaar. Online: cloze + imperativo Tetris.")

# ============================================================ DIA 13 · SPEAKING
def s13_speaking():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · SPEAKING · INTERACCIÓN", "Da consejos y tu opinión", "Speel de scène met de frames. Steun bouwt af: kaarten → beginwoorden → uit het hoofd.", num=3)
    avatar(s, "tu", Inches(11.4), Inches(1.7), Inches(1.3))
    labels = ["Un consejo", "Otro consejo", "Tu opinión", "Un argumento", "Reacciona", "Concluye"]
    frames = ["Come sano…", "Recicla…", "Creo que…", "…porque…", "Estoy de acuerdo…", "Por eso…"]
    x0, y0 = Inches(0.5), Inches(1.8); cw = Inches(3.4); rh = Inches(0.8)
    for i, (lab, fr) in enumerate(zip(labels, frames)):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=G, lw=1.2, shadow=False)
        text(s, x + Inches(0.15), y + Inches(0.05), cw - Inches(0.3), Inches(0.32), [[(lab, {"size": 10, "color": MUT})]])
        text(s, x + Inches(0.15), y + Inches(0.36), cw - Inches(0.3), Inches(0.4), [[(fr, {"size": 11.5, "bold": True, "color": GD, "font": DISPLAY})]])
    chip(s, Inches(0.5), Inches(4.65), "🎙️ Grábate online · «Mensaje de voz: tus consejos / tu opinión»", fill=GT, tcolor=GD, size=11)
    text(s, Inches(0.5), Inches(5.05), Inches(10.5), Inches(0.9),
         [[("Ronda 1: ", {"size": 12, "bold": True, "color": GD}), ("met de kaarten. ", {"size": 12, "color": INK}),
           ("Ronda 2: ", {"size": 12, "bold": True, "color": GD}), ("beginwoorden. ", {"size": 12, "color": INK}),
           ("Ronda 3: ", {"size": 12, "bold": True, "color": GD}), ("uit het hoofd. ", {"size": 12, "color": INK}),
           ("Ronda 4: ", {"size": 12, "bold": True, "color": GD}), ("grábate.", {"size": 12, "color": INK})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.6), Inches(12.3), Inches(0.65),
             [[("Modelo: ", {"bold": True, "color": GD}), ("«Come sano y haz deporte. Recicla el papel. Creo que debemos cuidar el planeta porque es de todos. Además, es fácil. Por eso, ¡empieza hoy!»", {"color": GD})]],
             trigger=btn, title_doc="MODELO · docent")
    foot(s)
    notes(s, "TEACHER · SPEAKING (interactie). Rondes met afbouwende steun. Online: recorder (tus consejos · tu opinión).")

# ============================================================ DIA 14 · WRITING
def s14_writing():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "WRITING · PRODUCCIÓN", "Mi cartel de opinión", "Schrijf een opinie-affiche. Klik → een modeltekst verschijnt.", num=5)
    card(s, Inches(0.5), Inches(1.7), Inches(6.0), Inches(3.9), fill=WHITE, line=LINE, lw=1.2)
    text(s, Inches(0.7), Inches(1.85), Inches(5.6), Inches(0.4), [[("✍️ Escribe tu cartel:", {"size": 12, "bold": True, "color": GD})]])
    for i in range(6):
        rect(s, Inches(0.7), Inches(2.4) + i * Inches(0.5), Inches(5.6), Inches(0.01), fill=LINE)
    chk = ["un tema (salud o medio ambiente)", "4 consejos (imperativo)", "un pronombre (cuídate, hazlo)", "una opinión (creo que + indicativo)", "dos conectores (porque, además)", "una objeción (sin embargo…)"]
    x = Inches(6.9); y = Inches(1.7)
    text(s, x, y, Inches(6), Inches(0.4), [[("Checklist:", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    for i, c in enumerate(chk):
        text(s, x, y + Inches(0.5) + i * Inches(0.45), Inches(6), Inches(0.4), [[("☐  " + c, {"size": 13, "color": INK})]])
    rev = card(s, x, Inches(4.35), Inches(6.0), Inches(1.25), fill=GT, line=G, lw=1.2)
    text(s, x + Inches(0.15), Inches(4.4), Inches(5.7), Inches(1.2),
         [[("Modelo: ", {"size": 12, "bold": True, "color": GD}),
           ("«¡Cuida el planeta! Recicla el papel. Ahorra agua. Usa la bici. Creo que es urgente porque contaminamos mucho. Además, es fácil. Por eso, ¡empieza hoy!»", {"size": 11, "italic": True, "color": INK})]], line=1.13)
    register_reveal(s, rev)
    noodroute(s); foot(s)
    notes(s, "TEACHER · WRITING (lezen→schrijven). Checklist = zichtbare steun; onthul het model pas na het schrijven. Nakijkfocus: imperativo, pronombre, opinión (indicativo), conectores. Voedt de Tarea.")

# ============================================================ DIA 15 · VOCAB salud/planeta (reveal)
def s15_antes():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · VOCABULARIO", "Salud y planeta", "Klik een kaart → la respuesta. Bouw je woordnetwerk.", num=1)
    data = [("sano", "gezond"), ("enfermo", "ziek"), ("el consejo", "de tip"), ("el estrés", "de stress"),
            ("reciclar", "recyclen"), ("la basura", "het afval"), ("ahorrar", "besparen"), ("proteger", "beschermen"),
            ("contaminar", "vervuilen"), ("el planeta", "de planeet"), ("el árbol", "de boom"), ("la energía", "de energie")]
    x0, y0 = Inches(0.5), Inches(1.7); cw = Inches(3.0); rh = Inches(0.7)
    for i, (es, nl) in enumerate(data):
        c = i % 4; r = i // 4; x = x0 + c * (cw + Inches(0.1)); y = y0 + r * (rh + Inches(0.14))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.12), y, Inches(1.8), rh, [[(es, {"size": 11, "bold": True, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(1.75), y, cw - Inches(1.85), rh, [[("→ " + nl, {"size": 10.5, "color": G})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.9),
             [[("Contrarios: ", {"bold": True, "color": GD}), ("sano ↔ enfermo · limpio ↔ sucio · ahorrar ↔ gastar · proteger ↔ contaminar.", {"color": GD})],
              [("Colocaciones: comer sano · hacer deporte · beber agua · ahorrar energía.", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCAB salud/planeta. Klik onthult. Online: memoria de la salud + el planeta + señala.")

# ============================================================ DIA 16 · TALLER
def s16_taller():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "TALLER DE LENGUA", "El acento enclítico + conectores", "Klik een item → correcte vorm. Gereedschap voor spelling en argumentatie.", num=1)
    text(s, Inches(0.5), Inches(1.5), Inches(6), Inches(0.35), [[("A · ortografía: el acento en los enclíticos", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    fixes = [("cuidate →", "cuídate"), ("comelo →", "cómelo"), ("protegelo →", "protégelo"), ("dimelo →", "dímelo")]
    y = Inches(1.95)
    for q, a in fixes:
        card(s, Inches(0.5), y, Inches(6.0), Inches(0.6), fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, Inches(0.62), y, Inches(3.0), Inches(0.6), [[(q, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, Inches(3.7), y, Inches(2.7), Inches(0.6), [[("→ " + a, {"size": 12, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y = y + Inches(0.72)
    text(s, Inches(6.9), Inches(1.5), Inches(6), Inches(0.35), [[("B · conectores de argumentación", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    conn = [("porque", "want/omdat"), ("además", "bovendien"), ("por eso", "daarom"), ("sin embargo", "echter")]
    y = Inches(1.95)
    for q, a in conn:
        card(s, Inches(6.9), y, Inches(5.9), Inches(0.6), fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, Inches(7.02), y, Inches(3.0), Inches(0.6), [[(q, {"size": 12, "bold": True, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, Inches(10.1), y, Inches(2.6), Inches(0.6), [[("→ " + a, {"size": 11, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y = y + Inches(0.72)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.85),
             [[("A: ", {"bold": True, "color": GD}), ("langere vormen krijgen accent: cuídate, cómelo, protégelo, dímelo. Korte: hazlo, dime.", {"color": GD})],
              [("B: porque (reden) · además (toevoeging) · por eso (gevolg) · sin embargo (tegenstelling).", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · TALLER. Accent enclíticos + argumentatie-connectoren. Online: drills in de hub.")

# ============================================================ DIA 17 · CULTURE
def s17_cultura():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "CULTURA · PARADA 7: COSTA RICA", "Costa Rica y la «pura vida»", "Klik een kaart → het weetje. Sin ejército, ecoturismo y biodiversidad.", num=1)
    cards = [("🕊️ Sin ejército", "In 1948 schafte Costa Rica zijn leger af. Het geld gaat naar onderwijs en gezondheidszorg. Een uniek voorbeeld van vrede.", "un ejemplo de paz"),
             ("🌿 Ecoturismo", "Meer dan 25 % van het land is beschermde natuur: regenwoud, vulkanen, stranden. Costa Rica huisvest ~5 % van alle soorten op aarde.", "biodiversidad"),
             ("🐒 ¡Pura vida!", "«Pura vida» hoor je overal: als groet, bedankje of «alles oké». Het vat de optimistische levensstijl van de «ticos» samen.", "una filosofía de vida")]
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
             [[("Actividad: ", {"bold": True, "color": GD}), ("¿te parece bien un país sin ejército? Geef je mening (creo que… porque…).", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · CULTURE (LPD 5). Onthul per kaart. Bruggetje: La Ruta parada 7 = Costa Rica (★, fin de la ruta). Online: klik op Costa Rica op de kaart.")

# ============================================================ DIA 18 · FINAL_MISSION
def s18_tarea():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(1.35), fill=GD)
    text(s, Inches(0.5), Inches(0.18), Inches(9), Inches(1.0),
         [[("📢 Tarea final · Mi cartel de opinión", {"size": 26, "bold": True, "color": WHITE, "font": DISPLAY})],
          [("Crea un cartel con consejos (imperativo) y tu opinión argumentada.", {"size": 13, "italic": True, "color": GT})]])
    avatar(s, "mochila", Inches(11.6), Inches(0.2), Inches(1.0))
    pasos = [("1", "Elige un tema", "salud o medio ambiente"),
             ("2", "Da 4 consejos", "«Recicla el papel», «Cuídate» (imperativo)"),
             ("3", "Escribe tu opinión", "«Creo que… porque… Además… Por eso…»"),
             ("4", "Reacciona a una objeción", "«Sin embargo, algunos dicen que… pero…»"),
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
    crit = ["imperativo", "un pronombre", "una opinión", "dos conectores"]
    x = Inches(0.5)
    for c in crit:
        chip(s, x, Inches(5.45), "☐ " + c, fill=GT, tcolor=GD, size=10, w=Inches(3.05)); x = x + Inches(3.15)
    text(s, Inches(0.5), Inches(6.05), Inches(12), Inches(0.4),
         [[("🎯 ", {"size": 12}), ("Afzender jij · ontvanger de klas · doel overtuigen & adviseren · situatie de expositie «Pura Vida» · resultaat: cartel + presentación oral.", {"size": 11.5, "italic": True, "color": MUT})]])
    foot(s)
    notes(s, "TEACHER · FINAL_MISSION (communicatieve eindtaak · P3-capstone). Beoordeel met de rúbrica; opname op de web.")

# ============================================================ DIA 19 · MEZCLA
def s19_mezcla():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "QUIZ · LA MEZCLA", "Ophaal door elkaar", "Gemengde ophaal van de hele unit. Klik → het antwoord. (retrieval)", num=1)
    items = [("comer → imperativo (tú)", "come"), ("hacer → imperativo (tú)", "haz"),
             ("cuida + te", "cuídate"), ("Creo que … importante", "es"),
             ("«want / omdat»", "porque"), ("«bovendien»", "además"),
             ("«ik ben het eens»", "estoy de acuerdo"), ("«daarom»", "por eso")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.62)
    for i, (q, a) in enumerate(items):
        c = i // 4; r = i % 4; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.16))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(4.0), rh, [[(q, {"size": 11.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.15), y, cw - Inches(4.3), rh, [[("→ " + a, {"size": 12, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.05), Inches(12.3), Inches(0.55),
             [[("Alles komt terug: ", {"bold": True, "color": GD}), ("imperativo (+ pronombre) · opinar (creo que + indicativo) · conectores.", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ mezcla (retrieval vóór herlezen). Exit-ticket. Zwakke punten → terug via menu.")

# ============================================================ DIA 20 · REPASO
def s20_repaso():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "REPASO · LO ESENCIAL", "Lo esencial de un vistazo", "De volledige herhaling (12 spellen, drills) staat online. Hier: de kern + semáforo.", num=1)
    ess = ["Imperativo (tú): -ar → -a (cuida) · -er/-ir → -e (come, vive).",
           "8 irregulares: ten · ven · pon · haz · di · sal · sé · ve.",
           "+ pronombre: cuídate · hazlo · dímelo (let op het accent).",
           "Opinar (indicativo): creo que / pienso que / en mi opinión + es/debemos… (géén subjuntivo).",
           "Conectores: porque (reden) · además (toevoeging) · por eso (gevolg) · sin embargo (tegenstelling).",
           "🔴 Trampas: haz (niet «hace») · accent cuídate · want/omdat = porque · dus = por eso."]
    card(s, Inches(0.5), Inches(1.6), Inches(12.3), Inches(2.9), fill=CREMA, line=None)
    y = Inches(1.78)
    for e in ess:
        text(s, Inches(0.8), y, Inches(11.8), Inches(0.45), [[("• ", {"size": 13, "bold": True, "color": GD}), (e, {"size": 12, "color": INK})]])
        y = y + Inches(0.44)
    text(s, Inches(0.5), Inches(4.65), Inches(12), Inches(0.35), [[("Semáforo — ¿cómo lo llevas?", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    can = ["advies geven (come, haz, cuídate)", "een pronomen aanplakken (cuídate, hazlo)", "mijn mening geven (creo que + indicativo)", "argumenteren (porque/además/por eso)", "praten over salud & medio ambiente"]
    y = Inches(5.05)
    for c in can:
        text(s, Inches(0.8), y, Inches(7.0), Inches(0.4), [[(c, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        for j, (em, col) in enumerate([("🔴", RED), ("🟠", AMBER), ("🟢", G)]):
            chip(s, Inches(8.0) + j * Inches(1.5), y + Inches(0.03), em + " ", fill=WHITE, tcolor=col, size=12, w=Inches(1.3))
        y = y + Inches(0.36)
    foot(s)
    notes(s, "TEACHER · FEEDBACK/REPASO. Semáforo = zelfevaluatie. Repaso-drills online. 🏁 ¡Fin de la ruta! España → México → Colombia → Argentina → Perú → Costa Rica. Presente, pasado (perfecto/indefinido/imperfecto), consejos y opinión.")

# ============================================================ DIA 21 · TEACHER
def s21_teacher():
    s = slide(); bg(s, GD)
    text(s, Inches(0.6), Inches(0.4), Inches(12), Inches(0.8), [[("TEACHER_NOTES · U7 «¡Opina y cuídate!»", {"size": 24, "bold": True, "color": WHITE, "font": DISPLAY})]])
    blocks = [("Timing (50 min)", "Menu 2' · salud/planeta 6' · imperativo 12' · + pronombre 5' · opinar 8' · conectores 7' · Tarea-briefing 5' · cierre de la ruta 5'."),
              ("Kernvalstrikken", "imperativo tú = -a/-e + 8 irr (haz, ve, sé, di, ten, ven, pon, sal) · enclítico + accent (cuídate, recíclalo) · creo que + INDICATIVO (géén subjuntivo: es, niet «sea») · want/omdat = porque · dus = por eso (niet «luego»)."),
              ("Buiten scope (hard)", "GÉÉN imperativo negativo/usted (= subjuntivo), géén futuro simple / condicional / subjuntivo. Enkel imperativo afirmativo (tú) + opinar met indicativo."),
              ("Digitaal", "12 spellen + flip cards + gramática interactiva (imperativo · opinar · conectores) + recorder (tus consejos · tu opinión) + Lectura («Diez consejos») + klikbare kaart (Costa Rica ★) op de página digital. QR's → juiste anker."),
              ("Evaluatie & LPD", "Tarea «Mi cartel de opinión» met rúbrica (imperativo · pronombre · opinión · conectores). LPD (III-Spa-d): salud/medio ambiente 7 · imperativo/argumentatie 8 · advies 3 · interactie 4 · lezen 1·2·5 · cultuur 5. P3-capstone: mening → volwaardig opiniestuk. 🏁 Fin de la ruta.")]
    y = Inches(1.4)
    for t, b in blocks:
        card(s, Inches(0.5), y, Inches(12.3), Inches(1.0), fill=RGBColor(0x47, 0x30, 0x69), line=None)
        text(s, Inches(0.75), y + Inches(0.08), Inches(11.8), Inches(0.4), [[(t, {"size": 14, "bold": True, "color": WHITE, "font": DISPLAY})]])
        text(s, Inches(0.75), y + Inches(0.48), Inches(11.8), Inches(0.5), [[(b, {"size": 11, "color": GT})]], line=1.1)
        y = y + Inches(1.12)
    footer(s, tab=TAB, page=pg())
    notes(s, "Alleen in het docentdeck. Volledige LPD-dekking en didactische route staan in het cursusdossier (cocktail + outline). Laatste unit → versie 1 klaar.")

# ============================================================ RUN + BUILD
def _run_all(include_teacher=True):
    s01_title(); s02_menu(); s03_vocab(); s04_imperf(); s05_imperf_quiz(); s06_contraste(); s07_comparativos()
    s08_comp_quiz(); s09_reading(); s10_listening(); s11_relativo(); s12_mezcla_imp(); s13_speaking(); s14_writing()
    s15_antes(); s16_taller(); s17_cultura()
    # Lectura en Escucha uit de gedeelde bron — zelfde inhoud als print en hub.
    E.s_lectura(_LD.C6P_U7); E.s_escucha(_ED.C6P_U7)
    s18_tarea(); s19_mezcla(); s20_repaso()
    if include_teacher:
        s21_teacher()

def _repaint(path):
    import zipfile, os as _os
    reps = [("1E9E74", "7C56A9"), ("1e9e74", "7c56a9"), ("2EB085", "9374C2"), ("2eb085", "9374c2"),
            ("C5 · A1 · La Ruta", "C6+ · ¡opina y cuídate!")]
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
