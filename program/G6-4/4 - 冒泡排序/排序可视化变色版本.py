# 排序可视化
import matplotlib.pyplot as plt
import random

plt.ion()  # 打开交互模式

# 冒泡排序函数， 参数data的值为列表
def bubble_sort(data):
    n = len(data)  # 返回列表长度
    for i in range(n - 1):
        for j in range(n - 1 - i):
            show_list(data, j, 1, i)  # 展示交换前
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                print(data)  # 每次有交换就打印一下
                show_list(data, j, 0, i)  # 展示交换后

    return data


# 将传入的列表以柱状图形式进行展现, data为列表， m为正在对比的数字， n 为布尔值： n = 0 红色， n = 1 绿色， l为已经排好序的数字
def show_list(data, m=-1, n=0, l=0):
    plt.cla()  # 先清屏
    tempbar = plt.bar(range(len(data)), data)  # 用一个变量来接受这个柱子对象
    # 如果有索引值，就把要调换的柱子标红
    if m != -1 and n == 0:
        tempbar[m].set_fc("red")
        tempbar[m + 1].set_fc("red")

    else:
        tempbar[m].set_fc("green")
        tempbar[m + 1].set_fc("green")

    for i in range(len(data) - 1, len(data) - 1 - l, -1):
        tempbar[i].set_fc("orange")

    # 给每个柱子加上标注
    for i in range(len(data)):
        plt.text(i, data[i], str(data[i]), ha="center", va="bottom")
    plt.xticks([])  # 传入个空列表，变向关闭x轴上的标注
    plt.ylim(0, 11)  # 把y轴标签范围设置大一点点，更加美观
    plt.pause(0.5)  # 暂停1秒


data = [random.randint(1, 10) for i in range(10)]  # 生成1~10的随机正整数列表，共10个数
print(data)  # 打印排序前的列表，不用传入索引值
# show_list(data) # 展示下初始情况
bubble_sort(data)
print(data)  # 打印排序后的列表

show_list(data, l=10)  # 展示最终排好的柱子，去掉红色（不传入索引值）

plt.ioff()
plt.show()
