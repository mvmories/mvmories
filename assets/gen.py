"""Static echo of the site's ParticlePortrait, as SVG circles."""
from PIL import Image

SRC = '/Users/miguel.vilhena/workspace/portfolio/frontend_react/public/hero/portrait-420.png'
COLUMNS = 108          # sampling density across the portrait
ALPHA_THRESHOLD = 0.35 # same as samplePoints()

def lerp(a, b, t):
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))

def hexc(c):
    return '#%02x%02x%02x' % c

def build(dark, light, out):
    im = Image.open(SRC).convert('RGBA')
    im = im.crop(im.getbbox())
    w, h = im.size
    step = max(1, w // COLUMNS)
    px = im.load()
    rows = []
    min_alpha = ALPHA_THRESHOLD * 255
    for y in range(0, h, step):
        for x in range(0, w, step):
            r, g, b, a = px[x, y]
            if a < min_alpha:
                continue
            lum = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255
            col = hexc(lerp(dark, light, lum))
            # Fade the very bottom rows so the bust dissolves instead of ending
            fade = min(1.0, (h - y) / (h * 0.16))
            op = round(0.25 + 0.75 * (a / 255) * fade, 3)
            rows.append(f'<circle cx="{x}" cy="{y}" r="{step*0.60:.2f}" fill="{col}" opacity="{op}"/>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
           f'width="{w}" height="{h}">' + ''.join(rows) + '</svg>')
    open(out, 'w').write(svg)
    print(out, len(rows), 'points', w, 'x', h)

# --- particle palettes, straight from _tokens.scss -------------------------
# light theme: --particle-dark: brand-800, --particle-light: brand-300
build((0x23, 0x2a, 0x85), (0xa8, 0xb9, 0xf7), 'particles-light.svg')
# dark theme:  --particle-dark: brand-700, --particle-light: accent-200
build((0x31, 0x3b, 0xac), (0xb0, 0xdf, 0xfb), 'particles-dark.svg')
