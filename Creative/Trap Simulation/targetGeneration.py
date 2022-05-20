from PIL import Image
image = Image.open('target.gif')
width, height = image.size
FACTOR = 100
for i in range(101):
    image = image.resize((round((width*FACTOR)/(FACTOR+i))+1, round((height * FACTOR)/(FACTOR+i))+1))
    image.save(f'image/{i}.gif')