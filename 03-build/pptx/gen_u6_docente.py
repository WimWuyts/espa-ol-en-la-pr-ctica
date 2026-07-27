#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_u6_docente.py — Interactieve PowerPoint C5 · Unidad 6 «De tiendas» (parada México/mercados)
================================================================================================
Zelfde engine/pijplijn als de golden sample (gen_u0_docente wordt geïmporteerd: low-level helpers,
on-click <p:timing>-animaties, hyperlink-navigatie). Enkel de SLIDES zijn U6-specifiek. Twee decks (beide .pptx):
  · C5_U6_docente.pptx — vrije navigatie, oplossingen bij klik + didactiek in spreker-notities.
  · C5_U6_alumno.pptx  — gewone diavoorstelling, antwoorden verschijnen bij klik (F5, geen kiosk).
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
OUT_DOCENTE = os.path.join(HERE, "C5_U6_docente.pptx")
OUT_ALUMNO_PPTX = os.path.join(HERE, "C5_U6_alumno.pptx")
TAB = "U6 · DE TIENDAS"

def foot(s): footer(s, tab=TAB, page=pg())

# ============================================================ DIA 1 · TITLE
def s01_title():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(4.7), fill=G)
    rect(s, 0, Inches(4.7), EMU_W, Inches(0.09), fill=GD)
    text(s, Inches(0.6), Inches(0.35), Inches(3.4), Inches(3.6),
         [[("6", {"size": 260, "bold": True, "color": RGBColor(0x2E,0xB0,0x85), "font": DISPLAY})]],
         anchor=MSO_ANCHOR.MIDDLE)
    chip(s, Inches(4.35), Inches(0.85), "LA RUTA · PARADA 6 · MÉXICO · LOS MERCADOS 🇲🇽", fill=WHITE, tcolor=GD, size=12)
    text(s, Inches(4.3), Inches(1.35), Inches(8.6), Inches(1.5),
         [[("De tiendas", {"size": 66, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(4.35), Inches(2.7), Inches(8.4), Inches(0.6),
         [[("La ropa y los colores: lo/la/los/las, acabar de, este/ese/aquel y la concordancia — de compras con Diego.", {"size": 14, "italic": True, "color": GT})]])
    text(s, Inches(4.35), Inches(3.35), Inches(8.4), Inches(0.9),
         [[("¿Qué te vas a comprar hoy?", {"size": 24, "bold": True, "color": WHITE, "font": DISPLAY})],
          [("Wat ga je vandaag kopen?", {"size": 13, "italic": True, "color": GT})]])
    text(s, Inches(0.6), Inches(4.95), Inches(6), Inches(0.4),
         [[("La gente de la ruta — je reisgezellen", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    x = Inches(0.6)
    for nm, city in [("diego","México 🇲🇽 · anfitrión"),("lucia","Sevilla 🇪🇸"),("valen","Cartagena 🇨🇴"),
                     ("nina","Cusco 🇵🇪"),("tu","Tú · Flandes 🇧🇪"),("mochila","La mochila")]:
        avatar(s, nm, x, Inches(5.4), Inches(1.0))
        text(s, x - Inches(0.15), Inches(6.42), Inches(1.3), Inches(0.5),
             [[(nm.capitalize() if nm!="tu" else "Tú", {"size": 10.5, "bold": True, "color": INK})],
              [(city.split("·")[-1].strip() if nm!="tu" else "de reiziger = jij", {"size": 8.5, "color": MUT})]],
             align=PP_ALIGN.CENTER)
        x = x + Inches(2.05)
    foot(s)
    notes(s, "TEACHER · TITLE. Parada 6 = México, los mercados y tianguis. Gastheer = Diego. Doel: ropa/colores benoemen, "
             "OD-pronombres lo/la/los/las (¿la falda? → la compro), acabar de + infinitivo (net gedaan), demostrativos este/ese/aquel (afstand), "
             "en de concordancia van het adjectief (camiseta roja · de rayas). Kernvalstrik: la compro (niet «compro la»); una falda azul (niet «azula»); "
             "acabo DE comprar. Docentdeck = vrije navigatie + oplossing in notities; leerlingdeck (.pptx, F5) = elke klik onthult het volgende antwoord.")

# ============================================================ DIA 2 · LESSON_MENU
def s02_menu():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "MENÚ DE LA LECCIÓN", "El mapa de la Unidad 6",
               "Kies je route — klik een tegel. Alles oefent naar de Tarea «Abre tu tienda» toe.", num=6)
    tiles = [
        ("§1", "lo/la/los/las", "¿la falda? → la compro", G, 4),
        ("§2", "Acabar de + inf.", "net iets gedaan", G, 6),
        ("§3", "este/ese/aquel", "cerca ↔ lejos", G, 7),
        ("§4", "Concordancia", "camiseta roja de rayas", G, 11),
        ("§5", "Lectura + escucha", "¡rebajas! + reseña", G, 9),
        ("★", "Cultura · compras", "rebajas · regateo · tianguis", GD, 16),
        ("🛍️", "Tarea · tu tienda", "escaparate + diálogo", GD, 18),
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
             "Begin bij §1 (lo/la/los/las) → §4 (concordancia) = het hart van de unit. Kruisverwijzing print/HTML: «oefen online — 20 juegos».")

# ============================================================ DIA 3 · VOCABULARY — la ropa
def s03_vocab():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§V · VOCABULARIO", "La ropa y los complementos", "De woorden van de kast — observa. Herken ze, dan gebruik je ze.", num=6)
    legend_func(s, Inches(9.7), Inches(0.55))
    rows = [("la camiseta","het T-shirt","👕 arriba"),("los pantalones","de broek","👖 abajo"),
            ("el vestido","de jurk","👗"),("la falda","de rok","👗 abajo"),
            ("los zapatos","de schoenen","👞 calzado"),("las zapatillas","de sportschoenen","👟"),
            ("la gorra","de pet","🧢 complemento"),("el bolso","de handtas","👜")]
    x0,y0 = Inches(0.5), Inches(1.6); cw=Inches(6.1); rh=Inches(0.6)
    for i,(k,v,nl) in enumerate(rows):
        c = 0 if i<4 else 1; r = i%4
        x = x0 + c*(cw+Inches(0.15)); y = y0 + r*(rh+Inches(0.12))
        card(s, x, y, cw, rh, fill=WHITE, line=LINE, lw=1.0, shadow=False)
        text(s, x+Inches(0.15), y, Inches(2.4), rh, [[(k, {"size":13,"bold":True,"color":GD})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x+Inches(2.5), y, Inches(2.3), rh, [[(v, {"size":12,"color":INK})]], anchor=MSO_ANCHOR.MIDDLE)
        text(s, x+Inches(4.6), y, Inches(1.4), rh, [[(nl, {"size":9,"italic":True,"color":MUT})]], anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(4.75), Inches(12.3), Inches(0.5),
         [[("Colores: ", {"size":13,"bold":True,"color":GD,"font":DISPLAY}),
           ("rojo/roja", {"size":13,"bold":True,"color":F_OBJ}), (" · ",{"size":13,"color":INK}),
           ("azul · gris · verde", {"size":13,"bold":True,"color":F_OBJ}), (" · ",{"size":13,"color":INK}),
           ("patrón: de rayas · de cuadros · de lunares", {"size":13,"bold":True,"color":F_PLAC})]])
    btn = noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.35), Inches(12.3), Inches(0.95),
             [[("🔴 Concordancia: ", {"bold":True,"color":RED}), ("camiseta rojA · zapatos rojOS · vestido rojO · botas rojAS.", {"bold":True,"color":GD})],
              [("Kleuren op -o veranderen; azul/gris/verde/marrón niet (enkel meervoud +s/+es).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCABULARY. Toon per cluster (arriba/abajo/calzado/complemento). Laat raden zónder de NL-gloss. "
             "Online: flip cards + Memoria de la ropa + ¿arriba, abajo, calzado o complemento?")

# ============================================================ DIA 4 · GRAMMAR — lo/la/los/las (color)
def s04_od():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · GRAMÁTICA VISUAL", "lo / la / los / las — vervang de prenda", "Kleur = het pronomen. Het staat vóór het vervoegde werkwoord.", num=1)
    legend_func(s, Inches(9.7), Inches(0.55))
    seg = [("¿La camisa? ", INK),("— Sí, ", INK),("la ", F_OBJ),("compro.", F_VERB),
           ("   ¿Los zapatos? — ", INK),("Los ", F_OBJ),("quiero.", F_VERB)]
    runs=[[(t,{"size":22,"bold":True,"color":c,"font":DISPLAY}) for t,c in seg]]
    card(s, Inches(0.5), Inches(1.7), Inches(12.3), Inches(1.2), fill=GT, line=None)
    text(s, Inches(0.8), Inches(1.7), Inches(11.7), Inches(1.2), runs, anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(3.15), Inches(12), Inches(0.4), [[("La concordancia — ¿qué pronombre?", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    frame=[("lo","m. ev. (el jersey)"),("la","v. ev. (la falda)"),("los","m. mv. (los zapatos)"),
           ("las","v. mv. (las botas)"),("vóór","el ww: la compro"),("achter","de infinitief: comprarla")]
    x0,y0=Inches(0.5),Inches(3.6); cw=Inches(4.0); rh=Inches(0.62)
    for i,(a,b) in enumerate(frame):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.12))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(1.7),rh,[[(a,{"size":12.5,"bold":True,"color":F_OBJ})]],anchor=MSO_ANCHOR.MIDDLE)
        text(s,x+Inches(1.85),y,cw-Inches(2.0),rh,[[(b,{"size":11,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.7), Inches(12.3), Inches(0.7),
             [[("Regla: ", {"bold":True,"color":GD}), ("lo/la/los/las vervangt de prenda en staat vóór het vervoegde ww (la compro) of vast achter de infinitief (comprarla).", {"color":GD})]],
             trigger=btn, title_doc="REGLA · docent")
    foot(s)
    notes(s, "TEACHER · GRAMMAR (color-coding). Maak de plaatsing fysiek zichtbaar. Truc: geslacht + aantal van de prenda → lo/la/los/las. "
             "Online: «¿lo, la, los o las?» (classify + cloze).")

# ============================================================ DIA 5 · QUIZ — lo/la/los/las
def s05_od_quiz():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · QUIZ", "¿lo, la, los o las?", "Klik een prenda → het juiste pronomen verschijnt. Kijk naar m/v en ev/mv.", num=1)
    items=[("la falda","la","v. ev."),("el jersey","lo","m. ev."),
           ("los zapatos","los","m. mv."),("las botas","las","v. mv."),
           ("el abrigo","lo","m. ev."),("las gafas","las","v. mv.")]
    x0,y0=Inches(0.5),Inches(1.7); cw=Inches(6.05); rh=Inches(0.7)
    for i,(q,ans,cat) in enumerate(items):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(3.6),rh,[[("¿"+q+"? → ___ compro",{"size":12.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(3.8),y,cw-Inches(3.9),rh,
                 [[(ans+" ",{"size":14,"bold":True,"color":GD}),("· "+cat,{"size":10,"italic":True,"color":G})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.95),
             [[("lo/la = ", {"bold":True,"color":G}), ("enkelvoud (m/v) · ", {"color":GD}),
               ("los/las = ", {"bold":True,"color":G}), ("meervoud (m/v). Kijk naar het lidwoord: el/la · los/las. Vóór het werkwoord!", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ (reveal). Laat de klas eerst kiezen, klik dan. Online: «lo-la-los-las» (classify) + cloze.")

# ============================================================ DIA 6 · GRAMMAR — acabar de + infinitivo (reveal)
def s06_acabar():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · GRAMÁTICA", "Acabar de + infinitivo — net gedaan", "Klik een kaart → de vorm verschijnt. Fórmula: acabar (presente) + de + infinitivo.", num=2)
    text(s, Inches(0.5), Inches(1.5), Inches(12.3), Inches(0.5),
         [[("La fórmula: ", {"size":14,"color":INK}),
           ("acabar (acabo, acabas, acaba…) ", {"size":14,"bold":True,"color":F_VERB}),
           ("+ de + ", {"size":14,"bold":True,"color":F_TIME}),
           ("infinitivo", {"size":14,"bold":True,"color":F_OBJ}),
           ("   →   Acabo de comprar una gorra.", {"size":14,"color":INK})]])
    pers=["yo","tú","él/ella","nosotros","vosotros","ellos"]
    forms=["acabo","acabas","acaba","acabamos","acabáis","acaban"]
    x0,y0=Inches(1.6),Inches(2.2); cw=Inches(3.4); ch=Inches(1.1)
    for i,(p,f) in enumerate(zip(pers,forms)):
        c=i%3; r=i//3; x=x0+c*(cw+Inches(0.3)); y=y0+r*(ch+Inches(0.25))
        card(s,x,y,cw,ch,fill=WHITE,line=G,lw=1.4)
        text(s,x,y+Inches(0.12),cw,Inches(0.35),[[(p,{"size":12,"color":MUT})]],align=PP_ALIGN.CENTER)
        rev=text(s,x,y+Inches(0.48),cw,Inches(0.55),[[(f+" de…",{"size":19,"bold":True,"color":GD,"font":DISPLAY})]],align=PP_ALIGN.CENTER)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.6), Inches(12.3), Inches(0.75),
             [[("🔴 Vergeet de «de» niet: ", {"bold":True,"color":RED}),
               ("acabo DE comprar. 🔴 Het tweede werkwoord blijft infinitief: ", {"color":GD}),
               ("acabo de COMPRAR", {"bold":True,"color":GD}), (". Betekenis: net (zopas) gedaan.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR acabar de + inf. Onthul per kaart; laat de vorm voorspellen. Twee delen: acabar (vervoegd) + de + infinitief. "
             "Niet verwarren met acabar = eindigen. Online: «acabar de + infinitivo» (cloze).")

# ============================================================ DIA 7 · GRAMMAR — este/ese/aquel (reveal)
def s07_demos():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · GRAMÁTICA", "Este / ese / aquel — cerca ↔ lejos", "Klik een afstand → de vorm verschijnt. Cerca=este · ahí=ese · lejos=aquel.", num=3)
    items=[("👉 aquí (cerca)","este / esta",G),("estos / estas","+ mv.",AMBER),
           ("👉👉 ahí","ese / esa",G),("esos / esas","+ mv.",AMBER),
           ("👉👉👉 allí (lejos)","aquel / aquella",G),("aquellos / aquellas","+ mv.",AMBER)]
    x0,y0=Inches(0.5),Inches(1.8); cw=Inches(6.05); ch=Inches(1.0)
    for i,(lab,txt,col) in enumerate(items):
        c=i%2; r=i//2; x=x0+c*(cw+Inches(0.2)); y=y0+r*(ch+Inches(0.18))
        card(s,x,y,cw,ch,fill=WHITE,line=col,lw=1.4)
        chip(s,x+Inches(0.2),y+Inches(0.12),lab,fill=GT,tcolor=GD,size=11)
        rev=text(s,x+Inches(0.2),y+Inches(0.5),cw-Inches(0.4),Inches(0.45),[[(txt,{"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
        register_reveal(s, rev)
    text(s, Inches(0.5), Inches(5.55), Inches(12.3), Inches(0.5),
         [[("🔴 Concuerda con la prenda: ", {"size":12,"bold":True,"color":RED}), ("estA falda (v) · estOS pantalones (m mv). Kijk naar het kledingstuk!", {"size":12,"color":INK})]])
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(6.1), Inches(12.3), Inches(0.55),
             [[("Afstand: ", {"bold":True,"color":GD}), ("este (aquí, in mijn hand) · ese (ahí, bij jou) · aquel (allí, in het escaparate).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR demostrativos. Fysiek maken: wijs voorwerpen aan op verschillende afstanden. Onthul per klik. "
             "Online: «cerca/ahí/lejos» (classify) + «este/ese/aquel» (cloze).")

# ============================================================ DIA 8 · QUIZ — este/ese/aquel
def s08_quiz_demos():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · QUIZ", "¿este, ese o aquel?", "Klik een zin → de juiste vorm verschijnt.", num=3)
    items=[("Me gusta ___ camiseta (aquí).","esta"),("¿Cuánto cuesta ___ gorra (ahí)?","esa"),
           ("___ abrigo (allí) es caro.","Aquel"),("___ zapatos (aquí) son cómodos.","estos"),
           ("Prefiero ___ vestido (ahí).","ese"),("___ botas (allí) son de cuero.","Aquellas")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(6.05); rh=Inches(0.78)
    for i,(q,a) in enumerate(items):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(4.0),rh,[[(q,{"size":11.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(4.2),y,cw-Inches(4.3),rh,[[("→ "+a,{"size":13,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("Cerca = este/esta/estos/estas · ahí = ese/esa… · lejos = aquel/aquella… ", {"bold":True,"color":GD}),
               ("Concuerda met de prenda (m/v · ev/mv).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ demostrativos (retrieval). Klas roept vóór de klik. Daarna in parejas: prendas aanwijzen en prijs vragen.")

# ============================================================ DIA 9 · READING — anuncio + reseña
def s09_reading():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§5 · LEER · COMPRENSIÓN", "¡Rebajas! + una reseña", "Lees en beantwoord. Klik een vraag → het antwoord verschijnt.", num=5)
    card(s, Inches(0.5), Inches(1.65), Inches(5.6), Inches(3.9), fill=GT, line=G, lw=1.4)
    avatar(s, "valen", Inches(0.85), Inches(1.95), Inches(1.1))
    text(s, Inches(2.1), Inches(2.0), Inches(3.8), Inches(1.5),
         [[("📣 Moda Diego · ¡−50 %! Camisetas 10→5 €, vaqueros 40→25 €, zapatillas 60→39 €. "
            "⭐ @valen: «Acabo de comprar unos vaqueros azules (25 €). Me los probé y me quedan bien. Pagué con tarjeta.»",{"size":12,"italic":True,"color":INK})]], line=1.2)
    qa=[("¿Cuánto cuestan los vaqueros en rebajas?","25 € (antes 40)"),("¿Qué compró Valen?","unos vaqueros azules"),
        ("¿Cómo pagó?","con tarjeta"),("¿Se probó la ropa? ¿Dónde?","Sí, en el probador")]
    x=Inches(6.4); y=Inches(1.7)
    for q,a in qa:
        card(s,x,y,Inches(6.4),Inches(0.85),fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y+Inches(0.06),Inches(6.1),Inches(0.4),[[(q,{"size":12.5,"bold":True,"color":GD})]])
        rev=text(s,x+Inches(0.15),y+Inches(0.44),Inches(6.1),Inches(0.35),[[("→ "+a,{"size":12,"color":INK})]])
        register_reveal(s, rev)
        y=y+Inches(0.98)
    btn=noodroute(s)
    exercise_solucion(s, Inches(6.4), Inches(5.65), Inches(6.4), Inches(0.6),
             [[("🎯 Leesdoel: ", {"bold":True,"color":GD}), ("scannen naar precios/descuentos en wat de klant wel/niet kocht — niet élk woord.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · READING (lezen→schrijven-keten). Eerst globaal (waarover?), dan scannen. Onthul de antwoorden pas na de klas. "
             "Daarna: leerlingen schrijven hun eigen reseña (transfer → Tarea Abre tu tienda).")

# ============================================================ DIA 10 · LISTENING — en la tienda
def s10_listening():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · ESCUCHAR", "Escucha en la tienda", "Vier clientes compran. Klik un nombre → wat ze kopen. (audio op de digitale pagina)", num=1)
    people=[("Leo","una camisa azul","talla M"),("Frida","unos vaqueros","25 €"),
            ("Mateo","unas zapatillas","talla 42"),("Sara","un vestido rojo","de lunares")]
    x0,y0=Inches(0.7),Inches(1.9); cw=Inches(2.95); ch=Inches(2.4)
    for i,(nm,com,beb) in enumerate(people):
        x=x0+i*(cw+Inches(0.1))
        card(s,x,y0,cw,ch,fill=WHITE,line=LINE,lw=1.2)
        rect(s,x,y0,cw,Inches(0.5),fill=GT)
        text(s,x,y0,cw,Inches(0.5),[[("🔊  "+nm,{"size":14,"bold":True,"color":GD,"font":DISPLAY})]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        text(s,x+Inches(0.15),y0+Inches(0.65),cw-Inches(0.3),Inches(0.4),[[("Compra:",{"size":12,"color":MUT})]])
        rev1=text(s,x+Inches(0.15),y0+Inches(1.0),cw-Inches(0.3),Inches(0.5),[[(com,{"size":13,"bold":True,"color":INK})]],line=1.05)
        text(s,x+Inches(0.15),y0+Inches(1.6),cw-Inches(0.3),Inches(0.4),[[("Detalle:",{"size":12,"color":MUT})]])
        rev2=text(s,x+Inches(0.15),y0+Inches(1.95),cw-Inches(0.3),Inches(0.4),[[(beb,{"size":13,"bold":True,"color":G})]])
        register_reveal(s, rev1); register_reveal(s, rev2)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.85),
             [[("Modelo-audio (docent leest of TTS): ", {"bold":True,"color":GD}),
               ("«Busco una camisa azul en talla M. ¿Puedo probármela?» …", {"color":GD})],
              [("Daarna spreken: leerling speelt de cliente en koopt zelf.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · LISTENING (selectief → spreken). Lees elk pedido voor (of TTS). Klas noteert prenda + detalle; onthul per klik. "
             "Koppel meteen aan de rollenspel-scène (§1).")

# ============================================================ DIA 11 · GRAMMAR — concordancia (reveal)
def s11_concord():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · GRAMÁTICA", "Concordancia — camiseta roja de rayas", "Klik een prenda → de juiste kleurvorm verschijnt. Kleur past bij de prenda (m/v · ev/mv).", num=4)
    R=[("un vestido (rojo)","rojo"),("una camiseta (rojo)","roja"),("unos zapatos (rojo)","rojos"),
       ("unas botas (rojo)","rojas"),("una falda (azul)","azul"),("unos vaqueros (azul)","azules")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(3.95); ch=Inches(1.25)
    for i,(p,v) in enumerate(R):
        c=i%3; r=i//3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(ch+Inches(0.2))
        card(s,x,y,cw,ch,fill=WHITE,line=G,lw=1.4)
        text(s,x,y+Inches(0.12),cw,Inches(0.4),[[(p,{"size":12,"color":MUT})]],align=PP_ALIGN.CENTER)
        rev=text(s,x,y+Inches(0.5),cw,Inches(0.6),[[("→ "+v,{"size":24,"bold":True,"color":GD,"font":DISPLAY})]],align=PP_ALIGN.CENTER)
        register_reveal(s, rev)
    text(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.5),
         [[("🟡 Dos tipos: ", {"size":12,"color":INK}),
           ("rojo/roja/rojos/rojas (verandert) · azul/gris/verde (enkel meervoud +s/+es).", {"size":12,"bold":True,"color":GD})]])
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.75), Inches(12.3), Inches(0.65),
             [[("Regla: ", {"bold":True,"color":GD}),
               ("het adjectief komt overeen in geslacht (m/v) en getal (ev/mv). Patronen met «de» (de rayas, de cuadros) veranderen niet.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR concordancia (reveal). Coro: klas zegt de vorm vóór de klik. Kernidee: kijk naar de prenda. "
             "Online: «color + prenda» (match) + concordancia-Tetris + «masculino/femenino».")

# ============================================================ DIA 12 · SPEAKING — de compras / regateo
def s12_speaking():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · SPEAKING · INTERACCIÓN", "¡Vas de compras! (regateo)", "Speel de scène met de zinnen. Steun bouwt af: kaarten → beginwoorden → uit het hoofd.", num=4)
    avatar(s, "tu", Inches(11.4), Inches(1.7), Inches(1.3))
    labels=["Saludar","Buscar","Probar","Precio","Regatear","Cerrar"]
    frames=["¿Qué desea?","Busco una…","¿Puedo probármelo?","¿Cuánto cuesta?","¿Me hace un descuento?","Me lo llevo."]
    x0,y0=Inches(0.5),Inches(1.8); cw=Inches(3.4); rh=Inches(0.8)
    for i,(lab,fr) in enumerate(zip(labels,frames)):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=G,lw=1.2,shadow=False)
        text(s,x+Inches(0.15),y+Inches(0.05),cw-Inches(0.3),Inches(0.32),[[(lab,{"size":10,"color":MUT})]])
        text(s,x+Inches(0.15),y+Inches(0.36),cw-Inches(0.3),Inches(0.4),[[(fr,{"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    text(s, Inches(0.5), Inches(5.0), Inches(10.5), Inches(0.9),
         [[("Ronda 1: ", {"size":12,"bold":True,"color":GD}), ("met de kaarten. ", {"size":12,"color":INK}),
           ("Ronda 2: ", {"size":12,"bold":True,"color":GD}), ("alleen beginwoorden. ", {"size":12,"color":INK}),
           ("Ronda 3: ", {"size":12,"bold":True,"color":GD}), ("uit het hoofd, andere prenda. ", {"size":12,"color":INK}),
           ("Ronda 4: ", {"size":12,"bold":True,"color":GD}), ("grábate en de digitale pagina.", {"size":12,"color":INK})]])
    chip(s, Inches(0.5), Inches(4.65), "🎙️ Grábate online · «Mensaje de voz: regatea»", fill=GT, tcolor=GD, size=11)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.6), Inches(12.3), Inches(0.65),
             [[("Modelo: ", {"bold":True,"color":GD}), ("«Busco una camisa azul. ¿Puedo probármela? … ¿Cuánto cuesta? Es un poco caro, ¿me hace un descuento? … Me la llevo.»", {"color":GD})]],
             trigger=btn, title_doc="MODELO · docent")
    foot(s)
    notes(s, "TEACHER · SPEAKING (interactie). Automatiseer saludar→buscar→probar→precio→regatear in rondes met afbouwende steun. "
             "Online: recorder (opname + zelfevaluatie). Print blijft bruikbaar zonder opname. NB: regatear enkel op de markt/tianguis.")

# ============================================================ DIA 13 · WRITING — mi escaparate
def s13_writing():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "WRITING · PRODUCCIÓN", "Mi escaparate (tienda)", "Ontwerp je etalage. Klik → een modeltekst verschijnt.", num=1)
    card(s, Inches(0.5), Inches(1.7), Inches(6.0), Inches(3.9), fill=WHITE, line=LINE, lw=1.2)
    text(s, Inches(0.7), Inches(1.85), Inches(5.6), Inches(0.4), [[("✍️ Escribe aquí tu escaparate:", {"size":12,"bold":True,"color":GD})]])
    for i in range(6):
        rect(s, Inches(0.7), Inches(2.4)+i*Inches(0.5), Inches(5.6), Inches(0.01), fill=LINE)
    chk=[("4 prendas + color/patrón + precio",),("concordancia correcta (roja/azules)",),("un anuncio de rebajas (antes→ahora)",),("diálogo: este/ese/aquel + lo/la",),("acabar de (net gekocht)",),("una reseña de tu compañero/a",)]
    x=Inches(6.9); y=Inches(1.7)
    text(s,x,y,Inches(6),Inches(0.4),[[("Checklist:",{"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    for i,(c,) in enumerate(chk):
        text(s,x,y+Inches(0.5)+i*Inches(0.45),Inches(6),Inches(0.4),[[("☐  "+c,{"size":13,"color":INK})]])
    rev=card(s, x, Inches(4.35), Inches(6.0), Inches(1.25), fill=GT, line=G, lw=1.2)
    text(s, x+Inches(0.15), Inches(4.4), Inches(5.7), Inches(1.2),
         [[("Modelo: ", {"size":12,"bold":True,"color":GD}),
           ("«Moda Diego. Camiseta roja de rayas (5 €). Vaqueros azules (25 €). Vestido de lunares (20 €). Zapatillas blancas (39 €). ¡Grandes rebajas −50 %!»",{"size":12,"italic":True,"color":INK})]], line=1.15)
    register_reveal(s, rev)
    noodroute(s); foot(s)
    notes(s, "TEACHER · WRITING (lezen→schrijven). Checklist = zichtbare steun; onthul het model pas na het schrijven (retrieval). "
             "Nakijkfocus: concordancia, precios, anuncio. Dit voedt de Tarea «Abre tu tienda».")

# ============================================================ DIA 14 · VOCAB — colores/tiendas (reveal)
def s14_colores_tiendas():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§V · VOCABULARIO · MERCADO", "Colores y tiendas", "Klik een woord → de vertaling verschijnt. Bouw je woordnetwerk.", num=6)
    data=[("rojo","rood"),("azul","blauw"),("verde","groen"),("negro","zwart"),
          ("la zapatería","schoenwinkel"),("la panadería","bakkerij"),("el mercado","markt"),("las rebajas","solden"),
          ("la talla","de maat"),("el probador","paskamer"),("la caja","de kassa"),("el descuento","de korting")]
    x0,y0=Inches(0.5),Inches(1.7); cw=Inches(3.0); rh=Inches(0.7)
    for i,(es,nl) in enumerate(data):
        c=i%4; r=i//4; x=x0+c*(cw+Inches(0.1)); y=y0+r*(rh+Inches(0.14))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.12),y,Inches(1.7),rh,[[(es,{"size":12,"bold":True,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(1.7),y,cw-Inches(1.8),rh,[[("→ "+nl,{"size":11.5,"color":G})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.9),
             [[("Combineer prenda + color: ", {"bold":True,"color":GD}),
               ("una camiseta roja · unos vaqueros azules · una gorra verde. Comprar en la zapatería, la panadería, el mercado.", {"color":GD})],
              [("En la tienda: la talla, el probador, la caja, las rebajas, el descuento.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCAB colores/tiendas. Klik onthult; koppel elk woord aan een concordancia-zin. Volledige set + audio op de digitale pagina "
             "(flip cards + memoria).")

# ============================================================ DIA 15 · TALLER — sílaba tónica + conectores
def s15_taller():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "TALLER DE LENGUA", "Sílaba tónica + conectores", "Klik een item → correcte vorm. Gereedschap voor klemtoon en verbindingswoorden.", num=6)
    text(s, Inches(0.5), Inches(1.5), Inches(6), Inches(0.35), [[("A · sílaba tónica: aguda · llana · esdrújula", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    fixes=[("panta-lón","aguda (laatste)"),("fal-da","llana (voorlaatste)"),("sá-ba-do","esdrújula (tilde)"),("el pantalón → los…","pantalones (tilde weg)")]
    y=Inches(1.95)
    for q,a in fixes:
        card(s,Inches(0.5),y,Inches(6.0),Inches(0.6),fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,Inches(0.62),y,Inches(3.2),Inches(0.6),[[(q,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,Inches(3.9),y,Inches(2.4),Inches(0.6),[[("→ "+a,{"size":11,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y=y+Inches(0.72)
    text(s, Inches(6.9), Inches(1.5), Inches(6), Inches(0.35), [[("B · conectores: y→e · o→u · pero/sino · así que", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    conn=[("madre ___ hija","e","vóór i-/hi-"),("siete ___ ocho","u","vóór o-/ho-"),("No es azul, ___ verde","sino","na ontkenning"),("Hay rebajas, ___ compro","así que","dus")]
    y=Inches(1.95)
    for q,a,gl in conn:
        card(s,Inches(6.9),y,Inches(5.9),Inches(0.6),fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,Inches(7.02),y,Inches(3.2),Inches(0.6),[[(q,{"size":11.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,Inches(10.3),y,Inches(2.4),Inches(0.6),[[(a+" ",{"size":12,"bold":True,"color":GD}),("· "+gl,{"size":9,"italic":True,"color":MUT})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y=y+Inches(0.72)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.85),
             [[("A: ", {"bold":True,"color":GD}), ("aguda=laatste · llana=voorlaatste · esdrújula=voor-voorlaatste (altijd tilde). 🔴 los pantalones/marrones (tilde weg).", {"color":GD})],
              [("🔴 B: ", {"bold":True,"color":RED}), ("«dus» = así que/por eso (niet luego). Na ontkenning «maar wel» = sino.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · TALLER. Sílaba tónica met de meervoudsval (pantalón→pantalones). Conectores meteen toepassen. "
             "Online: «sílaba tónica» + conectoren-oefeningen.")

# ============================================================ DIA 16 · CULTURE — rebajas, regateo, tianguis
def s16_cultura():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "CULTURA · PARADA 6", "Rebajas, regateo y tianguis", "Klik een kaart → het weetje verschijnt. Comprar también es cultura.", num=6)
    cards=[("🏷️ Las rebajas","Dos veces al año (enero y julio en España): descuentos de −30 %, −50 %. La gente hace cola en las tiendas.","Rebajas = solden."),
           ("🤝 El regateo","En el mercado o el tianguis se puede regatear: «¿Me hace un descuento?». En una tienda con etiqueta, no.","Regatear = afdingen (enkel op de markt)."),
           ("🧺 El tianguis","Del náhuatl «tiānquiztli»: mercado al aire libre e itinerante, desde tiempos aztecas. Ropa, comida, artesanía; se paga en efectivo.","Moda sostenible vs moda rápida.")]
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
             [[("Actividad: ", {"bold":True,"color":GD}), ("¿compras ropa nueva o de segunda mano? ¿regateas? Refrán: «Lo barato sale caro».", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · CULTURE (identiteit in diversiteit, LPD 5). Onthul per kaart. Tianguis = náhuatl-woord. Bruggetje naar de Tarea Abre tu tienda. "
             "Online: «prenda ↔ tienda» (match).")

# ============================================================ DIA 17 · QUIZ — completa la compra
def s17_quiz_compra():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · QUIZ · INTERACCIÓN", "Completa la compra", "Wat past? Klik → het antwoord verschijnt.", num=1)
    items=[("¿Qué ___? (u wenst)","desea"),("¿Puedo ___me la falda? (passen)","probar"),
           ("¿Cuánto ___? (kosten)","cuesta"),("Me queda bien. Me ___ llevo. (het)","lo"),
           ("Acabo ___ comprar. (van)","de"),("Pago con ___. (kaart)","tarjeta")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(6.05); rh=Inches(0.78)
    for i,(ans,q) in enumerate(items):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(4.0),rh,[[(ans,{"size":11.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(4.2),y,cw-Inches(4.35),rh,[[("→ "+q,{"size":12,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.6),
             [[("De winkelzinnen: ", {"bold":True,"color":GD}),
               ("¿Qué desea? · ¿Puedo probármelo/la? · ¿Cuánto cuesta? · Me lo llevo · Acabo de comprar · Pago con tarjeta.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ interactie. Klas vult de zin vóór de klik. Daarna de rollenspel-scène in parejas.")

# ============================================================ DIA 18 · FINAL_MISSION — Abre tu tienda
def s18_tarea():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(1.35), fill=GD)
    text(s, Inches(0.5), Inches(0.18), Inches(9), Inches(1.0),
         [[("🛍️ Tarea final · Abre tu tienda", {"size":30,"bold":True,"color":WHITE,"font":DISPLAY})],
          [("Ontwerp de tienda van je eigen winkel y representa la escena vendedor ↔ cliente.", {"size":13,"italic":True,"color":GT})]])
    avatar(s, "mochila", Inches(11.6), Inches(0.2), Inches(1.0))
    pasos=[("1","Elige un nombre y estilo","deportivo, elegante, sostenible…"),
           ("2","Diseña el escaparate","4 prendas + color/patrón + precio (concordancia)"),
           ("3","Escribe un anuncio de rebajas","antes → ahora · descuento"),
           ("4","Escribe el diálogo","saludar → este/ese → probador → precio/regateo → me lo llevo"),
           ("5","Representa + reseña","en pareja (of neem audio op) + review")]
    y=Inches(1.7)
    for n,es,nl in pasos:
        b=rect(s,Inches(0.5),y,Inches(0.5),Inches(0.5),fill=G,round=True,radius=0.5)
        tf=b.text_frame;tf.vertical_anchor=MSO_ANCHOR.MIDDLE;p=tf.paragraphs[0];p.alignment=PP_ALIGN.CENTER
        rr=p.add_run();rr.text=n;rr.font.size=Pt(15);rr.font.bold=True;rr.font.name=DISPLAY;rr.font.color.rgb=WHITE
        text(s,Inches(1.2),y,Inches(4.6),Inches(0.55),[[(es,{"size":14,"bold":True,"color":GD,"font":DISPLAY})]],anchor=MSO_ANCHOR.MIDDLE)
        text(s,Inches(5.9),y,Inches(6.8),Inches(0.55),[[(nl,{"size":11.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        y=y+Inches(0.62)
    text(s, Inches(0.5), Inches(5.0), Inches(12), Inches(0.35), [[("Rúbrica · ¿lo logré?", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    crit=["4 prendas + color + precio","lo/la/los/las in de dialoog","este/ese + acabar de","representar la escena"]
    x=Inches(0.5)
    for c in crit:
        chip(s,x,Inches(5.45),"☐ "+c,fill=GT,tcolor=GD,size=11,w=Inches(3.0)); x=x+Inches(3.1)
    text(s, Inches(0.5), Inches(6.05), Inches(12), Inches(0.4),
         [[("🎯 ", {"size":12}), ("Afzender jij (de winkel) · ontvanger de cliente · doel kleding aanbieden & verkopen · situatie una tienda/tianguis en México · resultaat: escaparate + anuncio + dialoog + reseña.", {"size":11.5,"italic":True,"color":MUT})]])
    foot(s)
    notes(s, "TEACHER · FINAL_MISSION (communicatieve eindtaak). Afzender/ontvanger/doel/situatie/resultaat expliciet. Beoordeel met de rúbrica; "
             "opname + zelfevaluatie op de digitale pagina. Voeg een mini-encuesta + grafiekje toe (ropa favorita van de klas).")

# ============================================================ DIA 19 · QUIZ — la mezcla
def s19_mezcla():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "QUIZ · LA MEZCLA", "Ophaal door elkaar", "Gemengde ophaal van de hele unit. Klik een vraag → het antwoord. (retrieval)", num=6)
    items=[("¿La falda? → ___ compro","la"),("¿Los zapatos? → ___ llevo","los"),("acabar, yo → ___ de comprar","acabo"),
           ("acabar, nosotros → ___ de pagar","acabamos"),("camiseta (rood) → roj__","roja"),("vaqueros (blauw) → azul__","azules"),
           ("cerca (v) → ___ camiseta","esta"),("lejos (m) → ___ abrigo","aquel")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(6.05); rh=Inches(0.62)
    for i,(q,a) in enumerate(items):
        c=i//4; r=i%4; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.16))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(3.6),rh,[[(q,{"size":11.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(3.75),y,cw-Inches(3.9),rh,[[("→ "+a,{"size":12,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.05), Inches(12.3), Inches(0.55),
             [[("Alles komt terug: ", {"bold":True,"color":GD}), ("lo/la/los/las · acabar de + infinitivo · este/ese/aquel · concordancia.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ mezcla (retrieval vóór herlezen). Zonder waarschuwing door elkaar. Exit-ticket. Zwakke punten → terug via menu.")

# ============================================================ DIA 20 · FEEDBACK/REPASO
def s20_repaso():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "REPASO · LO ESENCIAL", "Lo esencial de un vistazo", "De volledige herhaling (20 spellen, drills) staat online. Hier: de kern + semáforo.", num=6)
    ess=["lo/la/los/las: ¿la falda? → La compro. Vóór het vervoegde ww of vast achter de infinitief (comprarla).",
         "Acabar de + infinitivo: acabo/acabas/acaba… + de + infinitief = net (zopas) gedaan.",
         "este/ese/aquel: este (aquí) · ese (ahí) · aquel (allí) — past bij de prenda (este/esta/estos/estas…).",
         "Concordancia: camiseta rojA · zapatos rojOS. Kleuren op -o veranderen; azul/gris/verde niet (enkel mv.).",
         "🔴 Trampas: la compro (niet «compro la») · acabo DE comprar · una falda azul (niet «azula») · los pantalones (tilde weg)."]
    card(s, Inches(0.5), Inches(1.6), Inches(12.3), Inches(2.5), fill=CREMA, line=None)
    y=Inches(1.8)
    for e in ess:
        text(s, Inches(0.8), y, Inches(11.8), Inches(0.45), [[("• ", {"size":13,"bold":True,"color":GD}),(e,{"size":12,"color":INK})]])
        y=y+Inches(0.46)
    text(s, Inches(0.5), Inches(4.3), Inches(12), Inches(0.35), [[("Semáforo — ¿cómo lo llevas?", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    can=["ropa/colores benoemen","lo/la/los/las (la compro)","acabar de + infinitivo","este/ese/aquel (afstand)","concordancia (roja/azules)"]
    y=Inches(4.75)
    for c in can:
        text(s,Inches(0.8),y,Inches(7.0),Inches(0.4),[[(c,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        for j,(em,col) in enumerate([("🔴",RED),("🟠",AMBER),("🟢",G)]):
            chip(s,Inches(8.0)+j*Inches(1.5),y+Inches(0.03),em+" ",fill=WHITE,tcolor=col,size=12,w=Inches(1.3))
        y=y+Inches(0.42)
    foot(s)
    notes(s, "TEACHER · FEEDBACK/REPASO. Semáforo = zelfevaluatie. Repaso-drills online (20 spellen). Bruggetje: U7 «Mi casa y mi barrio» — "
             "Cartagena, Colombia: de casa, el barrio, describir dónde vives.")

# ============================================================ DIA 21 · TEACHER_NOTES
def s21_teacher():
    s = slide(); bg(s, GD)
    text(s, Inches(0.6), Inches(0.4), Inches(12), Inches(0.8), [[("TEACHER_NOTES · U6 «De tiendas»", {"size":26,"bold":True,"color":WHITE,"font":DISPLAY})]])
    blocks=[("Timing (50 min)","Menu 2' · lo/la/los/las 10' · acabar de + inf. 7' · este/ese/aquel 7' · concordancia 8' · lectura/escucha 8' · cultura 3' · Tarea-briefing 3'."),
            ("Kernvalstrikken","la compro (niet «compro la») · pronomen vóór het vervoegde ww / achter de infinitief · acabo DE comprar · una falda azul (niet «azula»); rojo/roja/rojos/rojas · los pantalones/marrones (tilde weg) · «dus» = así que/por eso."),
            ("Differentiatie (zij-instromers)","Alles start vanaf nul. Sterker: hele winkelscène + regateo + eigen escaparate + reseña. Zwakker: pronomen-kaart en acabar-tabel langer open, concordancia-kaart houden."),
            ("Digitaal","20 spellen + flip cards + klikbare kaart + recorder (Hablar) + Lectura (anuncio + reseña) op de página digital. QR's in het boek → juiste anker. Conjugador = aparte tool."),
            ("Evaluatie","Tarea «Abre tu tienda» met rúbrica (4 criteria). LPD 3·4·7·8 + 5 (cultura) + 1·2 (receptief: lezen/luisteren).")]
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
    s01_title(); s02_menu(); s03_vocab(); s04_od(); s05_od_quiz(); s06_acabar(); s07_demos()
    s08_quiz_demos(); s09_reading(); s10_listening(); s11_concord(); s12_speaking(); s13_writing()
    s14_colores_tiendas(); s15_taller(); s16_cultura(); s17_quiz_compra(); s18_tarea(); s19_mezcla(); s20_repaso()
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
