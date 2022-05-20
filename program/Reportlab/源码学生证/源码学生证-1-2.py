from reportlab.pdfgen import canvas
import webbrowser
import os
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.barcode import qr
from reportlab.graphics import renderPDF
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont

def createQrCode(canvas, x, y):
    with open('aduan.txt', 'r', encoding='utf-8-sig') as document:
        content = document.read()
    Qr_code = qr.QrCodeWidget(content, barBorder=2, barWidth=113, barHeight=113)
    drawing = Drawing(50, 50)
    drawing.add(Qr_code)
    renderPDF.draw(drawing, canvas, x, y)


c = canvas.Canvas('学生证.pdf')
c.scale(0.5, 0.5)
c.drawImage('1.png', 0, 0, width=372, height=665, mask=None)
c.drawImage('2.png', 150, 420, width = 87, height = 95, mask = 'auto')
c.roundRect(145, 415, 97, 105, 6, stroke = 1, fill = 0)

registerFont(TTFont('fangzheng','fangzheng.TTF'))

c.setFont('fangzheng',35)
c.drawString(95, 550, '学    生    证')

c.setFont('fangzheng', 20)
c.drawString(105, 370, '姓   名：阿          短')
c.drawString(105, 330, '班   级：六 年 一 班')
c.drawString(105, 290, '学   号:   1 0 0 0 1')
c.drawString(105, 250, '性   别:      男')

c.drawString(200, 95, '想了解更多信息')
c.drawString(200, 65, '请扫一扫')

createQrCode(c, 51, 28)
c.showPage()
c.save()
webbrowser.open('file://'+os.path.realpath("学生证.pdf"))
