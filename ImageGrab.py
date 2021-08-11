from PIL import Image, ImageDraw, ImageFont, ImageGrab
import bitfont

def zoomin(im):
    (width, height) = (im.width * 2 , im.height * 2)
    im = im.resize((width, height))
    return im

def zoomout(im):
    (width, height) = (im.width // 2 , im.height // 2)
    im = im.resize((width, height))
    return im

# im = Image.new("RGB", (400,200),color=(255,0,0))      # 新建图片
# im = bitfont.load_background()                        # 加载自定义bitfont库中背景
# im = im.resize((800,200))                             # 设置图片大小
im = ImageGrab.grab((0,0,800,500))                      # 拍摄屏幕快照。(空参数)默认全屏，参数 box 剪切部分
# im = ImageGrab.grabclipboard()                        # 拍摄剪贴板图像的快照（如果有）。
draw = ImageDraw.Draw(im)

font = ImageFont.truetype("DroidSansFallback.ttf", 26)
font_v = bitfont.load_vcrmono()
draw.text((5, 10), bitfont.text[1], font=font)
draw.text((5, 40), bitfont.text[1], (255,128,128), font=font_v)

draw.text((5, 100), "安卓黑体 DroidSansFallback.ttf\n中文字体测试 \ PIL 使用自己的字体文件格式来存储位图字体，\n限制为 256 个字符。\n 从版本 1.1.4 开始，PIL 可以配置为支持 TrueType \n和 OpenType 字体", (255,0,255), font=font)

font = ImageFont.truetype("DroidSansFallback.ttf", 72)
draw.text((50, 300), "Pillow屏幕截图和文字", (255,255,0), font=font)

# im.save('test.png')
# im.save('test.j2k')
im.save("test_web_high.jpg", quality="web_high")     
# JPEG 质量设置等同于 Photoshop 设置  web_low、web_medium、web_high、web_very_high、web_maximum、 low、medium、high、maximum

im.show()