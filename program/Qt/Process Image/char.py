from PIL import Image, ImageDraw

def to_char(img):

    width, height = (60, 60)

    img = img.convert('L').resize((width, height))

    # 70 level 字符串
    ASCII_HIHG = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!1I;:,\"^`'. '''

    # 灰度转字符串
    txt = ''
    for y in range(height):
        for x in range(width):
            pos = (x, y)
            gray = img.getpixel(pos)
            index = int(gray/256*70)
            txt += ASCII_HIHG[index] + ' '
        txt += '\n'

    img_new = Image.new("RGB", (width*12, height*15), 'white')
    draw = ImageDraw.Draw(img_new)
    draw.text((0, 0), txt, fill='black')

    return img_new.resize((width*12, width*12)).convert("RGBA")

if __name__ =="__main__":
    img = Image.open("bcm.jpg")
    to_char(img).save("bcm_char.png")
