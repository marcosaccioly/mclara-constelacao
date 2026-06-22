# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os

OUT = '/Users/maria/Documents/GitHub/mclara-constelacao/stages/03-roteiro/output/laminas'
os.makedirs(OUT, exist_ok=True)

W, H = 1080, 1350
BG = (255, 255, 255)
TERRA = (181, 82, 74)
TERRA_LIGHT = (196, 132, 122)
DARK = (58, 32, 32)
ACCENT = (212, 160, 144)
BORDER = (237, 216, 208)

def make_card():
    img = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W-1, H-1], outline=BORDER, width=3)
    d.line([(W-120, 3), (W-3, 3)], fill=BORDER, width=3)
    d.line([(W-3, 3), (W-3, 120)], fill=BORDER, width=3)
    d.line([(3, H-120), (3, H-3)], fill=BORDER, width=3)
    d.line([(3, H-3), (120, H-3)], fill=BORDER, width=3)
    return img, d

def get_font(size, bold=False):
    candidates = []
    if bold:
        candidates = [
            '/System/Library/Fonts/Supplemental/Georgia Bold.ttf',
            '/Library/Fonts/Georgia Bold.ttf',
        ]
    candidates += [
        '/System/Library/Fonts/Supplemental/Georgia.ttf',
        '/Library/Fonts/Georgia.ttf',
        '/System/Library/Fonts/Georgia.ttf',
    ]
    for p in candidates:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def draw_tag(d, text, y):
    f = get_font(28)
    d.text((80, y), text.upper(), font=f, fill=ACCENT)
    return y + 52

def draw_line(d, y, cx=None):
    x0 = cx - 50 if cx else 80
    x1 = x0 + 100
    d.rectangle([x0, y, x1, y+4], fill=ACCENT)
    return y + 52

def draw_sig(d, center=False):
    f = get_font(28)
    text = '@mariaclaragermano'
    if center:
        bb = d.textbbox((0, 0), text, font=f)
        x = (W - (bb[2] - bb[0])) // 2
    else:
        x = 80
    d.text((x, H-90), text, font=f, fill=ACCENT)

def wrap(d, text, x, y, font, color, max_w, lh):
    words = text.split()
    lines = []
    cur = ''
    for w in words:
        test = (cur + ' ' + w).strip()
        bb = d.textbbox((0, 0), test, font=font)
        if bb[2] - bb[0] <= max_w:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    for l in lines:
        d.text((x, y), l, font=font, fill=color)
        y += lh
    return y

def wrap_center(d, text, y, font, color, lh):
    words = text.split()
    lines = []
    cur = ''
    for w in words:
        test = (cur + ' ' + w).strip()
        bb = d.textbbox((0, 0), test, font=font)
        if bb[2] - bb[0] <= W - 160:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    for l in lines:
        bb = d.textbbox((0, 0), l, font=font)
        x = (W - (bb[2] - bb[0])) // 2
        d.text((x, y), l, font=font, fill=color)
        y += lh
    return y

MAX_W = W - 160

# SLIDE 1
img, d = make_card()
y = 240
y = draw_tag(d, 'peso que não é nosso', y)
y = draw_line(d, y)
fb = get_font(88, bold=True)
y = wrap(d, 'A gente carrega um peso que não é nosso,', 80, y, fb, TERRA, MAX_W, 108)
y += 52
d.rectangle([80, y, 180, y+4], fill=ACCENT)
y += 52
fi = get_font(44)
wrap(d, 'e aprendeu que esse é o papel de toda mulher.', 80, y, fi, TERRA_LIGHT, MAX_W, 60)
draw_sig(d)
img.save(f'{OUT}/01-capa.png')
print('01 ok')

# SLIDE 2
img, d = make_card()
y = 160
y = draw_tag(d, 'espelhamento', y)
y = draw_line(d, y)
f = get_font(46)
y = wrap(d, 'Desde pequena a gente aprende o que é "ser uma boa menina".', 80, y, f, DARK, MAX_W, 62)
y += 55
for linha in ['Agradar, ceder, caber.', 'Sorrir mesmo quando dói.', 'Existir dentro de um espaço que alguém definiu pra gente.']:
    y = wrap(d, linha, 80, y, f, TERRA, MAX_W, 62)
    y += 8
