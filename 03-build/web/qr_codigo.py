#!/usr/bin/env python3
"""Echte QR-codes, in pure Python — geen bibliotheek, want er is er geen.

WAAROM ZELF GESCHREVEN
De sandbox kan niet bij PyPI (403) en niet bij npm, dus `segno`, `qrcode` en de
JS-varianten vallen af. Tot nu stond er in de cursus een *nep*-QR: een SVG met
willekeurige blokjes die er van een afstand uitzag als een code maar nergens
naartoe leidde. Dat is precies het soort ding dat een leerling één keer probeert
en daarna nooit meer. Dus: een echte encoder.

WAT HET KAN
Byte-modus (ISO-8859-1 / ASCII), versies 1 t/m 10, foutcorrectie L/M/Q/H, met
maskerkeuze volgens de norm (de acht maskers worden alle acht geprobeerd en de
laagste strafscore wint). Dat is ruim genoeg voor een URL van ~150 tekens op
niveau M — en met niveau Q blijft een code leesbaar ook als de druk vuil is of
een leerling er met zijn duim op staat.

    from qr_codigo import qr_svg
    svg = qr_svg("https://example.com/c5-u0.html#esc_1", mm=18)

De implementatie volgt ISO/IEC 18004. Ze is geverifieerd tegen het
referentievoorbeeld uit de norm (numeriek «01234567», versie 1-M) én met een
eigen decoder die de gelegde matrix weer uitleest — zie `autotest()` onderaan.
"""

# ---------------------------------------------------------------------------
# Galois-veld GF(256), met het QR-priemveelterm 0x11D
# ---------------------------------------------------------------------------

_EXP = [0] * 512
_LOG = [0] * 256


def _init_gf():
    x = 1
    for i in range(255):
        _EXP[i] = x
        _LOG[x] = i
        x <<= 1
        if x & 0x100:
            x ^= 0x11D
    for i in range(255, 512):
        _EXP[i] = _EXP[i - 255]


_init_gf()


def _gf_mul(a, b):
    if a == 0 or b == 0:
        return 0
    return _EXP[_LOG[a] + _LOG[b]]


def _rs_generador(n):
    """Generatorveelterm van graad n, coëfficiënten hoog→laag."""
    g = [1]
    for i in range(n):
        nueva = [0] * (len(g) + 1)
        for j, c in enumerate(g):
            nueva[j] ^= _gf_mul(c, 1)
            nueva[j + 1] ^= _gf_mul(c, _EXP[i])
        g = nueva
    return g


def _rs_ecc(datos, n):
    """De n foutcorrectie-codewoorden bij een blok databytes."""
    gen = _rs_generador(n)
    resto = list(datos) + [0] * n
    for i in range(len(datos)):
        factor = resto[i]
        if factor:
            for j, c in enumerate(gen):
                resto[i + j] ^= _gf_mul(c, factor)
    return resto[len(datos):]


# ---------------------------------------------------------------------------
# Capaciteitstabellen (ISO/IEC 18004, tabellen 7–9), versies 1–10
# ---------------------------------------------------------------------------

# per versie: totaal aantal codewoorden in het symbool
_TOTAL_CW = {1: 26, 2: 44, 3: 70, 4: 100, 5: 134,
             6: 172, 7: 196, 8: 242, 9: 292, 10: 346}

