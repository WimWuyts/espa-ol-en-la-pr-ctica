#!/usr/bin/env python3
"""Vult `qr_links.json` met links die via WebSearch gevonden zijn.

Waarom een script en geen handwerk: de 196 onderwerpen worden ronde per ronde
ingevuld, en elke link moet dezelfde behandeling krijgen — scope-filter,
statusveld, herhaalbaar zonder dubbels.

BELANGRIJK OVER DE STATUS. De links zijn **niet inhoudelijk geverifieerd**.
De omgeving kan de pagina's niet openen: het netwerkbeleid laat het domein nu
wél door (de proxy geeft HTTP 200, niet meer 403), maar de site zelf zet er een
bot-controle van SiteGround voor (`/.well-known/sgcaptcha/`) voor bezoekers uit
een datacenter. Wat we hebben is dus de titel en de URL uit het zoekresultaat,
niet de inhoud. Daarom draagt elke link `status: "titel-gecontroleerd"`.

Wat wél gecontroleerd is: de SCOPE. III-Spa-d laat geen futuro simple, geen
condicional en geen subjuntivo toe. Zoekresultaten bevatten die wel degelijk —
bij het zoeken naar de presente kwam «¿Presente de indicativo o de subjuntivo?»
naar boven. Alles wat daarop wijst wordt hier geweigerd, niet stilzwijgend
overgenomen. Ook «avanzado» wordt geweigerd: dat ligt boven A2.
"""
import json
import os
import re

HIER = os.path.dirname(os.path.abspath(__file__))
DOEL = os.path.join(HIER, "qr_links.json")

# Buiten het leerplan (III-Spa-d) of boven het niveau.
VERBODEN = re.compile(
    r"subjuntiv|condicional|futuro[-\s]simple|pluscuamperfecto|avanzad|advanced", re.I)

