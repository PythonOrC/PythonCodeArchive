from PIL import Image

pic = Image.open('熊.png').convert('RGBA')
bg = Image.open('天空.png').convert('RGBA')
width, height = pic.size
bg = bg.resize((width, height))
for y in range(height):
    for x in range(width):
        RGB_value = pic.getpixel((x, y))
        if (sum(RGB_value))/4 > 220:
            pic.putpixel((x, y), (255, 255, 255, 0))
bg.paste(pic, (0,0), pic)
bg.show()