# per (versie, niveau): (ecc-codewoorden per blok, blokken groep 1,
#                        datacodewoorden per blok groep 1,
#                        blokken groep 2, datacodewoorden per blok groep 2)
_ECC = {
    (1, 'L'): (7, 1, 19, 0, 0),   (1, 'M'): (10, 1, 16, 0, 0),
    (1, 'Q'): (13, 1, 13, 0, 0),  (1, 'H'): (17, 1, 9, 0, 0),
    (2, 'L'): (10, 1, 34, 0, 0),  (2, 'M'): (16, 1, 28, 0, 0),
    (2, 'Q'): (22, 1, 22, 0, 0),  (2, 'H'): (28, 1, 16, 0, 0),
    (3, 'L'): (15, 1, 55, 0, 0),  (3, 'M'): (26, 1, 44, 0, 0),
    (3, 'Q'): (18, 2, 17, 0, 0),  (3, 'H'): (22, 2, 13, 0, 0),
    (4, 'L'): (20, 1, 80, 0, 0),  (4, 'M'): (18, 2, 32, 0, 0),
    (4, 'Q'): (26, 2, 24, 0, 0),  (4, 'H'): (16, 4, 9, 0, 0),
    (5, 'L'): (26, 1, 108, 0, 0), (5, 'M'): (24, 2, 43, 0, 0),
    (5, 'Q'): (18, 2, 15, 2, 16), (5, 'H'): (22, 2, 11, 2, 12),
    (6, 'L'): (18, 2, 68, 0, 0),  (6, 'M'): (16, 4, 27, 0, 0),
    (6, 'Q'): (24, 4, 19, 0, 0),  (6, 'H'): (28, 4, 15, 0, 0),
    (7, 'L'): (20, 2, 78, 0, 0),  (7, 'M'): (18, 4, 31, 0, 0),
    (7, 'Q'): (18, 2, 14, 4, 15), (7, 'H'): (26, 4, 13, 1, 14),
    (8, 'L'): (24, 2, 97, 0, 0),  (8, 'M'): (22, 2, 38, 2, 39),
    (8, 'Q'): (22, 4, 18, 2, 19), (8, 'H'): (26, 4, 14, 2, 15),
    (9, 'L'): (30, 2, 116, 0, 0), (9, 'M'): (22, 3, 36, 2, 37),
    (9, 'Q'): (20, 4, 16, 4, 17), (9, 'H'): (24, 4, 12, 4, 13),
    (10, 'L'): (18, 2, 68, 2, 69), (10, 'M'): (26, 4, 43, 1, 44),
    (10, 'Q'): (24, 6, 19, 2, 20), (10, 'H'): (28, 6, 15, 2, 16),
}

# middelpunten van de uitlijnpatronen per versie
_ALINEACION = {1: [], 2: [6, 18], 3: [6, 22], 4: [6, 26], 5: [6, 30],
               6: [6, 34], 7: [6, 22, 38], 8: [6, 24, 42], 9: [6, 26, 46],
               10: [6, 28, 50]}

_NIVEL_BITS = {'L': 0b01, 'M': 0b00, 'Q': 0b11, 'H': 0b10}


def _capacidad(version, nivel):
    ecc, b1, d1, b2, d2 = _ECC[(version, nivel)]
    return b1 * d1 + b2 * d2


# ---------------------------------------------------------------------------
# Bitstroom
# ---------------------------------------------------------------------------

class _Bits:
    def __init__(self):
        self.bits = []

    def add(self, valor, largo):
        for i in range(largo - 1, -1, -1):
            self.bits.append((valor >> i) & 1)

    def __len__(self):
        return len(self.bits)


def _codificar(datos, version, nivel):
    """Byte-modus → de volledige rij datacodewoorden, met opvulling."""
    cap = _capacidad(version, nivel) * 8
    b = _Bits()
    b.add(0b0100, 4)                                   # modus: byte
    b.add(len(datos), 8 if version < 10 else 16)       # lengteveld
    for byte in datos:
        b.add(byte, 8)
    # afsluiter: maximaal vier nullen, en dan aanvullen tot een hele byte
    b.add(0, min(4, cap - len(b)))
    while len(b) % 8:
        b.bits.append(0)
    # opvulbytes, afwisselend 11101100 / 00010001, tot het symbool vol is
    relleno = [0xEC, 0x11]
    i = 0
    while len(b) < cap:
        b.add(relleno[i % 2], 8)
        i += 1
    return [int("".join(str(x) for x in b.bits[k:k + 8]), 2)
            for k in range(0, len(b.bits), 8)]


