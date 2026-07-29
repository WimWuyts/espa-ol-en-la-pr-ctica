#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_c6plus_u2_docente.py — Interactieve PowerPoint C6+ · Unidad 2 «Aquí vivo»
=============================================================================
Zelfde engine/pijplijn als de golden sample (gen_u0_docente = de engine). Enkel de SLIDES
zijn C6+·U2-specifiek. Cursuskleur = PAARS. Twee decks (beide .pptx):
  · C6plus_U2_docente.pptx — vrije navigatie, oplossingen + didactiek in notities.
  · C6plus_U2_alumno.pptx  — gewone diavoorstelling, antwoorden bij klik (F5).
Grammatica: hay vs estar + preposiciones · estar + gerundio · OD-pronomina lo/la/los/las.
Spaans-eerst + NL-steun. ≥20 dia's. Dekt de vier vaardigheden.
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
E.F_OBJ  = RGBColor(0xB4, 0x30, 0x9A)   # magenta (voorwerp)
E.F_PLAC = RGBColor(0x64, 0x74, 0x8B)   # leisteenblauw (plaats)
F_OBJ, F_PLAC = E.F_OBJ, E.F_PLAC

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DOCENTE = os.path.join(HERE, "C6plus_U2_docente.pptx")
OUT_ALUMNO_PPTX = os.path.join(HERE, "C6plus_U2_alumno.pptx")
TAB = "U2 · AQUÍ VIVO"

def foot(s): footer(s, tab=TAB, page=pg())

