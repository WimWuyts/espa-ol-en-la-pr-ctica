# -*- coding: utf-8 -*-
"""Gedeelde vocab-iconen voor de C5-hubs (flashcards).

Levert per woord een consistent Lucide-lijnicoon (MIT), lijnstijl,
stroke="currentColor" fill="none" stroke-width=2 — grijswaarden-veilig.
Gebruikt door gen_u0_web.py / gen_u1_web.py / gen_u3_web.py / gen_u4_web.py
(en zo de template voor U2/U5+).

Keuzevolgorde in icon_svg():
  1) exact lemma in WORD_ICON
  2) trefwoord-substring in KEYWORD_ICON
  3) GROUP_ICON[group]  (fallback per vocab-groep → élke kaart krijgt een icoon)
  4) DEFAULT ("tag")
"""

# --------------------------------------------------------------------------
# LUCIDE = {naam: "<svg inner path-data>"}  (officiële Lucide 24x24 paden)
# --------------------------------------------------------------------------
LUCIDE = {
 "tag": '<path d="M12.586 2.586A2 2 0 0 0 11.172 2H4a2 2 0 0 0-2 2v7.172a2 2 0 0 0 .586 1.414l8.704 8.704a2.426 2.426 0 0 0 3.42 0l6.58-6.58a2.426 2.426 0 0 0 0-3.42z"/><circle cx="7.5" cy="7.5" r=".5" fill="currentColor"/>',
 "user": '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
 "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
 "clock": '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
 "watch": '<circle cx="12" cy="12" r="6"/><polyline points="12 10 12 12 13 13"/><path d="m16.13 7.66-.81-4.05a2 2 0 0 0-2-1.61h-2.68a2 2 0 0 0-2 1.61l-.78 4.05"/><path d="m7.88 16.36.8 4a2 2 0 0 0 2 1.61h2.72a2 2 0 0 0 2-1.61l.81-4.05"/>',
 "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/>',
 "moon": '<path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/>',
 "sunrise": '<path d="M12 2v8"/><path d="m4.93 10.93 1.41 1.41"/><path d="M2 18h2"/><path d="M20 18h2"/><path d="m19.07 10.93-1.41 1.41"/><path d="M22 22H2"/><path d="m8 6 4-4 4 4"/><path d="M16 18a4 4 0 0 0-8 0"/>',
 "sunset": '<path d="M12 10V2"/><path d="m4.93 10.93 1.41 1.41"/><path d="M2 18h2"/><path d="M20 18h2"/><path d="m19.07 10.93-1.41 1.41"/><path d="M22 22H2"/><path d="m16 6-4 4-4-4"/><path d="M16 18a4 4 0 0 0-8 0"/>',
 "calendar": '<rect width="18" height="18" x="3" y="4" rx="2" ry="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/>',
 "calendar-check": '<path d="M8 2v4"/><path d="M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/><path d="m9 16 2 2 4-4"/>',
 "repeat": '<path d="m17 2 4 4-4 4"/><path d="M3 11v-1a4 4 0 0 1 4-4h14"/><path d="m7 22-4-4 4-4"/><path d="M21 13v1a4 4 0 0 1-4 4H3"/>',
 "globe": '<circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/>',
 "flag": '<path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" x2="4" y1="22" y2="15"/>',
 "map-pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
 "route": '<circle cx="6" cy="19" r="3"/><path d="M9 19h8.5a3.5 3.5 0 0 0 0-7h-11a3.5 3.5 0 0 1 0-7H15"/><circle cx="18" cy="5" r="3"/>',
 "music": '<path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/>',
 "heart": '<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>',
 "thumbs-up": '<path d="M7 10v12"/><path d="M15 5.88 14 10h5.83a2 2 0 0 1 1.92 2.56l-2.33 8A2 2 0 0 1 17.5 22H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h2.76a2 2 0 0 0 1.79-1.11L12 2a3.13 3.13 0 0 1 3 3.88Z"/>',
 "smile": '<circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" x2="9.01" y1="9" y2="9"/><line x1="15" x2="15.01" y1="9" y2="9"/>',
 "frown": '<circle cx="12" cy="12" r="10"/><path d="M16 16s-1.5-2-4-2-4 2-4 2"/><line x1="9" x2="9.01" y1="9" y2="9"/><line x1="15" x2="15.01" y1="9" y2="9"/>',
 "star": '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
 "help-circle": '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" x2="12.01" y1="17" y2="17"/>',
 "message-circle": '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>',
 "hand": '<path d="M18 11V6a2 2 0 0 0-2-2a2 2 0 0 0-2 2"/><path d="M14 10V4a2 2 0 0 0-2-2a2 2 0 0 0-2 2v2"/><path d="M10 10.5V6a2 2 0 0 0-2-2a2 2 0 0 0-2 2v8"/><path d="M18 8a2 2 0 1 1 4 0v6a8 8 0 0 1-8 8h-2c-2.8 0-4.5-.86-5.99-2.34l-3.6-3.6a2 2 0 0 1 2.83-2.82L7 15"/>',
 "clipboard-list": '<rect width="8" height="4" x="8" y="2" rx="1" ry="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="M12 11h4"/><path d="M12 16h4"/><path d="M8 11h.01"/><path d="M8 16h.01"/>',
 "credit-card": '<rect width="20" height="14" x="2" y="5" rx="2"/><line x1="2" x2="22" y1="10" y2="10"/>',
 "mail": '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
 "at-sign": '<circle cx="12" cy="12" r="4"/><path d="M16 8v5a3 3 0 0 0 6 0v-1a10 10 0 1 0-4 8"/>',
 "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
 "hash": '<line x1="4" x2="20" y1="9" y2="9"/><line x1="4" x2="20" y1="15" y2="15"/><line x1="10" x2="8" y1="3" y2="21"/><line x1="16" x2="14" y1="3" y2="21"/>',
 "building": '<rect width="16" height="20" x="4" y="2" rx="2" ry="2"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01"/><path d="M16 6h.01"/><path d="M12 6h.01"/><path d="M12 10h.01"/><path d="M12 14h.01"/><path d="M16 10h.01"/><path d="M16 14h.01"/><path d="M8 10h.01"/><path d="M8 14h.01"/>',
 "home": '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>',
 "briefcase": '<rect width="20" height="14" x="2" y="7" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
 "book-open": '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>',
 "graduation-cap": '<path d="M21.42 10.922a1 1 0 0 0-.019-1.838L12.83 5.18a2 2 0 0 0-1.66 0L2.6 9.08a1 1 0 0 0 0 1.832l8.57 3.908a2 2 0 0 0 1.66 0z"/><path d="M22 10v6"/><path d="M6 12.5V16a6 3 0 0 0 12 0v-3.5"/>',
 "pen-line": '<path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z"/>',
 "type": '<polyline points="4 7 4 4 20 4 20 7"/><line x1="9" x2="15" y1="20" y2="20"/><line x1="12" x2="12" y1="4" y2="20"/>',
 "case-sensitive": '<path d="M3 15V9a3 3 0 0 1 6 0v6"/><path d="M3 12h6"/><path d="M14 15V9"/><path d="M21 12a3 3 0 1 0-6 0 3 3 0 0 0 6 0"/>',
 "volume-2": '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/>',
 "languages": '<path d="m5 8 6 6"/><path d="m4 14 6-6 2-3"/><path d="M2 5h12"/><path d="M7 2h1"/><path d="m22 22-5-10-5 10"/><path d="M14 18h6"/>',
 "minus": '<path d="M5 12h14"/>',
 "cake": '<path d="M20 21v-8a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v8"/><path d="M4 16s.5-1 2-1 2.5 2 4 2 2.5-2 4-2 2.5 2 4 2 2-1 2-1"/><path d="M2 21h20"/><path d="M7 8v3"/><path d="M12 8v3"/><path d="M17 8v3"/><path d="M7 4h.01"/><path d="M12 4h.01"/><path d="M17 4h.01"/>',
 "coffee": '<path d="M17 8h1a4 4 0 1 1 0 8h-1"/><path d="M3 8h14v9a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4Z"/><line x1="6" x2="6" y1="2" y2="4"/><line x1="10" x2="10" y1="2" y2="4"/><line x1="14" x2="14" y1="2" y2="4"/>',
 "utensils": '<path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 0 0 2-2V2"/><path d="M7 2v20"/><path d="M21 15V2a5 5 0 0 0-5 5v6c0 1.1.9 2 2 2h3Zm0 0v7"/>',
 "cup-soda": '<path d="m6 8 1.75 12.28a2 2 0 0 0 2 1.72h4.54a2 2 0 0 0 2-1.72L18 8"/><path d="M5 8h14"/><path d="M7 15a6.47 6.47 0 0 1 5 0 6.47 6.47 0 0 0 5 0"/><path d="m12 8 1-6h2"/>',
 "bed": '<path d="M2 4v16"/><path d="M2 8h18a2 2 0 0 1 2 2v10"/><path d="M2 17h20"/><path d="M6 8v9"/>',
 "droplet": '<path d="M12 22a7 7 0 0 0 7-7c0-2-1-3.9-3-5.5s-3.5-4-4-6.5c-.5 2.5-2 4.9-4 6.5C6 11.1 5 13 5 15a7 7 0 0 0 7 7z"/>',
 "shirt": '<path d="M20.38 3.46 16 2a4 4 0 0 1-8 0L3.62 3.46a2 2 0 0 0-1.34 2.23l.58 3.47a1 1 0 0 0 .99.84H6v10c0 1.1.9 2 2 2h8a2 2 0 0 0 2-2V10h2.15a1 1 0 0 0 .99-.84l.58-3.47a2 2 0 0 0-1.34-2.23z"/>',
 "door-open": '<path d="M13 4h3a2 2 0 0 1 2 2v14"/><path d="M2 20h3"/><path d="M13 20h9"/><path d="M10 12v.01"/><path d="M13 4.562v16.157a1 1 0 0 1-1.242.97L5 20V5.562a2 2 0 0 1 1.515-1.94l4-1A2 2 0 0 1 13 4.562Z"/>',
 "zap": '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>',
 "lightbulb": '<path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/>',
 "check": '<path d="M20 6 9 17l-5-5"/>',
 "gamepad-2": '<line x1="6" x2="10" y1="11" y2="11"/><line x1="8" x2="8" y1="9" y2="13"/><line x1="15" x2="15.01" y1="12" y2="12"/><line x1="18" x2="18.01" y1="10" y2="10"/><path d="M17.32 5H6.68a4 4 0 0 0-3.978 3.59c-.006.052-.01.101-.017.152C2.604 9.416 2 14.456 2 16a3 3 0 0 0 3 3c1 0 1.5-.5 2-1l1.414-1.414A2 2 0 0 1 9.828 16h4.344a2 2 0 0 1 1.414.586L17 18c.5.5 1 1 2 1a3 3 0 0 0 3-3c0-1.545-.604-6.584-.685-7.258-.007-.05-.011-.1-.017-.151A4 4 0 0 0 17.32 5z"/>',
 "dumbbell": '<path d="m6.5 6.5 11 11"/><path d="m21 21-1-1"/><path d="m3 3 1 1"/><path d="m18 22 4-4"/><path d="m2 6 4-4"/><path d="m3 10 7-7"/><path d="m14 21 7-7"/>',
 "waves": '<path d="M2 6c.6.5 1.2 1 2.5 1C7 7 7 5 9.5 5c2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"/><path d="M2 12c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"/><path d="M2 18c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"/>',
 "palmtree": '<path d="M13 8c0-2.76-2.46-5-5.5-5S2 5.24 2 8h2l1-1 1 1h4"/><path d="M13 7.14A5.82 5.82 0 0 1 16.5 6c3.04 0 5.5 2.24 5.5 5h-3l-1-1-1 1h-3"/><path d="M5.89 9.71c-2.15 2.15-2.3 5.47-.35 7.43l4.24-4.25.7-.7.71-.71 2.12-2.12c-1.95-1.96-5.27-1.8-7.42.35z"/><path d="M11 15.5c.5 2.5-.17 4.5-1 6.5h4c2-5.5-.5-12-1-14"/>',
 "umbrella": '<path d="M22 12a10.06 10.06 1 0 0-20 0Z"/><path d="M12 12v8a2 2 0 0 0 4 0"/><path d="M12 2v1"/>',
 "film": '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M7 3v18"/><path d="M3 7.5h4"/><path d="M3 12h18"/><path d="M3 16.5h4"/><path d="M17 3v18"/><path d="M17 7.5h4"/><path d="M17 16.5h4"/>',
 "file-text": '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M16 13H8"/><path d="M16 17H8"/><path d="M10 9H8"/>',
 "flame": '<path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/>',
 "list-checks": '<path d="m3 17 2 2 4-4"/><path d="m3 7 2 2 4-4"/><path d="M13 6h8"/><path d="M13 12h8"/><path d="M13 18h8"/>',
 "guitar": '<path d="m11.9 12.1 4.514-4.514"/><path d="M20.1 2.3a1 1 0 0 0-1.4 0l-1.114 1.114A2 2 0 0 0 17 4.828v1.344a2 2 0 0 1-.586 1.414A2 2 0 0 1 17.828 7h1.344a2 2 0 0 0 1.414-.586L21.7 5.3a1 1 0 0 0 0-1.4z"/><path d="M6 16a2 2 0 1 1-4 0 2 2 0 0 1 4 0"/><path d="M11.412 9.588A2 2 0 1 0 8.586 12.414"/>',
 "megaphone": '<path d="m3 11 18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/>',
 # ---- U2 extra glyphs ----
 "eye": '<path d="M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0"/><circle cx="12" cy="12" r="3"/>',
 "baby": '<path d="M9 12h.01"/><path d="M15 12h.01"/><path d="M10 16c.5.3 1.2.5 2 .5s1.5-.2 2-.5"/><path d="M17.5 6.5c0 1.5-1 3-2.5 3.5"/><path d="M12 3a9 9 0 0 0-9 9 9 9 0 0 0 18 0 9 9 0 0 0-9-9z"/>',
 "palette": '<circle cx="13.5" cy="6.5" r=".5" fill="currentColor"/><circle cx="17.5" cy="10.5" r=".5" fill="currentColor"/><circle cx="8.5" cy="7.5" r=".5" fill="currentColor"/><circle cx="6.5" cy="12.5" r=".5" fill="currentColor"/><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10c.926 0 1.648-.746 1.648-1.688 0-.437-.18-.835-.437-1.125-.29-.289-.438-.652-.438-1.125a1.64 1.64 0 0 1 1.668-1.668h1.996c3.051 0 5.555-2.503 5.555-5.554C21.965 6.012 17.461 2 12 2z"/>',
 "scissors": '<circle cx="6" cy="6" r="3"/><path d="M8.12 8.12 12 12"/><path d="M20 4 8.12 15.88"/><circle cx="6" cy="18" r="3"/><path d="M14.8 14.8 20 20"/>',
 "glasses": '<circle cx="6" cy="15" r="4"/><circle cx="18" cy="15" r="4"/><path d="M14 15a2 2 0 0 0-2-2 2 2 0 0 0-2 2"/><path d="M2.5 13 5 7c.7-1.3 1.4-2 3-2"/><path d="M21.5 13 19 7c-.7-1.3-1.5-2-3-2"/>',
 # ---- U5 «¡Ñam!» comida glyphs ----
 "apple": '<path d="M12 20.94c1.5 0 2.75 1.06 4 1.06 3 0 6-8 6-12.22A4.91 4.91 0 0 0 17 5c-2.22 0-4 1.44-5 2-1-.56-2.78-2-5-2a4.9 4.9 0 0 0-5 4.78C2 14 5 22 8 22c1.25 0 2.5-1.06 4-1.06Z"/><path d="M10 2c1 .5 2 2 2 5"/>',
 "banana": '<path d="M4 13c3.5-2 8-2 10 2a5.5 5.5 0 0 1 8 5"/><path d="M5.15 17.89c5.52-1.52 8.65-6.89 7-12C11.55 4 11.5 2 13 2c3.22 0 5 5.5 5 8 0 6.5-4.2 12-10.49 12C5.11 22 2 22 2 20c0-1.5 1.14-1.55 3.15-2.11Z"/>',
 "grape": '<path d="M22 5V2l-5.89 5.89"/><circle cx="16.6" cy="15.89" r="3"/><circle cx="8.11" cy="7.4" r="3"/><circle cx="12.35" cy="11.65" r="3"/><circle cx="13.91" cy="5.85" r="3"/><circle cx="18.15" cy="10.09" r="3"/><circle cx="6.56" cy="13.2" r="3"/><circle cx="10.8" cy="17.44" r="3"/><circle cx="5" cy="19" r="3"/>',
 "cherry": '<path d="M2 17a5 5 0 0 0 10 0c0-2.76-2.5-5-5-3-2.5-2-5 .24-5 3Z"/><path d="M12 17a5 5 0 0 0 10 0c0-2.76-2.5-5-5-3-2.5-2-5 .24-5 3Z"/><path d="M7 14c3.22-2.91 4.29-8.75 5-12 1.66 2.38 4.94 9 5 12"/><path d="M22 9c-4.29 0-7.14-2.33-10-7 5.71 0 10 4.67 10 7Z"/>',
 "citrus": '<path d="M21.66 17.67a1.08 1.08 0 0 1-.04 1.6A12 12 0 0 1 4.73 2.38a1.1 1.1 0 0 1 1.61-.04z"/><path d="M19.65 15.66A8 8 0 0 1 8.35 4.34"/><path d="m14 10-5.5 5.5"/><path d="M14 17.85V10H6.15"/>',
 "egg": '<path d="M12 22c6.23-.05 7.87-5.57 7.5-10-.36-4.34-3.95-9.96-7.5-10-3.55.04-7.14 5.66-7.5 10-.37 4.43 1.27 9.95 7.5 10z"/>',
 "beef": '<circle cx="12.5" cy="8.5" r="2.5"/><path d="M12.5 2a6.5 6.5 0 0 0-6.22 4.6c-1.1 3.13-.78 3.9-3.18 6.08A3 3 0 0 0 5 18c4 0 8.4-1.8 11.4-4.3A6.5 6.5 0 0 0 12.5 2Z"/><path d="m18.5 6 2.19 4.5a6.48 6.48 0 0 1 .31 2 6.49 6.49 0 0 1-2.6 5.2C15.4 20.2 11 22 7 22a3 3 0 0 1-2.68-1.66L2.4 16.5"/>',
 "fish": '<path d="M6.5 12c.94-3.46 4.94-6 8.5-6 3.56 0 6.06 2.54 7 6-.94 3.47-3.44 6-7 6s-7.56-2.53-8.5-6Z"/><path d="M18 12v.5"/><path d="M16 17.93a9.77 9.77 0 0 1 0-11.86"/><path d="M7 10.67C7 8 5.58 5.97 2.73 5.5c-1 1.5-1 5 .23 6.5-1.24 1.5-1.24 5-.23 6.5C5.58 18.03 7 16 7 13.33"/>',
 "soup": '<path d="M12 21a9 9 0 0 0 9-9H3a9 9 0 0 0 9 9Z"/><path d="M7 21h10"/><path d="M19.5 12 22 6"/><path d="M16.25 3c.27.1.8.53.75 1.36-.06.83-.93 1.2-1 2.02-.05.78.34 1.24.73 1.62"/><path d="M11.25 3c.27.1.8.53.74 1.36-.05.83-.93 1.2-.98 2.02-.06.78.33 1.24.72 1.62"/><path d="M6.25 3c.27.1.8.53.75 1.36-.06.83-.93 1.2-1 2.02-.05.78.34 1.24.74 1.62"/>',
 "salad": '<path d="M7 21h10"/><path d="M12 21a9 9 0 0 0 9-9H3a9 9 0 0 0 9 9Z"/><path d="M11.38 12a2.4 2.4 0 0 1-.4-4.77 2.4 2.4 0 0 1 3.2-2.77 2.4 2.4 0 0 1 3.47-.63 2.4 2.4 0 0 1 3.37 3.37 2.4 2.4 0 0 1-1.1 3.7 2.51 2.51 0 0 1 .03 1.1"/><path d="m13 12 4-4"/><path d="M10.9 7.25A3.99 3.99 0 0 0 4 10c0 .73.2 1.41.54 2"/>',
 "sandwich": '<path d="M3 11v3a1 1 0 0 0 1 1h16a1 1 0 0 0 1-1v-3"/><path d="M12 19H4a1 1 0 0 1-1-1v-2a1 1 0 0 1 1-1h16a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1h-3.83"/><path d="m3 11 7.77-6.04a2 2 0 0 1 2.46 0L21 11H3Z"/>',
 "cookie": '<path d="M12 2a10 10 0 1 0 10 10 4 4 0 0 1-5-5 4 4 0 0 1-5-5"/><path d="M8.5 8.5v.01"/><path d="M16 15.5v.01"/><path d="M12 12v.01"/><path d="M11 17v.01"/><path d="M7 14v.01"/>',
 "milk": '<path d="M8 2h8"/><path d="M9 2v2.789a4 4 0 0 1-.672 2.219l-.656.984A4 4 0 0 0 7 10.212V20a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2v-9.789a4 4 0 0 0-.672-2.219l-.656-.984A4 4 0 0 1 15 4.788V2"/><path d="M7 15a6.472 6.472 0 0 1 5 0 6.47 6.47 0 0 0 5 0"/>',
 "wine": '<path d="M8 22h8"/><path d="M7 10h10"/><path d="M12 15v7"/><path d="M12 15a5 5 0 0 0 5-5c0-2-.5-4-2-8H9c-1.5 4-2 6-2 8a5 5 0 0 0 5 5Z"/>',
 "beer": '<path d="M17 11h1a3 3 0 0 1 0 6h-1"/><path d="M9 12v6"/><path d="M13 12v6"/><path d="M14 7.5c-1 0-1.44.5-3 .5s-2-.5-3-.5-1.72.5-2.5.5a2.5 2.5 0 0 1 0-5c.78 0 1.57.5 2.5.5S9.44 3 11 3s2 .5 3 .5 1.72-.5 2.5-.5a2.5 2.5 0 0 1 0 5c-.78 0-1.5-.5-2.5-.5Z"/><path d="M5 8v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V8"/>',
 "utensils-crossed": '<path d="m16 2-2.3 2.3a3 3 0 0 0 0 4.2l1.8 1.8a3 3 0 0 0 4.2 0L22 8"/><path d="M15 15 3.3 3.3a4.2 4.2 0 0 0 0 6l7.3 7.3c.7.7 2 .7 2.8 0L15 15Zm0 0 7 7"/><path d="m2.1 21.8 6.4-6.3"/><path d="m19 5-7 7"/>',
 "receipt": '<path d="M4 2v20l2-1 2 1 2-1 2 1 2-1 2 1 2-1 2 1V2l-2 1-2-1-2 1-2-1-2 1-2-1-2 1Z"/><path d="M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8"/><path d="M12 17.5v-11"/>',
 "chef-hat": '<path d="M6 13.87A4 4 0 0 1 7.41 6a5.11 5.11 0 0 1 1.05-1.54 5 5 0 0 1 7.08 0A5.11 5.11 0 0 1 16.59 6 4 4 0 0 1 18 13.87V21H6Z"/><path d="M6 17h12"/>',
 "package": '<path d="M11 21.73a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73z"/><path d="M12 22V12"/><polyline points="3.29 7 12 12 20.71 7"/><path d="m7.5 4.27 9 5.15"/>',
 "shopping-cart": '<circle cx="8" cy="21" r="1"/><circle cx="19" cy="21" r="1"/><path d="M2.05 2.05h2l2.66 12.42a2 2 0 0 0 2 1.58h9.78a2 2 0 0 0 1.95-1.57l1.65-7.43H5.12"/>',
 "wheat": '<path d="M2 22 16 8"/><path d="M3.47 12.53 5 11l1.53 1.53a3.5 3.5 0 0 1 0 4.94L5 19l-1.53-1.53a3.5 3.5 0 0 1 0-4.94Z"/><path d="M7.47 8.53 9 7l1.53 1.53a3.5 3.5 0 0 1 0 4.94L9 15l-1.53-1.53a3.5 3.5 0 0 1 0-4.94Z"/><path d="M11.47 4.53 13 3l1.53 1.53a3.5 3.5 0 0 1 0 4.94L13 11l-1.53-1.53a3.5 3.5 0 0 1 0-4.94Z"/>',
}

