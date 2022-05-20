import turtle
import time

class Map():
    def __init__(self):
        self.t = turtle
        self.p = turtle.Pen()  # 生成画笔
        #结点以及对应的坐标值（新增了F）
        self.pos_dict = {'A': (0, 0), 'B': (100, 100), 'C': (100, -100),
                         'D': (200, 100), 'E': (200, -100),'F': (300,0) }
        self.edge = {("A","B"), ("A","C"),("B","D"), ("B","C"),("C","E"),("D","E"),("D","F")}

    # 画线函数
    def draw_line(self, point1, pint2, color='black'):
        # 画从点1到点2的线段
        self.p.penup()
        self.p.pencolor(color)  # 默认为黑色，后面选完路线的换一种颜色
        self.p.goto(point1)
        self.p.pendown()
        self.p.dot(15, 'blue')  # 打点，打粗一点
        self.p.goto(pint2)
        self.p.dot(15, 'blue')  # 打点，打粗一点

    # 写标注函数
    def write_label(self,point, label):
        self.p.penup()
        self.p.goto(point)
        self.p.write(label, font=('Arial', 20))

    # 初始化函数，把相关的点连起来
    def map_init(self):
        self.draw_line(self.pos_dict['A'], self.pos_dict['B'])
        self.draw_line(self.pos_dict['B'], self.pos_dict['D'])
        self.draw_line(self.pos_dict['D'], self.pos_dict['E'])
        self.draw_line(self.pos_dict['D'], self.pos_dict['C'])
        self.draw_line(self.pos_dict['C'], self.pos_dict['E'])
        self.draw_line(self.pos_dict['B'], self.pos_dict['C'])
        self.draw_line(self.pos_dict['A'], self.pos_dict['C'])
        #这里再补充一条
        self.draw_line(self.pos_dict['D'], self.pos_dict['F'])
        # 从字典循环取出标签名和对应的坐标
        for label, point in self.pos_dict.items():
            self.write_label(point, label)

    # 根据用户传入的点列表，连接成线
    def show_route(self,point_list):
        # 从列表中取出连续的两项，因此这里的索引值取到倒数第二项
        for i in range(len(point_list)-1):
            self.p.speed(1)  # 这次画慢一点
            a = (point_list[i],point_list[i+1])
            b = (point_list[i+1],point_list[i])
            if a in self.edge or b in self.edge:
                self.draw_line(self.pos_dict[point_list[i]], self.pos_dict[point_list[i+1]],
                               color='red')
                time.sleep(1)  # 等待1s
            else:
                print(a, "关系路径不存在,请停止程序，并重新输入正确路径")
                break
    # 保留画布
    def finish(self):
        self.t.done()
#
# #内部测试代码
# a = Map()
# a.map_init()
# a.finish()
