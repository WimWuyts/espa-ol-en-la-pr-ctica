#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_u7_docente.py — Interactieve PowerPoint C5 · Unidad 7 «Mi casa y mi barrio» (parada Colombia/Cartagena)
=========================================================================================================
Zelfde engine/pijplijn als de golden sample U0/U5 (gen_u0_docente wordt geïmporteerd:
low-level helpers, on-click <p:timing>-animaties, hyperlink-navigatie). Enkel de SLIDES
zijn U7-specifiek. Twee decks (beide .pptx):
  · C5_U7_docente.pptx — vrije navigatie, oplossingen bij klik + didactiek in spreker-notities.
  · C5_U7_alumno.pptx  — gewone diavoorstelling, antwoorden verschijnen bij klik (F5, geen kiosk).
Huisstijl groen (C5). Spaans-eerst + NL-steun. >=20 dia's. Dekt de vier vaardigheden. Valen = gastvrouw.
"""
import os
import gen_u0_docente as E
from gen_u0_docente import (
    slide, bg, rect, text, chip, avatar, card, sectionbar, footer, noodroute,
    exercise_solucion, check_badge, legend_func, link_to, register_reveal, notes, pg,
    G, GD, GT, INK, MUT, PAPER, CREMA, LINE, RED, AMBER, WHITE,
    F_SUBJ, F_VERB, F_OBJ, F_TIME, F_PLAC, F_NEG, F_STRA, ACC,
    DISPLAY, BODY, HAND, EMU_W, EMU_H,
    Inches, Pt, RGBColor, PP_ALIGN, MSO_ANCHOR,
)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DOCENTE = os.path.join(HERE, "C5_U7_docente.pptx")
OUT_ALUMNO_PPTX = os.path.join(HERE, "C5_U7_alumno.pptx")
TAB = "U7 · MI CASA Y MI BARRIO"

def foot(s): footer(s, tab=TAB, page=pg())

# ============================================================ DIA 1 · TITLE
def s01_title():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(4.7), fill=G)
    rect(s, 0, Inches(4.7), EMU_W, Inches(0.09), fill=GD)
    text(s, Inches(0.6), Inches(0.35), Inches(3.4), Inches(3.6),
         [[("7", {"size": 260, "bold": True, "color": RGBColor(0x2E,0xB0,0x85), "font": DISPLAY})]],
         anchor=MSO_ANCHOR.MIDDLE)
    chip(s, Inches(4.35), Inches(0.85), "LA RUTA · PARADA 7 · CARTAGENA · COLOMBIA 🇨🇴", fill=WHITE, tcolor=GD, size=12)
    text(s, Inches(4.3), Inches(1.35), Inches(8.6), Inches(1.5),
         [[("Mi casa y mi barrio", {"size": 48, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(4.35), Inches(2.7), Inches(8.4), Inches(0.6),
         [[("La casa, las habitaciones, dónde está todo y cómo llegar — en Cartagena, con Valen.", {"size": 15, "italic": True, "color": GT})]])
    text(s, Inches(4.35), Inches(3.35), Inches(8.4), Inches(0.9),
         [[("¿Dónde vives? ¿Cómo es tu barrio?", {"size": 23, "bold": True, "color": WHITE, "font": DISPLAY})],
          [("Waar woon je? Hoe is jouw buurt?", {"size": 13, "italic": True, "color": GT})]])
    text(s, Inches(0.6), Inches(4.95), Inches(6), Inches(0.4),
         [[("La gente de la ruta — je reisgezellen", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    x = Inches(0.6)
    for nm, city in [("valen","Cartagena 🇨🇴 · anfitriona"),("lucia","Sevilla 🇪🇸"),("diego","CDMX 🇲🇽"),
                     ("nina","Cusco 🇵🇪"),("tu","Tú · Flandes 🇧🇪"),("mochila","La mochila")]:
        avatar(s, nm, x, Inches(5.4), Inches(1.0))
        text(s, x - Inches(0.15), Inches(6.42), Inches(1.3), Inches(0.5),
             [[(nm.capitalize() if nm!="tu" else "Tú", {"size": 10.5, "bold": True, "color": INK})],
              [(city.split("·")[-1].strip() if nm!="tu" else "de reiziger = jij", {"size": 8.5, "color": MUT})]],
             align=PP_ALIGN.CENTER)
        x = x + Inches(2.05)
    foot(s)
    notes(s, "TEACHER · TITLE. Parada 7 = Cartagena (Colombia): bajamos por el Caribe. Gastvrouw = Valen. Doel: la casa/habitaciones/muebles "
             "benoemen, hay/estar (er is/waar het staat), preposiciones de lugar, estar + gerundio (nu bezig), imperativo (de weg wijzen) en "
             "ordinales + apócope (el primer piso). Kernvalstrik: niet «hay el parque»; de+el=del; estoy comiendo; el primer piso. "
             "Docentdeck = vrije navigatie + oplossing in notities; leerlingdeck (.pptx, F5) = elke klik onthult het volgende antwoord.")

# ============================================================ DIA 2 · LESSON_MENU
def s02_menu():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "MENÚ DE LA LECCIÓN", "El mapa de la Unidad 7",
               "Kies je route — klik een tegel. Alles oefent naar de Tarea «Mi barrio» toe.", num=7)
    tiles = [
        ("§1", "Hay / estar", "er is · waar het staat", G, 3),
        ("§2", "Preposiciones", "encima de · al lado de", G, 6),
        ("§3", "Estar + gerundio", "estoy cocinando", G, 11),
        ("§4", "El camino", "imperativo: gira, sigue", G, 12),
        ("§5", "Lectura + escucha", "anuncio de piso · barrio", G, 9),
        ("★", "Cultura · la plaza", "el barrio · Cartagena", GD, 16),
        ("🏘️", "Tarea · Mi barrio", "plano + visita guiada", GD, 18),
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
        tf=b.text_frame; tf.vertical_anchor=MSO_ANCHOR.MIDDLE; p=tf.paragraphs[0]; p.alignment=PP_ALIGN.CENTER
        rr=p.add_run(); rr.text=tag; rr.font.size=Pt(12); rr.font.bold=True; rr.font.name=DISPLAY; rr.font.color.rgb=col
        text(s, x + Inches(0.58), y + Inches(0.06), tw - Inches(0.7), Inches(0.4),
             [[(es, {"size": 14.5, "bold": True, "color": WHITE, "font": DISPLAY})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(0.18), y + Inches(0.68), tw - Inches(0.36), Inches(1.2), [[(nl, {"size": 11.5, "color": INK})]], line=1.12)
        chip(s, x + Inches(0.18), y + th - Inches(0.45), f"→ dia {dia}", fill=GT, tcolor=GD, size=9.5)
    foot(s)
    notes(s, "TEACHER · LESSON_MENU. Elke tegel = hyperlink; op elke oefendia staat ⌂ Menú terug. Richttijd 50 min. "
             "Begin bij §1 (hay/estar) → §2 (preposiciones) = het hart van de unit. Kruisverwijzing print/HTML: «oefen online — 20 juegos».")

# ============================================================ DIA 3 · VOCABULARY — la casa
def s03_vocab():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · VOCABULARIO", "La casa y las habitaciones", "De woorden van thuis — observa. Herken ze, dan gebruik je ze.", num=1)
    legend_func(s, Inches(9.7), Inches(0.55))
    rows = [("la casa","het huis","el piso · el apartamento"),("la habitación","de kamer","el dormitorio · el salón"),
            ("la cocina","de keuken","el baño · el comedor"),("los muebles","de meubels","la mesa · la silla"),
            ("el sofá","de bank","la cama · el armario"),("la puerta","de deur","la ventana · la pared"),
            ("la escalera","de trap","el ascensor · el pasillo"),("la terraza","het terras","el jardín 🌳"),]
    x0,y0 = Inches(0.5), Inches(1.6); cw=Inches(6.1); rh=Inches(0.6)
    for i,(k,v,nl) in enumerate(rows):
        c = 0 if i<4 else 1; r = i%4
        x = x0 + c*(cw+Inches(0.15)); y = y0 + r*(rh+Inches(0.12))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x+Inches(0.15), y, Inches(2.4), rh, [[(k, {"size":13,"bold":True,"color":GD})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x+Inches(2.5), y, Inches(2.3), rh, [[(v, {"size":12,"color":INK})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x+Inches(4.6), y, Inches(1.4), rh, [[(nl, {"size":9,"italic":True,"color":MUT})]], anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(4.75), Inches(12.3), Inches(0.5),
         [[("Preposiciones de lugar: ", {"size":13,"bold":True,"color":GD,"font":DISPLAY}),
           ("encima de", {"size":13,"bold":True,"color":F_PLAC}), (" · ",{"size":13,"color":INK}),
           ("al lado de", {"size":13,"bold":True,"color":F_PLAC}), (" · ",{"size":13,"color":INK}),
           ("entre · debajo de · enfrente de · dentro de", {"size":13,"bold":True,"color":F_PLAC})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.35), Inches(12.3), Inches(0.95),
             [[("🔴 Hay vs. estar: ", {"bold":True,"color":RED}), ("Hay un sofá (nieuw) · El sofá está al lado (bekend + plaats).", {"bold":True,"color":GD})],
              [("Nooit «hay el/la…». De casa = habitaciones (kamers) + muebles (meubels).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCABULARY. Toon per cluster (casa/habitaciones/muebles). Laat raden zónder de NL-gloss. "
             "Online: flip cards + Memoria de la casa + Memoria del barrio + ¿hay o está?")

# ============================================================ DIA 4 · GRAMMAR — hay/estar (color)
def s04_hayestar():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · GRAMÁTICA VISUAL", "Hay / estar — ¿qué hay y dónde está?", "Kleur = de plaats. Hay = nieuw · estar = waar iets bekends staat.", num=1)
    legend_func(s, Inches(9.7), Inches(0.55))
    seg = [("En mi barrio ", INK),("hay ", F_OBJ),("una plaza,", INK),(" y la iglesia ", INK),
           ("está ", F_VERB),("enfrente ", F_PLAC),("de la plaza.", INK)]
    runs=[[(t,{"size":22,"bold":True,"color":c,"font":DISPLAY}) for t,c in seg]]
    card(s, Inches(0.5), Inches(1.7), Inches(12.3), Inches(1.2), fill=GT, line=None)
    text(s, Inches(0.8), Inches(1.7), Inches(11.7), Inches(1.2), runs, anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(3.15), Inches(12), Inches(0.4), [[("¿hay o estar? — la decisión", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    frame=[("hay","+ un/una/número (nieuw)"),("hay","geen el/la: «hay un parque»"),("está","el/la + singular + plaats"),
           ("están","los/las + plural + plaats"),("está","«La plaza está en el centro»"),("están","«Los baños están arriba»")]
    x0,y0=Inches(0.5),Inches(3.6); cw=Inches(4.0); rh=Inches(0.62)
    for i,(a,b) in enumerate(frame):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.12))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(1.3),rh,[[(a,{"size":12.5,"bold":True,"color":F_VERB})]],anchor=MSO_ANCHOR.MIDDLE)
        text(s,x+Inches(1.45),y,cw-Inches(1.6),rh,[[(b,{"size":10.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.7), Inches(12.3), Inches(0.7),
             [[("Regla: ", {"bold":True,"color":GD}), ("hay = er is/zijn (nieuw, geen el/la) · está/están = waar iets bekends staat (met el/la + plaats).", {"color":GD})]],
             trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR (color-coding). Maak het contrast fysiek zichtbaar. Truc: un/una/número → hay; el/la + plaats → está/están. "
             "Online: «¿hay o está?» (classify) + «señala en el plano».")

# ============================================================ DIA 5 · QUIZ — hay/está/están
def s05_hayestar_quiz():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · QUIZ", "¿hay, está o están?", "Klik een zin → de juiste vorm verschijnt. Nieuw → hay · bekend + plaats → está/están.", num=1)
    items=[("En el salón ___ un sofá.","hay","un sofá = nieuw"),("El sofá ___ al lado.","está","bekend + plaats"),
           ("___ tres habitaciones.","hay","número"),("Los baños ___ arriba.","están","mv. bekend"),
           ("___ una plaza cerca.","hay","una = nieuw"),("La farmacia ___ en la esquina.","está","bekend + plaats")]
    x0,y0=Inches(0.5),Inches(1.7); cw=Inches(6.05); rh=Inches(0.7)
    for i,(q,ans,cat) in enumerate(items):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(3.6),rh,[[(q,{"size":12.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(3.8),y,cw-Inches(3.9),rh,
                 [[(ans+" ",{"size":14,"bold":True,"color":GD}),("· "+cat,{"size":10,"italic":True,"color":G})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.95),
             [[("hay = ", {"bold":True,"color":G}), ("iets nieuws (un/una/número) · ", {"color":GD}),
               ("está/están = ", {"bold":True,"color":G}), ("waar iets bekends (el/la) staat. Meervoud → están.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ (reveal). Laat de klas eerst kiezen, klik dan. Online: «¿hay o está?» (classify).")

# ============================================================ DIA 6 · GRAMMAR — preposiciones (reveal)
def s06_prepo():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · GRAMÁTICA", "¿Dónde está? — preposiciones de lugar", "Klik een kaart → de betekenis verschijnt. de + el = del.", num=2)
    text(s, Inches(0.5), Inches(1.5), Inches(12.3), Inches(0.5),
         [[("El gato está… ", {"size":14,"color":INK}),
           ("encima de ", {"size":14,"bold":True,"color":F_PLAC}),
           ("· debajo de · al lado de · entre… ", {"size":14,"bold":True,"color":F_PLAC}),
           ("  (de + el = del)", {"size":14,"color":INK})]])
    pares=[("encima de","boven op"),("debajo de","onder"),("al lado de","naast"),
           ("entre A y B","tussen"),("delante de","vóór"),("detrás de","achter"),
           ("dentro de","binnen in"),("enfrente de","tegenover"),("cerca de","dichtbij")]
    x0,y0=Inches(0.6),Inches(2.2); cw=Inches(3.9); ch=Inches(1.05)
    for i,(p,f) in enumerate(pares):
        c=i%3; r=i//3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(ch+Inches(0.12))
        card(s,x,y,cw,ch,fill=WHITE,line=G,lw=1.3)
        text(s,x,y+Inches(0.12),cw,Inches(0.4),[[(p,{"size":13,"bold":True,"color":GD,"font":DISPLAY})]],align=PP_ALIGN.CENTER)
        rev=text(s,x,y+Inches(0.55),cw,Inches(0.4),[[("→ "+f,{"size":13,"color":INK})]],align=PP_ALIGN.CENTER)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.9), Inches(12.3), Inches(0.6),
             [[("🔴 ", {"bold":True,"color":RED}), ("de + el = del (al lado del parque). Bij «entre» géén «de»: entre la mesa y la silla. Vorm: está (ev.) / están (mv.).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR preposiciones. Onthul per kaart; laat de betekenis voorspellen met een echt voorwerp in de klas. "
             "Online: «preposición de lugar» (cloze) + «señala en la habitación».")

# ============================================================ DIA 7 · QUIZ — preposiciones
def s07_prepo_quiz():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · QUIZ", "¿Qué preposición?", "Klik een zin → de juiste preposición verschijnt.", num=2)
    items=[("La lámpara está ___ la mesa (boven).","encima de"),("El gato está ___ la cama (onder).","debajo de"),
           ("El banco está ___ la farmacia (naast).","al lado de"),("El cine está ___ el banco y el parque.","entre"),
           ("El jardín está ___ la casa (achter).","detrás de"),("El museo está ___ la iglesia (tegenover).","enfrente de")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(6.05); rh=Inches(0.78)
    for i,(q,a) in enumerate(items):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(3.9),rh,[[(q,{"size":11.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(4.1),y,cw-Inches(4.2),rh,[[("→ "+a,{"size":12,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Tegenstellingen: ", {"bold":True,"color":GD}),
               ("encima ↔ debajo · delante ↔ detrás · cerca ↔ lejos · dentro ↔ fuera.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ preposiciones (retrieval). Klas roept de preposición vóór de klik. Daarna een info-gap in parejas (¿dónde está…?).")

# ============================================================ DIA 8 · GRAMMAR — el plano / dar indicaciones
def s08_plano():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · APLICACIÓN", "El plano del barrio", "Klik un edificio → dónde está. Aprende a decir la posición.", num=2)
    items=[("🥖 La panadería","está en la esquina",G),("🏦 El banco","está al lado de la farmacia",G),
           ("🎬 El cine","está entre el banco y el parque",G),("🏛️ El museo","está enfrente de la iglesia",G),
           ("🌳 El parque","está al final de la calle",G),("⛲ La plaza","está en el centro del barrio",G)]
    x0,y0=Inches(0.5),Inches(1.8); cw=Inches(6.05); ch=Inches(1.0)
    for i,(lab,txt,col) in enumerate(items):
        c=i%2; r=i//2; x=x0+c*(cw+Inches(0.2)); y=y0+r*(ch+Inches(0.18))
        card(s,x,y,cw,ch,fill=WHITE,line=col,lw=1.4)
        chip(s,x+Inches(0.2),y+Inches(0.12),lab,fill=GT,tcolor=GD,size=11)
        rev=text(s,x+Inches(0.2),y+Inches(0.5),cw-Inches(0.4),Inches(0.45),[[(txt,{"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
        register_reveal(s, rev)
    text(s, Inches(0.5), Inches(5.55), Inches(12.3), Inches(0.5),
         [[("🟡 Ordinales + apócope: ", {"size":12,"bold":True,"color":AMBER}), ("primero → el primer piso · tercero → el tercer piso (m. sing.).", {"size":12,"color":INK})]])
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(6.1), Inches(12.3), Inches(0.55),
             [[("Voor het adres: ", {"bold":True,"color":GD}), ("la planta baja · el primer piso · el segundo piso… (calle Real, 3º).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · APLICACIÓN plano + ordinales. Onthul per gebouw; laat leerlingen de positie beschrijven. Apócope: primer/tercer + m. sing. "
             "Online: «señala en el plano del barrio» + ordinales-quiz.")

# ============================================================ DIA 9 · READING — anuncio de piso
def s09_reading():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§5 · LEER · COMPRENSIÓN", "Se alquila piso (anuncio)", "Lees en beantwoord. Klik een vraag → het antwoord verschijnt.", num=5)
    card(s, Inches(0.5), Inches(1.65), Inches(5.6), Inches(3.9), fill=GT, line=G, lw=1.4)
    avatar(s, "valen", Inches(0.85), Inches(1.95), Inches(1.1))
    text(s, Inches(2.1), Inches(2.0), Inches(3.8), Inches(1.6),
         [[("«Bonito piso en el centro. Tercer piso con ascensor. Dos habitaciones, salón, cocina y baño. "
            "Terraza con vistas a la plaza. Cerca de la panadería y del parque. 600 € al mes.»",{"size":12.5,"italic":True,"color":INK})]], line=1.2)
    qa=[("¿En qué piso está?","Tercer piso (con ascensor)"),("¿Cuántas habitaciones?","Dos"),
        ("¿Qué hay en la terraza?","Vistas a la plaza"),("¿Cuánto cuesta al mes?","600 €")]
    x=Inches(6.4); y=Inches(1.7)
    for q,a in qa:
        card(s,x,y,Inches(6.4),Inches(0.85),fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y+Inches(0.06),Inches(6.1),Inches(0.4),[[(q,{"size":12.5,"bold":True,"color":GD})]])
        rev=text(s,x+Inches(0.15),y+Inches(0.44),Inches(6.1),Inches(0.35),[[("→ "+a,{"size":12,"color":INK})]])
        register_reveal(s, rev)
        y=y+Inches(0.98)
    btn=noodroute(s)
    exercise_solucion(s, Inches(6.4), Inches(5.65), Inches(6.4), Inches(0.6),
             [[("🎯 Leesdoel: ", {"bold":True,"color":GD}), ("scannen naar habitaciones, piso y precio — niet élk woord begrijpen.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · READING (lezen→spreken-keten). Eerst globaal (waarover?), dan scannen. Onthul de antwoorden pas na de klas. "
             "Daarna: leerlingen beschrijven zelf een woning (transfer → Tarea Mi barrio).")

# ============================================================ DIA 10 · LISTENING — Valen describe su barrio
def s10_listening():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · ESCUCHAR", "El barrio de Valen", "Klik un lugar → dónde está. (audio op de digitale pagina)", num=1)
    people=[("La plaza","enfrente de la casa","con palmeras"),("La panadería","al lado","pan fresco"),
            ("El parque","cerca del mar","para pasear"),("El supermercado","en la esquina","para la compra")]
    x0,y0=Inches(0.7),Inches(1.9); cw=Inches(2.95); ch=Inches(2.4)
    for i,(nm,com,beb) in enumerate(people):
        x=x0+i*(cw+Inches(0.1))
        card(s,x,y0,cw,ch,fill=WHITE,line=LINE,lw=1.2)
        rect(s,x,y0,cw,Inches(0.5),fill=GT)
        text(s,x,y0,cw,Inches(0.5),[[("🔊  "+nm,{"size":13,"bold":True,"color":GD,"font":DISPLAY})]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        text(s,x+Inches(0.15),y0+Inches(0.65),cw-Inches(0.3),Inches(0.4),[[("¿Dónde?",{"size":12,"color":MUT})]])
        rev1=text(s,x+Inches(0.15),y0+Inches(1.0),cw-Inches(0.3),Inches(0.5),[[(com,{"size":12.5,"bold":True,"color":INK})]],line=1.05)
        text(s,x+Inches(0.15),y0+Inches(1.6),cw-Inches(0.3),Inches(0.4),[[("Detalle:",{"size":12,"color":MUT})]])
        rev2=text(s,x+Inches(0.15),y0+Inches(1.95),cw-Inches(0.3),Inches(0.4),[[(beb,{"size":12,"bold":True,"color":G})]])
        register_reveal(s, rev1); register_reveal(s, rev2)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.85),
             [[("Modelo-audio (docent leest of TTS): ", {"bold":True,"color":GD}),
               ("«Enfrente de mi casa hay una plaza. La panadería está al lado y el parque está cerca del mar.» …", {"color":GD})],
              [("Daarna spreken: leerling beschrijft zelf zijn barrio.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · LISTENING (selectief → spreken). Lees Valens beschrijving voor (of TTS). Klas noteert ¿qué hay? + ¿dónde?; onthul per klik. "
             "Koppel meteen aan hun eigen barrio.")

# ============================================================ DIA 11 · GRAMMAR — estar + gerundio (reveal)
def s11_gerundio():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · GRAMÁTICA", "Estar + gerundio — ¿qué pasa ahora?", "Klik een kolomkop → de vormen. Fórmula: estar (presente) + -ando/-iendo.", num=3)
    text(s, Inches(0.5), Inches(1.5), Inches(12.3), Inches(0.5),
         [[("La fórmula: ", {"size":14,"color":INK}),
           ("estar (estoy, estás, está…) ", {"size":14,"bold":True,"color":F_VERB}),
           ("+ gerundio ", {"size":14,"bold":True,"color":F_OBJ}),
           ("   →   Estoy cocinando en la cocina.", {"size":14,"color":INK})]])
    pers=["yo","tú","él/ella","nosotros","vosotros","ellos"]
    forms=["estoy","estás","está","estamos","estáis","están"]
    x0,y0=Inches(1.6),Inches(2.2); cw=Inches(3.4); ch=Inches(1.1)
    for i,(p,f) in enumerate(zip(pers,forms)):
        c=i%3; r=i//3; x=x0+c*(cw+Inches(0.3)); y=y0+r*(ch+Inches(0.25))
        card(s,x,y,cw,ch,fill=WHITE,line=G,lw=1.4)
        text(s,x,y+Inches(0.12),cw,Inches(0.35),[[(p,{"size":12,"color":MUT})]],align=PP_ALIGN.CENTER)
        rev=text(s,x,y+Inches(0.48),cw,Inches(0.55),[[(f+" …ndo",{"size":20,"bold":True,"color":GD,"font":DISPLAY})]],align=PP_ALIGN.CENTER)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.6), Inches(12.3), Inches(0.75),
             [[("🔴 -ar → -ando ", {"bold":True,"color":RED}),
               ("(cocinar → cocinando) · -er/-ir → -iendo (comer → comiendo, vivir → viviendo). Onregelmatig: leer → leyendo, dormir → durmiendo.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR estar + gerundio. Onthul per kaart; laat de vorm voorspellen. Twee delen: estar (vervoegd) + gerundio (onveranderd). "
             "Online: «completa: estar + gerundio» (cloze).")

# ============================================================ DIA 12 · SPEAKING — explica el camino
def s12_speaking():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · SPEAKING · INTERACCIÓN", "¡Explica el camino!", "Speel de scène. Steun bouwt af: kaarten → beginwoorden → uit het hoofd.", num=4)
    avatar(s, "tu", Inches(11.4), Inches(1.7), Inches(1.3))
    labels=["Preguntar","Salir","Seguir","Girar","Cruzar","Llegar"]
    frames=["¿Cómo se va a…?","Sal de casa.","Sigue todo recto.","Gira a la derecha.","Cruza el semáforo.","Está a la izquierda."]
    x0,y0=Inches(0.5),Inches(1.8); cw=Inches(3.4); rh=Inches(0.8)
    for i,(lab,fr) in enumerate(zip(labels,frames)):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=G,lw=1.2,shadow=False)
        text(s,x+Inches(0.15),y+Inches(0.05),cw-Inches(0.3),Inches(0.32),[[(lab,{"size":10,"color":MUT})]])
        text(s,x+Inches(0.15),y+Inches(0.36),cw-Inches(0.3),Inches(0.4),[[(fr,{"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    text(s, Inches(0.5), Inches(5.0), Inches(10.5), Inches(0.9),
         [[("Ronda 1: ", {"size":12,"bold":True,"color":GD}), ("met de kaarten. ", {"size":12,"color":INK}),
           ("Ronda 2: ", {"size":12,"bold":True,"color":GD}), ("alleen beginwoorden. ", {"size":12,"color":INK}),
           ("Ronda 3: ", {"size":12,"bold":True,"color":GD}), ("uit het hoofd, andere ruta. ", {"size":12,"color":INK}),
           ("Ronda 4: ", {"size":12,"bold":True,"color":GD}), ("grábate en de digitale pagina.", {"size":12,"color":INK})]])
    chip(s, Inches(0.5), Inches(4.65), "🎙️ Grábate online · «Mensaje de voz: explica el camino»", fill=GT, tcolor=GD, size=11)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.6), Inches(12.3), Inches(0.65),
             [[("Modelo: ", {"bold":True,"color":GD}), ("«Perdona, ¿cómo se va a la plaza? — Sigue todo recto, gira a la derecha y cruza el semáforo. Está al final.»", {"color":GD})]],
             trigger=btn, title_doc="MODELO · docent")
    foot(s)
    notes(s, "TEACHER · SPEAKING (interactie). Automatiseer preguntar→seguir→girar→llegar in rondes met afbouwende steun. "
             "Online: recorder (opname + zelfevaluatie). Print blijft bruikbaar zonder opname.")

# ============================================================ DIA 13 · WRITING — mi barrio
def s13_writing():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "WRITING · PRODUCCIÓN", "Mi barrio (descripción)", "Beschrijf je buurt. Klik → een modeltekst verschijnt.", num=1)
    card(s, Inches(0.5), Inches(1.7), Inches(6.0), Inches(3.9), fill=WHITE, line=LINE, lw=1.2)
    text(s, Inches(0.7), Inches(1.85), Inches(5.6), Inches(0.4), [[("✍️ Escribe aquí sobre tu barrio:", {"size":12,"bold":True,"color":GD})]])
    for i in range(6):
        rect(s, Inches(0.7), Inches(2.4)+i*Inches(0.5), Inches(5.6), Inches(0.01), fill=LINE)
    chk=[("¿qué hay? (hay una plaza…)",),("¿dónde está? (está al lado de…)",),("2 preposiciones de lugar",),("¿cómo se llega? (imperativo)",),("un mueble / edificio típico",),("¿qué está pasando ahora?",)]
    x=Inches(6.9); y=Inches(1.7)
    text(s,x,y,Inches(6),Inches(0.4),[[("Checklist:",{"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    for i,(c,) in enumerate(chk):
        text(s,x,y+Inches(0.5)+i*Inches(0.45),Inches(6),Inches(0.4),[[("☐  "+c,{"size":13,"color":INK})]])
    rev=card(s, x, Inches(4.35), Inches(6.0), Inches(1.25), fill=GT, line=G, lw=1.2)
    text(s, x+Inches(0.15), Inches(4.4), Inches(5.7), Inches(1.2),
         [[("Modelo: ", {"size":12,"bold":True,"color":GD}),
           ("«En mi barrio hay una plaza. La panadería está al lado y el parque está enfrente. Para llegar, sigue todo recto. Ahora la gente está paseando.»",{"size":12,"italic":True,"color":INK})]], line=1.15)
    register_reveal(s, rev)
    noodroute(s); foot(s)
    notes(s, "TEACHER · WRITING (lezen→schrijven). Checklist = zichtbare steun; onthul het model pas na het schrijven (retrieval). "
             "Nakijkfocus: hay/estar, preposiciones, imperativo. Dit voedt de Tarea «Mi barrio».")

# ============================================================ DIA 14 · VOCAB — muebles/barrio (reveal)
def s14_muebles_barrio():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · VOCABULARIO · BARRIO", "Muebles y edificios", "Klik een woord → de vertaling verschijnt. Bouw je woordnetwerk.", num=1)
    data=[("el sofá","bank"),("la cama","bed"),("el armario","kast"),("la nevera","koelkast"),
          ("la panadería","bakkerij"),("la farmacia","apotheek"),("el banco","bank (geld)"),("el parque","park"),
          ("la estación","station"),("el autobús","bus"),("el metro","metro"),("la bicicleta","fiets")]
    x0,y0=Inches(0.5),Inches(1.7); cw=Inches(3.0); rh=Inches(0.7)
    for i,(es,nl) in enumerate(data):
        c=i%4; r=i//4; x=x0+c*(cw+Inches(0.1)); y=y0+r*(rh+Inches(0.14))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.12),y,Inches(1.6),rh,[[(es,{"size":12,"bold":True,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(1.7),y,cw-Inches(1.8),rh,[[("→ "+nl,{"size":11.5,"color":G})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.9),
             [[("Combineer met preposición: ", {"bold":True,"color":GD}),
               ("el sofá está al lado de la ventana · la panadería está enfrente del banco.", {"color":GD})],
              [("Transporte: en autobús · en metro · en bici · a pie. Direcciones: a la derecha / izquierda · todo recto.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCAB muebles/barrio. Klik onthult; koppel elk woord aan een preposición-zin. Volledige set + audio op de digitale pagina "
             "(flip cards + memoria).")

# ============================================================ DIA 15 · TALLER — conectores + ortografía
def s15_taller():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "TALLER DE LENGUA", "Conectores de lugar + ortografía", "Klik een item → correcte vorm. Gereedschap voor de ruta en spelling.", num=1)
    text(s, Inches(0.5), Inches(1.5), Inches(6), Inches(0.35), [[("A · conectores de lugar: todo recto · a la derecha · al final de…", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    fixes=[("Sigue ___ (rechtdoor)","todo recto"),("Gira ___ (rechts)","a la derecha"),("La plaza está ___ (aan het eind)","al final de la calle"),("El museo está ___ (tegenover)","enfrente de")]
    y=Inches(1.95)
    for q,a in fixes:
        card(s,Inches(0.5),y,Inches(6.0),Inches(0.6),fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,Inches(0.62),y,Inches(3.4),Inches(0.6),[[(q,{"size":11.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,Inches(4.1),y,Inches(2.3),Inches(0.6),[[("→ "+a,{"size":11.5,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y=y+Inches(0.72)
    text(s, Inches(6.9), Inches(1.5), Inches(6), Inches(0.35), [[("B · ortografía: ¿diptongo o hiato?", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    conn=[("panaderia","panadería","hiato: tilde op í"),("puerta","puerta","diptongo (ue)"),("pais","país","hiato: tilde op í"),("dia","día","hiato: tilde op í")]
    y=Inches(1.95)
    for q,a,gl in conn:
        card(s,Inches(6.9),y,Inches(5.9),Inches(0.6),fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,Inches(7.02),y,Inches(2.6),Inches(0.6),[[(q,{"size":11.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,Inches(9.7),y,Inches(3.0),Inches(0.6),[[(a+" ",{"size":12,"bold":True,"color":GD}),("· "+gl,{"size":9,"italic":True,"color":MUT})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y=y+Inches(0.72)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.85),
             [[("A: ", {"bold":True,"color":GD}), ("conectores de lugar structureren de rondleiding (todo recto → a la derecha → al final de).", {"color":GD})],
              [("🔴 B: ", {"bold":True,"color":RED}), ("hiato = tilde op í/ú breekt de tweeklank: panadería, día, país. Diptongo = twee klinkers samen: puerta, bueno.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · TALLER. Conectores de lugar = ideaal met een plano. Diptongo/hiato = spelling-leerlijn U7 (sombrero). Meteen toepassen in de descripción. "
             "Online: «diptongo o hiato» + «ordena las instrucciones».")

# ============================================================ DIA 16 · CULTURE — la plaza y el barrio
def s16_cultura():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "CULTURA · PARADA 7", "La plaza y el barrio", "Klik een kaart → het weetje verschijnt. La plaza es el corazón del barrio.", num=1)
    cards=[("🏛️ La plaza","El centro del barrio: hay bancos, árboles y una iglesia. Por la tarde la gente está paseando y charlando. En Cartagena, la Plaza de los Coches es famosa.","La plaza = de ontmoetingsplek."),
           ("🏘️ Casas de colores","Cartagena tiene un casco histórico con casas de colores y balcones con flores. Las murallas protegen la ciudad frente al mar Caribe. Barrio Getsemaní = arte y color.","Color, música y arte."),
           ("🌎 ¿Cómo se vive?","En España: un piso. En América: un apartamento. Con jardín: chalet (ES) o casa (AM). En el adres: la planta baja, el primer piso…","piso 🇪🇸 ↔ apartamento 🌎.")]
    x0,y0=Inches(0.5),Inches(1.7); cw=Inches(4.05); ch=Inches(3.4)
    for i,(t,f,nl) in enumerate(cards):
        x=x0+i*(cw+Inches(0.13))
        card(s,x,y0,cw,ch,fill=WHITE,line=G,lw=1.3)
        rect(s,x,y0,cw,Inches(0.6),fill=GT)
        text(s,x+Inches(0.15),y0,cw-Inches(0.3),Inches(0.6),[[(t,{"size":14,"bold":True,"color":GD,"font":DISPLAY})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(0.2),y0+Inches(0.8),cw-Inches(0.4),Inches(1.9),[[(f,{"size":12,"color":INK})]],line=1.2)
        register_reveal(s, rev)
        text(s,x+Inches(0.2),y0+Inches(2.75),cw-Inches(0.4),Inches(0.6),[[(nl,{"size":10.5,"italic":True,"color":MUT})]],line=1.1)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.35), Inches(12.3), Inches(0.6),
             [[("Actividad: ", {"bold":True,"color":GD}), ("schrijf 3 zinnen over een plein of buurt bij jou (¿qué hay? ¿dónde está? ¿qué haces ahí?).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · CULTURE (identiteit in diversiteit, LPD 5). Onthul per kaart. Vergelijk plazas ES/MX/CO/PE. Bruggetje naar de Tarea Mi barrio. "
             "Online: «lugar ↔ país» (match).")

# ============================================================ DIA 17 · QUIZ — la ruta / imperativo
def s17_quiz_ruta():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · QUIZ · INTERACCIÓN", "El camino: completa", "Wat past? Klik → het antwoord verschijnt.", num=4)
    items=[("___ todo recto. (seguir)","Sigue"),("___ a la derecha. (girar)","Gira"),
           ("___ la calle. (cruzar)","Cruza"),("Vivo en el ___ piso. (1º)","primer"),
           ("El baño está ___ pasillo (aan 't eind).","al final del"),("La farmacia está ___ (op de hoek).","en la esquina")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(6.05); rh=Inches(0.78)
    for i,(ans,q) in enumerate(items):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(3.7),rh,[[(ans,{"size":11.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(3.9),y,cw-Inches(4.05),rh,[[("→ "+q,{"size":12,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Imperativo (tú): ", {"bold":True,"color":GD}),
               ("-ar → -a (gira, cruza) · -er/-ir → -e (sube, sigue). ir → ve. Apócope: primer/tercer piso.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ camino (interactie). Klas vult vóór de klik. Daarna de rollenspel-scène (¿cómo se va a…?) in parejas.")

# ============================================================ DIA 18 · FINAL_MISSION — Mi barrio
def s18_tarea():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(1.35), fill=GD)
    text(s, Inches(0.5), Inches(0.18), Inches(9), Inches(1.0),
         [[("🏘️ Tarea final · Mi barrio", {"size":30,"bold":True,"color":WHITE,"font":DISPLAY})],
          [("Maak el plano de tu barrio y da una visita guiada — di qué hay, dónde está y cómo llegar.", {"size":13,"italic":True,"color":GT})]])
    avatar(s, "mochila", Inches(11.6), Inches(0.2), Inches(1.0))
    pasos=[("1","Dibuja el plano","calles, plaza, tiendas, tu casa"),
           ("2","Escribe 5 frases","qué hay + dónde está (preposiciones)"),
           ("3","Escribe el camino","de tu casa a la plaza (imperativo)"),
           ("4","Da la visita guiada","en pareja (of neem audio op)"),
           ("5","Responde","«¿Dónde está la farmacia?»")]
    y=Inches(1.7)
    for n,es,nl in pasos:
        b=rect(s,Inches(0.5),y,Inches(0.5),Inches(0.5),fill=G,round=True,radius=0.5)
        tf=b.text_frame;tf.vertical_anchor=MSO_ANCHOR.MIDDLE;p=tf.paragraphs[0];p.alignment=PP_ALIGN.CENTER
        rr=p.add_run();rr.text=n;rr.font.size=Pt(15);rr.font.bold=True;rr.font.name=DISPLAY;rr.font.color.rgb=WHITE
        text(s,Inches(1.2),y,Inches(4.2),Inches(0.55),[[(es,{"size":14,"bold":True,"color":GD,"font":DISPLAY})]],anchor=MSO_ANCHOR.MIDDLE)
        text(s,Inches(5.5),y,Inches(7.2),Inches(0.55),[[(nl,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        y=y+Inches(0.62)
    text(s, Inches(0.5), Inches(5.0), Inches(12), Inches(0.35), [[("Rúbrica · ¿lo logré?", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    crit=["5+ lugares con nombre","hay + está/están","preposiciones de lugar","el camino (imperativo)"]
    x=Inches(0.5)
    for c in crit:
        chip(s,x,Inches(5.45),"☐ "+c,fill=GT,tcolor=GD,size=11,w=Inches(3.0)); x=x+Inches(3.1)
    text(s, Inches(0.5), Inches(6.05), Inches(12), Inches(0.4),
         [[("🎯 ", {"size":12}), ("Afzender jij (de gids) · ontvanger een bezoeker · doel je buurt voorstellen & de weg uitleggen · situatie un paseo por el barrio · resultaat: plano + gespeelde rondleiding.", {"size":11.5,"italic":True,"color":MUT})]])
    foot(s)
    notes(s, "TEACHER · FINAL_MISSION (communicatieve eindtaak). Afzender/ontvanger/doel/situatie/resultaat expliciet. Beoordeel met de rúbrica; "
             "opname + zelfevaluatie op de digitale pagina. Voeg een mini-encuesta + grafiekje toe (¿qué hay en el barrio?).")

# ============================================================ DIA 19 · QUIZ — la mezcla
def s19_mezcla():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "QUIZ · LA MEZCLA", "Ophaal door elkaar", "Gemengde ophaal van de hele unit. Klik een vraag → het antwoord. (retrieval)", num=1)
    items=[("En el salón ___ un sofá.","hay"),("El sofá ___ al lado.","está"),("estar+ger, yo → cocinar","estoy cocinando"),
           ("gira, ¿infinitivo?","girar"),("el ___ piso (1º)","primer"),("La lámpara está ___ la mesa (boven).","encima de"),
           ("Los baños ___ arriba.","están"),("sigue, ¿infinitivo?","seguir")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(6.05); rh=Inches(0.62)
    for i,(q,a) in enumerate(items):
        c=i//4; r=i%4; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.16))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(3.6),rh,[[(q,{"size":11.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(3.75),y,cw-Inches(3.9),rh,[[("→ "+a,{"size":11.5,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.05), Inches(12.3), Inches(0.55),
             [[("Alles komt terug: ", {"bold":True,"color":GD}), ("hay/estar · preposiciones · estar + gerundio · imperativo · ordinales.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ mezcla (retrieval vóór herlezen). Zonder waarschuwing door elkaar. Exit-ticket. Zwakke punten → terug via menu.")

# ============================================================ DIA 20 · FEEDBACK/REPASO
def s20_repaso():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "REPASO · LO ESENCIAL", "Lo esencial de un vistazo", "De volledige herhaling (20 spellen, drills) staat online. Hier: de kern + semáforo.", num=1)
    ess=["Hay / estar: hay + un/una/número (nieuw) · el/la … está/están + plaats (bekend). Nooit «hay el/la».",
         "Preposiciones: encima/debajo/al lado/entre/delante/detrás/dentro/enfrente de (de + el = del).",
         "Estar + gerundio: estoy/estás/está… + -ando (-ar) / -iendo (-er/-ir): «Estoy cocinando».",
         "Imperativo (el camino): gira · sigue · cruza · toma · ve (ir). -ar→-a · -er/-ir→-e.",
         "🔴 Trampas: niet «hay el parque» · de+el=del · estoy comiendo · el primer piso · hiato panadería."]
    card(s, Inches(0.5), Inches(1.6), Inches(12.3), Inches(2.5), fill=CREMA, line=None)
    y=Inches(1.8)
    for e in ess:
        text(s, Inches(0.8), y, Inches(11.8), Inches(0.45), [[("• ", {"size":13,"bold":True,"color":GD}),(e,{"size":12,"color":INK})]])
        y=y+Inches(0.46)
    text(s, Inches(0.5), Inches(4.3), Inches(12), Inches(0.35), [[("Semáforo — ¿cómo lo llevas?", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    can=["la casa beschrijven (habitaciones/muebles)","hay/estar juist gebruiken","preposiciones de lugar","estar + gerundio (nu)","el camino (imperativo)"]
    y=Inches(4.75)
    for c in can:
        text(s,Inches(0.8),y,Inches(7.0),Inches(0.4),[[(c,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        for j,(em,col) in enumerate([("🔴",RED),("🟠",AMBER),("🟢",G)]):
            chip(s,Inches(8.0)+j*Inches(1.5),y+Inches(0.03),em+" ",fill=WHITE,tcolor=col,size=12,w=Inches(1.3))
        y=y+Inches(0.42)
    foot(s)
    notes(s, "TEACHER · FEEDBACK/REPASO. Semáforo = zelfevaluatie. Repaso-drills online (20 spellen). Bruggetje: U8 «¿Qué has hecho?» — "
             "viajar y contar lo que has hecho (pretérito perfecto).")

# ============================================================ DIA 21 · TEACHER_NOTES
def s21_teacher():
    s = slide(); bg(s, GD)
    text(s, Inches(0.6), Inches(0.4), Inches(12), Inches(0.8), [[("TEACHER_NOTES · U7 «Mi casa y mi barrio»", {"size":26,"bold":True,"color":WHITE,"font":DISPLAY})]])
    blocks=[("Timing (50 min)","Menu 2' · hay/estar 10' · preposiciones 10' · estar+gerundio 8' · imperativo/camino 8' · lectura/escucha 6' · cultura 3' · Tarea-briefing 3'."),
            ("Kernvalstrikken","Niet «hay el parque» (hay ≠ estar) · de+el=del · estoy comi-E-ndo · el primer/tercer piso (apócope, m. sing.) · hiato panadería/día/país."),
            ("Differentiatie (zij-instromers)","Alles start vanaf nul. Sterker: hele rondleiding + eigen plano + preguntas del visitante. Zwakker: hay/estar-kaart en preposición-ficha langer open, imperativo-frames houden."),
            ("Digitaal","20 spellen + flip cards + klikbare kaart + recorder (Hablar) + Lectura (anuncio + barrio) op de página digital. QR's in het boek → juiste anker. Conjugador = aparte tool."),
            ("Evaluatie","Tarea «Mi barrio» met rúbrica (4 criteria). LPD 3·4·7·8 + 5 (cultura) + 1·2 (receptief: lezen/luisteren).")]
    y=Inches(1.4)
    for t,b in blocks:
        card(s, Inches(0.5), y, Inches(12.3), Inches(1.0), fill=RGBColor(0x1B,0x63,0x49), line=None)
        text(s, Inches(0.75), y+Inches(0.08), Inches(11.8), Inches(0.4), [[(t, {"size":14,"bold":True,"color":WHITE,"font":DISPLAY})]])
        text(s, Inches(0.75), y+Inches(0.48), Inches(11.8), Inches(0.5), [[(b, {"size":11.5,"color":GT})]], line=1.12)
        y=y+Inches(1.12)
    footer(s, tab=TAB, page=pg())
    notes(s, "Alleen in het docentdeck. Volledige LPD-dekking en didactische route staan in het cursusdossier (bron.md).")

# ============================================================ RUN + BUILD
def _run_all(include_teacher=True):
    s01_title(); s02_menu(); s03_vocab(); s04_hayestar(); s05_hayestar_quiz(); s06_prepo(); s07_prepo_quiz()
    s08_plano(); s09_reading(); s10_listening(); s11_gerundio(); s12_speaking(); s13_writing()
    s14_muebles_barrio(); s15_taller(); s16_cultura(); s17_quiz_ruta(); s18_tarea(); s19_mezcla(); s20_repaso()
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
