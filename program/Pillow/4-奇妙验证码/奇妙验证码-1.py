from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random

lines = False
blur = False
edge_enhance = False

def randomColor(a,b):
    return tuple([random.randint(a, b) for i in range(3)])

def drawLine(draw,w,h):
    begin = (random.randint(0, w), random.randint(0, h))
    end = (random.randint(0, w), random.randint(0, h))
    draw.line([begin, end], fill=randomColor(30, 255))

w = 60*4
h = 60
image = Image.new('RGB', (w,h), (155,255,255))
font = ImageFont.truetype('FZDHTJW.ttf', 36)
draw = ImageDraw.Draw(image)
for x in range(w):
    for y in range(h):
        draw.point((x, y), fill=randomColor(32, 127))
for i in range(4):
    draw.text((60*i+15, 10), chr(random.randint(65, 90)),
              font=font, fill=randomColor(64, 255))

if lines:
    lines_num = random.randint(5,10)
    for i in range(lines_num):
        drawLine(draw,w,h)
if blur:
    image = image.filter(ImageFilter.BLUR)
if edge_enhance:
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)

image.show()