DEFAULT = "tag"

# --------------------------------------------------------------------------
# GROUP_ICON — fallback per vocab-groep (elke kaart krijgt zeker een icoon)
# --------------------------------------------------------------------------
GROUP_ICON = {
 # U1
 "datos": "user", "ficha": "clipboard-list", "interrog": "help-circle",
 "saludos": "hand", "pais": "flag", "mundo": "globe",
 # U3
 "hora": "clock", "rutina": "sunrise", "verbos": "zap",
 "frecuencia": "repeat", "tiempo": "calendar",
 # U4
 "opinar": "heart", "ocio": "gamepad-2", "musica": "music",
 "sentim": "smile", "planes": "calendar-check", "valencia": "palmtree",
 # U2
 "familia": "users", "fisico": "user", "colores": "palette",
 "caracter": "smile", "cuerpo": "user", "util": "message-circle",
 # U5 «¡Ñam!»
 "comida": "utensils", "fruta": "apple", "verdura": "carrot", "bebida": "cup-soda",
 "mesa": "utensils-crossed", "restaurante": "receipt", "cantidades": "package",
 "cortesia": "message-circle", "mexico": "flame",
}

# --------------------------------------------------------------------------
# WORD_ICON — exacte lemma's (zoals in de vocab-JSON's "es")
# --------------------------------------------------------------------------
WORD_ICON = {
 # ---- U1 ----
 "el nombre": "user", "el apellido": "users", "llamarse": "user",
 "la edad": "cake", "tener … años": "cake",
 "ser (de)": "map-pin", "vivir (en)": "home",
 "el país": "flag", "la nacionalidad": "flag",
 "la dirección": "map-pin", "el correo electrónico": "at-sign",
 "el teléfono": "phone", "el número": "hash", "la ciudad": "building",
 "el idioma": "languages", "hablar": "message-circle", "estudiar": "book-open",
 "trabajar": "briefcase", "aprender": "graduation-cap",
 "la fecha de nacimiento": "calendar", "el lugar de nacimiento": "map-pin",
 "el código postal": "hash", "el curso": "graduation-cap", "la firma": "pen-line",
 "rellenar / completar": "pen-line", "el documento de identidad (el DNI)": "credit-card",
 # ---- U3 ----
 "¿Qué hora es?": "clock", "la hora": "clock", "es la una": "clock",
 "son las dos": "clock", "y media": "clock", "y cuarto": "clock",
 "menos cuarto": "clock", "en punto": "clock", "el mediodía": "sun",
 "la medianoche": "moon", "de la mañana": "sunrise", "de la tarde": "sun",
 "de la noche": "moon", "¿A qué hora…?": "clock", "a las …": "clock",
 "el reloj": "watch", "temprano": "sunrise", "tarde": "sunset",
 "la rutina": "list-checks", "despertarse (e→ie)": "sunrise", "levantarse": "sunrise",
 "ducharse": "droplet", "lavarse": "droplet", "vestirse (e→i)": "shirt",
 "peinarse": "smile", "desayunar": "coffee", "almorzar (o→ue)": "utensils",
 "cenar": "utensils", "acostarse (o→ue)": "bed", "hacer los deberes": "book-open",
 "ir al instituto": "graduation-cap", "descansar": "moon",
 "por la mañana": "sunrise", "por la tarde": "sun", "por la noche": "moon",
 "empezar (e→ie)": "zap", "querer (e→ie)": "heart", "preferir (e→ie)": "thumbs-up",
 "poder (o→ue)": "zap", "dormir (o→ue)": "bed", "volver (o→ue)": "repeat",
 "pedir (e→i)": "message-circle", "jugar (u→ue)": "gamepad-2",
 "hacer (yo hago)": "zap", "ir (voy)": "route", "salir (yo salgo)": "door-open",
 "la primavera": "sunrise", "el verano": "sun", "el otoño": "umbrella",
 "el invierno": "moon",
 # ---- U4 ----
 "gustar": "thumbs-up", "encantar": "heart", "interesar": "lightbulb",
 "preferir": "thumbs-up", "odiar": "frown",
 "me gusta / me gustan": "thumbs-up",
 "también": "check", "tampoco": "minus",
 "¿por qué? / porque": "help-circle",
 "el deporte": "dumbbell", "el fútbol": "dumbbell", "el baloncesto": "dumbbell",
 "nadar": "waves", "bailar": "music", "jugar (a)": "gamepad-2",
 "el videojuego": "gamepad-2", "leer": "book-open", "la playa": "umbrella",
 "el tiempo libre": "clock", "salir con amigos": "users",
 "la música": "music", "la canción": "music", "el/la cantante": "megaphone",
 "el grupo / la banda": "users", "escuchar música": "music",
 "tocar (la guitarra)": "guitar", "la película": "film", "la serie": "film",
 "el cine": "film", "el/la artista": "star", "la letra": "file-text",
 "favorito/-a": "star",
 "divertido/-a": "smile", "aburrido/-a": "frown", "genial / guay": "star",
 "interesante": "lightbulb", "emocionante": "zap", "relajante": "moon",
 "me pone contento/-a": "smile", "me aburre": "frown",
 "querer (+ infinitivo)": "heart", "poder (+ infinitivo)": "zap",
 "quedar (con)": "calendar-check", "¿quieres…?": "message-circle",
 "¿por qué no…?": "help-circle", "vale / de acuerdo": "check",
 "¿a qué hora?": "clock", "el plan": "calendar-check",
 "València / Valencia": "map-pin", "la costa": "waves", "el mar": "waves",
 "la paella": "utensils", "las Fallas": "flame", "la horchata": "cup-soda",
 # ---- U0 ----
 "el alfabeto / el abecedario": "type", "la letra": "type", "deletrear": "type",
 "la vocal": "volume-2", "la consonante": "volume-2", "la sílaba": "volume-2",
 "la sílaba tónica": "volume-2", "la tilde / el acento (´)": "type",
 "el sombrero (metáfora de clase)": "type", "aguda": "volume-2", "llana": "volume-2",
 "esdrújula": "volume-2", "el monosílabo": "type", "la mayúscula": "case-sensitive",
 "la minúscula": "case-sensitive", "la diéresis (¨)": "type",
 "el dígrafo (ch, ll)": "type", "la arroba (@)": "at-sign", "el guion (-)": "minus",
 "con tilde / sin tilde": "type", "con be/uve · con/sin hache": "type",
 "el número": "hash", "contar (0 → 100)": "hash", "cero": "hash", "cien": "hash",
 "la edad": "cake", "tener … años": "cake", "¿Cuántos años tienes?": "cake",
 "el mundo hispano": "globe", "el país": "flag", "la lengua / el idioma": "languages",
 "el español / el castellano": "languages", "hispanohablante": "message-circle",
 "el cognado (palabra transparente)": "languages", "la ruta · la parada": "route",
 # ---- U2 «Mi gente» ----
 # familia
 "la familia": "users", "el padre / papá": "user", "la madre / mamá": "user",
 "los padres": "users", "el hermano": "user", "la hermana": "user",
 "el abuelo": "user", "la abuela": "user", "los abuelos": "users",
 "el tío": "user", "la tía": "user", "el primo": "user", "la prima": "user",
 "el hijo": "user", "la hija": "user", "el nieto / la nieta": "baby",
 "el marido / la mujer": "users", "la mascota": "heart",
 "mayor": "user", "menor": "baby", "casado/a": "heart", "soltero/a": "user",
 # físico
 "alto/a": "user", "bajo/a": "user", "delgado/a": "user", "gordito/a": "user",
 "guapo/a": "smile", "joven": "baby", "moreno/a": "user", "rubio/a": "user",
 "pelirrojo/a": "user", "el pelo": "scissors", "largo/a": "scissors",
 "corto/a": "scissors", "liso/a": "scissors", "rizado/a": "scissors",
 "los ojos": "eye", "la barba": "user", "las gafas": "glasses",
 # colores
 "marrón": "palette", "negro/a": "palette", "castaño/a": "palette",
 "azul": "palette", "verde": "palette", "gris": "palette",
 # carácter
 "simpático/a": "smile", "antipático/a": "frown", "majo/a": "smile",
 "tímido/a": "user", "gracioso/a": "smile", "trabajador/a": "briefcase",
 "inteligente": "lightbulb", "hablador/a": "message-circle",
 "tranquilo/a": "moon", "alegre": "smile",
 # cuerpo
 "la cabeza": "user", "la cara": "smile", "la nariz": "user",
 "la boca": "smile", "la mano": "hand",
 # útil
 "este / esta": "map-pin", "ese / esa": "map-pin", "tener": "hash",
 "ser": "user", "estar": "map-pin", "se llama": "user",
 "¿cuántos/as?": "help-circle", "también": "check", "pero": "minus",
 # ---- U5 «¡Ñam!» ----
 # comida
 "el pan": "sandwich", "los huevos": "egg", "el queso": "utensils", "la carne": "beef",
 "el pollo": "beef", "el pescado": "fish", "el arroz": "utensils", "la pasta": "utensils",
 "la sopa": "soup", "el bocadillo": "sandwich", "el jamón": "beef",
 # fruta
 "la manzana": "apple", "el plátano": "banana", "la naranja": "citrus", "la fresa": "cherry",
 "las uvas": "grape", "el limón": "citrus", "la piña": "apple",
 # verdura
 "la lechuga": "salad", "el tomate": "apple", "la patata": "carrot", "la cebolla": "carrot",
 "el ajo": "carrot", "el maíz": "wheat", "el pimiento": "carrot",
 # bebida
 "el agua": "droplet", "la leche": "milk", "el zumo": "cup-soda", "el café": "coffee",
 "el té": "coffee", "el refresco": "cup-soda",
 # mesa
 "el plato": "utensils", "el vaso": "cup-soda", "el tenedor": "utensils-crossed",
 "el cuchillo": "utensils-crossed", "la cuchara": "utensils", "la sal": "package",
 "la servilleta": "receipt",
 # restaurante
 "la carta": "clipboard-list", "el menú": "clipboard-list", "el/la camarero/a": "chef-hat",
 "la cuenta": "receipt", "la propina": "credit-card", "el primer plato": "soup",
 "el segundo plato": "beef", "el postre": "cake", "reservar": "calendar-check",
 # cantidades
 "mucho/-a": "package", "poco/-a": "minus", "un poco de": "minus", "un kilo de": "package",
 "una botella de": "wine", "un paquete de": "package",
 # cortesia
 "¿qué va a tomar?": "message-circle", "¿me pone…?": "message-circle", "para mí…": "hand",
 "¿me trae…?": "message-circle", "¡que aproveche!": "utensils", "rico/-a": "smile",
 "picante": "flame",
 # mexico
 "el taco": "utensils", "el guacamole": "salad", "el elote": "wheat", "la salsa": "flame",
 "el aguacate": "apple", "la arepa": "sandwich", "el ceviche": "fish", "los churros": "cookie",
}

