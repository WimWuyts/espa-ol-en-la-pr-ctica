#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_u8_docente.py — Interactieve PowerPoint C5 · Unidad 8 «¿Qué has hecho?» (parada Perú/Cusco · Machu Picchu)
=============================================================================================================
Zelfde engine/pijplijn als de golden sample U0/U1/U5 (gen_u0_docente wordt geïmporteerd:
low-level helpers, on-click <p:timing>-animaties, hyperlink-navigatie). Enkel de SLIDES zijn U8-specifiek.
Twee decks (beide .pptx):
  · C5_U8_docente.pptx — vrije navigatie, oplossingen bij klik + didactiek in spreker-notities.
  · C5_U8_alumno.pptx  — gewone diavoorstelling, antwoorden verschijnen bij klik (F5, geen kiosk).
Huisstijl groen (C5). Spaans-eerst + NL-steun. ≥20 dia's. Dekt de vier vaardigheden. Nina = gastvrouw.
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
OUT_DOCENTE = os.path.join(HERE, "C5_U8_docente.pptx")
OUT_ALUMNO_PPTX = os.path.join(HERE, "C5_U8_alumno.pptx")
TAB = "U8 · ¿QUÉ HAS HECHO?"

def foot(s): footer(s, tab=TAB, page=pg())