def _intercalar(cw, version, nivel):
    """Data en ECC blok voor blok verweven, zoals de norm voorschrijft."""
    n_ecc, b1, d1, b2, d2 = _ECC[(version, nivel)]
    bloques, i = [], 0
    for _ in range(b1):
        bloques.append(cw[i:i + d1]); i += d1
    for _ in range(b2):
        bloques.append(cw[i:i + d2]); i += d2
    eccs = [_rs_ecc(bl, n_ecc) for bl in bloques]

    salida = []
    for k in range(max(len(bl) for bl in bloques)):
        for bl in bloques:
            if k < len(bl):
                salida.append(bl[k])
    for k in range(n_ecc):
        for e in eccs:
            salida.append(e[k])
    return salida


# ---------------------------------------------------------------------------
# De matrix
# ---------------------------------------------------------------------------

def _matriz_base(version):
    """Lege matrix plus een masker dat zegt welke cellen functiepatroon zijn."""
    n = version * 4 + 17
    m = [[0] * n for _ in range(n)]
    fijo = [[False] * n for _ in range(n)]

    def buscador(fila, col):
        for dy in range(-1, 8):
            for dx in range(-1, 8):
                y, x = fila + dy, col + dx
                if 0 <= y < n and 0 <= x < n:
                    borde = dy in (-1, 7) or dx in (-1, 7)
                    anillo = dy in (0, 6) or dx in (0, 6)
                    centro = 2 <= dy <= 4 and 2 <= dx <= 4
                    m[y][x] = 0 if borde else (1 if (anillo or centro) else 0)
                    fijo[y][x] = True

    buscador(0, 0); buscador(0, n - 7); buscador(n - 7, 0)

    # tijdpatronen
    for i in range(8, n - 8):
        v = 1 - (i % 2)
        m[6][i] = v; fijo[6][i] = True
        m[i][6] = v; fijo[i][6] = True

    # uitlijnpatronen, behalve waar ze op een zoeker zouden vallen
    centros = _ALINEACION[version]
    for a in centros:
        for b in centros:
            if (a, b) in ((6, 6), (6, centros[-1]), (centros[-1], 6)):
                continue
            for dy in range(-2, 3):
                for dx in range(-2, 3):
                    m[a + dy][b + dx] = 1 if (max(abs(dy), abs(dx)) != 1) else 0
                    fijo[a + dy][b + dx] = True

    # de donkere module en de plaats van de formaatinformatie
    m[n - 8][8] = 1; fijo[n - 8][8] = True
    for i in range(9):
        if not fijo[8][i]:
            fijo[8][i] = True
        if not fijo[i][8]:
            fijo[i][8] = True
    for i in range(8):
        fijo[8][n - 1 - i] = True
        fijo[n - 1 - i][8] = True

    # versie-informatie (vanaf versie 7) — hier gereserveerd
    if version >= 7:
        for i in range(6):
            for j in range(3):
                fijo[n - 11 + j][i] = True
                fijo[i][n - 11 + j] = True
    return m, fijo


def _colocar(m, fijo, datos):
    """De datastroom in zigzag leggen, van rechtsonder naar boven."""
    n = len(m)
    bits = []
    for byte in datos:
        for i in range(7, -1, -1):
            bits.append((byte >> i) & 1)
    idx = 0
    col = n - 1
    arriba = True
    while col > 0:
        if col == 6:            # de tijdkolom wordt overgeslagen
            col -= 1
        filas = range(n - 1, -1, -1) if arriba else range(n)
        for fila in filas:
            for dx in (0, 1):
                x = col - dx
                if not fijo[fila][x]:
                    m[fila][x] = bits[idx] if idx < len(bits) else 0
                    idx += 1
        col -= 2
        arriba = not arriba
    return m