# --------------------------------------------------------------------------
# KEYWORD_ICON — substring-fallback (vangt varianten/samengestelde lemma's)
# volgorde = prioriteit (eerste match wint)
# --------------------------------------------------------------------------
KEYWORD_ICON = [
 ("→ ", "flag"),            # gentilicios "España → español" → landvlag
 ("hora", "clock"), ("reloj", "watch"),
 ("años", "cake"), ("edad", "cake"),
 ("hola", "hand"), ("adiós", "hand"), ("buenos días", "sun"),
 ("buenas tardes", "sun"), ("buenas noches", "moon"), ("qué tal", "hand"),
 ("cómo estás", "hand"), ("gracias", "heart"), ("por favor", "hand"),
 ("encantado", "hand"), ("mucho gusto", "hand"), ("hasta luego", "hand"),
 ("hasta mañana", "hand"), ("chao", "hand"), ("me llamo", "user"),
 ("cómo te llamas", "user"), ("soy de", "map-pin"), ("soy", "user"),
 ("y tú", "message-circle"), ("este es", "users"),
 ("cómo se dice", "message-circle"), ("qué significa", "help-circle"),
 ("no entiendo", "help-circle"), ("repetir", "repeat"), ("despacio", "clock"),
 ("no sé", "help-circle"), ("cómo se escribe", "pen-line"),
 ("pregunta", "help-circle"),
 ("número", "hash"), ("veinte", "hash"), ("treinta", "hash"),
 ("veinti", "hash"), ("dieci", "hash"), ("cuarenta", "hash"),
 ("diez", "hash"), ("cinco", "hash"), ("cien", "hash"), ("contar", "hash"),
 ("mañana", "sunrise"), ("tarde", "sunset"), ("noche", "moon"),
 ("música", "music"), ("canción", "music"), ("cantante", "megaphone"),
 ("película", "film"), ("serie", "film"), ("cine", "film"),
 ("deporte", "dumbbell"), ("fútbol", "dumbbell"),
 ("nadar", "waves"), ("mar", "waves"), ("playa", "umbrella"),
 ("gusta", "thumbs-up"), ("porque", "help-circle"), ("por qué", "help-circle"),
 ("país", "flag"), ("mundo", "globe"), ("idioma", "languages"),
 ("lengua", "languages"), ("español", "languages"),
 ("correo", "at-sign"), ("teléfono", "phone"), ("ciudad", "building"),
 ("dirección", "map-pin"), ("nombre", "user"), ("apellido", "users"),
 ("nacionalidad", "flag"), ("firma", "pen-line"),
 ("¿cómo", "help-circle"), ("¿dónde", "help-circle"), ("¿cuál", "help-circle"),
 ("¿quién", "help-circle"), ("¿qué", "help-circle"), ("¿de dónde", "help-circle"),
 ("¿cuántos", "help-circle"),
 ("desayun", "coffee"), ("almorzar", "utensils"), ("cenar", "utensils"),
 ("comida", "utensils"), ("dormir", "bed"), ("acostar", "bed"),
 ("ducha", "droplet"), ("lav", "droplet"), ("vestir", "shirt"),
 ("levantar", "sunrise"), ("despertar", "sunrise"),
 ("instituto", "graduation-cap"), ("deberes", "book-open"),
 ("leer", "book-open"), ("estudiar", "book-open"),
 ("siempre", "repeat"), ("nunca", "repeat"), ("veces", "repeat"),
 ("menudo", "repeat"), ("normalmente", "repeat"), ("semana", "calendar"),
 ("día", "calendar"), ("lunes", "calendar"), ("martes", "calendar"),
 ("miércoles", "calendar"), ("jueves", "calendar"), ("viernes", "calendar"),
 ("sábado", "calendar"), ("domingo", "calendar"),
 ("enero", "calendar"), ("abril", "calendar"), ("julio", "calendar"),
 ("octubre", "calendar"),
 ("primavera", "sunrise"), ("verano", "sun"), ("otoño", "umbrella"),
 ("invierno", "moon"), ("hoy", "calendar"),
 ("quedar", "calendar-check"), ("plan", "calendar-check"),
 ("acuerdo", "check"), ("vale", "check"), ("también", "check"),
 ("querer", "heart"), ("quieres", "message-circle"),
 ("poder", "zap"), ("empezar", "zap"), ("emocionante", "zap"),
 ("divertido", "smile"), ("aburri", "frown"), ("genial", "star"),
 ("guay", "star"), ("interes", "lightbulb"), ("relajante", "moon"),
 ("favorito", "star"), ("artista", "star"),
 ("paella", "utensils"), ("horchata", "cup-soda"), ("fallas", "flame"),
 ("valencia", "map-pin"), ("costa", "waves"),
 ("letra", "type"), ("vocal", "volume-2"), ("consonante", "volume-2"),
 ("sílaba", "volume-2"), ("tónica", "volume-2"), ("acento", "type"),
 ("tilde", "type"), ("aguda", "volume-2"), ("llana", "volume-2"),
 ("esdrújula", "volume-2"), ("mayúscula", "case-sensitive"),
 ("minúscula", "case-sensitive"), ("diéresis", "type"), ("dígrafo", "type"),
 ("arroba", "at-sign"), ("guion", "minus"), ("alfabeto", "type"),
 ("abecedario", "type"), ("deletrear", "type"), ("sombrero", "type"),
 ("cognado", "languages"), ("ruta", "route"), ("parada", "map-pin"),
 ("hispano", "globe"),
 # ---- U5 «¡Ñam!» keyword fallbacks ----
 ("manzana", "apple"), ("plátano", "banana"), ("naranja", "citrus"), ("limón", "citrus"),
 ("uva", "grape"), ("fresa", "cherry"), ("piña", "apple"), ("aguacate", "apple"),
 ("huevo", "egg"), ("carne", "beef"), ("pollo", "beef"), ("jamón", "beef"),
 ("pescado", "fish"), ("ceviche", "fish"), ("sopa", "soup"), ("ensalada", "salad"),
 ("lechuga", "salad"), ("guacamole", "salad"), ("bocadillo", "sandwich"), ("arepa", "sandwich"),
 ("pan", "sandwich"), ("maíz", "wheat"), ("elote", "wheat"),
 ("leche", "milk"), ("zumo", "cup-soda"), ("refresco", "cup-soda"), ("café", "coffee"),
 ("té", "coffee"), ("agua", "droplet"), ("botella", "wine"),
 ("cuchillo", "utensils-crossed"), ("tenedor", "utensils-crossed"), ("cuchara", "utensils"),
 ("vaso", "cup-soda"), ("plato", "utensils"), ("servilleta", "receipt"),
 ("carta", "clipboard-list"), ("menú", "clipboard-list"), ("camarero", "chef-hat"),
 ("cuenta", "receipt"), ("propina", "credit-card"), ("postre", "cake"), ("reservar", "calendar-check"),
 ("kilo", "package"), ("paquete", "package"), ("poco", "minus"), ("mucho", "package"),
 ("picante", "flame"), ("salsa", "flame"), ("rico", "smile"), ("aproveche", "utensils"),
 ("va a tomar", "message-circle"), ("me pone", "message-circle"), ("me trae", "message-circle"),
 ("para mí", "hand"), ("taco", "utensils"), ("churro", "cookie"), ("galleta", "cookie"),
 ("cebolla", "carrot"), ("ajo", "carrot"), ("patata", "carrot"), ("tomate", "apple"),
 ("pimiento", "carrot"), ("queso", "utensils"), ("arroz", "utensils"), ("pasta", "utensils"),
]


