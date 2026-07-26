#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_u5_docente.py — Interactieve PowerPoint C5 · Unidad 5 «¡Ñam!» (parada México/CDMX)
=======================================================================================
Zelfde engine/pijplijn als de golden sample U0/U1/U4 (gen_u0_docente wordt geïmporteerd:
low-level helpers, on-click <p:timing>-animaties, hyperlink-navigatie). Enkel de SLIDES
zijn U5-specifiek. Twee decks (beide .pptx):
  · C5_U5_docente.pptx — vrije navigatie, oplossingen bij klik + didactiek in spreker-notities.
  · C5_U5_alumno.pptx  — gewone diavoorstelling, antwoorden verschijnen bij klik (F5, geen kiosk).
Huisstijl groen (C5). Spaans-eerst + NL-steun. ≥20 dia's. Dekt de vier vaardigheden. Diego = gastheer.
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
OUT_DOCENTE = os.path.join(HERE, "C5_U5_docente.pptx")
OUT_ALUMNO_PPTX = os.path.join(HERE, "C5_U5_alumno.pptx")
TAB = "U5 · ¡ÑAM!"

def foot(s): footer(s, tab=TAB, page=pg())

# ============================================================ DIA 1 · TITLE
def s01_title():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(4.7), fill=G)
    rect(s, 0, Inches(4.7), EMU_W, Inches(0.09), fill=GD)
    text(s, Inches(0.6), Inches(0.35), Inches(3.4), Inches(3.6),
         [[("5", {"size": 260, "bold": True, "color": RGBColor(0x2E,0xB0,0x85), "font": DISPLAY})]],
         anchor=MSO_ANCHOR.MIDDLE)
    chip(s, Inches(4.35), Inches(0.85), "LA RUTA · PARADA 5 · MÉXICO · CDMX 🇲🇽", fill=WHITE, tcolor=GD, size=12)
    text(s, Inches(4.3), Inches(1.35), Inches(8.6), Inches(1.5),
         [[("¡Ñam!", {"size": 72, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(4.35), Inches(2.7), Inches(8.4), Inches(0.6),
         [[("Comida y restaurante: cantidades, «voy a comer» y pedir con cortesía — en la CDMX, con Diego.", {"size": 15, "italic": True, "color": GT})]])
    text(s, Inches(4.35), Inches(3.35), Inches(8.4), Inches(0.9),
         [[("¿Qué vas a comer hoy?", {"size": 24, "bold": True, "color": WHITE, "font": DISPLAY})],
          [("Wat ga je vandaag eten?", {"size": 13, "italic": True, "color": GT})]])
    text(s, Inches(0.6), Inches(4.95), Inches(6), Inches(0.4),
         [[("La gente de la ruta — je reisgezellen", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    x = Inches(0.6)
    for nm, city in [("diego","CDMX 🇲🇽 · anfitrión"),("lucia","Sevilla 🇪🇸"),("valen","Cartagena 🇨🇴"),
                     ("nina","Cusco 🇵🇪"),("tu","Tú · Flandes 🇧🇪"),("mochila","La mochila")]:
        avatar(s, nm, x, Inches(5.4), Inches(1.0))
        text(s, x - Inches(0.15), Inches(6.42), Inches(1.3), Inches(0.5),
             [[(nm.capitalize() if nm!="tu" else "Tú", {"size": 10.5, "bold": True, "color": INK})],
              [(city.split("·")[-1].strip() if nm!="tu" else "de reiziger = jij", {"size": 8.5, "color": MUT})]],
             align=PP_ALIGN.CENTER)
        x = x + Inches(2.05)
    foot(s)
    notes(s, "TEACHER · TITLE. Parada 5 = México (CDMX): cruzamos el charco. Gastheer = Diego. Doel: comida/bebida benoemen, cantidades "
             "(mucho/poco/un poco de · un kilo de), el futuro próximo (ir a + infinitivo), pedir con cortesía (¿me pone…?/para mí…) en la cuenta, "
             "en de OD-aanzet lo/la/los/las (la cuenta → la traigo). Kernvalstrik: much-A fruta ≠ mucho; voy A comer (a niet vergeten). "
             "Docentdeck = vrije navigatie + oplossing in notities; leerlingdeck (.pptx, F5) = elke klik onthult het volgende antwoord.")

# ============================================================ DIA 2 · LESSON_MENU
def s02_menu():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "MENÚ DE LA LECCIÓN", "El mapa de la Unidad 5",
               "Kies je route — klik een tegel. Alles oefent naar de Tarea «La carta» toe.", num=5)
    tiles = [
        ("§1", "Cantidades", "mucho/poco · un kilo de", G, 3),
        ("§2", "Voy a comer", "ir a + infinitivo", G, 6),
        ("§3", "Pedir · cortesía", "¿me pone…? · para mí…", G, 7),
        ("§4", "La cuenta (lo/la)", "lo/la/los/las", G, 11),
        ("§5", "Lectura + escucha", "dos cartas (menús)", G, 9),
        ("★", "Cultura · tacos", "mercados y horarios", GD, 16),
        ("🍽️", "Tarea · La carta", "je menu + restaurante", GD, 18),
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
             "Begin bij §1 (cantidades) → §3 (pedir) = het hart van de unit. Kruisverwijzing print/HTML: «oefen online — 17 juegos».")

# ============================================================ DIA 3 · VOCABULARY — comida
def s03_vocab():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · VOCABULARIO", "La comida y la bebida", "De woorden van tafel — observa. Herken ze, dan gebruik je ze.", num=1)
    legend_func(s, Inches(9.7), Inches(0.55))
    rows = [("la comida","het eten","el pan · la carne"),("la bebida","het drinken","el agua · el zumo"),
            ("la fruta","het fruit","la manzana · el plátano"),("la verdura","de groente","el tomate · la lechuga"),
            ("el pollo","de kip","el pescado · el arroz"),("la sopa","de soep","la ensalada"),
            ("el taco","de taco","el guacamole 🇲🇽"),("los cubiertos","het bestek","tenedor · cuchillo")]
    x0,y0 = Inches(0.5), Inches(1.6); cw=Inches(6.1); rh=Inches(0.6)
    for i,(k,v,nl) in enumerate(rows):
        c = 0 if i<4 else 1; r = i%4
        x = x0 + c*(cw+Inches(0.15)); y = y0 + r*(rh+Inches(0.12))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x+Inches(0.15), y, Inches(2.4), rh, [[(k, {"size":13,"bold":True,"color":GD})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x+Inches(2.5), y, Inches(2.3), rh, [[(v, {"size":12,"color":INK})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x+Inches(4.6), y, Inches(1.4), rh, [[(nl, {"size":9,"italic":True,"color":MUT})]], anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(4.75), Inches(12.3), Inches(0.5),
         [[("Cantidades: ", {"size":13,"bold":True,"color":GD,"font":DISPLAY}),
           ("mucho/poco", {"size":13,"bold":True,"color":F_OBJ}), (" · ",{"size":13,"color":INK}),
           ("un poco de", {"size":13,"bold":True,"color":F_OBJ}), (" · ",{"size":13,"color":INK}),
           ("un kilo de · una botella de · un paquete de", {"size":13,"bold":True,"color":F_OBJ})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.35), Inches(12.3), Inches(0.95),
             [[("🔴 Cantidad concuerda: ", {"bold":True,"color":RED}), ("muchO pan · muchA fruta · muchOS tomates · muchAS manzanas.", {"bold":True,"color":GD})],
              [("un poco de + niet-telbaar (queso, leche, agua) — verandert nooit.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCABULARY. Toon per cluster (comida/bebida/fruta/verdura/mesa). Laat raden zónder de NL-gloss. "
             "Online: flip cards + Memoria de la comida + Fruta y verdura + ¿comida o bebida?")

# ============================================================ DIA 4 · GRAMMAR — cantidades (color)
def s04_cantidades():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · GRAMÁTICA VISUAL", "Cantidades — mucho / poco / un poco de", "Kleur = het voorwerp. De cantidad past zich aan (m/v · ev/mv).", num=1)
    legend_func(s, Inches(9.7), Inches(0.55))
    seg = [("En el mercado hay ", INK),("mucha ", F_OBJ),("fruta ", F_PLAC),("y ", INK),
           ("muchos ", F_OBJ),("tomates,", F_PLAC),(" pero solo ", INK),("un poco de ", F_OBJ),("queso.", F_PLAC)]
    runs=[[(t,{"size":22,"bold":True,"color":c,"font":DISPLAY}) for t,c in seg]]
    card(s, Inches(0.5), Inches(1.7), Inches(12.3), Inches(1.2), fill=GT, line=None)
    text(s, Inches(0.8), Inches(1.7), Inches(11.7), Inches(1.2), runs, anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(3.15), Inches(12), Inches(0.4), [[("La concordancia — ¿qué forma?", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    frame=[("mucho","+ m. ev. (pan, arroz)"),("mucha","+ v. ev. (fruta, leche)"),("muchos","+ m. mv. (tomates)"),
           ("muchas","+ v. mv. (manzanas)"),("un poco de","niet-telbaar (queso)"),("un kilo de","envase + producto")]
    x0,y0=Inches(0.5),Inches(3.6); cw=Inches(4.0); rh=Inches(0.62)
    for i,(a,b) in enumerate(frame):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.12))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(1.7),rh,[[(a,{"size":12.5,"bold":True,"color":F_OBJ})]],anchor=MSO_ANCHOR.MIDDLE)
        text(s,x+Inches(1.85),y,cw-Inches(2.0),rh,[[(b,{"size":11,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.7), Inches(12.3), Inches(0.7),
             [[("Regla: ", {"bold":True,"color":GD}), ("mucho/-a/-os/-as past aan bij het woord · un poco de blijft gelijk (niet-telbaar) · envases: un kilo/una botella/un paquete de.", {"color":GD})]],
             trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR (color-coding). Maak concordantie fysiek zichtbaar. Truc: kijk naar geslacht + aantal. Kleur nooit als enige drager. "
             "Online: «¿mucho, mucha, muchos o muchas?» (classify) + cantidades Tetris.")

# ============================================================ DIA 5 · QUIZ — mucho/mucha/muchos/muchas
def s05_cantidad_quiz():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · QUIZ", "¿mucho, mucha, muchos o muchas?", "Klik een woord → de juiste vorm verschijnt. Kijk naar m/v en ev/mv.", num=1)
    items=[("___ pan","mucho","m. ev."),("___ fruta","mucha","v. ev."),
           ("___ tomates","muchos","m. mv."),("___ manzanas","muchas","v. mv."),
           ("___ leche","mucha","v. ev."),("___ huevos","muchos","m. mv.")]
    x0,y0=Inches(0.5),Inches(1.7); cw=Inches(6.05); rh=Inches(0.7)
    for i,(q,ans,cat) in enumerate(items):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(3.6),rh,[[(q,{"size":13,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(3.8),y,cw-Inches(3.9),rh,
                 [[(ans+" ",{"size":14,"bold":True,"color":GD}),("· "+cat,{"size":10,"italic":True,"color":G})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.95),
             [[("mucho/-a = ", {"bold":True,"color":G}), ("enkelvoud (m/v) · ", {"color":GD}),
               ("muchos/-as = ", {"bold":True,"color":G}), ("meervoud (m/v). Kijk naar het lidwoord: el/la · los/las.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ (reveal). Laat de klas eerst kiezen, klik dan. Online: «cantidad» (classify) + cantidades Tetris.")

# ============================================================ DIA 6 · GRAMMAR — ir a + infinitivo (reveal)
def s06_ir_a():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · GRAMÁTICA", "Voy a comer — ir a + infinitivo", "Klik een kolomkop → de vormen verschijnen. Fórmula: ir (presente) + a + infinitivo.", num=2)
    text(s, Inches(0.5), Inches(1.5), Inches(12.3), Inches(0.5),
         [[("La fórmula: ", {"size":14,"color":INK}),
           ("ir (voy, vas, va…) ", {"size":14,"bold":True,"color":F_VERB}),
           ("+ a + ", {"size":14,"bold":True,"color":F_TIME}),
           ("infinitivo", {"size":14,"bold":True,"color":F_OBJ}),
           ("   →   Voy a comer un taco.", {"size":14,"color":INK})]])
    pers=["yo","tú","él/ella","nosotros","vosotros","ellos"]
    forms=["voy","vas","va","vamos","vais","van"]
    x0,y0=Inches(1.6),Inches(2.2); cw=Inches(3.4); ch=Inches(1.1)
    for i,(p,f) in enumerate(zip(pers,forms)):
        c=i%3; r=i//3; x=x0+c*(cw+Inches(0.3)); y=y0+r*(ch+Inches(0.25))
        card(s,x,y,cw,ch,fill=WHITE,line=G,lw=1.4)
        text(s,x,y+Inches(0.12),cw,Inches(0.35),[[(p,{"size":12,"color":MUT})]],align=PP_ALIGN.CENTER)
        rev=text(s,x,y+Inches(0.48),cw,Inches(0.55),[[(f+" a…",{"size":20,"bold":True,"color":GD,"font":DISPLAY})]],align=PP_ALIGN.CENTER)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.6), Inches(12.3), Inches(0.75),
             [[("🔴 Vergeet de «a» niet: ", {"bold":True,"color":RED}),
               ("voy A comer (niet «voy comer»). 🔴 Het tweede werkwoord blijft infinitief: ", {"color":GD}),
               ("voy a COMER", {"bold":True,"color":GD}), (". Gebruik: plannen dichtbij.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR ir a + inf. Onthul per kaart; laat de vorm voorspellen. Twee delen: ir (vervoegd) + a + infinitief (onveranderd). "
             "Online: «completa: ir a + infinitivo» (cloze) + presente-Tetris.")

# ============================================================ DIA 7 · GRAMMAR — pedir & cortesía (reveal)
def s07_pedir():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · GRAMÁTICA · FUNCIONES", "Pedir con cortesía", "Twee rollen. Klik een kaart → wie zegt het. Camarero pregunta, cliente pide.", num=3)
    items=[("🧑‍🍳 Camarero","¿Qué va a tomar?",G),("🙋 Cliente","Para mí, una sopa.",AMBER),
           ("🧑‍🍳 Camarero","¿Y para beber?",G),("🙋 Cliente","¿Me pone agua?",AMBER),
           ("🧑‍🍳 Camarero","¡Que aproveche!",G),("🙋 Cliente","La cuenta, por favor.",AMBER)]
    x0,y0=Inches(0.5),Inches(1.8); cw=Inches(6.05); ch=Inches(1.0)
    for i,(lab,txt,col) in enumerate(items):
        c=i%2; r=i//2; x=x0+c*(cw+Inches(0.2)); y=y0+r*(ch+Inches(0.18))
        card(s,x,y,cw,ch,fill=WHITE,line=col,lw=1.4)
        chip(s,x+Inches(0.2),y+Inches(0.12),lab,fill=GT,tcolor=GD,size=11)
        rev=text(s,x+Inches(0.2),y+Inches(0.5),cw-Inches(0.4),Inches(0.45),[[(txt,{"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
        register_reveal(s, rev)
    text(s, Inches(0.5), Inches(5.55), Inches(12.3), Inches(0.5),
         [[("🔴 Pide con cortesía: ", {"size":12,"bold":True,"color":RED}), ("Para mí… / ¿Me pone…? / ¿Me trae…? + por favor. Niet enkel «quiero».", {"size":12,"color":INK})]])
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(6.1), Inches(12.3), Inches(0.55),
             [[("Structuur: ", {"bold":True,"color":GD}), ("de primero (voor) · de segundo (hoofd) · de postre (na) · para beber (drank).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR pedir. Twee rollen fysiek verdelen (klas in camareros/clientes). Onthul per klik. "
             "Online: «¿camarero o cliente?» (classify) + «ordena el diálogo» + «¡pide en el restaurante!» (sim).")

# ============================================================ DIA 8 · QUIZ — camarero o cliente
def s08_quiz_rol():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · QUIZ", "¿Camarero o cliente?", "Klik een zin → wie het zegt verschijnt.", num=3)
    items=[("¿Qué va a tomar?","el camarero"),("Para mí, una sopa.","el cliente"),
           ("¿Y para beber?","el camarero"),("¿Me pone un refresco?","el cliente"),
           ("¡Que aproveche!","el camarero"),("La cuenta, por favor.","el cliente")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(6.05); rh=Inches(0.78)
    for i,(q,a) in enumerate(items):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(3.6),rh,[[(q,{"size":12.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(3.8),y,cw-Inches(3.9),rh,[[("→ "+a,{"size":13,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Camarero = vraagt (¿qué va a tomar? / ¿y para beber?). ", {"bold":True,"color":GD}),
               ("Cliente = bestelt (para mí… / ¿me pone…? / la cuenta).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ rol (retrieval). Klas roept de rol vóór de klik. Daarna in parejas de scène spelen.")

# ============================================================ DIA 9 · READING — la carta
def s09_reading():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§5 · LEER · COMPRENSIÓN", "La carta de Diego (menú)", "Lees en beantwoord. Klik een vraag → het antwoord verschijnt.", num=5)
    card(s, Inches(0.5), Inches(1.65), Inches(5.6), Inches(3.9), fill=GT, line=G, lw=1.4)
    avatar(s, "diego", Inches(0.85), Inches(1.95), Inches(1.1))
    text(s, Inches(2.1), Inches(2.0), Inches(3.8), Inches(1.3),
         [[("«Para empezar: guacamole con nachos (5 €) y elote (4 €). Platos fuertes: tacos de pollo (8 €), ceviche (10 €). "
            "Para terminar: flan (3 €), piña con lima (3 €).»",{"size":12.5,"italic":True,"color":INK})]], line=1.2)
    qa=[("¿Qué hay para empezar?","Guacamole con nachos / elote"),("¿Cuánto cuestan los tacos?","8 €"),
        ("¿El ceviche es un plato fuerte?","Sí, cuesta 10 €"),("¿Qué hay de postre?","Flan / piña con lima")]
    x=Inches(6.4); y=Inches(1.7)
    for q,a in qa:
        card(s,x,y,Inches(6.4),Inches(0.85),fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y+Inches(0.06),Inches(6.1),Inches(0.4),[[(q,{"size":12.5,"bold":True,"color":GD})]])
        rev=text(s,x+Inches(0.15),y+Inches(0.44),Inches(6.1),Inches(0.35),[[("→ "+a,{"size":12,"color":INK})]])
        register_reveal(s, rev)
        y=y+Inches(0.98)
    btn=noodroute(s)
    exercise_solucion(s, Inches(6.4), Inches(5.65), Inches(6.4), Inches(0.6),
             [[("🎯 Leesdoel: ", {"bold":True,"color":GD}), ("scannen naar platos y precios — niet élk woord begrijpen. Vergelijk met de carta van Lucía.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · READING (lezen→spreken-keten). Eerst globaal (waarover?), dan scannen. Onthul de antwoorden pas na de klas. "
             "Daarna: leerlingen zeggen wat ze «van a pedir» (transfer → Tarea La carta).")

# ============================================================ DIA 10 · LISTENING — en el restaurante
def s10_listening():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · ESCUCHAR", "Escucha el pedido", "Vier clientes piden. Klik un nombre → wat ze bestellen. (audio op de digitale pagina)", num=3)
    people=[("Leo","sopa + pollo","agua"),("Frida","tacos de pollo","refresco"),
            ("Mateo","ensalada + pescado","zumo"),("Sara","guacamole + ceviche","agua")]
    x0,y0=Inches(0.7),Inches(1.9); cw=Inches(2.95); ch=Inches(2.4)
    for i,(nm,com,beb) in enumerate(people):
        x=x0+i*(cw+Inches(0.1))
        card(s,x,y0,cw,ch,fill=WHITE,line=LINE,lw=1.2)
        rect(s,x,y0,cw,Inches(0.5),fill=GT)
        text(s,x,y0,cw,Inches(0.5),[[("🔊  "+nm,{"size":14,"bold":True,"color":GD,"font":DISPLAY})]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        text(s,x+Inches(0.15),y0+Inches(0.65),cw-Inches(0.3),Inches(0.4),[[("Come:",{"size":12,"color":MUT})]])
        rev1=text(s,x+Inches(0.15),y0+Inches(1.0),cw-Inches(0.3),Inches(0.5),[[(com,{"size":13,"bold":True,"color":INK})]],line=1.05)
        text(s,x+Inches(0.15),y0+Inches(1.6),cw-Inches(0.3),Inches(0.4),[[("Bebe:",{"size":12,"color":MUT})]])
        rev2=text(s,x+Inches(0.15),y0+Inches(1.95),cw-Inches(0.3),Inches(0.4),[[(beb,{"size":13,"bold":True,"color":G})]])
        register_reveal(s, rev1); register_reveal(s, rev2)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.85),
             [[("Modelo-audio (docent leest of TTS): ", {"bold":True,"color":GD}),
               ("«Para mí, de primero una sopa y de segundo pollo. Para beber, agua.» …", {"color":GD})],
              [("Daarna spreken: leerling speelt de cliente en bestelt zelf.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · LISTENING (selectief → spreken). Lees elk pedido voor (of TTS). Klas noteert comida + bebida; onthul per klik. "
             "Koppel meteen aan de rollenspel-scène (§3).")

# ============================================================ DIA 11 · GRAMMAR — lo/la/los/las (reveal)
def s11_od():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · GRAMÁTICA", "La cuenta → la traigo (lo/la/los/las)", "Klik een woord → het pronomen verschijnt. Vervang het voorwerp, niet herhalen.", num=4)
    R=[("el pan","lo"),("la cuenta","la"),("los tacos","los"),("las gambas","las"),("el postre","lo"),("la carta","la")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(3.95); ch=Inches(1.25)
    for i,(p,v) in enumerate(R):
        c=i%3; r=i//3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(ch+Inches(0.2))
        card(s,x,y,cw,ch,fill=WHITE,line=G,lw=1.4)
        text(s,x,y+Inches(0.12),cw,Inches(0.4),[[(p,{"size":13,"color":MUT})]],align=PP_ALIGN.CENTER)
        rev=text(s,x,y+Inches(0.5),cw,Inches(0.6),[[("→ "+v,{"size":26,"bold":True,"color":GD,"font":DISPLAY})]],align=PP_ALIGN.CENTER)
        register_reveal(s, rev)
    text(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.5),
         [[("🟡 Vóór het werkwoord: ", {"size":12,"color":INK}),
           ("¿La cuenta? → La traigo.   ¿Los tacos? → Los quiero.", {"size":12,"bold":True,"color":GD})]])
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.75), Inches(12.3), Inches(0.65),
             [[("lo (m.ev.) · la (v.ev.) · los (m.mv.) · las (v.mv.). ", {"bold":True,"color":GD}),
               ("Het pronomen staat vóór het vervoegde werkwoord — zo herhaal je het voorwerp niet.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR OD (reveal, A2-aanzet). Coro: klas zegt het woord vóór de klik. Kernidee: lo/la/los/las = «het/ze» + vóór het ww. "
             "Online: «¿lo, la, los o las?» (cloze).")

# ============================================================ DIA 12 · SPEAKING — pide en el restaurante
def s12_speaking():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · SPEAKING · INTERACCIÓN", "¡Pide en el restaurante!", "Speel de scène met de zinnen. Steun bouwt af: kaarten → beginwoorden → uit het hoofd.", num=3)
    avatar(s, "tu", Inches(11.4), Inches(1.7), Inches(1.3))
    labels=["Saludar","Pedir 1º","Pedir 2º","Pedir bebida","Pedir la cuenta","Cerrar"]
    frames=["Buenas tardes.","De primero, …","De segundo, …","¿Me pone…?","La cuenta, por favor.","Gracias."]
    x0,y0=Inches(0.5),Inches(1.8); cw=Inches(3.4); rh=Inches(0.8)
    for i,(lab,fr) in enumerate(zip(labels,frames)):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=G,lw=1.2,shadow=False)
        text(s,x+Inches(0.15),y+Inches(0.05),cw-Inches(0.3),Inches(0.32),[[(lab,{"size":10,"color":MUT})]])
        text(s,x+Inches(0.15),y+Inches(0.36),cw-Inches(0.3),Inches(0.4),[[(fr,{"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    text(s, Inches(0.5), Inches(5.0), Inches(10.5), Inches(0.9),
         [[("Ronda 1: ", {"size":12,"bold":True,"color":GD}), ("met de kaarten. ", {"size":12,"color":INK}),
           ("Ronda 2: ", {"size":12,"bold":True,"color":GD}), ("alleen beginwoorden. ", {"size":12,"color":INK}),
           ("Ronda 3: ", {"size":12,"bold":True,"color":GD}), ("uit het hoofd, ander pedido. ", {"size":12,"color":INK}),
           ("Ronda 4: ", {"size":12,"bold":True,"color":GD}), ("grábate en de digitale pagina.", {"size":12,"color":INK})]])
    chip(s, Inches(0.5), Inches(4.65), "🎙️ Grábate online · «Mensaje de voz: pide comida»", fill=GT, tcolor=GD, size=11)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.6), Inches(12.3), Inches(0.65),
             [[("Modelo: ", {"bold":True,"color":GD}), ("«Buenas. Para mí, de primero una sopa y de segundo pollo. ¿Me pone agua? … La cuenta, por favor.»", {"color":GD})]],
             trigger=btn, title_doc="MODELO · docent")
    foot(s)
    notes(s, "TEACHER · SPEAKING (interactie). Automatiseer saludar→pedir→cuenta in rondes met afbouwende steun. "
             "Online: recorder (opname + zelfevaluatie). Print blijft bruikbaar zonder opname.")

# ============================================================ DIA 13 · WRITING — mi carta
def s13_writing():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "WRITING · PRODUCCIÓN", "Mi carta (menú)", "Ontwerp je menu. Klik → een modeltekst verschijnt.", num=1)
    card(s, Inches(0.5), Inches(1.7), Inches(6.0), Inches(3.9), fill=WHITE, line=LINE, lw=1.2)
    text(s, Inches(0.7), Inches(1.85), Inches(5.6), Inches(0.4), [[("✍️ Escribe aquí tu carta:", {"size":12,"bold":True,"color":GD})]])
    for i in range(6):
        rect(s, Inches(0.7), Inches(2.4)+i*Inches(0.5), Inches(5.6), Inches(0.01), fill=LINE)
    chk=[("de primero … (precio)",),("de segundo … (precio)",),("de postre … (precio)",),("para beber … (precio)",),("cortesía: para mí / ¿me pone?",),("un plato de tu país/estilo",)]
    x=Inches(6.9); y=Inches(1.7)
    text(s,x,y,Inches(6),Inches(0.4),[[("Checklist:",{"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    for i,(c,) in enumerate(chk):
        text(s,x,y+Inches(0.5)+i*Inches(0.45),Inches(6),Inches(0.4),[[("☐  "+c,{"size":13,"color":INK})]])
    rev=card(s, x, Inches(4.35), Inches(6.0), Inches(1.25), fill=GT, line=G, lw=1.2)
    text(s, x+Inches(0.15), Inches(4.4), Inches(5.7), Inches(1.2),
         [[("Modelo: ", {"size":12,"bold":True,"color":GD}),
           ("«El Sabor de Diego. De primero: guacamole (5 €). De segundo: tacos de pollo (8 €). De postre: flan (3 €). Para beber: refresco (2 €).»",{"size":12,"italic":True,"color":INK})]], line=1.15)
    register_reveal(s, rev)
    noodroute(s); foot(s)
    notes(s, "TEACHER · WRITING (lezen→schrijven). Checklist = zichtbare steun; onthul het model pas na het schrijven (retrieval). "
             "Nakijkfocus: secties, precios, cortesía. Dit voedt de Tarea «La carta».")

# ============================================================ DIA 14 · VOCAB — fruta/verdura/mesa (reveal)
def s14_fruta_mesa():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · VOCABULARIO · MERCADO", "Fruta, verdura y la mesa", "Klik een woord → de vertaling verschijnt. Bouw je woordnetwerk.", num=1)
    data=[("la manzana","appel"),("el plátano","banaan"),("las uvas","druiven"),("la piña","ananas"),
          ("el tomate","tomaat"),("la lechuga","sla"),("la cebolla","ui"),("el maíz","maïs"),
          ("el plato","bord"),("el vaso","glas"),("el tenedor","vork"),("la cuchara","lepel")]
    x0,y0=Inches(0.5),Inches(1.7); cw=Inches(3.0); rh=Inches(0.7)
    for i,(es,nl) in enumerate(data):
        c=i%4; r=i//4; x=x0+c*(cw+Inches(0.1)); y=y0+r*(rh+Inches(0.14))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.12),y,Inches(1.6),rh,[[(es,{"size":12,"bold":True,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(1.7),y,cw-Inches(1.8),rh,[[("→ "+nl,{"size":11.5,"color":G})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.9),
             [[("Combineer met cantidad: ", {"bold":True,"color":GD}),
               ("un kilo de manzanas · muchas uvas · un poco de maíz. Como con tenedor y cuchara.", {"color":GD})],
              [("Los cubiertos: el tenedor, el cuchillo, la cuchara. La mesa: el plato, el vaso, la servilleta.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCAB fruta/verdura/mesa. Klik onthult; koppel elk woord aan een cantidad-zin. Volledige set + audio op de digitale pagina "
             "(flip cards + memoria).")

# ============================================================ DIA 15 · TALLER — conectores + ortografía
def s15_taller():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "TALLER DE LENGUA", "Conectores de secuencia + ortografía", "Klik een item → correcte vorm. Gereedschap voor recepten en spelling.", num=1)
    text(s, Inches(0.5), Inches(1.5), Inches(6), Inches(0.35), [[("A · conectores: primero · luego · después · por último", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    fixes=[("___ , corta el tomate","Primero"),("___ , añade la sal","Luego"),("___ , espera 15 min","Después"),("___ , ¡a comer!","Por último")]
    y=Inches(1.95)
    for q,a in fixes:
        card(s,Inches(0.5),y,Inches(6.0),Inches(0.6),fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,Inches(0.62),y,Inches(3.6),Inches(0.6),[[(q,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,Inches(4.3),y,Inches(2.0),Inches(0.6),[[("→ "+a,{"size":12,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y=y+Inches(0.72)
    text(s, Inches(6.9), Inches(1.5), Inches(6), Inches(0.35), [[("B · ortografía: ¿n o ñ?", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    conn=[("la pi__a (ananas)","ñ","piña"),("el ni__o","ñ","niño"),("la ca__a","ñ","caña"),("a__o (jaar)","ñ","año")]
    y=Inches(1.95)
    for q,a,gl in conn:
        card(s,Inches(6.9),y,Inches(5.9),Inches(0.6),fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,Inches(7.02),y,Inches(3.2),Inches(0.6),[[(q,{"size":11.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,Inches(10.3),y,Inches(2.4),Inches(0.6),[[(a+" ",{"size":12,"bold":True,"color":GD}),("· "+gl,{"size":9,"italic":True,"color":MUT})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y=y+Inches(0.72)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.85),
             [[("A: ", {"bold":True,"color":GD}), ("primero → luego/después → por último (voor recepten en stappen).", {"color":GD})],
              [("🔴 B: ", {"bold":True,"color":RED}), ("la ñ klinkt «nj»: piña, niño, caña, año. Verwar niet met n (pena ≠ peña).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · TALLER. Conectores = ideaal met een receta (guacamole). ñ = spelling-valstrik. Meteen toepassen in de mini-receta. "
             "Online: «ordena la receta» + «ordena el diálogo».")

# ============================================================ DIA 16 · CULTURE — tacos & mercados
def s16_cultura():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "CULTURA · PARADA 5", "Tacos, mercados y horarios", "Klik een kaart → het weetje verschijnt. La comida une al mundo hispano.", num=1)
    cards=[("🌮 El taco","De maíz, con carne, verdura y salsa. En la CDMX hay taquerías por todas partes: al pastor, de pollo, de pescado.","El taco = het hart van de Mexicaanse keuken."),
           ("🏪 Los mercados","Compras fruta, verdura y comida fresca. Regatear el precio es normal. Colores, olores y mucha vida.","De plek om cantidades te oefenen."),
           ("🕐 Horarios","España cena muy tarde (21:30). México y Bélgica un poco antes. Contraste: paella 🇪🇸 · tacos 🇲🇽 · arepa 🇨🇴 · ceviche 🇵🇪.","No comas a las 18:00 en Madrid.")]
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
             [[("Actividad: ", {"bold":True,"color":GD}), ("schrijf 3 zinnen over een typisch gerecht bij jou thuis (¿qué es? ¿qué lleva? ¿cuándo lo comes?).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · CULTURE (identiteit in diversiteit, LPD 5). Onthul per kaart. Vergelijk horarios ES/MX/BE. Bruggetje naar de Tarea La carta. "
             "Online: «plato ↔ país» (match).")

# ============================================================ DIA 17 · QUIZ — haz la pregunta / pedido
def s17_quiz_pedido():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · QUIZ · INTERACCIÓN", "Completa el pedido", "Wat past? Klik → het antwoord verschijnt.", num=3)
    items=[("¿Qué va a ___? (nemen)","tomar"),("___ mí, una sopa.","Para"),
           ("¿Me ___ agua? (serveren)","pone"),("La ___, por favor.","cuenta"),
           ("Voy ___ comer un taco.","a"),("De ___, un flan. (na)","postre")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(6.05); rh=Inches(0.78)
    for i,(ans,q) in enumerate(items):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(3.6),rh,[[(ans,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(3.8),y,cw-Inches(3.95),rh,[[("→ "+q,{"size":12,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("De bestelzinnen: ", {"bold":True,"color":GD}),
               ("¿Qué va a tomar? · Para mí… · ¿Me pone…? · La cuenta, por favor · Voy a comer…", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ interactie. Klas vult de zin vóór de klik. Daarna de rollenspel-scène in parejas.")

# ============================================================ DIA 18 · FINAL_MISSION — La carta
def s18_tarea():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(1.35), fill=GD)
    text(s, Inches(0.5), Inches(0.18), Inches(9), Inches(1.0),
         [[("🍽️ Tarea final · La carta", {"size":30,"bold":True,"color":WHITE,"font":DISPLAY})],
          [("Maak de carta van je eigen restaurante y representa la escena camarero ↔ cliente.", {"size":13,"italic":True,"color":GT})]])
    avatar(s, "mochila", Inches(11.6), Inches(0.2), Inches(1.0))
    pasos=[("1","Elige un nombre y estilo","mexicano, español…"),
           ("2","Rellena la carta","primeros · segundos · postres · bebidas + precios"),
           ("3","Escribe el diálogo","saludar → pedir → ¡que aproveche! → la cuenta"),
           ("4","Representa la escena","en pareja (of neem audio op)"),
           ("5","Recomienda un plato","«Le recomiendo…» según los gustos del cliente")]
    y=Inches(1.7)
    for n,es,nl in pasos:
        b=rect(s,Inches(0.5),y,Inches(0.5),Inches(0.5),fill=G,round=True,radius=0.5)
        tf=b.text_frame;tf.vertical_anchor=MSO_ANCHOR.MIDDLE;p=tf.paragraphs[0];p.alignment=PP_ALIGN.CENTER
        rr=p.add_run();rr.text=n;rr.font.size=Pt(15);rr.font.bold=True;rr.font.name=DISPLAY;rr.font.color.rgb=WHITE
        text(s,Inches(1.2),y,Inches(4.2),Inches(0.55),[[(es,{"size":14,"bold":True,"color":GD,"font":DISPLAY})]],anchor=MSO_ANCHOR.MIDDLE)
        text(s,Inches(5.5),y,Inches(7.2),Inches(0.55),[[(nl,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        y=y+Inches(0.62)
    text(s, Inches(0.5), Inches(5.0), Inches(12), Inches(0.35), [[("Rúbrica · ¿lo logré?", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    crit=["4 secties + precios","cortesía (para mí/¿me pone?)","voy a pedir + la cuenta","representar la escena"]
    x=Inches(0.5)
    for c in crit:
        chip(s,x,Inches(5.45),"☐ "+c,fill=GT,tcolor=GD,size=11,w=Inches(3.0)); x=x+Inches(3.1)
    text(s, Inches(0.5), Inches(6.05), Inches(12), Inches(0.4),
         [[("🎯 ", {"size":12}), ("Afzender jij (het restaurant) · ontvanger de cliente · doel een menu aanbieden & een pedido opnemen · situatie un restaurante en CDMX · resultaat: carta + gespeelde dialoog.", {"size":11.5,"italic":True,"color":MUT})]])
    foot(s)
    notes(s, "TEACHER · FINAL_MISSION (communicatieve eindtaak). Afzender/ontvanger/doel/situatie/resultaat expliciet. Beoordeel met de rúbrica; "
             "opname + zelfevaluatie op de digitale pagina. Voeg een mini-encuesta + grafiekje toe (platos favoritos van de klas).")

# ============================================================ DIA 19 · QUIZ — la mezcla
def s19_mezcla():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "QUIZ · LA MEZCLA", "Ophaal door elkaar", "Gemengde ophaal van de hele unit. Klik een vraag → het antwoord. (retrieval)", num=1)
    items=[("___ fruta (veel)","mucha"),("___ tomates (veel)","muchos"),("ir, yo → futuro","voy a"),
           ("ir, nosotros → futuro","vamos a"),("bestellen: «para ___»","mí"),("¿Me ___ agua? (serveren)","pone"),
           ("¿La cuenta? → ___ traigo","la"),("Voy ___ comer","a")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(6.05); rh=Inches(0.62)
    for i,(q,a) in enumerate(items):
        c=i//4; r=i%4; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.16))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(3.4),rh,[[(q,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(3.55),y,cw-Inches(3.7),rh,[[("→ "+a,{"size":12,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.05), Inches(12.3), Inches(0.55),
             [[("Alles komt terug: ", {"bold":True,"color":GD}), ("cantidades (concord) · ir a + infinitivo · pedir/cortesía · lo/la/los/las.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ mezcla (retrieval vóór herlezen). Zonder waarschuwing door elkaar. Exit-ticket. Zwakke punten → terug via menu.")

# ============================================================ DIA 20 · FEEDBACK/REPASO
def s20_repaso():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "REPASO · LO ESENCIAL", "Lo esencial de un vistazo", "De volledige herhaling (17 spellen, drills) staat online. Hier: de kern + semáforo.", num=1)
    ess=["Cantidades: mucho/-a/-os/-as (past aan) · un poco de (blijft gelijk) · un kilo/una botella/un paquete de.",
         "Futuro próximo: ir (voy, vas, va, vamos, vais, van) + a + infinitivo: «Voy a comer».",
         "Pedir con cortesía: ¿Qué va a tomar? · Para mí… · ¿Me pone…? · La cuenta, por favor. De primero/segundo/postre.",
         "lo/la/los/las: ¿La cuenta? → La traigo. ¿Los tacos? → Los quiero (vóór het werkwoord).",
         "🔴 Trampas: muchA fruta ≠ mucho · voy A comer · pide con cortesía (niet enkel «quiero») · la ñ (piña)."]
    card(s, Inches(0.5), Inches(1.6), Inches(12.3), Inches(2.5), fill=CREMA, line=None)
    y=Inches(1.8)
    for e in ess:
        text(s, Inches(0.8), y, Inches(11.8), Inches(0.45), [[("• ", {"size":13,"bold":True,"color":GD}),(e,{"size":12,"color":INK})]])
        y=y+Inches(0.46)
    text(s, Inches(0.5), Inches(4.3), Inches(12), Inches(0.35), [[("Semáforo — ¿cómo lo llevas?", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    can=["comida/bebida benoemen","cantidades (mucho/un kilo de)","voy a comer (ir a + inf.)","pedir + la cuenta","lo/la/los/las"]
    y=Inches(4.75)
    for c in can:
        text(s,Inches(0.8),y,Inches(7.0),Inches(0.4),[[(c,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        for j,(em,col) in enumerate([("🔴",RED),("🟠",AMBER),("🟢",G)]):
            chip(s,Inches(8.0)+j*Inches(1.5),y+Inches(0.03),em+" ",fill=WHITE,tcolor=col,size=12,w=Inches(1.3))
        y=y+Inches(0.42)
    foot(s)
    notes(s, "TEACHER · FEEDBACK/REPASO. Semáforo = zelfevaluatie. Repaso-drills online (17 spellen). Bruggetje: U6 «De tiendas» — "
             "de compras en el mercado: precios, ofertas, regateo.")

# ============================================================ DIA 21 · TEACHER_NOTES
def s21_teacher():
    s = slide(); bg(s, GD)
    text(s, Inches(0.6), Inches(0.4), Inches(12), Inches(0.8), [[("TEACHER_NOTES · U5 «¡Ñam!»", {"size":26,"bold":True,"color":WHITE,"font":DISPLAY})]])
    blocks=[("Timing (50 min)","Menu 2' · cantidades 10' · ir a + inf. 8' · pedir/cortesía 10' · lo/la/los/las 6' · lectura/escucha 8' · cultura 3' · Tarea-briefing 3'."),
            ("Kernvalstrikken","muchA fruta ≠ mucho (concord) · un poco de blijft gelijk · voy A comer (a niet vergeten) · 2e ww = infinitief · pide con cortesía (para mí/¿me pone?) · lo/la/los/las vóór het ww · la ñ (piña)."),
            ("Differentiatie (zij-instromers)","Alles start vanaf nul. Sterker: hele restaurantscène + eigen carta + recomendar. Zwakker: cantidad-kaart en ir-tabel langer open, cortesía-frames houden."),
            ("Digitaal","17 spellen + flip cards + klikbare kaart + recorder (Hablar) + Lectura (dos cartas) op de página digital. QR's in het boek → juiste anker. Conjugador = aparte tool."),
            ("Evaluatie","Tarea «La carta» met rúbrica (4 criteria). LPD 3·4·7·8 + 5 (cultura) + 1·2 (receptief: lezen/luisteren).")]
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
    s01_title(); s02_menu(); s03_vocab(); s04_cantidades(); s05_cantidad_quiz(); s06_ir_a(); s07_pedir()
    s08_quiz_rol(); s09_reading(); s10_listening(); s11_od(); s12_speaking(); s13_writing()
    s14_fruta_mesa(); s15_taller(); s16_cultura(); s17_quiz_pedido(); s18_tarea(); s19_mezcla(); s20_repaso()
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
