#!/usr/bin/env python3
"""De rollenspellen: één gesprek per unit, met een doel en een einde.

WAAROM EEN GESLOTEN SCÈNE EN GEEN VRIJE CHAT
Een open gesprek met een taalmodel loopt op A1 binnen tien minuten vast op
hetzelfde: de leerling typt Nederlands, krijgt vlekkeloos Spaans terug ver boven
zijn niveau, en er wordt niets geleerd — het lijkt alleen zo. Daar helpt maar
één ding tegen, en dat is de vórm: een scène met een rol, een doel en een
einde. De ober vraagt wat je wil drinken; daar zijn maar zoveel antwoorden op.

Bovendien staat er hier geen model achter (auteur 2026-08-09: offline, geen
leerlingtekst die de school verlaat). De partner kent dus alleen wat hieronder
staat — en juist omdat de scène gesloten is, valt dat niet op.

HOE EEN STAP WERKT
Elke `paso` is één beurt van de ober plus wat de leerling daarop kan zeggen:

  di       wat de ober zegt (Spaans) + `nl` als steun eronder
  meta     wat de leerling in deze beurt moet klaarspelen (staat op het scherm)
  hueco    het invulkader: een zin met twee gaten die de leerling zelf typt,
           plus een woordbank als steun. Dit is de bélangrijkste stand — bij
           aanklikken kan een leerling gokken, bij twee gaten moet hij de vorm
           produceren. `respuestas` geeft per gat de aanvaarde antwoorden;
           `mal` legt uit wat er misgaat bij de fout die hier het meest gemaakt
           wordt.
  opciones antwoorden om uit te kiezen — precies één is goed (in één beurt twee,
           omdat afslaan er ook bij hoort). De foute zijn niet willekeurig: het
           zijn de fouten die déze leerling maakt, zoals een verkeerd lidwoord.
           **Twee opties mag.** Waar er maar één zinnige afleider bestaat, is een
           derde erbij verzinnen erger dan niets: een stroman met een Nederlands
           woord erin herkent de leerling meteen als «die zal het niet zijn», en
           dan oefent hij het uitsluiten van onzin in plaats van Spaans.
  acepta   voor wie zelf typt: de patronen die als goed gelden. **Eén ervan
           volstaat** — het zijn alternatieven, geen eisen die allemaal moeten
           kloppen. Ruim genomen, want «quiero una sopa», «para mí una sopa» en
           «una sopa, por favor» zijn alle drie juist en het zou pijnlijk zijn
           ze af te keuren. Wat er verder nog aan schort (kortaf, verkeerd
           lidwoord) vangt de corrector op; die staat los en zwijgt niet omdat
           de beurt geslaagd is.
  pista    de hint na een misser — nooit meteen het antwoord
  modelo   het modelantwoord, pas te zien ná een poging of via «muéstrame»

De patronen zijn JavaScript-regex; ze worden hoofdletter- en accentongevoelig
toegepast (zie `gen_rol.py`, functie `normaliza`), zodat «cafe» ook telt.
"""

# ── de scenario's, per cursus in een eigen bestand ──────────────────────────
# Eén bestand met dertig scènes wordt onleesbaar; per cursus blijft het te
# overzien en kan er aan C4 gewerkt worden zonder C5 aan te raken.
import rol_c5                                  # noqa: E402
import rol_c4                                  # noqa: E402
import rol_c6p                                 # noqa: E402

ROLES = {}
ROLES.update({("C4", u): r for u, r in rol_c4.ROLES.items()})
ROLES.update({("C5", u): r for u, r in rol_c5.ROLES.items()})
ROLES.update({("C6+", u): r for u, r in rol_c6p.ROLES.items()})


def rol(curso, unidad):
    return ROLES.get((curso, unidad))


if __name__ == "__main__":
    for (c, u), r in sorted(ROLES.items()):
        n_op = sum(len(p["opciones"]) for p in r["pasos"])
        print("%-4s U%-2d %-26s %d beurten · %d keuzes"
              % (c, u, r["titulo"], len(r["pasos"]), n_op))
    print("\n%d rollenspellen · nakijken met: python3 rol_check.py" % len(ROLES))
