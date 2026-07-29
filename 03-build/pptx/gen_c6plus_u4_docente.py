#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_c6plus_u4_docente.py — Interactieve PowerPoint C6+ · Unidad 4 «De viaje»
============================================================================
Zelfde engine/pijplijn als de golden sample (gen_u0_docente = de engine). Cursuskleur = PAARS.
Twee decks (.pptx): docente (oplossingen + notities) + alumno (F5, klik onthult).
Grammatica: pretérito perfecto compuesto (haber + participio) · por/para (intro).
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
OUT_DOCENTE = os.path.join(HERE, "C6plus_U4_docente.pptx")
OUT_ALUMNO_PPTX = os.path.join(HERE, "C6plus_U4_alumno.pptx")
TAB = "U4 · DE VIAJE"

def foot(s): footer(s, tab=TAB, page=pg())

# ============================================================ DIA 1 · TITLE
def s01_title():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(4.7), fill=G)
    rect(s, 0, Inches(4.7), EMU_W, Inches(0.09), fill=GD)
    text(s, Inches(0.6), Inches(0.35), Inches(3.4), Inches(3.6),
         [[("4", {"size": 260, "bold": True, "color": RGBColor(0x93, 0x74, 0xC2), "font": DISPLAY})]], anchor=MSO_ANCHOR.MIDDLE)
    chip(s, Inches(4.35), Inches(0.85), "LA RUTA · CHILE 🇨🇱 · DE VIAJE ✈️", fill=WHITE, tcolor=GD, size=12)
    text(s, Inches(4.3), Inches(1.35), Inches(8.6), Inches(1.5), [[("De viaje", {"size": 62, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(4.35), Inches(2.7), Inches(8.4), Inches(0.6),
         [[("Recente ervaringen: el perfecto (haber + participio) · por/para.", {"size": 15, "italic": True, "color": GT})]])
    text(s, Inches(4.35), Inches(3.35), Inches(8.4), Inches(0.9),
         [[("¿Has viajado alguna vez a un país hispano?", {"size": 22, "bold": True, "color": WHITE, "font": DISPLAY})],
          [("Ben je ooit naar een Spaanstalig land gereisd?", {"size": 13, "italic": True, "color": GT})]])
    text(s, Inches(0.6), Inches(4.95), Inches(6), Inches(0.4),
         [[("La gente de la ruta — parada 4: Chile, el gran viaje", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    x = Inches(0.6)
    for nm, city in [("lucia","Sevilla 🇪🇸"),("diego","CDMX 🇲🇽"),("valen","Cartagena 🇨🇴"),
                     ("nina","Cusco 🇵🇪"),("tu","Tú · Flandes 🇧🇪"),("mochila","La mochila")]:
        avatar(s, nm, x, Inches(5.4), Inches(1.0))
        text(s, x - Inches(0.15), Inches(6.42), Inches(1.3), Inches(0.5),
             [[(nm.capitalize() if nm != "tu" else "Tú", {"size": 10.5, "bold": True, "color": INK})],
              [(city.split("·")[-1].strip() if nm != "tu" else "de reiziger = jij", {"size": 8.5, "color": MUT})]], align=PP_ALIGN.CENTER)
        x = x + Inches(2.05)
    foot(s)
    notes(s, "TEACHER · TITLE. U4 = de eerste verleden tijd. Kerngrammatica: pretérito perfecto compuesto (haber + participio) + por/para. "
             "Parada 4 = Chile / el gran viaje. Kernvalstrikken: haber ≠ tener · onregelmatige participios (hecho/visto/dicho/vuelto) · por ≠ para. "
             "Docentdeck = oplossing; leerlingdeck (.pptx, F5) = klik onthult.")

# ============================================================ DIA 2 · MENU
def s02_menu():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "MENÚ DE LA LECCIÓN", "El mapa de la Unidad 4",
               "Kies je route — klik een tegel. Alles oefent naar de Tarea «Mi mejor viaje» toe.", num=4)
    tiles = [
        ("§1", "Transporte", "y alojamiento", G, 3),
        ("§2", "El perfecto", "haber + participio", G, 4),
        ("§2b", "Participios", "irregulares", G, 6),
        ("§3", "Por / para", "doel ↔ middel", G, 7),
        ("§4", "Experiencias", "ya · nunca · alguna vez", G, 11),
        ("★", "Lectura + escucha", "un viaje inolvidable", GD, 9),
        ("🗿", "Cultura", "el gran viaje", GD, 17),
        ("✈️", "Tarea · Mi viaje", "blog + opinión", GD, 18),
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
    notes(s, "TEACHER · LESSON_MENU. Kern = §2 el perfecto + §3 por/para. Kruisverwijzing: «oefen online — 12 juegos + 100+ oefeningen».")

# ============================================================ DIA 3 · VOCAB — transporte
def s03_vocab():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · VOCABULARIO", "Transporte y alojamiento", "De woorden van de reis — observa. Herken ze, dan gebruik je ze.", num=1)
    legend_func(s, Inches(9.7), Inches(0.55))
    rows = [("el avión", "het vliegtuig", "por avión"), ("el tren", "de trein", "la estación"),
            ("el billete", "het ticket", "de ida y vuelta"), ("la maleta", "de koffer", "hacer la maleta"),
            ("el hotel", "het hotel", "la reserva"), ("la habitación", "de kamer", "doble"),
            ("la llave", "de sleutel", "la recepción"), ("la playa", "het strand", "la montaña")]
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
           ("el avión, el tren, el billete, el hotel (m) · la maleta, la reserva, la llave, la playa (v)", {"size": 13, "color": INK})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.35), Inches(12.3), Inches(0.95),
             [[("Collocaties: ", {"bold": True, "color": GD}), ("comprar un billete · hacer la maleta · reservar una habitación · sacar fotos · coger el tren.", {"color": GD})],
              [("🔴 middel = por avión / por tren.", {"color": RED})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCABULARY. Media→viaje. Online: memoria del viaje (memory) + verbo↔participio (match).")

# ============================================================ DIA 4 · GRAMMAR — perfecto (color)
def s04_perfecto():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · GRAMÁTICA VISUAL", "El pretérito perfecto compuesto", "haber (he/has/ha…) + participio (-ado/-ido). «wat je gedaan hebt».", num=2)
    legend_func(s, Inches(9.7), Inches(0.55))
    seg = [("(Yo) ", F_SUBJ), ("he ", F_VERB), ("viajado ", F_OBJ), ("a Chile", F_PLAC)]
    runs = [[(t, {"size": 22, "bold": True, "color": c, "font": DISPLAY}) for t, c in seg]]
    card(s, Inches(0.5), Inches(1.7), Inches(12.3), Inches(1.2), fill=GT, line=None)
    text(s, Inches(0.8), Inches(1.7), Inches(11.7), Inches(1.2), runs, anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(3.15), Inches(12), Inches(0.4), [[("La conjugación de haber", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    frame = [("yo he", "he viajado"), ("tú has", "has comido"), ("él/ella ha", "ha salido"),
             ("nosotros hemos", "hemos visto"), ("vosotros habéis", "habéis reservado"), ("ellos han", "han llegado")]
    x0, y0 = Inches(0.5), Inches(3.6); cw = Inches(4.0); rh = Inches(0.62)
    for i, (a, b) in enumerate(frame):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.12))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(2.0), rh, [[(a, {"size": 11.5, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(2.15), y, cw - Inches(2.3), rh, [[(b, {"size": 10.5, "color": F_VERB, "bold": True})]], anchor=MSO_ANCHOR.MIDDLE)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.75), Inches(12.3), Inches(0.6),
             [[("Regla: ", {"bold": True, "color": GD}), ("haber (verandert) + participio (-ado/-ido, blijft gelijk). 🔴 haber ≠ tener: he comido, niet «tengo comido».", {"color": GD})]],
             trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR perfecto. Toon haber + participio. Online: completa el perfecto (cloze) + participio Tetris.")

# ============================================================ DIA 5 · QUIZ — perfecto (reveal)
def s05_perfecto_quiz():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · QUIZ", "¿Qué forma del perfecto?", "Klik een zin → de juiste vorm. Kijk naar de persoon.", num=2)
    items = [("(Yo) ___ (viajar) a Chile.", "he viajado"), ("¿(Tú) ___ (comer)?", "has comido"),
             ("Nosotros ___ (visitar) el museo.", "hemos visitado"), ("El avión ___ (llegar).", "ha llegado"),
             ("Mis amigos ___ (reservar).", "han reservado"), ("(Yo) ___ (dormir) mal.", "he dormido")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.78)
    for i, (q, a) in enumerate(items):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(4.0), rh, [[(q, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.2), y, cw - Inches(4.3), rh, [[("→ " + a, {"size": 12.5, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Truc: ", {"bold": True, "color": RED}), ("he/has/ha/hemos/habéis/han + participio (-ado/-ido). Het participio verandert niet.", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ perfecto (retrieval). Klas roept de vorm vóór de klik. Online: cloze el perfecto.")

# ============================================================ DIA 6 · GRAMMAR — participios irregulares (reveal)
def s06_participios():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2b · GRAMÁTICA", "Los participios irregulares", "Klik een verbo → het participio. Uit het hoofd leren.", num=2)
    items = [("hacer", "hecho"), ("ver", "visto"), ("decir", "dicho"), ("volver", "vuelto"),
             ("poner", "puesto"), ("escribir", "escrito"), ("abrir", "abierto"), ("romper", "roto")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.72)
    for i, (q, a) in enumerate(items):
        c = i // 4; r = i % 4; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.14))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(2.6), rh, [[(q, {"size": 12.5, "color": MUT})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(2.8), y, cw - Inches(2.9), rh, [[("→ " + a, {"size": 14, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.85), Inches(12.3), Inches(0.85),
             [[("Los 8 clásicos: ", {"bold": True, "color": GD}), ("hecho · visto · dicho · vuelto · puesto · escrito · abierto · roto.", {"color": GD})],
              [("🔴 acentos: leer → leído, oír → oído (i na klinker).", {"color": RED})]], trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR participios. Coro vóór de klik. Online: ¿regular o irregular? (classify) + participio Tetris.")

# ============================================================ DIA 7 · GRAMMAR — por/para (color)
def s07_porpara():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · GRAMÁTICA VISUAL", "Por y para", "para = doel/bestemming · por = middel/duur/reden.", num=3)
    legend_func(s, Inches(9.7), Inches(0.55))
    card(s, Inches(0.5), Inches(1.7), Inches(6.0), Inches(1.1), fill=GT, line=None)
    text(s, Inches(0.7), Inches(1.7), Inches(5.6), Inches(1.1),
         [[("Salgo ", {"size": 16, "color": INK}), ("para ", {"size": 18, "bold": True, "color": F_OBJ}), ("Chile", {"size": 16, "color": INK}), (".", {"size": 16, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
    card(s, Inches(6.8), Inches(1.7), Inches(6.0), Inches(1.1), fill=GT, line=None)
    text(s, Inches(7.0), Inches(1.7), Inches(5.6), Inches(1.1),
         [[("Viajo ", {"size": 16, "color": INK}), ("por ", {"size": 18, "bold": True, "color": F_VERB}), ("avión", {"size": 16, "color": INK}), (".", {"size": 16, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
    frame = [("para + destino", "para Chile"), ("para + inf. (doel)", "para descansar"), ("para + persona", "para ti"),
             ("por + medio", "por avión"), ("por + duración", "por dos días"), ("por + causa", "por el mal tiempo")]
    x0, y0 = Inches(0.5), Inches(3.15); cw = Inches(4.0); rh = Inches(0.62)
    for i, (a, b) in enumerate(frame):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.12))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(2.1), rh, [[(a, {"size": 11, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(2.25), y, cw - Inches(2.4), rh, [[(b, {"size": 10.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.75),
             [[("Regla: ", {"bold": True, "color": GD}), ("para = doel/bestemming/«om te» · por = middel/duur/reden/doorheen. Viajo por avión para visitar Chile.", {"color": GD})]],
             trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR por/para. Toon het contrast. Online: ¿por o para? (classify) + cloze.")

# ============================================================ DIA 8 · QUIZ — por/para (reveal)
def s08_porpara_quiz():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · QUIZ", "¿por o para?", "Klik een zin → de juiste optie.", num=3)
    items = [("Salgo ___ Chile.", "para"), ("Viajo ___ avión.", "por"), ("Estudio ___ aprobar.", "para"),
             ("Me quedo ___ dos días.", "por"), ("Es ___ ti.", "para"), ("Paseo ___ la playa.", "por")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.78)
    for i, (q, a) in enumerate(items):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(4.3), rh, [[(q, {"size": 12.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.5), y, cw - Inches(4.6), rh, [[("→ " + a, {"size": 14, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Regla: ", {"bold": True, "color": GD}), ("para = doel/bestemming · por = middel/duur/reden. Bij twijfel: «waarheen/waarvoor» = para.", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ por/para (retrieval). Online: ¿por o para? (classify) + cloze.")

# ============================================================ DIA 9 · READING
def s09_reading():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§5 · LEER · COMPRENSIÓN", "Dos viajes — «Un viaje inolvidable»", "Lees. Klik een vraag → het antwoord verschijnt.", num=5)
    card(s, Inches(0.5), Inches(1.65), Inches(5.6), Inches(3.9), fill=GT, line=G, lw=1.4)
    avatar(s, "nina", Inches(0.85), Inches(1.95), Inches(1.0))
    text(s, Inches(2.05), Inches(1.98), Inches(3.9), Inches(1.5),
         [[("«Este año he viajado a Chile. Hemos estado en el desierto de Atacama y he visto un cielo lleno de estrellas. Lo mejor ha sido el paisaje. Todavía no he estado en Rapa Nui.»", {"size": 11, "italic": True, "color": INK})]], line=1.16)
    avatar(s, "diego", Inches(0.85), Inches(3.65), Inches(1.0))
    text(s, Inches(2.05), Inches(3.68), Inches(3.9), Inches(1.5),
         [[("«He vuelto de un viaje por Europa. He probado la paella en València, he hecho muchas fotos y he escrito un diario. Lo peor ha sido el vuelo, muy largo.»", {"size": 11, "italic": True, "color": INK})]], line=1.16)
    qa = [("¿Adónde ha viajado Nina?", "A Chile"), ("¿Ya ha estado en Rapa Nui?", "Todavía no"),
          ("¿Qué ha probado Diego?", "La paella"), ("¿Qué ha sido lo peor (Diego)?", "El vuelo")]
    x = Inches(6.4); y = Inches(1.7)
    for q, a in qa:
        card(s, x, y, Inches(6.4), Inches(0.85), fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y + Inches(0.06), Inches(6.1), Inches(0.4), [[(q, {"size": 12.5, "bold": True, "color": GD})]])
        rev = text(s, x + Inches(0.15), y + Inches(0.44), Inches(6.1), Inches(0.35), [[("→ " + a, {"size": 12, "color": INK})]])
        register_reveal(s, rev); y = y + Inches(0.98)
    btn = noodroute(s)
    exercise_solucion(s, Inches(6.4), Inches(5.65), Inches(6.4), Inches(0.6),
             [[("🎯 Leesdoel: ", {"bold": True, "color": GD}), ("scannen naar het perfecto (he/ha…) + lo mejor/lo peor.", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · READING (lezen→schrijven). Eerst globaal, dan scannen. Daarna: eigen reis met el perfecto.")

# ============================================================ DIA 10 · LISTENING
def s10_listening():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · ESCUCHAR · INTERACCIÓN", "¿Qué tal el viaje?", "Volg het verhaal. Klik un dato → de info. (audio + script op de web)", num=2)
    pasos = [("🔊 ¿Adónde?", "Ha ido a Chile"), ("🔊 ¿Qué ha visto?", "El desierto, las estrellas"),
             ("🔊 ¿Qué ha hecho?", "Ha sacado fotos, ha subido"), ("🔊 ¿Lo mejor?", "El paisaje, inolvidable")]
    x0, y0 = Inches(0.7), Inches(1.9); cw = Inches(2.95); ch = Inches(2.4)
    for i, (mom, det) in enumerate(pasos):
        x = x0 + i * (cw + Inches(0.1))
        card(s, x, y0, cw, ch, fill=WHITE, line=LINE, lw=1.2); rect(s, x, y0, cw, Inches(0.5), fill=GT)
        text(s, x, y0, cw, Inches(0.5), [[("dato " + str(i+1), {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(0.15), y0 + Inches(0.7), cw - Inches(0.3), Inches(0.7), [[(mom, {"size": 14, "bold": True, "color": INK, "font": DISPLAY})]], line=1.05)
        rev = text(s, x + Inches(0.15), y0 + Inches(1.5), cw - Inches(0.3), Inches(0.7), [[(det, {"size": 11, "color": G})]], line=1.05)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.85),
             [[("Modelo-audio (docent/TTS): ", {"bold": True, "color": GD}),
               ("«He viajado a Chile. He visto el desierto y he sacado muchas fotos. Lo mejor ha sido el paisaje.» ", {"color": GD})],
              [("Daarna: A vertelt zijn reis, B stelt vragen (perfecto).", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · LISTENING (luisteren→spreken). Lees voor (of TTS); klas noteert adónde/qué. Online: ¿qué tal el viaje? (audio).")

# ============================================================ DIA 11 · GRAMMAR — marcadores (reveal)
def s11_marcadores():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · GRAMÁTICA", "Los marcadores del perfecto", "Klik een cue → de betekenis. ya · todavía no · nunca · alguna vez.", num=4)
    items = [("al (gedaan)", "ya"), ("nog niet", "todavía no"), ("nooit", "nunca"), ("ooit?", "¿… alguna vez?"),
             ("dit jaar", "este año"), ("deze week", "esta semana"), ("vandaag", "hoy"), ("de laatste tijd", "últimamente")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.72)
    for i, (q, a) in enumerate(items):
        c = i // 4; r = i % 4; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.14))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(2.6), rh, [[(q, {"size": 12, "color": MUT})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(2.8), y, cw - Inches(2.9), rh, [[("→ " + a, {"size": 13, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.85), Inches(12.3), Inches(0.85),
             [[("Chunks: ", {"bold": True, "color": GD}), ("¿Has estado alguna vez en…? — Sí, una vez. / No, nunca. / Todavía no.", {"color": GD})],
              [("Deze markers horen bij het perfecto (recente/onbepaalde tijd).", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR marcadores. Koppel aan het perfecto. Online: marcadores in de cloze/point.")

# ============================================================ DIA 12 · QUIZ — mezcla perfecto (reveal)
def s12_mezcla_perf():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2–§3 · QUIZ", "Perfecto + participios", "Klik → de juiste vorm. Let op de onregelmatige.", num=2)
    items = [("(Yo) ___ (hacer) las maletas.", "he hecho"), ("¿(Tú) ___ (ver) el mar?", "has visto"),
             ("Nosotros ___ (volver).", "hemos vuelto"), ("(Yo) ___ (escribir) una postal.", "he escrito"),
             ("Han ___ (abrir) el museo.", "abierto"), ("¿Has estado ___ vez en Perú?", "alguna")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.78)
    for i, (q, a) in enumerate(items):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(4.0), rh, [[(q, {"size": 11.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.2), y, cw - Inches(4.3), rh, [[("→ " + a, {"size": 12.5, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Irregulares: ", {"bold": True, "color": G}), ("hecho · visto · dicho · vuelto · puesto · escrito · abierto · roto.", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ mezcla (retrieval). Zonder waarschuwing door elkaar. Online: cloze + participio Tetris.")

# ============================================================ DIA 13 · SPEAKING
def s13_speaking():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · SPEAKING · INTERACCIÓN", "Habla de un viaje", "Speel de scène met de frames. Steun bouwt af: kaarten → beginwoorden → uit het hoofd.", num=2)
    avatar(s, "tu", Inches(11.4), Inches(1.7), Inches(1.3))
    labels = ["¿Adónde?", "¿Cómo? (por)", "¿Qué has visto?", "¿Qué has hecho?", "¿Lo mejor?", "Argumento"]
    frames = ["He viajado a…", "Por avión/tren…", "He visto…", "He hecho / probado…", "Lo mejor ha sido…", "…porque…"]
    x0, y0 = Inches(0.5), Inches(1.8); cw = Inches(3.4); rh = Inches(0.8)
    for i, (lab, fr) in enumerate(zip(labels, frames)):
        c = i // 3; r = i % 3; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.18))
        card(s, x, y, cw, rh, fill=WHITE, line=G, lw=1.2, shadow=False)
        text(s, x + Inches(0.15), y + Inches(0.05), cw - Inches(0.3), Inches(0.32), [[(lab, {"size": 10, "color": MUT})]])
        text(s, x + Inches(0.15), y + Inches(0.36), cw - Inches(0.3), Inches(0.4), [[(fr, {"size": 12.5, "bold": True, "color": GD, "font": DISPLAY})]])
    chip(s, Inches(0.5), Inches(4.65), "🎙️ Grábate online · «Mensaje de voz: mi viaje / mi opinión»", fill=GT, tcolor=GD, size=11)
    text(s, Inches(0.5), Inches(5.05), Inches(10.5), Inches(0.9),
         [[("Ronda 1: ", {"size": 12, "bold": True, "color": GD}), ("met de kaarten. ", {"size": 12, "color": INK}),
           ("Ronda 2: ", {"size": 12, "bold": True, "color": GD}), ("beginwoorden. ", {"size": 12, "color": INK}),
           ("Ronda 3: ", {"size": 12, "bold": True, "color": GD}), ("uit het hoofd. ", {"size": 12, "color": INK}),
           ("Ronda 4: ", {"size": 12, "bold": True, "color": GD}), ("grábate.", {"size": 12, "color": INK})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.6), Inches(12.3), Inches(0.65),
             [[("Modelo: ", {"bold": True, "color": GD}), ("«He viajado a Chile por avión. He visto el desierto y he sacado muchas fotos. Lo mejor ha sido el paisaje porque es impresionante.»", {"color": GD})]],
             trigger=btn, title_doc="MODELO · docent")
    foot(s)
    notes(s, "TEACHER · SPEAKING (interactie). Rondes met afbouwende steun. Online: recorder (mi viaje + mi opinión).")

# ============================================================ DIA 14 · WRITING
def s14_writing():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "WRITING · PRODUCCIÓN", "Mi mejor viaje", "Schrijf je reisblog. Klik → een modeltekst verschijnt.", num=5)
    card(s, Inches(0.5), Inches(1.7), Inches(6.0), Inches(3.9), fill=WHITE, line=LINE, lw=1.2)
    text(s, Inches(0.7), Inches(1.85), Inches(5.6), Inches(0.4), [[("✍️ Escribe tu blog de viaje:", {"size": 12, "bold": True, "color": GD})]])
    for i in range(6):
        rect(s, Inches(0.7), Inches(2.4) + i * Inches(0.5), Inches(5.6), Inches(0.01), fill=LINE)
    chk = ["adónde has viajado (+ por)", "3–4 experiencias (he visto/hecho…)", "2 participios irregulares", "por/para correct", "una opinión (lo mejor ha sido…)", "6–8 frases"]
    x = Inches(6.9); y = Inches(1.7)
    text(s, x, y, Inches(6), Inches(0.4), [[("Checklist:", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    for i, c in enumerate(chk):
        text(s, x, y + Inches(0.5) + i * Inches(0.45), Inches(6), Inches(0.4), [[("☐  " + c, {"size": 13, "color": INK})]])
    rev = card(s, x, Inches(4.35), Inches(6.0), Inches(1.25), fill=GT, line=G, lw=1.2)
    text(s, x + Inches(0.15), Inches(4.4), Inches(5.7), Inches(1.2),
         [[("Modelo: ", {"size": 12, "bold": True, "color": GD}),
           ("«Este año he viajado a Chile por avión para descansar. He estado en Atacama y he visto las estrellas. He hecho muchas fotos. Lo mejor ha sido el paisaje. ¡Ha sido inolvidable!»", {"size": 11, "italic": True, "color": INK})]], line=1.13)
    register_reveal(s, rev)
    noodroute(s); foot(s)
    notes(s, "TEACHER · WRITING (lezen→schrijven). Checklist = zichtbare steun; onthul het model pas na het schrijven. Nakijkfocus: haber+participio, por/para, opinión. Voedt de Tarea.")

# ============================================================ DIA 15 · VOCAB — experiencias (reveal)
def s15_experiencias():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · VOCABULARIO", "Experiencias y lugares", "Klik een kaart → la respuesta. Bouw je woordnetwerk.", num=4)
    data = [("he estado", "ik ben geweest"), ("he visto", "ik heb gezien"), ("he probado", "ik heb geproefd"), ("la playa", "het strand"),
            ("la montaña", "de berg"), ("el desierto", "de woestijn"), ("el paisaje", "het landschap"), ("impresionante", "indrukwekkend"),
            ("inolvidable", "onvergetelijk"), ("lo mejor", "het beste"), ("lo peor", "het ergste"), ("ya / todavía no", "al / nog niet")]
    x0, y0 = Inches(0.5), Inches(1.7); cw = Inches(3.0); rh = Inches(0.7)
    for i, (es, nl) in enumerate(data):
        c = i % 4; r = i // 4; x = x0 + c * (cw + Inches(0.1)); y = y0 + r * (rh + Inches(0.14))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.12), y, Inches(1.8), rh, [[(es, {"size": 11, "bold": True, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(1.75), y, cw - Inches(1.85), rh, [[("→ " + nl, {"size": 10.5, "color": G})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.9),
             [[("Opinión: ", {"bold": True, "color": GD}), ("Lo mejor ha sido… · Lo peor ha sido… · Ha sido impresionante/inolvidable.", {"color": GD})],
              [("Experiencias: he estado/visto/hecho/probado + ya/todavía no/nunca/alguna vez.", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCAB experiencias. Klik onthult. Online: memoria de acciones + señala.")

# ============================================================ DIA 16 · TALLER
def s16_taller():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "TALLER DE LENGUA", "La h muda + conectores", "Klik een item → correcte vorm. Gereedschap voor spelling en volgorde.", num=1)
    text(s, Inches(0.5), Inches(1.5), Inches(6), Inches(0.35), [[("A · ortografía: la h muda (klinkt niet)", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    fixes = [("___e comido", "he comido"), ("el ___otel", "hotel"), ("___acer → ___echo", "hacer → hecho"), ("la ___abitación", "habitación")]
    y = Inches(1.95)
    for q, a in fixes:
        card(s, Inches(0.5), y, Inches(6.0), Inches(0.6), fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, Inches(0.62), y, Inches(2.8), Inches(0.6), [[(q, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, Inches(3.5), y, Inches(2.9), Inches(0.6), [[("→ " + a, {"size": 12, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y = y + Inches(0.72)
    text(s, Inches(6.9), Inches(1.5), Inches(6), Inches(0.35), [[("B · conectores: cuenta tu viaje", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    conn = [("primero", "eerst"), ("luego / después", "daarna"), ("más tarde", "later"), ("al final", "ten slotte")]
    y = Inches(1.95)
    for q, a in conn:
        card(s, Inches(6.9), y, Inches(5.9), Inches(0.6), fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, Inches(7.02), y, Inches(2.6), Inches(0.6), [[(q, {"size": 12, "bold": True, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, Inches(9.7), y, Inches(3.0), Inches(0.6), [[("→ " + a, {"size": 11.5, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y = y + Inches(0.72)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.85),
             [[("A: ", {"bold": True, "color": GD}), ("de h wordt geschreven maar niet uitgesproken: he, has, hotel, hacer → hecho. 🔴 nooit «e comido».", {"color": GD})],
              [("B: primero → luego/después → más tarde → al final (om je reis te vertellen).", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · TALLER. h muda (cruciaal in he/has/ha) + tijdsconnectoren. Online: drills in de hub.")

# ============================================================ DIA 17 · CULTURE
def s17_cultura():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "CULTURA · PARADA 4: CHILE", "El gran viaje hispano", "Klik een kaart → het weetje. Atacama, el Camino y Rapa Nui.", num=1)
    cards = [("🏜️ El desierto de Atacama", "In Chile ligt de droogste woestijn ter wereld. 's Nachts zie je er de helderste sterrenhemel — grote sterrenwachten.", "Nina ha estado allí"),
             ("🥾 El Camino de Santiago", "In España lopen pelgrims al eeuwen de Camino naar Santiago. «He hecho el Camino» is een klassiek reisverhaal — honderden km te voet.", "un clásico"),
             ("🗿 Rapa Nui", "Isla de Pascua (Chile), midden in de Stille Oceaan, is beroemd om de moáis: reusachtige stenen beelden. Zeer afgelegen.", "todavía no…")]
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
             [[("Actividad: ", {"bold": True, "color": GD}), ("¿adónde has viajado o quieres viajar? Cuenta con el perfecto (he estado…) o «todavía no».", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · CULTURE (LPD 5). Onthul per kaart. Bruggetje: La Ruta parada 4 = Chile (★, viaje). Online: klik op Chile op de kaart.")

# ============================================================ DIA 18 · FINAL_MISSION
def s18_tarea():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(1.35), fill=GD)
    text(s, Inches(0.5), Inches(0.18), Inches(9), Inches(1.0),
         [[("✈️ Tarea final · Mi mejor viaje", {"size": 27, "bold": True, "color": WHITE, "font": DISPLAY})],
          [("Escribe un blog sobre un viaje con el perfecto, por/para y una opinión.", {"size": 13, "italic": True, "color": GT})]])
    avatar(s, "mochila", Inches(11.6), Inches(0.2), Inches(1.0))
    pasos = [("1", "Di adónde has viajado", "«He viajado a… por avión/tren»"),
             ("2", "Cuenta 3–4 experiencias", "«He visto…, he probado…, he hecho…»"),
             ("3", "Usa por/para", "«para descansar», «por una semana»"),
             ("4", "Añade tu opinión", "«Lo mejor ha sido… porque…»"),
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
    crit = ["perfecto (haber+part.)", "2 irregulares", "por/para", "una opinión"]
    x = Inches(0.5)
    for c in crit:
        chip(s, x, Inches(5.45), "☐ " + c, fill=GT, tcolor=GD, size=10, w=Inches(3.05)); x = x + Inches(3.15)
    text(s, Inches(0.5), Inches(6.05), Inches(12), Inches(0.4),
         [[("🎯 ", {"size": 12}), ("Afzender jij · ontvanger de klas · doel je reis delen · situatie een blog · resultaat: blog + presentación oral.", {"size": 11.5, "italic": True, "color": MUT})]])
    foot(s)
    notes(s, "TEACHER · FINAL_MISSION (communicatieve eindtaak). Beoordeel met de rúbrica; opname op de web.")

# ============================================================ DIA 19 · MEZCLA
def s19_mezcla():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "QUIZ · LA MEZCLA", "Ophaal door elkaar", "Gemengde ophaal van de hele unit. Klik → het antwoord. (retrieval)", num=1)
    items = [("«ik heb gereisd» =", "he viajado"), ("hacer → participio", "hecho"),
             ("ver → participio", "visto"), ("Salgo ___ Chile", "para"),
             ("Viajo ___ avión", "por"), ("«nog niet» =", "todavía no"),
             ("volver → participio", "vuelto"), ("El viaje ___ sido genial", "ha")]
    x0, y0 = Inches(0.5), Inches(1.75); cw = Inches(6.05); rh = Inches(0.62)
    for i, (q, a) in enumerate(items):
        c = i // 4; r = i % 4; x = x0 + c * (cw + Inches(0.2)); y = y0 + r * (rh + Inches(0.16))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x + Inches(0.15), y, Inches(4.0), rh, [[(q, {"size": 11.5, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        rev = text(s, x + Inches(4.15), y, cw - Inches(4.3), rh, [[("→ " + a, {"size": 12, "bold": True, "color": GD})]], anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.05), Inches(12.3), Inches(0.55),
             [[("Alles komt terug: ", {"bold": True, "color": GD}), ("perfecto · participios irregulares · por/para · marcadores.", {"color": GD})]], trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ mezcla (retrieval vóór herlezen). Exit-ticket. Zwakke punten → terug via menu.")

# ============================================================ DIA 20 · REPASO
def s20_repaso():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "REPASO · LO ESENCIAL", "Lo esencial de un vistazo", "De volledige herhaling (12 spellen, drills) staat online. Hier: de kern + semáforo.", num=1)
    ess = ["Perfecto: haber (he/has/ha/hemos/habéis/han) + participio (-ado/-ido). He viajado.",
           "Participios irregulares: hecho · visto · dicho · vuelto · puesto · escrito · abierto · roto.",
           "Marcadores: hoy · esta semana · este año · ya · todavía no · nunca · alguna vez.",
           "Para = doel/bestemming/«om te» · Por = middel/duur/reden/doorheen.",
           "🔴 Trampas: haber ≠ tener · vergeet de h niet (he, has) · hecho/visto (irreg.) · por ≠ para."]
    card(s, Inches(0.5), Inches(1.6), Inches(12.3), Inches(2.5), fill=CREMA, line=None)
    y = Inches(1.8)
    for e in ess:
        text(s, Inches(0.8), y, Inches(11.8), Inches(0.45), [[("• ", {"size": 13, "bold": True, "color": GD}), (e, {"size": 12, "color": INK})]])
        y = y + Inches(0.46)
    text(s, Inches(0.5), Inches(4.3), Inches(12), Inches(0.35), [[("Semáforo — ¿cómo lo llevas?", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    can = ["over transport en verblijf praten", "de perfecto vormen (haber + participio)", "de onregelmatige participios gebruiken", "por en para onderscheiden", "een reis vertellen met een mini-mening"]
    y = Inches(4.75)
    for c in can:
        text(s, Inches(0.8), y, Inches(7.0), Inches(0.4), [[(c, {"size": 12, "color": INK})]], anchor=MSO_ANCHOR.MIDDLE)
        for j, (em, col) in enumerate([("🔴", RED), ("🟠", AMBER), ("🟢", G)]):
            chip(s, Inches(8.0) + j * Inches(1.5), y + Inches(0.03), em + " ", fill=WHITE, tcolor=col, size=12, w=Inches(1.3))
        y = y + Inches(0.42)
    foot(s)
    notes(s, "TEACHER · FEEDBACK/REPASO. Semáforo = zelfevaluatie. Repaso-drills online (12 spellen). Bruggetje: U5 «Érase una vez» — el indefinido, biografías (Mateo, BsAs).")

# ============================================================ DIA 21 · TEACHER
def s21_teacher():
    s = slide(); bg(s, GD)
    text(s, Inches(0.6), Inches(0.4), Inches(12), Inches(0.8), [[("TEACHER_NOTES · U4 «De viaje»", {"size": 26, "bold": True, "color": WHITE, "font": DISPLAY})]])
    blocks = [("Timing (50 min)", "Menu 2' · transporte 6' · el perfecto 12' · participios 6' · por/para 10' · experiencias/escucha 8' · Tarea-briefing 4'."),
              ("Kernvalstrikken", "haber ≠ tener (he comido, niet «tengo comido») · onregelmatige participios (hecho/visto/dicho/vuelto/puesto/escrito/abierto/roto) · h muda (vergeet de h niet) · por (middel/duur/reden) ≠ para (doel/bestemming)."),
              ("Differentiatie", "Sterker: volledig reisverhaal + 3 irregulares + por/para + una opinión con porque. Zwakker: perfecto-kaart + participios-lijst langer open, frames houden; por/para met vaste voorbeeldparen."),
              ("Digitaal", "12 spellen + flip cards + gramática interactiva (perfecto · participios · por/para) + recorder (mi viaje · mi opinión) + Lectura (dos viajes) + klikbare kaart (Chile ★, viaje) op de página digital. QR's → juiste anker."),
              ("Evaluatie & LPD", "Tarea «Mi mejor viaje» met rúbrica (4 criteria). LPD (III-Spa-d): viaje 7 · perfecto 8·3 · participios/por-para 8 · interactie 4 · lezen 1·2·5 · cultuur 5. Bron: perfecto = A2-kern (leerplan) + reservoir.")]
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
    s01_title(); s02_menu(); s03_vocab(); s04_perfecto(); s05_perfecto_quiz(); s06_participios(); s07_porpara()
    s08_porpara_quiz(); s09_reading(); s10_listening(); s11_marcadores(); s12_mezcla_perf(); s13_speaking(); s14_writing()
    s15_experiencias(); s16_taller(); s17_cultura(); s18_tarea(); s19_mezcla(); s20_repaso()
    if include_teacher:
        s21_teacher()

def _repaint(path):
    import zipfile, os as _os
    reps = [("1E9E74", "7C56A9"), ("1e9e74", "7c56a9"), ("2EB085", "9374C2"), ("2eb085", "9374c2"),
            ("C5 · A1 · La Ruta", "C6+ · de viaje")]
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
