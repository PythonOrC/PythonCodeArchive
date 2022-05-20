import json
import webbrowser
from pyecharts import Bar, Line, Pie

def plot(data_file,type):
    with open(data_file) as f:
        data = json.load(f)

    attr = data['attr']
    value = data['value']

    if type == '柱状图':
        chart = Bar('柱状图数据')
    elif type == '折线图':
        chart = Line('折线图数据')
    elif type == '饼状图':
        chart = Pie('饼状图数据')

    chart.add(type, attr, value)
    chart.render()

if __name__ == '__main__':
    plot(data_file = 'data.json',type = '折线图')