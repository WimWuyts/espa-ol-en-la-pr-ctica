#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_u3_docente.py — Interactieve PowerPoint C5 · Unidad 3 «El tiempo vuela» (parada Barcelona)
=========================================================================================
Zelfde engine/pijplijn als de golden sample U0/U1 (gen_u0_docente wordt geïmporteerd:
alle low-level helpers, on-click <p:timing>-animaties, hyperlink-navigatie).
Enkel de SLIDES (content) zijn U3-specifiek. Twee decks (beide .pptx):
  · C5_U3_docente.pptx — vrije navigatie, oplossingen bij klik + didactiek in spreker-notities.
  · C5_U3_alumno.pptx  — gewone diavoorstelling (F5), antwoorden verschijnen bij klik (geen kiosk).
Huisstijl groen (C5). Spaans-eerst + NL-steun. ≥20 dia's. Vier vaardigheden gedekt (lezen/luisteren/spreken/schrijven).
"""
import os
import gen_u0_docente as E
import lectura_data as _LD, escucha_data as _ED
from gen_u0_docente import (
    slide, bg, rect, text, chip, avatar, card, sectionbar, footer, noodroute,
    exercise_solucion, check_badge, legend_func, link_to, register_reveal, notes, pg,
    G, GD, GT, INK, MUT, PAPER, CREMA, LINE, RED, AMBER, WHITE,
    F_SUBJ, F_VERB, F_OBJ, F_TIME, F_PLAC, F_NEG, F_STRA, ACC,
    DISPLAY, BODY, HAND, EMU_W, EMU_H,
    Inches, Pt, RGBColor, PP_ALIGN, MSO_ANCHOR,
)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DOCENTE = os.path.join(HERE, "C5_U3_docente.pptx")
OUT_ALUMNO_PPTX = os.path.join(HERE, "C5_U3_alumno.pptx")
TAB = "U3 · EL TIEMPO VUELA"

def foot(s): footer(s, tab=TAB, page=pg())

# ============================================================ DIA 1 · TITLE
def s01_title():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(4.7), fill=G)
    rect(s, 0, Inches(4.7), EMU_W, Inches(0.09), fill=GD)
    text(s, Inches(0.6), Inches(0.35), Inches(3.4), Inches(3.6),
         [[("3", {"size": 260, "bold": True, "color": RGBColor(0x2E,0xB0,0x85), "font": DISPLAY})]],
         anchor=MSO_ANCHOR.MIDDLE)
    chip(s, Inches(4.35), Inches(0.85), "LA RUTA · PARADA 3 · BARCELONA 🇪🇸", fill=WHITE, tcolor=GD, size=12)
    text(s, Inches(4.3), Inches(1.35), Inches(8.6), Inches(1.5),
         [[("El tiempo vuela", {"size": 60, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(4.35), Inches(2.6), Inches(8.4), Inches(0.6),
         [[("La hora · la rutina · el presente irregular — en Barcelona, con Lucía y Pau.", {"size": 15, "italic": True, "color": GT})]])
    text(s, Inches(4.35), Inches(3.25), Inches(8.4), Inches(0.9),
         [[("¿Qué hora es… y qué haces cada día?", {"size": 24, "bold": True, "color": WHITE, "font": DISPLAY})],
          [("Hoe laat is het… en wat doe je elke dag?", {"size": 13, "italic": True, "color": GT})]])
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
    notes(s, "TEACHER · TITLE. Parada 3 = Barcelona, met gastvrouw Lucía en haar vriend Pau (catalán, alleen in tekst). "
             "Doel: la hora zeggen/vragen · dagroutine met reflexieve werkwoorden · presente irregular (o→ue, e→ie, e→i) + hacer/ir/salir. "
             "Kernvalstrik meteen: Es la una (1u) vs. Son las dos… (≥2u), en het reflexief pronomen vóór het werkwoord (me levanto). "
             "Instructietaal Spaans-eerst met NL-steun. Docentdeck = vrije navigatie + oplossing; leerlingdeck = elke klik onthult (geen kiosk).")

# ============================================================ DIA 2 · LESSON_MENU
def s02_menu():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "MENÚ DE LA LECCIÓN", "El mapa de la Unidad 3",
               "Kies je route — klik een tegel. Alles oefent naar de Tarea «Un día en mi vida» toe.", num=3)
    tiles = [
        ("§1", "La hora", "¿Qué hora es? · y media · ¿a qué hora?", G, 3),
        ("§2", "Mi rutina", "verbos reflexivos · me/te/se", G, 5),
        ("§3", "Presente irregular", "o→ue · e→ie · e→i · hacer/ir/salir", G, 8),
        ("§4", "Frecuencia + tiempo", "siempre/nunca · días · meses", G, 15),
        ("📖", "Lectura + escuchar", "el día de Pau · la hora", GD, 11),
        ("✈", "Tarea · Un día en mi vida", "vlog/tekst + presentarlo", GD, 19),
        ("?", "Quiz «La mezcla»", "gemengde ophaal — mét oplossing", AMBER, 20),
        ("◎", "Repaso + semáforo", "lo esencial · zelfevaluatie", GD, 21),
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
    notes(s, "TEACHER · LESSON_MENU. Elke tegel = hyperlink naar de sectie; op elke oefendia staat ⌂ Menú terug. Richttijd 50 min. "
             "Zij-instromers: begin bij §1 (la hora) en §2 (rutina) — daar zit de communicatieve kern.")

# ============================================================ DIA 3 · VOCABULARY/GRAMMAR — la hora (reveal)
def s03_hora():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · GRAMÁTICA VISUAL", "¿Qué hora es?", "Klik een klok → de tijd verschijnt. Es la UNA (1u) · Son LAS dos… (≥2u).", num=1)
    items=[("1:00","Es la una"),("2:30","Son las dos y media"),("3:15","Son las tres y cuarto"),
           ("4:45","Son las cinco menos cuarto"),("6:00","Son las seis en punto"),("9:20","Son las nueve y veinte")]
    x0,y0=Inches(0.5),Inches(1.7); cw=Inches(6.05); rh=Inches(0.72)
    for i,(dig,frase) in enumerate(items):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.16))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.2),y,Inches(1.6),rh,[[("🕐 "+dig,{"size":15,"bold":True,"color":GD,"font":DISPLAY})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(1.9),y,cw-Inches(2.0),rh,[[(frase,{"size":13,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.95),
             [[("🔴 Es la una ", {"bold":True,"color":RED}), ("(enkelvoud, alléén 1 uur) · ", {"color":GD}),
               ("Son las ", {"bold":True,"color":RED}), ("dos, tres… (meervoud, vanaf 2 uur).", {"color":GD})],
              [("y media / y cuarto (tot half) · menos cuarto (na half) · en punto (precies) · a las … de la mañana/tarde/noche.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR la hora (reveal). Klas zegt de tijd vóór je klikt. Benadruk es la/son las en y/menos. "
             "Online: «La hora» (reloj ↔ frase) + recorder «escucha y repite: la hora».")

# ============================================================ DIA 4 · GRAMMAR — mi rutina (color)
def s04_rutina_color():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · GRAMÁTICA VISUAL", "Mi rutina — la frase con color", "Kleur = taalfunctie. Reflexief pronomen (paars/oranje) vóór het werkwoord.", num=2)
    legend_func(s, Inches(9.7), Inches(0.55))
    seg = [("Yo ", F_SUBJ),("me levanto ", F_VERB),("a las siete, ", F_TIME),("me ducho ", F_VERB),
           ("y ", INK),("empiezo ", F_VERB),("en el instituto ", F_PLAC),("a las nueve.", F_TIME)]
    runs=[[(t,{"size":24,"bold":True,"color":c,"font":DISPLAY}) for t,c in seg]]
    card(s, Inches(0.5), Inches(1.7), Inches(12.3), Inches(1.2), fill=GT, line=None)
    text(s, Inches(0.8), Inches(1.7), Inches(11.7), Inches(1.2), runs, anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(3.15), Inches(12), Inches(0.4), [[("El marco — cuenta tu día:", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    frame=[("Me despierto","+ a las …"),("Me levanto","+ a las …"),("Me ducho / me visto","+ acción"),
           ("Desayuno / almuerzo / ceno","+ hora"),("Voy / salgo","+ lugar"),("Me acuesto","+ a las …")]
    x0,y0=Inches(0.5),Inches(3.6); cw=Inches(4.0); rh=Inches(0.62)
    for i,(a,b) in enumerate(frame):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.12))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(2.5),rh,[[(a,{"size":12,"bold":True,"color":F_VERB})]],anchor=MSO_ANCHOR.MIDDLE)
        text(s,x+Inches(2.65),y,cw-Inches(2.8),rh,[[(b,{"size":11,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.7), Inches(12.3), Inches(0.7),
             [[("Modelo: ", {"bold":True,"color":GD}), ("«Me despierto a las siete, me ducho, desayuno y salgo de casa a las ocho. Por la tarde hago los deberes.»", {"color":GD})]],
             trigger=btn, title_doc="MODELO · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR rutina (color-coding). Elke leerling bouwt zijn dag met het marco. Steun bouwt af (marco → beginwoorden → uit het hoofd). "
             "Kleur is nooit de enige drager. Online: «Carrusel: mi día» (recorder).")

# ============================================================ DIA 5 · GRAMMAR — reflexivos (reveal)
def s05_reflexivos():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · GRAMÁTICA", "Verbos reflexivos (me/te/se)", "Denk het pronombre + de vorm, klik de kaart. Pronomen vóór het werkwoord.", num=2)
    R=[("yo","me levanto"),("tú","te levantas"),("él/ella/usted","se levanta"),
       ("nosotros/-as","nos levantamos"),("vosotros/-as","os levantáis"),("ellos/-as/ustedes","se levantan")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(3.95); ch=Inches(1.25)
    for i,(p,v) in enumerate(R):
        c=i%3; r=i//3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(ch+Inches(0.2))
        card(s,x,y,cw,ch,fill=WHITE,line=G,lw=1.4)
        text(s,x,y+Inches(0.12),cw,Inches(0.4),[[(p,{"size":13,"color":MUT})]],align=PP_ALIGN.CENTER)
        rev=text(s,x,y+Inches(0.5),cw,Inches(0.6),[[(v,{"size":22,"bold":True,"color":GD,"font":DISPLAY})]],align=PP_ALIGN.CENTER)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.5), Inches(12.3), Inches(0.9),
             [[("🔴 Het pronombre staat VÓÓR het werkwoord: ", {"bold":True,"color":RED}), ("me levanto", {"bold":True,"color":GD}),
               (" (niet «levanto me»). Het werkwoord vervoeg je gewoon.", {"color":GD})],
              [("me/te/se/nos/os/se — past bij de persoon. Zo ook: me ducho, se acuesta (o→ue), me visto (e→i).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR reflexivos (reveal). Coro: klas zegt pronombre + vorm vóór de klik. Grote NL-valstrik: pronomen vergeten of achteraan zetten. "
             "Online: «¿reflexivo o no?» + «verbos reflexivos» (cloze).")

# ============================================================ DIA 6 · QUIZ — ¿reflexivo o no? (reveal)
def s06_quiz_reflex():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · QUIZ", "¿Reflexivo o no?", "Klik een werkwoord → reflexief of niet? Let op het pronombre.", num=2)
    items=[("levantarse","reflexivo · me levanto"),("desayunar","no · desayuno"),("ducharse","reflexivo · me ducho"),
           ("cenar","no · ceno"),("acostarse","reflexivo · me acuesto"),("hacer los deberes","no · hago")]
    x0,y0=Inches(0.5),Inches(1.7); cw=Inches(6.05); rh=Inches(0.72)
    for i,(q,ans) in enumerate(items):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.16))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(2.6),rh,[[(q,{"size":13,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        col = (F_TIME if ans.startswith("reflexivo") else G)
        rev=text(s,x+Inches(2.8),y,cw-Inches(2.95),rh,[[(ans,{"size":12,"bold":True,"color":col})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.7),
             [[("Reflexivo = una acción sobre ti mismo (me/te/se): ", {"bold":True,"color":GD}),
               ("levantarse, ducharse, vestirse, acostarse, despertarse, peinarse, lavarse.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ reflexivo (reveal). Laat de klas eerst kiezen (hand/stem). De meeste acties van de ochtend zijn reflexief.")

# ============================================================ DIA 7 · GRAMMAR — presente irregular o→ue (reveal)
def s07_oue():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · GRAMÁTICA", "Presente irregular · o → ue", "Klik een cel → de vorm. De vocal wordt UE… behalve nosotros/vosotros («la bota»).", num=3)
    cols=[("poder",["puedo","puedes","puede","podemos","podéis","pueden"]),
          ("dormir",["duermo","duermes","duerme","dormimos","dormís","duermen"]),
          ("volver",["vuelvo","vuelves","vuelve","volvemos","volvéis","vuelven"])]
    pers=["yo","tú","él/ella","nosotros","vosotros","ellos"]
    x0,y0=Inches(0.7),Inches(1.7); cw=Inches(3.9)
    for ci,(title,forms) in enumerate(cols):
        x=x0+Inches(1.7)+ci*(cw)
        card(s,x,y0,cw-Inches(0.2),Inches(0.5),fill=G,line=None)
        text(s,x,y0,cw-Inches(0.2),Inches(0.5),[[(title,{"size":13,"bold":True,"color":WHITE,"font":DISPLAY})]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    for ri,pr in enumerate(pers):
        y=y0+Inches(0.6)+ri*Inches(0.6)
        text(s,Inches(0.7),y,Inches(1.6),Inches(0.55),[[(pr,{"size":12,"color":MUT})]],anchor=MSO_ANCHOR.MIDDLE)
        for ci,(title,forms) in enumerate(cols):
            x=x0+Inches(1.7)+ci*(cw)
            card(s,x,y,cw-Inches(0.2),Inches(0.55),fill=WHITE,line=LINE,lw=1.0,shadow=False)
            noreg = (ri in (3,4))
            col = INK if noreg else F_VERB
            rev=text(s,x,y,cw-Inches(0.2),Inches(0.55),[[(forms[ri],{"size":13,"bold":not noreg,"color":col})]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
            register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(6.0), Inches(12.3), Inches(0.55),
             [[("De vocal o→ue in álle vormen BEHALVE nosotros/vosotros ", {"bold":True,"color":GD}),
               ("(podemos, dormimos). Zo ook: acostarse→me acuesto, almorzar→almuerzo, jugar→juego (u→ue).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR o→ue (reveal per cel). Teken «la bota» rond yo/tú/él/ellos. Laat de klas nosotros/vosotros voorspellen (géén wissel!). "
             "Online: «cambio de raíz» + «presente irregular Tetris».")

# ============================================================ DIA 8 · GRAMMAR — e→ie / e→i (reveal)
def s08_ieei():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · GRAMÁTICA", "Presente irregular · e→ie y e→i", "Zelfde «bota». Klik een cel → de vorm verschijnt.", num=3)
    cols=[("empezar (e→ie)",["empiezo","empiezas","empieza","empezamos","empezáis","empiezan"]),
          ("querer (e→ie)",["quiero","quieres","quiere","queremos","queréis","quieren"]),
          ("pedir (e→i)",["pido","pides","pide","pedimos","pedís","piden"])]
    pers=["yo","tú","él/ella","nosotros","vosotros","ellos"]
    x0,y0=Inches(0.7),Inches(1.7); cw=Inches(3.9)
    for ci,(title,forms) in enumerate(cols):
        x=x0+Inches(1.7)+ci*(cw)
        card(s,x,y0,cw-Inches(0.2),Inches(0.5),fill=G,line=None)
        text(s,x,y0,cw-Inches(0.2),Inches(0.5),[[(title,{"size":12,"bold":True,"color":WHITE,"font":DISPLAY})]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    for ri,pr in enumerate(pers):
        y=y0+Inches(0.6)+ri*Inches(0.6)
        text(s,Inches(0.7),y,Inches(1.6),Inches(0.55),[[(pr,{"size":12,"color":MUT})]],anchor=MSO_ANCHOR.MIDDLE)
        for ci,(title,forms) in enumerate(cols):
            x=x0+Inches(1.7)+ci*(cw)
            card(s,x,y,cw-Inches(0.2),Inches(0.55),fill=WHITE,line=LINE,lw=1.0,shadow=False)
            noreg = (ri in (3,4))
            rev=text(s,x,y,cw-Inches(0.2),Inches(0.55),[[(forms[ri],{"size":13,"bold":not noreg,"color":(INK if noreg else F_VERB)})]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
            register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(6.0), Inches(12.3), Inches(0.55),
             [[("e→ie (empiezo, quiero, prefiero, me despierto) · e→i (pido, me visto, sirvo). ", {"bold":True,"color":GD}),
               ("Nosotros/vosotros: geen wissel (empezamos, pedimos).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR e→ie/e→i (reveal). Onthul rij per rij; laat de klas de wissel voorspellen. Werkwoordsvervoeging verder = aparte Conjugador-tool. "
             "Inoefenen: online «presente irregular» (cloze) + de cloze in de cursus (§3.2).")

# ============================================================ DIA 9 · GRAMMAR — hacer/ir/salir (reveal)
def s09_hacerir():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · GRAMÁTICA", "hacer · ir · salir — el «yo» especial", "Klik een cel → de vorm. De verrassing zit in de yo-vorm.", num=3)
    cols=[("hacer",["hago","haces","hace","hacemos","hacéis","hacen"]),
          ("ir",["voy","vas","va","vamos","vais","van"]),
          ("salir",["salgo","sales","sale","salimos","salís","salen"])]
    pers=["yo","tú","él/ella","nosotros","vosotros","ellos"]
    x0,y0=Inches(0.7),Inches(1.7); cw=Inches(3.9)
    for ci,(title,forms) in enumerate(cols):
        x=x0+Inches(1.7)+ci*(cw)
        card(s,x,y0,cw-Inches(0.2),Inches(0.5),fill=G,line=None)
        text(s,x,y0,cw-Inches(0.2),Inches(0.5),[[(title,{"size":13,"bold":True,"color":WHITE,"font":DISPLAY})]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    for ri,pr in enumerate(pers):
        y=y0+Inches(0.6)+ri*Inches(0.6)
        text(s,Inches(0.7),y,Inches(1.6),Inches(0.55),[[(pr,{"size":12,"color":MUT})]],anchor=MSO_ANCHOR.MIDDLE)
        for ci,(title,forms) in enumerate(cols):
            x=x0+Inches(1.7)+ci*(cw)
            card(s,x,y,cw-Inches(0.2),Inches(0.55),fill=WHITE,line=LINE,lw=1.0,shadow=False)
            yo = (ri==0)
            rev=text(s,x,y,cw-Inches(0.2),Inches(0.55),[[(forms[ri],{"size":13,"bold":yo,"color":(F_VERB if yo else INK)})]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
            register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(6.0), Inches(12.3), Inches(0.55),
             [[("🟡 hago · salgo krijgen -g- in de yo-vorm; ir is helemaal apart (voy, vas, va…). ", {"bold":True,"color":GD}),
               ("De rest is regelmatig.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR hacer/ir/salir (reveal). Enkel de yo-vorm is speciaal (hago/salgo/voy). Laat de klas de rest afleiden.")

# ============================================================ DIA 10 · SPEAKING — cuenta tu día
def s10_speaking():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "SPEAKING · PRODUCCIÓN", "Cuenta tu día", "Bouw je dag met de substitutietabel. Steun bouwt af: tabel → beginwoorden → uit het hoofd.", num=2)
    avatar(s, "tu", Inches(11.4), Inches(1.7), Inches(1.3))
    labels=["Empiezo","Mañana","Mediodía","Tarde","Noche","Frecuencia"]
    frames=["Me levanto a las ___","Me ducho / me visto","Almuerzo a las ___","Hago los deberes","Ceno / me acuesto","Siempre / a veces / nunca"]
    x0,y0=Inches(0.5),Inches(1.8); cw=Inches(3.4); rh=Inches(0.8)
    for i,(lab,fr) in enumerate(zip(labels,frames)):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=G,lw=1.2,shadow=False)
        text(s,x+Inches(0.15),y+Inches(0.05),cw-Inches(0.3),Inches(0.32),[[(lab,{"size":10,"color":MUT})]])
        text(s,x+Inches(0.15),y+Inches(0.36),cw-Inches(0.3),Inches(0.4),[[(fr,{"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    text(s, Inches(0.5), Inches(5.0), Inches(10.5), Inches(0.9),
         [[("Ronda 1: ", {"size":12,"bold":True,"color":GD}), ("met de tabel. ", {"size":12,"color":INK}),
           ("Ronda 2: ", {"size":12,"bold":True,"color":GD}), ("alleen beginwoorden. ", {"size":12,"color":INK}),
           ("Ronda 3: ", {"size":12,"bold":True,"color":GD}), ("uit het hoofd, tegen 3 klasgenoten. ", {"size":12,"color":INK}),
           ("Ronda 4: ", {"size":12,"bold":True,"color":GD}), ("grábate → terugluisteren.", {"size":12,"color":INK})]])
    chip(s, Inches(0.5), Inches(4.65), "🎙️ Grábate online · «Carrusel: mi día»", fill=GT, tcolor=GD, size=11)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.6), Inches(12.3), Inches(0.65),
             [[("Modelo: ", {"bold":True,"color":GD}), ("«Me levanto a las siete, me ducho y desayuno. Empiezo el insti a las nueve. Por la tarde juego al fútbol. A veces ceno tarde.»", {"color":GD})]],
             trigger=btn, title_doc="MODELO · docent")
    foot(s)
    notes(s, "TEACHER · SPEAKING (substitutie → productie). Automatiseer de dagvertelling in 3 rondes met afbouwende steun. "
             "Online: SubstitutionCarousel + recorder. Print blijft bruikbaar zonder opname.")

# ============================================================ DIA 11 · READING — el día de Pau
def s11_reading():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§5 · LEER · COMPRENSIÓN", "El día de Pau", "Lees en beantwoord. Klik een vraag → het antwoord verschijnt.", num=5)
    card(s, Inches(0.5), Inches(1.65), Inches(5.8), Inches(4.4), fill=GT, line=G, lw=1.4)
    avatar(s, "diego", Inches(0.8), Inches(1.9), Inches(1.0))
    text(s, Inches(2.0), Inches(1.95), Inches(4.1), Inches(4.0),
         [[("«Me despierto a las siete y me levanto enseguida. Me ducho, me visto y desayuno. Salgo de casa a las ocho y voy al instituto en metro. Las clases empiezan a las nueve. Al mediodía almuerzo con mis amigos. Por la tarde hago los deberes y juego al fútbol. Ceno a las nueve y me acuesto a las once.»",{"size":12.5,"italic":True,"color":INK})]], line=1.22)
    qa=[("¿A qué hora se despierta Pau?","A las siete"),("¿Cómo va al instituto?","En metro"),
        ("¿A qué hora empiezan las clases?","A las nueve"),("¿Qué hace por la tarde?","Los deberes y juega al fútbol"),
        ("¿A qué hora se acuesta?","A las once")]
    x=Inches(6.5); y=Inches(1.7)
    for q,a in qa:
        card(s,x,y,Inches(6.3),Inches(0.78),fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y+Inches(0.05),Inches(6.0),Inches(0.36),[[(q,{"size":12,"bold":True,"color":GD})]])
        rev=text(s,x+Inches(0.15),y+Inches(0.4),Inches(6.0),Inches(0.32),[[("→ "+a,{"size":12,"color":INK})]])
        register_reveal(s, rev)
        y=y+Inches(0.88)
    btn=noodroute(s)
    exercise_solucion(s, Inches(6.5), Inches(6.15), Inches(6.3), Inches(0.5),
             [[("Daarna: ", {"bold":True,"color":GD}), ("leerlingen maken hun EIGEN horario (transfer → Tarea).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · READING (lezen→spreken/schrijven-keten). Eerst globaal (waarover?), dan detail (uren scannen). Onthul de antwoorden pas na de klas. "
             "Online: audio «el día de Pau» + V/F-taak.")

# ============================================================ DIA 12 · LISTENING — escucha la hora
def s12_listening():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · ESCUCHAR", "Escucha y anota la hora", "Vier momenten van de dag. Klik een kaart → hora + acción. (audio op de digitale pagina)", num=1)
    people=[("Por la mañana","7:00","me levanto"),("Al mediodía","14:30","almuerzo"),("Por la tarde","17:00","hago los deberes"),("Por la noche","23:00","me acuesto")]
    x0,y0=Inches(0.7),Inches(1.9); cw=Inches(2.95); ch=Inches(2.4)
    for i,(mom,hora,acc) in enumerate(people):
        x=x0+i*(cw+Inches(0.1))
        card(s,x,y0,cw,ch,fill=WHITE,line=LINE,lw=1.2)
        rect(s,x,y0,cw,Inches(0.5),fill=GT)
        text(s,x,y0,cw,Inches(0.5),[[("🔊  "+mom,{"size":13,"bold":True,"color":GD,"font":DISPLAY})]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        text(s,x+Inches(0.15),y0+Inches(0.65),cw-Inches(0.3),Inches(0.4),[[("Hora:",{"size":12,"color":MUT})]])
        rev1=text(s,x+Inches(0.15),y0+Inches(1.0),cw-Inches(0.3),Inches(0.4),[[(hora,{"size":16,"bold":True,"color":INK,"font":DISPLAY})]])
        text(s,x+Inches(0.15),y0+Inches(1.5),cw-Inches(0.3),Inches(0.4),[[("Acción:",{"size":12,"color":MUT})]])
        rev2=text(s,x+Inches(0.15),y0+Inches(1.85),cw-Inches(0.3),Inches(0.4),[[(acc,{"size":14,"bold":True,"color":G})]])
        register_reveal(s, rev1); register_reveal(s, rev2)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.85),
             [[("Modelo-audio (docent leest of TTS): ", {"bold":True,"color":GD}),
               ("«Por la mañana, a las siete, me levanto.» …", {"color":GD})],
              [("de la mañana/tarde/noche = concreet uur · por la mañana/tarde/noche = dagdeel (geen uur).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · LISTENING (selectief). Lees elk moment voor (of TTS). Klas noteert hora; onthul per klik. Daarna spreken: leerling vertelt zijn eigen dag.")

# ============================================================ DIA 13 · WRITING — un día en mi vida
def s13_writing():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "WRITING · PRODUCCIÓN", "Un día en mi vida", "Schrijf 6 zinnen over jouw dag. Klik → een modeltekst verschijnt.", num=2)
    card(s, Inches(0.5), Inches(1.7), Inches(6.0), Inches(3.9), fill=WHITE, line=LINE, lw=1.2)
    text(s, Inches(0.7), Inches(1.85), Inches(5.6), Inches(0.4), [[("✍️ Escribe aquí:", {"size":12,"bold":True,"color":GD})]])
    for i in range(6):
        rect(s, Inches(0.7), Inches(2.4)+i*Inches(0.5), Inches(5.6), Inches(0.01), fill=LINE)
    chk=[("una hora (es la / son las…)",),("un verbo reflexivo (me levanto…)",),("un verbo irregular (empiezo…)",),
         ("un conector (primero, después…)",),("una frecuencia (siempre, a veces)",),("mañana + tarde + noche",)]
    x=Inches(6.9); y=Inches(1.7)
    text(s,x,y,Inches(6),Inches(0.4),[[("Checklist:",{"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    for i,(c,) in enumerate(chk):
        text(s,x,y+Inches(0.5)+i*Inches(0.45),Inches(6),Inches(0.4),[[("☐  "+c,{"size":13,"color":INK})]])
    rev=card(s, x, Inches(4.5), Inches(6.0), Inches(1.1), fill=GT, line=G, lw=1.2)
    text(s, x+Inches(0.15), Inches(4.55), Inches(5.7), Inches(1.0),
         [[("Modelo: ", {"size":12,"bold":True,"color":GD}),
           ("«Normalmente me levanto a las siete, me ducho y desayuno. Empiezo el insti a las nueve. Por la tarde hago los deberes y a veces juego al fútbol. Me acuesto a las once.»",{"size":12,"italic":True,"color":INK})]], line=1.15)
    register_reveal(s, rev)
    noodroute(s); foot(s)
    notes(s, "TEACHER · WRITING (lezen→schrijven-keten). Checklist = zichtbare steun; onthul het model pas na het schrijven (retrieval vóór herlezen). "
             "Nakijkfocus: la hora, reflexivos, presente irregular, conectores. Voedt de Tarea «Un día en mi vida».")

# ============================================================ DIA 14 · TALLER — conectores + tildes
def s14_taller():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "TALLER DE LENGUA", "Conectores temporales y tildes", "Klik een item → correcte vorm. Twee gereedschappen om je dag te vertellen.", num=2)
    text(s, Inches(0.5), Inches(1.5), Inches(6), Inches(0.35), [[("A · conectores temporales", {"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
    conn=[("___ me levanto.","Primero","eerst"),("___ desayuno.","Después / Luego","daarna"),("___ hago los deberes.","Más tarde","later"),("___ me acuesto.","Por fin","ten slotte")]
    y=Inches(1.95)
    for q,a,gl in conn:
        card(s,Inches(0.5),y,Inches(6.0),Inches(0.6),fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,Inches(0.62),y,Inches(2.9),Inches(0.6),[[(q,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,Inches(3.5),y,Inches(2.9),Inches(0.6),[[(a+" ",{"size":12,"bold":True,"color":GD}),("· "+gl,{"size":9,"italic":True,"color":MUT})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y=y+Inches(0.72)
    text(s, Inches(6.9), Inches(1.5), Inches(6), Inches(0.35), [[("B · pon la tilde", {"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
    fixes=[("miercoles","miércoles"),("sabado","sábado"),("despues","después"),("¿que hora es?","¿qué hora es?")]
    y=Inches(1.95)
    for wrong,right in fixes:
        card(s,Inches(6.9),y,Inches(5.9),Inches(0.6),fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,Inches(7.02),y,Inches(3.0),Inches(0.6),[[(wrong,{"size":12,"color":RED})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,Inches(10.1),y,Inches(2.6),Inches(0.6),[[("→ "+right,{"size":12,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y=y+Inches(0.72)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.85),
             [[("A: ", {"bold":True,"color":GD}), ("primero → después/luego → más tarde → por fin. 🔴 «dan» = después/luego, niet «entonces».", {"color":GD})],
              [("B: ", {"bold":True,"color":GD}), ("veel tijdwoorden dragen een tilde: miércoles, sábado, después, mediodía; vraagwoorden altijd (¿qué?).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · TALLER. Onthul per klik. Conectores temporales structureren de dagvertelling; tildes op tijdwoorden. Meteen toepassen in de Tarea.")

# ============================================================ DIA 15 · VOCAB — frecuencia + días/meses
def s15_frecuencia():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · VOCABULARIO", "Frecuencia + días, meses y estaciones", "Klik een woord → betekenis/plaats. Días y meses met kleine letter!", num=4)
    text(s, Inches(0.5), Inches(1.5), Inches(12), Inches(0.35), [[("Escala de frecuencia (100% → 0%):", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    esc=["siempre","normalmente","a menudo","a veces","casi nunca","nunca"]
    x=Inches(0.5)
    for i,w in enumerate(esc):
        chip(s,x,Inches(1.95),w,fill=(GT if i%2==0 else CREMA),tcolor=GD,size=12,w=Inches(2.0)); x=x+Inches(2.06)
    data=[("lunes … domingo","los 7 días (klein!)"),("enero … diciembre","los 12 meses (klein!)"),
          ("primavera · verano","otoño · invierno = las estaciones"),("el fin de semana","todos los días · una vez por semana")]
    x0,y0=Inches(0.5),Inches(2.7); cw=Inches(6.05); rh=Inches(0.8)
    for i,(w,info) in enumerate(data):
        c=i%2; r=i//2; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(2.7),rh,[[(w,{"size":13,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(2.9),y,cw-Inches(3.05),rh,[[("→ "+info,{"size":11.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.95), Inches(12.3), Inches(0.85),
             [[("🔴 días/meses = kleine letter ", {"bold":True,"color":RED}), ("(lunes, enero) — anders dan landen/steden (Barcelona). ", {"color":GD})],
              [("«op maandag» = el lunes · «elke maandag» = los lunes. Frecuentie meestal vóór het werkwoord.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCAB frecuencia + tiempo. Onthul per kaart. Mayúscula-valstrik (dagen/maanden klein). Online: «frecuencia», «día vs mes».")

# ============================================================ DIA 16 · QUIZ — ¿qué hora es? (reveal)
def s16_quiz_hora():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · QUIZ · INTERACCIÓN", "Di la hora", "Bij dit uur — welke zin? Klik → de zin verschijnt.", num=1)
    items=[("1:00","Es la una."),("2:30","Son las dos y media."),("7:45","Son las ocho menos cuarto."),
           ("6:15","Son las seis y cuarto."),("12:00","Son las doce (mediodía)."),("9:00","Son las nueve en punto.")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(6.05); rh=Inches(0.78)
    for i,(dig,frase) in enumerate(items):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.2),y,Inches(1.6),rh,[[("🕐 "+dig,{"size":15,"bold":True,"color":GD,"font":DISPLAY})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(1.9),y,cw-Inches(2.0),rh,[[(frase,{"size":13,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("y (tot half) · menos (na half) · en punto (precies). ", {"bold":True,"color":GD}),
               ("Es la una (1u) / Son las… (≥2u).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ la hora. Klas formuleert de zin vóór de klik. Daarna: leerlingen vragen elkaar «¿a qué hora…?».")

# ============================================================ DIA 17 · CULTURE — el horario español
def s17_cultura():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "CULTURA · PARADA 3", "El horario español", "Klik een kaart → het weetje. In España eet en cena men later dan in België.", num=5)
    cards=[("🍽️ Las comidas","desayuno (~8h) · comida/almuerzo (~14–15h, ¡la principal!) · merienda (~18h) · cena (~21–22h).","In België: eten rond 12h en 18h — een paar uur vroeger."),
           ("🏫 El instituto","Van ~8:30 tot ~14:30, soms met pauze. Namiddag: deberes, deporte, amigos.","Ander ritme dan een lange schooldag."),
           ("😴 La siesta","Meer mito dan realidad: weinigen doen echt siesta, vooral mayores. De cultuur eet gewoon later.","Vergelijk met je eigen dagritme in Bélgica.")]
    x0,y0=Inches(0.5),Inches(1.7); cw=Inches(4.05); ch=Inches(3.4)
    for i,(t,f,nl) in enumerate(cards):
        x=x0+i*(cw+Inches(0.13))
        card(s,x,y0,cw,ch,fill=WHITE,line=G,lw=1.3)
        rect(s,x,y0,cw,Inches(0.6),fill=GT)
        text(s,x+Inches(0.15),y0,cw-Inches(0.3),Inches(0.6),[[(t,{"size":14,"bold":True,"color":GD,"font":DISPLAY})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(0.2),y0+Inches(0.8),cw-Inches(0.4),Inches(1.8),[[(f,{"size":12,"color":INK})]],line=1.2)
        register_reveal(s, rev)
        text(s,x+Inches(0.2),y0+Inches(2.7),cw-Inches(0.4),Inches(0.6),[[(nl,{"size":10.5,"italic":True,"color":MUT})]],line=1.1)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.35), Inches(12.3), Inches(0.6),
             [[("Actividad: ", {"bold":True,"color":GD}), ("vergelijk: ¿a qué hora comes y cenas TÚ en Bélgica? Schrijf jouw «horario español».", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · CULTURE (identiteit in diversiteit, LPD 5). Onthul per kaart. Het latere horario + siesta-mythe zijn kernculturele verschillen. "
             "Verbind met de klas: hoe laat eten jullie?")

# ============================================================ DIA 18 · QUIZ — conjuga (reveal)
def s18_quiz_conjuga():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · QUIZ · CONJUGA", "Conjuga el presente irregular", "Klik een cel → de juiste vorm. Let op de «bota» en de yo-vorm.", num=3)
    items=[("yo · empezar","empiezo"),("nosotros · empezar","empezamos"),("Pau · dormir","duerme"),
           ("yo · hacer","hago"),("tú · querer","quieres"),("yo · ir","voy"),
           ("ellos · pedir","piden"),("yo · salir","salgo")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(6.05); rh=Inches(0.62)
    for i,(q,a) in enumerate(items):
        c=i//4; r=i%4; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.16))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(3.2),rh,[[(q,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(3.35),y,cw-Inches(3.5),rh,[[("→ "+a,{"size":13,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.05), Inches(12.3), Inches(0.55),
             [[("Nosotros = geen wissel (empezamos). Yo speciaal bij hacer/salir/ir (hago/salgo/voy). ", {"bold":True,"color":GD}),
               ("Alle vormen nagerekend via de motor-generator.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ conjuga (retrieval). Klas geeft de vorm vóór de klik. Online: «presente irregular Tetris» + Conjugador (aparte tool).")

# ============================================================ DIA 19 · FINAL_MISSION — Un día en mi vida
def s19_tarea():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(1.35), fill=GD)
    text(s, Inches(0.5), Inches(0.18), Inches(9.5), Inches(1.0),
         [[("✈ Tarea final · Un día en mi vida", {"size":28,"bold":True,"color":WHITE,"font":DISPLAY})],
          [("Maak je vlog of tekst met horario over een dag uit je leven.", {"size":13,"italic":True,"color":GT})]])
    avatar(s, "mochila", Inches(11.6), Inches(0.2), Inches(1.0))
    pasos=[("1","Haz tu horario","de uren van jouw dag"),
           ("2","Escribe tu día","6–8 frases: hora + reflexivos + presente irregular + conectores"),
           ("3","Di la frecuencia","siempre · a veces · nunca"),
           ("4","Preséntalo","a la clase of vlog/audio (digitale pagina)"),
           ("5","Pregunta a un compañero","en presenta su día (3ª persona)")]
    y=Inches(1.7)
    for n,es,nl in pasos:
        b=rect(s,Inches(0.5),y,Inches(0.5),Inches(0.5),fill=G,round=True,radius=0.5)
        tf=b.text_frame;tf.vertical_anchor=MSO_ANCHOR.MIDDLE;p=tf.paragraphs[0];p.alignment=PP_ALIGN.CENTER
        rr=p.add_run();rr.text=n;rr.font.size=Pt(15);rr.font.bold=True;rr.font.name=DISPLAY;rr.font.color.rgb=WHITE
        text(s,Inches(1.2),y,Inches(4.0),Inches(0.55),[[(es,{"size":14,"bold":True,"color":GD,"font":DISPLAY})]],anchor=MSO_ANCHOR.MIDDLE)
        text(s,Inches(5.3),y,Inches(7.4),Inches(0.55),[[(nl,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        y=y+Inches(0.62)
    text(s, Inches(0.5), Inches(5.0), Inches(12), Inches(0.35), [[("Rúbrica · ¿lo logré?", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    crit=["la hora correct","reflexivos (me/te/se)","presente irregular","conectores + frecuencia"]
    x=Inches(0.5)
    for c in crit:
        chip(s,x,Inches(5.45),"☐ "+c,fill=GT,tcolor=GD,size=11,w=Inches(3.0)); x=x+Inches(3.1)
    text(s, Inches(0.5), Inches(6.05), Inches(12), Inches(0.4),
         [[("🎯 ", {"size":12}), ("Afzender jij · ontvanger de klas/Lucía · doel je dag vertellen · situatie een dag in Barcelona · resultaat: horario + vlog/tekst.", {"size":11.5,"italic":True,"color":MUT})]])
    foot(s)
    notes(s, "TEACHER · FINAL_MISSION (communicatieve eindtaak). Afzender/ontvanger/doel/situatie/resultaat expliciet. "
             "Beoordeel met de rúbrica; opname + zelfevaluatie op de digitale pagina («mensaje de voz: mi día»).")

# ============================================================ DIA 20 · QUIZ — la mezcla
def s20_mezcla():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "QUIZ · LA MEZCLA", "Ophaal door elkaar", "Gemengde ophaal van de hele unit. Klik een vraag → het antwoord. (retrieval)", num=1)
    items=[("1:00 (frase)","Es la una"),("yo · levantarse","me levanto"),("yo · poder","puedo"),
           ("nosotros · empezar","empezamos"),("yo · hacer","hago"),("0% frecuencia","nunca"),
           ("«dan/daarna»","después / luego"),("día con tilde","miércoles / sábado")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(6.05); rh=Inches(0.62)
    for i,(q,a) in enumerate(items):
        c=i//4; r=i%4; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.16))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(3.2),rh,[[(q,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(3.35),y,cw-Inches(3.5),rh,[[("→ "+a,{"size":12,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.05), Inches(12.3), Inches(0.55),
             [[("Alles komt terug: ", {"bold":True,"color":GD}), ("la hora · reflexivos · presente irregular · frecuencia · conectores · tildes.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ mezcla (retrieval vóór herlezen). Zonder waarschuwing door elkaar. Exit-ticket of tussentijdse check.")

# ============================================================ DIA 21 · FEEDBACK/REPASO
def s21_repaso():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "REPASO · LO ESENCIAL", "Lo esencial de un vistazo", "De volledige herhaling (20 spellen, drills) staat online. Hier: de kern + semáforo.", num=5)
    ess=["La hora: Es la una · Son las dos… · y media/cuarto · menos cuarto · en punto · ¿a qué hora? a las…",
         "Reflexivos: me/te/se/nos/os/se + verbo (me levanto). Pronombre vóór het werkwoord.",
         "Presente irregular: o→ue (puedo), e→ie (empiezo), e→i (pido) · hago · voy · salgo. NIET bij nosotros/vosotros.",
         "Frecuencia: siempre · normalmente · a menudo · a veces · casi nunca · nunca.",
         "🔴 Trampas: Es la una / Son las… · me levanto (niet levanto me) · podemos (geen ue) · días/meses klein."]
    card(s, Inches(0.5), Inches(1.6), Inches(12.3), Inches(2.5), fill=CREMA, line=None)
    y=Inches(1.8)
    for e in ess:
        text(s, Inches(0.8), y, Inches(11.8), Inches(0.45), [[("• ", {"size":13,"bold":True,"color":GD}),(e,{"size":12,"color":INK})]])
        y=y+Inches(0.46)
    text(s, Inches(0.5), Inches(4.3), Inches(12), Inches(0.35), [[("Semáforo — ¿cómo lo llevas?", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    can=["de hora zeggen en vragen","mijn rutina met reflexivos","presente irregular","frecuencia","días/meses/estaciones"]
    y=Inches(4.75)
    for c in can:
        text(s,Inches(0.8),y,Inches(7.0),Inches(0.4),[[(c,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        for j,(em,col) in enumerate([("🔴",RED),("🟠",AMBER),("🟢",G)]):
            chip(s,Inches(8.0)+j*Inches(1.5),y+Inches(0.03),em+" ",fill=WHITE,tcolor=col,size=12,w=Inches(1.3))
        y=y+Inches(0.42)
    foot(s)
    notes(s, "TEACHER · FEEDBACK/REPASO. Semáforo = zelfevaluatie. Repaso-drills online (20 spellen + zelfcorrectie). "
             "Bruggetje: U4 «Me gusta» (València) — gustos & aficiones (me gusta / me encanta).")

# ============================================================ DIA 22 · TEACHER_NOTES
def s22_teacher():
    s = slide(); bg(s, GD)
    text(s, Inches(0.6), Inches(0.4), Inches(12), Inches(0.8), [[("TEACHER_NOTES · U3 «El tiempo vuela»", {"size":26,"bold":True,"color":WHITE,"font":DISPLAY})]])
    blocks=[("Timing (50 min)","Menu 2' · la hora 8' · rutina/reflexivos 10' · presente irregular 12' · reading/listening 8' · speaking/writing 6' · Tarea-briefing 4'."),
            ("Kernvalstrikken","Es la una / Son las… · pronomen vóór verbo (me levanto) · nosotros/vosotros géén stamwissel · hago/salgo/voy · de la vs por la · días/meses klein."),
            ("Differentiatie (zij-instromers)","Alles start vanaf nul. Sterker: hele dag + frecuencia. Zwakker: la hora eerst automatiseren, marco/tabel langer open."),
            ("Digitaal","20 spellen + flip cards + klikbare kaart + recorder («la hora», «mi día», «mensaje de voz») op de página digital. QR's → juiste anker. Conjugador = aparte tool."),
            ("Evaluatie","Tarea «Un día en mi vida» met rúbrica (4 criteria). LPD 3·4·7·8 + 5 (cultura: el horario) + 1·2 (receptief: el día de Pau).")]
    y=Inches(1.4)
    for t,b in blocks:
        card(s, Inches(0.5), y, Inches(12.3), Inches(1.0), fill=RGBColor(0x1B,0x63,0x49), line=None)
        text(s, Inches(0.75), y+Inches(0.08), Inches(11.8), Inches(0.4), [[(t, {"size":14,"bold":True,"color":WHITE,"font":DISPLAY})]])
        text(s, Inches(0.75), y+Inches(0.48), Inches(11.8), Inches(0.5), [[(b, {"size":11.5,"color":GT})]], line=1.12)
        y=y+Inches(1.12)
    footer(s, tab=TAB, page=pg())
    notes(s, "Alleen in het docentdeck. Volledige LPD-dekking en didactische route staan in het cursusdossier (U3_bron.md).")

# ============================================================ RUN + BUILD
def _run_all(include_teacher=True):
    s01_title(); s02_menu(); s03_hora(); s04_rutina_color(); s05_reflexivos(); s06_quiz_reflex()
    s07_oue(); s08_ieei(); s09_hacerir(); s10_speaking(); s11_reading(); s12_listening(); s13_writing()
    s14_taller(); s15_frecuencia(); s16_quiz_hora(); s17_cultura(); s18_quiz_conjuga()
    # Lectura en Escucha uit de gedeelde bron — zelfde inhoud als print en hub.
    E.s_lectura(_LD.C5_U3); E.s_escucha(_ED.C5_U3)
    s19_tarea()
    s20_mezcla(); s21_repaso()
    if include_teacher:
        s22_teacher()

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
    # Leerlingdeck als .pptx (NIET .ppsx — PowerPoint weigert dat slideshow-contenttype). Zie HANDOVER §3c/§9.
    build("alumno", OUT_ALUMNO_PPTX, include_teacher=False)
    from pptx import Presentation
    _ = Presentation(OUT_ALUMNO_PPTX)
    print("alumno-deck geverifieerd (.pptx):", OUT_ALUMNO_PPTX)

if __name__ == "__main__":
    build("docente", OUT_DOCENTE, include_teacher=True)
    build_alumno()
