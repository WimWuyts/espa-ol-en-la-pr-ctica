#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_c6plus_u3_docente.py — Interactieve PowerPoint C6+ · Unidad 3 «Conectados»
==============================================================================
Zelfde engine/pijplijn als de golden sample (gen_u0_docente = de engine). Enkel de SLIDES
zijn C6+·U3-specifiek. Cursuskleur = PAARS. Twee decks (beide .pptx):
  · C6plus_U3_docente.pptx — vrije navigatie, oplossingen + didactiek in notities.
  · C6plus_U3_alumno.pptx  — gewone diavoorstelling, antwoorden bij klik (F5).
Grammatica: ir a + infinitivo (futuro próximo) + acabar de · OI-pronomina le/les · creo que + indicativo.
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
OUT_DOCENTE = os.path.join(HERE, "C6plus_U3_docente.pptx")
OUT_ALUMNO_PPTX = os.path.join(HERE, "C6plus_U3_alumno.pptx")
TAB = "U3 · CONECTADOS"

def foot(s): footer(s, tab=TAB, page=pg())

# ============================================================ DIA 1 · TITLE
def s01_title():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(4.7), fill=G)
    rect(s, 0, Inches(4.7), EMU_W, Inches(0.09), fill=GD)
    text(s, Inches(0.6), Inches(0.35), Inches(3.4), Inches(3.6),
         [[("3", {"size": 260, "bold": True, "color": RGBColor(0x93, 0x74, 0xC2), "font": DISPLAY})]],
         anchor=MSO_ANCHOR.MIDDLE)
    chip(s, Inches(4.35), Inches(0.85), "LA RUTA · CDMX 🇲🇽 · CONECTADOS 📱", fill=WHITE, tcolor=GD, size=12)
    text(s, Inches(4.3), Inches(1.35), Inches(8.6), Inches(1.5),
         [[("Conectados", {"size": 62, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(4.35), Inches(2.7), Inches(8.4), Inches(0.6),
         [[("Media y planes: ir a + infinitivo · le/les · creo que + indicativo.", {"size": 15, "italic": True, "color": GT})]])
    text(s, Inches(4.35), Inches(3.35), Inches(8.4), Inches(0.9),
         [[("¿Qué vas a hacer este finde?", {"size": 24, "bold": True, "color": WHITE, "font": DISPLAY})],
          [("Wat ga je dit weekend doen?", {"size": 13, "italic": True, "color": GT})]])
    text(s, Inches(0.6), Inches(4.95), Inches(6), Inches(0.4),
         [[("La gente de la ruta — parada 3: CDMX (Diego)", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
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
    notes(s, "TEACHER · TITLE. U3 = media, redes y planes. Kerngrammatica: ir a + infinitivo (futuro próximo) + acabar de, "
             "OI-pronomina le/les, creo que + indicativo. Parada 3 = CDMX (Diego). Kernvalstrikken: voy A subir (vergeet de a niet) · "
             "creo que + INDICATIVO (nooit subjuntivo) · le (1 persoon) ≠ les (meer). Docentdeck = oplossing; leerlingdeck (.pptx, F5) = klik onthult.")

# ============================================================ DIA 2 · LESSON_MENU
def s02_menu():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "MENÚ DE LA LECCIÓN", "El mapa de la Unidad 3",
               "Kies je route — klik een tegel. Alles oefent naar de Tarea «Mi plan de fin de semana» toe.", num=3)
    tiles = [
        ("§1", "El móvil", "medios · redes", G, 3),
        ("§2", "Ir a + inf.", "futuro próximo", G, 4),
        ("§3", "Le / les", "¿a quién? (OI)", G, 7),
        ("§4", "Creo que", "+ indicativo · acabar de", G, 11),
        ("§5", "Comunicar", "y hacer planes", G, 15),
        ("★", "Lectura + escucha", "¿adicto al móvil?", GD, 9),
        ("🎵", "Cultura", "el mundo digital", GD, 17),
        ("📱", "Tarea · Mi finde", "chat + opinión", GD, 18),
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
             "Kern = §2 ir a + infinitivo + §3 le/les + §4 creo que. Kruisverwijzing: «oefen online — 13 juegos + 100+ oefeningen».")

# ============================================================ DIA 3 · VOCAB — el móvil y las redes
def s03_vocab():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · VOCABULARIO", "El móvil y las redes", "De woorden van de digitale wereld — observa. Herken ze, dan gebruik je ze.", num=1)
    legend_func(s, Inches(9.7), Inches(0.55))
    rows = [("el móvil", "de gsm", "cargar, apagar"), ("el ordenador", "de computer", "encender"),
            ("la pantalla", "het scherm", "mirar"), ("los auriculares", "de oortjes", "escuchar"),
            ("el perfil", "het profiel", "las redes"), ("el mensaje", "het bericht", "mandar"),
            ("la contraseña", "het wachtwoord", "el usuario"), ("el vídeo", "de video", "subir")]
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
           ("el móvil, el mensaje, el perfil, el vídeo (m) · la tableta, la pantalla, la app, la contraseña (v)", {"size": 13, "color": INK})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.35), Inches(12.3), Inches(0.95),
             [[("Las acciones: ", {"bold": True, "color": GD}), ("subir un vídeo · descargar una app · chatear con un amigo · seguir a un artista · compartir una foto.", {"color": GD})],
              [("🔴 los auriculares = altijd meervoud (de oortjes).", {"color": RED})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCABULARY. Laat de media-woorden raden zónder gloss. Koppel verbo → objeto (subir un vídeo). Online: memoria digital (memory) + verbo↔objeto (match).")

# ============================================================ DIA 4 · GRAMMAR — ir a + infinitivo (color)
def s04_ira():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · GRAMÁTICA VISUAL", "Ir a + infinitivo — el futuro próximo", "ir (voy/vas/va…) + a + infinitivo. Kleur = de functie.", num=2)
    legend_func(s, Inches(9.7), Inches(0.55))
    seg = [("Este finde ", F_TIME), ("voy a ", F_VERB), ("subir ", F_OBJ), ("un vídeo", F_PLAC)]
    runs = [[(t, {"size": 22, "bold": True, "color": c, "font": DISPLAY}) for t, c in seg]]
    card(s, Inches(0.5), Inches(1.7), Inches(12.3), Inches(1.2), fill=GT, line=None)
    text(s, Inches(0.8), Inches(1.7), Inches(11.7), Inches(1.2), runs, anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(3.15), Inches(12), Inches(0.4), [[("La conjugación de ir", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    frame = [("yo voy a", "voy a subir"), ("tú vas a", "vas a salir"), ("él/ella va a", "va a chatear"),
             ("nosotros vamos a", "vamos a quedar"), ("vosotros vais a", "vais a estudiar"), ("ellos van a", "van a ver")]
    x0, y0 = Inches(0.5), Inches(3.6); cw = Inches(4.0); rh = Inches(0.62)
    for i, (a, b) in enumerate(frame):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.12))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(2.0), rh, [[(a, {"size": 11.5, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(2.15), y, cw - Inches(2.3), rh, [[(b, {"size": 10.5, "color": F_VERB, "bold": True})]], anchor=MSO_ANCHOR.MIDDLE)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.75), Inches(12.3), Inches(0.6),
             [[("Regla: ", {"bold": True, "color": GD}), ("enkel ir verandert (voy/vas/va…); daarna altijd a + infinitivo. 🔴 vergeet de a niet: «voy subir» → voy a subir.", {"color": GD})]],
             trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR ir a. Toon de bouw ir + a + infinitivo. Benadruk de a. Online: ir a + infinitivo (cloze) + ir a Tetris.")

# ============================================================ DIA 5 · QUIZ — ir a (reveal)
def s05_ira_quiz():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · QUIZ", "¿Qué forma de ir?", "Klik een zin → de juiste vorm. Kijk naar de persoon.", num=2)
    items = [("Yo ___ subir un vídeo.", "voy a"), ("¿Tú ___ salir el sábado?", "vas a"),
             ("Diego ___ chatear.", "va a"), ("Nosotros ___ quedar.", "vamos a"),
             ("Mis amigos ___ ver una peli.", "van a"), ("¿Vosotros ___ estudiar?", "vais a")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.78)
    for i, (q, a) in enumerate(items):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(4.3), rh, [[(q, {"size": 12.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.5), y, cw - Inches(4.6), rh, [[("→ " + a, {"size": 14, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Truc: ", {"bold": True, "color": RED}), ("ir vervoegd + a + infinitivo. voy/vas/va/vamos/vais/van a + hele werkwoord.", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ ir a (retrieval). Klas roept de vorm vóór de klik. Online: ir a + infinitivo (cloze).")

# ============================================================ DIA 6 · GRAMMAR — acabar de + expresiones de tiempo (reveal)
def s06_acabar():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · GRAMÁTICA", "Acabar de + tijd", "Klik een cue → de vorm. acabar de = «net gedaan». + expresiones de tiempo.", num=2)
    items = [("net gedaan (yo)", "acabo de comer"), ("net gedaan (él)", "acaba de subir"),
             ("straks", "luego / más tarde"), ("morgen", "mañana"),
             ("dit weekend", "este fin de semana"), ("binnenkort", "pronto"),
             ("later", "más tarde"), ("volgend jaar", "el próximo año")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.72)
    for i, (q, a) in enumerate(items):
        c = i // 4; r = i % 4; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.14))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(2.6), rh, [[(q, {"size": 12, "color": MUT})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(2.8), y, cw - Inches(2.9), rh, [[("→ " + a, {"size": 13, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.85), Inches(12.3), Inches(0.85),
             [[("Acabar de: ", {"bold": True, "color": GD}), ("acabo/acabas/acaba… + de + infinitivo = «net … gedaan». Acabo de mandar un mensaje.", {"color": GD})],
              [("🔴 futuro (ir a) vs recién (acabar de): «Mañana voy a…» tegenover «Acabo de…».", {"color": RED})]],
             trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR acabar de + tijd. Contrast ir a (straks) ↔ acabar de (net). Online: ¿ahora o después? (classify) + cloze.")

# ============================================================ DIA 7 · GRAMMAR — le/les (color)
def s07_leles():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · GRAMÁTICA VISUAL", "Los pronombres le/les — ¿a quién?", "Het meewerkend voorwerp: aan/voor wie? Kleur = de functie.", num=3)
    legend_func(s, Inches(9.7), Inches(0.55))
    card(s, Inches(0.5), Inches(1.7), Inches(6.0), Inches(1.1), fill=GT, line=None)
    text(s, Inches(0.7), Inches(1.7), Inches(5.6), Inches(1.1),
         [[("Escribo ", {"size": 15, "color": INK}), ("a Diego", {"size": 15, "bold": True, "color": F_PLAC}),
           (" → ", {"size": 15, "color": MUT}), ("Le", {"size": 18, "bold": True, "color": F_PLAC}), (" escribo.", {"size": 15, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
    card(s, Inches(6.8), Inches(1.7), Inches(6.0), Inches(1.1), fill=GT, line=None)
    text(s, Inches(7.0), Inches(1.7), Inches(5.6), Inches(1.1),
         [[("Mando fotos ", {"size": 15, "color": INK}), ("a mis amigos", {"size": 15, "bold": True, "color": F_PLAC}),
           (" → ", {"size": 15, "color": MUT}), ("Les", {"size": 18, "bold": True, "color": F_PLAC}), (" mando.", {"size": 15, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
    frame = [("me", "a mí"), ("te", "a ti"), ("le", "a él/ella/usted"),
             ("nos", "a nosotros"), ("os", "a vosotros"), ("les", "a ellos/ellas")]
    x0, y0 = Inches(0.5), Inches(3.15); cw = Inches(4.0); rh = Inches(0.62)
    for i, (a, b) in enumerate(frame):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.12))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(1.1), rh, [[(a, {"size": 15, "bold": True, "color": F_PLAC, "font": DISPLAY})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(1.3), y, cw - Inches(1.4), rh, [[(b, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.9),
             [[("Regla: ", {"bold": True, "color": GD}), ("le = aan één persoon · les = aan meerdere. Staat vóór het vervoegde werkwoord. ", {"color": GD})],
              [("In het Spaans zeg je vaak le én a Diego samen: «Le escribo a Diego» — dat is normaal.", {"color": GD})]],
             trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR le/les. Koppel gustar (le gusta, U1) → le/les. Online: ¿le o les? (classify) + le/les (cloze).")

# ============================================================ DIA 8 · QUIZ — le/les (reveal)
def s08_leles_quiz():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · QUIZ", "¿le o les?", "Klik een zin → het juiste pronomen. ¿Una persona o varias?", num=3)
    items = [("___ escribo a mi amiga.", "Le"), ("___ mando fotos a mis padres.", "Les"),
             ("___ cuento un secreto a Diego.", "Le"), ("___ regalo algo a mis hermanos.", "Les"),
             ("___ pregunto la hora a Valen.", "Le"), ("___ enseño el perfil a mis amigos.", "Les")]
    x0, y0 = Inches(0.5), Inches(1.7); cw = Inches(6.05); rh = Inches(0.7)
    for i, (q, ans) in enumerate(items):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(4.3), rh, [[(q, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.5), y, cw - Inches(4.6), rh, [[("→ " + ans, {"size": 13.5, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.9),
             [[("Regla: ", {"bold": True, "color": G}), ("a + één persoon → le · a + meer personen → les.", {"color": GD})],
              [("Plaats: vóór het vervoegde werkwoord (of achter de infinitivo: voy a escribirle).", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ le/les (reveal). Coro vóór de klik. Online: le/les (cloze) + le/les (classify).")

# ============================================================ DIA 9 · READING — dos perfiles
def s09_reading():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§6 · LEER · COMPRENSIÓN", "Dos opiniones — «¿Adicto al móvil?»", "Lees. Klik een vraag → het antwoord verschijnt.", num=6)
    card(s, Inches(0.5), Inches(1.65), Inches(5.6), Inches(3.9), fill=GT, line=G, lw=1.4)
    avatar(s, "diego", Inches(0.85), Inches(1.95), Inches(1.0))
    text(s, Inches(2.05), Inches(1.98), Inches(3.9), Inches(1.5),
         [[("«Paso muchas horas con el móvil: subo vídeos y chateo. Creo que es útil para estudiar, pero también es adictivo. Este finde voy a apagar el móvil dos horas al día.»", {"size": 11, "italic": True, "color": INK})]], line=1.16)
    avatar(s, "lucia", Inches(0.85), Inches(3.65), Inches(1.0))
    text(s, Inches(2.05), Inches(3.68), Inches(3.9), Inches(1.5),
         [[("«Me gustan las redes, pero no paso tanto tiempo. Creo que conectan a la gente, pero pueden ser peligrosas. Lo importante es el equilibrio.»", {"size": 11, "italic": True, "color": INK})]], line=1.16)
    qa = [("¿Qué cree Diego del móvil?", "Es útil pero adictivo"), ("¿Qué va a hacer Diego el finde?", "Apagar el móvil 2 h/día"),
          ("¿Qué piensa Lucía de las redes?", "Conectan, pero peligrosas"), ("Para Lucía, lo importante es…", "El equilibrio")]
    x = Inches(6.4); y = Inches(1.7)
    for q, a in qa:
        card(s, x, y, Inches(6.4), Inches(0.85), fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y + Inches(0.06), Inches(6.1), Inches(0.4), [[(q, {"size": 12.5, "bold": True, "color": GD})]])
        rev = text(s, x + Inches(0.15), y + Inches(0.44), Inches(6.1), Inches(0.35), [[("→ " + a, {"size": 12, "color": INK})]])
        register_reveal(s, rev)
        y = y + Inches(0.98)
    btn = noodroute(s)
    exercise_solucion(s, Inches(6.4), Inches(5.65), Inches(6.4), Inches(0.6),
             [[("🎯 Leesdoel: ", {"bold": True, "color": GD}), ("scannen naar de mening (creo que…) + het plan (voy a…).", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · READING (lezen→schrijven). Eerst globaal, dan scannen. Daarna: leerlingen geven hun eigen mening (creo que + porque) + een plan (voy a).")

# ============================================================ DIA 10 · LISTENING — ¿qué vas a hacer el finde?
def s10_listening():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · ESCUCHAR · INTERACCIÓN", "¿Qué vas a hacer el finde?", "Volg het gesprek. Klik un dato → de info. (audio + script op de web)", num=2)
    pasos = [("🔊 ¿Qué?", "Van a quedar y ver una peli"), ("🔊 ¿Cuándo?", "El sábado por la tarde"),
             ("🔊 ¿Dónde?", "En la plaza, luego en casa"), ("🔊 ¿Y antes?", "Diego va a subir un vídeo")]
    x0, y0 = Inches(0.7), Inches(1.9); cw = Inches(2.95); ch = Inches(2.4)
    for i, (mom, det) in enumerate(pasos):
        x = x0 + i * (cw + Inches(0.1))
        card(s, x, y0, cw, ch, fill=WHITE, line=LINE, lw=1.2)
        rect(s, x, y0, cw, Inches(0.5), fill=GT)
        text(s, x, y0, cw, Inches(0.5), [[("dato " + str(i+1), {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(0.15), y0 + Inches(0.7), cw - Inches(0.3), Inches(0.7), [[(mom, {"size": 14, "bold": True, "color": INK, "font": DISPLAY})]], line=1.05)
        rev = text(s, x + Inches(0.15), y0 + Inches(1.5), cw - Inches(0.3), Inches(0.7), [[(det, {"size": 11.5, "color": G})]], line=1.05)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.85),
             [[("Modelo-audio (docent/TTS): ", {"bold": True, "color": GD}),
               ("«— ¿Qué vas a hacer el finde? — El sábado voy a quedar con Diego. Vamos a ver una peli.» ", {"color": GD})],
              [("Daarna: A vraagt B naar zijn plannen (info-gap).", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · LISTENING (luisteren→spreken). Lees het gesprek voor (of TTS); klas noteert qué/cuándo/dónde. Daarna info-gap in parejas. Online: ¿qué vas a hacer el finde? (audio + script).")

# ============================================================ DIA 11 · GRAMMAR — creo que + indicativo
def s11_creoque():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · GRAMÁTICA VISUAL", "Creo que + indicativo — tu opinión", "creo que / pienso que / me parece que + de gewone tijd. Nooit subjuntivo.", num=4)
    legend_func(s, Inches(9.7), Inches(0.55))
    seg = [("Creo que ", F_STRA), ("las redes ", F_SUBJ), ("son ", F_VERB), ("útiles", F_OBJ)]
    runs = [[(t, {"size": 22, "bold": True, "color": c, "font": DISPLAY}) for t, c in seg]]
    card(s, Inches(0.5), Inches(1.7), Inches(12.3), Inches(1.2), fill=GT, line=None)
    text(s, Inches(0.8), Inches(1.7), Inches(11.7), Inches(1.2), runs, anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(3.15), Inches(12), Inches(0.4), [[("Para opinar y reaccionar", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    frame = [("creo que…", "ik vind/denk dat"), ("pienso que…", "ik denk dat"), ("me parece que…", "het lijkt me dat"),
             ("(no) estoy de acuerdo", "ik ben het (niet) eens"), ("tienes razón", "je hebt gelijk"), ("por un lado… por otro…", "enerzijds… anderzijds…")]
    x0, y0 = Inches(0.5), Inches(3.6); cw = Inches(4.0); rh = Inches(0.62)
    for i, (a, b) in enumerate(frame):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.12))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(2.1), rh, [[(a, {"size": 11.5, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(2.25), y, cw - Inches(2.4), rh, [[(b, {"size": 10, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.75), Inches(12.3), Inches(0.6),
             [[("Regla: ", {"bold": True, "color": GD}), ("creo que + indicativo (de gewone tijd): «creo que es útil». 🔴 nooit subjuntivo. Bouw af met porque.", {"color": GD})]],
             trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR creo que. Benadruk: creo que + INDICATIVO (buiten scope: subjuntivo). Online: creo que + indicativo (cloze).")

# ============================================================ DIA 12 · QUIZ — creo que (reveal)
def s12_creoque_quiz():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · QUIZ", "Creo que + indicativo", "Klik → de gewone vorm. (nooit subjuntivo!)", num=4)
    items = [("Creo que las redes ___ (ser) útiles.", "son"), ("Pienso que Diego ___ (tener) razón.", "tiene"),
             ("Me parece que (nosotros) ___ (pasar) mucho tiempo.", "pasamos"), ("Creo que el móvil ___ (ayudar).", "ayuda"),
             ("Pienso que los juegos ___ (poder) ser adictivos.", "pueden"), ("Creo que la wifi ___ (ser) rápida.", "es")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.78)
    for i, (q, ans) in enumerate(items):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(4.6), rh, [[(q, {"size": 11.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.8), y, cw - Inches(4.9), rh, [[("→ " + ans, {"size": 14, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Indicativo: ", {"bold": True, "color": GD}), ("son · tiene · pasamos · ayuda · pueden · es. Dezelfde gewone tijd die je al kent.", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ creo que (retrieval). Klas roept de indicativo vóór de klik. Online: creo que + indicativo (cloze).")

# ============================================================ DIA 13 · SPEAKING — habla de tus planes
def s13_speaking():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · SPEAKING · INTERACCIÓN", "Habla de tus planes y tu opinión", "Speel de scène met de frames. Steun bouwt af: kaarten → beginwoorden → uit het hoofd.", num=2)
    avatar(s, "tu", Inches(11.4), Inches(1.7), Inches(1.3))
    labels = ["Un plan", "¿Cuándo?", "¿Con quién?", "Acabas de…", "Tu opinión", "Argumento"]
    frames = ["Voy a…", "Este finde / mañana…", "Le escribo a…", "Acabo de…", "Creo que…", "…porque…"]
    x0, y0 = Inches(0.5), Inches(1.8); cw = Inches(3.4); rh = Inches(0.8)
    for i, (lab, fr) in enumerate(zip(labels, frames)):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=G, lw=1.2, shadow=False)
        text(s, x + Inches(0.15), y + Inches(0.05), cw - Inches(0.3), Inches(0.32), [[(lab, {"size": 10, "color": MUT})]])
        text(s, x + Inches(0.15), y + Inches(0.36), cw - Inches(0.3), Inches(0.4), [[(fr, {"size": 12.5, "bold": True, "color": GD, "font": DISPLAY})]])
    chip(s, Inches(0.5), Inches(4.65), "🎙️ Grábate online · «Mensaje de voz: mi finde / mi opinión»", fill=GT, tcolor=GD, size=11)
    text(s, Inches(0.5), Inches(5.05), Inches(10.5), Inches(0.9),
         [[("Ronda 1: ", {"size": 12, "bold": True, "color": GD}), ("met de kaarten. ", {"size": 12, "color": INK}),
           ("Ronda 2: ", {"size": 12, "bold": True, "color": GD}), ("beginwoorden. ", {"size": 12, "color": INK}),
           ("Ronda 3: ", {"size": 12, "bold": True, "color": GD}), ("uit het hoofd. ", {"size": 12, "color": INK}),
           ("Ronda 4: ", {"size": 12, "bold": True, "color": GD}), ("grábate.", {"size": 12, "color": INK})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.6), Inches(12.3), Inches(0.65),
             [[("Modelo: ", {"bold": True, "color": GD}), ("«Este finde voy a quedar con Diego. Le escribo para invitarlo. Acabo de crear el grupo. Creo que va a ser genial porque hace tiempo que no nos vemos.»", {"color": GD})]],
             trigger=btn, title_doc="MODELO · docent")
    foot(s)
    notes(s, "TEACHER · SPEAKING (interactie). Rondes met afbouwende steun. Online: recorder (mi finde + mi opinión). Print blijft bruikbaar zonder opname.")

# ============================================================ DIA 14 · WRITING — mi plan de fin de semana
def s14_writing():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "WRITING · PRODUCCIÓN", "Mi plan de fin de semana", "Schrijf je weekendplan-chat. Klik → een modeltekst verschijnt.", num=2)
    card(s, Inches(0.5), Inches(1.7), Inches(6.0), Inches(3.9), fill=WHITE, line=LINE, lw=1.2)
    text(s, Inches(0.7), Inches(1.85), Inches(5.6), Inches(0.4), [[("✍️ Escribe tu chat de planes:", {"size": 12, "bold": True, "color": GD})]])
    for i in range(6):
        rect(s, Inches(0.7), Inches(2.4) + i * Inches(0.5), Inches(5.6), Inches(0.01), fill=LINE)
    chk = ["3–4 planes (ir a + infinitivo + a)", "una expresión de tiempo (este finde…)", "a quién escribes (le/les)", "algo que acabas de hacer (acabar de)", "una opinión (creo que… porque)", "6–8 mensajes de chat"]
    x = Inches(6.9); y = Inches(1.7)
    text(s, x, y, Inches(6), Inches(0.4), [[("Checklist:", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    for i, c in enumerate(chk):
        text(s, x, y + Inches(0.5) + i * Inches(0.45), Inches(6), Inches(0.4), [[("☐  " + c, {"size": 13, "color": INK})]])
    rev = card(s, x, Inches(4.35), Inches(6.0), Inches(1.25), fill=GT, line=G, lw=1.2)
    text(s, x + Inches(0.15), Inches(4.4), Inches(5.7), Inches(1.2),
         [[("Modelo: ", {"size": 12, "bold": True, "color": GD}),
           ("«¡Hola! Este finde voy a quedar con Diego. Le escribo para invitarlo y les mando la hora a los demás. Acabo de crear el grupo. Creo que va a ser un finde genial porque vamos a ver la final.»", {"size": 11, "italic": True, "color": INK})]], line=1.13)
    register_reveal(s, rev)
    noodroute(s); foot(s)
    notes(s, "TEACHER · WRITING (lezen→schrijven). Checklist = zichtbare steun; onthul het model pas na het schrijven. Nakijkfocus: ir a + a, le/les, acabar de, creo que + indicativo. Voedt de Tarea «Mi plan de fin de semana».")

# ============================================================ DIA 15 · VOCAB — comunicar y planes (reveal)
def s15_comunicar():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§5 · VOCABULARIO", "Comunicar y hacer planes", "Klik een kaart → la respuesta. Bouw je woordnetwerk.", num=5)
    data = [("escribir", "schrijven"), ("mandar / enviar", "sturen"), ("llamar", "bellen"), ("contestar", "antwoorden"),
            ("contar", "vertellen"), ("preguntar", "vragen"), ("quedar", "afspreken"), ("salir", "uitgaan"),
            ("hacer planes", "plannen maken"), ("¿quedamos?", "spreken we af?"), ("¿a qué hora?", "hoe laat?"), ("nos vemos", "tot dan")]
    x0, y0 = Inches(0.5), Inches(1.7); cw = Inches(3.0); rh = Inches(0.7)
    for i, (es, nl) in enumerate(data):
        c = i % 4; r = i // 4; x = x0 + c * (cw + Inches(0.1)); y = y0 + r * (rh + Inches(0.14))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.12), y, Inches(1.8), rh, [[(es, {"size": 11.5, "bold": True, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(1.85), y, cw - Inches(1.95), rh, [[("→ " + nl, {"size": 11, "color": G})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.9),
             [[("Chunks para quedar: ", {"bold": True, "color": GD}), ("¿Quedamos el sábado? · ¿A qué hora? · ¿Dónde? · Vale, nos vemos.", {"color": GD})],
              [("Verbos + le/les: escribir/mandar/decir/contar/preguntar/regalar a alguien.", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCAB comunicar/planes. Klik onthult; koppel verbo → le/les. Online: verbo↔objeto (match) + memoria de acciones.")

# ============================================================ DIA 16 · TALLER — c/z/qu + conectores de tiempo
def s16_taller():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "TALLER DE LENGUA", "c/z/qu + conectores de tiempo", "Klik een item → correcte vorm. Gereedschap voor spelling en volgorde.", num=1)
    text(s, Inches(0.5), Inches(1.5), Inches(6), Inches(0.35), [[("A · ortografía: c / z / qu", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    fixes = [("la _ontraseña", "contraseña (c)"), ("_edar", "quedar (qu)"), ("el _umo", "zumo (z)"), ("la músi_a", "música (c)")]
    y = Inches(1.95)
    for q, a in fixes:
        card(s, Inches(0.5), y, Inches(6.0), Inches(0.6), fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, Inches(0.62), y, Inches(2.6), Inches(0.6), [[(q, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, Inches(3.3), y, Inches(3.1), Inches(0.6), [[("→ " + a, {"size": 12, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y = y + Inches(0.72)
    text(s, Inches(6.9), Inches(1.5), Inches(6), Inches(0.35), [[("B · conectores: ordena tu plan", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    conn = [("primero", "eerst"), ("después / luego", "daarna"), ("más tarde", "later"), ("al final / por último", "ten slotte")]
    y = Inches(1.95)
    for q, a in conn:
        card(s, Inches(6.9), y, Inches(5.9), Inches(0.6), fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, Inches(7.02), y, Inches(2.6), Inches(0.6), [[(q, {"size": 12, "bold": True, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, Inches(9.7), y, Inches(3.0), Inches(0.6), [[("→ " + a, {"size": 11.5, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y = y + Inches(0.72)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.85),
             [[("A: ", {"bold": True, "color": GD}), ("/k/ = c (a/o/u) of qu (e/i): contraseña, quedar · /θ/ = z (a/o/u) of c (e/i): zumo, música.", {"color": GD})],
              [("B: primero → después/luego → más tarde → al final. Zo orden je je weekendplan.", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · TALLER. c/z/qu-spelling + tijdsconnectoren. Online: drills in de hub.")

# ============================================================ DIA 17 · CULTURE — el mundo digital hispano
def s17_cultura():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "CULTURA · PARADA 3: CDMX", "El mundo digital hispano", "Klik een kaart → het weetje. Música, WhatsApp y el español online.", num=1)
    cards = [("🎵 El reguetón manda", "Artiesten als Bad Bunny (Puerto Rico) en Karol G (Colombia) breken streamingrecords op Spotify en YouTube. Het Spaans klinkt wereldwijd.", "Diego lo escucha cada día"),
             ("💬 WhatsApp, la red nº 1", "In veel Latijns-Amerikaanse landen is WhatsApp dé manier om te communiceren — met familie, vrienden én winkels.", "«Te mando un audio»"),
             ("🌐 El español en internet", "Het Spaans is de tweede taal op sociale media na het Engels. Meer dan 500 miljoen sprekers.", "tu feed habla español")]
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
             [[("Actividad: ", {"bold": True, "color": GD}), ("¿qué redes/música hispana conoces? Da tu opinión: «Creo que… porque…».", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · CULTURE (identiteit in diversiteit, LPD 5). Onthul per kaart. Bruggetje: La Ruta parada 3 = CDMX (★, música). Online: klik op México op de kaart.")

# ============================================================ DIA 18 · FINAL_MISSION
def s18_tarea():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(1.35), fill=GD)
    text(s, Inches(0.5), Inches(0.18), Inches(9), Inches(1.0),
         [[("📱 Tarea final · Mi plan de fin de semana", {"size": 27, "bold": True, "color": WHITE, "font": DISPLAY})],
          [("Escribe un chat/post con tus planes, a quién escribes y tu opinión.", {"size": 13, "italic": True, "color": GT})]])
    avatar(s, "mochila", Inches(11.6), Inches(0.2), Inches(1.0))
    pasos = [("1", "Escribe 3–4 planes", "ir a + infinitivo + una expresión de tiempo"),
             ("2", "Di a quién escribes", "«le escribo a Diego» · «les mando la hora»"),
             ("3", "Añade algo reciente", "«acabo de crear el grupo»"),
             ("4", "Da tu opinión", "«creo que va a ser genial porque…»"),
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
    crit = ["ir a + inf. (+ a)", "le én les", "acabar de", "creo que + indicativo"]
    x = Inches(0.5)
    for c in crit:
        chip(s, x, Inches(5.45), "☐ " + c, fill=GT, tcolor=GD, size=10, w=Inches(3.05)); x = x + Inches(3.15)
    text(s, Inches(0.5), Inches(6.05), Inches(12), Inches(0.4),
         [[("🎯 ", {"size": 12}), ("Afzender jij · ontvanger de klasgroep · doel je plan delen · situatie een chat · resultaat: chat/post + presentación oral.", {"size": 11.5, "italic": True, "color": MUT})]])
    foot(s)
    notes(s, "TEACHER · FINAL_MISSION (communicatieve eindtaak). Afzender/ontvanger/doel/situatie/resultaat expliciet. Beoordeel met de rúbrica; opname op de web.")

# ============================================================ DIA 19 · QUIZ — la mezcla (retrieval)
def s19_mezcla():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "QUIZ · LA MEZCLA", "Ophaal door elkaar", "Gemengde ophaal van de hele unit. Klik → het antwoord. (retrieval)", num=1)
    items = [("Yo ___ subir un vídeo (ir a)", "voy a"), ("«ik heb net gegeten» =", "acabo de comer"),
             ("___ escribo a Diego (le/les)", "le"), ("___ mando fotos a mis amigos", "les"),
             ("Creo que las redes ___ (ser) útiles", "son"), ("¿Tú ___ salir el sábado?", "vas a"),
             ("«dit weekend» =", "este finde"), ("Nosotros ___ quedar", "vamos a")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.62)
    for i, (q, a) in enumerate(items):
        c = i // 4; r = i % 4; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.16))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(4.0), rh, [[(q, {"size": 11.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.15), y, cw - Inches(4.3), rh, [[("→ " + a, {"size": 12, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.05), Inches(12.3), Inches(0.55),
             [[("Alles komt terug: ", {"bold": True, "color": GD}), ("ir a + infinitivo · acabar de · le/les · creo que + indicativo · expresiones de tiempo.", {"color": GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ mezcla (retrieval vóór herlezen). Zonder waarschuwing door elkaar. Exit-ticket. Zwakke punten → terug via menu.")

# ============================================================ DIA 20 · FEEDBACK/REPASO
def s20_repaso():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "REPASO · LO ESENCIAL", "Lo esencial de un vistazo", "De volledige herhaling (13 spellen, drills) staat online. Hier: de kern + semáforo.", num=1)
    ess = ["Ir a + infinitivo: voy/vas/va/vamos/vais/van + a + infinitivo. Vergeet de a niet!",
           "Acabar de + infinitivo: acabo/acabas/acaba… + de + infinitivo = «net gedaan».",
           "Le/les (OI): le = één persoon · les = meerdere. Vóór het ww. of achter de infinitivo.",
           "Creo que + indicativo: mening met de gewone tijd (nooit subjuntivo). Creo que es útil.",
           "🔴 Trampas: voy A subir · le/les vóór het ww. · creo que + indicativo · los auriculares = mv."]
    card(s, Inches(0.5), Inches(1.6), Inches(12.3), Inches(2.5), fill=CREMA, line=None)
    y = Inches(1.8)
    for e in ess:
        text(s, Inches(0.8), y, Inches(11.8), Inches(0.45), [[("• ", {"size": 13, "bold": True, "color": GD}), (e, {"size": 12, "color": INK})]])
        y = y + Inches(0.46)
    text(s, Inches(0.5), Inches(4.3), Inches(12), Inches(0.35), [[("Semáforo — ¿cómo lo llevas?", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    can = ["over media en redes praten", "plannen maken (ir a + infinitivo)", "le/les gebruiken (¿a quién?)", "zeggen wat ik net deed (acabar de)", "mijn mening geven (creo que + porque)"]
    y = Inches(4.75)
    for c in can:
        text(s, Inches(0.8), y, Inches(7.0), Inches(0.4), [[(c, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        for j, (em, col) in enumerate([("🔴", RED), ("🟠", AMBER), ("🟢", G)]):
            chip(s, Inches(8.0) + j * Inches(1.5), y + Inches(0.03), em + " ", fill=WHITE, tcolor=col, size=12, w=Inches(1.3))
        y = y + Inches(0.42)
    foot(s)
    notes(s, "TEACHER · FEEDBACK/REPASO. Semáforo = zelfevaluatie. Repaso-drills online (13 spellen). Bruggetje: U4 «De viaje» — reizen, transport, alojamiento.")

# ============================================================ DIA 21 · TEACHER_NOTES
def s21_teacher():
    s = slide(); bg(s, GD)
    text(s, Inches(0.6), Inches(0.4), Inches(12), Inches(0.8), [[("TEACHER_NOTES · U3 «Conectados»", {"size": 26, "bold": True, "color": WHITE, "font": DISPLAY})]])
    blocks = [("Timing (50 min)", "Menu 2' · el móvil 6' · ir a + infinitivo 12' · le/les 10' · creo que 8' · comunicar/escucha 8' · Tarea-briefing 4'."),
              ("Kernvalstrikken", "ir a + infinitivo: vergeet de a niet (voy A subir) · le (1 persoon) ≠ les (meer) · le/les vóór het vervoegde werkwoord (of achter de infinitivo: voy a escribirle) · creo que + INDICATIVO (nooit subjuntivo — buiten scope)."),
              ("Differentiatie", "Sterker: volledig weekendplan + le/les + acabar de + una opinión con porque. Zwakker: ir a-kaart + le/les-frame langer open, frames houden; creo que met vaste modelzinnen."),
              ("Digitaal", "13 spellen + flip cards + gramática interactiva (ir a · le/les · creo que) + recorder (mi finde · mi opinión) + Lectura (dos opiniones) + klikbare kaart (México ★, música) op de página digital. QR's → juiste anker."),
              ("Evaluatie & LPD", "Tarea «Mi plan de fin de semana» met rúbrica (4 criteria). LPD (III-Spa-d): media/redes 7 · ir a + infinitivo 8·3 · le/les 8·4 · acabar de/creo que 8·3 · interactie 4 · lezen 1·2·5 · cultuur 5. Bron: EELP (comunicación/cognición) + reservoir.")]
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
    s01_title(); s02_menu(); s03_vocab(); s04_ira(); s05_ira_quiz(); s06_acabar(); s07_leles()
    s08_leles_quiz(); s09_reading(); s10_listening(); s11_creoque(); s12_creoque_quiz(); s13_speaking(); s14_writing()
    s15_comunicar(); s16_taller(); s17_cultura(); s18_tarea(); s19_mezcla(); s20_repaso()
    if include_teacher:
        s21_teacher()

def _repaint(path):
    import zipfile, os as _os
    reps = [("1E9E74", "7C56A9"), ("1e9e74", "7c56a9"), ("2EB085", "9374C2"), ("2eb085", "9374c2"),
            ("C5 · A1 · La Ruta", "C6+ · conectados")]
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
