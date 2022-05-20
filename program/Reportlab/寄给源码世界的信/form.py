from reportlab.pdfgen import canvas
import webbrowser
import os
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('fangzheng', 'fangzheng.TTF'))

c = canvas.Canvas('form.pdf')
c.setFont('fangzheng', 15)
c.drawString(298, 800, '寄往源码世界的信')
form = c.acroForm
c.drawCentredString(200, 700, '昵称')
form.textfield(x=300, y=680, fillColor=colors.white)
c.drawCentredString(200, 600, '性别')
c.drawCentredString(300, 600, '男')
form.checkbox(x=320, y=595, buttonStyle='check')
c.drawCentredString(400, 600, '女')
form.checkbox(x=420, y=595, buttonStyle='check')
c.drawCentredString(200, 500, '年龄')
form.choice(x=300, y=480, value='6', options=[str(i) for i in range(6, 19)])
c.drawCentredString(200, 400, '寄语')
form.textfield(x=300, y=220, width=230, height=200, fillColor=colors.white)

c.save()
webbrowser.open('file://'+os.path.realpath('form.pdf'))
