import os, sys, glob
from PIL import Image, ImageDraw, ImageFont

text = [ "!\"#$%&]'()*+,-./0123456789:;<=>?@",
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`",
    "abcdefghijklmnopqrstuvwxyz{|}~"  ]

files = []
for f in sys.argv[1:]:
    files = files + glob.glob(f)

for f in files:
    im = Image.open("bg.png")
    (width, height) = (im.width // 2, im.height // 2)
    im = im.resize((width, height))
    draw = ImageDraw.Draw(im)

    try:
        # use a bitmap font
        font = ImageFont.load(f)
    except (SyntaxError, IOError):
        try:
            # 使用ttf字体
            font = ImageFont.truetype(f, 26, encoding="utf-8")
        except (SyntaxError, IOError):
            break

    draw.text((5, 10), text[0], font=font)
    draw.text((5, 30), text[1], (255, 0, 0), font=font)
    draw.text((5, 50), text[2], (10, 10, 10),  font=font)
    draw.text((5, 70), "FontName:" + f , font=font)
    im.save(f + '.png')
    im.close()
    print("FontName:" + f + "  ...OK")

print("\nUsage: python3 image_font.py fontfiles...")

