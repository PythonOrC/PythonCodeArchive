from reportlab.pdfgen import canvas
import webbrowser
import os
import json

with open('task.txt', 'r') as f:
    task = json.load(f)

c = canvas.Canvas('todolist.pdf')
c.setLineWidth(3)
c.line(0, 421, 595, 421)
c.line(298, 0, 298, 841)

c.drawCentredString(446, 841 - 30, 'Do')
c.drawCentredString(149, 841 - 30, 'Plan')
c.drawCentredString(149, 421 - 30, 'Delegate')
c.drawCentredString(446, 421 - 30, 'Eliminate')

for i in task:
    if i == 'Do':
        for j in range(len(task[i])):
            c.drawCentredString(446, 841 - 30 - 40*(j+1), task[i][j])
    if i == 'Plan':
        for j in range(len(task[i])):
            c.drawCentredString(149, 841 - 30 - 40*(j+1), task[i][j])
    if i == 'Delegate':
        for j in range(len(task[i])):
            c.drawCentredString(149, 421 - 30 - 40*(j+1), task[i][j])
    if i == 'Eliminate':
        for j in range(len(task[i])):
            c.drawCentredString(446, 421 - 30 - 40*(j+1), task[i][j])

c.save()
webbrowser.open('file://'+os.path.realpath('todolist.pdf'))
