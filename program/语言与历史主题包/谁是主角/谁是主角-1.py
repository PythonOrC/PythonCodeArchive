import codecs
import jieba
import matplotlib.pyplot as plt
from matplotlib import rcParams

line_list = []
with codecs.open('西游记.txt', 'r', encoding='utf-8-sig') as f:
    for line in f.readlines():
        line_list.extend(jieba.lcut(line.strip()))


with codecs.open('西游记人物.txt', 'r', encoding='utf-8-sig') as f:
    names_list = [name.strip() for name in f.readlines()]

showup_list = []
cnt = 0
for name in names_list:
    for word in line_list:
        if word == name:
            cnt +=1
    showup_list.append([cnt, name])
    cnt = 0

showup_list.sort(reverse=True)
print(showup_list)

x_axis = [i[1] for i in showup_list]
y_axis = [i[0] for i in showup_list]

plt.bar(range(len(x_axis)), y_axis, tick_label=x_axis)
rcParams['font.sans-serif'] = 'SimHei'
plt.xlabel('出现的人物')
plt.ylabel('出现的次数')
plt.title('西游记人物出现柱状图')
plt.show()
