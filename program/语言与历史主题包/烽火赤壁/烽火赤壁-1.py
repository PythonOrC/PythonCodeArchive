from pyecharts import GeoLines, Style
import webbrowser
import os
import json

with open('site.json','r', encoding='utf-8-sig') as f:
    coords = json.load(f)
print(coords)

style=Style(
    width=1820,
    height=880,
    background_color='#ffffff',
    title_color='red',
    title_pos='center',
    
)
style_geo = style.add(
    geo_cities_coords=coords,
    geo_normal_color='#c7d9f1',
    geo_emphasis_color='#ddbd74',
    border_color='#ffffff',
    legend_text_color=['#bb4f8c','#5d3ab6','#2d2f71'],
    legend_pos='right',
    label_color=['#bb4f8c','#5d3ab6','#2d2f71'],
    label_pos='right',
    label_formatter='{b}: {a}',
    label_text_color=['#bb4f8c', '#5d3ab6', '#2d2f71'],
    is_label_show=True,
    line_curve=0.2,
    geo_effect_symbol='arrow',
    geo_effect_symbolsize=13,
    geo_effect_traillength=0.8,
    geo_effect_color=['#bb4f8c', '#5d3ab6', '#2d2f71'],
)

caojun_assult = [['新野', '襄阳'], ['襄阳', '长坂坡'], ['长坂坡', '江陵'], ['江陵', '乌林']]
liujun_assult = [['樊口', '赤壁战场']]
sunjun_assult = [['柴桑', '樊口'], ['樊口', '赤壁战场']]

geolines = GeoLines('赤壁之战',** style.init_style)
geolines.add('曹军进攻路线', caojun_assult, ** style_geo)
geolines.add('刘军进攻路线', liujun_assult, ** style_geo)
geolines.add('孙军进攻路线', sunjun_assult, ** style_geo)
geolines.render()
webbrowser.open('file://'+os.path.realpath('render.html'))
