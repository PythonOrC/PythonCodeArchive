from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak, Spacer
from reportlab.platypus.xpreformatted import PythonPreformatted
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import webbrowser
import os
import glob


pdfmetrics.registerFont(TTFont('fangzheng', 'fangzheng.TTF'))
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Code_cn', parent=styles['Code'], fontName='fangzheng'))
styles.add(ParagraphStyle(name='Normal_cn', parent=styles['Normal'], fontName='fangzheng', fontSize=12))

doc = SimpleDocTemplate('源码手账.pdf', title='源码手账', author='阿短', subject='展现代码', keywords=[
                        'Python', '代码', 'Canvas', 'Reportlab', '展现'])
content = []


py_list = glob.glob('E:\Personal\Python\program\Reportlab\**\*.py')
self_name = os.path.realpath(os.path.basename(__file__))
print(py_list)
py_list.remove(self_name)

for name in py_list:
    with open(name, 'r', encoding='utf-8') as f:
        code = f.read()

    content.append(Paragraph(name, styles['Normal_cn']))
    content.append(Spacer(20, 20))
    content.append(PythonPreformatted(code, styles['Code_cn']))
    content.append(PageBreak())

doc.build(content)
webbrowser.open('file://'+os.path.realpath("源码手账.pdf"))
