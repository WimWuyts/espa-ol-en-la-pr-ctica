#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_u4_docente.py — Interactieve PowerPoint C5 · Unidad 4 «Me gusta» (parada València)
=======================================================================================
Zelfde engine/pijplijn als de golden sample U0/U1 (gen_u0_docente.py wordt geïmporteerd:
low-level helpers, on-click <p:timing>-animaties, hyperlink-navigatie). Enkel de SLIDES
zijn U4-specifiek. Twee decks (beide .pptx):
  · C5_U4_docente.pptx — vrije navigatie, oplossingen bij klik + didactiek in spreker-notities.
  · C5_U4_alumno.pptx  — gewone diavoorstelling, antwoorden verschijnen bij klik (F5, geen kiosk).
Huisstijl groen (C5). Spaans-eerst + NL-steun. ≥20 dia's. Dekt de vier vaardigheden.
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
OUT_DOCENTE = os.path.join(HERE, "C5_U4_docente.pptx")
OUT_ALUMNO_PPTX = os.path.join(HERE, "C5_U4_alumno.pptx")
TAB = "U4 · ME GUSTA"

def foot(s): footer(s, tab=TAB, page=pg())

# ============================================================ DIA 1 · TITLE
def s01_title():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(4.7), fill=G)
    rect(s, 0, Inches(4.7), EMU_W, Inches(0.09), fill=GD)
    text(s, Inches(0.6), Inches(0.35), Inches(3.4), Inches(3.6),
         [[("4", {"size": 260, "bold": True, "color": RGBColor(0x2E,0xB0,0x85), "font": DISPLAY})]],
         anchor=MSO_ANCHOR.MIDDLE)
    chip(s, Inches(4.35), Inches(0.85), "LA RUTA · PARADA 4 · VALÈNCIA 🇪🇸", fill=WHITE, tcolor=GD, size=12)
    text(s, Inches(4.3), Inches(1.35), Inches(8.6), Inches(1.5),
         [[("Me gusta", {"size": 72, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(4.35), Inches(2.7), Inches(8.4), Inches(0.6),
         [[("Hablar de gustos: música, deportes, cine y planes — en València, con Lucía y Bea.", {"size": 15, "italic": True, "color": GT})]])
    text(s, Inches(4.35), Inches(3.35), Inches(8.4), Inches(0.9),
         [[("¿Qué te gusta hacer en tu tiempo libre?", {"size": 24, "bold": True, "color": WHITE, "font": DISPLAY})],
          [("Wat doe je graag in je vrije tijd?", {"size": 13, "italic": True, "color": GT})]])
    text(s, Inches(0.6), Inches(4.95), Inches(6), Inches(0.4),
         [[("La gente de la ruta — je reisgezellen", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    x = Inches(0.6)
    for nm, city in [("lucia","Sevilla 🇪🇸"),("diego","CDMX 🇲🇽"),("valen","Cartagena 🇨🇴"),
                     ("nina","Cusco 🇵🇪"),("tu","Tú · Flandes 🇧🇪"),("mochila","La mochila")]:
        avatar(s, nm, x, Inches(5.4), Inches(1.0))
        text(s, x - Inches(0.15), Inches(6.42), Inches(1.3), Inches(0.5),
             [[(nm.capitalize() if nm!="tu" else "Tú", {"size": 10.5, "bold": True, "color": INK})],
              [(city.split("·")[-1].strip() if nm!="tu" else "de reiziger = jij", {"size": 8.5, "color": MUT})]],
             align=PP_ALIGN.CENTER)
        x = x + Inches(2.05)
    foot(s)
    notes(s, "TEACHER · TITLE. Parada 4 = València (la costa), met Lucía en haar valenciaanse vriendin Bea. Doel: hablar de gustos "
             "(gustar/encantar), akkoord gaan of niet (también/tampoco/a mí sí/no) en un plan proponer (querer/poder + infinitivo, quedar). "
             "Kernvalstrik meteen benoemen: gustar werkt ómgekeerd — «me gusta la música» = «de muziek bevalt mij»; meervoud → gustaN. "
             "Docentdeck = vrije navigatie + oplossing in notities; leerlingdeck (.pptx, F5) = elke klik onthult het volgende antwoord.")

# ============================================================ DIA 2 · LESSON_MENU
def s02_menu():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "MENÚ DE LA LECCIÓN", "El mapa de la Unidad 4",
               "Kies je route — klik een tegel. Alles oefent naar de Tarea «Mi playlist» toe.", num=4)
    tiles = [
        ("§1", "Me gusta(n)", "gustar/encantar · pronombres OI", G, 3),
        ("§2", "De acuerdo o no", "también/tampoco · a mí sí/no", G, 7),
        ("§3", "Proponer un plan", "querer/poder + inf. · quedar", G, 11),
        ("§4", "Lectura + escucha", "perfiles de gustos", G, 9),
        ("★", "Cultura · Rosalía", "música y ocio joven", GD, 16),
        ("🎧", "Tarea · Mi playlist", "je playlist + presentarla", GD, 18),
        ("?", "Quiz «La mezcla»", "gemengde ophaal — mét oplossing", AMBER, 19),
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
             "Begin bij §1 (gustar) — het hart van de unit. Kruisverwijzing print/HTML: «oefen online — 24 juegos».")

# ============================================================ DIA 3 · VOCABULARY — gustos/ocio
def s03_vocab():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · VOCABULARIO", "Los gustos y el ocio", "De woorden van je vrije tijd — observa. Herken ze, dan gebruik je ze.", num=1)
    legend_func(s, Inches(9.7), Inches(0.55))
    rows = [("me gusta(n)","leuk vinden","el fútbol"),("me encanta(n)","dol zijn op","bailar"),
            ("el deporte","de sport","nadar · jugar"),("la música","de muziek","escuchar · tocar"),
            ("la canción","het liedje","el/la cantante"),("la película","de film","la serie · el cine"),
            ("la playa","het strand","el mar · la costa"),("los videojuegos","videospellen","salir con amigos")]
    x0,y0 = Inches(0.5), Inches(1.6); cw=Inches(6.1); rh=Inches(0.6)
    for i,(k,v,nl) in enumerate(rows):
        c = 0 if i<4 else 1; r = i%4
        x = x0 + c*(cw+Inches(0.15)); y = y0 + r*(rh+Inches(0.12))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x+Inches(0.15), y, Inches(2.4), rh, [[(k, {"size":13,"bold":True,"color":GD})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x+Inches(2.5), y, Inches(2.3), rh, [[(v, {"size":12,"color":INK})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x+Inches(4.6), y, Inches(1.4), rh, [[(nl, {"size":9,"italic":True,"color":MUT})]], anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(4.75), Inches(12.3), Inches(0.5),
         [[("Opinar: ", {"size":13,"bold":True,"color":GD,"font":DISPLAY}),
           ("Me gusta", {"size":13,"bold":True,"color":F_VERB}), (" (1/inf.) · ",{"size":13,"color":INK}),
           ("Me gustan", {"size":13,"bold":True,"color":F_VERB}), (" (mv.) · ",{"size":13,"color":INK}),
           ("Me encanta(n)", {"size":13,"bold":True,"color":F_VERB}), (" (sterker) · ",{"size":13,"color":INK}),
           ("No me gusta(n)", {"size":13,"bold":True,"color":F_NEG}), (" (–)",{"size":13,"color":INK})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.35), Inches(12.3), Inches(0.95),
             [[("🔴 Gustar al revés: ", {"bold":True,"color":RED}), ("me gusta la música", {"bold":True,"color":GD}),
               (" = «de muziek bevalt mij». ", {"color":GD}),
               ("🔴 Meervoud → gustaN: ", {"bold":True,"color":RED}), ("me gustan los deportes.", {"bold":True,"color":GD})],
              [("Adverbios de frecuencia: siempre · a menudo · a veces · casi nunca · nunca · todos los días.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCABULARY. Toon de woorden per cluster (ocio/música/sentimientos). Laat raden zónder de NL-gloss. "
             "Kernframe «(A mí) me gusta(n)…» meteen inoefenen. Online: flip cards + Memoria de los gustos + Música y cine.")

# ============================================================ DIA 4 · GRAMMAR — gustar al revés (color)
def s04_gustar():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · GRAMÁTICA VISUAL", "Gustar — al revés («het bevalt mij»)", "Kleur = taalfunctie. Het ding is het ONDERWERP; jij bent OI.", num=1)
    legend_func(s, Inches(9.7), Inches(0.55))
    seg = [("A mí ", F_OBJ),("me ", F_SUBJ),("gusta ", F_VERB),("la música ", F_PLAC),("y ", INK),
           ("me ", F_SUBJ),("gustan ", F_VERB),("los deportes.", F_PLAC)]
    runs=[[(t,{"size":25,"bold":True,"color":c,"font":DISPLAY}) for t,c in seg]]
    card(s, Inches(0.5), Inches(1.7), Inches(12.3), Inches(1.2), fill=GT, line=None)
    text(s, Inches(0.8), Inches(1.7), Inches(11.7), Inches(1.2), runs, anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(3.15), Inches(12), Inches(0.4), [[("Los pronombres OI — ¿a quién le gusta?", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    frame=[("(a mí) me","gusta el mar"),("(a ti) te","¿gusta bailar?"),("(a él/ella) le","gusta la playa"),
           ("(a nosotros) nos","gustan los conciertos"),("(a vosotros) os","¿gusta el cine?"),("(a ellos) les","gusta la música")]
    x0,y0=Inches(0.5),Inches(3.6); cw=Inches(4.0); rh=Inches(0.62)
    for i,(a,b) in enumerate(frame):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.12))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(1.7),rh,[[(a,{"size":12.5,"bold":True,"color":F_SUBJ})]],anchor=MSO_ANCHOR.MIDDLE)
        text(s,x+Inches(1.85),y,cw-Inches(2.0),rh,[[(b,{"size":11.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.7), Inches(12.3), Inches(0.7),
             [[("Regla: ", {"bold":True,"color":GD}), ("gusta + 1 ding of infinitivo · gustan + meervoud. Idem encanta/encantan. Al revés: het ding is het onderwerp!", {"color":GD})]],
             trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR (color-coding). Maak de omgekeerde constructie fysiek zichtbaar: teken twee pijlen (ik ↔ het ding). "
             "gustaN = het meest hardnekkige punt. Elke leerling bouwt «(A mí) me gusta(n)…» met eigen woorden. Kleur nooit als enige drager.")

# ============================================================ DIA 5 · QUIZ — gusta o gustan
def s05_gusta_gustan():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · QUIZ", "¿gusta o gustan?", "Klik een zin → de juiste vorm verschijnt. Eén ding/infinitivo = gusta · meerdere = gustan.", num=1)
    items=[("Me ___ los deportes.","gustan","mv."),("Me ___ el fútbol.","gusta","1 ding"),
           ("Me ___ bailar.","gusta","infinitivo"),("Me ___ las series.","gustan","mv."),
           ("Me ___ la playa.","gusta","1 ding"),("Me ___ los videojuegos.","gustan","mv.")]
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
             [[("gusta = ", {"bold":True,"color":G}), ("één ding of een infinitivo (bailar, leer…).", {"color":GD})],
              [("gustan = ", {"bold":True,"color":G}), ("meerdere dingen (los deportes, las series). Tel wat je leuk vindt!", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ (reveal). Laat de klas eerst kiezen, klik dan. Truc: tel het aantal dingen. Een infinitief telt als 1 → gusta. "
             "Online: «¿gusta o gustan?» (classify) + «completa: gusta o gustan» (cloze).")

# ============================================================ DIA 6 · GRAMMAR — pronombres OI (reveal)
def s06_oi():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · GRAMÁTICA", "Los pronombres OI (me/te/le…)", "Denk het woord, klik de kaart → het verschijnt. Voor élke persoon een ander OI-woord.", num=1)
    R=[("a mí","me"),("a ti","te"),("a él/ella/usted","le"),("a nosotros/-as","nos"),("a vosotros/-as","os"),("a ellos/-as/ustedes","les")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(3.95); ch=Inches(1.25)
    for i,(p,v) in enumerate(R):
        c=i%3; r=i//3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(ch+Inches(0.2))
        card(s,x,y,cw,ch,fill=WHITE,line=G,lw=1.4)
        text(s,x,y+Inches(0.12),cw,Inches(0.4),[[(p,{"size":13,"color":MUT})]],align=PP_ALIGN.CENTER)
        rev=text(s,x,y+Inches(0.5),cw,Inches(0.6),[[(v,{"size":26,"bold":True,"color":GD,"font":DISPLAY})]],align=PP_ALIGN.CENTER)
        register_reveal(s, rev)
    text(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.5),
         [[("🟡 Verduidelijk met «a + persoon»: ", {"size":12,"color":INK}),
           ("A Bea le gusta la playa.", {"size":12,"bold":True,"color":GD}),
           ("   A mis amigos les gustan los conciertos.", {"size":12,"color":INK})]])
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.75), Inches(12.3), Inches(0.65),
             [[("me · te · le · nos · os · les. ", {"bold":True,"color":GD}),
               ("Het OI-woord verandert per persoon; gusta/gustan hangt af van het DING, niet van de persoon.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR OI (reveal). Coro: klas zegt het woord vóór de klik. Kernidee: me/te/le… = «aan wie», gusta/gustan = «wat». "
             "Online: «el pronombre OI» (classify) + «¿me, te, le…?» (cloze).")

# ============================================================ DIA 7 · GRAMMAR — reacciones
def s07_reacciones():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · GRAMÁTICA", "Estar de acuerdo o no", "Vier korte reacties. Klik een situatie → de reactie verschijnt.", num=2)
    items=[("+ akkoord","«Me gusta.» → A mí también",G),("+ oneens","«Me gusta.» → A mí no",AMBER),
           ("– akkoord","«No me gusta.» → A mí tampoco",G),("– oneens","«No me gusta.» → A mí sí",AMBER)]
    x0,y0=Inches(0.5),Inches(1.8); cw=Inches(6.05); ch=Inches(1.2)
    for i,(lab,txt,col) in enumerate(items):
        c=i%2; r=i//2; x=x0+c*(cw+Inches(0.2)); y=y0+r*(ch+Inches(0.2))
        card(s,x,y,cw,ch,fill=WHITE,line=col,lw=1.4)
        chip(s,x+Inches(0.2),y+Inches(0.15),lab,fill=GT,tcolor=GD,size=11)
        rev=text(s,x+Inches(0.2),y+Inches(0.6),cw-Inches(0.4),Inches(0.5),[[(txt,{"size":15,"bold":True,"color":GD,"font":DISPLAY})]])
        register_reveal(s, rev)
    text(s, Inches(0.5), Inches(4.55), Inches(12.3), Inches(0.5),
         [[("🔴 tampoco = «ook niet» ", {"size":12,"bold":True,"color":RED}), ("(na een negatieve zin), niet «ook». Zeg altijd «a mí», niet «yo».", {"size":12,"color":INK})]])
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.2), Inches(12.3), Inches(0.9),
             [[("+ akkoord → también · + oneens → a mí no · – akkoord → tampoco · – oneens → a mí sí.", {"bold":True,"color":GD})],
              [("Espejo: eerst kijken of de zin + of – is, dan of je akkoord bent.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR reacciones. Twee assen: +/– én akkoord/oneens. Onthul per klik. Snelle klasrespons met kaartjes/handen. "
             "Online: «la reacción correcta» (classify) + «el espejo de reacciones» (match).")

# ============================================================ DIA 8 · QUIZ — reacción reveal
def s08_quiz_reaccion():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · QUIZ", "Reacciona (akkoord)", "Klik een uitspraak → de juiste akkoord-reactie verschijnt.", num=2)
    items=[("Me gusta el mar.","A mí también"),("No me gusta el frío.","A mí tampoco"),
           ("Me encanta bailar.","A mí también"),("No me gustan los lunes.","A mí tampoco"),
           ("Me gustan los videojuegos.","A mí también"),("No me gusta madrugar.","A mí tampoco")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(6.05); rh=Inches(0.78)
    for i,(q,a) in enumerate(items):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(3.4),rh,[[(q,{"size":12.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(3.6),y,cw-Inches(3.7),rh,[[("→ "+a,{"size":13,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Akkoord: + → también · – → tampoco. ", {"bold":True,"color":GD}),
               ("Oneens zou zijn: + → a mí no · – → a mí sí.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ reacciones (retrieval). Klas roept de reactie vóór de klik. Daarna in parejas: gustos delen en reageren.")

# ============================================================ DIA 9 · READING — perfil de gustos
def s09_reading():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · LEER · COMPRENSIÓN", "El perfil de Lucía (playlist)", "Lees en beantwoord. Klik een vraag → het antwoord verschijnt.", num=4)
    card(s, Inches(0.5), Inches(1.65), Inches(5.6), Inches(3.9), fill=GT, line=G, lw=1.4)
    avatar(s, "lucia", Inches(0.85), Inches(1.95), Inches(1.1))
    text(s, Inches(2.1), Inches(2.0), Inches(3.8), Inches(1.3),
         [[("«¡Hola! Me encanta la música. Mi artista favorita es Rosalía. También me gusta bailar flamenco. "
            "Los fines de semana voy a la playa. No me gustan los videojuegos, prefiero salir.»",{"size":12.5,"italic":True,"color":INK})]], line=1.2)
    qa=[("¿Qué le encanta a Lucía?","La música"),("¿Quién es su artista favorita?","Rosalía"),
        ("¿Qué le gusta hacer?","Bailar flamenco / ir a la playa"),("¿Qué no le gusta?","Los videojuegos")]
    x=Inches(6.4); y=Inches(1.7)
    for q,a in qa:
        card(s,x,y,Inches(6.4),Inches(0.85),fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y+Inches(0.06),Inches(6.1),Inches(0.4),[[(q,{"size":12.5,"bold":True,"color":GD})]])
        rev=text(s,x+Inches(0.15),y+Inches(0.44),Inches(6.1),Inches(0.35),[[("→ "+a,{"size":12,"color":INK})]])
        register_reveal(s, rev)
        y=y+Inches(0.98)
    btn=noodroute(s)
    exercise_solucion(s, Inches(6.4), Inches(5.65), Inches(6.4), Inches(0.6),
             [[("🎯 Leesdoel: ", {"bold":True,"color":GD}), ("scannen naar wat iemand (niet) leuk vindt — niet élk woord begrijpen.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · READING (lezen→schrijven-keten). Eerst globaal (waarover?), dan scannen. Onthul de antwoorden pas na de klas. "
             "Daarna: leerlingen schrijven hun EIGEN perfil (transfer → Tarea Mi playlist).")

# ============================================================ DIA 10 · LISTENING — escucha los gustos
def s10_listening():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · ESCUCHAR", "Escucha y anota el gusto", "Vier jongeren praten over hun smaak. Klik een naam → wat ze leuk vinden. (audio op de digitale pagina)", num=4)
    people=[("Leo","la música pop","no: el deporte"),("Frida","los videojuegos","no: madrugar"),
            ("Mateo","el fútbol","no: las series"),("Sara","bailar y el cine","no: el frío")]
    x0,y0=Inches(0.7),Inches(1.9); cw=Inches(2.95); ch=Inches(2.4)
    for i,(nm,si,no) in enumerate(people):
        x=x0+i*(cw+Inches(0.1))
        card(s,x,y0,cw,ch,fill=WHITE,line=LINE,lw=1.2)
        rect(s,x,y0,cw,Inches(0.5),fill=GT)
        text(s,x,y0,cw,Inches(0.5),[[("🔊  "+nm,{"size":14,"bold":True,"color":GD,"font":DISPLAY})]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        text(s,x+Inches(0.15),y0+Inches(0.65),cw-Inches(0.3),Inches(0.4),[[("Le gusta:",{"size":12,"color":MUT})]])
        rev1=text(s,x+Inches(0.15),y0+Inches(1.0),cw-Inches(0.3),Inches(0.5),[[(si,{"size":13,"bold":True,"color":INK})]],line=1.05)
        text(s,x+Inches(0.15),y0+Inches(1.6),cw-Inches(0.3),Inches(0.4),[[("No le gusta:",{"size":12,"color":MUT})]])
        rev2=text(s,x+Inches(0.15),y0+Inches(1.95),cw-Inches(0.3),Inches(0.4),[[(no.replace("no: ",""),{"size":13,"bold":True,"color":RED})]])
        register_reveal(s, rev1); register_reveal(s, rev2)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.85),
             [[("Modelo-audio (docent leest of TTS): ", {"bold":True,"color":GD}),
               ("«A mí me gusta la música pop, pero no me gusta el deporte.» …", {"color":GD})],
              [("Daarna spreken: leerling reageert (a mí también/tampoco/sí/no) op elk personage.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · LISTENING (selectief → spreken). Lees elk profiel voor (of TTS op de digitale pagina). Klas noteert gusto + no gusto; "
             "onthul per klik. Koppel meteen aan reacties (§2).")

# ============================================================ DIA 11 · GRAMMAR — querer/poder + inf.
def s11_querer_poder():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · GRAMÁTICA", "Querer / poder + infinitivo", "Klik een kolomkop → de vormen verschijnen. Let op: e→ie, o→ue (behalve nosotros/vosotros).", num=3)
    cols=[("querer (e→ie)",["quiero","quieres","quiere","queremos","queréis","quieren"]),
          ("poder (o→ue)",["puedo","puedes","puede","podemos","podéis","pueden"])]
    pers=["yo","tú","él/ella","nosotros","vosotros","ellos"]
    x0,y0=Inches(1.2),Inches(1.7); cw=Inches(4.6)
    for ci,(title,ends) in enumerate(cols):
        x=x0+Inches(1.7)+ci*(cw)
        card(s,x,y0,cw-Inches(0.2),Inches(0.5),fill=G,line=None)
        text(s,x,y0,cw-Inches(0.2),Inches(0.5),[[(title,{"size":13,"bold":True,"color":WHITE,"font":DISPLAY})]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    for ri,pr in enumerate(pers):
        y=y0+Inches(0.6)+ri*Inches(0.55)
        text(s,Inches(1.2),y,Inches(1.6),Inches(0.5),[[(pr,{"size":12,"color":MUT})]],anchor=MSO_ANCHOR.MIDDLE)
        for ci,(title,ends) in enumerate(cols):
            x=x0+Inches(1.7)+ci*(cw)
            card(s,x,y,cw-Inches(0.2),Inches(0.5),fill=WHITE,line=LINE,lw=1.0,shadow=False)
            hl = (ri in (3,4))  # nosotros/vosotros = geen wissel
            rev=text(s,x,y,cw-Inches(0.2),Inches(0.5),[[(ends[ri],{"size":14,"bold":True,"color":(MUT if hl else F_VERB)})]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
            register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.6), Inches(12.3), Inches(0.75),
             [[("🔴 De klinker verandert NIET bij nosotros/vosotros ", {"bold":True,"color":RED}),
               ("(queremos, podemos). 🔴 Het tweede werkwoord blijft infinitief: ", {"color":GD}),
               ("Quiero IR", {"bold":True,"color":GD}), (" (niet «quiero voy»).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR querer/poder. Onthul rij per rij; laat de klas de vorm voorspellen. De grijze rijen (nosotros/vosotros) = geen "
             "stamwissel. Tweede werkwoord = infinitief. Volledige vervoeging = aparte Conjugador-tool. Online: «¿querer o poder?» + verbo-cloze.")

# ============================================================ DIA 12 · SPEAKING — propón un plan
def s12_speaking():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · SPEAKING · INTERACCIÓN", "¡Quedamos!", "Stel een plan voor met de zinnen. Steun bouwt af: kaarten → beginwoorden → uit het hoofd.", num=3)
    avatar(s, "tu", Inches(11.4), Inches(1.7), Inches(1.3))
    labels=["Proponer","Aceptar","Preguntar la hora","Confirmar","Alternativa","Cierre"]
    frames=["¿Quieres ir a…?","¡Vale! / De acuerdo","¿A qué hora quedamos?","Quedamos a las…","¿Por qué no…? / ¿Podemos…?","¡Hasta el sábado!"]
    x0,y0=Inches(0.5),Inches(1.8); cw=Inches(3.4); rh=Inches(0.8)
    for i,(lab,fr) in enumerate(zip(labels,frames)):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=G,lw=1.2,shadow=False)
        text(s,x+Inches(0.15),y+Inches(0.05),cw-Inches(0.3),Inches(0.32),[[(lab,{"size":10,"color":MUT})]])
        text(s,x+Inches(0.15),y+Inches(0.36),cw-Inches(0.3),Inches(0.4),[[(fr,{"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    text(s, Inches(0.5), Inches(5.0), Inches(10.5), Inches(0.9),
         [[("Ronda 1: ", {"size":12,"bold":True,"color":GD}), ("met de kaarten. ", {"size":12,"color":INK}),
           ("Ronda 2: ", {"size":12,"bold":True,"color":GD}), ("alleen beginwoorden. ", {"size":12,"color":INK}),
           ("Ronda 3: ", {"size":12,"bold":True,"color":GD}), ("uit het hoofd, ander plan. ", {"size":12,"color":INK}),
           ("Ronda 4: ", {"size":12,"bold":True,"color":GD}), ("grábate en de digitale pagina.", {"size":12,"color":INK})]])
    chip(s, Inches(0.5), Inches(4.65), "🎙️ Grábate online · «Mensaje de voz: propón un plan»", fill=GT, tcolor=GD, size=11)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.6), Inches(12.3), Inches(0.65),
             [[("Modelo: ", {"bold":True,"color":GD}), ("«¿Quieres ir a la playa el sábado? —¡Vale! ¿A qué hora quedamos? —¿Podemos a las once? —De acuerdo.»", {"color":GD})]],
             trigger=btn, title_doc="MODELO · docent")
    foot(s)
    notes(s, "TEACHER · SPEAKING (interactie). Automatiseer proponer→aceptar→quedar in rondes met afbouwende steun. "
             "Online: recorder (opname + zelfevaluatie). Print blijft bruikbaar zonder opname.")

# ============================================================ DIA 13 · WRITING — mi perfil de gustos
def s13_writing():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "WRITING · PRODUCCIÓN", "Mi perfil de gustos", "Schrijf 4–5 zinnen over jouw smaak. Klik → een modeltekst verschijnt.", num=1)
    card(s, Inches(0.5), Inches(1.7), Inches(6.0), Inches(3.9), fill=WHITE, line=LINE, lw=1.2)
    text(s, Inches(0.7), Inches(1.85), Inches(5.6), Inches(0.4), [[("✍️ Escribe aquí:", {"size":12,"bold":True,"color":GD})]])
    for i in range(6):
        rect(s, Inches(0.7), Inches(2.4)+i*Inches(0.5), Inches(5.6), Inches(0.01), fill=LINE)
    chk=[("me gusta(n) …",),("me encanta(n) …",),("no me gusta …",),("porque … (una razón)",),("un conector: y también / pero",),("un plan: quiero / quedar",)]
    x=Inches(6.9); y=Inches(1.7)
    text(s,x,y,Inches(6),Inches(0.4),[[("Checklist:",{"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    for i,(c,) in enumerate(chk):
        text(s,x,y+Inches(0.5)+i*Inches(0.45),Inches(6),Inches(0.4),[[("☐  "+c,{"size":13,"color":INK})]])
    rev=card(s, x, Inches(4.35), Inches(6.0), Inches(1.25), fill=GT, line=G, lw=1.2)
    text(s, x+Inches(0.15), Inches(4.4), Inches(5.7), Inches(1.2),
         [[("Modelo: ", {"size":12,"bold":True,"color":GD}),
           ("«Me encanta la música, sobre todo el pop, y me gustan los deportes. No me gusta el fútbol porque es aburrido. El sábado quiero ir a la playa.»",{"size":12,"italic":True,"color":INK})]], line=1.15)
    register_reveal(s, rev)
    noodroute(s); foot(s)
    notes(s, "TEACHER · WRITING (lezen→schrijven). Checklist = zichtbare steun; onthul het model pas na het schrijven (retrieval). "
             "Nakijkfocus: gusta/gustan, OI-woord, porque. Dit voedt de Tarea «Mi playlist».")

# ============================================================ DIA 14 · VOCAB — ocio & música (reveal)
def s14_ocio_musica():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · VOCABULARIO · OCIO", "Deportes, música y sentimientos", "Klik een woord → de vertaling verschijnt. Bouw je woordnetwerk.", num=1)
    data=[("nadar","zwemmen"),("bailar","dansen"),("jugar","spelen"),("leer","lezen"),
          ("la canción","het liedje"),("la película","de film"),("la serie","de serie"),("el/la cantante","de zanger(es)"),
          ("divertido","leuk/grappig"),("aburrido","saai"),("genial","geweldig"),("relajante","ontspannend")]
    x0,y0=Inches(0.5),Inches(1.7); cw=Inches(3.0); rh=Inches(0.7)
    for i,(es,nl) in enumerate(data):
        c=i%4; r=i//4; x=x0+c*(cw+Inches(0.1)); y=y0+r*(rh+Inches(0.14))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.12),y,Inches(1.6),rh,[[(es,{"size":12,"bold":True,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(1.7),y,cw-Inches(1.8),rh,[[("→ "+nl,{"size":11.5,"color":G})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.9),
             [[("Combineer met gustar: ", {"bold":True,"color":GD}),
               ("Me gusta nadar. · Me gustan las series. · Me encanta la canción porque es divertida.", {"color":GD})],
              [("Adjetivos concuerdan: divertidO / divertidA, aburridO / aburridA. genial e interesante = invariable.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCAB ocio. Klik onthult; koppel elk woord aan een gustar-zin. Volledige set + audio op de digitale pagina "
             "(flip cards + memoria). Adjectief-concordantie kort tonen.")

# ============================================================ DIA 15 · TALLER — porque + conectores
def s15_taller():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "TALLER DE LENGUA", "¿por qué? / porque + conectores", "Klik een item → correcte vorm. Gereedschap om je mening te geven.", num=1)
    text(s, Inches(0.5), Inches(1.5), Inches(6), Inches(0.35), [[("A · ¿por qué? o porque", {"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
    fixes=[("¿___ te gusta el mar?","por qué"),("Me gusta ___ es relajante","porque"),("¿___ no quieres ir?","por qué"),("No puedo ___ trabajo","porque")]
    y=Inches(1.95)
    for q,a in fixes:
        card(s,Inches(0.5),y,Inches(6.0),Inches(0.6),fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,Inches(0.62),y,Inches(3.6),Inches(0.6),[[(q,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,Inches(4.3),y,Inches(2.0),Inches(0.6),[[("→ "+a,{"size":12,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y=y+Inches(0.72)
    text(s, Inches(6.9), Inches(1.5), Inches(6), Inches(0.35), [[("B · conectores: y también · pero · además · sobre todo", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    conn=[("Me gusta el cine, ___ no las series","pero","tegenstelling"),("Me gusta nadar ___ bailar","y también","toevoegen"),("Es divertido; ___, es barato","además","bovendien"),("Me gusta la música, ___ el pop","sobre todo","vooral")]
    y=Inches(1.95)
    for q,a,gl in conn:
        card(s,Inches(6.9),y,Inches(5.9),Inches(0.6),fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,Inches(7.02),y,Inches(3.2),Inches(0.6),[[(q,{"size":11.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,Inches(10.3),y,Inches(2.4),Inches(0.6),[[(a+" ",{"size":12,"bold":True,"color":GD}),("· "+gl,{"size":9,"italic":True,"color":MUT})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y=y+Inches(0.72)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.85),
             [[("🔴 A: ", {"bold":True,"color":RED}), ("¿por qué? = waarom (twee woorden + tilde) · porque = want/omdat (één woord).", {"color":GD})],
              [("B: ", {"bold":True,"color":GD}), ("y también (+) · pero (tegenstelling) · además (bovendien) · sobre todo (vooral).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · TALLER. ¿por qué?/porque = grote valstrik. Conectoren maken de mening rijker → meteen toepassen in het perfil/de Tarea. "
             "Online: «¿por qué o porque?» + «conectores de opinión».")

# ============================================================ DIA 16 · CULTURE — Rosalía & ocio
def s16_cultura():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "CULTURA · PARADA 4", "Rosalía y el ocio joven", "Klik een kaart → het weetje verschijnt. La música une al mundo hispano.", num=1)
    cards=[("🎵 Rosalía","Cantante de Barcelona. Mezcla flamenco con pop y reguetón. Álbumes: El mal querer, Motomami. Canta en español.","Un puente entre tradición y las listas de hoy."),
           ("🏖️ El ocio joven","Salir con amigos, escuchar música, ver series, hacer deporte, ir a la playa. Muziek & samen zijn staan centraal.","En València: las Fallas, la paella y la horchata."),
           ("🌍 El español suena","Rosalía, Bad Bunny, Shakira, Karol G… en el top mundial. El español es de los idiomas más escuchados.","Muziek = de leukste manier om te oefenen.")]
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
             [[("Actividad: ", {"bold":True,"color":GD}), ("schrijf 3 zinnen over jouw favoriete artiest met «me gusta/encanta … porque …».", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · CULTURE (identiteit in diversiteit, LPD 5). Onthul per kaart. Speel eventueel een fragment (rechtenvrij/eigen keuze). "
             "Verbind met de klas: welke Spaanstalige artiesten kennen jullie? Bruggetje naar de Tarea Mi playlist.")

# ============================================================ DIA 17 · QUIZ — haz la pregunta
def s17_quiz_pregunta():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · QUIZ · INTERACCIÓN", "Haz la pregunta", "Bij dit antwoord — welke vraag? Klik → de vraag verschijnt.", num=1)
    items=[("Me gusta nadar.","¿Qué te gusta hacer?"),("No, no me gusta.","¿Te gusta el fútbol?"),
           ("Porque canta muy bien.","¿Por qué te gusta Rosalía?"),("¡Vale! ¿A qué hora?","¿Quieres ir a la playa?"),
           ("A las once.","¿A qué hora quedamos?"),("Sí, puedo por la tarde.","¿Puedes quedar el sábado?")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(6.05); rh=Inches(0.78)
    for i,(ans,q) in enumerate(items):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(2.6),rh,[[(ans,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(2.8),y,cw-Inches(2.95),rh,[[(q,{"size":12,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Vragen over gustos & planes: ", {"bold":True,"color":GD}),
               ("¿Qué te gusta…? · ¿Te gusta…? · ¿Por qué…? · ¿Quieres…? · ¿A qué hora…?", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ interactie. Klas formuleert de vraag vóór de klik. Daarna klassikale enquête: gustos vragen en rapporteren "
             "(A Tom le gusta… / no le gusta…).")

# ============================================================ DIA 18 · FINAL_MISSION — Mi playlist
def s18_tarea():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(1.35), fill=GD)
    text(s, Inches(0.5), Inches(0.18), Inches(9), Inches(1.0),
         [[("🎧 Tarea final · Mi playlist", {"size":30,"bold":True,"color":WHITE,"font":DISPLAY})],
          [("Maak je persoonlijke playlist: canciones + por qué + qué sientes, en presenteer ze.", {"size":13,"italic":True,"color":GT})]])
    avatar(s, "mochila", Inches(11.6), Inches(0.2), Inches(1.0))
    pasos=[("1","Elige 4 canciones/artistas","que te gustan o te encantan"),
           ("2","Rellena la playlist","canción · por qué (porque…) · qué sientes"),
           ("3","Escribe tu presentación","5–6 frases: gustar/encantar + porque + conectores"),
           ("4","Presenta a la clase","of neem audio op (digitale pagina)"),
           ("5","Pregunta a un compañero","por sus gustos y reacciona (también/tampoco/sí/no)")]
    y=Inches(1.7)
    for n,es,nl in pasos:
        b=rect(s,Inches(0.5),y,Inches(0.5),Inches(0.5),fill=G,round=True,radius=0.5)
        tf=b.text_frame;tf.vertical_anchor=MSO_ANCHOR.MIDDLE;p=tf.paragraphs[0];p.alignment=PP_ALIGN.CENTER
        rr=p.add_run();rr.text=n;rr.font.size=Pt(15);rr.font.bold=True;rr.font.name=DISPLAY;rr.font.color.rgb=WHITE
        text(s,Inches(1.2),y,Inches(4.0),Inches(0.55),[[(es,{"size":14,"bold":True,"color":GD,"font":DISPLAY})]],anchor=MSO_ANCHOR.MIDDLE)
        text(s,Inches(5.3),y,Inches(7.4),Inches(0.55),[[(nl,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        y=y+Inches(0.62)
    text(s, Inches(0.5), Inches(5.0), Inches(12), Inches(0.35), [[("Rúbrica · ¿lo logré?", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    crit=["4 items + una razón","gusta/gustan + encanta(n)","porque + conectores","presentar + reaccionar"]
    x=Inches(0.5)
    for c in crit:
        chip(s,x,Inches(5.45),"☐ "+c,fill=GT,tcolor=GD,size=11,w=Inches(3.0)); x=x+Inches(3.1)
    text(s, Inches(0.5), Inches(6.05), Inches(12), Inches(0.4),
         [[("🎯 ", {"size":12}), ("Afzender jij · ontvanger de klas/Lucía · doel je smaak delen & motiveren · situatie muziekavond in València · resultaat: playlist + presentatie.", {"size":11.5,"italic":True,"color":MUT})]])
    foot(s)
    notes(s, "TEACHER · FINAL_MISSION (communicatieve eindtaak). Afzender/ontvanger/doel/situatie/resultaat expliciet. Beoordeel met de rúbrica; "
             "opname + zelfevaluatie op de digitale pagina. Voeg een mini-encuesta + grafiekje toe (gustos van de klas).")

# ============================================================ DIA 19 · QUIZ — la mezcla
def s19_mezcla():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "QUIZ · LA MEZCLA", "Ophaal door elkaar", "Gemengde ophaal van de hele unit. Klik een vraag → het antwoord. (retrieval)", num=1)
    items=[("Me ___ los deportes.","gustan"),("a mí (persoon) → pronombre","me"),("querer, yo","quiero"),
           ("poder, nosotros","podemos"),("«Me gusta.» akkoord","a mí también"),("«No me gusta.» akkoord","a mí tampoco"),
           ("waarom (vraag)","¿por qué?"),("Quiero ___ a la playa.","ir (infinitivo)")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(6.05); rh=Inches(0.62)
    for i,(q,a) in enumerate(items):
        c=i//4; r=i%4; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.16))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(3.2),rh,[[(q,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(3.35),y,cw-Inches(3.5),rh,[[("→ "+a,{"size":12,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.05), Inches(12.3), Inches(0.55),
             [[("Alles komt terug: ", {"bold":True,"color":GD}), ("gustar (concord) · pronombres OI · también/tampoco · querer/poder + inf. · porque.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ mezcla (retrieval vóór herlezen). Zonder waarschuwing door elkaar. Exit-ticket. Zwakke punten → terug via menu.")

# ============================================================ DIA 20 · FEEDBACK/REPASO
def s20_repaso():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "REPASO · LO ESENCIAL", "Lo esencial de un vistazo", "De volledige herhaling (24 spellen, drills) staat online. Hier: de kern + semáforo.", num=1)
    ess=["Gustar (al revés): me/te/le/nos/os/les + gusta (1/inf.) · gustan (mv.). Idem encanta(n).",
         "Reacciones: + akkoord también · + oneens a mí no · – akkoord tampoco · – oneens a mí sí.",
         "Proponer: querer (e→ie) / poder (o→ue) + infinitivo · quedar (afspreken).",
         "Opinar: ¿por qué? → porque + conectoren (y también · pero · además · sobre todo).",
         "🔴 Trampas: gustar = «bevalt mij» · gustaN bij mv. · tampoco = ook niet · nosotros/vosotros zonder stamwissel."]
    card(s, Inches(0.5), Inches(1.6), Inches(12.3), Inches(2.5), fill=CREMA, line=None)
    y=Inches(1.8)
    for e in ess:
        text(s, Inches(0.8), y, Inches(11.8), Inches(0.45), [[("• ", {"size":13,"bold":True,"color":GD}),(e,{"size":12,"color":INK})]])
        y=y+Inches(0.46)
    text(s, Inches(0.5), Inches(4.3), Inches(12), Inches(0.35), [[("Semáforo — ¿cómo lo llevas?", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    can=["zeggen wat ik leuk vind","OI-woorden (me/te/le…)","akkoord/oneens","plan voorstellen","mening motiveren"]
    y=Inches(4.75)
    for c in can:
        text(s,Inches(0.8),y,Inches(7.0),Inches(0.4),[[(c,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        for j,(em,col) in enumerate([("🔴",RED),("🟠",AMBER),("🟢",G)]):
            chip(s,Inches(8.0)+j*Inches(1.5),y+Inches(0.03),em+" ",fill=WHITE,tcolor=col,size=12,w=Inches(1.3))
        y=y+Inches(0.42)
    foot(s)
    notes(s, "TEACHER · FEEDBACK/REPASO. Semáforo = zelfevaluatie. Repaso-drills online (24 spellen). Bruggetje: U5 «¡Ñam!» (CDMX) — "
             "cruzamos el charco a México: comida en un restaurante.")

# ============================================================ DIA 21 · TEACHER_NOTES
def s21_teacher():
    s = slide(); bg(s, GD)
    text(s, Inches(0.6), Inches(0.4), Inches(12), Inches(0.8), [[("TEACHER_NOTES · U4 «Me gusta»", {"size":26,"bold":True,"color":WHITE,"font":DISPLAY})]])
    blocks=[("Timing (50 min)","Menu 2' · gustar + pronombres 12' · también/tampoco 8' · querer/poder + quedar 10' · lectura/escucha 8' · cultura 4' · Tarea-briefing 6'."),
            ("Kernvalstrikken","gustar al revés (het ding = onderwerp) · gustaN bij meervoud · tampoco = ook niet · «a mí», niet «yo» · querer/poder zónder wissel bij nosotros/vosotros · 2e ww = infinitief · ¿por qué? ≠ porque."),
            ("Differentiatie (zij-instromers)","Alles start vanaf nul. Sterker: encantar + conectoren + eigen playlist toelichten. Zwakker: gusta/gustan-kaart en OI-tabel langer open."),
            ("Digitaal","24 spellen + flip cards + klikbare kaart + recorder (Hablar) + Lectura op de página digital. QR's in het boek → juiste anker. Conjugador = aparte tool."),
            ("Evaluatie","Tarea «Mi playlist» met rúbrica (4 criteria). LPD 3·4·7·8 + 5 (cultura) + 1·2 (receptief).")]
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
    s01_title(); s02_menu(); s03_vocab(); s04_gustar(); s05_gusta_gustan(); s06_oi(); s07_reacciones()
    s08_quiz_reaccion(); s09_reading(); s10_listening(); s11_querer_poder(); s12_speaking(); s13_writing()
    s14_ocio_musica(); s15_taller(); s16_cultura(); s17_quiz_pregunta(); s18_tarea(); s19_mezcla(); s20_repaso()
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