# ============================================================ DIA 1 · TITLE
def s01_title():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(4.7), fill=G)
    rect(s, 0, Inches(4.7), EMU_W, Inches(0.09), fill=GD)
    text(s, Inches(0.6), Inches(0.35), Inches(3.4), Inches(3.6),
         [[("8", {"size": 260, "bold": True, "color": RGBColor(0x2E,0xB0,0x85), "font": DISPLAY})]],
         anchor=MSO_ANCHOR.MIDDLE)
    chip(s, Inches(4.35), Inches(0.85), "LA RUTA · PARADA 8 · PERÚ · CUSCO · MACHU PICCHU 🇵🇪", fill=WHITE, tcolor=GD, size=12)
    text(s, Inches(4.3), Inches(1.35), Inches(8.6), Inches(1.5),
         [[("¿Qué has hecho?", {"size": 60, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(4.35), Inches(2.7), Inches(8.4), Inches(0.6),
         [[("Viajes y experiencias recientes: el perfecto compuesto, los participios y el tiempo — en los Andes, con Nina.", {"size": 14, "italic": True, "color": GT})]])
    text(s, Inches(4.35), Inches(3.35), Inches(8.4), Inches(0.9),
         [[("¿Qué has hecho este año?", {"size": 24, "bold": True, "color": WHITE, "font": DISPLAY})],
          [("Wat heb je dit jaar gedaan?", {"size": 13, "italic": True, "color": GT})]])
    text(s, Inches(0.6), Inches(4.95), Inches(6), Inches(0.4),
         [[("La gente de la ruta — je reisgezellen", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    x = Inches(0.6)
    for nm, city in [("nina","Cusco 🇵🇪 · anfitriona"),("lucia","Sevilla 🇪🇸"),("diego","CDMX 🇲🇽"),
                     ("valen","Cartagena 🇨🇴"),("tu","Tú · Flandes 🇧🇪"),("mochila","La mochila")]:
        avatar(s, nm, x, Inches(5.4), Inches(1.0))
        text(s, x - Inches(0.15), Inches(6.42), Inches(1.3), Inches(0.5),
             [[(nm.capitalize() if nm!="tu" else "Tú", {"size": 10.5, "bold": True, "color": INK})],
              [(city.split("·")[-1].strip() if nm!="tu" else "de reiziger = jij", {"size": 8.5, "color": MUT})]],
             align=PP_ALIGN.CENTER)
        x = x + Inches(2.05)
    foot(s)
    notes(s, "TEACHER · TITLE. Parada 8 = Perú (Cusco · Machu Picchu): de laatste halte van jaar 5. Gastvrouw = Nina. Doel: contar qué has hecho "
             "met het pretérito perfecto compuesto (haber + participio), de participios (reg. -ado/-ido + irregular hecho/visto/dicho…), de marcadores "
             "(ya/todavía no/hoy/alguna vez/nunca) en el tiempo (hace sol/frío, llueve, nieva, está nublado). Kernvalstrik: haber ≠ tener (has hecho, niet tienes hecho); "
             "participio blijft gelijk (ha comidO). Docentdeck = vrije navigatie + oplossing in notities; leerlingdeck (.pptx, F5) = elke klik onthult het antwoord.")

# ============================================================ DIA 2 · LESSON_MENU
def s02_menu():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "MENÚ DE LA LECCIÓN", "El mapa de la Unidad 8",
               "Kies je route — klik een tegel. Alles oefent naar de Tarea «Mis vacaciones» toe.", num=8)
    tiles = [
        ("§1", "He hecho…", "perfecto compuesto", G, 3),
        ("§2", "Participios", "-ado/-ido + irregular", G, 6),
        ("§3", "Marcadores", "ya · todavía no · nunca", G, 7),
        ("§4", "¿Qué tiempo hace?", "hace sol · llueve · nieva", G, 4),
        ("§5", "Lectura + escucha", "el diario de Nina", G, 9),
        ("★", "Cultura · Machu Picchu", "los Andes y el clima", GD, 16),
        ("🎒", "Tarea · Mis vacaciones", "reisverslag (vlog/tekst)", GD, 18),
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
             [[(es, {"size": 14, "bold": True, "color": WHITE, "font": DISPLAY})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + Inches(0.18), y + Inches(0.68), tw - Inches(0.36), Inches(1.2), [[(nl, {"size": 11.5, "color": INK})]], line=1.12)
        chip(s, x + Inches(0.18), y + th - Inches(0.45), f"→ dia {dia}", fill=GT, tcolor=GD, size=9.5)
    foot(s)
    notes(s, "TEACHER · LESSON_MENU. Elke tegel = hyperlink; op elke oefendia staat ⌂ Menú terug. Richttijd 50 min. "
             "Begin bij §1 (perfecto compuesto) → §2 (participios) = het hart van de unit. Kruisverwijzing print/HTML: «oefen online — 18 juegos».")

# ============================================================ DIA 3 · VOCABULARY — viajes & clima
def s03_vocab():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§V · VOCABULARIO", "Viajes, transporte y el tiempo", "De woorden van de reis — observa. Herken ze, dan gebruik je ze.", num=1)
    legend_func(s, Inches(9.7), Inches(0.55))
    rows = [("el viaje","de reis","la maleta · el billete"),("las vacaciones","de vakantie","el hotel · la playa"),
            ("el avión","het vliegtuig","el tren · el barco"),("la montaña","de berg","el mar · la excursión"),
            ("hace sol","het is zonnig","hace calor · hace frío"),("llueve","het regent","nieva · está nublado"),
            ("la llama","de lama","Machu Picchu 🇵🇪"),("el pasaporte","het paspoort","la foto · el recuerdo")]
    x0,y0 = Inches(0.5), Inches(1.6); cw=Inches(6.1); rh=Inches(0.6)
    for i,(k,v,nl) in enumerate(rows):
        c = 0 if i<4 else 1; r = i%4
        x = x0 + c*(cw+Inches(0.15)); y = y0 + r*(rh+Inches(0.12))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x+Inches(0.15), y, Inches(2.4), rh, [[(k, {"size":13,"bold":True,"color":GD})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x+Inches(2.5), y, Inches(2.3), rh, [[(v, {"size":12,"color":INK})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x+Inches(4.6), y, Inches(1.4), rh, [[(nl, {"size":9,"italic":True,"color":MUT})]], anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(4.75), Inches(12.3), Inches(0.5),
         [[("Marcadores: ", {"size":13,"bold":True,"color":GD,"font":DISPLAY}),
           ("hoy · esta semana · este año", {"size":13,"bold":True,"color":F_TIME}), (" · ",{"size":13,"color":INK}),
           ("ya ↔ todavía no · alguna vez · nunca", {"size":13,"bold":True,"color":F_TIME})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.35), Inches(12.3), Inches(0.95),
             [[("🔴 «Het is warm (weer)» = ", {"bold":True,"color":RED}), ("hace calor", {"bold":True,"color":GD}), (" (niet «es caliente»).", {"color":GD})],
              [("Drie manieren voor het weer: hace (sol/frío) · un verbo (llueve/nieva) · está (nublado).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCABULARY. Toon per cluster (viajes/transporte/clima). Laat raden zónder de NL-gloss. "
             "Online: flip cards + Memoria de los viajes + El tiempo y el clima.")

# ============================================================ DIA 4 · GRAMMAR — perfecto compuesto (color)
def s04_perfecto():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · GRAMÁTICA VISUAL", "Pretérito perfecto compuesto — haber + participio", "Kleur = de functie. haber (he/has/ha…) + participio.", num=1)
    legend_func(s, Inches(9.7), Inches(0.55))
    seg = [("(Yo) ", F_SUBJ),("he ", F_VERB),("visto ", F_OBJ),("Machu Picchu ", F_PLAC),("hoy.", F_TIME)]
    runs=[[(t,{"size":24,"bold":True,"color":c,"font":DISPLAY}) for t,c in seg]]
    card(s, Inches(0.5), Inches(1.7), Inches(12.3), Inches(1.2), fill=GT, line=None)
    text(s, Inches(0.8), Inches(1.7), Inches(11.7), Inches(1.2), runs, anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(3.15), Inches(12), Inches(0.4), [[("El auxiliar «haber» — ¿qué forma?", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    frame=[("yo → he","he viajado"),("tú → has","has comido"),("él/ella → ha","ha subido"),
           ("nosotros → hemos","hemos ido"),("vosotros → habéis","habéis hecho"),("ellos → han","han vuelto")]
    x0,y0=Inches(0.5),Inches(3.6); cw=Inches(4.0); rh=Inches(0.62)
    for i,(a,b) in enumerate(frame):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.12))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(1.9),rh,[[(a,{"size":12,"bold":True,"color":F_VERB})]],anchor=MSO_ANCHOR.MIDDLE)
        text(s,x+Inches(2.05),y,cw-Inches(2.2),rh,[[(b,{"size":11,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.7), Inches(12.3), Inches(0.7),
             [[("Regla: ", {"bold":True,"color":GD}), ("haber (he, has, ha, hemos, habéis, han) + participio. Auxiliar = haber, niet tener. De participio blijft gelijk (ha comidO).", {"color":GD})]],
             trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR (color-coding). Twee delen zichtbaar maken: haber (vervoegd) + participio (vast). Verbindt verleden met nu (hoy/esta semana). "
             "Online: «completa: haber + participio» (cloze) + haber Tetris.")

# ============================================================ DIA 5 · QUIZ — haber + participio
def s05_perfecto_quiz():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · QUIZ", "Completa: haber + participio", "Klik een zin → de juiste vorm verschijnt. Let op de onregelmatige participios.", num=1)
    items=[("(Yo) ___ a Machu Picchu (subir)","he subido"),("¿(Tú) ___ las llamas? (ver)","has visto"),
           ("(Nosotros) ___ fotos (sacar)","hemos sacado"),("Nina ___ una postal (escribir)","ha escrito"),
           ("(Ellos) ___ en tren (viajar)","han viajado"),("¿(Vosotros) ___ la maleta? (hacer)","habéis hecho")]
    x0,y0=Inches(0.5),Inches(1.7); cw=Inches(6.05); rh=Inches(0.7)
    for i,(q,ans) in enumerate(items):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(3.9),rh,[[(q,{"size":11.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(4.1),y,cw-Inches(4.2),rh,[[(ans,{"size":13,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.95),
             [[("Onregelmatige participios hier: ", {"bold":True,"color":G}), ("ver → visto · escribir → escrito · hacer → hecho.", {"color":GD})],
              [("De rest is regelmatig: subir → subido · sacar → sacado · viajar → viajado.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ (reveal). Laat de klas eerst de vorm bouwen (haber + participio), klik dan. Online: «haber + participio» (cloze) + haber Tetris.")

# ============================================================ DIA 6 · GRAMMAR — participios (reveal)
def s06_participios():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · GRAMÁTICA", "Los participios — la máquina", "Klik een kaart → de participio verschijnt. -ar → -ado · -er/-ir → -ido · irregulares.", num=2)
    text(s, Inches(0.5), Inches(1.5), Inches(12.3), Inches(0.5),
         [[("La fórmula: ", {"size":14,"color":INK}),
           ("-ar → -ado ", {"size":14,"bold":True,"color":F_VERB}),
           ("· -er/-ir → -ido ", {"size":14,"bold":True,"color":F_OBJ}),
           ("· irregulares (memorizar)", {"size":14,"bold":True,"color":RED})]])
    inf=["viajar","comer","vivir","hacer","ver","escribir","volver","poner","abrir"]
    par=["viajado","comido","vivido","hecho","visto","escrito","vuelto","puesto","abierto"]
    x0,y0=Inches(0.5),Inches(2.2); cw=Inches(4.0); ch=Inches(1.0)
    for i,(p,f) in enumerate(zip(inf,par)):
        c=i%3; r=i//3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(ch+Inches(0.15))
        irr = f in ("hecho","visto","escrito","vuelto","puesto","abierto")
        card(s,x,y,cw,ch,fill=WHITE,line=(RED if irr else G),lw=1.4)
        text(s,x,y+Inches(0.1),cw,Inches(0.35),[[(p,{"size":12,"color":MUT})]],align=PP_ALIGN.CENTER)
        rev=text(s,x,y+Inches(0.44),cw,Inches(0.5),[[("→ "+f,{"size":19,"bold":True,"color":(RED if irr else GD),"font":DISPLAY})]],align=PP_ALIGN.CENTER)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.9), Inches(12.3), Inches(0.7),
             [[("🔴 Los 8 irregulares: ", {"bold":True,"color":RED}),
               ("hecho, visto, dicho, escrito, vuelto, puesto, abierto, roto. ", {"bold":True,"color":GD}),
               ("Truco: muchos acaban en -to o -cho.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR participios (reveal). Onthul per kaart; laat de vorm voorspellen. Rood = irregular (memoriseren). "
             "Online: «participio ↔ infinitivo» (match) + «regular o irregular» (classify) + «participio irregular» (cloze).")

# ============================================================ DIA 7 · GRAMMAR — marcadores (reveal)
def s07_marcadores():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · GRAMÁTICA · FUNCIONES", "Marcadores — ya / todavía no / nunca", "Klik een kaart → periode of ervaring. Ze kondigen het perfecto compuesto aan.", num=3)
    items=[("📅 Periodo abierto","hoy · esta semana · este año",G),("✅ ya","ya he hecho la maleta",AMBER),
           ("⏳ todavía no","todavía no he comido",G),("🌍 Experiencia","¿Has viajado alguna vez?",AMBER),
           ("🚫 nunca","Nunca he estado en Perú",G),("🔁 muchas veces","Lo he visto muchas veces",AMBER)]
    x0,y0=Inches(0.5),Inches(1.8); cw=Inches(6.05); ch=Inches(1.0)
    for i,(lab,txt,col) in enumerate(items):
        c=i%2; r=i//2; x=x0+c*(cw+Inches(0.2)); y=y0+r*(ch+Inches(0.18))
        card(s,x,y,cw,ch,fill=WHITE,line=col,lw=1.4)
        chip(s,x+Inches(0.2),y+Inches(0.12),lab,fill=GT,tcolor=GD,size=11)
        rev=text(s,x+Inches(0.2),y+Inches(0.5),cw-Inches(0.4),Inches(0.45),[[(txt,{"size":13.5,"bold":True,"color":GD,"font":DISPLAY})]])
        register_reveal(s, rev)
    text(s, Inches(0.5), Inches(5.55), Inches(12.3), Inches(0.5),
         [[("🔴 ya (klaar ✅) ↔ todavía no (nog niet ⏳). ", {"size":12,"bold":True,"color":RED}), ("nunca + he… = «ik heb nooit…».", {"size":12,"color":INK})]])
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(6.1), Inches(12.3), Inches(0.55),
             [[("Deze marcadores + perfecto compuesto: ", {"bold":True,"color":GD}), ("hoy · esta semana · este año · ya · todavía no · alguna vez · nunca · muchas veces.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR marcadores. Twee soorten: periode-die-loopt vs. ervaring. Onthul per klik. "
             "Online: «¿ya, todavía no o…?» (cloze) + «periodo o experiencia» (classify).")

# ============================================================ DIA 8 · QUIZ — regular o irregular
def s08_quiz_participio():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · QUIZ", "¿Participio regular o irregular?", "Klik een werkwoord → de participio + het type verschijnt.", num=2)
    items=[("viajar","viajado · regular"),("hacer","hecho · irregular"),("comer","comido · regular"),
           ("ver","visto · irregular"),("escribir","escrito · irregular"),("subir","subido · regular")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(6.05); rh=Inches(0.78)
    for i,(q,a) in enumerate(items):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(2.4),rh,[[(q,{"size":13,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(2.6),y,cw-Inches(2.7),rh,[[("→ "+a,{"size":12.5,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Regular = -ado (-ar) / -ido (-er,-ir). ", {"bold":True,"color":GD}),
               ("Irregular = hecho, visto, dicho, escrito, vuelto, puesto, abierto, roto.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ participio (retrieval). Klas roept regular/irregular vóór de klik. Online: «regular o irregular» (classify).")

# ============================================================ DIA 9 · READING — el diario de Nina
def s09_reading():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§5 · LEER · COMPRENSIÓN", "El diario de viaje de Nina", "Lees en beantwoord. Klik een vraag → het antwoord verschijnt.", num=5)
    card(s, Inches(0.5), Inches(1.65), Inches(5.6), Inches(3.9), fill=GT, line=G, lw=1.4)
    avatar(s, "nina", Inches(0.85), Inches(1.95), Inches(1.1))
    text(s, Inches(2.1), Inches(2.0), Inches(3.8), Inches(1.5),
         [[("«Lunes: he llegado a Cusco en avión. Hace frío y está nublado. He visto la Plaza de Armas. "
            "Martes: he cogido el tren y he subido a Machu Picchu. Ha hecho sol. He visto las llamas y he escrito una postal.»",{"size":12,"italic":True,"color":INK})]], line=1.18)
    qa=[("¿Cómo ha viajado a Cusco?","En avión"),("¿Qué tiempo hace en Cusco?","Hace frío y está nublado"),
        ("¿Cómo ha ido a Machu Picchu?","En tren"),("¿Qué ha visto en Machu Picchu?","Las llamas")]
    x=Inches(6.4); y=Inches(1.7)
    for q,a in qa:
        card(s,x,y,Inches(6.4),Inches(0.85),fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y+Inches(0.06),Inches(6.1),Inches(0.4),[[(q,{"size":12.5,"bold":True,"color":GD})]])
        rev=text(s,x+Inches(0.15),y+Inches(0.44),Inches(6.1),Inches(0.35),[[("→ "+a,{"size":12,"color":INK})]])
        register_reveal(s, rev)
        y=y+Inches(0.98)
    btn=noodroute(s)
    exercise_solucion(s, Inches(6.4), Inches(5.65), Inches(6.4), Inches(0.6),
             [[("🎯 Leesdoel: ", {"bold":True,"color":GD}), ("volg wat Nina wél/niet gedaan heeft + het weer. Scannen, niet élk woord.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · READING (lezen→schrijven-keten). Eerst voorspellen (titel/foto), dan scannen. Onthul de antwoorden pas na de klas. "
             "Daarna: leerlingen schrijven hun eigen dagboekdag (transfer → Tarea Mis vacaciones).")

# ============================================================ DIA 10 · LISTENING — ¿qué han hecho?
def s10_listening():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · ESCUCHAR", "¿Qué han hecho este verano?", "Vier personas cuentan. Klik un nombre → wat ze gedaan hebben. (audio op de digitale pagina)", num=1)
    people=[("Nina","ha subido a Machu Picchu","🇵🇪"),("Diego","ha comido en un mercado","🇲🇽"),
            ("Lucía","ha ido a la playa","🇪🇸"),("Valen","ha viajado en barco","🇨🇴")]
    x0,y0=Inches(0.7),Inches(1.9); cw=Inches(2.95); ch=Inches(2.4)
    for i,(nm,com,fl) in enumerate(people):
        x=x0+i*(cw+Inches(0.1))
        card(s,x,y0,cw,ch,fill=WHITE,line=LINE,lw=1.2)
        rect(s,x,y0,cw,Inches(0.5),fill=GT)
        text(s,x,y0,cw,Inches(0.5),[[("🔊  "+nm+" "+fl,{"size":14,"bold":True,"color":GD,"font":DISPLAY})]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        text(s,x+Inches(0.15),y0+Inches(0.7),cw-Inches(0.3),Inches(0.4),[[("Ha…",{"size":12,"color":MUT})]])
        rev1=text(s,x+Inches(0.15),y0+Inches(1.1),cw-Inches(0.3),Inches(0.9),[[(com,{"size":13,"bold":True,"color":INK})]],line=1.1)
        register_reveal(s, rev1)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.85),
             [[("Modelo-audio (docent leest of TTS): ", {"bold":True,"color":GD}),
               ("«Este verano he subido a Machu Picchu y he sacado muchas fotos.» …", {"color":GD})],
              [("Daarna spreken: leerling vertelt zelf wat hij/zij gedaan heeft.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · LISTENING (selectief → spreken). Lees elk verhaal voor (of TTS). Klas noteert het participio; onthul per klik. "
             "Koppel meteen aan de spreekopdracht (§1 ¿qué has hecho tú?).")

# ============================================================ DIA 11 · GRAMMAR — ya / todavía no (reveal)
def s11_ya():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · GRAMÁTICA", "¿ya o todavía no?", "Klik een taak → ya (✅) of todavía no (⏳). De checklist van Nina.", num=3)
    R=[("He hecho la maleta ✅","ya"),("He reservado el hotel ⏳","todavía no"),("He comprado el billete ✅","ya"),
       ("He llamado al hotel ⏳","todavía no"),("Me he puesto el abrigo ✅","ya"),("He subido a la montaña ⏳","todavía no")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(6.05); rh=Inches(0.78)
    for i,(p,v) in enumerate(R):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=G,lw=1.2)
        text(s,x+Inches(0.15),y,Inches(3.9),rh,[[(p,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(4.1),y,cw-Inches(4.2),rh,[[("→ "+v,{"size":13,"bold":True,"color":GD,"font":DISPLAY})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    text(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.5),
         [[("🟡 ", {"size":12}), ("ya = al (klaar) · todavía no = nog niet. ¿Ya has comido? → No, todavía no.", {"size":12,"bold":True,"color":GD})]])
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.75), Inches(12.3), Inches(0.65),
             [[("ya (✅ klaar) staat vóór het perfecto; todavía no (⏳) ook. ", {"bold":True,"color":GD}),
               ("¿Alguna vez has…? = «Heb je ooit…?».", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR ya/todavía no (reveal). Coro: klas zegt ya/todavía no vóór de klik. Online: «¿ya, todavía no o…?» (cloze).")

# ============================================================ DIA 12 · SPEAKING — cuenta tu viaje
def s12_speaking():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · SPEAKING · INTERACCIÓN", "¡Cuenta tu viaje!", "Vertel wat je gedaan hebt. Steun bouwt af: kaarten → beginwoorden → uit het hoofd.", num=1)
    avatar(s, "tu", Inches(11.4), Inches(1.7), Inches(1.3))
    labels=["¿Adónde?","¿Cómo?","¿Qué tiempo?","¿Qué has visto?","¿Con quién?","¿Te ha gustado?"]
    frames=["He ido a…","He viajado en…","Ha hecho…","He visto…","con…","Me ha encantado."]
    x0,y0=Inches(0.5),Inches(1.8); cw=Inches(3.4); rh=Inches(0.8)
    for i,(lab,fr) in enumerate(zip(labels,frames)):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=G,lw=1.2,shadow=False)
        text(s,x+Inches(0.15),y+Inches(0.05),cw-Inches(0.3),Inches(0.32),[[(lab,{"size":10,"color":MUT})]])
        text(s,x+Inches(0.15),y+Inches(0.36),cw-Inches(0.3),Inches(0.4),[[(fr,{"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    text(s, Inches(0.5), Inches(5.0), Inches(10.5), Inches(0.9),
         [[("Ronda 1: ", {"size":12,"bold":True,"color":GD}), ("met de kaarten. ", {"size":12,"color":INK}),
           ("Ronda 2: ", {"size":12,"bold":True,"color":GD}), ("alleen beginwoorden. ", {"size":12,"color":INK}),
           ("Ronda 3: ", {"size":12,"bold":True,"color":GD}), ("uit het hoofd, ander viaje. ", {"size":12,"color":INK}),
           ("Ronda 4: ", {"size":12,"bold":True,"color":GD}), ("grábate en de digitale pagina.", {"size":12,"color":INK})]])
    chip(s, Inches(0.5), Inches(4.65), "🎙️ Grábate online · «Mensaje de voz: cuenta tu viaje»", fill=GT, tcolor=GD, size=11)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.6), Inches(12.3), Inches(0.65),
             [[("Modelo: ", {"bold":True,"color":GD}), ("«He ido a Perú. He viajado en avión. Ha hecho frío en la sierra. He visto Machu Picchu. Me ha encantado.»", {"color":GD})]],
             trigger=btn, title_doc="MODELO · docent")
    foot(s)
    notes(s, "TEACHER · SPEAKING (interactie). Automatiseer vertellen-wat-je-gedaan-hebt in rondes met afbouwende steun. "
             "Online: recorder (opname + zelfevaluatie). Print blijft bruikbaar zonder opname.")

# ============================================================ DIA 13 · WRITING — mi diario
def s13_writing():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "WRITING · PRODUCCIÓN", "Mi diario de viaje", "Schrijf één dagboekdag. Klik → een modeltekst verschijnt.", num=1)
    card(s, Inches(0.5), Inches(1.7), Inches(6.0), Inches(3.9), fill=WHITE, line=LINE, lw=1.2)
    text(s, Inches(0.7), Inches(1.85), Inches(5.6), Inches(0.4), [[("✍️ Escribe aquí tu diario:", {"size":12,"bold":True,"color":GD})]])
    for i in range(6):
        rect(s, Inches(0.7), Inches(2.4)+i*Inches(0.5), Inches(5.6), Inches(0.01), fill=LINE)
    chk=[("4× perfecto compuesto","he + participio"),("1 marcador","hoy · ya · nunca…"),("el transporte","he viajado en…"),("el tiempo","ha hecho…"),("conectores","primero · luego · al final"),("una foto/dibujo","con onderschrift")]
    x=Inches(6.9); y=Inches(1.7)
    text(s,x,y,Inches(6),Inches(0.4),[[("Checklist:",{"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    for i,(c,h) in enumerate(chk):
        text(s,x,y+Inches(0.5)+i*Inches(0.42),Inches(6),Inches(0.4),[[("☐  "+c+" ",{"size":12.5,"color":INK}),("· "+h,{"size":10,"italic":True,"color":MUT})]])
    rev=card(s, x, Inches(4.35), Inches(6.0), Inches(1.25), fill=GT, line=G, lw=1.2)
    text(s, x+Inches(0.15), Inches(4.4), Inches(5.7), Inches(1.2),
         [[("Modelo: ", {"size":12,"bold":True,"color":GD}),
           ("«Hoy he llegado a Cusco en avión. Ha hecho frío. Primero he visto la plaza, luego he comido. Todavía no he subido a la montaña.»",{"size":12,"italic":True,"color":INK})]], line=1.15)
    register_reveal(s, rev)
    noodroute(s); foot(s)
    notes(s, "TEACHER · WRITING (lezen→schrijven). Checklist = zichtbare steun; onthul het model pas na het schrijven (retrieval). "
             "Nakijkfocus: perfecto compuesto (4×), participios, marcadores, het weer. Dit voedt de Tarea «Mis vacaciones».")

# ============================================================ DIA 14 · VOCAB — transporte/clima (reveal)
def s14_transporte():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§V · VOCABULARIO · CLIMA", "El transporte y el tiempo", "Klik een woord → de vertaling verschijnt. Bouw je woordnetwerk.", num=1)
    data=[("el avión","vliegtuig"),("el tren","trein"),("el barco","boot"),("la bicicleta","fiets"),
          ("hace sol","het is zonnig"),("hace frío","het is koud"),("llueve","het regent"),("nieva","het sneeuwt"),
          ("está nublado","bewolkt"),("la tormenta","storm"),("el paraguas","paraplu"),("la nieve","sneeuw")]
    x0,y0=Inches(0.5),Inches(1.7); cw=Inches(3.0); rh=Inches(0.7)
    for i,(es,nl) in enumerate(data):
        c=i%4; r=i//4; x=x0+c*(cw+Inches(0.1)); y=y0+r*(rh+Inches(0.14))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.12),y,Inches(1.6),rh,[[(es,{"size":12,"bold":True,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(1.7),y,cw-Inches(1.8),rh,[[("→ "+nl,{"size":11,"color":G})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.9),
             [[("Combineer met perfecto compuesto: ", {"bold":True,"color":GD}),
               ("He viajado en tren · ha hecho sol · me he puesto el abrigo (hace frío).", {"color":GD})],
              [("Drie manieren voor het weer: hace (sol/frío) · un verbo (llueve/nieva) · está (nublado).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCAB transporte/clima. Klik onthult; koppel elk woord aan een perfecto-compuesto-zin. "
             "Volledige set + audio op de digitale pagina (flip cards + memoria).")

# ============================================================ DIA 15 · TALLER — tilde diacrítica
def s15_taller():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "TALLER DE LENGUA", "La tilde diacrítica + conectores", "Klik een item → correcte vorm. Zelfde letters, ander streepje = andere betekenis.", num=1)
    text(s, Inches(0.5), Inches(1.5), Inches(6), Inches(0.35), [[("A · tilde diacrítica: mismo sonido, tilde ≠ significado", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    fixes=[("¿(Tú/Tu) ___ has viajado?","Tú (persoon)"),("Este es (él/el) ___ tren","el (lidwoord)"),("¿(Qué/Que) ___ has visto?","Qué (vraag)"),("—¿Has comido? —(Sí/Si) ___","Sí (ja)")]
    y=Inches(1.95)
    for q,a in fixes:
        card(s,Inches(0.5),y,Inches(6.0),Inches(0.6),fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,Inches(0.62),y,Inches(3.6),Inches(0.6),[[(q,{"size":11.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,Inches(4.3),y,Inches(2.1),Inches(0.6),[[("→ "+a,{"size":11.5,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y=y+Inches(0.72)
    text(s, Inches(6.9), Inches(1.5), Inches(6), Inches(0.35), [[("B · conectores del relato", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    conn=[("___ , he cogido el tren","Primero"),("___ , he subido","Luego"),("___ , he sacado fotos","Después"),("___ , he vuelto","Al final")]
    y=Inches(1.95)
    for q,a in conn:
        card(s,Inches(6.9),y,Inches(5.9),Inches(0.6),fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,Inches(7.02),y,Inches(3.6),Inches(0.6),[[(q,{"size":11.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,Inches(10.7),y,Inches(2.0),Inches(0.6),[[("→ "+a,{"size":11.5,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y=y+Inches(0.72)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.85),
             [[("🔴 A: ", {"bold":True,"color":RED}), ("het streepje zit op het woord met de «sterkste» betekenis: persoon (tú, él), vraag (qué), ja (sí), meer (más).", {"color":GD})],
              [("B: ", {"bold":True,"color":GD}), ("primero → luego/después → al final (voor je reisverslag).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · TALLER. Tilde diacrítica = valstrik. Conectores = ideaal voor het reisdagboek. Meteen toepassen in de mini-tekst. "
             "Online: «tilde diacrítica» + «ordena el diario».")

# ============================================================ DIA 16 · CULTURE — Machu Picchu
def s16_cultura():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "CULTURA · PARADA 8", "Machu Picchu y el clima andino", "Klik een kaart → het weetje verschijnt. Perú: tres climas en un país.", num=1)
    cards=[("🏔️ Machu Picchu","La ciudad inca, a 2430 m. Se llega en tren desde Cusco y luego a pie. Una de las siete maravillas del mundo.","El símbolo de Perú."),
           ("🦙 Los Andes y las llamas","La sierra es alta y fría. Allí viven las llamas y las alpacas. En Cusco (3400 m) hace frío por la noche.","Cusco = capital inca."),
           ("🌦️ Los tres climas","Costa (sol, seco), sierra (frío, nieva) y selva (calor, llueve). ¡Tres climas en un día! Nina lleva abrigo y paraguas.","No comas a las 18:00… lleva paraguas.")]
    x0,y0=Inches(0.5),Inches(1.7); cw=Inches(4.05); ch=Inches(3.4)
    for i,(t,f,nl) in enumerate(cards):
        x=x0+i*(cw+Inches(0.13))
        card(s,x,y0,cw,ch,fill=WHITE,line=G,lw=1.3)
        rect(s,x,y0,cw,Inches(0.6),fill=GT)
        text(s,x+Inches(0.15),y0,cw-Inches(0.3),Inches(0.6),[[(t,{"size":13.5,"bold":True,"color":GD,"font":DISPLAY})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(0.2),y0+Inches(0.8),cw-Inches(0.4),Inches(1.9),[[(f,{"size":12,"color":INK})]],line=1.2)
        register_reveal(s, rev)
        text(s,x+Inches(0.2),y0+Inches(2.75),cw-Inches(0.4),Inches(0.6),[[(nl,{"size":10.5,"italic":True,"color":MUT})]],line=1.1)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.35), Inches(12.3), Inches(0.6),
             [[("Actividad: ", {"bold":True,"color":GD}), ("schrijf 3 zinnen over het weer waar jij woont in verschillende seizoenen (¿qué tiempo hace en verano/invierno?).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · CULTURE (identiteit in diversiteit, LPD 5). Onthul per kaart. Vergelijk de drie klimaatzones met België. Bruggetje naar de Tarea Mis vacaciones. "
             "Online: «país ↔ clima» (match) + de kaart van de Spaanstalige wereld.")

# ============================================================ DIA 17 · QUIZ — completa (perfecto)
def s17_quiz_completa():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · QUIZ · EL TIEMPO", "¿Qué tiempo hace?", "Wat past? Klik → het antwoord verschijnt.", num=4)
    items=[("___ sol (het is zonnig)","hace"),("___ nublado","está"),
           ("___ (het regent)","llueve"),("___ frío en Cusco","hace"),
           ("___ (het sneeuwt) en los Andes","nieva"),("___ a 20 grados","estamos")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(6.05); rh=Inches(0.78)
    for i,(ans,q) in enumerate(items):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(3.9),rh,[[(ans,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(4.1),y,cw-Inches(4.25),rh,[[("→ "+q,{"size":12.5,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Drie manieren: ", {"bold":True,"color":GD}),
               ("hace + sol/frío/calor · un verbo (llueve/nieva) · está nublado / hay tormenta. Temperatuur: estamos a … grados.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ el tiempo. Klas vult de zin vóór de klik. Daarna: het weerbericht van een verzonnen stad vertellen (spreken).")

# ============================================================ DIA 18 · FINAL_MISSION — Mis vacaciones
def s18_tarea():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(1.35), fill=GD)
    text(s, Inches(0.5), Inches(0.18), Inches(9), Inches(1.0),
         [[("🎒 Tarea final · Mis vacaciones", {"size":30,"bold":True,"color":WHITE,"font":DISPLAY})],
          [("Escribe (of graba en vlog) el diario de tus vacaciones con el perfecto compuesto.", {"size":13,"italic":True,"color":GT})]])
    avatar(s, "mochila", Inches(11.6), Inches(0.2), Inches(1.0))
    pasos=[("1","Elige un destino y el momento","echt of verzonnen"),
           ("2","Rellena la ficha","transporte · tiempo · 3 cosas que has hecho"),
           ("3","Escribe el diario (mín. 5 frases)","perfecto compuesto + marcadores + el tiempo"),
           ("4","Graba un vlog","of doe het in pareja"),
           ("5","Añade una foto/dibujo","con onderschrift («He visto…»)")]
    y=Inches(1.7)
    for n,es,nl in pasos:
        b=rect(s,Inches(0.5),y,Inches(0.5),Inches(0.5),fill=G,round=True,radius=0.5)
        tf=b.text_frame;tf.vertical_anchor=MSO_ANCHOR.MIDDLE;p=tf.paragraphs[0];p.alignment=PP_ALIGN.CENTER
        rr=p.add_run();rr.text=n;rr.font.size=Pt(15);rr.font.bold=True;rr.font.name=DISPLAY;rr.font.color.rgb=WHITE
        text(s,Inches(1.2),y,Inches(4.6),Inches(0.55),[[(es,{"size":14,"bold":True,"color":GD,"font":DISPLAY})]],anchor=MSO_ANCHOR.MIDDLE)
        text(s,Inches(5.9),y,Inches(6.8),Inches(0.55),[[(nl,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        y=y+Inches(0.62)
    text(s, Inches(0.5), Inches(5.0), Inches(12), Inches(0.35), [[("Rúbrica · ¿lo logré?", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    crit=["5× perfecto compuesto","participios correctos","el tiempo + transporte","marcadores/conectores"]
    x=Inches(0.5)
    for c in crit:
        chip(s,x,Inches(5.45),"☐ "+c,fill=GT,tcolor=GD,size=11,w=Inches(3.0)); x=x+Inches(3.1)
    text(s, Inches(0.5), Inches(6.05), Inches(12), Inches(0.4),
         [[("🎯 ", {"size":12}), ("Afzender jij (de reiziger) · ontvanger je familie/vrienden · doel je reis navertellen · situatie terug van vakantie · resultaat: reisverslag (of vlog) met perfecto compuesto.", {"size":11.5,"italic":True,"color":MUT})]])
    foot(s)
    notes(s, "TEACHER · FINAL_MISSION (communicatieve eindtaak). Afzender/ontvanger/doel/situatie/resultaat expliciet. Beoordeel met de rúbrica; "
             "opname + zelfevaluatie op de digitale pagina. Voeg een mini-encuesta + grafiekje toe (¿adónde ha viajado la clase?).")

# ============================================================ DIA 19 · QUIZ — la mezcla
def s19_mezcla():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "QUIZ · LA MEZCLA", "Ophaal door elkaar", "Gemengde ophaal van de hele unit. Klik een vraag → het antwoord. (retrieval)", num=1)
    items=[("haber, yo","he"),("haber, nosotros","hemos"),("participio de hacer","hecho"),
           ("participio de ver","visto"),("marcador «nog niet»","todavía no"),("¿qué ___ hecho? (tú)","has"),
           ("weer: ___ sol","hace"),("participio de escribir","escrito")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(6.05); rh=Inches(0.62)
    for i,(q,a) in enumerate(items):
        c=i//4; r=i%4; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.16))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(3.6),rh,[[(q,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(3.75),y,cw-Inches(3.9),rh,[[("→ "+a,{"size":12,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.05), Inches(12.3), Inches(0.55),
             [[("Alles komt terug: ", {"bold":True,"color":GD}), ("haber · participios (reg/irreg) · marcadores · el tiempo.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ mezcla (retrieval vóór herlezen). Zonder waarschuwing door elkaar. Exit-ticket. Zwakke punten → terug via menu.")

# ============================================================ DIA 20 · FEEDBACK/REPASO
def s20_repaso():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "REPASO · LO ESENCIAL", "Lo esencial de un vistazo", "De volledige herhaling (18 spellen, drills) staat online. Hier: de kern + semáforo.", num=1)
    ess=["Perfecto compuesto: haber (he, has, ha, hemos, habéis, han) + participio: «He viajado. ¿Has visto?».",
         "Participios: -ar → -ado · -er/-ir → -ido. Irregular: hecho, visto, dicho, escrito, vuelto, puesto, abierto, roto.",
         "Marcadores: hoy · esta semana · este año (periode) · ya ↔ todavía no · alguna vez · nunca · muchas veces (ervaring).",
         "El tiempo: hace sol/calor/frío/viento · llueve · nieva · está nublado · estamos a … grados.",
         "🔴 Trampas: haber ≠ tener (has hecho) · participio blijft gelijk (ha comidO) · tilde diacrítica (tú/tu · qué/que)."]
    card(s, Inches(0.5), Inches(1.6), Inches(12.3), Inches(2.5), fill=CREMA, line=None)
    y=Inches(1.8)
    for e in ess:
        text(s, Inches(0.8), y, Inches(11.8), Inches(0.45), [[("• ", {"size":13,"bold":True,"color":GD}),(e,{"size":12,"color":INK})]])
        y=y+Inches(0.46)
    text(s, Inches(0.5), Inches(4.3), Inches(12), Inches(0.35), [[("Semáforo — ¿cómo lo llevas?", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    can=["contar qué has hecho (perfecto)","participios (reg + irreg)","marcadores (ya/todavía no/nunca)","hablar del tiempo","viajes/transporte benoemen"]
    y=Inches(4.75)
    for c in can:
        text(s,Inches(0.8),y,Inches(7.0),Inches(0.4),[[(c,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        for j,(em,col) in enumerate([("🔴",RED),("🟠",AMBER),("🟢",G)]):
            chip(s,Inches(8.0)+j*Inches(1.5),y+Inches(0.03),em+" ",fill=WHITE,tcolor=col,size=12,w=Inches(1.3))
        y=y+Inches(0.42)
    foot(s)
    notes(s, "TEACHER · FEEDBACK/REPASO. Semáforo = zelfevaluatie. Repaso-drills online (18 spellen). Fin del viaje de 5º; bruggetje: C6 «Historias y mundos» — "
             "el viaje continúa hacia el pasado (indefinido/imperfecto, biografías).")

# ============================================================ DIA 21 · TEACHER_NOTES
def s21_teacher():
    s = slide(); bg(s, GD)
    text(s, Inches(0.6), Inches(0.4), Inches(12), Inches(0.8), [[("TEACHER_NOTES · U8 «¿Qué has hecho?»", {"size":26,"bold":True,"color":WHITE,"font":DISPLAY})]])
    blocks=[("Timing (50 min)","Menu 2' · perfecto compuesto 10' · participios 8' · marcadores 6' · el tiempo 6' · lectura/escucha 8' · cultura 3' · Tarea-briefing 3' · repaso 4'."),
            ("Kernvalstrikken","haber ≠ tener (has hecho, niet tienes hecho) · participio blijft gelijk (ha comidO) · irregulares (hecho/visto/dicho/escrito/vuelto/puesto/abierto/roto) · hace calor ≠ es caliente · tilde diacrítica (tú/tu · qué/que · sí/si · más/mas)."),
            ("Differentiatie (zij-instromers)","Alles start vanaf nul. Sterker: volledig reisverslag met marcadores + het weer + irregulares. Zwakker: haber-tabel + participio-lijst langer open, zinsframes houden."),
            ("Digitaal","18 spellen + flip cards + klikbare kaart + recorder (Hablar) + Lectura (diario de Nina) op de página digital. QR's in het boek → juiste anker. Conjugador = aparte tool (enkel presente)."),
            ("Evaluatie","Tarea «Mis vacaciones» met rúbrica (4 criteria). LPD 3·4·7·8 + 5 (cultura) + 1·2 (receptief: lezen/luisteren). Scope: perfecto compuesto = A2-eindstructuur jaar 5 (géén indefinido/imperfecto/futuro/subjuntivo).")]
    y=Inches(1.4)
    for t,b in blocks:
        card(s, Inches(0.5), y, Inches(12.3), Inches(1.0), fill=RGBColor(0x1B,0x63,0x49), line=None)
        text(s, Inches(0.75), y+Inches(0.08), Inches(11.8), Inches(0.4), [[(t, {"size":14,"bold":True,"color":WHITE,"font":DISPLAY})]])
        text(s, Inches(0.75), y+Inches(0.48), Inches(11.8), Inches(0.5), [[(b, {"size":11,"color":GT})]], line=1.1)
        y=y+Inches(1.12)
    footer(s, tab=TAB, page=pg())
    notes(s, "Alleen in het docentdeck. Volledige LPD-dekking en didactische route staan in het cursusdossier (U8_cocktail.md).")

# ============================================================ RUN + BUILD
def _run_all(include_teacher=True):
    s01_title(); s02_menu(); s03_vocab(); s04_perfecto(); s05_perfecto_quiz(); s06_participios(); s07_marcadores()
    s08_quiz_participio(); s09_reading(); s10_listening(); s11_ya(); s12_speaking(); s13_writing()
    s14_transporte(); s15_taller(); s16_cultura(); s17_quiz_completa(); s18_tarea(); s19_mezcla(); s20_repaso()
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
