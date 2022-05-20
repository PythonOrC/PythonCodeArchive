import matplotlib.pyplot as plt
from matplotlib import rcParams

temp_list = [-2, 0, 4, 10, 19, 28]
print(temp_list)
month_list = ['{}月'.format(i) for i in range(1, 7)]
print(month_list)

def style():
    rcParams['font.sans-serif'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False
    plt.ylim(-10, 33)
    plt.xticks([0,1,2,3,4,5], month_list)
    plt.yticks([i for i in range(-10, 34, 2)])
    plt.axhline(color='#add8e6',zorder=0)
    for i in range(len(month_list)):
        if temp_list[i] >= 0:
            plt.text(i, temp_list[i]+0.5, str(temp_list[i]), ha='center',va='bottom')
        else:
            plt.text(i, temp_list[i]-0.5, str(temp_list[i]), ha='center',va='top')

plt.subplot(131)
plt.bar(month_list, temp_list)
style()

plt.subplot(132)
plt.plot(month_list, temp_list)
style()

plt.subplot(133)
plt.scatter(month_list, temp_list)
style()

plt.suptitle('每月天气变化')
plt.show()