# ============================================================ DIA 1 · TITLE
def s01_title():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(4.7), fill=G)
    rect(s, 0, Inches(4.7), EMU_W, Inches(0.09), fill=GD)
    text(s, Inches(0.6), Inches(0.35), Inches(3.4), Inches(3.6),
         [[("2", {"size": 260, "bold": True, "color": RGBColor(0x93, 0x74, 0xC2), "font": DISPLAY})]],
         anchor=MSO_ANCHOR.MIDDLE)
    chip(s, Inches(4.35), Inches(0.85), "LA RUTA · CARTAGENA 🇨🇴 · AQUÍ VIVO 🏠", fill=WHITE, tcolor=GD, size=12)
    text(s, Inches(4.3), Inches(1.35), Inches(8.6), Inches(1.5),
         [[("Aquí vivo", {"size": 62, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(4.35), Inches(2.7), Inches(8.4), Inches(0.6),
         [[("Tu casa y tu barrio: hay/estar + preposiciones · estar + gerundio · lo/la/los/las.", {"size": 15, "italic": True, "color": GT})]])
    text(s, Inches(4.35), Inches(3.35), Inches(8.4), Inches(0.9),
         [[("¿Dónde vives tú?", {"size": 24, "bold": True, "color": WHITE, "font": DISPLAY})],
          [("Waar woon jij?", {"size": 13, "italic": True, "color": GT})]])
    text(s, Inches(0.6), Inches(4.95), Inches(6), Inches(0.4),
         [[("La gente de la ruta — parada 2: Cartagena (Valen)", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
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
    notes(s, "TEACHER · TITLE. U2 = la casa y el barrio. Kerngrammatica: hay vs estar + preposiciones de lugar, estar + gerundio, "
             "OD-pronomina lo/la/los/las. Parada 2 = Cartagena (Valen). Kernvalstrikken: hay (onbepaald) ≠ está (bepaald) · de+el=del · "
             "lo/la vóór het werkwoord + concordancia. Docentdeck = oplossing; leerlingdeck (.pptx, F5) = klik onthult.")

# ============================================================ DIA 2 · LESSON_MENU
def s02_menu():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "MENÚ DE LA LECCIÓN", "El mapa de la Unidad 2",
               "Kies je route — klik een tegel. Alles oefent naar de Tarea «Mapa de mi barrio» toe.", num=2)
    tiles = [
        ("§1", "La casa", "habitaciones · muebles", G, 3),
        ("§2", "Hay / estar", "+ preposiciones", G, 4),
        ("§3", "Gerundio", "estar + -ando/-iendo", G, 7),
        ("§4", "Lo / la", "los/las (OD)", G, 11),
        ("§5", "El barrio", "cómo llegar", G, 10),
        ("★", "Lectura + escucha", "mi barrio", GD, 9),
        ("🌺", "Cultura", "la vivienda hispana", GD, 17),
        ("🗺️", "Tarea · Mi barrio", "plano + ruta", GD, 18),
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
    notes(s, "TEACHER · LESSON_MENU. Elke tegel = hyperlink; ⌂ Menú terug op elke oefendia. Richttijd 50 min. "
             "Kern = §2 hay/estar + §3 gerundio + §4 lo/la. Kruisverwijzing: «oefen online — 12 juegos + 100+ oefeningen».")

# ============================================================ DIA 3 · VOCAB — la casa
def s03_vocab():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · VOCABULARIO", "La casa — habitaciones y muebles", "De woorden van je huis — observa. Herken ze, dan gebruik je ze.", num=1)
    legend_func(s, Inches(9.7), Inches(0.55))
    rows = [("el dormitorio", "de slaapkamer", "la cama, el armario"), ("el salón", "de woonkamer", "el sofá"),
            ("la cocina", "de keuken", "la nevera, la mesa"), ("el baño", "de badkamer", "el espejo"),
            ("la cama", "het bed", "dormir"), ("el sofá", "de zetel", "el salón"),
            ("el armario", "de kast", "la ropa"), ("la nevera", "de koelkast", "la cocina")]
    x0, y0 = Inches(0.5), Inches(1.6); cw = Inches(6.1); rh = Inches(0.6)
    for i, (k, v, nl) in enumerate(rows):
        c = 0 if i < 4 else 1; r = i % 4
        x = x0 + c * (cw + Inches(0.15)); y = y0 + r * (rh + Inches(0.12))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(2.4), rh, [[(k, {"size": 13, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(2.5), y, Inches(2.1), rh, [[(v, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(4.5), y, Inches(1.5), rh, [[(nl, {"size": 9, "italic": True, "color": MUT})]], anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(4.75), Inches(12.3), Inches(0.5),
         [[("¡Ojo! el/la: ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("el dormitorio, el salón, el sofá (m) · la cocina, la cama, la nevera (v)", {"size": 13, "color": INK})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.35), Inches(12.3), Inches(0.95),
             [[("En cada habitación hay muebles: ", {"bold": True, "color": GD}), ("en el dormitorio hay una cama; en el salón, un sofá.", {"color": GD})],
              [("🔴 el sofá (m ondanks -á) · la mano, la foto (v ondanks -o).", {"color": RED})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCABULARY. Laat de casa-woorden raden zónder gloss. Koppel habitación → mueble. Online: memoria de la casa (memory) + mueble↔habitación (match).")

# ============================================================ DIA 4 · GRAMMAR — hay vs estar (color)
def s04_hayestar():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · GRAMÁTICA VISUAL", "Hay vs estar — ¿qué y dónde?", "hay = er is (onbepaald) · está(n) = staat (bepaald). Kleur = de functie.", num=2)
    legend_func(s, Inches(9.7), Inches(0.55))
    card(s, Inches(0.5), Inches(1.7), Inches(6.0), Inches(1.1), fill=GT, line=None)
    text(s, Inches(0.7), Inches(1.7), Inches(5.6), Inches(1.1),
         [[("En el salón ", {"size": 16, "color": INK}), ("hay ", {"size": 18, "bold": True, "color": F_VERB}),
           ("un sofá", {"size": 16, "bold": True, "color": F_OBJ}), (".", {"size": 16, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
    card(s, Inches(6.8), Inches(1.7), Inches(6.0), Inches(1.1), fill=GT, line=None)
    text(s, Inches(7.0), Inches(1.7), Inches(5.6), Inches(1.1),
         [[("El sofá ", {"size": 16, "bold": True, "color": F_SUBJ}), ("está ", {"size": 18, "bold": True, "color": F_PLAC}),
           ("delante de la tele", {"size": 16, "color": INK}), (".", {"size": 16, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
    frame = [("hay + un/una", "onbepaald: hay un parque"), ("hay + dos/mucho", "hay dos baños"), ("hay = invariable", "verandert nooit"),
             ("está + el/la", "bepaald: el parque está…"), ("están + los/las", "los libros están…"), ("🔴 hay ≠ está", "un parque / el parque")]
    x0, y0 = Inches(0.5), Inches(3.15); cw = Inches(4.0); rh = Inches(0.62)
    for i, (a, b) in enumerate(frame):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.12))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(1.9), rh, [[(a, {"size": 11.5, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(2.05), y, cw - Inches(2.2), rh, [[(b, {"size": 10, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.35), Inches(12.3), Inches(0.75),
             [[("Regla: ", {"bold": True, "color": GD}), ("onbepaald (un/dos/mucho) → hay · bepaald (el/la/mi) → está(n). Hay un parque → El parque está cerca.", {"color": GD})]],
             trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR hay/estar. Toon het contrast: eerst «hay un…», dan «el… está…». Online: ¿hay o está(n)? (classify).")

# ============================================================ DIA 5 · QUIZ — ¿hay o está? (reveal)
def s05_hayestar_quiz():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · QUIZ", "¿hay o está(n)?", "Klik een zin → de juiste vorm. Kijk naar het lidwoord.", num=2)
    items = [("En el salón ___ un sofá.", "hay"), ("El sofá ___ delante de la tele.", "está"),
             ("En mi barrio ___ dos parques.", "hay"), ("Los parques ___ cerca.", "están"),
             ("¿___ una farmacia cerca?", "hay"), ("La farmacia ___ en la esquina.", "está")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.78)
    for i, (q, a) in enumerate(items):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(4.3), rh, [[(q, {"size": 12.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.5), y, cw - Inches(4.6), rh, [[("→ " + a, {"size": 14, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Truc: ", {"bold": True, "color": RED}), ("un/una/dos/mucho → hay · el/la/los/las/mi → está(n).", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ hay/estar (retrieval). Klas roept hay/está vóór de klik. Online: ¿hay o está(n)? (classify).")

# ============================================================ DIA 6 · GRAMMAR — preposiciones (reveal)
def s06_preposiciones():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · GRAMÁTICA", "Las preposiciones de lugar", "Klik een cue → de preposición. Casi todas met «de» (de+el=del).", num=2)
    items = [("op / boven", "encima de"), ("onder", "debajo de"), ("naast", "al lado de"),
             ("vóór", "delante de"), ("achter", "detrás de"), ("tussen", "entre"),
             ("dichtbij ↔ ver", "cerca de ↔ lejos de"), ("rechts ↔ links", "a la derecha/izquierda de")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.72)
    for i, (q, a) in enumerate(items):
        c = i // 4; r = i % 4; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.14))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(2.6), rh, [[(q, {"size": 12, "color": MUT})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(2.8), y, cw - Inches(2.9), rh, [[("→ " + a, {"size": 13, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.85), Inches(12.3), Inches(0.85),
             [[("La habitación: ", {"bold": True, "color": GD}), ("La cama está al lado de la ventana. Los libros están encima de la estantería.", {"color": GD})],
              [("🔴 de + el = del: al lado del banco (niet «de el»). Bij la/los/las blijft de: al lado de la plaza.", {"color": RED})]],
             trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR preposiciones. Toon ze fysiek met objecten in de klas. Online: completa la preposición + señala en el plano.")

# ============================================================ DIA 7 · GRAMMAR — estar + gerundio
def s07_gerundio():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · GRAMÁTICA VISUAL", "Estar + gerundio — ahora mismo", "estar + -ando (-ar) / -iendo (-er,-ir). «aan het …».", num=3)
    legend_func(s, Inches(9.7), Inches(0.55))
    seg = [("Valen ", F_SUBJ), ("está ", F_VERB), ("cocinando ", F_OBJ), ("en la cocina", F_PLAC)]
    runs = [[(t, {"size": 22, "bold": True, "color": c, "font": DISPLAY}) for t, c in seg]]
    card(s, Inches(0.5), Inches(1.7), Inches(12.3), Inches(1.2), fill=GT, line=None)
    text(s, Inches(0.8), Inches(1.7), Inches(11.7), Inches(1.2), runs, anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(3.15), Inches(12), Inches(0.4), [[("La formación", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    frame = [("-ar cocinar", "cocin- + ando → cocinando"), ("-er comer", "com- + iendo → comiendo"),
             ("-ir escribir", "escrib- + iendo → escribiendo")]
    x0, y0 = Inches(0.5), Inches(3.6); cw = Inches(4.0); rh = Inches(0.9)
    for i, (a, b) in enumerate(frame):
        x = x0 + i * (cw + Inches(0.15)); y = y0
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y + Inches(0.1), cw - Inches(0.3), Inches(0.35), [[(a, {"size": 13, "bold": True, "color": GD})]])
        text(s, x + Inches(0.15), y + Inches(0.46), cw - Inches(0.3), Inches(0.4), [[(b, {"size": 11, "color": F_VERB, "bold": True})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.9),
             [[("Regla: ", {"bold": True, "color": GD}), ("estar (vervoegd) + gerundio. Enkel estar verandert: estoy/estás/está… comiendo.", {"color": GD})],
              [("Onregelmatig: leer→leyendo · dormir→durmiendo · pedir→pidiendo · decir→diciendo.", {"color": GD})]],
             trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR gerundio. Maak raíz+uitgang zichtbaar. Online: completa: estar + gerundio (cloze) + ¿-ando o -iendo? (classify).")

# ============================================================ DIA 8 · QUIZ — gerundio (reveal)
def s08_gerundio_quiz():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · QUIZ", "¿Qué están haciendo?", "Klik een zin → de juiste vorm. Kijk naar de persoon.", num=3)
    items = [("Valen ___ (cocinar).", "está cocinando"), ("(Yo) ___ (estudiar).", "estoy estudiando"),
             ("Los niños ___ (dormir).", "están durmiendo"), ("¿Tú ___ (leer)?", "estás leyendo"),
             ("Mamá ___ (escribir).", "está escribiendo"), ("Diego ___ (pedir) pizza.", "está pidiendo")]
    x0, y0 = Inches(0.5), Inches(1.7); cw = Inches(6.05); rh = Inches(0.7)
    for i, (q, ans) in enumerate(items):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(3.6), rh, [[(q, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(3.8), y, cw - Inches(3.9), rh, [[("→ " + ans, {"size": 12.5, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.9),
             [[("Enkel estar verandert: ", {"bold": True, "color": G}), ("estoy/estás/está/estamos/estáis/están + gerundio.", {"color": GD})],
              [("Irregulares: leyendo · durmiendo · pidiendo.", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ gerundio (reveal). Coro vóór de klik. Online: cloze estar + gerundio.")

# ============================================================ DIA 9 · READING — dos perfiles
def s09_reading():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§6 · LEER · COMPRENSIÓN", "Dos perfiles — «Mi barrio»", "Lees. Klik een vraag → het antwoord verschijnt.", num=6)
    card(s, Inches(0.5), Inches(1.65), Inches(5.6), Inches(3.9), fill=GT, line=G, lw=1.4)
    avatar(s, "valen", Inches(0.85), Inches(1.95), Inches(1.0))
    text(s, Inches(2.05), Inches(1.98), Inches(3.9), Inches(1.5),
         [[("«Vivo en el centro histórico de Cartagena. Mi casa es antigua, con un balcón con flores. Delante hay una plaza; al lado está la panadería. Mi barrio es tranquilo.»", {"size": 11, "italic": True, "color": INK})]], line=1.16)
    avatar(s, "diego", Inches(0.85), Inches(3.65), Inches(1.0))
    text(s, Inches(2.05), Inches(3.68), Inches(3.9), Inches(1.5),
         [[("«Vivo en un barrio grande de CDMX. Es ruidoso pero me gusta. Detrás de mi edificio hay un mercado. El metro está cerca y lo cojo cada día.»", {"size": 11, "italic": True, "color": INK})]], line=1.16)
    qa = [("¿Qué hay delante de la casa de Valen?", "Una plaza"), ("¿Dónde está la panadería?", "Al lado"),
          ("¿Cómo es el barrio de Diego?", "Ruidoso"), ("¿Qué transporte coge Diego?", "El metro")]
    x = Inches(6.4); y = Inches(1.7)
    for q, a in qa:
        card(s, x, y, Inches(6.4), Inches(0.85), fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y + Inches(0.06), Inches(6.1), Inches(0.4), [[(q, {"size": 12.5, "bold": True, "color": GD})]])
        rev = text(s, x + Inches(0.15), y + Inches(0.44), Inches(6.1), Inches(0.35), [[("→ " + a, {"size": 12, "color": INK})]])
        register_reveal(s, rev)
        y = y + Inches(0.98)
    btn = noodroute(s)
    exercise_solucion(s, Inches(6.4), Inches(5.65), Inches(6.4), Inches(0.6),
             [[("🎯 Leesdoel: ", {"bold": True, "color": GD}), ("scannen naar hay/está + lugares — niet élk woord.", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · READING (lezen→schrijven). Eerst globaal, dan scannen. Daarna: leerlingen vergelijken met hun eigen barrio (hay/está + porque).")

# ============================================================ DIA 10 · LISTENING — ¿cómo llego?
def s10_listening():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§5 · ESCUCHAR · INTERACCIÓN", "¿Cómo llego a la plaza?", "Volg de ruta. Klik un paso → de instructie. (audio + plano op de web)", num=5)
    pasos = [("1️⃣ Sal de casa", "…y ve a la calle"), ("2️⃣ Sigue recto", "hasta el semáforo"),
             ("3️⃣ Gira a la derecha", "en la esquina"), ("4️⃣ La plaza", "está a la izquierda")]
    x0, y0 = Inches(0.7), Inches(1.9); cw = Inches(2.95); ch = Inches(2.4)
    for i, (mom, det) in enumerate(pasos):
        x = x0 + i * (cw + Inches(0.1))
        card(s, x, y0, cw, ch, fill=WHITE, line=LINE, lw=1.2)
        rect(s, x, y0, cw, Inches(0.5), fill=GT)
        text(s, x, y0, cw, Inches(0.5), [[("🔊 paso " + str(i+1), {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(0.15), y0 + Inches(0.7), cw - Inches(0.3), Inches(0.7), [[(mom, {"size": 14, "bold": True, "color": INK, "font": DISPLAY})]], line=1.05)
        rev = text(s, x + Inches(0.15), y0 + Inches(1.5), cw - Inches(0.3), Inches(0.7), [[(det, {"size": 12, "color": G})]], line=1.05)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.85),
             [[("Modelo-audio (docent/TTS): ", {"bold": True, "color": GD}),
               ("«Sal de casa, sigue recto hasta el semáforo, gira a la derecha y la plaza está a la izquierda.» ", {"color": GD})],
              [("Daarna: A vraagt de weg, B geeft die (info-gap).", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · LISTENING (luisteren→spreken). Lees de ruta voor (of TTS); klas volgt op een plano. Daarna info-gap in parejas. Online: ¿cómo llego? (audio + plano).")

# ============================================================ DIA 11 · GRAMMAR — lo/la/los/las
def s11_odpron():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · GRAMÁTICA VISUAL", "Los pronombres lo/la/los/las", "Vervang het voorwerp; concordancia + plaats vóór het werkwoord.", num=4)
    legend_func(s, Inches(9.7), Inches(0.55))
    card(s, Inches(0.5), Inches(1.7), Inches(6.0), Inches(1.1), fill=GT, line=None)
    text(s, Inches(0.7), Inches(1.7), Inches(5.6), Inches(1.1),
         [[("Veo ", {"size": 16, "color": INK}), ("la casa", {"size": 16, "bold": True, "color": F_OBJ}),
           (" → ", {"size": 16, "color": MUT}), ("La", {"size": 18, "bold": True, "color": F_OBJ}), (" veo.", {"size": 16, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
    card(s, Inches(6.8), Inches(1.7), Inches(6.0), Inches(1.1), fill=GT, line=None)
    text(s, Inches(7.0), Inches(1.7), Inches(5.6), Inches(1.1),
         [[("Compro ", {"size": 16, "color": INK}), ("los muebles", {"size": 16, "bold": True, "color": F_OBJ}),
           (" → ", {"size": 16, "color": MUT}), ("Los", {"size": 18, "bold": True, "color": F_OBJ}), (" compro.", {"size": 16, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
    frame = [("lo", "m. ev. (el libro → lo)"), ("la", "v. ev. (la casa → la)"),
             ("los", "m. mv. (los muebles → los)"), ("las", "v. mv. (las sillas → las)")]
    x0, y0 = Inches(0.5), Inches(3.15); cw = Inches(6.0); rh = Inches(0.62)
    for i, (a, b) in enumerate(frame):
        c = i % 2; r = i // 2; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.14))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(1.2), rh, [[(a, {"size": 15, "bold": True, "color": F_OBJ, "font": DISPLAY})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(1.4), y, cw - Inches(1.5), rh, [[(b, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.75), Inches(12.3), Inches(0.9),
             [[("Regla: ", {"bold": True, "color": GD}), ("het pronomen komt overeen (m/v·ev/mv) en staat vóór het vervoegde werkwoord. ", {"color": GD})],
              [("Bij infinitief/gerundio ook achteraan: Voy a comprarlo = Lo voy a comprar · Estoy leyéndolo.", {"color": GD})]],
             trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR OD-pron. Toon doorhalen & vervangen. Online: completa lo/la (cloze) + lo/la Tetris.")

# ============================================================ DIA 12 · QUIZ — lo/la (reveal)
def s12_odpron_quiz():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · QUIZ", "¿lo, la, los o las?", "Klik → het juiste pronomen. Kijk naar het voorwerp.", num=4)
    items = [("¿El sofá? ___ pongo aquí.", "Lo"), ("¿La cama? ___ pongo aquí.", "La"),
             ("¿Los platos? ___ lavo.", "Los"), ("¿Las sillas? ___ pongo.", "Las"),
             ("¿La tele? ___ veo.", "La"), ("¿El coche? ___ aparco.", "Lo")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.78)
    for i, (q, ans) in enumerate(items):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(4.3), rh, [[(q, {"size": 12.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.5), y, cw - Inches(4.6), rh, [[("→ " + ans, {"size": 14, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Concordancia: ", {"bold": True, "color": GD}), ("el→lo · la→la · los→los · las→las. Plaats: vóór het werkwoord.", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ lo/la (retrieval). Klas roept het pronomen vóór de klik. Online: lo/la Tetris.")

# ============================================================ DIA 13 · SPEAKING — describe tu casa
def s13_speaking():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · SPEAKING · INTERACCIÓN", "Describe tu casa y da la ruta", "Speel de scène met de frames. Steun bouwt af: kaarten → beginwoorden → uit het hoofd.", num=2)
    avatar(s, "tu", Inches(11.4), Inches(1.7), Inches(1.3))
    labels = ["¿Qué hay?", "¿Dónde está?", "Preposición", "Cómo llegar", "Distancia", "Opinión"]
    frames = ["En mi casa hay…", "La cama está…", "…al lado de / encima de…", "Sigue recto, gira…", "Está a … minutos.", "Me gusta porque…"]
    x0, y0 = Inches(0.5), Inches(1.8); cw = Inches(3.4); rh = Inches(0.8)
    for i, (lab, fr) in enumerate(zip(labels, frames)):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=G, lw=1.2, shadow=False)
        text(s, x + Inches(0.15), y + Inches(0.05), cw - Inches(0.3), Inches(0.32), [[(lab, {"size": 10, "color": MUT})]])
        text(s, x + Inches(0.15), y + Inches(0.36), cw - Inches(0.3), Inches(0.4), [[(fr, {"size": 12.5, "bold": True, "color": GD, "font": DISPLAY})]])
    chip(s, Inches(0.5), Inches(4.65), "🎙️ Grábate online · «Mensaje de voz: mi habitación / da direcciones»", fill=GT, tcolor=GD, size=11)
    text(s, Inches(0.5), Inches(5.05), Inches(10.5), Inches(0.9),
         [[("Ronda 1: ", {"size": 12, "bold": True, "color": GD}), ("met de kaarten. ", {"size": 12, "color": INK}),
           ("Ronda 2: ", {"size": 12, "bold": True, "color": GD}), ("beginwoorden. ", {"size": 12, "color": INK}),
           ("Ronda 3: ", {"size": 12, "bold": True, "color": GD}), ("uit het hoofd. ", {"size": 12, "color": INK}),
           ("Ronda 4: ", {"size": 12, "bold": True, "color": GD}), ("grábate.", {"size": 12, "color": INK})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.6), Inches(12.3), Inches(0.65),
             [[("Modelo: ", {"bold": True, "color": GD}), ("«En mi cuarto hay una cama y un armario. La cama está al lado de la ventana. Para ir a la plaza, sigue recto y gira a la derecha.»", {"color": GD})]],
             trigger=btn, title_doc="MODELO · docent")
    foot(s)
    notes(s, "TEACHER · SPEAKING (interactie). Rondes met afbouwende steun. Online: recorder (mi habitación + direcciones). Print blijft bruikbaar zonder opname.")

# ============================================================ DIA 14 · WRITING — mapa de mi barrio
def s14_writing():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "WRITING · PRODUCCIÓN", "Mapa de mi barrio", "Schrijf je buurtbeschrijving. Klik → een modeltekst verschijnt.", num=5)
    card(s, Inches(0.5), Inches(1.7), Inches(6.0), Inches(3.9), fill=WHITE, line=LINE, lw=1.2)
    text(s, Inches(0.7), Inches(1.85), Inches(5.6), Inches(0.4), [[("✍️ Escribe aquí tu barrio:", {"size": 12, "bold": True, "color": GD})]])
    for i in range(6):
        rect(s, Inches(0.7), Inches(2.4) + i * Inches(0.5), Inches(5.6), Inches(0.01), fill=LINE)
    chk = ["qué hay (hay un/una…)", "dónde está (está al lado de…)", "4 preposiciones de lugar", "una ruta (sigue recto, gira…)", "la distancia (a … minutos)", "una opinión (me gusta… porque)"]
    x = Inches(6.9); y = Inches(1.7)
    text(s, x, y, Inches(6), Inches(0.4), [[("Checklist:", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    for i, c in enumerate(chk):
        text(s, x, y + Inches(0.5) + i * Inches(0.45), Inches(6), Inches(0.4), [[("☐  " + c, {"size": 13, "color": INK})]])
    rev = card(s, x, Inches(4.35), Inches(6.0), Inches(1.25), fill=GT, line=G, lw=1.2)
    text(s, x + Inches(0.15), Inches(4.4), Inches(5.7), Inches(1.2),
         [[("Modelo: ", {"size": 12, "bold": True, "color": GD}),
           ("«En mi barrio hay una plaza y un parque. La tienda está al lado de mi casa. Para ir al insti, sigo recto y giro a la izquierda; está a cinco minutos. Me gusta mi barrio porque es tranquilo.»", {"size": 11, "italic": True, "color": INK})]], line=1.13)
    register_reveal(s, rev)
    noodroute(s); foot(s)
    notes(s, "TEACHER · WRITING (lezen→schrijven). Checklist = zichtbare steun; onthul het model pas na het schrijven. Nakijkfocus: hay/está, preposiciones (del/de la), una ruta, una opinión. Voedt de Tarea «Mapa de mi barrio».")

# ============================================================ DIA 15 · VOCAB — el barrio + direcciones (reveal)
def s15_barrio():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§5 · VOCABULARIO", "El barrio y las direcciones", "Klik een kaart → la respuesta. Bouw je woordnetwerk.", num=5)
    data = [("la plaza", "het plein"), ("el parque", "het park"), ("la tienda", "de winkel"), ("la farmacia", "de apotheek"),
            ("la parada", "de halte"), ("el semáforo", "verkeerslicht"), ("sigue recto", "ga rechtdoor"), ("gira a la derecha", "sla rechts af"),
            ("cruza la calle", "steek over"), ("está a … minutos", "op … minuten"), ("¿cómo llego a…?", "hoe geraak ik bij…?"), ("la esquina", "de hoek")]
    x0, y0 = Inches(0.5), Inches(1.7); cw = Inches(3.0); rh = Inches(0.7)
    for i, (es, nl) in enumerate(data):
        c = i % 4; r = i // 4; x = x0 + c * (cw + Inches(0.1)); y = y0 + r * (rh + Inches(0.14))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.12), y, Inches(1.8), rh, [[(es, {"size": 11.5, "bold": True, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(1.85), y, cw - Inches(1.95), rh, [[("→ " + nl, {"size": 11, "color": G})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.9),
             [[("Direcciones: ", {"bold": True, "color": GD}), ("¿Cómo llego a…? → sigue recto · gira a la derecha/izquierda · cruza · está a … minutos.", {"color": GD})],
              [("Lugares: la plaza, el parque, la tienda, la farmacia, la parada, la estación, el banco.", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCAB barrio. Klik onthult; koppel lugar → función. Online: lugar↔función (match) + memoria del barrio.")

# ============================================================ DIA 16 · TALLER — b/v + adverbios de lugar
def s16_taller():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "TALLER DE LENGUA", "b/v + adverbios de lugar", "Klik een item → correcte vorm. Gereedschap voor spelling en ruimte.", num=1)
    text(s, Inches(0.5), Inches(1.5), Inches(6), Inches(0.35), [[("A · ortografía: b of v (klinken gelijk)", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    fixes = [("_entana", "ventana (v)"), ("_arrio", "barrio (b)"), ("_ivir", "vivir (v)"), ("_alcón", "balcón (b)")]
    y = Inches(1.95)
    for q, a in fixes:
        card(s, Inches(0.5), y, Inches(6.0), Inches(0.6), fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, Inches(0.62), y, Inches(2.6), Inches(0.6), [[(q, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, Inches(3.3), y, Inches(3.1), Inches(0.6), [[("→ " + a, {"size": 12, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y = y + Inches(0.72)
    text(s, Inches(6.9), Inches(1.5), Inches(6), Inches(0.35), [[("B · adverbios: aquí · ahí · allí", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    conn = [("aquí", "hier (dichtbij)"), ("ahí", "daar (bij jou)"), ("allí / allá", "daar (ver)"), ("cerca ↔ lejos", "dichtbij ↔ ver")]
    y = Inches(1.95)
    for q, a in conn:
        card(s, Inches(6.9), y, Inches(5.9), Inches(0.6), fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, Inches(7.02), y, Inches(2.6), Inches(0.6), [[(q, {"size": 12, "bold": True, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, Inches(9.7), y, Inches(3.0), Inches(0.6), [[("→ " + a, {"size": 11.5, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y = y + Inches(0.72)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.85),
             [[("A: ", {"bold": True, "color": GD}), ("b en v klinken gelijk (≈ b); de spelling leer je uit het hoofd: ventana, vivir, barrio, balcón.", {"color": GD})],
              [("B: aquí (hier) · ahí (bij jou) · allí/allá (ver).", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · TALLER. b/v-spelling (uit het hoofd) + aquí/ahí/allí. Online: drills in de hub.")

# ============================================================ DIA 17 · CULTURE — la vivienda hispana
def s17_cultura():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "CULTURA · PARADA 2: CARTAGENA", "La vivienda hispana", "Klik een kaart → het weetje. Patios, balcones y plazas.", num=1)
    cards = [("🏛️ El patio andaluz", "In het zuiden van España (Sevilla, Córdoba) heeft het huis een patio: een binnentuin met planten en een fontein, koel in de zomer.", "Lucía kent ze goed"),
             ("🌺 Los balcones de Cartagena", "In Cartagena (Colombia) zijn de koloniale huizen kleurrijk, met houten balcones vol bloemen. De ciudad amurallada is UNESCO-erfgoed.", "Valen woont er"),
             ("🟨 La plaza, corazón del barrio", "Overal in de Spaanstalige wereld is de plaza het middelpunt: markt, terrasjes, ontmoeting. «Quedamos en la plaza».", "el corazón del barrio")]
    x0, y0 = Inches(0.5), Inches(1.7); cw = Inches(4.05); ch = Inches(3.4)
    for i, (t, f, nl) in enumerate(cards):
        x = x0 + i * (cw + Inches(0.13))
        card(s, x, y0, cw, ch, fill=WHITE, line=G, lw=1.3)
        rect(s, x, y0, cw, Inches(0.6), fill=GT)
        text(s, x + Inches(0.15), y0, cw - Inches(0.3), Inches(0.6), [[(t, {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(0.2), y0 + Inches(0.8), cw - Inches(0.4), Inches(1.9), [[(f, {"size": 11.5, "color": INK})]], line=1.2)
        register_reveal(s, rev)
        text(s, x + Inches(0.2), y0 + Inches(2.75), cw - Inches(0.4), Inches(0.6), [[(nl, {"size": 10.5, "italic": True, "color": MUT})]], line=1.1)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.35), Inches(12.3), Inches(0.6),
             [[("Actividad: ", {"bold": True, "color": GD}), ("compara tu casa/barrio con un patio o un balcón hispano. ¿Qué hay? ¿Qué es diferente?", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · CULTURE (identiteit in diversiteit, LPD 5). Onthul per kaart. Bruggetje: La Ruta parada 2 = Cartagena (★). Online: klik op Colombia op de kaart.")

# ============================================================ DIA 18 · FINAL_MISSION
def s18_tarea():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(1.35), fill=GD)
    text(s, Inches(0.5), Inches(0.18), Inches(9), Inches(1.0),
         [[("🗺️ Tarea final · Mapa de mi barrio", {"size": 27, "bold": True, "color": WHITE, "font": DISPLAY})],
          [("Dibuja el plano de tu barrio y haz una ruta guiada.", {"size": 13, "italic": True, "color": GT})]])
    avatar(s, "mochila", Inches(11.6), Inches(0.2), Inches(1.0))
    pasos = [("1", "Dibuja el plano", "5–6 lugares (tienda, parque, parada…)"),
             ("2", "Escribe qué hay y dónde está", "«hay un…» · «la tienda está al lado de…»"),
             ("3", "Añade una ruta", "«sigue recto, gira…» (está a … minutos)"),
             ("4", "Añade tu opinión", "«me gusta mi barrio porque…»"),
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
    crit = ["hay + está(n)", "4 preposiciones", "una ruta (sigue/gira)", "una opinión (porque)"]
    x = Inches(0.5)
    for c in crit:
        chip(s, x, Inches(5.45), "☐ " + c, fill=GT, tcolor=GD, size=10, w=Inches(3.05)); x = x + Inches(3.15)
    text(s, Inches(0.5), Inches(6.05), Inches(12), Inches(0.4),
         [[("🎯 ", {"size": 12}), ("Afzender jij · ontvanger de klas · doel je barrio delen · situatie een rondleiding · resultaat: plano + presentación oral.", {"size": 11.5, "italic": True, "color": MUT})]])
    foot(s)
    notes(s, "TEACHER · FINAL_MISSION (communicatieve eindtaak). Afzender/ontvanger/doel/situatie/resultaat expliciet. Beoordeel met de rúbrica; opname op de web.")

# ============================================================ DIA 19 · QUIZ — la mezcla (retrieval)
def s19_mezcla():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "QUIZ · LA MEZCLA", "Ophaal door elkaar", "Gemengde ophaal van de hele unit. Klik → het antwoord. (retrieval)", num=1)
    items = [("En el salón ___ un sofá (hay/está)", "hay"), ("El sofá ___ delante de la tele", "está"),
             ("de + el =", "del"), ("comer → gerundio", "comiendo"),
             ("dormir → gerundio", "durmiendo"), ("¿La casa? ___ veo", "la"),
             ("¿Los muebles? ___ compro", "los"), ("«naast» =", "al lado de")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.62)
    for i, (q, a) in enumerate(items):
        c = i // 4; r = i % 4; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.16))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(4.0), rh, [[(q, {"size": 11.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.15), y, cw - Inches(4.3), rh, [[("→ " + a, {"size": 12, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.05), Inches(12.3), Inches(0.55),
             [[("Alles komt terug: ", {"bold": True, "color": GD}), ("hay/estar + preposiciones · estar + gerundio · lo/la/los/las · direcciones.", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ mezcla (retrieval vóór herlezen). Zonder waarschuwing door elkaar. Exit-ticket. Zwakke punten → terug via menu.")

# ============================================================ DIA 20 · FEEDBACK/REPASO
def s20_repaso():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "REPASO · LO ESENCIAL", "Lo esencial de un vistazo", "De volledige herhaling (12 spellen, drills) staat online. Hier: de kern + semáforo.", num=1)
    ess = ["Hay vs estar: hay + un/dos (onbepaald) · está(n) + el/la/mi (bepaald).",
           "Preposiciones: encima/debajo/al lado/delante/detrás de · entre · cerca/lejos de. (de+el=del).",
           "Estar + gerundio: estoy/estás/está… + -ando/-iendo. Irreg.: leyendo, durmiendo, pidiendo.",
           "Lo/la/los/las (OD): vervangt het voorwerp, concordantie, vóór het ww. of achter inf./gerundio.",
           "🔴 Trampas: hay ≠ está · de+el=del · lo/la vóór het ww. · concordancia lo/la/los/las."]
    card(s, Inches(0.5), Inches(1.6), Inches(12.3), Inches(2.5), fill=CREMA, line=None)
    y = Inches(1.8)
    for e in ess:
        text(s, Inches(0.8), y, Inches(11.8), Inches(0.45), [[("• ", {"size": 13, "bold": True, "color": GD}), (e, {"size": 12, "color": INK})]])
        y = y + Inches(0.46)
    text(s, Inches(0.5), Inches(4.3), Inches(12), Inches(0.35), [[("Semáforo — ¿cómo lo llevas?", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    can = ["mijn huis beschrijven (habitaciones/muebles)", "hay + estar + preposiciones", "estar + gerundio (qué está pasando)", "de pronombres lo/la/los/las", "de weg vragen en wijzen"]
    y = Inches(4.75)
    for c in can:
        text(s, Inches(0.8), y, Inches(7.0), Inches(0.4), [[(c, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        for j, (em, col) in enumerate([("🔴", RED), ("🟠", AMBER), ("🟢", G)]):
            chip(s, Inches(8.0) + j * Inches(1.5), y + Inches(0.03), em + " ", fill=WHITE, tcolor=col, size=12, w=Inches(1.3))
        y = y + Inches(0.42)
    foot(s)
    notes(s, "TEACHER · FEEDBACK/REPASO. Semáforo = zelfevaluatie. Repaso-drills online (12 spellen). Bruggetje: U3 «Conectados» — media, ir a + inf., le/les.")

# ============================================================ DIA 21 · TEACHER_NOTES
def s21_teacher():
    s = slide(); bg(s, GD)
    text(s, Inches(0.6), Inches(0.4), Inches(12), Inches(0.8), [[("TEACHER_NOTES · U2 «Aquí vivo»", {"size": 26, "bold": True, "color": WHITE, "font": DISPLAY})]])
    blocks = [("Timing (50 min)", "Menu 2' · la casa 6' · hay/estar + preposiciones 12' · estar+gerundio 10' · lo/la 8' · el barrio/escucha 8' · Tarea-briefing 4'."),
              ("Kernvalstrikken", "hay (onbepaald: un/dos) ≠ está (bepaald: el/la) · de + el = del (al lado del banco) · lo/la vóór het vervoegde werkwoord + concordancia (la casa → la veo) · gerundio-irreg.: leyendo, durmiendo, pidiendo."),
              ("Differentiatie", "Sterker: volledige buurtbeschrijving + ruta + una opinión + estar+gerundio in 3ª persoon. Zwakker: hay/está-kaart + preposiciones-scène langer open, frames houden; lo/la met vaste vraag-antwoord-paren."),
              ("Digitaal", "12 spellen + flip cards + gramática interactiva (hay/estar · gerundio · lo/la) + recorder (mi habitación · direcciones) + Lectura (dos perfiles) + klikbare kaart (Colombia ★) op de página digital. QR's → juiste anker."),
              ("Evaluatie & LPD", "Tarea «Mapa de mi barrio» met rúbrica (4 criteria). LPD (III-Spa-d): casa/barrio 7 · hay/estar+preposiciones 8·4 · gerundio 8 · lo/la 8 · direcciones/interactie 4·9 · lezen 1·2·5 · cultuur 5. Bron: EELP-U2 (estar/lugar) + reservoir.")]
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
    s01_title(); s02_menu(); s03_vocab(); s04_hayestar(); s05_hayestar_quiz(); s06_preposiciones(); s07_gerundio()
    s08_gerundio_quiz(); s09_reading(); s10_listening(); s11_odpron(); s12_odpron_quiz(); s13_speaking(); s14_writing()
    s15_barrio(); s16_taller(); s17_cultura(); s18_tarea(); s19_mezcla(); s20_repaso()
    if include_teacher:
        s21_teacher()

def _repaint(path):
    import zipfile, os as _os
    reps = [("1E9E74", "7C56A9"), ("1e9e74", "7c56a9"), ("2EB085", "9374C2"), ("2eb085", "9374c2"),
            ("C5 · A1 · La Ruta", "C6+ · aquí vivo")]
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
