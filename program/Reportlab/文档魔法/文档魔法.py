import webbrowser
import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('fangzheng', 'fangzheng.TTF'))

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='cn', fontName='fangzheng'))

doc = SimpleDocTemplate('doc.pdf')
content = []
for i in range(100):
    p = Paragraph('句子一。句子二', styles['cn'])
    content.append(p)
    content.append(Spacer(20, 20))


def myOnFirstPage(canvas, doc):
    canvas.setFont('fangzheng', 10)
    canvas.drawCentredString(298, 30, '首页')


def myOnLaterPages(canvas, doc):
    canvas.setFont('fangzheng', 10)
    canvas.drawCentredString(298, 30, '第{}页'.format(doc.page))



doc.build(content, myOnFirstPage, myOnLaterPages)
webbrowser.open('file://'+os.path.realpath('doc.pdf'))