# (cursus, unit, onderwerp) -> [(titel, url)]
GEVONDEN = {
    ("C5", 0, "alfabet y sonidos"): [
        ("El abecedario", "https://paginadelespanol.com/el-abecedario-espanol/"),
        ("El alfabeto o abecedario", "https://paginadelespanol.com/el-alfabeto-o-abecedario/"),
    ],
    # «acentuación y tilde» leverde geen eigen oefenpagina op — bewust leeg
    # gelaten in plaats van er een pagina bij te slepen die er niet over gaat.
    ("C5", 0, "números 0–100"): [
        ("Los números del 0 al 100", "https://paginadelespanol.com/los-numeros-del-0-al-100/"),
        ("Los números del 0 al 10", "https://paginadelespanol.com/los-numeros-del-0-al-10/"),
        ("Los números del 10 al 20", "https://paginadelespanol.com/los-numeros-del-10-al-20/"),
        ("Escribe el nombre de los números", "https://paginadelespanol.com/nombre-de-los-numeros-espanol/"),
    ],
    ("C6+", 0, "presente regular"): [
        ("Completa con los verbos en presente", "https://paginadelespanol.com/completa-con-los-verbos-en-presente/"),
        ("Juego de memoria: los verbos en presente", "https://paginadelespanol.com/juego-memoria-verbos-presente/"),
        ("Regulares o irregulares", "https://paginadelespanol.com/verbos-regulares-o-irregulares/"),
    ],
    ("C6+", 0, "ser/estar/tener/hacer/ir/dar/venir"): [
        ("El presente de algunos verbos irregulares", "https://paginadelespanol.com/el-presente-de-algunos-verbos-irregulares/"),
        ("SER, ESTAR o TENER", "https://paginadelespanol.com/ser-estar-o-tener/"),
        ("Ser, estar, haber", "https://paginadelespanol.com/ejercicio-ser-estar-haber/"),
        ("Conjuga estos verbos irregulares", "https://paginadelespanol.com/conjuga-estos-verbos-irregulares/"),
        ("Completa con los verbos SER, TENER y LLEVAR", "https://paginadelespanol.com/completa-con-los-verbos-ser-estar-llevar/"),
    ],
    ("C6+", 0, "artículos, género y número"): [
        ("Los artículos", "https://paginadelespanol.com/los-articulos/"),
        ("Completa con los artículos", "https://paginadelespanol.com/articulos/"),
    ],
    ("C6+", 0, "formar preguntas"): [
        ("Interrogativos", "https://paginadelespanol.com/interrogativos/"),
        ("Pronombres interrogativos", "https://paginadelespanol.com/pronombres-interrogativos/"),
        ("Quién, quiénes, cómo, cuándo, dónde…", "https://paginadelespanol.com/quien-quienes-como-cuando-donde/"),
        ("Para hacer preguntas (pronombres interrogativos)", "https://paginadelespanol.com/para-hacer-preguntas-pronombres-interrogativos/"),
        ("¿Qué o cuál?", "https://paginadelespanol.com/que-o-cual/"),
        ("¿Cómo o qué tal?", "https://paginadelespanol.com/como-o-que-tal/"),
    ],
    ("C6+", 0, "saludos"): [
        ("Saludos y despedidas", "https://paginadelespanol.com/saludos-y-despedidas-espanol/"),
    ],
    ("C6+", 0, "presentarse"): [
        ("Preguntas y respuestas", "https://paginadelespanol.com/preguntas-y-respuestas/"),
    ],
    ("C6+", 0, "nacionalidades"): [
        ("Nacionalidades de los países hispanohablantes",
         "https://paginadelespanol.com/nacionalidades-de-los-paises-hispanohablantes/"),
    ],
    ("C6+", 0, "paises"): [
        ("Nacionalidades de los países hispanohablantes",
         "https://paginadelespanol.com/nacionalidades-de-los-paises-hispanohablantes/"),
    ],
    ("C6+", 0, "descripcion"): [
        ("60 adjetivos para describir a una persona",
         "https://paginadelespanol.com/60-adjetivos-para-describir-a-una-persona/"),
        ("La personalidad", "https://paginadelespanol.com/la-personalidad/"),
        ("Adjetivos", "https://paginadelespanol.com/ejercicio-adjetivos/"),
        ("Adjetivos y sus contrarios", "https://paginadelespanol.com/adjetivos-y-sus-contrarios/"),
    ],
    ("C6+", 0, "familia"): [
        ("Mi familia", "https://paginadelespanol.com/mi-familia/"),
    ],
    ("C6+", 0, "verbos"): [
        ("Conjuga estos verbos irregulares", "https://paginadelespanol.com/conjuga-estos-verbos-irregulares/"),
    ],
    ("C6+", 0, "numeros"): [
        ("Los números del 0 al 100", "https://paginadelespanol.com/los-numeros-del-0-al-100/"),
    ],
}


def main():
    data = json.load(open(DOEL, encoding="utf-8"))
    index = {(u["curso"], u["unidad"]): u for u in data}
    toegevoegd = geweigerd = 0
    for (curso, unidad, onderwerp), links in GEVONDEN.items():
        unit = index.get((curso, unidad))
        assert unit, "onbekende unit: %s U%s" % (curso, unidad)
        doel = next((o for o in unit["onderwerpen"] if o["onderwerp"] == onderwerp), None)
        assert doel, "onbekend onderwerp: %s U%s · %s" % (curso, unidad, onderwerp)
        bestaand = {u["url"] for u in doel["urls"]}
        for titulo, url in links:
            if VERBODEN.search(titulo) or VERBODEN.search(url):
                geweigerd += 1
                continue
            if url in bestaand:
                continue
            doel["urls"].append({
                "titulo": titulo, "url": url,
                "bron": "websearch",
                "status": "titel-gecontroleerd",   # inhoud niet opgehaald: bot-controle van de site
            })
            toegevoegd += 1

    json.dump(data, open(DOEL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    tot = sum(len(u["onderwerpen"]) for u in data)
    ing = sum(1 for u in data for o in u["onderwerpen"] if o["urls"])
    print("%d links toegevoegd · %d geweigerd (buiten III-Spa-d of boven niveau)" % (toegevoegd, geweigerd))
    print("onderwerpen met minstens één link: %d / %d" % (ing, tot))


if __name__ == "__main__":
    main()
