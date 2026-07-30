#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_c6plus_u1_docente.py — Interactieve PowerPoint C6+ · Unidad 1 «El día a día»
================================================================================
Zelfde engine/pijplijn als de golden sample (gen_u0_docente = de engine). Enkel de SLIDES
zijn C6+·U1-specifiek. Cursuskleur = PAARS (C6+). Twee decks (beide .pptx):
  · C6plus_U1_docente.pptx — vrije navigatie, oplossingen bij klik + didactiek in notities.
  · C6plus_U1_alumno.pptx  — gewone diavoorstelling, antwoorden bij klik (F5, geen kiosk).
Grammatica: reflexivos · ser/estar-contrast · gustar + OI · P3-seed «me gusta… porque».
Spaans-eerst + NL-steun. ≥20 dia's. Dekt de vier vaardigheden.
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

# ---- PAARS-override (C6+) ----
E.G  = RGBColor(0x7C, 0x56, 0xA9)
E.GD = RGBColor(0x5B, 0x3E, 0x83)
E.GT = RGBColor(0xEE, 0xE8, 0xF5)
G, GD, GT = E.G, E.GD, E.GT
# ---- GEEN GROEN-lek: functioneel 'voorwerp'-groen en 'plaats'-teal wegwerken ----
E.F_OBJ  = RGBColor(0xB4, 0x30, 0x9A)   # magenta (voorwerp)
E.F_PLAC = RGBColor(0x64, 0x74, 0x8B)   # leisteenblauw (plaats)
F_OBJ, F_PLAC = E.F_OBJ, E.F_PLAC
F_REFL = RGBColor(0x7C, 0x3A, 0xED)     # paars-violet voor het reflexief pronomen

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DOCENTE = os.path.join(HERE, "C6plus_U1_docente.pptx")
OUT_ALUMNO_PPTX = os.path.join(HERE, "C6plus_U1_alumno.pptx")
TAB = "U1 · EL DÍA A DÍA"

def foot(s): footer(s, tab=TAB, page=pg())

