from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import webbrowser
import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('fangzheng', 'fangzheng.TTF'))

doc = SimpleDocTemplate('源码表格.pdf')
content = []
data = [['中', '文'], ['字', '体']]
t = Table(data, colWidths=100, rowHeights=100)
t.setStyle(TableStyle([
    ('TEXTCOLOR', (0, 0), (1, 1), colors.red), 
    ('TEXTCOLOR', (0, 0), (0, 0), colors.blue),
    ('TEXTCOLOR', (1, 1), (1, 1), colors.blue),
    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('FONTNAME', (0, 0), (-1, -1), 'fangzheng'),
    ('FONTSIZE', (0, 0), (-1, -1), 20)
]))

content.append(t)
doc.build(content)
webbrowser.open('file://'+os.path.realpath('源码表格.pdf'))
