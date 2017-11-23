from io import BytesIO

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
from flask import url_for

# 随机字母
def rndChar():
    char = chr(random.randint(65, 90))
    return char

# 随机颜色
def rndColor():
    r = random.randint(64, 255)
    g = random.randint(64, 255)
    b = random.randint(64, 255)
    return (r, g, b)

# 随机颜色2:
def rndColor2():
    r = random.randint(32, 127)
    g = random.randint(32, 127)
    b = random.randint(32, 127)
    return (r, g, b)

def generate_code_str():
    code = ''
    # 240X60 定义大小
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))

    # 创建Font对象:
    font = ImageFont.truetype('Arial.ttf', 36)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    # 输出文字:
    for t in range(4):
        singleLetter = rndChar()
        code += singleLetter
        draw.text((60 * t + 10, 10), singleLetter, font=font, fill=rndColor2())
    # 模糊:
    image = image.filter(ImageFilter.BLUR)
    image.save('app/static/images/code.jpg', 'jpeg')
    return image,code

def generate_verification_code():
    code_img, str_text = generate_code_str()
    buf = BytesIO()
    code_img.save(buf, 'JPEG', quality=70)
    buf_str = buf.getvalue()
    return buf_str, str_text
