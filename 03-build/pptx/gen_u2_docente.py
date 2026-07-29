#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_u2_docente.py — Interactieve PowerPoint C5 · Unidad 2 «Mi gente» (parada Sevilla · Lucía)
=========================================================================================
Zelfde engine/pijplijn als de golden sample U0/U1/U3 (gen_u0_docente wordt geïmporteerd:
alle low-level helpers, on-click <p:timing>-animaties, hyperlink-navigatie).
Enkel de SLIDES (content) zijn U2-specifiek. Twee decks (beide .pptx):
  · C5_U2_docente.pptx — vrije navigatie, oplossingen bij klik + didactiek in spreker-notities.
  · C5_U2_alumno.pptx  — gewone diavoorstelling (F5), antwoorden verschijnen bij klik (geen kiosk).
Huisstijl groen (C5). Spaans-eerst + NL-steun. ≥20 dia's. Vier vaardigheden gedekt (lezen/luisteren/spreken/schrijven).
Gastvrouw = Lucía (Sevilla) — prominent. Werkwoordsvormen exact volgens U2_bron.md §3.
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
OUT_DOCENTE = os.path.join(HERE, "C5_U2_docente.pptx")
OUT_ALUMNO_PPTX = os.path.join(HERE, "C5_U2_alumno.pptx")
TAB = "U2 · MI GENTE"

# Functionele kleursemantiek voor de ser/estar-tegenstelling (§13): ser=identiteit (blauw), estar=toestand/plaats (turquoise)
C_SER = F_SUBJ
C_ESTAR = F_PLAC

def foot(s): footer(s, tab=TAB, page=pg())

# ============================================================ DIA 1 · TITLE
def s01_title():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(4.7), fill=G)
    rect(s, 0, Inches(4.7), EMU_W, Inches(0.09), fill=GD)
    text(s, Inches(0.6), Inches(0.35), Inches(3.4), Inches(3.6),
         [[("2", {"size": 260, "bold": True, "color": RGBColor(0x2E,0xB0,0x85), "font": DISPLAY})]],
         anchor=MSO_ANCHOR.MIDDLE)
    chip(s, Inches(4.35), Inches(0.85), "LA RUTA · PARADA 2 · SEVILLA 🇪🇸", fill=WHITE, tcolor=GD, size=12)
    text(s, Inches(4.3), Inches(1.35), Inches(8.6), Inches(1.5),
         [[("Mi gente", {"size": 60, "bold": True, "color": WHITE, "font": DISPLAY})]])
    text(s, Inches(4.35), Inches(2.6), Inches(8.4), Inches(0.6),
         [[("La familia · describir a las personas · ser y estar — en Sevilla, con Lucía.", {"size": 15, "italic": True, "color": GT})]])
    text(s, Inches(4.35), Inches(3.25), Inches(8.4), Inches(0.9),
         [[("¿Quién es tu gente… y cómo es?", {"size": 24, "bold": True, "color": WHITE, "font": DISPLAY})],
          [("Wie zijn jouw mensen… en hoe zijn ze?", {"size": 13, "italic": True, "color": GT})]])
    text(s, Inches(0.6), Inches(4.95), Inches(8), Inches(0.4),
         [[("Tu anfitriona en Sevilla — Lucía te presenta a su familia", {"size": 13, "bold": True, "color": GD, "font": DISPLAY})]])
    # Lucía prominent als gastvrouw + de cast
    avatar(s, "lucia", Inches(0.6), Inches(5.3), Inches(1.35))
    text(s, Inches(0.45), Inches(6.7), Inches(1.7), Inches(0.5),
         [[("Lucía", {"size": 12, "bold": True, "color": INK})],
          [("Sevilla 🇪🇸 · anfitriona", {"size": 8.5, "color": MUT})]], align=PP_ALIGN.CENTER)
    x = Inches(2.6)
    for nm, city in [("diego","CDMX 🇲🇽"),("valen","Cartagena 🇨🇴"),
                     ("nina","Cusco 🇵🇪"),("tu","Tú · Flandes 🇧🇪"),("mochila","La mochila")]:
        avatar(s, nm, x, Inches(5.4), Inches(1.0))
        text(s, x - Inches(0.15), Inches(6.42), Inches(1.3), Inches(0.5),
             [[(nm.capitalize() if nm!="tu" else "Tú", {"size": 10.5, "bold": True, "color": INK})],
              [(city.split("·")[-1].strip() if nm!="tu" else "de reiziger = jij", {"size": 8.5, "color": MUT})]],
             align=PP_ALIGN.CENTER)
        x = x + Inches(2.05)
    foot(s)
    notes(s, "TEACHER · TITLE. Parada 2 = Sevilla, met gastvrouw Lucía (dit is HAAR thuisstad → zij stelt haar familie voor). "
             "Doel: familieleden benoemen + tener · beschrijven (física + carácter) met congruentie van adjetivos · posesivos (mi/tu/su/nuestro) · "
             "DÉ valstrik ser vs. estar (beide = «zijn») · demostrativos (este/ese) bij foto's. "
             "Instructietaal Spaans-eerst met NL-steun. Docentdeck = vrije navigatie + oplossing; leerlingdeck = elke klik onthult (geen kiosk). "
             "Tarea = «Álbum de familia».")

# ============================================================ DIA 2 · LESSON_MENU
def s02_menu():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "MENÚ DE LA LECCIÓN", "El mapa de la Unidad 2",
               "Kies je route — klik een tegel. Alles oefent naar de Tarea «Álbum de familia» toe.", num=2)
    tiles = [
        ("§1", "La familia + tener", "padre/madre/hermano · tengo/tienes/tiene", G, 3),
        ("§2", "Los posesivos", "mi/tu/su/nuestro · getal", G, 6),
        ("§3", "Los adjetivos", "física + carácter · congruencia o/a", G, 8),
        ("§4", "Ser / estar", "🔴 beide = «zijn» — de valstrik", GD, 11),
        ("§5", "Demostrativos", "este/ese — señala en el álbum", G, 14),
        ("📖", "Lectura + escuchar", "«La familia de Lucía» · ¿quién es?", GD, 16),
        ("✈", "Tarea · Álbum de familia", "árbol + fotos + «¿Quién es?»", GD, 21),
        ("◎", "Quiz + Repaso", "la mezcla · lo esencial · semáforo", AMBER, 22),
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
             "Zij-instromers: begin bij §1 (familia + tener) — daar zit de communicatieve kern. Alles start vanaf nul.")

