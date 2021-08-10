## Python脚本内嵌base64编码点阵字体库 `bitfont.py`  [详细使用参考](https://262235.xyz/index.php/archives/284/)

![bitfont](https://262235.xyz/usr/uploads/2021/08/828349640.png)

- 下载 bitfont.py 文件，输入如下命令，就能显示演示图

    python3 bitfont.py

## Python学习: pillow_font 图片上填写文本

![](https://raw.githubusercontent.com/hongwenjun/pillow_font/main/png/Fixedsys12.pil.png)
![](https://raw.githubusercontent.com/hongwenjun/pillow_font/main/png/VCRMono16.pil.png)

### 脚本 image_font.py ，批量生成字体预览图, pil 和 ttf 支持

```
Usage: python3 image_font.py fontfiles...

$ python3 image_font.py  *.pil  ttf/*.ttf
```

![](https://raw.githubusercontent.com/hongwenjun/pillow_font/main/png/VCR_OSD_MONO_1.001.ttf.png)
![](https://raw.githubusercontent.com/hongwenjun/pillow_font/main/png/fixedsys_excelsior.ttf.png)

### 项目文件和工具简介
```bash
image_font.py
pilfont.py        # pillow 字体转换工具
Fixedsys12.pbm    
Fixedsys12.pil    # 使用 pilfont.py 工具，bdf转pil
VCRMono16.pbm     # pbm 为点阵位图，如果缺少pil没法使用
VCRMono16.pil

./bdf:       # 目录下2个bdf字体,使用ttf2bdf工具转换所得
Fixedsys12.bdf
VCRMono16.bdf

./png:
Fixedsys12.pil.png
fixedsys_excelsior.ttf.png
FreeMono.ttf.png
VCRMono16.pil.png
VCR_OSD_MONO_1.001.ttf.png

./tools:         # ttf2bdf工具和Bdf查看编辑
BdfEditor.exe
ttf2bdf.exe

./ttf:           # pil 点阵字体源 ttf 文件
fixedsys_excelsior.ttf
VCR_OSD_MONO_1.001.ttf
FreeMono.ttf
```

![](https://raw.githubusercontent.com/hongwenjun/pillow_font/main/png/FreeMono.ttf.png)

###  image_font.py  源码
```python
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

```
