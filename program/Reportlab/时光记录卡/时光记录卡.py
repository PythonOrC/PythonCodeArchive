from reportlab.pdfgen import canvas
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Drawing
from reportlab.lib.colors import red, yellow, green, blue, orange, purple
from reportlab.graphics.charts.legends import Legend
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont
import webbrowser
import os

plan = ['睡觉', '上课', '写作业', '兴趣班', '吃饭']
data = [9, 8, 2, 2, 2, 1]

c = canvas.Canvas('文件名.pdf')
c.scale(0.5, 0.5)
c.drawImage('card.png', 0, 0, width=372, height=665, mask=None)
registerFont(TTFont('fangzheng', 'fangzheng.TTF'))
drawing = Drawing(372, 665)

pc = Pie()
pc.x = 115
pc.y = 350
pc.height = 150
pc.width = 150
pc.data = data
pc.labels = [str(i) for i in data]
pc.sideLabels = 1

colors = [red, orange, yellow, green, blue, purple]
count = 0
for i in colors:
    pc.slices[count].fillColor = i
    count += 1

pc.slices.popout = 5

legend = Legend()
legend.x = 133
legend.y = 260
legend.colorNamePairs = list(zip(colors, plan))
legend.fontName = 'fangzheng'
legend.alignment = 'right'

drawing.add(pc)
drawing.add(legend)
renderPDF.draw(drawing, c, 0, 0)

c.setFont('fangzheng', 16)
c.drawString(145, 300, '我的时光记录')

c.save()
webbrowser.open('file://'+os.path.realpath("文件名.pdf"))
