from reportlab.pdfgen import canvas
import webbrowser
import os
from PIL import Image

from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont
registerFont(TTFont('fangzheng', 'fangzheng.ttf'))

c = canvas.Canvas('源码奖状.pdf')

c.setFont('fangzheng', 40)
c.drawCentredString(298, 600, '课程证书')

c.drawImage('1.png', 0, 0, mask="auto", width=595.27, height=841.89)

img2 = Image.open('2.png')
img2.close()
c.drawImage('2.png', 298 - img2.width/8, 500, mask="auto", width=img2.width/4, height=img2.height/4)

img3 = Image.open('3.png')
img3.close()
c.drawImage('3.png', 298 - img3.width/8, 700, mask="auto", width=img3.width/4, height=img3.height/4)

img4 = Image.open('4.png')
img4.close()
c.drawImage('4.png', 298 - img4.width/8, 100, mask="auto", width=img4.width/4, height=img4.height/4)

c.setFontSize(20)
c.drawCentredString(298,400,'兹证明')

c.setFontSize(30)
c.drawCentredString(298,350,'我')

c.setFontSize(20)
c.drawCentredString(298,300,'完成了《源码奖状》课程')

c.save()
webbrowser.open('file://'+os.path.realpath("源码奖状.pdf"))
