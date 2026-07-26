#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_u1_docente.py — Interactieve PowerPoint C5 · Unidad 1 «¿Quién eres?» (parada Madrid)
=========================================================================================
Zelfde engine/pijplijn als de golden sample U0 (gen_u0_docente.py wordt geïmporteerd:
alle low-level helpers, on-click <p:timing>-animaties, hyperlink-navigatie, .ppsx-conversie).
Enkel de SLIDES (content) zijn U1-specifiek. Twee decks:
  · C5_U1_docente.pptx — vrije navigatie, oplossingen bij klik + didactiek in spreker-notities.
  · C5_U1_alumno.ppsx  — gewone diavoorstelling, antwoorden verschijnen bij klik (geen kiosk).
Huisstijl groen (C5). Spaans-eerst + NL-steun. ≥20 dia's.
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
OUT_DOCENTE = os.path.join(HERE, "C5_U1_docente.pptx")
OUT_ALUMNO_PPTX = os.path.join(HERE, "C5_U1_alumno.pptx")
OUT_ALUMNO = os.path.join(HERE, "C5_U1_alumno.ppsx")
TAB = "U1 · ¿QUIÉN ERES?"

def foot(s): footer(s, tab=TAB, page=pg())

# ============================================================ DIA 1 · TITLE
def s01_title():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(4.7), fill=G)
    rect(s, 0, Inches(4.7), EMU_W, Inches(0.09), fill=GD)
    text(s, Inches(0.6), Inches(0.35), Inches(3.4), Inches(3.6),
         [[("1", {"size": 260, "bold": True, "color": RGBColor(0x2E,0xB0,0x85), "font": DISPLAY})]],
         anchor=MSO_ANCHOR.MIDDLE)
    chip(s, Inches(4.35), Inches(0.85), "LA RUTA · PARADA 1 · MADRID 🇪🇸", fill=WHITE, tcolor=GD, size=12)
    text(s, Inches(4.3), Inches(1.35), Inches(8.6), Inches(1.5),
         [[("¿Quién eres?", {"size": 72, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(4.35), Inches(2.7), Inches(8.4), Inches(0.6),
         [[("Presentarse: nombre, edad, país, idiomas — en Madrid, con Lucía.", {"size": 16, "italic": True, "color": GT})]])
    text(s, Inches(4.35), Inches(3.35), Inches(8.4), Inches(0.9),
         [[("¿Cómo te llamas… y de dónde eres?", {"size": 26, "bold": True, "color": WHITE, "font": DISPLAY})],
          [("Hoe heet je… en waar kom je vandaan?", {"size": 13, "italic": True, "color": GT})]])
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
    notes(s, "TEACHER · TITLE. Parada 1 = Madrid, met gastvrouw Lucía. Doel van de unit: zich voorstellen "
             "(nombre/edad/país/idiomas) + iemand ernaar vragen. Kernvalstrik meteen benoemen: leeftijd = TENER "
             "(Tengo 15 años), niet SER. Instructietaal Spaans-eerst met NL-steun. Docentdeck = vrije navigatie + "
             "oplossing in notities; leerlingdeck (.ppsx) = elke klik onthult het volgende antwoord (geen kiosk).")

# ============================================================ DIA 2 · LESSON_MENU
def s02_menu():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "MENÚ DE LA LECCIÓN", "El mapa de la Unidad 1",
               "Kies je route — klik een tegel. Alles oefent naar de Tarea «Mi pasaporte» toe.", num=1)
    tiles = [
        ("§1", "Tus datos personales", "nombre · edad · país · idiomas", G, 3),
        ("§2", "El verbo SER", "soy · eres · es · presentarse", G, 6),
        ("§3", "Presente regular", "-ar · -er · -ir · hablar/vivir", G, 7),
        ("§4", "Preguntar + el/la", "interrogativos · género · artículos", G, 11),
        ("★", "Cultura · Madrid", "los dos apellidos · tú/usted", GD, 16),
        ("✈", "Tarea · Mi pasaporte", "je paspoort + presentarte", GD, 18),
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
    notes(s, "TEACHER · LESSON_MENU. Elke tegel = hyperlink naar de sectie; op elke oefendia staat ⌂ Menú terug. "
             "Bij veel zij-instromers: begin gerust bij §1 (datos) — de kern van zich voorstellen. Richttijd 50 min.")

# ============================================================ DIA 3 · VOCABULARY — datos (ficha)
def s03_datos():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · VOCABULARIO", "Tus datos personales", "De ficha van Lucía — observa. Herken de woorden, dan gebruik je ze.", num=1)
    legend_func(s, Inches(9.7), Inches(0.55))
    rows = [("el nombre","Lucía","voornaam"),("el apellido","Ramírez García","achternaam ×2"),
            ("la edad","16 años","leeftijd"),("el país","España","land"),
            ("la nacionalidad","española","nationaliteit"),("la ciudad","Sevilla","stad"),
            ("los idiomas","español, inglés","talen"),("el correo","lucia@mail.com","e-mail")]
    x0,y0 = Inches(0.5), Inches(1.6); cw=Inches(6.1); rh=Inches(0.6)
    for i,(k,v,nl) in enumerate(rows):
        c = 0 if i<4 else 1; r = i%4
        x = x0 + c*(cw+Inches(0.15)); y = y0 + r*(rh+Inches(0.12))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x+Inches(0.15), y, Inches(2.4), rh, [[(k, {"size":13,"bold":True,"color":GD})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x+Inches(2.5), y, Inches(2.5), rh, [[(v, {"size":13,"color":INK})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x+Inches(4.7), y, Inches(1.3), rh, [[(nl, {"size":9,"italic":True,"color":MUT})]], anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(4.75), Inches(12.3), Inches(0.5),
         [[("Presentarse: ", {"size":13,"bold":True,"color":GD,"font":DISPLAY}),
           ("Me llamo", {"size":13,"bold":True,"color":F_VERB}), (" + naam · ",{"size":13,"color":INK}),
           ("Soy de", {"size":13,"bold":True,"color":F_VERB}), (" + land · ",{"size":13,"color":INK}),
           ("Tengo", {"size":13,"bold":True,"color":F_VERB}), (" + ",{"size":13,"color":INK}),
           ("… años", {"size":13,"bold":True,"color":F_TIME}), (" · ",{"size":13,"color":INK}),
           ("Vivo en", {"size":13,"bold":True,"color":F_VERB}), (" + stad",{"size":13,"color":INK})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.35), Inches(12.3), Inches(0.95),
             [[("🔴 Leeftijd = TENER: ", {"bold":True,"color":RED}), ("Tengo 15 años", {"bold":True,"color":GD}),
               (" (niet ", {"color":GD}), ("soy 15", {"color":RED}), ("). ", {"color":GD}),
               ("🔴 Nationaliteit met kleine letter: ", {"bold":True,"color":RED}), ("belga, español.", {"color":GD})],
              [("el nombre = voornaam · el apellido = achternaam (in het Spaans twee: padre + madre → Cultura).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCABULARY. Toon eerst de ficha, laat leerlingen woorden raden zónder de NL-gloss (die staat klein). "
             "Kernframe presentarse meteen inoefenen. Valstrik tener/ser en mayúsculas benadrukken. Online: flip cards + Memoria de los datos.")

# ============================================================ DIA 4 · GRAMMAR — presentarse (color)
def s04_presentarse():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · GRAMÁTICA VISUAL", "Presentarse — las frases clave", "Kleur = taalfunctie. Beweeg van betekenis naar vorm.", num=1)
    legend_func(s, Inches(9.7), Inches(0.55))
    # gekleurde zin
    seg = [("Yo ", F_SUBJ),("me llamo ", F_VERB),("Leo, ", INK),("soy ", F_VERB),("de Bélgica ", F_PLAC),
           ("y ", INK),("tengo ", F_VERB),("15 años.", F_TIME)]
    runs=[[(t,{"size":26,"bold":True,"color":c,"font":DISPLAY}) for t,c in seg]]
    card(s, Inches(0.5), Inches(1.7), Inches(12.3), Inches(1.2), fill=GT, line=None)
    text(s, Inches(0.8), Inches(1.7), Inches(11.7), Inches(1.2), runs, anchor=MSO_ANCHOR.MIDDLE)
    # frame-tabel
    text(s, Inches(0.5), Inches(3.15), Inches(12), Inches(0.4), [[("El marco — bouw je eigen voorstelling:", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    frame=[("Me llamo","+ (voor)naam"),("Soy de","+ land / stad"),("Soy","+ nationaliteit"),
           ("Tengo","+ getal + años"),("Vivo en","+ stad"),("Hablo","+ taal/talen")]
    x0,y0=Inches(0.5),Inches(3.6); cw=Inches(4.0); rh=Inches(0.62)
    for i,(a,b) in enumerate(frame):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.12))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(1.6),rh,[[(a,{"size":13,"bold":True,"color":F_VERB})]],anchor=MSO_ANCHOR.MIDDLE)
        text(s,x+Inches(1.75),y,cw-Inches(1.9),rh,[[(b,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.7), Inches(12.3), Inches(0.7),
             [[("Modelo: ", {"bold":True,"color":GD}), ("«Hola, me llamo Leo, soy de Bélgica y tengo 15 años. Vivo en Gante y hablo neerlandés y español.»", {"color":GD})]],
             trigger=btn, title_doc="MODELO · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR (color-coding = functionele taalsemantiek). Elke leerling bouwt zijn eigen voorstelling met het marco. "
             "Steun bouwt af: marco zichtbaar → alleen beginwoorden → uit het hoofd. Kleur is nooit de enige drager (ook label/vorm).")

# ============================================================ DIA 5 · QUIZ — ser o tener
def s05_ser_tener():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · QUIZ", "¿SER o TENER?", "Welk werkwoord past? Klik een zin → het juiste werkwoord verschijnt. Let op de leeftijd!", num=1)
    items=[("Yo ___ de Bélgica.","soy","ser"),("Yo ___ 15 años.","tengo","tener"),
           ("Ella ___ española.","es","ser"),("¿Cuántos años ___?","tienes","tener"),
           ("Nosotros ___ estudiantes.","somos","ser"),("Mi hermano ___ 12 años.","tiene","tener")]
    x0,y0=Inches(0.5),Inches(1.7); cw=Inches(6.05); rh=Inches(0.7)
    for i,(q,ans,cat) in enumerate(items):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        qshp=text(s,x+Inches(0.15),y,Inches(3.9),rh,[[(q,{"size":13,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(4.1),y,cw-Inches(4.2),rh,
                 [[(ans+" ",{"size":14,"bold":True,"color":GD}),("· "+cat,{"size":10,"italic":True,"color":(RED if cat=="tener" else G)})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.95),
             [[("SER = ", {"bold":True,"color":G}), ("identiteit, afkomst, nationaliteit, eigenschap", {"color":GD}),
               (" (soy/eres/es/somos/sois/son).", {"color":GD})],
              [("TENER = ", {"bold":True,"color":RED}), ("bezit én LEEFTIJD: ", {"color":GD}),
               ("Tengo 15 años", {"bold":True,"color":GD}), (" — nooit «soy 15».", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ (reveal per klik). Laat de klas eerst kiezen (hand/stem), klik dan het antwoord. "
             "Rode categorie = tener (leeftijd/bezit). De hardnekkigste NL-fout: «soy 15 años». Herhaal mondeling.")

# ============================================================ DIA 6 · GRAMMAR — SER (reveal)
def s06_ser():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · GRAMÁTICA", "El verbo SER (irregular)", "Denk de vorm, klik de kaart → de vorm verschijnt. Kortste én belangrijkste werkwoord.", num=2)
    R=[("yo","soy"),("tú","eres"),("él/ella/usted","es"),("nosotros/-as","somos"),("vosotros/-as","sois"),("ellos/-as/ustedes","son")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(3.95); ch=Inches(1.25)
    for i,(p,v) in enumerate(R):
        c=i%3; r=i//3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(ch+Inches(0.2))
        card(s,x,y,cw,ch,fill=WHITE,line=G,lw=1.4)
        text(s,x,y+Inches(0.12),cw,Inches(0.4),[[(p,{"size":13,"color":MUT})]],align=PP_ALIGN.CENTER)
        rev=text(s,x,y+Inches(0.5),cw,Inches(0.6),[[(v,{"size":26,"bold":True,"color":GD,"font":DISPLAY})]],align=PP_ALIGN.CENTER)
        register_reveal(s, rev)
    text(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.5),
         [[("🟡 Onderwerp mag weg — de vorm zegt al wie: ", {"size":12,"color":INK}),
           ("(Yo) soy Leo.", {"size":12,"bold":True,"color":GD}),
           ("   🟡 tú (leeftijdsgenoot) ↔ usted (beleefd, 3e pers.: usted es).", {"size":12,"color":INK})]])
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.75), Inches(12.3), Inches(0.65),
             [[("soy · eres · es · somos · sois · son. ", {"bold":True,"color":GD}),
               ("Gebruik: identidad (soy Leo), origen (soy de Bélgica), nacionalidad (soy belga), cualidad (es simpática).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR SER (reveal). Coro: klas zegt de vorm vóór je klikt. Wijs op yo→soy (onregelmatig). "
             "tú vs usted kort aanraken (uitwerking in Cultura). Online: «El verbo SER» + «Presente Tetris».")

# ============================================================ DIA 7 · GRAMMAR — presente regular
def s07_presente():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · GRAMÁTICA", "El presente regular", "Quita la terminación, añade la nueva. Klik een kolomkop → de uitgangen verschijnen.", num=3)
    cols=[("hablar (-ar)",["-o","-as","-a","-amos","-áis","-an"]),
          ("aprender (-er)",["-o","-es","-e","-emos","-éis","-en"]),
          ("vivir (-ir)",["-o","-es","-e","-imos","-ís","-en"])]
    pers=["yo","tú","él/ella","nosotros","vosotros","ellos"]
    x0,y0=Inches(0.7),Inches(1.7); cw=Inches(3.9);
    text(s,Inches(0.7),y0,Inches(1.6),Inches(0.4),[[("",{"size":10})]])
    for ci,(title,ends) in enumerate(cols):
        x=x0+Inches(1.7)+ci*(cw)
        hdr=card(s,x,y0,cw-Inches(0.2),Inches(0.5),fill=G,line=None)
        text(s,x,y0,cw-Inches(0.2),Inches(0.5),[[(title,{"size":13,"bold":True,"color":WHITE,"font":DISPLAY})]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    for ri,pr in enumerate(pers):
        y=y0+Inches(0.6)+ri*Inches(0.6)
        text(s,Inches(0.7),y,Inches(1.6),Inches(0.55),[[(pr,{"size":12,"color":MUT})]],anchor=MSO_ANCHOR.MIDDLE)
        for ci,(title,ends) in enumerate(cols):
            x=x0+Inches(1.7)+ci*(cw)
            stem=title.split()[0][:-2]
            card(s,x,y,cw-Inches(0.2),Inches(0.55),fill=WHITE,line=LINE,lw=1.0,shadow=False)
            rev=text(s,x,y,cw-Inches(0.2),Inches(0.55),[[(stem,{"size":13,"color":INK}),(ends[ri],{"size":13,"bold":True,"color":F_VERB})]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
            register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(6.0), Inches(12.3), Inches(0.55),
             [[("-er en -ir zijn bijna gelijk ", {"bold":True,"color":GD}),
               ("(alleen nosotros/vosotros verschillen). De yo-vorm eindigt altijd op -o.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR presente. Onthul rij per rij; laat de klas de uitgang voorspellen. Benadruk: één patroon, "
             "drie families; -er/-ir alleen bij nosotros/vosotros anders. Werkwoordsvervoeging verder = aparte Conjugador-tool, niet hier. "
             "Inoefenen: online cloze-spel «Completa el verbo» (invullen van de juiste vorm) + de cloze-oefening in de cursus (§3.2).")

# ============================================================ DIA 8 · QUIZ — el/la + conjuga
def s08_quiz_ella():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · QUIZ", "¿el o la? — género", "Klik een woord → het juiste lidwoord verschijnt. Let op de valstrikken.", num=4)
    items=[("nombre","el"),("ciudad","la"),("país","el"),("dirección","la"),("idioma","el (🔴)"),("edad","la"),
           ("correo","el"),("nacionalidad","la"),("día","el (🔴)"),("firma","la"),("apellido","el"),("mano","la (🔴)")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(3.0); rh=Inches(0.75)
    for i,(w,art) in enumerate(items):
        c=i%4; r=i//4; x=x0+c*(cw+Inches(0.1)); y=y0+r*(rh+Inches(0.15))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(1.7),rh,[[(w,{"size":13,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(1.8),y,cw-Inches(1.9),rh,[[(art,{"size":15,"bold":True,"color":GD,"font":DISPLAY})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.9),
             [[("🔴 Valstrikken: ", {"bold":True,"color":RED}),
               ("el idioma, el día, el mapa, el problema", {"bold":True,"color":GD}),
               (" (op -a, tóch mannelijk!) · ", {"color":GD}), ("la mano", {"bold":True,"color":GD}), (" (op -o, tóch vrouwelijk).", {"color":GD})],
              [("Leer elk substantief mét lidwoord — dan ken je meteen het geslacht. Meervoud: los / las.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ género. Onthul per klik. De -a/-o-regel klopt meestal, maar de valstrikken (idioma/día/mapa; mano) "
             "moeten los geleerd. Online: «¿el o la?» (generator, nagerekend).")

# ============================================================ DIA 9 · READING — la ficha de Lucía
def s09_reading():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · LEER · COMPRENSIÓN", "La ficha de Lucía", "Lees en beantwoord. Klik een vraag → het antwoord verschijnt.", num=1)
    card(s, Inches(0.5), Inches(1.65), Inches(5.6), Inches(3.9), fill=GT, line=G, lw=1.4)
    avatar(s, "lucia", Inches(0.85), Inches(1.95), Inches(1.1))
    text(s, Inches(2.1), Inches(2.0), Inches(3.8), Inches(1.0),
         [[("«¡Hola! Me llamo Lucía Ramírez García. Soy de Sevilla, en España, y soy española. Tengo 16 años. "
            "Hablo español e inglés. Mi correo es lucia@mail.com.»",{"size":13,"italic":True,"color":INK})]], line=1.2)
    qa=[("¿Cómo se llama?","Lucía Ramírez García"),("¿De dónde es?","De Sevilla (España)"),
        ("¿Cuántos años tiene?","16 años"),("¿Qué idiomas habla?","Español e inglés")]
    x=Inches(6.4); y=Inches(1.7)
    for q,a in qa:
        card(s,x,y,Inches(6.4),Inches(0.85),fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y+Inches(0.06),Inches(6.1),Inches(0.4),[[(q,{"size":12.5,"bold":True,"color":GD})]])
        rev=text(s,x+Inches(0.15),y+Inches(0.44),Inches(6.1),Inches(0.35),[[("→ "+a,{"size":12,"color":INK})]])
        register_reveal(s, rev)
        y=y+Inches(0.98)
    btn=noodroute(s)
    exercise_solucion(s, Inches(6.4), Inches(5.65), Inches(6.4), Inches(0.6),
             [[("🔴 «e» i.p.v. «y» vóór i-/hi-: ", {"bold":True,"color":RED}), ("español e inglés", {"bold":True,"color":GD}), (".", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · READING (lezen→spreken-keten). Eerst globaal (waarover?), dan detail. Onthul de antwoorden pas na de klas. "
             "Daarna: leerlingen maken hun EIGEN ficha (transfer → Tarea). Let op «e» vóór inglés.")

# ============================================================ DIA 10 · LISTENING — escucha el país
def s10_listening():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · ESCUCHAR", "Escucha y anota el país", "Vier personen stellen zich voor. Klik een naam → land + nationaliteit verschijnen. (audio op de digitale pagina)", num=1)
    people=[("Leo","Bélgica","belga"),("Frida","México","mexicana"),("Mateo","Argentina","argentino"),("Sara","los Países Bajos","neerlandesa")]
    x0,y0=Inches(0.7),Inches(1.9); cw=Inches(2.95); ch=Inches(2.4)
    for i,(nm,pais,nac) in enumerate(people):
        x=x0+i*(cw+Inches(0.1))
        card(s,x,y0,cw,ch,fill=WHITE,line=LINE,lw=1.2)
        rect(s,x,y0,cw,Inches(0.5),fill=GT)
        text(s,x,y0,cw,Inches(0.5),[[("🔊  "+nm,{"size":14,"bold":True,"color":GD,"font":DISPLAY})]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        text(s,x+Inches(0.15),y0+Inches(0.65),cw-Inches(0.3),Inches(0.4),[[("País:",{"size":12,"color":MUT})]])
        rev1=text(s,x+Inches(0.15),y0+Inches(1.0),cw-Inches(0.3),Inches(0.4),[[(pais,{"size":14,"bold":True,"color":INK})]])
        text(s,x+Inches(0.15),y0+Inches(1.5),cw-Inches(0.3),Inches(0.4),[[("Nacionalidad:",{"size":12,"color":MUT})]])
        rev2=text(s,x+Inches(0.15),y0+Inches(1.85),cw-Inches(0.3),Inches(0.4),[[(nac,{"size":14,"bold":True,"color":G})]])
        register_reveal(s, rev1); register_reveal(s, rev2)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.85),
             [[("Modelo-audio (docent leest of TTS): ", {"bold":True,"color":GD}),
               ("«Hola, me llamo Leo, soy de Bélgica, soy belga.» …", {"color":GD})],
              [("Nationaliteiten m./v.: mexicano/mexicana · argentino/argentina · neerlandés/neerlandesa. Kleine letter!", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · LISTENING (selectief). Lees elk profiel voor (of gebruik TTS op de digitale pagina). Klas noteert país; "
             "onthul per klik. Koppel nationaliteit (m./v.) aan het land. Daarna spreken: leerling stelt een personage voor in 3e persoon.")

# ============================================================ DIA 11 · GRAMMAR — interrogativos
def s11_interrog():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · GRAMÁTICA", "Preguntar — palabras interrogativas", "Klik een vraag → wát ze vraagt + een modelantwoord. Vraagwoorden dragen een tilde.", num=4)
    items=[("¿Cómo te llamas?","de naam","Me llamo Leo."),("¿De dónde eres?","de afkomst","Soy de Bélgica."),
           ("¿Dónde vives?","de woonplaats","Vivo en Gante."),("¿Cuántos años tienes?","de leeftijd","Tengo 15 años."),
           ("¿Cuál es tu correo?","een gegeven","Es leo@mail.com."),("¿Qué idiomas hablas?","info (open)","Hablo dos idiomas.")]
    x0,y0=Inches(0.5),Inches(1.7); cw=Inches(6.05); rh=Inches(0.72)
    for i,(q,fn,ans) in enumerate(items):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.16))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(2.9),rh,[[(q,{"size":12.5,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(3.05),y,cw-Inches(3.2),rh,[[(fn+" → ",{"size":10.5,"italic":True,"color":MUT}),(ans,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.9),
             [[("🔴 ¿Cuál? vs ¿Qué? ", {"bold":True,"color":RED}),
               ("vóór ser + gegeven → ¿Cuál es tu nombre?", {"bold":True,"color":GD}), (" (niet ¿Qué es…?).", {"color":GD})],
              [("Vraagwoorden mét tilde: cómo, dónde, cuál, qué, quién, cuántos.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR interrogativos. Koppel elk vraagwoord aan het antwoordtype (spiegel). ¿Cuál? vs ¿Qué? is dé valstrik. "
             "Daarna: interactie — leerlingen interviewen elkaar (nombre/edad/ciudad). Online: «Palabras interrogativas», «Pregunta ↔ respuesta».")

# ============================================================ DIA 12 · SPEAKING — preséntate
def s12_speaking():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "SPEAKING · PRODUCCIÓN", "¡Preséntate!", "Bouw je voorstelling met de substitutietabel. Steun bouwt af: tabel → beginwoorden → uit het hoofd.", num=1)
    avatar(s, "tu", Inches(11.4), Inches(1.7), Inches(1.3))
    cols=[("Yo","me llamo…","soy de…","tengo… años","vivo en…","hablo…")]
    labels=["Persona","Nombre","Origen","Edad","Ciudad","Idiomas"]
    frames=["Yo / (tú)","Me llamo ___","Soy de ___","Tengo ___ años","Vivo en ___","Hablo ___"]
    x0,y0=Inches(0.5),Inches(1.8); cw=Inches(3.4); rh=Inches(0.8)
    for i,(lab,fr) in enumerate(zip(labels,frames)):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=G,lw=1.2,shadow=False)
        text(s,x+Inches(0.15),y+Inches(0.05),cw-Inches(0.3),Inches(0.32),[[(lab,{"size":10,"color":MUT})]])
        text(s,x+Inches(0.15),y+Inches(0.36),cw-Inches(0.3),Inches(0.4),[[(fr,{"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
    text(s, Inches(0.5), Inches(5.0), Inches(10.5), Inches(0.9),
         [[("Ronda 1: ", {"size":12,"bold":True,"color":GD}), ("met de tabel. ", {"size":12,"color":INK}),
           ("Ronda 2: ", {"size":12,"bold":True,"color":GD}), ("alleen beginwoorden. ", {"size":12,"color":INK}),
           ("Ronda 3: ", {"size":12,"bold":True,"color":GD}), ("uit het hoofd, tegen 3 klasgenoten. ", {"size":12,"color":INK}),
           ("Ronda 4: ", {"size":12,"bold":True,"color":GD}), ("grábate en de digitale pagina → terugluisteren.", {"size":12,"color":INK})]])
    chip(s, Inches(0.5), Inches(4.65), "🎙️ Grábate online · «Carrusel: preséntate»", fill=GT, tcolor=GD, size=11)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.6), Inches(12.3), Inches(0.65),
             [[("Modelo: ", {"bold":True,"color":GD}), ("«Hola, me llamo Sara, soy de Bélgica, tengo 14 años. Vivo en Amberes y hablo neerlandés e inglés.»", {"color":GD})]],
             trigger=btn, title_doc="MODELO · docent")
    foot(s)
    notes(s, "TEACHER · SPEAKING (substitutie → productie). Automatiseer de zelfvoorstelling in 3 rondes met afbouwende steun. "
             "Online: SubstitutionCarousel + recorder (opname + zelfevaluatie). Print blijft bruikbaar zonder opname.")

# ============================================================ DIA 13 · WRITING — mi mini-perfil
def s13_writing():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "WRITING · PRODUCCIÓN", "Mi mini-perfil", "Schrijf 4–5 zinnen over jezelf (echt of fictief). Klik → een modeltekst verschijnt.", num=1)
    card(s, Inches(0.5), Inches(1.7), Inches(6.0), Inches(3.9), fill=WHITE, line=LINE, lw=1.2)
    text(s, Inches(0.7), Inches(1.85), Inches(5.6), Inches(0.4), [[("✍️ Escribe aquí:", {"size":12,"bold":True,"color":GD})]])
    for i in range(6):
        rect(s, Inches(0.7), Inches(2.4)+i*Inches(0.5), Inches(5.6), Inches(0.01), fill=LINE)
    chk=[("nombre + apellido",),("edad (tener… años)",),("país + nacionalidad",),("ciudad (vivo en…)",),("idiomas (hablo…)",),("conector: y / porque",)]
    x=Inches(6.9); y=Inches(1.7)
    text(s,x,y,Inches(6),Inches(0.4),[[("Checklist:",{"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    for i,(c,) in enumerate(chk):
        text(s,x,y+Inches(0.5)+i*Inches(0.45),Inches(6),Inches(0.4),[[("☐  "+c,{"size":13,"color":INK})]])
    rev=card(s, x, Inches(4.35), Inches(6.0), Inches(1.25), fill=GT, line=G, lw=1.2)
    text(s, x+Inches(0.15), Inches(4.4), Inches(5.7), Inches(1.2),
         [[("Modelo: ", {"size":12,"bold":True,"color":GD}),
           ("«Me llamo Nina Quispe. Tengo 16 años y soy de Perú, soy peruana. Vivo en Cusco y hablo español e inglés porque me gusta viajar.»",{"size":12,"italic":True,"color":INK})]], line=1.15)
    register_reveal(s, rev)
    noodroute(s); foot(s)
    notes(s, "TEACHER · WRITING (lezen→schrijven-keten). Checklist = zichtbare steun; onthul het model pas na het schrijven "
             "(retrieval vóór herlezen). Nakijkfocus: ser/tener, mayúsculas, conector. Dit voedt rechtstreeks de Tarea «Mi pasaporte».")

# ============================================================ DIA 14 · VOCAB/CULTURE — países
def s14_paises():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · VOCABULARIO · MUNDO", "Países y nacionalidades", "De kaart groeit mee. Klik een land → de nacionalidad verschijnt. Land = hoofdletter, nationaliteit = klein.", num=1)
    data=[("🇧🇪 Bélgica","belga"),("🇪🇸 España","español"),("🇲🇽 México","mexicano"),("🇦🇷 Argentina","argentino"),
          ("🇨🇴 Colombia","colombiano"),("🇵🇪 Perú","peruano"),("🇨🇱 Chile","chileno"),("🇻🇪 Venezuela","venezolano"),
          ("🇫🇷 Francia","francés"),("🇩🇪 Alemania","alemán"),("🇮🇹 Italia","italiano"),("🇧🇷 Brasil","brasileño")]
    x0,y0=Inches(0.5),Inches(1.7); cw=Inches(3.0); rh=Inches(0.7)
    for i,(pais,nac) in enumerate(data):
        c=i%4; r=i//4; x=x0+c*(cw+Inches(0.1)); y=y0+r*(rh+Inches(0.14))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.12),y,Inches(1.75),rh,[[(pais,{"size":12,"bold":True,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(1.85),y,cw-Inches(1.95),rh,[[("→ "+nac,{"size":12,"color":G})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.9),
             [[("Onze route (paradas): ", {"bold":True,"color":GD}),
               ("España → México → Colombia → Perú.", {"bold":True,"color":GD}),
               ("  Spaans is officieel in +20 landen (~500 mln sprekers), ook in Guinea Ecuatorial (Afrika).", {"color":GD})],
              [("Genderneutraal in vorm: belga, estadounidense, canadiense, nicaragüense, marroquí. Klein!", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCAB/CULTURE. Koppel land↔nationaliteit; klik onthult. Volledige set (Spaanstalige + ~25 wereldlanden) "
             "op de digitale pagina (flip cards + «país ↔ nacionalidad» + klikbare kaart). Mayúscula-regel benadrukken.")

# ============================================================ DIA 15 · TALLER — mayúsculas + conectores
def s15_taller():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "TALLER DE LENGUA", "Mayúsculas y conectores", "Klik een item → correcte vorm. Twee schrijfgereedschappen voor je perfil.", num=1)
    text(s, Inches(0.5), Inches(1.5), Inches(6), Inches(0.35), [[("A · ¿mayúscula o minúscula?", {"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
    fixes=[("soy Español","soy español"),("vivo en bélgica","vivo en Bélgica"),("hablo Francés","hablo francés"),("es de madrid","es de Madrid")]
    y=Inches(1.95)
    for wrong,right in fixes:
        card(s,Inches(0.5),y,Inches(6.0),Inches(0.6),fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,Inches(0.62),y,Inches(2.9),Inches(0.6),[[(wrong,{"size":12,"color":RED})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,Inches(3.5),y,Inches(2.9),Inches(0.6),[[("→ "+right,{"size":12,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y=y+Inches(0.72)
    text(s, Inches(6.9), Inches(1.5), Inches(6), Inches(0.35), [[("B · conectores: y / e / o / u / porque", {"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
    conn=[("español ___ inglés","e","«en» vóór i-/hi-"),("siete ___ ocho","u","«of» vóór o-/ho-"),("belga ___ hablo español","y","en"),("aprendo español ___ me gusta","porque","want/omdat")]
    y=Inches(1.95)
    for q,a,gl in conn:
        card(s,Inches(6.9),y,Inches(5.9),Inches(0.6),fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,Inches(7.02),y,Inches(3.0),Inches(0.6),[[(q,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,Inches(10.1),y,Inches(2.6),Inches(0.6),[[(a+" ",{"size":13,"bold":True,"color":GD}),("· "+gl,{"size":9,"italic":True,"color":MUT})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y=y+Inches(0.72)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.85),
             [[("A: ", {"bold":True,"color":GD}), ("land/stad/naam = hoofdletter; nationaliteit/taal = kleine letter.", {"color":GD})],
              [("🔴 B: ", {"bold":True,"color":RED}), ("want én omdat = porque (één woord!). «dus» = así que / por eso, niet luego.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · TALLER. Onthul per klik. Mayúscula-regel = grote NL-valstrik (NL schrijft Spaans/Belg met hoofdletter). "
             "Conector porque dekt want én omdat. Deze twee gereedschappen meteen toepassen in het perfil / de Tarea.")

# ============================================================ DIA 16 · CULTURE — Madrid
def s16_cultura():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "CULTURA · PARADA 1", "Madrid y los nombres hispanos", "Klik een kaart → het weetje verschijnt. La Ruta verankert in een echte plek.", num=1)
    cards=[("🏙️ Madrid","Hoofdstad van España (~3,3 mln). Puerta del Sol, el Prado, el Retiro, el Real Madrid.","Ons vertrekpunt op La Ruta."),
           ("👥 Los dos apellidos","Lucía Ramírez García = apellido del padre + de la madre. Bij trouwen verandert de naam níet.","NL heeft één achternaam; hier twee."),
           ("🗣️ ¿Tú o usted?","Vrienden/leeftijdsgenoten: tú. Beleefd/onbekende volwassene: usted (+ es).","España: veel tú. Colombia/Perú: vaker usted. C6: vos (Argentina).")]
    x0,y0=Inches(0.5),Inches(1.7); cw=Inches(4.05); ch=Inches(3.4)
    for i,(t,f,nl) in enumerate(cards):
        x=x0+i*(cw+Inches(0.13))
        card(s,x,y0,cw,ch,fill=WHITE,line=G,lw=1.3)
        rect(s,x,y0,cw,Inches(0.6),fill=GT)
        text(s,x+Inches(0.15),y0,cw-Inches(0.3),Inches(0.6),[[(t,{"size":14,"bold":True,"color":GD,"font":DISPLAY})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(0.2),y0+Inches(0.8),cw-Inches(0.4),Inches(1.8),[[(f,{"size":12.5,"color":INK})]],line=1.2)
        register_reveal(s, rev)
        text(s,x+Inches(0.2),y0+Inches(2.7),cw-Inches(0.4),Inches(0.6),[[(nl,{"size":10.5,"italic":True,"color":MUT})]],line=1.1)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.35), Inches(12.3), Inches(0.6),
             [[("Actividad: ", {"bold":True,"color":GD}), ("schrijf 3 namen «à la manière hispanique» (nombre + 2 apellidos) en kies per situatie tú/usted.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · CULTURE (identiteit in diversiteit, LPD 5). Onthul per kaart. Los dos apellidos + tú/usted zijn kernculturele "
             "verschillen. Verbind met de klas: welke namen/achternamen kennen jullie? Bruggetje naar Mateo (vos) in C6.")

# ============================================================ DIA 17 · QUIZ — haz la pregunta
def s17_quiz_pregunta():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · QUIZ · INTERACCIÓN", "Haz la pregunta", "Bij dit antwoord — welke vraag? Klik → de vraag verschijnt.", num=4)
    items=[("Soy de Colombia.","¿De dónde eres?"),("Tengo 14 años.","¿Cuántos años tienes?"),
           ("Me llamo Nina.","¿Cómo te llamas?"),("Vivo en Madrid.","¿Dónde vives?"),
           ("Es leo@mail.com.","¿Cuál es tu correo?"),("Hablo español.","¿Qué idiomas hablas?")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(6.05); rh=Inches(0.78)
    for i,(ans,q) in enumerate(items):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(2.6),rh,[[(ans,{"size":12.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(2.8),y,cw-Inches(2.95),rh,[[(q,{"size":12.5,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Vraagwoord ↔ antwoordtype: ", {"bold":True,"color":GD}),
               ("origen→¿De dónde?, edad→¿Cuántos años?, nombre→¿Cómo?, dato→¿Cuál?.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ interactie. Klas formuleert de vraag vóór de klik. Daarna klassikale enquête: leerlingen stellen "
             "elkaar de vragen en rapporteren in 3e persoon (Tom tiene 15 años y vive en…).")

# ============================================================ DIA 18 · FINAL_MISSION — Mi pasaporte
def s18_tarea():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(1.35), fill=GD)
    text(s, Inches(0.5), Inches(0.18), Inches(9), Inches(1.0),
         [[("✈ Tarea final · Mi pasaporte", {"size":30,"bold":True,"color":WHITE,"font":DISPLAY})],
          [("Maak je La Ruta-paspoort en stel je voor (echt of met een nieuwe identiteit).", {"size":13,"italic":True,"color":GT})]])
    avatar(s, "mochila", Inches(11.6), Inches(0.2), Inches(1.0))
    pasos=[("1","Elige tu identidad","nombre + 2 apellidos, país, ciudad, edad, idiomas"),
           ("2","Rellena el pasaporte","in hele woorden"),
           ("3","Escribe tu presentación","5–6 frases: ser + presente + conectores"),
           ("4","Preséntate a la clase","of neem audio/video op (digitale pagina)"),
           ("5","Pregunta a un compañero","en presenta a esa persona (3ª persona)")]
    y=Inches(1.7)
    for n,es,nl in pasos:
        b=rect(s,Inches(0.5),y,Inches(0.5),Inches(0.5),fill=G,round=True,radius=0.5)
        tf=b.text_frame;tf.vertical_anchor=MSO_ANCHOR.MIDDLE;p=tf.paragraphs[0];p.alignment=PP_ALIGN.CENTER
        rr=p.add_run();rr.text=n;rr.font.size=Pt(15);rr.font.bold=True;rr.font.name=DISPLAY;rr.font.color.rgb=WHITE
        text(s,Inches(1.2),y,Inches(4.0),Inches(0.55),[[(es,{"size":14,"bold":True,"color":GD,"font":DISPLAY})]],anchor=MSO_ANCHOR.MIDDLE)
        text(s,Inches(5.3),y,Inches(7.4),Inches(0.55),[[(nl,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        y=y+Inches(0.62)
    # rúbrica
    text(s, Inches(0.5), Inches(5.0), Inches(12), Inches(0.35), [[("Rúbrica · ¿lo logré?", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    crit=["alle gegevens","ser + presente correct","y/porque + mayúsculas","mondeling voorstellen"]
    x=Inches(0.5)
    for c in crit:
        chip(s,x,Inches(5.45),"☐ "+c,fill=GT,tcolor=GD,size=11,w=Inches(3.0)); x=x+Inches(3.1)
    text(s, Inches(0.5), Inches(6.05), Inches(12), Inches(0.4),
         [[("🎯 ", {"size":12}), ("Afzender jij · ontvanger de klas/Lucía · doel jezelf voorstellen · situatie aankomst in Madrid · resultaat: paspoort + voorstelling.", {"size":11.5,"italic":True,"color":MUT})]])
    foot(s)
    notes(s, "TEACHER · FINAL_MISSION (communicatieve eindtaak). Afzender/ontvanger/doel/situatie/resultaat expliciet. "
             "Beoordeel met de rúbrica; opname + zelfevaluatie op de digitale pagina. Fictieve identiteit mag (recycling in nieuwe context).")

# ============================================================ DIA 19 · QUIZ — la mezcla
def s19_mezcla():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "QUIZ · LA MEZCLA", "Ophaal door elkaar", "Gemengde ophaal van de hele unit. Klik een vraag → het antwoord. (retrieval)", num=1)
    items=[("yo (ser)","soy"),("leeftijd-werkwoord","tener (Tengo… años)"),("nosotros hablar","hablamos"),
           ("¿___ te llamas?","Cómo"),("España → nationaliteit","español (klein!)"),("el of la: idioma","el idioma"),
           ("vivir, tú","vives"),("want/omdat","porque")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(6.05); rh=Inches(0.62)
    for i,(q,a) in enumerate(items):
        c=i//4; r=i%4; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.16))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(3.2),rh,[[(q,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(3.35),y,cw-Inches(3.5),rh,[[("→ "+a,{"size":12,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.05), Inches(12.3), Inches(0.55),
             [[("Alles komt terug: ", {"bold":True,"color":GD}), ("ser · tener (edad) · presente · interrogativos · género · mayúsculas · conectores.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ mezcla (retrieval vóór herlezen). Zonder waarschuwing door elkaar. Gebruik als exit-ticket of "
             "tussentijdse check. Zwakke punten → terug naar de betreffende dia (hyperlink via menu).")

# ============================================================ DIA 20 · FEEDBACK/REPASO
def s20_repaso():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "REPASO · LO ESENCIAL", "Lo esencial de un vistazo", "De volledige herhaling (spellen, drills) staat online. Hier: de kern + semáforo.", num=1)
    ess=["Presentarse: Me llamo… · Soy de… · Soy + nat. · Tengo… años · Vivo en… · Hablo…",
         "Ser: soy·eres·es·somos·sois·son. Presente reg.: -o/-as/-a/-amos/-áis/-an.",
         "Preguntar: ¿Cómo? ¿De dónde? ¿Dónde? ¿Cuántos años? ¿Cuál? ¿Qué? ¿Quién?",
         "Artículos: el/la · los/las · un/una (leer met lidwoord!).",
         "🔴 Trampas: edad=tener · nationaliteit=klein · ¿Cuál? vóór ser · want/omdat=porque."]
    card(s, Inches(0.5), Inches(1.6), Inches(12.3), Inches(2.5), fill=CREMA, line=None)
    y=Inches(1.8)
    for e in ess:
        text(s, Inches(0.8), y, Inches(11.8), Inches(0.45), [[("• ", {"size":13,"bold":True,"color":GD}),(e,{"size":12.5,"color":INK})]])
        y=y+Inches(0.46)
    # semáforo
    text(s, Inches(0.5), Inches(4.3), Inches(12), Inches(0.35), [[("Semáforo — ¿cómo lo llevas?", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    can=["mezelf voorstellen","ser + presente","vragen stellen","el/la kiezen","landen/nationaliteiten"]
    y=Inches(4.75)
    for c in can:
        text(s,Inches(0.8),y,Inches(7.0),Inches(0.4),[[(c,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        for j,(em,col) in enumerate([("🔴",RED),("🟠",AMBER),("🟢",G)]):
            chip(s,Inches(8.0)+j*Inches(1.5),y+Inches(0.03),em+" ",fill=WHITE,tcolor=col,size=12,w=Inches(1.3))
        y=y+Inches(0.42)
    foot(s)
    notes(s, "TEACHER · FEEDBACK/REPASO. Semáforo = zelfevaluatie (receptief/productief). Repaso-drills staan online (spellen + "
             "zelfcorrectie). Bruggetje: U2 «Mi gente» (Sevilla) — familie voorstellen met tener + posesivos.")

# ============================================================ DIA 21 · TEACHER_NOTES
def s21_teacher():
    s = slide(); bg(s, GD)
    text(s, Inches(0.6), Inches(0.4), Inches(12), Inches(0.8), [[("TEACHER_NOTES · U1 «¿Quién eres?»", {"size":26,"bold":True,"color":WHITE,"font":DISPLAY})]])
    blocks=[("Timing (50 min)","Menu 2' · datos/presentarse 10' · ser/presente 12' · reading/listening 8' · interrogativos + speaking 10' · cultura 4' · Tarea-briefing 4'."),
            ("Kernvalstrikken","edad = TENER · nationaliteit kleine letter · ¿Cuál? vóór ser · want/omdat = porque · el idioma/día (m.) · «e» vóór inglés."),
            ("Differentiatie (zij-instromers)","Alles start vanaf nul. Sterkere leerlingen: meer landen + fictieve identiteit. Zwakkere: marco/tabel langer open houden."),
            ("Digitaal","18 spellen + flip cards + klikbare kaart + recorder op de página digital. QR's in het boek → juiste anker. Conjugador = aparte tool."),
            ("Evaluatie","Tarea «Mi pasaporte» met rúbrica (4 criteria). LPD 3·4·7·8 + 5 (cultura) + 1·2 (receptief).")]
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
    s01_title(); s02_menu(); s03_datos(); s04_presentarse(); s05_ser_tener(); s06_ser(); s07_presente()
    s08_quiz_ella(); s09_reading(); s10_listening(); s11_interrog(); s12_speaking(); s13_writing()
    s14_paises(); s15_taller(); s16_cultura(); s17_quiz_pregunta(); s18_tarea(); s19_mezcla(); s20_repaso()
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

def build_alumno():
    build("alumno", OUT_ALUMNO_PPTX, include_teacher=False)
    from pptx import Presentation
    _ = Presentation(OUT_ALUMNO_PPTX)
    E.to_ppsx(OUT_ALUMNO_PPTX, OUT_ALUMNO)
    import zipfile
    with zipfile.ZipFile(OUT_ALUMNO) as z:
        assert z.testzip() is None
        assert "slideshow.main+xml" in z.read("[Content_Types].xml").decode("utf-8")
    print("opgeslagen (.ppsx geverifieerd):", OUT_ALUMNO)

if __name__ == "__main__":
    build("docente", OUT_DOCENTE, include_teacher=True)
    build_alumno()