def _norm(s):
    return (s or "").strip().lower()


def _pick(word, group):
    """Kies de iconnaam voor een woord (zonder SVG te bouwen)."""
    w = word or ""
    # 1) exact lemma
    if w in WORD_ICON:
        return WORD_ICON[w]
    nw = _norm(w)
    # 2) trefwoord-substring
    for kw, name in KEYWORD_ICON:
        if kw in nw:
            return name
    # 3) groep-fallback
    if group and group in GROUP_ICON:
        return GROUP_ICON[group]
    # 4) default
    return DEFAULT


def icon_name(word, group=""):
    """Alleen de iconnaam (voor tests/debug)."""
    return _pick(word, group)


def icon_svg(word, group="", size=36, color="currentColor"):
    """Inline-SVG-string voor de flashcard-voorkant (grijswaarden-veilig).

    Wordt als visueel anker BOVEN het woord getoond. aria-hidden: het woord
    blijft de tekstdrager. color mag een CSS-var zijn, bv. 'var(--gd)'.
    """
    name = _pick(word, group)
    inner = LUCIDE.get(name, LUCIDE[DEFAULT])
    return (
        '<span class="fcic" aria-hidden="true" '
        'style="display:flex;justify-content:center;line-height:0;margin-bottom:5px;color:%s">'
        '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">%s</svg></span>'
        % (color, size, size, inner)
    )


if __name__ == "__main__":
    # snelle self-check
    import json, sys, os
    ROOT = "/home/user/espa-ol-en-la-pr-ctica"
    for u, lu in [("U0", "u0"), ("U1", "u1"), ("U3", "u3"), ("U4", "u4")]:
        p = f"{ROOT}/01-cursussen/05-a1/{u}/{lu}_vocab.json"
        if not os.path.exists(p):
            print(u, "geen vocab-json"); continue
        d = json.load(open(p, encoding="utf-8"))
        miss = [v["es"] for v in d if icon_name(v["es"], v.get("grp", "")) == DEFAULT]
        print(f"{u}: {len(d)} woorden · {len(d)-len(miss)} specifiek · {len(miss)} default")
        for m in miss:
            print("   default →", m)
