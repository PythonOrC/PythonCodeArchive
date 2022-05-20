import json
import matplotlib.pyplot as plt
from matplotlib import rcParams

with open('全球温度.json', 'r', encoding='utf-8')as f:
    climate_data = json.load(f)
processed_data = {}
for item in climate_data:
    processed_data[int(''.join(item['日期'].split('-')[:2]))] = item['平均温度']

x1_data = []
y1_data = []
x2_data = []
y2_data = []
cnt = 0
temp = 0
for i in range(180001, 201601):
    if processed_data.get(i) is not None and processed_data.get(i) != '':
        x1_data.append(i)
        y1_data.append(processed_data.get(i))
        cnt += 1
        temp+= processed_data.get(i)
        if cnt >=12:
            x2_data.append(i//100)
            y2_data.append(temp/cnt) 
            cnt = 0
            temp = 0
#print(x_data)
#print(y_data)

def Style():
    rcParams['font.sans-serif'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False



plt.ion()

index1_list = range(len(x1_data))
index2_list = range(len(x2_data))

'''
for i in index1_list:
    plt.subplot(121)
    plt.clf()
    plt.plot(index1_list[:i+1], y1_data[:i+1])
    Style()
    plt.pause(0.005)
plt.ioff()
plt.show()
'''
for i in index2_list:
    plt.subplot(122)
    plt.clf()
    plt.plot(index2_list[:i+1], y2_data[:i+1])
    Style()
    plt.pause(0.005)
plt.ioff()
print(index1_list)
print(index2_list)
plt.show()
