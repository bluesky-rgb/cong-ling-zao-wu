import subprocess, math
from PIL import Image, ImageDraw, ImageFont

W, H, FPS, SS = 1920, 1080, 30, 2  # output size, fps, supersample factor
NOTO = '/usr/share/fonts/opentype/noto/'

# palette (dark variant of 从零造电)
BG = (18, 24, 27)
SHEET = (26, 34, 38)
INK = (227, 234, 236)
MUTED = (151, 166, 171)
LINE = (44, 56, 61)
COPPER = (224, 138, 82)
FIELD = (111, 176, 222)
SPARK = (242, 189, 69)
NRED = (216, 75, 58)
SBLUE = (61, 120, 184)

_fc = {}
def font(kind, px):
    key = (kind, px)
    if key not in _fc:
        path, idx = {'sans': ('NotoSansCJK-Regular.ttc', 2), 'bold': ('NotoSansCJK-Bold.ttc', 2),
                     'serif': ('NotoSerifCJK-Black.ttc', 2), 'mono': ('NotoSansCJK-Bold.ttc', 7)}[kind]
        _fc[key] = ImageFont.truetype(NOTO + path, int(px * SS), index=idx)
    return _fc[key]

class Canvas:
    """Draw in 1920x1080 coordinates; rendered at SS x and downsampled."""
    def __init__(self):
        self.im = Image.new('RGB', (W * SS, H * SS), BG)
        self.d = ImageDraw.Draw(self.im)
    def s(self, *v):
        return [x * SS for x in v]
    def rect(self, x0, y0, x1, y1, fill=None, outline=None, width=1, r=0):
        self.d.rounded_rectangle(self.s(x0, y0, x1, y1), radius=r * SS, fill=fill, outline=outline, width=int(width * SS))
    def ellipse(self, cx, cy, rx, ry, fill=None, outline=None, width=1):
        self.d.ellipse(self.s(cx - rx, cy - ry, cx + rx, cy + ry), fill=fill, outline=outline, width=int(width * SS))
    def arc(self, cx, cy, rx, ry, a0, a1, fill, width=1):
        self.d.arc(self.s(cx - rx, cy - ry, cx + rx, cy + ry), a0, a1, fill=fill, width=int(width * SS))
    def line(self, pts, fill, width=2):
        self.d.line([p * SS for xy in pts for p in xy], fill=fill, width=int(width * SS), joint='curve')
    def poly(self, pts, fill):
        self.d.polygon([p * SS for xy in pts for p in xy], fill=fill)
    def text(self, x, y, s, kind='sans', px=32, fill=INK, anchor='la'):
        self.d.text((x * SS, y * SS), s, font=font(kind, px), fill=fill, anchor=anchor)
    def textw(self, s, kind='sans', px=32):
        return self.d.textlength(s, font=font(kind, px)) / SS
    def arrow(self, x0, y0, x1, y1, fill, width=4, head=16):
        self.line([(x0, y0), (x1, y1)], fill, width)
        a = math.atan2(y1 - y0, x1 - x0)
        p1 = (x1 - head * math.cos(a - 0.45), y1 - head * math.sin(a - 0.45))
        p2 = (x1 - head * math.cos(a + 0.45), y1 - head * math.sin(a + 0.45))
        self.poly([(x1, y1), p1, p2], fill)
    def frame(self):
        return self.im.reduce(SS).tobytes()

def mix(c1, c2, t):
    t = max(0.0, min(1.0, t))
    return tuple(int(a + (b - a) * t) for a, b in zip(c1, c2))

def ease(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)

def fade(t, t0, t1):
    """0→1 between t0 and t1."""
    return ease((t - t0) / (t1 - t0)) if t1 > t0 else float(t >= t0)

def render(path, seconds, draw):
    n = int(seconds * FPS)
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
                          '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-preset', 'medium',
                          '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', path], stdin=subprocess.PIPE)
    for i in range(n):
        c = Canvas()
        draw(c, i / FPS, i)
        p.stdin.write(c.frame())
    p.stdin.close()
    p.wait()
    return path

def corner_tag(c, label):
    c.text(60, 56, label, 'mono', 22, MUTED)
