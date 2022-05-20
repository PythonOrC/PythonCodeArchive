from reportlab.pdfgen import canvas
import webbrowser
import os
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont
registerFont(TTFont('fangzheng','fangzheng.TTF'))
c = canvas.Canvas('hello.pdf', pagesize=(500,500))
c.setFont('fangzheng',15)
c.drawString(250,250, "第一页")
c.showPage()
c.setFont('fangzheng', 20)
c.drawString(250, 250, "第二页")
c.save()
webbrowser.open('file://'+os.path.realpath('hello.pdf'))
