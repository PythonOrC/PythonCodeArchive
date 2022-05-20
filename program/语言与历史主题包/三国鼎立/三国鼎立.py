from pyecharts import Map
import webbrowser
import os

data = [('四川', 12), ('重庆', 12), ('云南', 12)]

attr, value = Map.cast(data)
print(attr, value)
map = Map('例子', width=800, height=600)
map.add('四川', 
        attr, value, 
        maptype='china', 
        is_visualmap=True, 
        visual_range=[1, 15])
map.render()
webbrowser.open('file://'+os.path.realpath('render.html'))
