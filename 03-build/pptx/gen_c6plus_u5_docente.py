#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_c6plus_u5_docente.py — Interactieve PowerPoint C6+ · Unidad 5 «Érase una vez»
=================================================================================
Zelfde engine/pijplijn als de golden sample (gen_u0_docente = de engine). Cursuskleur = PAARS.
Twee decks (.pptx): docente (oplossingen + notities) + alumno (F5, klik onthult).
Grammatica: pretérito indefinido (regular + fuertes) · OD+OI juntos (se lo).
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
OUT_DOCENTE = os.path.join(HERE, "C6plus_U5_docente.pptx")
OUT_ALUMNO_PPTX = os.path.join(HERE, "C6plus_U5_alumno.pptx")
TAB = "U5 · ÉRASE UNA VEZ"

def foot(s): footer(s, tab=TAB, page=pg())

# ============================================================ DIA 1 · TITLE
def s01_title():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(4.7), fill=G)
    rect(s, 0, Inches(4.7), EMU_W, Inches(0.09), fill=GD)
    text(s, Inches(0.6), Inches(0.35), Inches(3.4), Inches(3.6),
         [[("5", {"size": 260, "bold": True, "color": RGBColor(0x93, 0x74, 0xC2), "font": DISPLAY})]], anchor=MSO_ANCHOR.MIDDLE)
    chip(s, Inches(4.35), Inches(0.85), "LA RUTA · BUENOS AIRES 🇦🇷 · ÉRASE UNA VEZ 📖", fill=WHITE, tcolor=GD, size=12)
    text(s, Inches(4.3), Inches(1.35), Inches(8.6), Inches(1.5), [[("Érase una vez", {"size": 54, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(4.35), Inches(2.7), Inches(8.4), Inches(0.6),
         [[("Biografías y relatos: el pretérito indefinido (fue, hizo) · se lo/se la.", {"size": 15, "italic": True, "color": GT})]])
    text(s, Inches(4.35), Inches(3.35), Inches(8.4), Inches(0.9),
         [[("¿A qué persona famosa admiras?", {"size": 22, "bold": True, "color": WHITE, "font": DISPLAY})],
          [("Welke beroemde persoon bewonder je?", {"size": 13, "italic": True, "color": GT})]])
    text(s, Inches(0.6), Inches(4.95), Inches(6), Inches(0.4),
         [[("La gente de la ruta — parada 5: Buenos Aires (Mateo · voseo)", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    x = Inches(0.6)
    for nm, city in [("diego","CDMX 🇲🇽"),("valen","Cartagena 🇨🇴"),("nina","Cusco 🇵🇪"),
                     ("mateo","BsAs 🇦🇷"),("tu","Tú · Flandes 🇧🇪"),("mochila","La mochila")]:
        avatar(s, nm, x, Inches(5.4), Inches(1.0))
        text(s, x - Inches(0.15), Inches(6.42), Inches(1.3), Inches(0.5),
             [[(nm.capitalize() if nm != "tu" else "Tú", {"size": 10.5, "bold": True, "color": INK})],
              [(city.split("·")[-1].strip() if nm != "tu" else "de reiziger = jij", {"size": 8.5, "color": MUT})]], align=PP_ALIGN.CENTER)
        x = x + Inches(2.05)
    foot(s)
    notes(s, "TEACHER · TITLE. U5 = de kern-verleden tijd. Kerngrammatica: pretérito indefinido (regular + fuertes: fue/hizo/tuvo/estuvo/dijo) + se lo/se la. "
             "Parada 5 = Buenos Aires (Mateo, voseo). Kernvalstrikken: indefinido = afgeronde feiten (ayer, en 1919) ≠ perfecto · hizo (z) · fue = ser én ir · le lo → se lo. "
             "Docentdeck = oplossing; leerlingdeck (.pptx, F5) = klik onthult.")

# ============================================================ DIA 2 · MENU
def s02_menu():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "MENÚ DE LA LECCIÓN", "El mapa de la Unidad 5",
               "Kies je route — klik een tegel. Alles oefent naar de Tarea «Una biografía» toe.", num=5)
    tiles = [
        ("§1", "Biografía", "y logros", G, 3),
        ("§2", "Indefinido", "regular", G, 4),
        ("§2b", "Fuertes", "fue · hizo · tuvo", G, 6),
        ("§3", "Se lo / se la", "OD + OI", G, 7),
        ("§4", "Contar", "una historia", G, 11),
        ("★", "Lectura + escucha", "una vida de película", GD, 9),
        ("🎭", "Cultura", "figuras hispanas", GD, 17),
        ("📖", "Tarea · Biografía", "vida + opinión", GD, 18),
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
        text(s, x + Inches(0.58), y + Inches(0.06), tw - Inches(0.7), Inches(0.4), [[(es, {"size": 14.5, "bold": True, "color": WHITE, "font": DISPLAY})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(0.18), y + Inches(0.68), tw - Inches(0.36), Inches(1.2), [[(nl, {"size": 11.5, "color": INK})]], line=1.12)
        chip(s, x + Inches(0.18), y + th - Inches(0.45), f"→ dia {dia}", fill=GT, tcolor=GD, size=9.5)
    foot(s)
    notes(s, "TEACHER · LESSON_MENU. Kern = §2 indefinido + §3 se lo. Kruisverwijzing: «oefen online — 12 juegos + 100+ oefeningen».")

# ============================================================ DIA 3 · VOCAB
def s03_vocab():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · VOCABULARIO", "Biografía y logros", "De woorden van een leven — observa. Herken ze, dan gebruik je ze.", num=1)
    legend_func(s, Inches(9.7), Inches(0.55))
    rows = [("nacer", "geboren worden", "en 1927"), ("crecer", "opgroeien", "en un pueblo"),
            ("casarse", "trouwen", "joven"), ("morir", "sterven", "en 1954"),
            ("ganar", "winnen", "un premio"), ("escribir", "schrijven", "novelas"),
            ("el escritor", "de schrijver", "el pintor, el cantante"), ("famoso", "beroemd", "un icono")]
    x0, y0 = Inches(0.5), Inches(1.6); cw = Inches(6.1); rh = Inches(0.6)
    for i, (k, v, nl) in enumerate(rows):
        c = 0 if i < 4 else 1; r = i % 4
        x = x0 + c * (cw + Inches(0.15)); y = y0 + r * (rh + Inches(0.12))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(2.4), rh, [[(k, {"size": 13, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(2.5), y, Inches(2.1), rh, [[(v, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(4.5), y, Inches(1.5), rh, [[(nl, {"size": 9, "italic": True, "color": MUT})]], anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(4.75), Inches(12.3), Inches(0.5),
         [[("Woordfamilie: ", {"size": 13, "bold": True, "color": GD, "font": DISPLAY}),
           ("escribir → el escritor · pintar → el pintor · cantar → el cantante. Het beroep zit in de actie.", {"size": 13, "color": INK})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.35), Inches(12.3), Inches(0.95),
             [[("Etapas: ", {"bold": True, "color": GD}), ("nacer → crecer → estudiar → casarse → morir. Logros: ganar, escribir, pintar, componer, descubrir.", {"color": GD})],
              [("Personas: el escritor, la pintora, el cantante, el futbolista, el científico.", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCABULARY. Laat de biografiewoorden raden. Koppel persona → logro. Online: memoria de la vida + memoria de oficios.")

# ============================================================ DIA 4 · GRAMMAR indefinido (color)
def s04_indef():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · GRAMÁTICA VISUAL", "El pretérito indefinido (regular)", "-ar → é/aste/ó… · -er/-ir → í/iste/ió… voor afgeronde feiten.", num=2)
    legend_func(s, Inches(9.7), Inches(0.55))
    seg = [("García Márquez ", F_SUBJ), ("escribió ", F_VERB), ("novelas ", F_OBJ), ("en 1967", F_TIME)]
    runs = [[(t, {"size": 20, "bold": True, "color": c, "font": DISPLAY}) for t, c in seg]]
    card(s, Inches(0.5), Inches(1.7), Inches(12.3), Inches(1.2), fill=GT, line=None)
    text(s, Inches(0.8), Inches(1.7), Inches(11.7), Inches(1.2), runs, anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(3.15), Inches(12), Inches(0.4), [[("Las terminaciones", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    frame = [("yo -é / -í", "hablé / comí"), ("tú -aste / -iste", "hablaste / comiste"), ("él -ó / -ió", "habló / comió"),
             ("nos. -amos / -imos", "hablamos / comimos"), ("vos. -asteis / -isteis", "hablasteis"), ("ellos -aron / -ieron", "hablaron / comieron")]
    x0, y0 = Inches(0.5), Inches(3.6); cw = Inches(4.0); rh = Inches(0.62)
    for i, (a, b) in enumerate(frame):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.12))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(2.1), rh, [[(a, {"size": 10.5, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(2.25), y, cw - Inches(2.4), rh, [[(b, {"size": 10, "color": F_VERB, "bold": True})]], anchor=MSO_ANCHOR.MIDDLE)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.75), Inches(12.3), Inches(0.6),
             [[("Regla: ", {"bold": True, "color": GD}), ("de klemtoon staat op de uitgang: hablé, habló, comí, comió. -er en -ir zijn identiek. Marker: ayer, en 1967.", {"color": GD})]],
             trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR indefinido. Toon raíz + uitgang. Online: completa el indefinido (cloze) + indefinido Tetris.")

# ============================================================ DIA 5 · QUIZ indefinido (reveal)
def s05_indef_quiz():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · QUIZ", "¿Qué forma del indefinido?", "Klik een zin → de juiste vorm.", num=2)
    items = [("(Él) ___ (nacer) en 1927.", "nació"), ("(Ella) ___ (pintar).", "pintó"),
             ("Messi ___ (ganar).", "ganó"), ("(Yo) ___ (estudiar).", "estudié"),
             ("Nosotros ___ (comer).", "comimos"), ("¿(Tú) ___ (viajar)?", "viajaste")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.78)
    for i, (q, a) in enumerate(items):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(4.0), rh, [[(q, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.2), y, cw - Inches(4.3), rh, [[("→ " + a, {"size": 12.5, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Truc: ", {"bold": True, "color": RED}), ("-ar → é/ó · -er/-ir → í/ió. Klemtoon op de uitgang.", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ indefinido (retrieval). Klas roept de vorm vóór de klik. Online: cloze el indefinido.")

# ============================================================ DIA 6 · GRAMMAR fuertes (reveal)
def s06_fuertes():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2b · GRAMÁTICA", "Los pretéritos fuertes", "Klik een verbo → de él-vorm. Uit het hoofd leren.", num=2)
    items = [("ser / ir", "fue"), ("hacer", "hizo"), ("tener", "tuvo"), ("estar", "estuvo"),
             ("decir", "dijo"), ("venir", "vino"), ("dar", "dio"), ("ver", "vio")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.72)
    for i, (q, a) in enumerate(items):
        c = i // 4; r = i % 4; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.14))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(2.6), rh, [[(q, {"size": 12.5, "color": MUT})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(2.8), y, cw - Inches(2.9), rh, [[("→ " + a, {"size": 14, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.85), Inches(12.3), Inches(0.85),
             [[("Sin acento: ", {"bold": True, "color": GD}), ("fue · hizo · tuvo · estuvo · dijo · vino · dio · vio.", {"color": GD})],
              [("🔴 hizo (z) · fue = ser én ir (Fue médico / Fue a París).", {"color": RED})]], trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR fuertes. Coro vóór de klik. Online: ¿regular o irregular? (classify) + indefinido Tetris.")

# ============================================================ DIA 7 · GRAMMAR se lo (color)
def s07_selo():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · GRAMÁTICA VISUAL", "Los pronombres juntos — se lo / se la", "le/les + lo/la → se lo/se la. Twee voornaamwoorden na elkaar.", num=3)
    legend_func(s, Inches(9.7), Inches(0.55))
    card(s, Inches(0.5), Inches(1.7), Inches(12.3), Inches(1.1), fill=GT, line=None)
    text(s, Inches(0.8), Inches(1.7), Inches(11.7), Inches(1.1),
         [[("Di el libro ", {"size": 16, "color": INK}), ("a Mateo ", {"size": 16, "bold": True, "color": F_PLAC}),
           ("→ ", {"size": 16, "color": MUT}), ("Le ", {"size": 16, "color": F_PLAC}), ("lo ", {"size": 16, "color": F_OBJ}),
           ("di → ", {"size": 16, "color": MUT}), ("Se ", {"size": 18, "bold": True, "color": F_PLAC}), ("lo ", {"size": 18, "bold": True, "color": F_OBJ}), ("di.", {"size": 16, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
    frame = [("le/les + lo", "se lo"), ("le/les + la", "se la"), ("le/les + los", "se los"), ("le/les + las", "se las")]
    x0, y0 = Inches(0.5), Inches(3.15); cw = Inches(6.0); rh = Inches(0.62)
    for i, (a, b) in enumerate(frame):
        c = i % 2; r = i // 2; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.14))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(2.3), rh, [[(a, {"size": 12, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(2.5), y, cw - Inches(2.6), rh, [[("→ " + b, {"size": 13, "color": F_OBJ, "bold": True})]], anchor=MSO_ANCHOR.MIDDLE)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.75), Inches(12.3), Inches(0.9),
             [[("Regla: ", {"bold": True, "color": GD}), ("als le/les + lo/la samenkomen → le/les wordt se. Volgorde: se + lo/la + werkwoord. ", {"color": GD})],
              [("Bij infinitivo: dárselo = se lo voy a dar.", {"color": GD})]], trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR se lo. Toon le+lo → se lo. Online: completa se lo/se la (cloze) + vervangingsanimatie.")

# ============================================================ DIA 8 · QUIZ se lo (reveal)
def s08_selo_quiz():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · QUIZ", "¿se lo, se la, se los o se las?", "Klik een pregunta → de respuesta.", num=3)
    items = [("¿El libro a Mateo?", "Se lo di"), ("¿La carta a Nina?", "Se la mandé"),
             ("¿Los discos a Diego?", "Se los presté"), ("¿Las fotos a Valen?", "Se las enseñé"),
             ("¿El secreto a ella?", "Se lo conté"), ("¿La noticia a él?", "Se la dije")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.78)
    for i, (q, a) in enumerate(items):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(3.6), rh, [[(q, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(3.8), y, cw - Inches(3.9), rh, [[("→ " + a, {"size": 12.5, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Concordancia OD: ", {"bold": True, "color": GD}), ("el→lo · la→la · los→los · las→las. Altijd «se» als OI vooraan.", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ se lo (retrieval). Klas roept vóór de klik. Online: cloze se lo/se la.")

# ============================================================ DIA 9 · READING
def s09_reading():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§5 · LEER · COMPRENSIÓN", "Dos vidas — «Una vida de película»", "Lees. Klik een vraag → het antwoord verschijnt.", num=5)
    card(s, Inches(0.5), Inches(1.65), Inches(5.6), Inches(3.9), fill=GT, line=G, lw=1.4)
    avatar(s, "mateo", Inches(0.85), Inches(1.95), Inches(1.0))
    text(s, Inches(2.05), Inches(1.98), Inches(3.9), Inches(1.5),
         [[("«Frida Kahlo nació en México en 1907. Tuvo un accidente y empezó a pintar. Pintó autorretratos, se casó con Diego Rivera y fue una artista única. Murió en 1954.»", {"size": 11, "italic": True, "color": INK})]], line=1.16)
    avatar(s, "mateo", Inches(0.85), Inches(3.65), Inches(1.0))
    text(s, Inches(2.05), Inches(3.68), Inches(3.9), Inches(1.5),
         [[("«Lionel Messi nació en Rosario en 1987. Jugó en un equipo local, se mudó a Barcelona, ganó muchos títulos y en 2022 fue campeón del Mundo. Hizo historia.»", {"size": 11, "italic": True, "color": INK})]], line=1.16)
    qa = [("¿Cuándo nació Frida?", "En 1907"), ("¿Con quién se casó?", "Con Diego Rivera"),
          ("¿Dónde nació Messi?", "En Rosario"), ("¿Qué ganó en 2022?", "El Mundial")]
    x = Inches(6.4); y = Inches(1.7)
    for q, a in qa:
        card(s, x, y, Inches(6.4), Inches(0.85), fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y + Inches(0.06), Inches(6.1), Inches(0.4), [[(q, {"size": 12.5, "bold": True, "color": GD})]])
        rev = text(s, x + Inches(0.15), y + Inches(0.44), Inches(6.1), Inches(0.35), [[("→ " + a, {"size": 12, "color": INK})]])
        register_reveal(s, rev); y = y + Inches(0.98)
    btn = noodroute(s)
    exercise_solucion(s, Inches(6.4), Inches(5.65), Inches(6.4), Inches(0.6),
             [[("🎯 Leesdoel: ", {"bold": True, "color": GD}), ("scannen naar het indefinido (nació, ganó…) + datums.", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · READING (lezen→schrijven, LPD 6). Eerst globaal, dan scannen. Daarna: eigen minibiografie met el indefinido.")

# ============================================================ DIA 10 · LISTENING
def s10_listening():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · ESCUCHAR · INTERACCIÓN", "¿Quién fue…?", "Volg de minibiografie. Klik un dato → de info. (audio + script op de web)", num=2)
    pasos = [("🔊 ¿Dónde nació?", "En Rosario, 1987"), ("🔊 ¿Qué hizo de joven?", "Jugó al fútbol"),
             ("🔊 ¿Qué logró?", "Ganó el Mundial"), ("🔊 ¿Quién es?", "¡Messi!")]
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
               ("«Nació en Rosario en 1987. De niño jugó al fútbol. Ganó muchos títulos y fue campeón del Mundo. ¿Quién es?» ", {"color": GD})],
              [("Daarna: A beschrijft een figuur, B raadt (info-gap).", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · LISTENING (luisteren→spreken). Lees voor (of TTS); klas raadt. Daarna adivina el personaje in parejas. Online: ¿quién fue? (audio).")

# ============================================================ DIA 11 · GRAMMAR conectores/marcadores (reveal)
def s11_conectores():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · GRAMÁTICA", "Marcadores y conectores del relato", "Klik een cue → de betekenis. Ordena la historia.", num=4)
    items = [("gisteren", "ayer"), ("in 1919", "en 1919"), ("vorig jaar", "el año pasado"), ("plots", "de repente"),
             ("er was eens", "érase una vez"), ("eerst / daarna", "primero / después"), ("toen / dus", "entonces"), ("uiteindelijk", "al final")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.72)
    for i, (q, a) in enumerate(items):
        c = i // 4; r = i % 4; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.14))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(2.6), rh, [[(q, {"size": 12, "color": MUT})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(2.8), y, cw - Inches(2.9), rh, [[("→ " + a, {"size": 13, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.85), Inches(12.3), Inches(0.85),
             [[("Estructura: ", {"bold": True, "color": GD}), ("Érase una vez… Primero nació… Después estudió… Entonces triunfó… Al final murió famoso.", {"color": GD})],
              [("De markers (ayer, en 1919, el año pasado) horen bij het indefinido.", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR conectores. Structuur van een biografie. Online: ordena la biografía (order).")

# ============================================================ DIA 12 · QUIZ mezcla (reveal)
def s12_mezcla_ind():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2–§3 · QUIZ", "Indefinido + fuertes + se lo", "Klik → de juiste vorm.", num=2)
    items = [("hacer → él", "hizo"), ("ser/ir → él", "fue"), ("tener → yo", "tuve"),
             ("escribir → él", "escribió"), ("¿El libro a él? ___ di", "se lo"), ("¿Las fotos a ella? ___ mandé", "se las")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.78)
    for i, (q, a) in enumerate(items):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(4.0), rh, [[(q, {"size": 11.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.2), y, cw - Inches(4.3), rh, [[("→ " + a, {"size": 12.5, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Fuertes: ", {"bold": True, "color": G}), ("fue · hizo · tuvo · estuvo · dijo · vino · dio. Se lo = le/les + lo.", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ mezcla (retrieval). Door elkaar. Online: cloze + indefinido Tetris.")

# ============================================================ DIA 13 · SPEAKING
def s13_speaking():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · SPEAKING · INTERACCIÓN", "Cuenta una biografía", "Speel de scène met de frames. Steun bouwt af: kaarten → beginwoorden → uit het hoofd.", num=2)
    avatar(s, "tu", Inches(11.4), Inches(1.7), Inches(1.3))
    labels = ["¿Dónde/cuándo?", "De joven…", "¿Qué logró?", "¿Y después?", "Al final…", "Tu opinión"]
    frames = ["Nació en… en (año)", "Estudió / jugó…", "Ganó / escribió…", "Después…", "Murió en…", "Creo que fue…"]
    x0, y0 = Inches(0.5), Inches(1.8); cw = Inches(3.4); rh = Inches(0.8)
    for i, (lab, fr) in enumerate(zip(labels, frames)):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=G, lw=1.2, shadow=False)
        text(s, x + Inches(0.15), y + Inches(0.05), cw - Inches(0.3), Inches(0.32), [[(lab, {"size": 10, "color": MUT})]])
        text(s, x + Inches(0.15), y + Inches(0.36), cw - Inches(0.3), Inches(0.4), [[(fr, {"size": 12, "bold": True, "color": GD, "font": DISPLAY})]])
    chip(s, Inches(0.5), Inches(4.65), "🎙️ Grábate online · «Mensaje de voz: una biografía / mi opinión»", fill=GT, tcolor=GD, size=11)
    text(s, Inches(0.5), Inches(5.05), Inches(10.5), Inches(0.9),
         [[("Ronda 1: ", {"size": 12, "bold": True, "color": GD}), ("met de kaarten. ", {"size": 12, "color": INK}),
           ("Ronda 2: ", {"size": 12, "bold": True, "color": GD}), ("beginwoorden. ", {"size": 12, "color": INK}),
           ("Ronda 3: ", {"size": 12, "bold": True, "color": GD}), ("uit het hoofd. ", {"size": 12, "color": INK}),
           ("Ronda 4: ", {"size": 12, "bold": True, "color": GD}), ("grábate.", {"size": 12, "color": INK})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.6), Inches(12.3), Inches(0.65),
             [[("Modelo: ", {"bold": True, "color": GD}), ("«Frida Kahlo nació en México en 1907. Tuvo un accidente y empezó a pintar. Pintó autorretratos. Murió en 1954. Creo que fue una artista genial porque cambió el arte.»", {"color": GD})]],
             trigger=btn, title_doc="MODELO · docent")
    foot(s)
    notes(s, "TEACHER · SPEAKING (interactie). Rondes met afbouwende steun. Online: recorder (una biografía + mi opinión).")

# ============================================================ DIA 14 · WRITING
def s14_writing():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "WRITING · PRODUCCIÓN", "Una biografía", "Schrijf een biografie. Klik → een modeltekst verschijnt.", num=5)
    card(s, Inches(0.5), Inches(1.7), Inches(6.0), Inches(3.9), fill=WHITE, line=LINE, lw=1.2)
    text(s, Inches(0.7), Inches(1.85), Inches(5.6), Inches(0.4), [[("✍️ Escribe tu biografía:", {"size": 12, "bold": True, "color": GD})]])
    for i in range(6):
        rect(s, Inches(0.7), Inches(2.4) + i * Inches(0.5), Inches(5.6), Inches(0.01), fill=LINE)
    chk = ["datos (nació en… en año)", "3–4 hechos (estudió, escribió, ganó…)", "2 formas fuertes (fue, hizo…)", "conectores (primero, después, al final)", "una opinión (creo que fue…)", "6–8 frases"]
    x = Inches(6.9); y = Inches(1.7)
    text(s, x, y, Inches(6), Inches(0.4), [[("Checklist:", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    for i, c in enumerate(chk):
        text(s, x, y + Inches(0.5) + i * Inches(0.45), Inches(6), Inches(0.4), [[("☐  " + c, {"size": 13, "color": INK})]])
    rev = card(s, x, Inches(4.35), Inches(6.0), Inches(1.25), fill=GT, line=G, lw=1.2)
    text(s, x + Inches(0.15), Inches(4.4), Inches(5.7), Inches(1.2),
         [[("Modelo: ", {"size": 12, "bold": True, "color": GD}),
           ("«García Márquez nació en Colombia en 1927. Primero estudió periodismo. Después escribió «Cien años de soledad» y ganó el Nobel. Al final murió en 2014. Creo que fue un genio porque creó el realismo mágico.»", {"size": 11, "italic": True, "color": INK})]], line=1.13)
    register_reveal(s, rev)
    noodroute(s); foot(s)
    notes(s, "TEACHER · WRITING (lezen→schrijven, LPD 6). Checklist = zichtbare steun; onthul het model pas na het schrijven. Nakijkfocus: indefinido, fuertes, conectores, opinión. Voedt de Tarea.")

# ============================================================ DIA 15 · VOCAB personas (reveal)
def s15_personas():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · VOCABULARIO", "Personas y logros", "Klik een kaart → la respuesta. Bouw je woordnetwerk.", num=1)
    data = [("el escritor", "de schrijver"), ("la pintora", "de schilderes"), ("el cantante", "de zanger"), ("el futbolista", "de voetballer"),
            ("el científico", "de wetenschapper"), ("el líder", "de leider"), ("el premio", "de prijs"), ("el éxito", "het succes"),
            ("la leyenda", "de legende"), ("el personaje", "het personage"), ("famoso", "beroemd"), ("increíble", "ongelooflijk")]
    x0, y0 = Inches(0.5), Inches(1.7); cw = Inches(3.0); rh = Inches(0.7)
    for i, (es, nl) in enumerate(data):
        c = i % 4; r = i // 4; x = x0 + c * (cw + Inches(0.1)); y = y0 + r * (rh + Inches(0.14))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.12), y, Inches(1.8), rh, [[(es, {"size": 11, "bold": True, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(1.75), y, cw - Inches(1.85), rh, [[("→ " + nl, {"size": 10.5, "color": G})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.9),
             [[("Woordfamilie: ", {"bold": True, "color": GD}), ("escribir → escritor · pintar → pintor · cantar → cantante · la ciencia → científico.", {"color": GD})],
              [("Opinión: creo que fue… · lo más importante fue… · admiro a…", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCAB personas. Klik onthult. Online: memoria de oficios + señala.")

# ============================================================ DIA 16 · TALLER
def s16_taller():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "TALLER DE LENGUA", "Ortografía (yo) + conectores", "Klik een item → correcte vorm. Gereedschap voor spelling en volgorde.", num=1)
    text(s, Inches(0.5), Inches(1.5), Inches(6), Inches(0.35), [[("A · ortografía: c→qu / g→gu / z→c (yo)", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    fixes = [("buscar → yo", "busqué"), ("llegar → yo", "llegué"), ("empezar → yo", "empecé"), ("jugar → yo", "jugué")]
    y = Inches(1.95)
    for q, a in fixes:
        card(s, Inches(0.5), y, Inches(6.0), Inches(0.6), fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, Inches(0.62), y, Inches(3.0), Inches(0.6), [[(q, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, Inches(3.7), y, Inches(2.7), Inches(0.6), [[("→ " + a, {"size": 12, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y = y + Inches(0.72)
    text(s, Inches(6.9), Inches(1.5), Inches(6), Inches(0.35), [[("B · conectores del relato", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    conn = [("érase una vez", "er was eens"), ("primero / después", "eerst / daarna"), ("entonces", "toen / dus"), ("al final / por eso", "uiteindelijk / daarom")]
    y = Inches(1.95)
    for q, a in conn:
        card(s, Inches(6.9), y, Inches(5.9), Inches(0.6), fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, Inches(7.02), y, Inches(3.0), Inches(0.6), [[(q, {"size": 12, "bold": True, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, Inches(10.1), y, Inches(2.6), Inches(0.6), [[("→ " + a, {"size": 11, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y = y + Inches(0.72)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.85),
             [[("A: ", {"bold": True, "color": GD}), ("enkel bij yo verandert de spelling: busqué, llegué, empecé, saqué, jugué, toqué.", {"color": GD})],
              [("B: érase una vez → primero → después → entonces → al final.", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · TALLER. Spellingwissels (yo) + conectoren. Online: drills in de hub.")

# ============================================================ DIA 17 · CULTURE
def s17_cultura():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "CULTURA · PARADA 5: BUENOS AIRES", "Figuras del mundo hispano", "Klik een kaart → het weetje. Gardel, Messi, Frida y García Márquez.", num=1)
    cards = [("🎵 Carlos Gardel", "De legende van de tango. Hij groeide op in Buenos Aires en werd de stem van het genre. «Gardel cada día canta mejor».", "Mateo's stad"),
             ("⚽ Messi y Maradona", "Twee argentijnse voetbalgoden. Maradona maakte in 1986 het «gol del siglo»; Messi werd in 2022 wereldkampioen. Hicieron historia.", "orgullo argentino"),
             ("🎨 Frida & García Márquez", "Frida Kahlo (México) schilderde autorretratos; García Márquez (Colombia) won de Nobelprijs met het «realismo mágico».", "iconos hispanos")]
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
             [[("Voseo (Mateo): ", {"bold": True, "color": GD}), ("«¿de dónde sos?» «vos tenés razón». Rasgo típico del Río de la Plata. Actividad: ¿a quién admiras?", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · CULTURE (LPD 5·6). Onthul per kaart. Bruggetje: La Ruta parada 5 = Argentina (★, persona). Online: klik op Argentina op de kaart.")

# ============================================================ DIA 18 · FINAL_MISSION
def s18_tarea():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(1.35), fill=GD)
    text(s, Inches(0.5), Inches(0.18), Inches(9), Inches(1.0),
         [[("📖 Tarea final · Una biografía", {"size": 27, "bold": True, "color": WHITE, "font": DISPLAY})],
          [("Escribe la vida de una persona con el indefinido, conectores y una opinión.", {"size": 13, "italic": True, "color": GT})]])
    avatar(s, "mochila", Inches(11.6), Inches(0.2), Inches(1.0))
    pasos = [("1", "Empieza con los datos", "«Nació en… en (año). Creció en…»"),
             ("2", "Cuenta 3–4 hechos", "«Estudió…, escribió…, ganó…, hizo…»"),
             ("3", "Usa conectores", "primero · después · entonces · al final"),
             ("4", "Añade tu opinión", "«Creo que fue… porque…»"),
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
    crit = ["indefinido", "2 fuertes", "conectores", "una opinión"]
    x = Inches(0.5)
    for c in crit:
        chip(s, x, Inches(5.45), "☐ " + c, fill=GT, tcolor=GD, size=10, w=Inches(3.05)); x = x + Inches(3.15)
    text(s, Inches(0.5), Inches(6.05), Inches(12), Inches(0.4),
         [[("🎯 ", {"size": 12}), ("Afzender jij · ontvanger de klas · doel een leven delen · situatie een biografie · resultaat: biografía + presentación oral.", {"size": 11.5, "italic": True, "color": MUT})]])
    foot(s)
    notes(s, "TEACHER · FINAL_MISSION (communicatieve eindtaak, LPD 6). Beoordeel met de rúbrica; opname op de web.")

# ============================================================ DIA 19 · MEZCLA
def s19_mezcla():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "QUIZ · LA MEZCLA", "Ophaal door elkaar", "Gemengde ophaal van de hele unit. Klik → het antwoord. (retrieval)", num=1)
    items = [("escribir → él", "escribió"), ("hacer → él", "hizo"), ("ser/ir → él", "fue"),
             ("tener → yo", "tuve"), ("¿El libro a él? ___", "se lo"), ("¿Las fotos a ella? ___", "se las"),
             ("«uiteindelijk» =", "al final"), ("buscar → yo", "busqué")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.62)
    for i, (q, a) in enumerate(items):
        c = i // 4; r = i % 4; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.16))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(4.0), rh, [[(q, {"size": 11.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.15), y, cw - Inches(4.3), rh, [[("→ " + a, {"size": 12, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.05), Inches(12.3), Inches(0.55),
             [[("Alles komt terug: ", {"bold": True, "color": GD}), ("indefinido regular · fuertes · se lo · conectores · ortografía yo.", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ mezcla (retrieval vóór herlezen). Exit-ticket. Zwakke punten → terug via menu.")

# ============================================================ DIA 20 · REPASO
def s20_repaso():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "REPASO · LO ESENCIAL", "Lo esencial de un vistazo", "De volledige herhaling (12 spellen, drills) staat online. Hier: de kern + semáforo.", num=1)
    ess = ["Indefinido regular: -ar → é/aste/ó/amos/asteis/aron · -er/-ir → í/iste/ió/imos/isteis/ieron.",
           "Fuertes: ser/ir → fue · hacer → hizo · tener → tuvo · estar → estuvo · decir → dijo · venir → vino · dar → dio.",
           "Se lo/se la: le/les + lo/la → se lo/se la. «¿El libro? Se lo di».",
           "Marcadores: ayer · el año pasado · en 1919 · de repente. Conectoren: primero, después, al final.",
           "🔴 Trampas: hizo (z) · fue = ser én ir · le lo → se lo · yo: busqué/llegué/empecé."]
    card(s, Inches(0.5), Inches(1.6), Inches(12.3), Inches(2.5), fill=CREMA, line=None)
    y = Inches(1.8)
    for e in ess:
        text(s, Inches(0.8), y, Inches(11.8), Inches(0.45), [[("• ", {"size": 13, "bold": True, "color": GD}), (e, {"size": 12, "color": INK})]])
        y = y + Inches(0.46)
    text(s, Inches(0.5), Inches(4.3), Inches(12), Inches(0.35), [[("Semáforo — ¿cómo lo llevas?", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    can = ["over biografieën praten (oficios/logros)", "de indefinido vormen (regelmatig)", "de sterke vormen gebruiken (fue, hizo…)", "se lo / se la gebruiken", "een verhaal vertellen met conectoren"]
    y = Inches(4.75)
    for c in can:
        text(s, Inches(0.8), y, Inches(7.0), Inches(0.4), [[(c, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        for j, (em, col) in enumerate([("🔴", RED), ("🟠", AMBER), ("🟢", G)]):
            chip(s, Inches(8.0) + j * Inches(1.5), y + Inches(0.03), em + " ", fill=WHITE, tcolor=col, size=12, w=Inches(1.3))
        y = y + Inches(0.42)
    foot(s)
    notes(s, "TEACHER · FEEDBACK/REPASO. Semáforo = zelfevaluatie. Repaso-drills online (12 spellen). Bruggetje: U6 «Cuando era pequeño» — el imperfecto + contrast (Cusco, Nina).")

# ============================================================ DIA 21 · TEACHER
def s21_teacher():
    s = slide(); bg(s, GD)
    text(s, Inches(0.6), Inches(0.4), Inches(12), Inches(0.8), [[("TEACHER_NOTES · U5 «Érase una vez»", {"size": 26, "bold": True, "color": WHITE, "font": DISPLAY})]])
    blocks = [("Timing (50 min)", "Menu 2' · biografía 6' · indefinido regular 12' · fuertes 6' · se lo 10' · contar/escucha 8' · Tarea-briefing 4'."),
              ("Kernvalstrikken", "indefinido = afgeronde feiten (ayer, en 1919) ≠ perfecto (hoy) · hizo met z · fue = ser én ir · le lo → se lo (concordancia OD) · yo-spelling: busqué/llegué/empecé."),
              ("Differentiatie", "Sterker: volledige biografie + 3 fuertes + se lo + una opinión con porque. Zwakker: indefinido-tabel + fuertes-lijst langer open, frames houden; se lo met vaste vraag-antwoord-paren."),
              ("Digitaal", "12 spellen + flip cards + gramática interactiva (indefinido · fuertes · se lo) + recorder (una biografía · mi opinión) + Lectura (Frida/Messi) + klikbare kaart (Argentina ★, persona) op de página digital. QR's → juiste anker."),
              ("Evaluatie & LPD", "Tarea «Una biografía» met rúbrica (4 criteria). LPD (III-Spa-d): biografía 7 · indefinido/se lo 8 · vertellen 3 · interactie 4 · literatuur (biografía/leyenda) 6 · lezen 1·2·5 · cultuur 5. Nieuwe cast: Mateo (voseo).")]
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
    s01_title(); s02_menu(); s03_vocab(); s04_indef(); s05_indef_quiz(); s06_fuertes(); s07_selo()
    s08_selo_quiz(); s09_reading(); s10_listening(); s11_conectores(); s12_mezcla_ind(); s13_speaking(); s14_writing()
    s15_personas(); s16_taller(); s17_cultura(); s18_tarea(); s19_mezcla(); s20_repaso()
    if include_teacher:
        s21_teacher()

def _repaint(path):
    import zipfile, os as _os
    reps = [("1E9E74", "7C56A9"), ("1e9e74", "7c56a9"), ("2EB085", "9374C2"), ("2eb085", "9374c2"),
            ("C5 · A1 · La Ruta", "C6+ · érase una vez")]
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