# ============================================================ DIA 1 · TITLE
def s01_title():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(4.7), fill=G)
    rect(s, 0, Inches(4.7), EMU_W, Inches(0.09), fill=GD)
    text(s, Inches(0.6), Inches(0.35), Inches(3.4), Inches(3.6),
         [[("1", {"size": 260, "bold": True, "color": RGBColor(0x93, 0x74, 0xC2), "font": DISPLAY})]],
         anchor=MSO_ANCHOR.MIDDLE)
    chip(s, Inches(4.35), Inches(0.85), "LA RUTA · ESPAÑA · EL DÍA A DÍA ⏰", fill=WHITE, tcolor=GD, size=12)
    text(s, Inches(4.3), Inches(1.35), Inches(8.6), Inches(1.5),
         [[("El día a día", {"size": 60, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(4.35), Inches(2.7), Inches(8.4), Inches(0.6),
         [[("Tu rutina, la hora, cómo te sientes y qué te gusta (reflexivos · ser/estar · gustar).", {"size": 15, "italic": True, "color": GT})]])
    text(s, Inches(4.35), Inches(3.35), Inches(8.4), Inches(0.9),
         [[("¿Cómo es un día en tu vida?", {"size": 24, "bold": True, "color": WHITE, "font": DISPLAY})],
          [("Hoe ziet jouw dag eruit?", {"size": 13, "italic": True, "color": GT})]])
    text(s, Inches(0.6), Inches(4.95), Inches(6), Inches(0.4),
         [[("La gente de la ruta — parada 1: España (Lucía)", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
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
    notes(s, "TEACHER · TITLE. U1 = start van de A2-motor. Kerngrammatica: reflexieve werkwoorden (me/te/se…), ser vs estar-contrast, "
             "gustar + OI. P3-seed: «me gusta… porque». Parada 1 = España (el horario español, Lucía). "
             "Kernvalstrikken: nunca «yo levanto» (reflexief heeft me/te/se) · gustar «al revés» (me gusta la música) · es aburrido ≠ está aburrido. "
             "Docentdeck = vrije navigatie + oplossing; leerlingdeck (.pptx, F5) = elke klik onthult het volgende antwoord.")

# ============================================================ DIA 2 · LESSON_MENU
def s02_menu():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "MENÚ DE LA LECCIÓN", "El mapa de la Unidad 1",
               "Kies je route — klik een tegel. Alles oefent naar de Tarea «Mi día a día» toe.", num=1)
    tiles = [
        ("§1", "La hora", "¿qué hora es?", G, 15),
        ("§2", "Mi rutina", "acciones · conectores", G, 3),
        ("§3", "Reflexivos", "me/te/se + verbo", G, 4),
        ("§4", "Ser / estar", "identiteit ↔ gevoel", G, 7),
        ("§5", "Gustar + OI", "me gusta… porque", G, 11),
        ("★", "Lectura + escucha", "dos perfiles", GD, 9),
        ("🌞", "Cultura", "el horario español", GD, 17),
        ("🗓️", "Tarea · Mi día", "blog + presentación", GD, 18),
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
             "Kern = §3 reflexivos + §4 ser/estar + §5 gustar. Kruisverwijzing print/HTML: «oefen online — 13 juegos + ~100 oefeningen».")

# ============================================================ DIA 3 · VOCABULARY — la rutina
def s03_vocab():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · VOCABULARIO", "Las acciones de la rutina", "De woorden van je dag — observa. Herken ze, dan gebruik je ze.", num=2)
    legend_func(s, Inches(9.7), Inches(0.55))
    rows = [("me levanto", "ik sta op", "levantarse"), ("me ducho", "ik douche", "ducharse"),
            ("desayuno", "ik ontbijt", "desayunar"), ("como / meriendo", "ik eet / snack", "a las 2 / 5"),
            ("hago los deberes", "ik maak huiswerk", "por la tarde"), ("vuelvo a casa", "ik keer terug", "volver (o→ue)"),
            ("ceno", "ik eet 's avonds", "cenar"), ("me acuesto", "ik ga naar bed", "acostarse (o→ue)")]
    x0, y0 = Inches(0.5), Inches(1.6); cw = Inches(6.1); rh = Inches(0.6)
    for i, (k, v, nl) in enumerate(rows):
        c = 0 if i < 4 else 1; r = i % 4
        x = x0 + c * (cw + Inches(0.15)); y = y0 + r * (rh + Inches(0.12))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(2.4), rh, [[(k, {"size": 13, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(2.5), y, Inches(2.1), rh, [[(v, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(4.5), y, Inches(1.5), rh, [[(nl, {"size": 9, "italic": True, "color": MUT})]], anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(4.75), Inches(12.3), Inches(0.5),
         [[("Conectores de secuencia: ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("primero · luego · después · por último", {"size": 13, "bold": True, "color": F_TIME})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.35), Inches(12.3), Inches(0.95),
             [[("Un día: ", {"bold": True, "color": GD}), ("Primero me levanto, luego me ducho, después desayuno y por último voy al instituto.", {"color": GD})],
              [("Frecuencia: siempre · normalmente · a veces · nunca.", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCABULARY. Laat de acties raden zónder de NL-gloss. Koppel meteen aan de hora (§1) en aan de reflexivos (§3). "
             "Online: flip cards + memoria de la rutina + acción↔hora (match).")

# ============================================================ DIA 4 · GRAMMAR — reflexivos (color)
def s04_reflexivos():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · GRAMÁTICA VISUAL", "Los reflexivos — la acción vuelve a ti", "Kleur = de functie. Pronombre (me/te/se…) + werkwoord.", num=3)
    legend_func(s, Inches(9.7), Inches(0.55))
    seg = [("(Yo) ", F_SUBJ), ("me ", F_REFL), ("levanto ", F_VERB), ("a las siete", F_PLAC)]
    runs = [[(t, {"size": 24, "bold": True, "color": c, "font": DISPLAY}) for t, c in seg]]
    card(s, Inches(0.5), Inches(1.7), Inches(12.3), Inches(1.2), fill=GT, line=None)
    text(s, Inches(0.8), Inches(1.7), Inches(11.7), Inches(1.2), runs, anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(3.15), Inches(12), Inches(0.4), [[("Los pronombres reflexivos", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    frame = [("yo → me", "me levanto"), ("tú → te", "te levantas"), ("él/ella → se", "se levanta"),
             ("nosotros → nos", "nos levantamos"), ("vosotros → os", "os levantáis"), ("ellos → se", "se levantan")]
    x0, y0 = Inches(0.5), Inches(3.6); cw = Inches(4.0); rh = Inches(0.62)
    for i, (a, b) in enumerate(frame):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.12))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(1.8), rh, [[(a, {"size": 12, "bold": True, "color": F_REFL})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(2.0), y, cw - Inches(2.1), rh, [[(b, {"size": 12, "color": F_VERB, "bold": True})]], anchor=MSO_ANCHOR.MIDDLE)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.6), Inches(12.3), Inches(0.75),
             [[("Regla: ", {"bold": True, "color": GD}), ("pronombre + verbo, in die volgorde. Het pronomen past bij het onderwerp: me (yo), te (tú), se (él/ella)…", {"color": GD})]],
             trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR (color-coding). Maak pronombre + verbo zichtbaar. Kleur nooit als enige drager. "
             "Online: «completa: los reflexivos» (cloze) + pronombre Tetris.")

# ============================================================ DIA 5 · QUIZ — reflexivos (reveal)
def s05_reflexivos_quiz():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · QUIZ", "Completa los reflexivos", "Klik een zin → de juiste vorm verschijnt. Kijk naar de persoon.", num=3)
    items = [("Yo ___ (levantarse) a las 7.", "me levanto"), ("¿Tú ___ (ducharse) hoy?", "te duchas"),
             ("Lucía ___ (despertarse) temprano.", "se despierta"), ("Nosotros ___ (acostarse) a las 11.", "nos acostamos"),
             ("Diego ___ (vestirse) rápido.", "se viste"), ("Ellos ___ (peinarse) ahora.", "se peinan")]
    x0, y0 = Inches(0.5), Inches(1.7); cw = Inches(6.05); rh = Inches(0.7)
    for i, (q, ans) in enumerate(items):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(4.0), rh, [[(q, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.2), y, cw - Inches(4.3), rh, [[("→ " + ans, {"size": 13, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.95),
             [[("Pronombre + vorm: ", {"bold": True, "color": G}),
               ("me/te/se/nos/os/se + verbo. Cambio vocálico: me despierto, me acuesto, me visto (nosotros/vosotros GEEN wissel).", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ (reveal). Laat de klas pronombre+vorm roepen vóór de klik. Online: «completa: los reflexivos» (cloze).")

# ============================================================ DIA 6 · GRAMMAR — la conjugación (reveal)
def s06_conjugacion():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · GRAMÁTICA", "«levantarse» — klik om te onthullen", "Denk eerst pronombre + vorm; klik dan de kaart.", num=3)
    pers = ["yo", "tú", "él/ella", "nosotros", "vosotros", "ellos"]
    forms = ["me levanto", "te levantas", "se levanta", "nos levantamos", "os levantáis", "se levantan"]
    x0, y0 = Inches(1.6), Inches(1.9); cw = Inches(3.4); ch = Inches(1.0)
    for i, (p, f) in enumerate(zip(pers, forms)):
        c = i % 3; r = i // 3; x = x0 + c * (cw + Inches(0.3)); y = y0 + r * (ch + Inches(0.22))
        card(s, x, y, cw, ch, fill=WHITE, line=G, lw=1.4)
        text(s, x, y + Inches(0.1), cw, Inches(0.32), [[(p, {"size": 12, "color": MUT})]], align=PP_ALIGN.CENTER)
        rev = text(s, x, y + Inches(0.44), cw, Inches(0.5), [[(f, {"size": 18, "bold": True, "color": GD, "font": DISPLAY})]], align=PP_ALIGN.CENTER)
        register_reveal(s, rev)
    text(s, Inches(0.5), Inches(5.05), Inches(12.3), Inches(0.5),
         [[("🟣 ", {"size": 12}), ("La posición: ", {"size": 13, "bold": True, "color": GD}),
           ("normaal vóór het werkwoord (Me ducho); bij infinitief mag ook achteraan: Quiero ducharme = Me quiero duchar.", {"size": 12, "color": INK})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.65), Inches(12.3), Inches(0.7),
             [[("La bota: ", {"bold": True, "color": GD}), ("cambio vocálico in yo·tú·él·ellos (me despierto, me acuesto), NIET in nosotros/vosotros.", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR reflexief (reveal). Coro vóór de klik. Online: vervoegingswiel + pronombre Tetris.")

# ============================================================ DIA 7 · GRAMMAR — ser vs estar
def s07_serestar():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · GRAMÁTICA VISUAL", "Ser vs estar — el contraste", "ser = wie/wat je bent (permanent) · estar = waar/hoe (plaats/gevoel).", num=4)
    legend_func(s, Inches(9.7), Inches(0.55))
    card(s, Inches(0.5), Inches(1.7), Inches(6.0), Inches(1.1), fill=GT, line=None)
    text(s, Inches(0.7), Inches(1.7), Inches(5.6), Inches(1.1),
         [[("Lucía ", {"size": 18, "bold": True, "color": INK}), ("es ", {"size": 18, "bold": True, "color": F_SUBJ}),
           ("simpática", {"size": 18, "bold": True, "color": INK}), ("  (karakter)", {"size": 12, "color": MUT})]], anchor=MSO_ANCHOR.MIDDLE)
    card(s, Inches(6.8), Inches(1.7), Inches(6.0), Inches(1.1), fill=GT, line=None)
    text(s, Inches(7.0), Inches(1.7), Inches(5.6), Inches(1.1),
         [[("Lucía ", {"size": 18, "bold": True, "color": INK}), ("está ", {"size": 18, "bold": True, "color": F_PLAC}),
           ("cansada", {"size": 18, "bold": True, "color": INK}), ("  (gevoel nu)", {"size": 12, "color": MUT})]], anchor=MSO_ANCHOR.MIDDLE)
    frame = [("ser →", "identiteit / herkomst"), ("ser →", "beroep / karakter"), ("ser →", "uur & datum"),
             ("estar →", "plaats (dónde)"), ("estar →", "gevoel / toestand"), ("🔴 es ≠ está", "aburrido: saai ≠ verveelt zich")]
    x0, y0 = Inches(0.5), Inches(3.15); cw = Inches(4.0); rh = Inches(0.62)
    for i, (a, b) in enumerate(frame):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.12))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(1.6), rh, [[(a, {"size": 12, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(1.75), y, cw - Inches(1.9), rh, [[(b, {"size": 10.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.35), Inches(12.3), Inches(0.75),
             [[("Regla: ", {"bold": True, "color": GD}), ("permanent/eigenschap → ser (soy simpático) · plaats/gevoel/toestand nu → estar (estoy cansado).", {"color": GD})]],
             trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR ser/estar. Toon het contrast fysiek (es cansada? nee → está cansada). Online: «¿ser o estar?» (classify) + minimale paren.")

# ============================================================ DIA 8 · QUIZ — ¿ser o estar? (reveal)
def s08_serestar_quiz():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · QUIZ", "¿ser o estar?", "Klik een zin → de juiste vorm. Kijk naar de betekenis.", num=4)
    items = [("Lucía ___ de Sevilla.", "es"), ("Hoy ___ cansado.", "estoy"), ("___ estudiante.", "soy"),
             ("La mochila ___ en clase.", "está"), ("La clase ___ aburrida (saai).", "es"), ("(Yo) ___ aburrido (nu).", "estoy")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.78)
    for i, (q, a) in enumerate(items):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(4.3), rh, [[(q, {"size": 12.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.5), y, cw - Inches(4.6), rh, [[("→ " + a, {"size": 14, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Contraste: ", {"bold": True, "color": RED}), ("es aburrido = saai (eigenschap) · está aburrido = verveelt zich (nu). Idem: es/está listo, rico, bueno.", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ ser/estar (retrieval). Klas roept ser/estar vóór de klik. Online: «¿ser o estar?» (classify).")

# ============================================================ DIA 9 · READING — dos perfiles
def s09_reading():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§6 · LEER · COMPRENSIÓN", "Dos perfiles — «¿Qué les gusta?»", "Lees su día y sus gustos. Klik een vraag → het antwoord verschijnt.", num=6)
    card(s, Inches(0.5), Inches(1.65), Inches(5.6), Inches(3.9), fill=GT, line=G, lw=1.4)
    avatar(s, "lucia", Inches(0.85), Inches(1.95), Inches(1.0))
    text(s, Inches(2.05), Inches(1.98), Inches(3.9), Inches(1.5),
         [[("«Me despierto a las siete y me levanto enseguida. Como a las tres. Por la tarde me gusta bailar flamenco. Hoy estoy contenta porque es viernes.»", {"size": 11, "italic": True, "color": INK})]], line=1.16)
    avatar(s, "diego", Inches(0.85), Inches(3.65), Inches(1.0))
    text(s, Inches(2.05), Inches(3.68), Inches(3.9), Inches(1.5),
         [[("«Me levanto a las seis y media. Me encantan los videojuegos, pero no me gusta nada madrugar. Me acuesto a las once. Estoy cansado, pero feliz.»", {"size": 11, "italic": True, "color": INK})]], line=1.16)
    qa = [("¿A qué hora se levanta Lucía?", "A las siete"), ("¿Qué le gusta a Lucía?", "Bailar flamenco"),
          ("¿Qué NO le gusta a Diego?", "Madrugar"), ("¿Cómo está Diego?", "Cansado, pero feliz")]
    x = Inches(6.4); y = Inches(1.7)
    for q, a in qa:
        card(s, x, y, Inches(6.4), Inches(0.85), fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y + Inches(0.06), Inches(6.1), Inches(0.4), [[(q, {"size": 12.5, "bold": True, "color": GD})]])
        rev = text(s, x + Inches(0.15), y + Inches(0.44), Inches(6.1), Inches(0.35), [[("→ " + a, {"size": 12, "color": INK})]])
        register_reveal(s, rev)
        y = y + Inches(0.98)
    btn = noodroute(s)
    exercise_solucion(s, Inches(6.4), Inches(5.65), Inches(6.4), Inches(0.6),
             [[("🎯 Leesdoel: ", {"bold": True, "color": GD}), ("scannen naar la hora, los gustos y el ánimo — niet élk woord.", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · READING (lezen→spreken-keten). Eerst globaal, dan scannen. Onthul antwoorden pas na de klas. "
             "Daarna: leerlingen zeggen met wie ze meer gemeen hebben + hun gustos (me gusta… porque).")

# ============================================================ DIA 10 · LISTENING — un día con Lucía
def s10_listening():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · ESCUCHAR", "Un día con Lucía (el horario)", "Klik un momento → la hora + la acción. (audio op de digitale pagina)", num=2)
    moments = [("🌅 la mañana", "7:00", "se levanta y se ducha"), ("🍽️ la comida", "14:00", "come (¡tarde!)"),
               ("📓 la tarde", "18:00", "hace los deberes"), ("🌙 la noche", "22:00", "cena y se acuesta")]
    x0, y0 = Inches(0.7), Inches(1.9); cw = Inches(2.95); ch = Inches(2.4)
    for i, (mom, hora, act) in enumerate(moments):
        x = x0 + i * (cw + Inches(0.1))
        card(s, x, y0, cw, ch, fill=WHITE, line=LINE, lw=1.2)
        rect(s, x, y0, cw, Inches(0.5), fill=GT)
        text(s, x, y0, cw, Inches(0.5), [[("🔊 " + mom, {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(0.15), y0 + Inches(0.65), cw - Inches(0.3), Inches(0.4), [[("¿Qué hora?", {"size": 12, "color": MUT})]])
        rev1 = text(s, x + Inches(0.15), y0 + Inches(1.0), cw - Inches(0.3), Inches(0.5), [[(hora, {"size": 20, "bold": True, "color": INK, "font": DISPLAY})]])
        text(s, x + Inches(0.15), y0 + Inches(1.6), cw - Inches(0.3), Inches(0.4), [[("¿Qué hace?", {"size": 11, "color": MUT})]])
        rev2 = text(s, x + Inches(0.15), y0 + Inches(1.95), cw - Inches(0.3), Inches(0.4), [[(act, {"size": 11.5, "bold": True, "color": G})]])
        register_reveal(s, rev1); register_reveal(s, rev2)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.85),
             [[("Modelo-audio (docent leest of TTS): ", {"bold": True, "color": GD}),
               ("«Me llamo Lucía. Me levanto a las siete, me ducho y desayuno. Como a las dos…» ", {"color": GD})],
              [("Daarna schrijven: elke leerling noteert zijn eigen horario.", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · LISTENING (selectief → schrijven). Lees «Un día con Lucía» voor (of TTS). Klas noteert hora + acción; onthul per klik. "
             "Koppel meteen aan het eigen dagverhaal.")

# ============================================================ DIA 11 · GRAMMAR — gustar al revés
def s11_gustar():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§5 · GRAMÁTICA VISUAL", "Gustar — ¡al revés! ¿gusta o gustan?", "Me gusta la música = de muziek bevalt míj. Nooit «yo gusto».", num=5)
    card(s, Inches(0.5), Inches(1.7), Inches(6.0), Inches(1.1), fill=CREMA, line=None)
    text(s, Inches(0.7), Inches(1.7), Inches(5.6), Inches(1.1),
         [[("NL: ", {"size": 12, "bold": True, "color": MUT}), ("Ik", {"size": 14, "bold": True, "color": F_SUBJ}),
           (" vind muziek leuk.", {"size": 14, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
    card(s, Inches(6.8), Inches(1.7), Inches(6.0), Inches(1.1), fill=GT, line=None)
    text(s, Inches(7.0), Inches(1.7), Inches(5.6), Inches(1.1),
         [[("ES: ", {"size": 12, "bold": True, "color": MUT}), ("Me ", {"size": 14, "bold": True, "color": F_REFL}),
           ("gusta ", {"size": 14, "bold": True, "color": F_VERB}), ("la música", {"size": 14, "bold": True, "color": F_OBJ}), (".", {"size": 14, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
    frame = [("gusta", "+ 1 cosa (el/la)"), ("gusta", "+ infinitivo (bailar)"), ("gustan", "+ varias cosas (los/las)")]
    x0, y0 = Inches(0.5), Inches(3.15); cw = Inches(4.0); rh = Inches(0.75)
    for i, (a, b) in enumerate(frame):
        x = x0 + i * (cw + Inches(0.15)); y = y0
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y + Inches(0.08), cw - Inches(0.3), Inches(0.32), [[(a, {"size": 14, "bold": True, "color": GD, "font": DISPLAY})]])
        text(s, x + Inches(0.15), y + Inches(0.42), cw - Inches(0.3), Inches(0.3), [[(b, {"size": 11, "color": INK})]])
    text(s, Inches(0.5), Inches(4.2), Inches(12.3), Inches(0.5),
         [[("¿A quién? ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("(a mí) me · (a ti) te · (a él/ella) le · (a nosotros) nos · (a vosotros) os · (a ellos) les", {"size": 12, "color": INK})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.95), Inches(12.3), Inches(0.9),
             [[("Regla: ", {"bold": True, "color": GD}), ("het werkwoord volgt het DING (ev/mv), niet de persoon. Me gusta el fútbol · Me gustan los perros. ", {"color": GD})],
              [("🔴 nunca «yo gusto» · met sustantivo altijd el/la/los/las.", {"color": RED})]],
             trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR gustar. Maak «al revés» fysiek: het ding is het onderwerp. Online: «¿gusta o gustan?» (classify) + sleep-woordvolgorde.")

# ============================================================ DIA 12 · GRAMMAR — gustar pronombres + escala (reveal)
def s12_gustar_quiz():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§5 · QUIZ · P3-SEED", "Gustos: pronombre + «porque»", "Klik → de juiste vorm. Y da tu opinión con «me gusta… porque…».", num=5)
    items = [("A mí ___ el fútbol.", "me gusta"), ("A ti ___ los deportes.", "te gustan"),
             ("A Lucía ___ bailar.", "le gusta"), ("A mis padres ___ la siesta.", "les gusta"),
             ("A mí no ___ los lunes.", "me gustan"), ("A nosotros ___ viajar.", "nos gusta")]
    x0, y0 = Inches(0.5), Inches(1.7); cw = Inches(6.05); rh = Inches(0.68)
    for i, (q, ans) in enumerate(items):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.16))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(3.9), rh, [[(q, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.1), y, cw - Inches(4.25), rh, [[("→ " + ans, {"size": 13, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    text(s, Inches(0.5), Inches(4.55), Inches(12.3), Inches(0.6),
         [[("La escala: ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("me encanta 😍 → me gusta mucho → me gusta 🙂 → no me gusta → no me gusta nada 🙁", {"size": 12, "color": INK})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.2), Inches(12.3), Inches(0.85),
             [[("P3-seed (mi opinión): ", {"bold": True, "color": G}), ("Me gusta la música latina porque es alegre. No me gustan los lunes porque estoy cansado.", {"color": GD})],
              [("Reageren: a mí también (+) · a mí tampoco (−).", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ gustar + P3-seed. Klas vult vóór de klik. Daarna geeft elke leerling één mening «me gusta… porque…». Online: «completa: gustar» (cloze).")

# ============================================================ DIA 13 · SPEAKING — describe tu día
def s13_speaking():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · SPEAKING · INTERACCIÓN", "¡Cuenta tu día!", "Speel de scène met de frames. Steun bouwt af: kaarten → beginwoorden → uit het hoofd.", num=3)
    avatar(s, "tu", Inches(11.4), Inches(1.7), Inches(1.3))
    labels = ["Despertar", "Higiene", "Desayuno", "Instituto", "Tarde", "Noche"]
    frames = ["Me despierto a las…", "Me ducho y me visto.", "Desayuno…", "Voy al insti a las…", "Hago los deberes / me gusta…", "Ceno y me acuesto a las…"]
    x0, y0 = Inches(0.5), Inches(1.8); cw = Inches(3.4); rh = Inches(0.8)
    for i, (lab, fr) in enumerate(zip(labels, frames)):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=G, lw=1.2, shadow=False)
        text(s, x + Inches(0.15), y + Inches(0.05), cw - Inches(0.3), Inches(0.32), [[(lab, {"size": 10, "color": MUT})]])
        text(s, x + Inches(0.15), y + Inches(0.36), cw - Inches(0.3), Inches(0.4), [[(fr, {"size": 12.5, "bold": True, "color": GD, "font": DISPLAY})]])
    chip(s, Inches(0.5), Inches(4.65), "🎙️ Grábate online · «Mensaje de voz: mi día a día»", fill=GT, tcolor=GD, size=11)
    text(s, Inches(0.5), Inches(5.05), Inches(10.5), Inches(0.9),
         [[("Ronda 1: ", {"size": 12, "bold": True, "color": GD}), ("met de kaarten. ", {"size": 12, "color": INK}),
           ("Ronda 2: ", {"size": 12, "bold": True, "color": GD}), ("beginwoorden. ", {"size": 12, "color": INK}),
           ("Ronda 3: ", {"size": 12, "bold": True, "color": GD}), ("uit het hoofd. ", {"size": 12, "color": INK}),
           ("Ronda 4: ", {"size": 12, "bold": True, "color": GD}), ("grábate.", {"size": 12, "color": INK})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.6), Inches(12.3), Inches(0.65),
             [[("Modelo: ", {"bold": True, "color": GD}), ("«Me levanto a las siete, me ducho y desayuno. Voy al insti a las ocho. Por la tarde me gusta bailar. Ceno y me acuesto a las once.»", {"color": GD})]],
             trigger=btn, title_doc="MODELO · docent")
    foot(s)
    notes(s, "TEACHER · SPEAKING (interactie). Automatiseer de rutina in rondes met afbouwende steun. "
             "Online: recorder (opname + zelfevaluatie). Print blijft bruikbaar zonder opname.")

# ============================================================ DIA 14 · WRITING — mi día a día
def s14_writing():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "WRITING · PRODUCCIÓN", "Mi día a día (el blog)", "Schrijf je dagblog. Klik → een modeltekst verschijnt.", num=3)
    card(s, Inches(0.5), Inches(1.7), Inches(6.0), Inches(3.9), fill=WHITE, line=LINE, lw=1.2)
    text(s, Inches(0.7), Inches(1.85), Inches(5.6), Inches(0.4), [[("✍️ Escribe aquí tu día:", {"size": 12, "bold": True, "color": GD})]])
    for i in range(6):
        rect(s, Inches(0.7), Inches(2.4) + i * Inches(0.5), Inches(5.6), Inches(0.01), fill=LINE)
    chk = ["5 verbos reflexivos (me levanto…)", "la hora (a las siete)", "conectores (primero, luego…)", "la frecuencia (siempre, a veces)", "un gusto (me gusta… porque…)", "cómo estás (estoy…)"]
    x = Inches(6.9); y = Inches(1.7)
    text(s, x, y, Inches(6), Inches(0.4), [[("Checklist:", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    for i, c in enumerate(chk):
        text(s, x, y + Inches(0.5) + i * Inches(0.45), Inches(6), Inches(0.4), [[("☐  " + c, {"size": 13, "color": INK})]])
    rev = card(s, x, Inches(4.35), Inches(6.0), Inches(1.25), fill=GT, line=G, lw=1.2)
    text(s, x + Inches(0.15), Inches(4.4), Inches(5.7), Inches(1.2),
         [[("Modelo: ", {"size": 12, "bold": True, "color": GD}),
           ("«Normalmente me levanto a las siete. Primero me ducho, luego desayuno. Como a las dos. Por la tarde me gusta bailar porque es divertido. Me acuesto a las once. Hoy estoy contento.»", {"size": 11.5, "italic": True, "color": INK})]], line=1.14)
    register_reveal(s, rev)
    noodroute(s); foot(s)
    notes(s, "TEACHER · WRITING (luisteren→schrijven). Checklist = zichtbare steun; onthul het model pas na het schrijven (retrieval). "
             "Nakijkfocus: reflexivos correct, la hora, ser/estar, gustar, één opinión met porque. Dit voedt de Tarea «Mi día a día».")

# ============================================================ DIA 15 · VOCAB — la hora + sentimientos (reveal)
def s15_hora():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · VOCABULARIO", "La hora y los sentimientos", "Klik een kaart → la respuesta. Bouw je woordnetwerk.", num=1)
    data = [("Es la una", "1:00"), ("Son las dos", "2:00"), ("y cuarto", ":15"), ("y media", ":30"),
            ("menos cuarto", ":45"), ("en punto", "op het uur"), ("contento", "blij"), ("cansado", "moe"),
            ("nervioso", "nerveus"), ("aburrido", "verveeld"), ("¿qué hora es?", "hoe laat is het?"), ("¿a qué hora?", "om hoe laat?")]
    x0, y0 = Inches(0.5), Inches(1.7); cw = Inches(3.0); rh = Inches(0.7)
    for i, (es, nl) in enumerate(data):
        c = i % 4; r = i // 4; x = x0 + c * (cw + Inches(0.1)); y = y0 + r * (rh + Inches(0.14))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.12), y, Inches(1.8), rh, [[(es, {"size": 12, "bold": True, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(1.9), y, cw - Inches(2.0), rh, [[("→ " + nl, {"size": 11.5, "color": G})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.9),
             [[("La hora: ", {"bold": True, "color": GD}), ("es la una (1) · son las + 2,3… · y cuarto/y media/menos cuarto. ¿A qué hora? → A las siete.", {"color": GD})],
              [("Sentimientos: estar + adjetivo (estoy contento/cansado). Concordancia: contento/contenta.", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCAB la hora + sentimientos. Klik onthult; koppel la hora aan de rutina en estar aan de sentimientos. Online: dictado de horas + ¿cómo estás? (memory).")

# ============================================================ DIA 16 · TALLER — sílaba tónica + conectores
def s16_taller():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "TALLER DE LENGUA", "Sílaba tónica + conectores", "Klik een item → correcte vorm. Gereedschap voor uitspraak en verbinden.", num=1)
    text(s, Inches(0.5), Inches(1.5), Inches(6), Inches(0.35), [[("A · acento en los reflexivos", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    fixes = [("me DU-cho", "llana (voorlaatste)"), ("se des-PIER-ta", "llana"), ("des-per-TAR", "aguda"), ("MIÉR-co-les", "esdrújula (tilde!)")]
    y = Inches(1.95)
    for q, a in fixes:
        card(s, Inches(0.5), y, Inches(6.0), Inches(0.6), fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, Inches(0.62), y, Inches(2.6), Inches(0.6), [[(q, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, Inches(3.3), y, Inches(3.1), Inches(0.6), [[("→ " + a, {"size": 12, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y = y + Inches(0.72)
    text(s, Inches(6.9), Inches(1.5), Inches(6), Inches(0.35), [[("B · conectores: primero · luego · después · porque", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    conn = [("___ me levanto, ___ me ducho.", "primero … luego"), ("___ desayuno.", "después"),
            ("Me gusta el finde ___ no hay clase.", "porque"), ("___, me acuesto.", "por último")]
    y = Inches(1.95)
    for q, a in conn:
        card(s, Inches(6.9), y, Inches(5.9), Inches(0.6), fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, Inches(7.02), y, Inches(4.0), Inches(0.6), [[(q, {"size": 10.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, Inches(11.1), y, Inches(1.6), Inches(0.6), [[("→ " + a, {"size": 10.5, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y = y + Inches(0.72)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.85),
             [[("A: ", {"bold": True, "color": GD}), ("de meeste reflexieve vormen zijn llana (me DU-cho); draagt het een tilde, volg de tilde.", {"color": GD})],
              [("🔴 B: ", {"bold": True, "color": RED}), ("«want» én «omdat» = porque · «dus» = así que/por eso.", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · TALLER. Sílaba tónica in reflexieve vormen; porque = kernvalstrik NL. Online: drills in de hub.")

# ============================================================ DIA 17 · CULTURE — el horario español
def s17_cultura():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "CULTURA · PARADA 1: ESPAÑA", "El horario español", "Klik een kaart → het weetje verschijnt. Un día hispano tiene su ritmo.", num=1)
    cards = [("🍽️ Se come tarde", "In España is la comida (lunch) de hoofdmaaltijd, om 14–15u. La cena is licht en laat: 21–22u. Desayuno = klein.", "la comida ≠ el desayuno"),
             ("😴 La siesta — mito y realidad", "Na de comida rusten sommigen even (la siesta), vooral in kleine steden en de zomer. In grote steden bijna niemand meer.", "geen siesta voor iedereen"),
             ("🌎 No es igual en todo el mundo", "In México eet men ook rond 14–15u maar ontbijt steviger. In veel LatAm-landen eet men vroeger dan in España.", "un día hispano ≠ un solo horario")]
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
             [[("Actividad: ", {"bold": True, "color": GD}), ("compara tu horario con el de España. ¿A qué hora comes tú? ¿Y cenas?", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · CULTURE (identiteit in diversiteit, LPD 5). Onthul per kaart. Bruggetje naar La Ruta (parada 1 = España). "
             "Online: vergelijk het horario van Lucía (Sevilla) en Diego (CDMX).")

# ============================================================ DIA 18 · FINAL_MISSION — Mi día a día
def s18_tarea():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(1.35), fill=GD)
    text(s, Inches(0.5), Inches(0.18), Inches(9), Inches(1.0),
         [[("🗓️ Tarea final · Mi día a día", {"size": 28, "bold": True, "color": WHITE, "font": DISPLAY})],
          [("Maak je dagblog voor de klasmuur y preséntalo en pareja.", {"size": 13, "italic": True, "color": GT})]])
    avatar(s, "mochila", Inches(11.6), Inches(0.2), Inches(1.0))
    pasos = [("1", "Planifica", "6–8 acciones + la hora (me levanto a las…)"),
             ("2", "Escribe tu blog", "6–8 frases: reflexivos + conectores + hora + frecuencia"),
             ("3", "Añade gustos y ánimo", "«me gusta… porque…» y «por la mañana estoy…»"),
             ("4", "Preséntalo en pareja", "lee en voz alta; tu compañero/a anota una hora y pregunta"),
             ("5", "Graba tu presentación", "en la web (recorder) — escúchate y mejora")]
    y = Inches(1.7)
    for n, es, nl in pasos:
        b = rect(s, Inches(0.5), y, Inches(0.5), Inches(0.5), fill=G, round=True, radius=0.5)
        tf = b.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE; p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        rr = p.add_run(); rr.text = n; rr.font.size = Pt(15); rr.font.bold = True; rr.font.name = DISPLAY; rr.font.color.rgb = WHITE
        text(s, Inches(1.2), y, Inches(4.2), Inches(0.55), [[(es, {"size": 14, "bold": True, "color": GD, "font": DISPLAY})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, Inches(5.5), y, Inches(7.2), Inches(0.55), [[(nl, {"size": 11.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        y = y + Inches(0.62)
    text(s, Inches(0.5), Inches(5.0), Inches(12), Inches(0.35), [[("Rúbrica · ¿lo logré?", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    crit = ["5 verbos reflexivos", "la hora + conectores", "ser/estar + gustar", "una opinión (porque)"]
    x = Inches(0.5)
    for c in crit:
        chip(s, x, Inches(5.45), "☐ " + c, fill=GT, tcolor=GD, size=10, w=Inches(3.05)); x = x + Inches(3.15)
    text(s, Inches(0.5), Inches(6.05), Inches(12), Inches(0.4),
         [[("🎯 ", {"size": 12}), ("Afzender jij · ontvanger de klas (el muro) · doel je dag delen · situatie het begin van het jaar · resultaat: blog + presentación oral.", {"size": 11.5, "italic": True, "color": MUT})]])
    foot(s)
    notes(s, "TEACHER · FINAL_MISSION (communicatieve eindtaak). Afzender/ontvanger/doel/situatie/resultaat expliciet. Beoordeel met de rúbrica; "
             "opname + zelfevaluatie op de digitale pagina.")

# ============================================================ DIA 19 · QUIZ — la mezcla (retrieval)
def s19_mezcla():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "QUIZ · LA MEZCLA", "Ophaal door elkaar", "Gemengde ophaal van de hele unit. Klik een vraag → het antwoord. (retrieval)", num=1)
    items = [("yo (levantarse)", "me levanto"), ("tú (ducharse)", "te duchas"), ("nosotros (acostarse)", "nos acostamos"),
             ("Lucía ___ de Sevilla (ser/estar)", "es"), ("Hoy ___ cansado (ser/estar)", "estoy"),
             ("Me ___ los perros (gusta/gustan)", "gustan"), ("A Diego ___ gusta el fútbol (pron.)", "le"), ("3:30 = son las tres…", "y media")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.62)
    for i, (q, a) in enumerate(items):
        c = i // 4; r = i % 4; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.16))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(4.0), rh, [[(q, {"size": 11.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.15), y, cw - Inches(4.3), rh, [[("→ " + a, {"size": 12, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.05), Inches(12.3), Inches(0.55),
             [[("Alles komt terug: ", {"bold": True, "color": GD}), ("reflexivos · ser/estar · gustar + OI · la hora · «me gusta… porque».", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ mezcla (retrieval vóór herlezen). Zonder waarschuwing door elkaar. Exit-ticket. Zwakke punten → terug via menu.")

# ============================================================ DIA 20 · FEEDBACK/REPASO
def s20_repaso():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "REPASO · LO ESENCIAL", "Lo esencial de un vistazo", "De volledige herhaling (13 spellen, drills) staat online. Hier: de kern + semáforo.", num=1)
    ess = ["La hora: es la una · son las dos… · y cuarto/y media/menos cuarto · A las siete me levanto.",
           "Reflexivos: pronombre (me·te·se·nos·os·se) + verbo. Cambio vocálico: me despierto, me acuesto, me visto.",
           "Ser vs estar: ser = identiteit/karakter (soy simpático) · estar = plaats/gevoel (estoy cansado). es aburrido ≠ está aburrido.",
           "Gustar + OI: me/te/le/nos/os/les + gusta (1/inf.) / gustan (varios). ¡Al revés!",
           "🔴 Trampas: nunca «yo gusto» · me gusta el fútbol (lidwoord) · me/te/se bij reflexief · a mí también (niet yo también)."]
    card(s, Inches(0.5), Inches(1.6), Inches(12.3), Inches(2.5), fill=CREMA, line=None)
    y = Inches(1.8)
    for e in ess:
        text(s, Inches(0.8), y, Inches(11.8), Inches(0.45), [[("• ", {"size": 13, "bold": True, "color": GD}), (e, {"size": 12, "color": INK})]])
        y = y + Inches(0.46)
    text(s, Inches(0.5), Inches(4.3), Inches(12), Inches(0.35), [[("Semáforo — ¿cómo lo llevas?", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    can = ["de hora zeggen", "mijn rutina met reflexivos vertellen", "ser vs estar contrasteren", "gustar + OI gebruiken", "una opinión con «me gusta… porque»"]
    y = Inches(4.75)
    for c in can:
        text(s, Inches(0.8), y, Inches(7.0), Inches(0.4), [[(c, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        for j, (em, col) in enumerate([("🔴", RED), ("🟠", AMBER), ("🟢", G)]):
            chip(s, Inches(8.0) + j * Inches(1.5), y + Inches(0.03), em + " ", fill=WHITE, tcolor=col, size=12, w=Inches(1.3))
        y = y + Inches(0.42)
    foot(s)
    notes(s, "TEACHER · FEEDBACK/REPASO. Semáforo = zelfevaluatie. Repaso-drills online (13 spellen). Bruggetje: U2 «Aquí vivo» — "
             "wonen, de buurt, hay/estar en lo/la.")

# ============================================================ DIA 21 · TEACHER_NOTES
def s21_teacher():
    s = slide(); bg(s, GD)
    text(s, Inches(0.6), Inches(0.4), Inches(12), Inches(0.8), [[("TEACHER_NOTES · U1 «El día a día»", {"size": 26, "bold": True, "color": WHITE, "font": DISPLAY})]])
    blocks = [("Timing (50 min)", "Menu 2' · la hora 6' · rutina 6' · reflexivos 12' · ser/estar 8' · gustar 8' · lectura/escucha 5' · Tarea-briefing 3'."),
              ("Kernvalstrikken", "nunca «yo levanto» (reflexief = me/te/se + verbo) · gustar «al revés» (me gusta la música, nunca yo gusto) · me gusta + el/la (lidwoord verplicht) · es aburrido (saai) ≠ está aburrido (verveelt zich) · a mí también (niet yo también)."),
              ("Differentiatie", "Sterker: volledige rutina + gustos + opinión met porque + 3ª persoon (mijn buur). Zwakker: reflexief-tabel + ser/estar-kaart langer open, frames houden; gustar met vaste chunks (me gusta / me gustan)."),
              ("Digitaal", "13 spellen + flip cards + gramática interactiva (reflexivos/ser-estar/gustar) + recorder (Hablar) + Lectura (dos perfiles) op de página digital. QR's in het boek → juiste anker. Conjugador = aparte tool."),
              ("Evaluatie & LPD", "Tarea «Mi día a día» met rúbrica (4 criteria). LPD (III-Spa-d): rutina/reflexivos 8·3 · la hora 8·7 · ser/estar 8·7 · gustar 8·7 · lezen 1·2·5 · cultuur 5 · spreken/interactie 3·4. Bron: oude cursus U3/U4 + reservoir.")]
    y = Inches(1.4)
    for t, b in blocks:
        card(s, Inches(0.5), y, Inches(12.3), Inches(1.0), fill=RGBColor(0x47, 0x30, 0x69), line=None)
        text(s, Inches(0.75), y + Inches(0.08), Inches(11.8), Inches(0.4), [[(t, {"size": 14, "bold": True, "color": WHITE, "font": DISPLAY})]])
        text(s, Inches(0.75), y + Inches(0.48), Inches(11.8), Inches(0.5), [[(b, {"size": 11, "color": GT})]], line=1.1)
        y = y + Inches(1.12)
    footer(s, tab=TAB, page=pg())
    notes(s, "Alleen in het docentdeck. Volledige LPD-dekking en didactische route staan in het cursusdossier (cocktail + outline). Échte LPD-codes uit EELP-U3/U4.")

# ============================================================ RUN + BUILD
def _run_all(include_teacher=True):
    s01_title(); s02_menu(); s03_vocab(); s04_reflexivos(); s05_reflexivos_quiz(); s06_conjugacion(); s07_serestar()
    s08_serestar_quiz(); s09_reading(); s10_listening(); s11_gustar(); s12_gustar_quiz(); s13_speaking(); s14_writing()
    s15_hora(); s16_taller(); s17_cultura()
    # Lectura en Escucha uit de gedeelde bron — zelfde inhoud als print en hub.
    E.s_lectura(_LD.C6P_U1); E.s_escucha(_ED.C6P_U1)
    s18_tarea(); s19_mezcla(); s20_repaso()
    if include_teacher:
        s21_teacher()

def _repaint(path):
    """Kogelvrije nabewerking: elke resterende engine-groen -> paars, en foute footer-tekst fixen."""
    import zipfile, os as _os
    reps = [("1E9E74", "7C56A9"), ("1e9e74", "7c56a9"), ("2EB085", "9374C2"), ("2eb085", "9374c2"),
            ("C5 · A1 · La Ruta", "C6+ · el día a día")]
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
