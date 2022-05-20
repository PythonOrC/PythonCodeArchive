from path import Map


map = Map()  # 生成地图对象
map.map_init()  # 初始化地图
map.show_route(["A", "B", "F"])

map.finish()  # 完成绘制并保留画布
meiyancuowu = input("请输入你的路径：")
