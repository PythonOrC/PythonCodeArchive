from pyecharts import Map
import webbrowser
import os
import csv
import turtle

screen = turtle.Screen()
'''
data = []
with open('三国数据.csv', 'r') as fp:
    reader = csv.reader(fp)
    titles = next(reader)
    for x in reader:
        data.append(tuple(x))
print(titles)
print(data)

attr, value = Map.cast(data)
map = Map('三国鼎立', width=800, height=600)
map.add('三国势力分布图',
        attr, value,
        maptype='china',
        is_visualmap=True,
        visual_range=[1, 15],
        pieces=[
            {'max': 16, "min": 14, "label": '魏'},
            {'max': 13, 'min': 9, 'label': '蜀'},
            {'max': 10, 'min': 9, 'label': '吴'}
        ],
        is_piecewise=True,
        visual_range_text=['','']
    )
map.render()
webbrowser.open('file://'+os.path.realpath('render.html'))
'''
screen.setup(1000,750)
screen.bgpic('三国鼎立.png')
turtle.done()