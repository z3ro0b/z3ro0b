import random

random.seed(7)

FONT = "IBM Plex Mono, SFMono-Regular, Menlo, Consolas, monospace"

TOKENS_DARK = {
    "void": "#07070A",
    "carbon": "#101016",
    "ink": "#1E1E27",
    "periwinkle": "#5A5F7D",
    "lens": "#A8DDF0",
    "window": "#F0B03C",
    "arterial": "#B01020",
    "bone": "#E4E4E8",
    "ash": "#7C7C88",
}

# Light variant: invert the canvas/panel/text roles, keep accent hues intact
# (lens/window/arterial read the same in both themes -- only the neutrals flip).
TOKENS_LIGHT = {
    "void": "#F4F4F2",
    "carbon": "#E7E7E4",
    "ink": "#D2D2CE",
    "periwinkle": "#8A8FA8",
    "lens": "#1E7A9C",
    "window": "#B5750E",
    "arterial": "#B01020",
    "bone": "#101016",
    "ash": "#5C5C66",
}


def skyline_group(tokens, seed_offset=0):
    rng = random.Random(7 + seed_offset)
    bldgs = []
    windows = []
    x = -10
    base_y = 320
    while x < 1300:
        w = rng.randint(34, 68)
        h = rng.randint(45, 100)
        y = base_y - h
        bldgs.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h+20}"/>')
        # lit windows inside this building
        rows = max(2, h // 26)
        cols = max(1, w // 18)
        for r in range(rows):
            for c in range(cols):
                if rng.random() < 0.22:
                    wx = x + 6 + c * 16
                    wy = y + 10 + r * 22
                    if wx + 6 < x + w:
                        roll = rng.random()
                        if roll < 0.06:
                            fill = tokens["arterial"]
                        elif roll < 0.55:
                            fill = tokens["lens"]
                        else:
                            fill = tokens["window"]
                        windows.append(
                            f'<rect x="{wx}" y="{wy}" width="5" height="7" fill="{fill}" fill-opacity="0.9"/>'
                        )
        x += w + rng.randint(6, 16)

    bldg_svg = (
        f'<g fill="{tokens["periwinkle"]}" fill-opacity="0.16">' + "".join(bldgs) + "</g>"
    )
    win_svg = "<g>" + "".join(windows) + "</g>"
    return bldg_svg, win_svg


def banner_svg(tokens, theme):
    bldg_svg, win_svg = skyline_group(tokens)
    handle_fill = tokens["bone"]
    sub_fill = tokens["ash"]
    accent = tokens["lens"]

    return f'''<svg width="1280" height="320" viewBox="0 0 1280 320" xmlns="http://www.w3.org/2000/svg">
  <rect width="1280" height="320" fill="{tokens["void"]}"/>
  {bldg_svg}
  {win_svg}
  <text x="-16" y="168" font-family="{FONT}" font-size="150" font-weight="700"
        fill="{handle_fill}" letter-spacing="-5">z3rob</text>
  <rect x="1044" y="234" width="7" height="10" fill="{accent}" fill-opacity="0.9"/>
  <text x="1256" y="244" text-anchor="end" font-family="{FONT}" font-size="15"
        fill="{sub_fill}" letter-spacing="1.5">SANDBOX ESCAPES &#183; OKTA PAM AUTHZ</text>
  <text x="1256" y="270" text-anchor="end" font-family="{FONT}" font-size="13"
        fill="{sub_fill}" letter-spacing="1" fill-opacity="0.7">WEB AUTHZ &#183; IDOR/BOLA &#183; BFLA</text>
</svg>'''


def stat_strip_svg(tokens, theme, stats):
    # stats: list of (value_placeholder, label)
    n = len(stats)
    cell_w = 1280 / n
    cells = []
    for i, (val, label) in enumerate(stats):
        cx = i * cell_w
        divider = ""
        if i > 0:
            divider = f'<line x1="{cx:.1f}" y1="14" x2="{cx:.1f}" y2="66" stroke="{tokens["ink"]}" stroke-width="1"/>'
        # tiny lit-window glyph before the number, in rotating accent
        glyph_colors = [tokens["lens"], tokens["window"], tokens["lens"], tokens["window"]]
        gx = cx + cell_w / 2 - 46
        cells.append(
            f'{divider}'
            f'<rect x="{gx:.1f}" y="24" width="6" height="10" fill="{glyph_colors[i % 4]}" fill-opacity="0.9"/>'
            f'<text x="{cx + cell_w/2 - 30:.1f}" y="36" font-family="{FONT}" font-size="26" font-weight="700" '
            f'fill="{tokens["bone"]}">{val}</text>'
            f'<text x="{cx + cell_w/2:.1f}" y="58" text-anchor="middle" font-family="{FONT}" font-size="12" '
            f'letter-spacing="1" fill="{tokens["ash"]}">{label}</text>'
        )
    body = "".join(cells)
    return f'''<svg width="1280" height="80" viewBox="0 0 1280 80" xmlns="http://www.w3.org/2000/svg">
  <rect width="1280" height="80" fill="{tokens["carbon"]}"/>
  {body}
</svg>'''


STATS = [
    ("[N]", "SUBMITTED"),
    ("[N]", "ACCEPTED"),
    ("[N]", "RESOLVED"),
    ("[N]", "HALL OF FAME"),
]

import os
os.makedirs("/home/claude/assets", exist_ok=True)

with open("/home/claude/assets/banner-dark.svg", "w") as f:
    f.write(banner_svg(TOKENS_DARK, "dark"))
with open("/home/claude/assets/banner-light.svg", "w") as f:
    f.write(banner_svg(TOKENS_LIGHT, "light"))
with open("/home/claude/assets/stat-strip-dark.svg", "w") as f:
    f.write(stat_strip_svg(TOKENS_DARK, "dark", STATS))
with open("/home/claude/assets/stat-strip-light.svg", "w") as f:
    f.write(stat_strip_svg(TOKENS_LIGHT, "light", STATS))

print("done")