y += 45
wrap(d, 'E foi tão repetido que virou voz dentro de nós.', 80, y, f, DARK, MAX_W, 62)
draw_sig(d)
img.save(f'{OUT}/02-espelhamento.png')
print('02 ok')

# SLIDE 3
img, d = make_card()
y = 160
y = draw_tag(d, 'de onde veio', y)
y = draw_line(d, y)
f = get_font(46)
y = wrap(d, 'Às mulheres foi ensinado, por gerações,', 80, y, f, DARK, MAX_W, 62)
y += 55
for linha in ['que depender era segurança,', 'que cuidar era amor,', 'que escolher pra si era egoísmo.']:
    d.text((80, y), linha, font=f, fill=TERRA)
    y += 66
y += 45
y = wrap(d, 'Isso atravessou mães, avós, bisavós.', 80, y, f, DARK, MAX_W, 62)
y += 65
wrap(d, 'E chegou até nós.', 80, y, f, TERRA, MAX_W, 62)
draw_sig(d)
img.save(f'{OUT}/03-de-onde-veio.png')
print('03 ok')

# SLIDE 4
img, d = make_card()
y = 160
y = draw_tag(d, 'a voz', y)
y = draw_line(d, y)
f = get_font(46)
y = wrap(d, 'Quando a gente escolhe o próprio caminho, ela aparece.', 80, y, f, DARK, MAX_W, 62)
y += 60
y = wrap(d, 'Sussurra que estamos errando, que estamos decepcionando quem amamos, que mulher que se cuida é egoísta.', 80, y, f, TERRA_LIGHT, MAX_W, 62)
y += 65
y = wrap(d, 'Essa voz parece nossa.', 80, y, f, DARK, MAX_W, 62)
y += 8
wrap(d, 'Mas ela veio antes da gente.', 80, y, f, TERRA, MAX_W, 62)
draw_sig(d)
img.save(f'{OUT}/04-a-voz.png')
print('04 ok')

# SLIDE 5
img, d = make_card()
y = 160
y = draw_tag(d, 'a mãe', y)
y = draw_line(d, y)
f = get_font(46)
y = wrap(d, 'A nossa mãe talvez tenha olhado com estranhamento quando escolhemos diferente.', 80, y, f, DARK, MAX_W, 62)
y += 60
y = wrap(d, 'E dói, porque a gente queria tanto que ela entendesse.', 80, y, f, TERRA_LIGHT, MAX_W, 62)
y += 60
y = wrap(d, 'Ela fez o que aprendeu, dentro do mundo que viveu. A gente tá tentando fazer diferente.', 80, y, f, DARK, MAX_W, 62)
y += 60
wrap(d, 'Essas duas coisas podem ser verdade ao mesmo tempo.', 80, y, f, TERRA, MAX_W, 62)
draw_sig(d)
img.save(f'{OUT}/05-a-mae.png')
print('05 ok')

# SLIDE 6
img, d = make_card()
y = 220
y = draw_tag(d, 'o peso faz sentido', y)
y = draw_line(d, y)
f = get_font(50)
y = wrap(d, 'O cansaço que a gente sente enquanto persegue o que quer tem um tamanho proporcional ao que estamos rompendo.', 80, y, f, DARK, MAX_W, 68)
y += 80
f_lg = get_font(62)
wrap(d, 'Faz sentido se sentir pesada.', 80, y, f_lg, TERRA, MAX_W, 80)
draw_sig(d)
img.save(f'{OUT}/06-o-peso.png')
print('06 ok')

# SLIDE 7
img, d = make_card()
f = get_font(52)
y = 340
y = draw_line(d, y, cx=W//2)
y = wrap_center(d, 'Reconhecer de onde vem essa voz muda o que a gente faz com ela.', y, f, DARK, 72)
y += 72
for linha in ['Você já se sentiu assim?']:
    y = wrap_center(d, linha, y, f, TERRA, 72)
y += 52
d.rectangle([(W-100)//2, y, (W+100)//2, y+4], fill=ACCENT)
draw_sig(d, center=True)
img.save(f'{OUT}/07-fechamento.png')
print('07 ok')

print(f'\nPronto! 7 lâminas salvas em:\n{OUT}')