def _mascara(fila, col, k):
    if k == 0: return (fila + col) % 2 == 0
    if k == 1: return fila % 2 == 0
    if k == 2: return col % 3 == 0
    if k == 3: return (fila + col) % 3 == 0
    if k == 4: return (fila // 2 + col // 3) % 2 == 0
    if k == 5: return (fila * col) % 2 + (fila * col) % 3 == 0
    if k == 6: return ((fila * col) % 2 + (fila * col) % 3) % 2 == 0
    return ((fila + col) % 2 + (fila * col) % 3) % 2 == 0


_FORMATO_G = 0b10100110111
_FORMATO_MASCARA = 0b101010000010010


def _bits_formato(nivel, mascara):
    datos = (_NIVEL_BITS[nivel] << 3) | mascara
    resto = datos << 10
    for i in range(4, -1, -1):
        if resto & (1 << (i + 10)):
            resto ^= _FORMATO_G << i
    return ((datos << 10) | resto) ^ _FORMATO_MASCARA


_VERSION_G = 0b1111100100101


def _bits_version(version):
    resto = version << 12
    for i in range(5, -1, -1):
        if resto & (1 << (i + 12)):
            resto ^= _VERSION_G << i
    return (version << 12) | resto


def _poner_formato(m, nivel, mascara):
    n = len(m)
    bits = _bits_formato(nivel, mascara)
    for i in range(15):
        b = (bits >> i) & 1
        if i < 6:
            m[8][i] = b
        elif i == 6:
            m[8][7] = b
        elif i == 7:
            m[8][8] = b
        elif i == 8:
            m[7][8] = b
        else:
            m[14 - i][8] = b
    for i in range(15):
        b = (bits >> i) & 1
        if i < 8:
            m[n - 1 - i][8] = b
        else:
            m[8][n - 15 + i] = b
    m[n - 8][8] = 1
    return m


def _poner_version(m, version):
    if version < 7:
        return m
    n = len(m)
    bits = _bits_version(version)
    for i in range(18):
        b = (bits >> i) & 1
        fila, col = i // 3, i % 3
        m[n - 11 + col][fila] = b
        m[fila][n - 11 + col] = b
    return m


def _penalizacion(m):
    """De vier strafregels uit de norm; de laagste som wint."""
    n = len(m)
    total = 0

    # 1 · rijen of kolommen van vijf of meer gelijke modules
    for linea in list(m) + [list(col) for col in zip(*m)]:
        run, prev = 1, linea[0]
        for v in linea[1:]:
            if v == prev:
                run += 1
            else:
                if run >= 5:
                    total += 3 + (run - 5)
                run, prev = 1, v
        if run >= 5:
            total += 3 + (run - 5)

    # 2 · blokken van 2×2
    for y in range(n - 1):
        for x in range(n - 1):
            if m[y][x] == m[y][x + 1] == m[y + 1][x] == m[y + 1][x + 1]:
                total += 3

    # 3 · het zoekerpatroon 1:1:3:1:1 met vier lichte modules ernaast
    patrones = ([1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1])
    for linea in list(m) + [list(col) for col in zip(*m)]:
        for i in range(n - 10):
            trozo = linea[i:i + 11]
            if trozo in patrones:
                total += 40

    # 4 · afwijking van vijftig procent donker
    oscuro = sum(sum(f) for f in m)
    porcentaje = oscuro * 100 // (n * n)
    total += 10 * (min(abs(porcentaje - 50) // 5, 10))
    return total


# ---------------------------------------------------------------------------
# Publiek
# ---------------------------------------------------------------------------

def matriz(texto, nivel='M', version=None):
    """De QR-matrix als lijst van rijen met nullen en enen."""
    datos = texto.encode('iso-8859-1', 'replace')
    if version is None:
        for v in range(1, 11):
            cabecera = 4 + (8 if v < 10 else 16)
            if (cabecera + len(datos) * 8) <= _capacidad(v, nivel) * 8:
                version = v
                break
        else:
            raise ValueError("te lang voor versie 10 op niveau %s: %d tekens"
                             % (nivel, len(datos)))
    cw = _intercalar(_codificar(datos, version, nivel), version, nivel)

    mejor, mejor_pena = None, None
    for k in range(8):
        m, fijo = _matriz_base(version)
        _colocar(m, fijo, cw)
        for y in range(len(m)):
            for x in range(len(m)):
                if not fijo[y][x] and _mascara(y, x, k):
                    m[y][x] ^= 1
        _poner_formato(m, nivel, k)
        _poner_version(m, version)
        pena = _penalizacion(m)
        if mejor_pena is None or pena < mejor_pena:
            mejor, mejor_pena = m, pena
    return mejor


def qr_svg(texto, mm=18, nivel='M', quiet=4, color="#20242E", fondo="#fff"):
    """Een QR-code als inline SVG, klaar om in de print-HTML te zetten.

    `quiet` is de verplichte stille rand; zonder die rand leest geen enkele
    scanner de code, ook al ziet ze er goed uit.
    """
    m = matriz(texto, nivel)
    n = len(m)
    total = n + 2 * quiet
    # één pad voor alle donkere modules: veel kleiner dan losse rects
    partes = []
    for y, fila in enumerate(m):
        x = 0
        while x < n:
            if fila[x]:
                ancho = 1
                while x + ancho < n and fila[x + ancho]:
                    ancho += 1
                partes.append("M%d %dh%dv1h-%dz" % (x + quiet, y + quiet, ancho, ancho))
                x += ancho
            else:
                x += 1
    return ('<svg width="%(mm)smm" height="%(mm)smm" viewBox="0 0 %(t)d %(t)d" '
            'shape-rendering="crispEdges" role="img" aria-label="QR-code">'
            '<rect width="%(t)d" height="%(t)d" fill="%(f)s"/>'
            '<path d="%(p)s" fill="%(c)s"/></svg>'
            % {"mm": mm, "t": total, "p": "".join(partes), "c": color, "f": fondo})


# ---------------------------------------------------------------------------
# Zelftest — een encoder die je niet nagerekend hebt, is een tekening
# ---------------------------------------------------------------------------

def _leer(m, version, nivel, mascara):
    """Onafhankelijke uitlezer: haalt de datastroom weer uit de matrix."""
    _, fijo = _matriz_base(version)
    n = len(m)
    bits = []
    col, arriba = n - 1, True
    while col > 0:
        if col == 6:
            col -= 1
        for fila in (range(n - 1, -1, -1) if arriba else range(n)):
            for dx in (0, 1):
                x = col - dx
                if not fijo[fila][x]:
                    b = m[fila][x]
                    if _mascara(fila, x, mascara):
                        b ^= 1
                    bits.append(b)
        col -= 2
        arriba = not arriba
    return [int("".join(str(b) for b in bits[i:i + 8]), 2)
            for i in range(0, len(bits) // 8 * 8, 8)]


def _desintercalar(cw, version, nivel):
    """De omgekeerde van `_intercalar`: de datacodewoorden weer op een rij."""
    n_ecc, b1, d1, b2, d2 = _ECC[(version, nivel)]
    largos = [d1] * b1 + [d2] * b2
    bloques = [[] for _ in largos]
    i = 0
    for k in range(max(largos)):
        for j, largo in enumerate(largos):
            if k < largo:
                bloques[j].append(cw[i]); i += 1
    return [b for bl in bloques for b in bl]


def _decodificar(datos, version):
    """Byte-modus terug naar tekst — de tegenhanger van `_codificar`."""
    bits = []
    for byte in datos:
        for i in range(7, -1, -1):
            bits.append((byte >> i) & 1)

    def leer(n, pos):
        v = 0
        for b in bits[pos:pos + n]:
            v = (v << 1) | b
        return v, pos + n

    modo, p = leer(4, 0)
    if modo != 0b0100:
        raise ValueError("geen byte-modus (%d)" % modo)
    largo, p = leer(8 if version < 10 else 16, p)
    cuerpo = []
    for _ in range(largo):
        v, p = leer(8, p)
        cuerpo.append(v)
    return bytes(cuerpo).decode('iso-8859-1')


def _mascara_de(m):
    """Het gebruikte masker uit de formaatinformatie halen."""
    leidos = 0
    for i in range(15):
        if i < 6:
            b = m[8][i]
        elif i == 6:
            b = m[8][7]
        elif i == 7:
            b = m[8][8]
        elif i == 8:
            b = m[7][8]
        else:
            b = m[14 - i][8]
        leidos |= b << i
    for nivel in ('L', 'M', 'Q', 'H'):
        for k in range(8):
            if _bits_formato(nivel, k) == leidos:
                return nivel, k
    raise ValueError("formaatinformatie onleesbaar")


def autotest():
    fallos = []

    # 1 · het referentievoorbeeld uit de norm: «01234567», versie 1-M.
    #     De ECC-codewoorden staan in de norm uitgeschreven; als onze
    #     Reed-Solomon klopt, komen we er exact op uit.
    datos = [0x10, 0x20, 0x0C, 0x56, 0x61, 0x80, 0xEC, 0x11,
             0xEC, 0x11, 0xEC, 0x11, 0xEC, 0x11, 0xEC, 0x11]
    esperado = [0xA5, 0x24, 0xD4, 0xC1, 0xED, 0x36, 0xC7, 0x87, 0x2C, 0x55]
    obtenido = _rs_ecc(datos, 10)
    if obtenido != esperado:
        fallos.append("Reed-Solomon wijkt af van het normvoorbeeld: %s" % obtenido)

    # 2 · volledige rondrit, ook over de versies met meerdere blokken:
    #     coderen → matrix leggen → masker en niveau uit de formaatbits halen →
    #     uitlezen → ontweven → decoderen → moet exact de oorspronkelijke tekst zijn.
    URL = "https://espanol-en-la-practica.wim-wuyts1979.chatgpt.site/"
    pruebas = ["HOLA", URL, URL + "c5-u0.html#esc_1",
               URL + "c6plus-u7.html#retos_c6p_u7", "a" * 100,
               "¿Qué tal? · acentos: áéíóú ñ ¡!"]
    for texto in pruebas:
        for nivel in ("L", "M", "Q", "H"):
            try:
                m = matriz(texto, nivel)
                version = (len(m) - 17) // 4
                nivel_leido, k = _mascara_de(m)
                if nivel_leido != nivel:
                    fallos.append("niveau verkeerd gelezen: %s → %s" % (nivel, nivel_leido))
                    continue
                cw = _leer(m, version, nivel, k)
                d = _desintercalar(cw, version, nivel)
                vuelta = _decodificar(d, version)
                esperada = texto.encode('iso-8859-1', 'replace').decode('iso-8859-1')
                if vuelta != esperada:
                    fallos.append("rondrit %s/%s: %r ≠ %r"
                                  % (nivel, version, vuelta[:40], esperada[:40]))
            except Exception as e:
                fallos.append("rondrit %r op %s: %s" % (texto[:24], nivel, e))

    # 3 · vorm van het symbool: zoekers, tijdpatroon, donkere module
    m = matriz("test", 'M')
    n = len(m)
    if not (m[0][0] == m[0][6] == m[6][0] == m[6][6] == 1):
        fallos.append("zoeker linksboven klopt niet")
    if m[n - 8][8] != 1:
        fallos.append("de donkere module ontbreekt")
    if [m[6][i] for i in range(8, 12)] != [1, 0, 1, 0]:
        fallos.append("het tijdpatroon klopt niet")

    # 4 · te lange invoer hoort te weigeren in plaats van stil af te kappen
    try:
        matriz("x" * 400, 'H')
        fallos.append("te lange tekst werd niet geweigerd")
    except ValueError:
        pass

    # 5 · de stille rand moet in de SVG zitten, anders leest geen scanner mee
    svg = qr_svg("test")
    if 'viewBox="0 0 29 29"' not in svg:      # 21 modules + 2×4 rand
        fallos.append("de stille rand ontbreekt in de SVG")

    return fallos


if __name__ == "__main__":
    problemas = autotest()
    if problemas:
        for p in problemas:
            print("FOUT:", p)
        raise SystemExit(1)
    m = matriz("https://espanol-en-la-practica.wim-wuyts1979.chatgpt.site/c5-u0.html#esc_1")
    print("zelftest in orde · symbool %dx%d modules" % (len(m), len(m)))
    for fila in m:
        print("".join("██" if v else "  " for v in fila))
