#!/usr/bin/env python3
"""Genereert nette ronde avatar-PNG's (gekleurde cirkel + initiaal) als placeholder
voor de cast van La Ruta. Echte cast-PNG's komen later; deze zijn verzorgd, niet lelijk."""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(__file__), "assets")
os.makedirs(OUT, exist_ok=True)

# cast: naam -> (initiaal, accentkleur, stad)
CAST = {
    "lucia":   ("L", (224, 122, 95),  "Sevilla"),   # #E07A5F
    "diego":   ("D", (91, 141, 239),  "CDMX"),       # #5B8DEF
    "valen":   ("V", (47, 168, 160),  "Cartagena"),  # #2FA8A0
    "nina":    ("N", (214, 154, 46),  "Cusco"),       # #D69A2E
    "tu":      ("T", (138, 123, 224), "Flandes"),     # #8A7BE0
    "mochila": ("M", (30, 158, 116),  "La Ruta"),      # #1E9E74 (mascotte)
}

SZ = 400  # supersample
def font(size):
    for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"]:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def lighten(c, f=0.82):
    return tuple(int(v + (255 - v) * f) for v in c)

for name, (ini, acc, city) in CAST.items():
    img = Image.new("RGBA", (SZ, SZ), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    pad = 14
    # zachte binnenvlak
    d.ellipse([pad, pad, SZ - pad, SZ - pad], fill=lighten(acc, 0.86))
    # ring
    ring = 22
    d.ellipse([pad, pad, SZ - pad, SZ - pad], outline=acc, width=ring)
    # onderste "buste"-boog in accentkleur voor iets meer karakter
    d.pieslice([SZ*0.14, SZ*0.52, SZ*0.86, SZ*1.25], start=180, end=360, fill=acc)
    # initiaal
    f = font(190)
    tb = d.textbbox((0, 0), ini, font=f)
    tw, th = tb[2] - tb[0], tb[3] - tb[1]
    d.text(((SZ - tw) / 2 - tb[0], SZ*0.30 - tb[1]), ini, font=f, fill=(255, 255, 255))
    img = img.resize((200, 200), Image.LANCZOS)
    img.save(os.path.join(OUT, f"{name}.png"))
    print("avatar:", name)
print("klaar ->", OUT)
