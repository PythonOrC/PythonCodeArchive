from pyecharts import GeoLines, Style
import webbrowser
import json
import os

with open("site.json", "r", encoding="utf-8-sig") as f:
    coords = json.load(f)
print(coords)
style = Style(
    width=1200,          # 界面宽度
    height=600,          # 界面高度
    title_pos="center",  # 标题位置
    title_color="red",           # 标题颜色
    background_color="#ffffff",  # 背景颜色
)
style_geo = style.add(

    geo_cities_coords=coords,       # 用户自定义地区经纬度


    geo_normal_color="#c7d9f1",     # 正常地图区域颜色
    geo_emphasis_color="#ddbd74",   # 高亮地图颜色
    border_color="#ffffff",         # 地图边界颜色

    legend_text_color=['#bb4f8c', '#5d3ab6', '#2d2f71'],  # 说明文本颜色
    legend_pos="right",                                   # 说明位置

    geo_effect_symbol='arrow',     # 特效图形的标记
    geo_effect_symbolsize=13,      # 特效标记的大小
    geo_effect_traillength=0.8,    # 特效尾迹的长度
    geo_effect_color=['#bb4f8c', '#5d3ab6', '#2d2f71'],    # 特效标记的颜色


    label_color=['#bb4f8c', '#5d3ab6', '#2d2f71'],          # 标签的颜色
    label_pos="right",                                      # 标签的位置
    #label_formatter="{b}：{a}",                            # 标签格式
    label_text_color=['#bb4f8c', '#5d3ab6', '#2d2f71'],     # 标签字体颜色
    is_label_show=True,                                     # 是否显示标签
    line_curve=0.2,                                         # 路线弧度


)
#曹军进攻路线数据
caojun_assault = [
    ["新野", "襄阳"],
    ["襄阳", "当阳"],
    ["当阳", "江陵"],
    ["江陵", "乌林"],
]
#刘备军进攻路线数据
liujun_assault = [
    ["樊口", "赤壁战场"]
]
#孙权军进攻路线数据
sunjun_assault = [
    ["柴桑", "樊口"],
    ["樊口", "赤壁战场"]
]
#创建地理坐标系线图
geolines = GeoLines("赤壁之战", ** style.init_style)
#添加数据
geolines.add(
    "曹军进军方向",
    caojun_assault,
    label_formatter="{b}：{a}",                            # 标签格式
    #geo_effect_color="#12abd1",       # 特效标记的颜色
    ** style_geo
)


geolines.add(
    "孙刘联军进军方向",
    liujun_assault,
    label_formatter="{b}：{a}",                            # 标签格式
    #geo_effect_color="#ffa022",
    **style_geo,
)

geolines.add(
    "孙军进军方向",
    sunjun_assault,
    label_formatter="{b}",                                 # 标签格式
    #geo_effect_color="#f26c2a",
    **style_geo
)
geolines.render()
webbrowser.open("file://"+os.path.realpath("render.html"))