# ============================================================ DIA 3 · VOCABULARY — la familia (árbol, reveal)
def s03_familia():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · VOCABULARIO", "La familia — el árbol genealógico", "Klik een kaart → betekenis. Mannelijk el / vrouwelijk la; -o/-a-paren.", num=1)
    items=[("el padre / la madre","de vader / de moeder"),("los padres","de ouders"),
           ("el hermano / la hermana","de broer / de zus"),("el abuelo / la abuela","de opa / de oma"),
           ("el tío / la tía","de oom / de tante"),("el primo / la prima","de neef / de nicht"),
           ("el hijo / la hija","de zoon / de dochter"),("el nieto / la nieta","de kleinzoon / kleindochter")]
    x0,y0=Inches(0.5),Inches(1.7); cw=Inches(6.05); rh=Inches(0.72)
    for i,(es,nl) in enumerate(items):
        c=i//4; r=i%4; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.14))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.2),y,Inches(3.4),rh,[[(es,{"size":13.5,"bold":True,"color":GD,"font":DISPLAY})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(3.65),y,cw-Inches(3.8),rh,[[("→ "+nl,{"size":11.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.9),
             [[("La familia hispana: ", {"bold":True,"color":GD}), ("mannelijk meervoud omvat beide: ", {"color":GD}),
               ("los padres", {"bold":True,"color":GD}), (" = vader én moeder · ", {"color":GD}),
               ("los abuelos", {"bold":True,"color":GD}), (" = opa én oma · ", {"color":GD}),
               ("los hermanos", {"bold":True,"color":GD}), (" = broer(s) én zus(sen).", {"color":GD})],
              [("mayor (ouder/oudste) · menor (jonger/jongste) · casado/a (getrouwd) · soltero/a (vrijgezel) · la mascota (huisdier).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCAB familia (reveal). Bouw een árbol genealógico op het bord terwijl je onthult. Wijs op de -o/-a-paren. "
             "Zie het boek §1.1 → el árbol genealógico de ROSALÍA (parel) + het ¡Ojo!-kader: primo/prima (kind van tío/tía) vs. sobrino/sobrina (kind van hermano/hermana). "
             "Online: «familia-memoria» + flip cards ES↔NL.")

# ============================================================ DIA 4 · GRAMMAR — tener (conjugation reveal)
def s04_tener():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · GRAMÁTICA", "El verbo tener (hebben)", "Denk de vorm, klik de kaart. Onregelmatig: tengo, tienes, tiene…", num=1)
    R=[("yo","tengo"),("tú","tienes"),("él/ella/usted","tiene"),
       ("nosotros/-as","tenemos"),("vosotros/-as","tenéis"),("ellos/-as/ustedes","tienen")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(3.95); ch=Inches(1.25)
    for i,(p,v) in enumerate(R):
        c=i%3; r=i//3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(ch+Inches(0.2))
        card(s,x,y,cw,ch,fill=WHITE,line=G,lw=1.4)
        text(s,x,y+Inches(0.12),cw,Inches(0.4),[[(p,{"size":13,"color":MUT})]],align=PP_ALIGN.CENTER)
        rev=text(s,x,y+Inches(0.5),cw,Inches(0.6),[[(v,{"size":22,"bold":True,"color":GD,"font":DISPLAY})]],align=PP_ALIGN.CENTER)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.5), Inches(12.3), Inches(0.9),
             [[("🟡 tener = onregelmatig: ", {"bold":True,"color":GD}), ("teng-o · tien-es · tien-e · ten-emos · ten-éis · tien-en. ", {"bold":True,"color":GD})],
              [("Gebruik: ", {"bold":True,"color":GD}), ("«Tengo dos hermanos» · «¿Cuántos primos tienes?» · leeftijd: «Tengo catorce años».", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR tener (reveal per kaart). Coro: klas zegt de vorm vóór de klik. tener voor bezit, familie én leeftijd (tener … años). "
             "Zie het boek §1.2 (verbo-machine/tabel). Online: «tener-cloze» + «tener-persona» (classify).")

# ============================================================ DIA 5 · SPEAKING/QUIZ — ¿cuántos? contar la familia
def s05_cuantos():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§1 · INTERACCIÓN", "¿Cuántos… tienes? — cuenta tu familia", "Vraag & antwoord met tener. Klik een kaart → een modelantwoord.", num=1)
    avatar(s, "lucia", Inches(11.4), Inches(1.6), Inches(1.3))
    qa=[("¿Cuántos hermanos tienes?","Tengo dos hermanos. / No tengo hermanos."),
        ("¿Tienes primos?","Sí, tengo tres primos. / No, no tengo primos."),
        ("¿Cuántos años tiene tu hermano?","Tiene diecinueve años."),
        ("¿Tienes mascota?","Sí, tengo un perro. / No tengo mascota."),
        ("¿Cuántas personas sois en tu familia?","Somos cinco: mis padres, mis hermanos y yo.")]
    y=Inches(1.75)
    for q,a in qa:
        card(s,Inches(0.5),y,Inches(10.4),Inches(0.82),fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,Inches(0.65),y+Inches(0.05),Inches(10.0),Inches(0.36),[[("❓ "+q,{"size":12.5,"bold":True,"color":GD})]])
        rev=text(s,Inches(0.65),y+Inches(0.42),Inches(10.0),Inches(0.34),[[("→ "+a,{"size":12,"italic":True,"color":INK})]])
        register_reveal(s, rev)
        y=y+Inches(0.92)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(6.35), Inches(12.3), Inches(0.5),
             [[("Ronda: ", {"bold":True,"color":GD}), ("vraag 3 klasgenoten en presenteer daarna één familie in de 3ª persona (tiene / son).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · SPEAKING (interactie met tener/ser). Circuleer: leerlingen vragen elkaar. Let op tener (bezit/leeftijd) vs. somos (aantal). "
             "Online: «carrusel-familia» (recorder). Print blijft bruikbaar zonder opname.")

# ============================================================ DIA 6 · GRAMMAR — posesivos (color + reveal)
def s06_posesivos():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · GRAMÁTICA VISUAL", "Los posesivos — mi / tu / su / nuestro", "Kleur = taalfunctie. Het bezit past in GETAL bij het zelfstandig naamwoord.", num=2)
    legend_func(s, Inches(9.7), Inches(0.55))
    seg=[("Mi ", F_SUBJ),("hermana ", F_OBJ),("es alta ", INK),("y ", INK),("mis ", F_SUBJ),("hermanos ", F_OBJ),("son morenos.", INK)]
    runs=[[(t,{"size":23,"bold":True,"color":c,"font":DISPLAY}) for t,c in seg]]
    card(s, Inches(0.5), Inches(1.65), Inches(12.3), Inches(1.1), fill=GT, line=None)
    text(s, Inches(0.8), Inches(1.65), Inches(11.7), Inches(1.1), runs, anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(0.5), Inches(3.0), Inches(12), Inches(0.4), [[("El mecanismo — klik een cel → de vorm:", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    grid=[("mi / mis","mijn"),("tu / tus","jouw"),("su / sus","zijn/haar/hun/uw"),("nuestro/-a/-os/-as","onze")]
    x0,y0=Inches(0.5),Inches(3.5); cw=Inches(6.05); rh=Inches(0.78)
    for i,(a,b) in enumerate(grid):
        c=i%2; r=i//2; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.16))
        card(s,x,y,cw,rh,fill=WHITE,line=G,lw=1.1,shadow=False)
        text(s,x+Inches(0.2),y,Inches(3.2),rh,[[(a,{"size":15,"bold":True,"color":F_SUBJ,"font":DISPLAY})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(3.4),y,cw-Inches(3.55),rh,[[("→ "+b,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.7), Inches(12.3), Inches(0.9),
             [[("🔴 Overeenkomst in GETAL (niet in geslacht, behalve nuestro): ", {"bold":True,"color":RED}),
               ("mi hermana → mis hermanas · tu primo → tus primos.", {"bold":True,"color":GD})],
              [("su = zijn/haar/hun/uw (context beslist) · nuestro/nuestra/nuestros/nuestras past óók in geslacht.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR posesivos (color + reveal). Grote NL-valstrik: getalscongruentie (mis hermanas). su is ambigu → context. "
             "Zie het boek §2. Online: «posesivo-cloze» + «posesivo-numero» (classify sing/plur).")

# ============================================================ DIA 7 · QUIZ — posesivo: número (reveal)
def s07_quiz_posesivo():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§2 · QUIZ", "Singular o plural — mi o mis", "Klik een zin → de juiste vorm. Tel het zelfstandig naamwoord.", num=2)
    items=[("___ hermano (1)","mi"),("___ hermanas (2)","mis"),("___ primos (varios)","mis"),
           ("___ abuela (1)","mi"),("¿Cómo se llama ___ padre?","tu"),("¿Dónde viven ___ abuelos?","tus"),
           ("___ familia es grande. (onze)","nuestra"),("___ tíos son majos. (haar)","sus")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(6.05); rh=Inches(0.62)
    for i,(q,a) in enumerate(items):
        c=i//4; r=i%4; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.16))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(4.0),rh,[[(q,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(4.2),y,cw-Inches(4.35),rh,[[("→ "+a,{"size":13,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.05), Inches(12.3), Inches(0.55),
             [[("Enkelvoud zn. → mi/tu/su · meervoud zn. → mis/tus/sus. ", {"bold":True,"color":GD}),
               ("nuestro/-a/-os/-as past in geslacht én getal.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ posesivo número (retrieval). Laat de klas eerst kiezen (hand/stem). Focus: getalscongruentie, niet geslacht (behalve nuestro).")

# ============================================================ DIA 8 · VOCABULARY — descripción física (reveal)
def s08_fisico():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · VOCABULARIO", "¿Cómo es? — descripción física", "Klik een kaart → betekenis. Descripción met ser + tener/llevar.", num=3)
    items=[("alto/a ↔ bajo/a","lang/groot ↔ klein"),("delgado/a ↔ gordito/a","slank ↔ mollig"),
           ("guapo/a","knap / mooi"),("moreno/a ↔ rubio/a","donker ↔ blond"),
           ("pelirrojo/a","roodharig"),("el pelo largo/corto","lang/kort haar"),
           ("liso ↔ rizado","steil ↔ krullend"),("los ojos + color","de ogen + kleur"),
           ("la barba","de baard"),("llevar gafas","een bril dragen")]
    x0,y0=Inches(0.5),Inches(1.7); cw=Inches(6.05); rh=Inches(0.68)
    for i,(es,nl) in enumerate(items):
        c=i//5; r=i%5; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.13))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.18),y,Inches(3.3),rh,[[(es,{"size":12.5,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(3.55),y,cw-Inches(3.7),rh,[[("→ "+nl,{"size":11,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.4), Inches(12.3), Inches(0.9),
             [[("Constructies: ", {"bold":True,"color":GD}), ("es alto (ser + eigenschap) · tiene el pelo largo / los ojos verdes (tener + kenmerk) · lleva gafas (llevar).", {"color":GD})],
              [("colores: marrón · negro · castaño · azul · verde · gris. «Tiene los ojos marrones» (congruentie in getal).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · VOCAB física (reveal). Bouw tegenstellingsparen (alto↔bajo). ser voor eigenschap, tener/llevar voor haar/ogen/bril. "
             "Zie het boek §3.1. Online: «fisico-caracter» (classify) + «colores-match».")

# ============================================================ DIA 9 · GRAMMAR — congruencia del adjetivo (color/xray)
def s09_congruencia():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · GRAMÁTICA VISUAL", "El adjetivo concuerda — género y número", "Röntgen: het bijv. nw. past bij het zn. in geslacht én getal, en staat ERNA.", num=3)
    # Bouwstroken / agree-kaart met 4 vormen
    grid=[("el chico alt-o","m. enkelvoud", F_OBJ),("la chica alt-a","v. enkelvoud", F_OBJ),
          ("los chicos alt-os","m. meervoud", F_OBJ),("las chicas alt-as","v. meervoud", F_OBJ)]
    x0,y0=Inches(0.5),Inches(1.7); cw=Inches(6.05); rh=Inches(0.95)
    for i,(es,nl,col) in enumerate(grid):
        c=i%2; r=i//2; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=GT,line=G,lw=1.2)
        text(s,x+Inches(0.25),y+Inches(0.12),cw-Inches(0.5),Inches(0.45),[[(es,{"size":18,"bold":True,"color":GD,"font":DISPLAY})]])
        text(s,x+Inches(0.25),y+Inches(0.55),cw-Inches(0.5),Inches(0.32),[[(nl,{"size":11,"italic":True,"color":MUT})]])
    text(s, Inches(0.5), Inches(4.05), Inches(12), Inches(0.4), [[("Klik → de speciale gevallen:", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    special=[("inteligente","→ blijft gelijk (m/v): chico/chica inteligente"),
             ("joven → jóvenes","→ enkel meervoud verandert"),
             ("hablador → habladora","→ -or krijgt wél -a in het vrouwelijk"),
             ("los ojos verdes","→ kleur past in getal (verde → verdes)")]
    x0,y0=Inches(0.5),Inches(4.5); cw=Inches(6.05); rh=Inches(0.62)
    for i,(a,b) in enumerate(special):
        c=i%2; r=i//2; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.14))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(2.5),rh,[[(a,{"size":12,"bold":True,"color":F_OBJ})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(2.65),y,cw-Inches(2.8),rh,[[(b,{"size":10.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(6.05), Inches(12.3), Inches(0.55),
             [[("🔴 Het adjetivo staat NÁ het zn. en past mee: ", {"bold":True,"color":RED}),
               ("una chica alta, unos ojos verdes. -e/-ista/-consonant zijn vaak onveranderlijk in geslacht.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR congruencia (agree-kaart/röntgen). Kernvalstrik NL: bijv.nw. staat ná het zn. + moet mee-verbuigen. "
             "Zie het boek §3.2. Online: «masculino-femenino» + «adjetivo-concuerda» (cloze).")

# ============================================================ DIA 10 · VOCAB/GRAMMAR — carácter + posición
def s10_caracter():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§3 · VOCABULARIO", "¿Cómo es su carácter?", "Klik een kaart → betekenis. ser + carácter (es simpático).", num=3)
    items=[("simpático/a ↔ antipático/a","aardig ↔ onaardig"),("majo/a","leuk/vriendelijk (Sp.)"),
           ("tímido/a","verlegen"),("gracioso/a","grappig"),("trabajador/a","hardwerkend"),
           ("inteligente","slim"),("hablador/a","praatgraag"),("tranquilo/a","rustig"),
           ("alegre","vrolijk")]
    x0,y0=Inches(0.5),Inches(1.7); cw=Inches(4.05); rh=Inches(0.72)
    for i,(es,nl) in enumerate(items):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.13)); y=y0+r*(rh+Inches(0.16))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(2.3),rh,[[(es,{"size":11.5,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(2.45),y,cw-Inches(2.6),rh,[[("→ "+nl,{"size":10,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.85),
             [[("Modelo (docent): ", {"bold":True,"color":GD}),
               ("«Mi hermana es simpática, un poco tímida pero muy graciosa. Mi padre es tranquilo y trabajador.»", {"color":GD})],
              [("«muy» (heel) + «un poco» (een beetje) + «pero» (maar) nuanceren de beschrijving.", {"color":GD})]],
             trigger=btn, title_doc="MODELO · docent")
    foot(s)
    notes(s, "TEACHER · VOCAB carácter (reveal). Combineer física + carácter met conectores (y/pero/también). muy / un poco als versterkers. "
             "Zie het boek §3.3. Online: «describe-persona» (speak) + «fisico-caracter» (classify).")

# ============================================================ DIA 11 · GRAMMAR — ser/estar contrast (color)
def s11_serestar_color():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · GRAMÁTICA VISUAL", "Ser y estar — 🔴 la trampa (beide = «zijn»)", "Twee-kolom-spiegel: SER = wie/hoe iemand is · ESTAR = toestand/plaats.", num=4)
    # Twee kolommen (mirror)
    card(s, Inches(0.5), Inches(1.65), Inches(6.0), Inches(3.6), fill=GT, line=C_SER, lw=1.6)
    text(s, Inches(0.7), Inches(1.8), Inches(5.6), Inches(0.5), [[("SER — identidad / descripción", {"size":16,"bold":True,"color":C_SER,"font":DISPLAY})]])
    ser_ex=["Soy Lucía. (identiteit)","Es de Sevilla. (herkomst)","Mi padre es alto y moreno. (uiterlijk)",
            "Mi tía es muy simpática. (karakter)","Somos cinco. (aantal)"]
    y=Inches(2.4)
    for e in ser_ex:
        text(s, Inches(0.75), y, Inches(5.6), Inches(0.42), [[("• ",{"size":13,"bold":True,"color":C_SER}),(e,{"size":12.5,"color":INK})]])
        y=y+Inches(0.5)
    card(s, Inches(6.8), Inches(1.65), Inches(6.0), Inches(3.6), fill=CREMA, line=C_ESTAR, lw=1.6)
    text(s, Inches(7.0), Inches(1.8), Inches(5.6), Inches(0.5), [[("ESTAR — estado / lugar", {"size":16,"bold":True,"color":C_ESTAR,"font":DISPLAY})]])
    est_ex=["Estoy bien / cansada. (toestand)","Mi abuela está en casa. (plaats)","¿Dónde estás? (plaats)",
            "Mis tíos están casados. (burg. staat)","Hoy estamos contentos. (stemming nu)"]
    y=Inches(2.4)
    for e in est_ex:
        text(s, Inches(7.05), y, Inches(5.6), Inches(0.42), [[("• ",{"size":13,"bold":True,"color":C_ESTAR}),(e,{"size":12.5,"color":INK})]])
        y=y+Inches(0.5)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.45), Inches(12.3), Inches(0.85),
             [[("🔴 Nederlands heeft één «zijn», Spaans twee: ", {"bold":True,"color":RED}),
               ("SER = wie/hoe iemand IS (blijvend: naam, herkomst, uiterlijk, karakter) · ", {"color":GD})],
              [("ESTAR = toestand nú of PLAATS (cansada, en casa). «Es simpática» (altijd) ↔ «Está cansada» (nu).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR ser/estar contrast (mirror). DÉ valstrik voor Nederlandstaligen: beide = «zijn». "
             "SER = identiteit/beschrijving (blijvend) · ESTAR = toestand/plaats (tijdelijk/locatie). "
             "Zie het boek §4.1. Online: «ser-estar» (classify).")

# ============================================================ DIA 12 · GRAMMAR — ser/estar formas (reveal)
def s12_serestar_formas():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · GRAMÁTICA", "Las formas — ser · estar", "Klik een cel → de vorm. Beide onregelmatig; let op de yo-vorm.", num=4)
    cols=[("ser (identidad)",["soy","eres","es","somos","sois","son"], C_SER),
          ("estar (estado/lugar)",["estoy","estás","está","estamos","estáis","están"], C_ESTAR)]
    pers=["yo","tú","él/ella","nosotros","vosotros","ellos"]
    x0,y0=Inches(2.0),Inches(1.75); cw=Inches(5.3)
    for ci,(title,forms,col) in enumerate(cols):
        x=x0+Inches(1.6)+ci*(cw)
        card(s,x,y0,cw-Inches(0.2),Inches(0.55),fill=col,line=None)
        text(s,x,y0,cw-Inches(0.2),Inches(0.55),[[(title,{"size":13,"bold":True,"color":WHITE,"font":DISPLAY})]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    for ri,pr in enumerate(pers):
        y=y0+Inches(0.65)+ri*Inches(0.62)
        text(s,Inches(2.0),y,Inches(1.5),Inches(0.55),[[(pr,{"size":12,"color":MUT})]],anchor=MSO_ANCHOR.MIDDLE)
        for ci,(title,forms,col) in enumerate(cols):
            x=x0+Inches(1.6)+ci*(cw)
            card(s,x,y,cw-Inches(0.2),Inches(0.55),fill=WHITE,line=LINE,lw=1.0,shadow=False)
            rev=text(s,x,y,cw-Inches(0.2),Inches(0.55),[[(forms[ri],{"size":14,"bold":True,"color":col})]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
            register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.7), Inches(12.3), Inches(0.6),
             [[("ser: ", {"bold":True,"color":C_SER}), ("soy·eres·es·somos·sois·son · ", {"bold":True,"color":GD}),
               ("estar: ", {"bold":True,"color":C_ESTAR}), ("estoy·estás·está·estamos·estáis·están (klemtoon estás/está!).", {"bold":True,"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR ser/estar formas (reveal per cel). Coro vóór de klik. Let op tildes: estás, está, estáis. "
             "Vormen exact volgens U2_bron.md §3. Werkwoordsvervoeging verder = aparte Conjugador-tool.")

# ============================================================ DIA 13 · CLOZE — tener + ser/estar (VERPLICHT)
def s13_cloze():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§4 · QUIZ · CONJUGA", "Cloze — tener · ser · estar", "Klik een zin → de juiste vorm(en). Kies tussen ser/estar en vervoeg tener.", num=4)
    items=[("Mi abuela ___ (ser) simpática y hoy ___ (estar) en Sevilla.","es · está"),
           ("Yo ___ (tener) dos primos.","tengo"),
           ("Mis padres ___ (ser) de Andalucía.","son"),
           ("Nosotros ___ (estar) en casa.","estamos"),
           ("¿Cuántos hermanos ___ (tener) tú?","tienes"),
           ("Lucía ___ (tener) el pelo largo y ___ (ser) morena.","tiene · es"),
           ("Mi hermano ___ (estar) cansado.","está"),
           ("Vosotros ___ (ser) muy majos.","sois")]
    x0,y0=Inches(0.5),Inches(1.7); cw=Inches(6.05); rh=Inches(0.72)
    for i,(q,a) in enumerate(items):
        c=i//4; r=i%4; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.14))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y+Inches(0.04),cw-Inches(0.3),Inches(0.4),[[(q,{"size":11,"color":INK})]])
        rev=text(s,x+Inches(0.15),y+Inches(0.42),cw-Inches(0.3),Inches(0.28),[[("→ "+a,{"size":12,"bold":True,"color":GD})]])
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(4.9), Inches(12.3), Inches(0.85),
             [[("Sleutel: ", {"bold":True,"color":GD}),
               ("1 es·está · 2 tengo · 3 son · 4 estamos · 5 tienes · 6 tiene·es · 7 está · 8 sois. ", {"color":GD})],
              [("SER = eigenschap/herkomst (simpática, de Andalucía, morena, majos) · ESTAR = toestand/plaats (en Sevilla, en casa, cansado).", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · CLOZE (verplichte klassieke gap-fill · retrieval). Klas geeft de vorm vóór de klik. Alle vormen nagerekend (U2_bron §4). "
             "Zie het boek §4-cloze. Online: «ser-estar-cloze» + «tener-cloze».")

# ============================================================ DIA 14 · GRAMMAR — demostrativos este/ese (reveal)
def s14_demostrativos():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§5 · GRAMÁTICA", "Demostrativos — este / ese (señala en el álbum)", "Zoom: dit (dichtbij) = este · dat (verder) = ese. Klik → de vorm.", num=5)
    grid=[("este (m. sg.)","deze — dichtbij","Este es mi hermano."),
          ("esta (v. sg.)","deze — dichtbij","Esta es mi abuela."),
          ("estos (m. pl.)","deze — dichtbij","Estos son mis primos."),
          ("estas (v. pl.)","deze — dichtbij","Estas son mis tías."),
          ("ese/esa (sg.)","die — verder","Ese es mi tío."),
          ("esos/esas (pl.)","die — verder","Esas son mis hermanas.")]
    x0,y0=Inches(0.5),Inches(1.7); cw=Inches(4.05); ch=Inches(1.6)
    for i,(a,nl,ej) in enumerate(grid):
        c=i%3; r=i//3; x=x0+c*(cw+Inches(0.13)); y=y0+r*(ch+Inches(0.18))
        card(s,x,y,cw,ch,fill=WHITE,line=G,lw=1.2)
        text(s,x+Inches(0.15),y+Inches(0.1),cw-Inches(0.3),Inches(0.4),[[(a,{"size":15,"bold":True,"color":GD,"font":DISPLAY})]])
        text(s,x+Inches(0.15),y+Inches(0.55),cw-Inches(0.3),Inches(0.32),[[(nl,{"size":10.5,"italic":True,"color":MUT})]])
        rev=text(s,x+Inches(0.15),y+Inches(0.95),cw-Inches(0.3),Inches(0.5),[[("→ "+ej,{"size":11.5,"color":INK})]],line=1.1)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.55), Inches(12.3), Inches(0.6),
             [[("🔴 Ze passen in geslacht én getal bij het zn.: ", {"bold":True,"color":RED}),
               ("este/esta/estos/estas (dichtbij) · ese/esa/esos/esas (verder). Bij foto's: «Este es… / Esta es…».", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · GRAMMAR demostrativos (reveal). Gebruik echte foto's of het árbol: leerling wijst en zegt «Este es mi…». "
             "Zie het boek §5. Online: «este-ese» (classify/point). Voedt de Tarea (fotobijschriften).")

# ============================================================ DIA 15 · READING — La familia de Lucía
def s15_reading():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "§6 · LEER · COMPRENSIÓN", "La familia de Lucía", "Lees het album en beantwoord. Klik een vraag → het antwoord + bewijs.", num=6)
    card(s, Inches(0.5), Inches(1.65), Inches(6.0), Inches(4.5), fill=GT, line=G, lw=1.4)
    avatar(s, "lucia", Inches(0.75), Inches(1.9), Inches(1.0))
    text(s, Inches(1.95), Inches(1.95), Inches(4.35), Inches(4.1),
         [[("«¡Hola! Soy Lucía y esta es mi familia de Sevilla. Somos cinco: mis padres, mi hermano mayor Marco, mi hermana menor Ana y yo. Mi padre se llama Antonio; es alto, moreno y muy tranquilo. Mi madre, Rosa, es baja, rubia y muy habladora. Marco tiene diecinueve años; es delgado y lleva gafas. Ana solo tiene ocho años: es pequeña, graciosa y un poco tímida. También tengo dos abuelos, Pepe y Carmen, y una prima, Julia, que es pelirroja y muy simpática. Hoy todos estamos en casa de los abuelos. ¡Es una familia grande y muy alegre!»",{"size":11,"italic":True,"color":INK})]], line=1.18)
    qa=[("¿Cuántos son en la familia?","Somos cinco (bewijs: «Somos cinco»)"),
        ("¿Cómo es el padre, Antonio?","Alto, moreno y tranquilo"),
        ("¿Cuántos años tiene Marco?","Diecinueve (y lleva gafas)"),
        ("¿Quién es pelirroja?","La prima Julia"),
        ("¿Dónde están hoy todos?","En casa de los abuelos (estar = plaats)")]
    x=Inches(6.65); y=Inches(1.7)
    for q,a in qa:
        card(s,x,y,Inches(6.15),Inches(0.82),fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y+Inches(0.05),Inches(5.85),Inches(0.36),[[(q,{"size":11.5,"bold":True,"color":GD})]])
        rev=text(s,x+Inches(0.15),y+Inches(0.42),Inches(5.85),Inches(0.34),[[("→ "+a,{"size":11,"color":INK})]])
        register_reveal(s, rev)
        y=y+Inches(0.9)
    btn=noodroute(s)
    exercise_solucion(s, Inches(6.65), Inches(6.25), Inches(6.15), Inches(0.5),
             [[("Betekenis uit context: ", {"bold":True,"color":GD}), ("majo ≈ simpático · mayor/menor = ouder/jonger. Daarna: beschrijf je EIGEN familie.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · READING (lezen→schrijven-keten). Voorspellen (waarover?) → globaal → scannen (uren/aantal) → juist/fout + bewijs (evidence) → "
             "betekenis uit context (majo/mayor) → productieve reactie (eigen familie). Zie het boek §6. Online: audio «La familia de Lucía» + V/F-taak.")

# ============================================================ DIA 16 · LISTENING — ¿Quién es? (reveal)
def s16_listening():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "ESCUCHAR · COMPRENSIÓN", "Escucha y adivina — ¿quién es?", "Vier beschrijvingen. Klik een kaart → wie het is. (audio op de digitale pagina)", num=6)
    people=[("«Es alta, rubia y muy habladora.»","→ la madre, Rosa"),
            ("«Es alto, moreno y tranquilo.»","→ el padre, Antonio"),
            ("«Tiene 19 años, es delgado y lleva gafas.»","→ el hermano, Marco"),
            ("«Es pequeña, graciosa y un poco tímida.»","→ la hermana, Ana")]
    x0,y0=Inches(0.5),Inches(1.9); cw=Inches(6.05); ch=Inches(1.3)
    for i,(desc,ans) in enumerate(people):
        c=i%2; r=i//2; x=x0+c*(cw+Inches(0.2)); y=y0+r*(ch+Inches(0.2))
        card(s,x,y,cw,ch,fill=WHITE,line=LINE,lw=1.2)
        rect(s,x,y,cw,Inches(0.45),fill=GT)
        text(s,x+Inches(0.15),y,cw-Inches(0.3),Inches(0.45),[[("🔊  Descripción "+str(i+1),{"size":12,"bold":True,"color":GD,"font":DISPLAY})]],anchor=MSO_ANCHOR.MIDDLE)
        text(s,x+Inches(0.2),y+Inches(0.55),cw-Inches(0.4),Inches(0.4),[[(desc,{"size":12,"italic":True,"color":INK})]])
        rev=text(s,x+Inches(0.2),y+Inches(0.92),cw-Inches(0.4),Inches(0.32),[[(ans,{"size":13,"bold":True,"color":G})]])
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.15), Inches(12.3), Inches(0.7),
             [[("Docent leest de descripciones (of TTS); klas raadt. ", {"bold":True,"color":GD}),
               ("Let op: ser (uiterlijk/karakter) + tener/llevar (haar/gafas). Daarna zelf een familielid beschrijven → de klas raadt.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · LISTENING (selectief → spreken). Lees elke descripción voor (of TTS). Klas raadt wie. "
             "Keten: luisteren→spreken (eigen beschrijving). Online: recorder «shadowing-lucia» + «quien-es».")

# ============================================================ DIA 17 · SPEAKING — ¿Quién es? (raadspel)
def s17_speaking():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "SPEAKING · INTERACCIÓN", "Juego «¿Quién es?» — describe y adivina", "Beschrijf een familielid → de klas raadt. Steun bouwt af: marco → sleutelwoorden → vrij.", num=4)
    avatar(s, "tu", Inches(11.4), Inches(1.65), Inches(1.3))
    labels=["Relación","Física","Pelo / ojos","Carácter","Estado/lugar","Adivina"]
    frames=["Es mi ___ (hermano/tía…)","Es alto/a, delgado/a…","Tiene el pelo ___ y los ojos ___","Es simpático/a, gracioso/a…","Está en ___ / está ___","¿Quién es? → adivinan"]
    x0,y0=Inches(0.5),Inches(1.85); cw=Inches(3.4); rh=Inches(0.82)
    for i,(lab,fr) in enumerate(zip(labels,frames)):
        c=i//3; r=i%3; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.18))
        card(s,x,y,cw,rh,fill=WHITE,line=G,lw=1.2,shadow=False)
        text(s,x+Inches(0.15),y+Inches(0.05),cw-Inches(0.3),Inches(0.32),[[(lab,{"size":10,"color":MUT})]])
        text(s,x+Inches(0.15),y+Inches(0.36),cw-Inches(0.3),Inches(0.4),[[(fr,{"size":12,"bold":True,"color":GD,"font":DISPLAY})]])
    text(s, Inches(0.5), Inches(5.1), Inches(10.5), Inches(0.5),
         [[("Ronda 1: ", {"size":12,"bold":True,"color":GD}), ("met het marco. ", {"size":12,"color":INK}),
           ("Ronda 2: ", {"size":12,"bold":True,"color":GD}), ("alleen sleutelwoorden. ", {"size":12,"color":INK}),
           ("Ronda 3: ", {"size":12,"bold":True,"color":GD}), ("vrij → grábate online.", {"size":12,"color":INK})]])
    chip(s, Inches(0.5), Inches(4.7), "🎙️ Grábate online · «describe-familiar» / «quien-es»", fill=GT, tcolor=GD, size=11)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.6), Inches(12.3), Inches(0.65),
             [[("Modelo: ", {"bold":True,"color":GD}), ("«Es mi hermana. Es baja y delgada, tiene el pelo largo y los ojos verdes. Es muy graciosa. Está en casa. ¿Quién es?»", {"color":GD})]],
             trigger=btn, title_doc="MODELO · docent")
    foot(s)
    notes(s, "TEACHER · SPEAKING (descriptie → interactie/raadspel). 3 rondes met afbouwende steun. Recycle ser/estar + tener/llevar + adjetivos. "
             "Online: SubstitutionCarousel + recorder. Print blijft bruikbaar zonder opname. Voedt de Tarea «Álbum de familia».")

# ============================================================ DIA 18 · WRITING — Álbum de familia
def s18_writing():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "WRITING · PRODUCCIÓN", "Escribe tu álbum de familia", "Schrijf 6 bijschriften (este es… + descripción). Klik → een modeltekst.", num=4)
    card(s, Inches(0.5), Inches(1.7), Inches(6.0), Inches(3.9), fill=WHITE, line=LINE, lw=1.2)
    text(s, Inches(0.7), Inches(1.85), Inches(5.6), Inches(0.4), [[("✍️ Escribe aquí (pie de foto):", {"size":12,"bold":True,"color":GD})]])
    for i in range(6):
        rect(s, Inches(0.7), Inches(2.4)+i*Inches(0.5), Inches(5.6), Inches(0.01), fill=LINE)
    chk=[("un demostrativo (este/esta es…)",),("la relación (mi hermano, mi tía…)",),("descripción física (es alto, tiene…)",),
         ("el carácter (es simpático/a)",),("un posesivo (mi/mis/nuestro)",),("un conector (y, pero, también, porque)",)]
    x=Inches(6.9); y=Inches(1.7)
    text(s,x,y,Inches(6),Inches(0.4),[[("Checklist:",{"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    for i,(c,) in enumerate(chk):
        text(s,x,y+Inches(0.5)+i*Inches(0.45),Inches(6),Inches(0.4),[[("☐  "+c,{"size":13,"color":INK})]])
    rev=card(s, x, Inches(4.5), Inches(6.0), Inches(1.15), fill=GT, line=G, lw=1.2)
    text(s, x+Inches(0.15), Inches(4.55), Inches(5.7), Inches(1.05),
         [[("Modelo: ", {"size":12,"bold":True,"color":GD}),
           ("«Esta es mi familia. Este es mi padre; es alto, moreno y tranquilo. Esta es mi hermana Ana: es pequeña y muy graciosa, pero un poco tímida. También tengo dos abuelos muy majos.»",{"size":11,"italic":True,"color":INK})]], line=1.14)
    register_reveal(s, rev)
    noodroute(s); foot(s)
    notes(s, "TEACHER · WRITING (lezen→schrijven-keten). Checklist = zichtbare steun; onthul het model pas na het schrijven (retrieval vóór herlezen). "
             "Nakijkfocus: demostrativos, congruentie adjetivos, ser/estar, posesivos, conectores. Voedt de Tarea «Álbum de familia».")

# ============================================================ DIA 19 · TALLER — conectores + ortografía
def s19_taller():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "TALLER DE LENGUA", "Conectores y ortografía", "Klik een item → correcte vorm. Twee gereedschappen om je familie te beschrijven.", num=4)
    text(s, Inches(0.5), Inches(1.5), Inches(6), Inches(0.35), [[("A · conectores", {"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
    conn=[("Es alto ___ delgado.","y","en"),("Es bajo ___ muy fuerte.","pero","maar"),("Mi hermana ___ es morena.","también","ook"),("Es simpática ___ es alegre.","porque","want/omdat")]
    y=Inches(1.95)
    for q,a,gl in conn:
        card(s,Inches(0.5),y,Inches(6.0),Inches(0.6),fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,Inches(0.62),y,Inches(3.4),Inches(0.6),[[(q,{"size":11.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,Inches(4.1),y,Inches(2.3),Inches(0.6),[[(a+" ",{"size":12,"bold":True,"color":GD}),("· "+gl,{"size":9,"italic":True,"color":MUT})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y=y+Inches(0.72)
    text(s, Inches(6.9), Inches(1.5), Inches(6), Inches(0.35), [[("B · mayúsculas y tildes", {"size":14,"bold":True,"color":GD,"font":DISPLAY})]])
    fixes=[("antonio y rosa","Antonio y Rosa"),("es de sevilla","es de Sevilla"),("mi tia","mi tía"),("¿como es?","¿cómo es?")]
    y=Inches(1.95)
    for wrong,right in fixes:
        card(s,Inches(6.9),y,Inches(5.9),Inches(0.6),fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,Inches(7.02),y,Inches(3.0),Inches(0.6),[[(wrong,{"size":12,"color":RED})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,Inches(10.1),y,Inches(2.6),Inches(0.6),[[("→ "+right,{"size":12,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev); y=y+Inches(0.72)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.0), Inches(12.3), Inches(0.85),
             [[("A: ", {"bold":True,"color":GD}), ("y (en) · pero (maar) · también (ook) · 🔴 porque = want ÉN omdat (één woord!).", {"color":GD})],
              [("B: ", {"bold":True,"color":GD}), ("nombres/apellidos/steden met hoofdletter (Antonio, Sevilla); vraagwoorden met tilde (¿cómo? ¿cuántos?); tía/años dragen tilde.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · TALLER. Onthul per klik. Valstrik NL: «want» én «omdat» = porque. Hoofdletters bij eigennamen/steden, tildes op vraagwoorden. "
             "Zie het boek Taller de lengua. Meteen toepassen in de Tarea.")

# ============================================================ DIA 20 · CULTURE — la familia hispana
def s20_cultura():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "CULTURA · PARADA 2", "La familia hispana", "Klik een kaart → het weetje. Grote, hechte families in de Spaanstalige wereld.", num=6)
    cards=[("👪 La familia unida","Grote, hechte families: abuelos, tíos en primos wonen vaak dichtbij en komen vaak samen. «Apodos» (bijnamen): Pepe=José, Paco=Francisco, Lola=Dolores.","Vergelijk met je eigen familie in België."),
           ("🎉 La quinceañera","Het 15e-verjaardagsfeest van een meisje (vooral Latijns-Amerika): een groot familiefeest met jurk, dans en misa. Overgang naar de volwassenheid.","Bestaat er zoiets bij jou? Een lentefeest?"),
           ("🎨 Frida Kahlo","De Mexicaanse schilderes maakte «Mi familia / árbol genealógico»: familie als thema in de kunst. Een geschilderde stamboom.","Maak je eigen árbol genealógico als kunstwerk.")]
    x0,y0=Inches(0.5),Inches(1.7); cw=Inches(4.05); ch=Inches(3.5)
    for i,(t,f,nl) in enumerate(cards):
        x=x0+i*(cw+Inches(0.13))
        card(s,x,y0,cw,ch,fill=WHITE,line=G,lw=1.3)
        rect(s,x,y0,cw,Inches(0.6),fill=GT)
        text(s,x+Inches(0.15),y0,cw-Inches(0.3),Inches(0.6),[[(t,{"size":14,"bold":True,"color":GD,"font":DISPLAY})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(0.2),y0+Inches(0.8),cw-Inches(0.4),Inches(1.9),[[(f,{"size":11.5,"color":INK})]],line=1.2)
        register_reveal(s, rev)
        text(s,x+Inches(0.2),y0+Inches(2.8),cw-Inches(0.4),Inches(0.6),[[(nl,{"size":10,"italic":True,"color":MUT})]],line=1.1)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.45), Inches(12.3), Inches(0.6),
             [[("Actividad: ", {"bold":True,"color":GD}), ("¿cómo es tu familia? ¿grande o pequeña? ¿tenéis apodos? Beschrijf je familie en vergelijk met «la familia hispana».", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · CULTURE (identiteit in diversiteit, LPD 5). Onthul per kaart. La familia hispana (unida + apodos) · la quinceañera · Frida Kahlo (árbol als kunst). "
             "Verbind met de klas: hoe groot is jullie familie? Zie het boek Cultura.")

# ============================================================ DIA 21 · FINAL_MISSION — Álbum de familia
def s21_tarea():
    s = slide(); bg(s, PAPER)
    rect(s, 0, 0, EMU_W, Inches(1.35), fill=GD)
    text(s, Inches(0.5), Inches(0.18), Inches(9.5), Inches(1.0),
         [[("✈ Tarea final · Álbum de familia", {"size":28,"bold":True,"color":WHITE,"font":DISPLAY})],
          [("Maak je familiealbum met árbol genealógico + het raadspel «¿Quién es?».", {"size":13,"italic":True,"color":GT})]])
    avatar(s, "lucia", Inches(11.6), Inches(0.18), Inches(1.0))
    pasos=[("1","Haz tu árbol genealógico","teken je stamboom met de namen"),
           ("2","Escribe los pies de foto","«Este es mi… / Esta es mi…» + descripción física + carácter"),
           ("3","Usa ser y estar","es simpático (ser) · está en casa (estar)"),
           ("4","Preséntalo","a la clase of vlog/audio (digitale pagina)"),
           ("5","Juega «¿Quién es?»","beschrijf één familielid → de klas raadt")]
    y=Inches(1.7)
    for n,es,nl in pasos:
        b=rect(s,Inches(0.5),y,Inches(0.5),Inches(0.5),fill=G,round=True,radius=0.5)
        tf=b.text_frame;tf.vertical_anchor=MSO_ANCHOR.MIDDLE;p=tf.paragraphs[0];p.alignment=PP_ALIGN.CENTER
        rr=p.add_run();rr.text=n;rr.font.size=Pt(15);rr.font.bold=True;rr.font.name=DISPLAY;rr.font.color.rgb=WHITE
        text(s,Inches(1.2),y,Inches(4.3),Inches(0.55),[[(es,{"size":14,"bold":True,"color":GD,"font":DISPLAY})]],anchor=MSO_ANCHOR.MIDDLE)
        text(s,Inches(5.6),y,Inches(7.1),Inches(0.55),[[(nl,{"size":11.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        y=y+Inches(0.62)
    text(s, Inches(0.5), Inches(5.0), Inches(12), Inches(0.35), [[("Rúbrica · ¿lo logré?", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    crit=["familia + tener","adjetivos (congruentie)","ser / estar correct","posesivos + demostrativos"]
    x=Inches(0.5)
    for c in crit:
        chip(s,x,Inches(5.45),"☐ "+c,fill=GT,tcolor=GD,size=11,w=Inches(3.0)); x=x+Inches(3.1)
    text(s, Inches(0.5), Inches(6.05), Inches(12), Inches(0.4),
         [[("🎯 ", {"size":12}), ("Afzender jij · ontvanger de klas/Lucía · doel je familie voorstellen · situatie Lucía deelt haar album, jij het jouwe · resultaat: álbum + árbol + «¿Quién es?».", {"size":11,"italic":True,"color":MUT})]])
    foot(s)
    notes(s, "TEACHER · FINAL_MISSION (communicatieve eindtaak). Afzender/ontvanger/doel/situatie/resultaat expliciet. "
             "Beoordeel met de rúbrica; opname + zelfevaluatie op de digitale pagina («mensaje-familia»). LPD 3·4·7·8 + 5 (cultura) + 1·2 (receptief).")

# ============================================================ DIA 22 · QUIZ — la mezcla (reveal)
def s22_mezcla():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "QUIZ · LA MEZCLA", "Ophaal door elkaar", "Gemengde ophaal van de hele unit. Klik een vraag → het antwoord. (retrieval)", num=6)
    items=[("yo · tener","tengo"),("mi hermana → mis ___ (2)","hermanas"),("«es simpática»: ser o estar","ser (karakter)"),
           ("«está en casa»: ser o estar","estar (plaats)"),("los padres = …","vader + moeder"),("una chica alt__","alta"),
           ("«want/omdat» = …","porque"),("Este es mi… / Esta es mi… → wijzen","demostrativos (dichtbij)")]
    x0,y0=Inches(0.5),Inches(1.75); cw=Inches(6.05); rh=Inches(0.62)
    for i,(q,a) in enumerate(items):
        c=i//4; r=i%4; x=x0+c*(cw+Inches(0.2)); y=y0+r*(rh+Inches(0.16))
        card(s,x,y,cw,rh,fill=WHITE,line=LINE,lw=1.0,shadow=False)
        text(s,x+Inches(0.15),y,Inches(3.4),rh,[[(q,{"size":11.5,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        rev=text(s,x+Inches(3.55),y,cw-Inches(3.7),rh,[[("→ "+a,{"size":12,"bold":True,"color":GD})]],anchor=MSO_ANCHOR.MIDDLE)
        register_reveal(s, rev)
    btn=noodroute(s)
    exercise_solucion(s, Inches(0.5), Inches(5.05), Inches(12.3), Inches(0.55),
             [[("Alles komt terug: ", {"bold":True,"color":GD}), ("familia + tener · congruentie adjetivos · ser/estar · posesivos · demostrativos · conectores.", {"color":GD})]],
             trigger=btn)
    foot(s)
    notes(s, "TEACHER · QUIZ mezcla (retrieval vóór herlezen). Zonder waarschuwing door elkaar. Exit-ticket of tussentijdse check. Online: «la mezcla» + Tetris.")

# ============================================================ DIA 23 · FEEDBACK/REPASO
def s23_repaso():
    s = slide(); bg(s, PAPER)
    sectionbar(s, "REPASO · LO ESENCIAL", "Lo esencial de un vistazo", "De volledige herhaling (spellen, drills) staat online. Hier: de kern + semáforo.", num=6)
    ess=["Familia + tener: tengo·tienes·tiene·tenemos·tenéis·tienen. «Tengo dos hermanos» · leeftijd: «Tengo 14 años».",
         "Posesivos: mi/tu/su + mis/tus/sus (getal) · nuestro/-a/-os/-as. «mi hermana → mis hermanas».",
         "Adjetivos: NÁ het zn. + congruentie o/a/os/as. «una chica alta», «los ojos verdes».",
         "🔴 SER (identiteit/beschrijving: es alta, es de Sevilla) ↔ ESTAR (toestand/plaats: está cansada, está en casa).",
         "Demostrativos: este/esta/estos/estas (dichtbij) · ese/esa/esos/esas (verder). Conectores: y·pero·también·porque."]
    card(s, Inches(0.5), Inches(1.6), Inches(12.3), Inches(2.55), fill=CREMA, line=None)
    y=Inches(1.8)
    for e in ess:
        text(s, Inches(0.8), y, Inches(11.8), Inches(0.45), [[("• ", {"size":13,"bold":True,"color":GD}),(e,{"size":11.5,"color":INK})]])
        y=y+Inches(0.47)
    text(s, Inches(0.5), Inches(4.35), Inches(12), Inches(0.35), [[("Semáforo — ¿cómo lo llevas?", {"size":13,"bold":True,"color":GD,"font":DISPLAY})]])
    can=["familieleden + tener","posesivos (mi/mis…)","adjetivos met congruentie","ser vs. estar","demostrativos (este/ese)"]
    y=Inches(4.8)
    for c in can:
        text(s,Inches(0.8),y,Inches(7.0),Inches(0.4),[[(c,{"size":12,"color":INK})]],anchor=MSO_ANCHOR.MIDDLE)
        for j,(em,col) in enumerate([("🔴",RED),("🟠",AMBER),("🟢",G)]):
            chip(s,Inches(8.0)+j*Inches(1.5),y+Inches(0.03),em+" ",fill=WHITE,tcolor=col,size=12,w=Inches(1.3))
        y=y+Inches(0.42)
    foot(s)
    notes(s, "TEACHER · FEEDBACK/REPASO. Semáforo = zelfevaluatie. Repaso-drills online (spellen + zelfcorrectie). "
             "Bruggetje: U3 «El tiempo vuela» (Barcelona) — la hora, rutina & presente irregular.")

# ============================================================ DIA 24 · TEACHER_NOTES
def s24_teacher():
    s = slide(); bg(s, GD)
    text(s, Inches(0.6), Inches(0.4), Inches(12), Inches(0.8), [[("TEACHER_NOTES · U2 «Mi gente»", {"size":26,"bold":True,"color":WHITE,"font":DISPLAY})]])
    blocks=[("Timing (50 min)","Menu 2' · familia+tener 8' · posesivos 6' · adjetivos+congruencia 10' · ser/estar 12' · demostrativos 4' · lectura/tarea-briefing 8'."),
            ("Kernvalstrikken","ser ↔ estar (beide = «zijn») · adjetivo NÁ het zn. + congruentie o/a · posesivo in getal (mis hermanas) · porque = want ÉN omdat · días/nombres met hoofdletter."),
            ("Differentiatie (zij-instromers)","Alles start vanaf nul. Sterker: física + carácter + ser/estar combineren in het album. Zwakker: familia + tener eerst automatiseren, marco/tabel langer open."),
            ("Digitaal","~20 spellen + flip cards ES↔NL + klikbare kaart + recorder («shadowing-lucia», «describe-familiar», «mensaje-familia») op de página digital. QR's → juiste anker. Conjugador = aparte tool."),
            ("Evaluatie","Tarea «Álbum de familia» met rúbrica (4 criteria). LPD 3·4·7·8·9 + 5 (cultura: familia hispana/quinceañera/Frida) + 1·2 (receptief: «La familia de Lucía»).")]
    y=Inches(1.4)
    for t,b in blocks:
        card(s, Inches(0.5), y, Inches(12.3), Inches(1.0), fill=RGBColor(0x1B,0x63,0x49), line=None)
        text(s, Inches(0.75), y+Inches(0.08), Inches(11.8), Inches(0.4), [[(t, {"size":14,"bold":True,"color":WHITE,"font":DISPLAY})]])
        text(s, Inches(0.75), y+Inches(0.48), Inches(11.8), Inches(0.5), [[(b, {"size":11.5,"color":GT})]], line=1.12)
        y=y+Inches(1.12)
    footer(s, tab=TAB, page=pg())
    notes(s, "Alleen in het docentdeck. Volledige LPD-dekking en didactische route staan in het cursusdossier (U2_bron.md). Vormen (tener/ser/estar) nagerekend volgens §3.")

# ============================================================ RUN + BUILD
def _run_all(include_teacher=True):
    s01_title(); s02_menu(); s03_familia(); s04_tener(); s05_cuantos(); s06_posesivos()
    s07_quiz_posesivo(); s08_fisico(); s09_congruencia(); s10_caracter(); s11_serestar_color()
    s12_serestar_formas(); s13_cloze(); s14_demostrativos(); s15_reading(); s16_listening()
    s17_speaking(); s18_writing(); s19_taller(); s20_cultura(); s21_tarea(); s22_mezcla(); s23_repaso()
    if include_teacher:
        s24_teacher()

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
