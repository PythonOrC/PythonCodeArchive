from reportlab.pdfgen import canvas
import webbrowser
import os
from PIL import Image


def imgtopdf(filename):
    img = Image.open(filename+'.png')
    pix = img.load()

    minX = 10000
    maxX = 0
    y = 0

    for x in range(0, img.width):
        if pix[x, y][3] != 0:
            if minX > x:
                minX = x
            if maxX < x:
                maxX = x

    width = maxX - minX
    img = img.crop((minX, 0, maxX, img.height))
    img.save(filename+'_裁剪.png')
    img.close()

    c = canvas.Canvas('test.pdf', pagesize=(width, img.height))
    c.drawImage(filename+'_裁剪.png', 0, 0, mask='auto')
    c.save()
    webbrowser.open('file://'+os.path.realpath('test.pdf'))

filename = '讲义'
imgtopdf(filename)