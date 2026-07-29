# -*- coding: utf-8 -*-
# mapa_c6plus.py — route (PARADAS) + themalagen (UNIT_TEMA) voor C6+ (paars).
# Gebruikt de gedeelde feitenlaag paises_data.py (cursus-onafhankelijk).
# Elke unit krijgt één meebewegende themalaag; thema_key MOET in paises_data.TEMAS bestaan.

# ---- welke themalaag per C6+-unit (8 units, U0–U7) ----
# Bewust 8 verschillende thema's zodat de kaart per unidad «meebeweegt».
UNIT_TEMA = {
 0: ("simbolo", "🌎 Símbolo"),          # U0 ¡Volvemos! — el mundo hispano
 1: ("rutina",  "🕐 El ritmo del día"),  # U1 El día a día — rutina/horario
 2: ("lugar",   "🏙️ Un lugar"),          # U2 Aquí vivo — wonen/barrio
 3: ("musica",  "🎵 Música"),            # U3 Conectados — media/cultuur
 4: ("viaje",   "✈️ Para visitar"),       # U4 De viaje — reizen
 5: ("persona", "⭐ Alguien de aquí"),    # U5 Érase una vez — biografieën
 6: ("familia", "👪 En familia"),         # U6 Cuando era pequeño — jeugd/vroeger
 7: ("comida",  "🍽️ En la mesa"),         # U7 ¡Opina y cuídate! — gezondheid/eten
}

# ---- La Ruta van C6+: {landcode: (start-unit, "rango", "NL-beschrijving")} ----
# «Terugkeer»-vertrekpunt (España), daarna over de Spaanstalige wereld met de vaste cast.
# Provisoir vanaf U3 (wordt herzien bij het bouwen van die units); U0–U2 = vastgelegd.
PARADAS = {
 "ESP": (0, "U0–U1", "el mundo hispano · España (Lucía)"),
 "COL": (2, "U2",    "Cartagena (Valen)"),
 "MEX": (3, "U3",    "CDMX (Diego)"),
 "CHL": (4, "U4",    "Chile · el gran viaje (Patagonia, Atacama)"),
 "ARG": (5, "U5",    "Buenos Aires (Mateo · voseo)"),
 "PER": (6, "U6",    "Cusco (Nina)"),
 "CRI": (7, "U7",    "Costa Rica · «pura vida» (salud y medio ambiente)"),
}
